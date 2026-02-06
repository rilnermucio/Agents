#!/usr/bin/env python3
"""
Readability Checker - Analisa legibilidade de textos

Métricas:
- Flesch Reading Ease (adaptado para português)
- Tempo de leitura estimado
- Complexidade de vocabulário
- Estrutura de sentenças

Uso:
    python readability_checker.py "Seu texto aqui"
    python readability_checker.py --file artigo.txt
    python readability_checker.py --url https://exemplo.com/artigo
"""

import re
import sys
import argparse
from typing import Dict, List, Tuple
from collections import Counter

# Conectivos e palavras de transição (bom sinal)
TRANSITION_WORDS = [
    "portanto", "porém", "contudo", "entretanto", "todavia",
    "além disso", "ademais", "por outro lado", "em contrapartida",
    "por exemplo", "ou seja", "isto é", "em outras palavras",
    "em resumo", "em suma", "finalmente", "primeiramente",
    "em seguida", "posteriormente", "consequentemente",
    "assim", "dessa forma", "desse modo", "sendo assim"
]

# Palavras difíceis comuns que podem ser simplificadas
COMPLEX_WORDS = {
    "utilizar": "usar",
    "realizar": "fazer",
    "efetuar": "fazer",
    "implementar": "criar/fazer",
    "otimizar": "melhorar",
    "potencializar": "aumentar",
    "viabilizar": "permitir",
    "disponibilizar": "oferecer",
    "priorizar": "dar prioridade",
    "customizar": "personalizar"
}

# Jargões a evitar
JARGON_WORDS = [
    "sinergia", "paradigma", "disruptivo", "escalável",
    "holístico", "proativo", "stakeholder", "mindset",
    "benchmark", "brainstorm", "deadline", "feedback",
    "insight", "expertise", "networking", "approach"
]


def count_syllables_pt(word: str) -> int:
    """Conta sílabas em português (aproximação)."""
    word = word.lower()
    vowels = "aeiouáéíóúâêôãõ"
    count = 0
    prev_was_vowel = False

    for char in word:
        is_vowel = char in vowels
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    # Ajustes para ditongos e hiatos comuns
    # Ditongos decrescentes (contam como 1 sílaba)
    ditongos = ["ai", "ei", "oi", "ui", "au", "eu", "ou", "iu"]
    for d in ditongos:
        if d in word:
            count -= word.count(d)
            count += word.count(d)  # Mantém contagem

    return max(1, count)


def get_sentences(text: str) -> List[str]:
    """Divide texto em sentenças."""
    # Divide por pontuação final
    sentences = re.split(r'[.!?]+', text)
    # Remove vazios e limpa espaços
    return [s.strip() for s in sentences if s.strip()]


def get_words(text: str) -> List[str]:
    """Extrai palavras do texto."""
    # Remove pontuação e divide
    words = re.findall(r'\b[a-záéíóúâêôãõç]+\b', text.lower())
    return words


def calculate_flesch_pt(text: str) -> Tuple[float, str]:
    """
    Calcula Flesch Reading Ease adaptado para português.
    Fórmula: 248.835 - (1.015 × ASL) - (84.6 × ASW)
    ASL = Average Sentence Length
    ASW = Average Syllables per Word
    """
    sentences = get_sentences(text)
    words = get_words(text)

    if not sentences or not words:
        return 0, "Texto muito curto"

    # Média de palavras por sentença
    asl = len(words) / len(sentences)

    # Média de sílabas por palavra
    total_syllables = sum(count_syllables_pt(w) for w in words)
    asw = total_syllables / len(words)

    # Fórmula Flesch adaptada para português
    score = 248.835 - (1.015 * asl) - (84.6 * asw)
    score = max(0, min(100, score))

    # Interpretação
    if score >= 80:
        level = "Muito fácil (5º ano)"
    elif score >= 70:
        level = "Fácil (6º-7º ano)"
    elif score >= 60:
        level = "Moderado (8º-9º ano)"
    elif score >= 50:
        level = "Médio (Ensino Médio)"
    elif score >= 30:
        level = "Difícil (Superior)"
    else:
        level = "Muito difícil (Acadêmico)"

    return round(score, 1), level


def calculate_reading_time(text: str) -> Dict:
    """Calcula tempo de leitura estimado."""
    words = get_words(text)
    word_count = len(words)

    # Velocidades médias de leitura
    speeds = {
        "leitura_rapida": 300,  # palavras por minuto
        "leitura_normal": 200,
        "leitura_atenta": 150
    }

    times = {}
    for speed_name, wpm in speeds.items():
        minutes = word_count / wpm
        if minutes < 1:
            times[speed_name] = f"{int(minutes * 60)} segundos"
        else:
            times[speed_name] = f"{round(minutes, 1)} minutos"

    return {
        "word_count": word_count,
        "times": times
    }


def analyze_sentences(text: str) -> Dict:
    """Analisa estrutura das sentenças."""
    sentences = get_sentences(text)

    if not sentences:
        return {"error": "Sem sentenças para analisar"}

    lengths = [len(get_words(s)) for s in sentences]

    analysis = {
        "total_sentences": len(sentences),
        "avg_length": round(sum(lengths) / len(lengths), 1),
        "shortest": min(lengths),
        "longest": max(lengths),
        "very_long": sum(1 for l in lengths if l > 25),  # Sentenças muito longas
        "very_short": sum(1 for l in lengths if l < 5),  # Sentenças muito curtas
    }

    # Variação (bom ter mix)
    if len(lengths) > 1:
        import statistics
        analysis["std_dev"] = round(statistics.stdev(lengths), 1)
        if analysis["std_dev"] > 5:
            analysis["variation"] = "✅ Boa variação"
        else:
            analysis["variation"] = "⚠️ Pouca variação"
    else:
        analysis["variation"] = "N/A"

    return analysis


def find_transition_words(text: str) -> List[str]:
    """Encontra palavras de transição."""
    text_lower = text.lower()
    found = []

    for word in TRANSITION_WORDS:
        if word in text_lower:
            found.append(word)

    return found


def find_complex_words(text: str) -> List[Tuple[str, str]]:
    """Encontra palavras complexas e sugere alternativas."""
    text_lower = text.lower()
    found = []

    for complex_word, simple in COMPLEX_WORDS.items():
        if complex_word in text_lower:
            found.append((complex_word, simple))

    return found


def find_jargon(text: str) -> List[str]:
    """Encontra jargões no texto."""
    text_lower = text.lower()
    return [j for j in JARGON_WORDS if j in text_lower]


def analyze_paragraphs(text: str) -> Dict:
    """Analisa estrutura de parágrafos."""
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

    if not paragraphs:
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]

    if not paragraphs:
        return {"error": "Sem parágrafos"}

    lengths = [len(get_words(p)) for p in paragraphs]

    return {
        "total": len(paragraphs),
        "avg_words": round(sum(lengths) / len(lengths), 1),
        "ideal_range": "50-150 palavras por parágrafo",
        "too_long": sum(1 for l in lengths if l > 150),
        "too_short": sum(1 for l in lengths if l < 20)
    }


def get_vocabulary_stats(text: str) -> Dict:
    """Estatísticas de vocabulário."""
    words = get_words(text)

    if not words:
        return {"error": "Sem palavras"}

    word_freq = Counter(words)
    unique_words = len(word_freq)

    # Lexical diversity (type-token ratio)
    ttr = unique_words / len(words)

    # Palavras longas (4+ sílabas)
    long_words = [w for w in words if count_syllables_pt(w) >= 4]

    return {
        "total_words": len(words),
        "unique_words": unique_words,
        "lexical_diversity": round(ttr, 3),
        "long_words_count": len(long_words),
        "long_words_percent": round(len(long_words) / len(words) * 100, 1),
        "most_common": word_freq.most_common(10)
    }


def full_analysis(text: str) -> Dict:
    """Análise completa de legibilidade."""
    results = {
        "text_preview": text[:200] + "..." if len(text) > 200 else text
    }

    # Flesch
    flesch_score, flesch_level = calculate_flesch_pt(text)
    results["flesch"] = {
        "score": flesch_score,
        "level": flesch_level
    }

    # Tempo de leitura
    results["reading_time"] = calculate_reading_time(text)

    # Sentenças
    results["sentences"] = analyze_sentences(text)

    # Parágrafos
    results["paragraphs"] = analyze_paragraphs(text)

    # Vocabulário
    results["vocabulary"] = get_vocabulary_stats(text)

    # Transições
    results["transitions"] = find_transition_words(text)

    # Palavras complexas
    results["complex_words"] = find_complex_words(text)

    # Jargões
    results["jargon"] = find_jargon(text)

    # Score geral (0-100)
    score = flesch_score * 0.4  # 40% flesch

    # Bonus por transições
    if results["transitions"]:
        score += min(10, len(results["transitions"]) * 2)

    # Penalidade por sentenças longas
    if results["sentences"].get("very_long", 0) > 0:
        score -= results["sentences"]["very_long"] * 3

    # Penalidade por jargões
    score -= len(results["jargon"]) * 2

    results["overall_score"] = round(max(0, min(100, score)), 1)

    # Classificação
    if results["overall_score"] >= 70:
        results["classification"] = "✅ Excelente legibilidade"
    elif results["overall_score"] >= 50:
        results["classification"] = "👍 Boa legibilidade"
    elif results["overall_score"] >= 30:
        results["classification"] = "⚠️ Legibilidade média"
    else:
        results["classification"] = "❌ Difícil de ler"

    return results


def print_report(results: Dict):
    """Imprime relatório formatado."""
    print("\n" + "="*60)
    print("📖 ANÁLISE DE LEGIBILIDADE")
    print("="*60)

    print(f"\n🎯 SCORE GERAL: {results['overall_score']}/100")
    print(f"   {results['classification']}")

    print("\n" + "-"*60)
    print("📊 MÉTRICAS PRINCIPAIS")
    print("-"*60)

    # Flesch
    print(f"\n📈 Índice Flesch: {results['flesch']['score']}")
    print(f"   Nível: {results['flesch']['level']}")

    # Tempo de leitura
    rt = results['reading_time']
    print(f"\n⏱️ Tempo de Leitura ({rt['word_count']} palavras):")
    print(f"   • Leitura rápida: {rt['times']['leitura_rapida']}")
    print(f"   • Leitura normal: {rt['times']['leitura_normal']}")
    print(f"   • Leitura atenta: {rt['times']['leitura_atenta']}")

    # Sentenças
    sent = results['sentences']
    if "error" not in sent:
        print(f"\n📝 Sentenças ({sent['total_sentences']} total):")
        print(f"   • Média de palavras: {sent['avg_length']}")
        print(f"   • Mais curta: {sent['shortest']} | Mais longa: {sent['longest']}")
        if sent['very_long'] > 0:
            print(f"   ⚠️ {sent['very_long']} sentenças muito longas (>25 palavras)")
        print(f"   • Variação: {sent['variation']}")

    # Parágrafos
    para = results['paragraphs']
    if "error" not in para:
        print(f"\n📄 Parágrafos ({para['total']} total):")
        print(f"   • Média: {para['avg_words']} palavras")
        print(f"   • Ideal: {para['ideal_range']}")

    # Vocabulário
    vocab = results['vocabulary']
    if "error" not in vocab:
        print(f"\n📚 Vocabulário:")
        print(f"   • Palavras únicas: {vocab['unique_words']} de {vocab['total_words']}")
        print(f"   • Diversidade lexical: {vocab['lexical_diversity']}")
        print(f"   • Palavras longas (4+ sílabas): {vocab['long_words_percent']}%")

    print("\n" + "-"*60)
    print("💡 ANÁLISE QUALITATIVA")
    print("-"*60)

    # Transições
    if results['transitions']:
        print(f"\n✅ Conectivos encontrados ({len(results['transitions'])}):")
        print(f"   {', '.join(results['transitions'][:8])}")
    else:
        print("\n⚠️ Nenhum conectivo/palavra de transição encontrado")
        print("   Considere adicionar: portanto, além disso, por exemplo...")

    # Palavras complexas
    if results['complex_words']:
        print(f"\n⚠️ Palavras que podem ser simplificadas:")
        for complex_w, simple in results['complex_words'][:5]:
            print(f"   • '{complex_w}' → '{simple}'")

    # Jargões
    if results['jargon']:
        print(f"\n⚠️ Jargões encontrados:")
        print(f"   {', '.join(results['jargon'])}")
        print("   Considere explicar ou substituir por termos mais simples")

    print("\n" + "-"*60)
    print("📋 RECOMENDAÇÕES")
    print("-"*60)

    recommendations = []

    if results['flesch']['score'] < 50:
        recommendations.append("Simplifique o texto: use frases mais curtas e palavras mais simples")

    if sent.get('very_long', 0) > 2:
        recommendations.append("Quebre sentenças longas em duas ou mais")

    if not results['transitions']:
        recommendations.append("Adicione conectivos para melhorar a fluidez")

    if vocab.get('long_words_percent', 0) > 20:
        recommendations.append("Reduza o uso de palavras longas/técnicas")

    if results['jargon']:
        recommendations.append("Substitua jargões por termos mais acessíveis")

    if para.get('too_long', 0) > 0:
        recommendations.append("Divida parágrafos muito longos")

    if not recommendations:
        recommendations.append("Texto bem escrito! Mantenha o bom trabalho.")

    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec}")

    print("\n" + "="*60)


def main():
    parser = argparse.ArgumentParser(description="Analisa legibilidade de textos")
    parser.add_argument("text", nargs="*", help="Texto para analisar")
    parser.add_argument("--file", "-f", help="Arquivo de texto")

    args = parser.parse_args()

    text = ""

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif args.text:
        text = " ".join(args.text)
    else:
        print("Uso: python readability_checker.py \"Seu texto aqui\"")
        print("     python readability_checker.py --file artigo.txt")
        sys.exit(1)

    if len(text) < 50:
        print("❌ Texto muito curto para análise significativa (mínimo 50 caracteres)")
        sys.exit(1)

    results = full_analysis(text)
    print_report(results)


if __name__ == "__main__":
    main()
