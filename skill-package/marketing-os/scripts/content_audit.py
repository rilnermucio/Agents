#!/usr/bin/env python3
"""
Content Audit - Auditar conteúdo existente e sugerir melhorias
Analisa arquivos de conteúdo e fornece recomendações de otimização.

Uso:
    python content_audit.py arquivo.md [--tipo blog|social|email|landing]
    python content_audit.py --pasta ./conteudo [--formato json|markdown|tabela]
    python content_audit.py arquivo.md --completo

Exemplos:
    python content_audit.py artigo.md --tipo blog
    python content_audit.py post.txt --tipo social
    python content_audit.py --pasta ./posts --formato markdown
"""

import sys
import os
import re
import json
from datetime import datetime
from typing import Optional, List, Dict, Tuple
from collections import Counter
import math


# Palavras de poder para copywriting
PALAVRAS_PODER = {
    "urgencia": ["agora", "hoje", "imediato", "urgente", "última", "últimas", "limitado", "expira"],
    "exclusividade": ["exclusivo", "único", "especial", "vip", "premium", "selecionado"],
    "facilidade": ["fácil", "simples", "rápido", "prático", "sem esforço", "descomplicado"],
    "garantia": ["garantido", "garantia", "seguro", "comprovado", "testado", "certificado"],
    "novidade": ["novo", "lançamento", "inédito", "revolucionário", "inovador", "atualizado"],
    "gratuito": ["grátis", "gratuito", "free", "sem custo", "bônus", "brinde"],
    "resultados": ["resultado", "sucesso", "conquista", "transformação", "mudança", "melhoria"]
}

# Stop words em português
STOP_WORDS = {
    'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas', 'para', 'por', 'com',
    'que', 'o', 'a', 'os', 'as', 'um', 'uma', 'uns', 'umas', 'e', 'é', 'ou', 'se', 'mas',
    'como', 'mais', 'seu', 'sua', 'seus', 'suas', 'ele', 'ela', 'eles', 'elas', 'isso',
    'isto', 'esse', 'essa', 'este', 'esta', 'ao', 'aos', 'às', 'pelo', 'pela', 'pelos',
    'pelas', 'num', 'numa', 'nuns', 'numas', 'quando', 'onde', 'quem', 'qual', 'quais',
    'muito', 'muita', 'muitos', 'muitas', 'também', 'já', 'ainda', 'só', 'sobre', 'após',
    'até', 'entre', 'sem', 'sob', 'foi', 'ser', 'ter', 'está', 'são', 'tem', 'pode'
}


def ler_arquivo(caminho: str) -> Tuple[str, str]:
    """Lê arquivo e retorna conteúdo e extensão."""
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        _, ext = os.path.splitext(caminho)
        return conteudo, ext.lower()
    except FileNotFoundError:
        return None, None
    except Exception as e:
        return None, None


def contar_palavras(texto: str) -> int:
    """Conta palavras no texto."""
    palavras = re.findall(r'\b\w+\b', texto)
    return len(palavras)


def contar_caracteres(texto: str) -> Dict[str, int]:
    """Conta caracteres no texto."""
    return {
        "total": len(texto),
        "sem_espacos": len(texto.replace(" ", "").replace("\n", "")),
        "espacos": texto.count(" "),
        "linhas": texto.count("\n") + 1
    }


def calcular_tempo_leitura(palavras: int, wpm: int = 200) -> str:
    """Calcula tempo estimado de leitura."""
    minutos = palavras / wpm
    if minutos < 1:
        return "< 1 min"
    elif minutos < 2:
        return "1-2 min"
    else:
        return f"{int(minutos)} min"


def analisar_legibilidade(texto: str) -> Dict:
    """
    Analisa legibilidade do texto.
    Baseado em métricas adaptadas para português.
    """
    # Limpar texto
    texto_limpo = re.sub(r'[#*_\[\](){}]', '', texto)
    texto_limpo = re.sub(r'\n+', ' ', texto_limpo)

    # Contar elementos
    sentencas = re.split(r'[.!?]+', texto_limpo)
    sentencas = [s.strip() for s in sentencas if s.strip()]

    palavras = re.findall(r'\b\w+\b', texto_limpo.lower())

    # Contar sílabas (aproximação para português)
    def contar_silabas(palavra):
        vogais = 'aeiouáéíóúâêîôûãõ'
        count = 0
        anterior_vogal = False
        for char in palavra.lower():
            eh_vogal = char in vogais
            if eh_vogal and not anterior_vogal:
                count += 1
            anterior_vogal = eh_vogal
        return max(1, count)

    total_silabas = sum(contar_silabas(p) for p in palavras)

    # Métricas
    n_sentencas = max(1, len(sentencas))
    n_palavras = max(1, len(palavras))

    media_palavras_sentenca = n_palavras / n_sentencas
    media_silabas_palavra = total_silabas / n_palavras

    # Índice de Flesch adaptado para português
    # Quanto maior, mais fácil de ler (0-100)
    flesch = 206.835 - (1.015 * media_palavras_sentenca) - (84.6 * media_silabas_palavra)
    flesch = max(0, min(100, flesch))

    # Classificar legibilidade
    if flesch >= 80:
        nivel = "Muito fácil"
        publico = "Fundamental I"
    elif flesch >= 60:
        nivel = "Fácil"
        publico = "Fundamental II"
    elif flesch >= 40:
        nivel = "Moderado"
        publico = "Ensino Médio"
    elif flesch >= 20:
        nivel = "Difícil"
        publico = "Ensino Superior"
    else:
        nivel = "Muito difícil"
        publico = "Especialistas"

    return {
        "indice_flesch": round(flesch, 1),
        "nivel": nivel,
        "publico_alvo": publico,
        "media_palavras_por_sentenca": round(media_palavras_sentenca, 1),
        "media_silabas_por_palavra": round(media_silabas_palavra, 2),
        "total_sentencas": n_sentencas,
        "recomendacao": "Ideal: 15-20 palavras por sentença" if media_palavras_sentenca > 25 else "Bom comprimento de sentença"
    }


def analisar_estrutura_markdown(texto: str) -> Dict:
    """Analisa estrutura de documento Markdown."""
    estrutura = {
        "headings": {
            "h1": len(re.findall(r'^# ', texto, re.MULTILINE)),
            "h2": len(re.findall(r'^## ', texto, re.MULTILINE)),
            "h3": len(re.findall(r'^### ', texto, re.MULTILINE)),
            "h4": len(re.findall(r'^#### ', texto, re.MULTILINE))
        },
        "listas": {
            "nao_ordenadas": len(re.findall(r'^[-*+] ', texto, re.MULTILINE)),
            "ordenadas": len(re.findall(r'^\d+\. ', texto, re.MULTILINE))
        },
        "formatacao": {
            "negrito": len(re.findall(r'\*\*[^*]+\*\*', texto)),
            "italico": len(re.findall(r'(?<!\*)\*[^*]+\*(?!\*)', texto)),
            "codigo": len(re.findall(r'`[^`]+`', texto)),
            "blocos_codigo": len(re.findall(r'```', texto)) // 2
        },
        "links": len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', texto)),
        "imagens": len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', texto)),
        "citacoes": len(re.findall(r'^> ', texto, re.MULTILINE))
    }

    # Extrair headings
    headings_texto = re.findall(r'^(#{1,4})\s+(.+)$', texto, re.MULTILINE)
    estrutura["headings_lista"] = [
        {"nivel": len(h[0]), "texto": h[1][:50]}
        for h in headings_texto[:10]
    ]

    return estrutura


def analisar_seo(texto: str, titulo: Optional[str] = None, keyword: Optional[str] = None) -> Dict:
    """Analisa aspectos de SEO do conteúdo."""
    seo = {
        "pontuacao": 0,
        "max_pontuacao": 100,
        "itens": [],
        "sugestoes": []
    }

    texto_lower = texto.lower()
    n_palavras = contar_palavras(texto)

    # Verificar título
    if titulo:
        titulo_len = len(titulo)
        if 50 <= titulo_len <= 60:
            seo["itens"].append({"item": "Título com comprimento ideal (50-60 chars)", "ok": True})
            seo["pontuacao"] += 10
        else:
            seo["itens"].append({"item": f"Título com {titulo_len} chars (ideal: 50-60)", "ok": False})
            seo["sugestoes"].append("Ajustar título para 50-60 caracteres")

    # Verificar keyword
    if keyword:
        keyword_lower = keyword.lower()
        keyword_count = texto_lower.count(keyword_lower)
        densidade = (keyword_count / n_palavras) * 100 if n_palavras > 0 else 0

        if 1 <= densidade <= 3:
            seo["itens"].append({"item": f"Densidade de keyword boa ({densidade:.1f}%)", "ok": True})
            seo["pontuacao"] += 15
        elif densidade < 1:
            seo["itens"].append({"item": f"Densidade de keyword baixa ({densidade:.1f}%)", "ok": False})
            seo["sugestoes"].append(f"Aumentar uso da keyword '{keyword}' (ideal: 1-3%)")
        else:
            seo["itens"].append({"item": f"Densidade de keyword alta ({densidade:.1f}%)", "ok": False})
            seo["sugestoes"].append("Reduzir keyword stuffing (ideal: 1-3%)")

        # Keyword no início
        primeiras_100 = texto_lower[:500]
        if keyword_lower in primeiras_100:
            seo["itens"].append({"item": "Keyword aparece no início do conteúdo", "ok": True})
            seo["pontuacao"] += 10
        else:
            seo["sugestoes"].append("Incluir keyword nos primeiros parágrafos")

    # Verificar comprimento do conteúdo
    if n_palavras >= 1500:
        seo["itens"].append({"item": f"Conteúdo longo ({n_palavras} palavras) - bom para SEO", "ok": True})
        seo["pontuacao"] += 15
    elif n_palavras >= 800:
        seo["itens"].append({"item": f"Conteúdo médio ({n_palavras} palavras)", "ok": True})
        seo["pontuacao"] += 10
    elif n_palavras >= 300:
        seo["itens"].append({"item": f"Conteúdo curto ({n_palavras} palavras)", "ok": False})
        seo["sugestoes"].append("Expandir conteúdo para pelo menos 800 palavras")
    else:
        seo["itens"].append({"item": f"Conteúdo muito curto ({n_palavras} palavras)", "ok": False})
        seo["sugestoes"].append("Conteúdo muito curto para SEO - ideal: 800+ palavras")

    # Verificar headings
    h1_count = len(re.findall(r'^# ', texto, re.MULTILINE))
    h2_count = len(re.findall(r'^## ', texto, re.MULTILINE))

    if h1_count == 1:
        seo["itens"].append({"item": "Um H1 presente (correto)", "ok": True})
        seo["pontuacao"] += 10
    elif h1_count == 0:
        seo["itens"].append({"item": "Nenhum H1 encontrado", "ok": False})
        seo["sugestoes"].append("Adicionar um título H1 único")
    else:
        seo["itens"].append({"item": f"Múltiplos H1 ({h1_count})", "ok": False})
        seo["sugestoes"].append("Usar apenas um H1 por página")

    if h2_count >= 2:
        seo["itens"].append({"item": f"{h2_count} subtítulos H2 (boa estrutura)", "ok": True})
        seo["pontuacao"] += 10
    else:
        seo["sugestoes"].append("Adicionar mais subtítulos H2 para melhorar escaneabilidade")

    # Verificar links
    links_internos = len(re.findall(r'\[([^\]]+)\]\((?!http)([^)]+)\)', texto))
    links_externos = len(re.findall(r'\[([^\]]+)\]\(https?://([^)]+)\)', texto))

    if links_internos >= 2:
        seo["itens"].append({"item": f"{links_internos} links internos", "ok": True})
        seo["pontuacao"] += 10
    else:
        seo["sugestoes"].append("Adicionar links internos para outros conteúdos")

    if links_externos >= 1:
        seo["itens"].append({"item": f"{links_externos} links externos", "ok": True})
        seo["pontuacao"] += 5
    else:
        seo["sugestoes"].append("Considerar adicionar links externos para fontes confiáveis")

    # Verificar imagens
    imagens = len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', texto))
    if imagens >= 1:
        seo["itens"].append({"item": f"{imagens} imagens encontradas", "ok": True})
        seo["pontuacao"] += 5

        # Verificar alt text
        imagens_sem_alt = len(re.findall(r'!\[\]\(', texto))
        if imagens_sem_alt > 0:
            seo["sugestoes"].append(f"{imagens_sem_alt} imagens sem texto alternativo (alt)")
    else:
        seo["sugestoes"].append("Adicionar imagens relevantes com alt text")

    # Verificar meta description (primeiro parágrafo)
    paragrafos = [p.strip() for p in texto.split('\n\n') if p.strip() and not p.startswith('#')]
    if paragrafos:
        primeiro_paragrafo = paragrafos[0]
        if 120 <= len(primeiro_paragrafo) <= 160:
            seo["itens"].append({"item": "Primeiro parágrafo com tamanho ideal para meta", "ok": True})
            seo["pontuacao"] += 5

    return seo


def analisar_copywriting(texto: str) -> Dict:
    """Analisa elementos de copywriting e persuasão."""
    resultado = {
        "palavras_poder": {},
        "total_palavras_poder": 0,
        "ctas_encontrados": [],
        "perguntas": 0,
        "pontuacao": 0,
        "sugestoes": []
    }

    texto_lower = texto.lower()

    # Contar palavras de poder por categoria
    for categoria, palavras in PALAVRAS_PODER.items():
        count = sum(1 for p in palavras if p in texto_lower)
        if count > 0:
            resultado["palavras_poder"][categoria] = count
            resultado["total_palavras_poder"] += count

    # Pontuação baseada em palavras de poder
    if resultado["total_palavras_poder"] >= 10:
        resultado["pontuacao"] += 25
    elif resultado["total_palavras_poder"] >= 5:
        resultado["pontuacao"] += 15
    elif resultado["total_palavras_poder"] >= 2:
        resultado["pontuacao"] += 10
    else:
        resultado["sugestoes"].append("Adicionar mais palavras de poder para aumentar persuasão")

    # Detectar CTAs (Call to Action)
    padroes_cta = [
        r'(?:clique|click)\s+(?:aqui|agora|no botão)',
        r'(?:saiba|descubra|conheça)\s+mais',
        r'(?:baixe|download|faça download)',
        r'(?:inscreva-se|cadastre-se|registre-se)',
        r'(?:compre|adquira|garanta)\s+(?:agora|já|hoje)',
        r'(?:comece|inicie|experimente)\s+(?:agora|já|grátis)',
        r'(?:entre em contato|fale conosco|fale com)',
        r'(?:aproveite|não perca|garanta)',
        r'(?:assine|teste grátis|trial)',
        r'(?:reserve|agende|marque)'
    ]

    for padrao in padroes_cta:
        matches = re.findall(padrao, texto_lower)
        resultado["ctas_encontrados"].extend(matches)

    if len(resultado["ctas_encontrados"]) >= 2:
        resultado["pontuacao"] += 20
    elif len(resultado["ctas_encontrados"]) >= 1:
        resultado["pontuacao"] += 10
    else:
        resultado["sugestoes"].append("Adicionar pelo menos um CTA (Call to Action) claro")

    # Contar perguntas (engajamento)
    resultado["perguntas"] = len(re.findall(r'\?', texto))
    if resultado["perguntas"] >= 3:
        resultado["pontuacao"] += 15
    elif resultado["perguntas"] >= 1:
        resultado["pontuacao"] += 10
    else:
        resultado["sugestoes"].append("Adicionar perguntas para engajar o leitor")

    # Verificar uso de números/estatísticas
    numeros = re.findall(r'\b\d+(?:[.,]\d+)?(?:\s*%|\s*x|\s*vezes)?\b', texto)
    if len(numeros) >= 3:
        resultado["pontuacao"] += 15
        resultado["usa_numeros"] = True
    else:
        resultado["sugestoes"].append("Incluir números e estatísticas para credibilidade")
        resultado["usa_numeros"] = False

    # Verificar uso de "você"
    uso_voce = len(re.findall(r'\bvocê\b', texto_lower))
    if uso_voce >= 5:
        resultado["pontuacao"] += 10
        resultado["linguagem_direta"] = True
    else:
        resultado["sugestoes"].append("Usar mais 'você' para linguagem direta e pessoal")
        resultado["linguagem_direta"] = False

    # Verificar urgência/escassez
    tem_urgencia = any(p in texto_lower for p in PALAVRAS_PODER["urgencia"])
    if tem_urgencia:
        resultado["pontuacao"] += 5
        resultado["tem_urgencia"] = True
    else:
        resultado["tem_urgencia"] = False

    return resultado


def analisar_social(texto: str) -> Dict:
    """Analisa texto para redes sociais."""
    n_caracteres = len(texto)
    n_palavras = contar_palavras(texto)

    resultado = {
        "caracteres": n_caracteres,
        "palavras": n_palavras,
        "hashtags": re.findall(r'#\w+', texto),
        "mencoes": re.findall(r'@\w+', texto),
        "emojis": len(re.findall(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]', texto)),
        "links": len(re.findall(r'https?://\S+', texto)),
        "adequacao_plataformas": {}
    }

    # Verificar adequação por plataforma
    plataformas = {
        "Twitter/X": {"max_chars": 280, "hashtags_ideal": "1-3", "emojis": "opcional"},
        "Instagram": {"max_chars": 2200, "hashtags_ideal": "5-30", "emojis": "recomendado"},
        "LinkedIn": {"max_chars": 3000, "hashtags_ideal": "3-5", "emojis": "moderado"},
        "Facebook": {"max_chars": 63206, "hashtags_ideal": "1-2", "emojis": "opcional"},
        "TikTok": {"max_chars": 2200, "hashtags_ideal": "3-5", "emojis": "recomendado"}
    }

    for plataforma, specs in plataformas.items():
        adequado = n_caracteres <= specs["max_chars"]
        resultado["adequacao_plataformas"][plataforma] = {
            "dentro_limite": adequado,
            "caracteres_restantes": specs["max_chars"] - n_caracteres if adequado else 0
        }

    # Sugestões
    resultado["sugestoes"] = []

    n_hashtags = len(resultado["hashtags"])
    if n_hashtags == 0:
        resultado["sugestoes"].append("Adicionar hashtags relevantes")
    elif n_hashtags > 30:
        resultado["sugestoes"].append("Reduzir número de hashtags (máx recomendado: 30)")

    if resultado["emojis"] == 0:
        resultado["sugestoes"].append("Considerar adicionar emojis para engajamento")

    if not any(palavra in texto.lower() for palavra in ['clique', 'link', 'bio', 'saiba mais', 'comente', 'compartilhe']):
        resultado["sugestoes"].append("Adicionar CTA (ex: 'Comente', 'Compartilhe', 'Link na bio')")

    return resultado


def analisar_email(texto: str) -> Dict:
    """Analisa texto para email marketing."""
    resultado = {
        "linhas": texto.count('\n') + 1,
        "caracteres": len(texto),
        "palavras": contar_palavras(texto),
        "spam_words": [],
        "pontuacao": 0,
        "sugestoes": []
    }

    texto_lower = texto.lower()

    # Palavras que podem acionar filtros de spam
    spam_triggers = [
        'grátis', 'free', 'clique aqui', 'oferta especial', 'por tempo limitado',
        'ganhe dinheiro', 'sem custo', '100%', 'garantido', 'urgente', 'aja agora',
        'não perca', 'última chance', 'exclusivo', 'bônus', 'presente', 'promoção'
    ]

    for palavra in spam_triggers:
        if palavra in texto_lower:
            resultado["spam_words"].append(palavra)

    # Pontuação
    if len(resultado["spam_words"]) <= 2:
        resultado["pontuacao"] += 20
    elif len(resultado["spam_words"]) <= 5:
        resultado["pontuacao"] += 10
        resultado["sugestoes"].append("Muitas palavras que podem acionar filtros de spam")
    else:
        resultado["sugestoes"].append("Alto risco de spam - considerar reescrever")

    # Verificar personalização
    if any(tag in texto for tag in ['{{nome}}', '{nome}', '{{primeiro_nome}}', '{primeiro_nome}', '[NOME]']):
        resultado["pontuacao"] += 15
        resultado["personalizado"] = True
    else:
        resultado["sugestoes"].append("Adicionar personalização (ex: {{nome}})")
        resultado["personalizado"] = False

    # Verificar assunto (primeira linha)
    linhas = texto.strip().split('\n')
    if linhas:
        assunto = linhas[0]
        if len(assunto) <= 50:
            resultado["pontuacao"] += 15
            resultado["assunto_ok"] = True
        else:
            resultado["sugestoes"].append(f"Assunto muito longo ({len(assunto)} chars). Ideal: até 50")
            resultado["assunto_ok"] = False

        # Verificar se tem emoji no assunto
        if re.search(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF]', assunto):
            resultado["pontuacao"] += 5

    # Verificar CTA
    ctas_email = ['clique', 'acesse', 'baixe', 'confira', 'veja', 'descubra', 'saiba mais']
    if any(cta in texto_lower for cta in ctas_email):
        resultado["pontuacao"] += 15
        resultado["tem_cta"] = True
    else:
        resultado["sugestoes"].append("Adicionar um CTA claro")
        resultado["tem_cta"] = False

    # Verificar link de descadastro
    if 'descadastrar' in texto_lower or 'unsubscribe' in texto_lower or 'cancelar inscrição' in texto_lower:
        resultado["pontuacao"] += 10
        resultado["tem_unsubscribe"] = True
    else:
        resultado["sugestoes"].append("Importante: incluir link de descadastro")
        resultado["tem_unsubscribe"] = False

    return resultado


def extrair_palavras_chave(texto: str, n: int = 10) -> List[Tuple[str, int]]:
    """Extrai palavras-chave mais frequentes do texto."""
    palavras = re.findall(r'\b\w+\b', texto.lower())

    # Filtrar stop words e palavras curtas
    palavras_filtradas = [
        p for p in palavras
        if p not in STOP_WORDS and len(p) > 3
    ]

    # Contar frequência
    contador = Counter(palavras_filtradas)

    return contador.most_common(n)


def calcular_pontuacao_geral(resultados: Dict) -> Dict:
    """Calcula pontuação geral do conteúdo."""
    pontuacao = {
        "total": 0,
        "max": 100,
        "categorias": {},
        "nivel": "",
        "cor": ""
    }

    # Coletar pontuações de diferentes análises
    if "legibilidade" in resultados:
        leg = resultados["legibilidade"]
        # Normalizar Flesch para 0-25
        pontos_leg = min(25, (leg.get("indice_flesch", 0) / 100) * 25)
        pontuacao["categorias"]["legibilidade"] = round(pontos_leg, 1)
        pontuacao["total"] += pontos_leg

    if "seo" in resultados:
        # SEO já está em 0-100, normalizar para 0-25
        pontos_seo = min(25, (resultados["seo"].get("pontuacao", 0) / 100) * 25)
        pontuacao["categorias"]["seo"] = round(pontos_seo, 1)
        pontuacao["total"] += pontos_seo

    if "copywriting" in resultados:
        # Copywriting em 0-100, normalizar para 0-25
        pontos_copy = min(25, (resultados["copywriting"].get("pontuacao", 0) / 100) * 25)
        pontuacao["categorias"]["copywriting"] = round(pontos_copy, 1)
        pontuacao["total"] += pontos_copy

    if "estrutura" in resultados:
        est = resultados["estrutura"]
        # Calcular pontuação de estrutura
        pontos_est = 0
        if est.get("headings", {}).get("h1", 0) >= 1:
            pontos_est += 5
        if est.get("headings", {}).get("h2", 0) >= 2:
            pontos_est += 5
        if est.get("listas", {}).get("nao_ordenadas", 0) + est.get("listas", {}).get("ordenadas", 0) >= 1:
            pontos_est += 5
        if est.get("links", 0) >= 1:
            pontos_est += 5
        if est.get("imagens", 0) >= 1:
            pontos_est += 5
        pontuacao["categorias"]["estrutura"] = pontos_est
        pontuacao["total"] += pontos_est

    # Arredondar total
    pontuacao["total"] = round(pontuacao["total"])

    # Classificar
    if pontuacao["total"] >= 80:
        pontuacao["nivel"] = "Excelente"
        pontuacao["cor"] = "verde"
    elif pontuacao["total"] >= 60:
        pontuacao["nivel"] = "Bom"
        pontuacao["cor"] = "azul"
    elif pontuacao["total"] >= 40:
        pontuacao["nivel"] = "Regular"
        pontuacao["cor"] = "amarelo"
    else:
        pontuacao["nivel"] = "Precisa melhorar"
        pontuacao["cor"] = "vermelho"

    return pontuacao


def formatar_tabela(resultados: Dict, arquivo: str) -> str:
    """Formata resultados em tabela ASCII."""
    linhas = []
    linhas.append("=" * 70)
    linhas.append(f"  AUDITORIA DE CONTEÚDO: {os.path.basename(arquivo)}")
    linhas.append("=" * 70)

    # Métricas básicas
    if "metricas" in resultados:
        m = resultados["metricas"]
        linhas.append("\n📊 MÉTRICAS BÁSICAS")
        linhas.append("-" * 40)
        linhas.append(f"  Palavras:      {m.get('palavras', 0)}")
        linhas.append(f"  Caracteres:    {m.get('caracteres', {}).get('total', 0)}")
        linhas.append(f"  Linhas:        {m.get('caracteres', {}).get('linhas', 0)}")
        linhas.append(f"  Tempo leitura: {m.get('tempo_leitura', 'N/A')}")

    # Legibilidade
    if "legibilidade" in resultados:
        leg = resultados["legibilidade"]
        linhas.append("\n📖 LEGIBILIDADE")
        linhas.append("-" * 40)
        linhas.append(f"  Índice Flesch:  {leg.get('indice_flesch', 0)}/100")
        linhas.append(f"  Nível:          {leg.get('nivel', 'N/A')}")
        linhas.append(f"  Público-alvo:   {leg.get('publico_alvo', 'N/A')}")
        linhas.append(f"  Palavras/frase: {leg.get('media_palavras_por_sentenca', 0)}")

    # SEO
    if "seo" in resultados:
        seo = resultados["seo"]
        linhas.append("\n🔍 SEO")
        linhas.append("-" * 40)
        linhas.append(f"  Pontuação: {seo.get('pontuacao', 0)}/{seo.get('max_pontuacao', 100)}")
        for item in seo.get("itens", [])[:5]:
            status = "✓" if item.get("ok") else "✗"
            linhas.append(f"  {status} {item.get('item', '')}")

    # Copywriting
    if "copywriting" in resultados:
        copy = resultados["copywriting"]
        linhas.append("\n✍️ COPYWRITING")
        linhas.append("-" * 40)
        linhas.append(f"  Pontuação:        {copy.get('pontuacao', 0)}/100")
        linhas.append(f"  Palavras poder:   {copy.get('total_palavras_poder', 0)}")
        linhas.append(f"  CTAs encontrados: {len(copy.get('ctas_encontrados', []))}")
        linhas.append(f"  Perguntas:        {copy.get('perguntas', 0)}")

    # Palavras-chave
    if "palavras_chave" in resultados:
        linhas.append("\n🔑 TOP PALAVRAS-CHAVE")
        linhas.append("-" * 40)
        for palavra, freq in resultados["palavras_chave"][:5]:
            linhas.append(f"  {palavra}: {freq}x")

    # Pontuação geral
    if "pontuacao_geral" in resultados:
        pg = resultados["pontuacao_geral"]
        linhas.append("\n" + "=" * 70)
        linhas.append(f"  PONTUAÇÃO GERAL: {pg.get('total', 0)}/{pg.get('max', 100)} - {pg.get('nivel', '')}")
        linhas.append("=" * 70)

    # Sugestões
    todas_sugestoes = []
    for key in ["seo", "copywriting", "legibilidade"]:
        if key in resultados and "sugestoes" in resultados[key]:
            todas_sugestoes.extend(resultados[key]["sugestoes"])

    if todas_sugestoes:
        linhas.append("\n💡 SUGESTÕES DE MELHORIA")
        linhas.append("-" * 40)
        for i, sug in enumerate(todas_sugestoes[:8], 1):
            linhas.append(f"  {i}. {sug}")

    return "\n".join(linhas)


def formatar_markdown(resultados: Dict, arquivo: str) -> str:
    """Formata resultados em Markdown."""
    linhas = []
    linhas.append(f"# Auditoria de Conteúdo: {os.path.basename(arquivo)}")
    linhas.append(f"\n*Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")

    # Pontuação geral
    if "pontuacao_geral" in resultados:
        pg = resultados["pontuacao_geral"]
        linhas.append(f"## 🎯 Pontuação Geral: {pg.get('total', 0)}/100 ({pg.get('nivel', '')})\n")

        linhas.append("| Categoria | Pontos |")
        linhas.append("|-----------|--------|")
        for cat, pontos in pg.get("categorias", {}).items():
            linhas.append(f"| {cat.capitalize()} | {pontos} |")
        linhas.append("")

    # Métricas básicas
    if "metricas" in resultados:
        m = resultados["metricas"]
        linhas.append("## 📊 Métricas Básicas\n")
        linhas.append(f"- **Palavras:** {m.get('palavras', 0)}")
        linhas.append(f"- **Caracteres:** {m.get('caracteres', {}).get('total', 0)}")
        linhas.append(f"- **Linhas:** {m.get('caracteres', {}).get('linhas', 0)}")
        linhas.append(f"- **Tempo de leitura:** {m.get('tempo_leitura', 'N/A')}\n")

    # Legibilidade
    if "legibilidade" in resultados:
        leg = resultados["legibilidade"]
        linhas.append("## 📖 Legibilidade\n")
        linhas.append(f"- **Índice Flesch:** {leg.get('indice_flesch', 0)}/100")
        linhas.append(f"- **Nível:** {leg.get('nivel', 'N/A')}")
        linhas.append(f"- **Público-alvo:** {leg.get('publico_alvo', 'N/A')}")
        linhas.append(f"- **Média palavras/sentença:** {leg.get('media_palavras_por_sentenca', 0)}\n")

    # SEO
    if "seo" in resultados:
        seo = resultados["seo"]
        linhas.append(f"## 🔍 SEO ({seo.get('pontuacao', 0)}/{seo.get('max_pontuacao', 100)})\n")
        for item in seo.get("itens", []):
            emoji = "✅" if item.get("ok") else "❌"
            linhas.append(f"- {emoji} {item.get('item', '')}")
        linhas.append("")

    # Copywriting
    if "copywriting" in resultados:
        copy = resultados["copywriting"]
        linhas.append(f"## ✍️ Copywriting ({copy.get('pontuacao', 0)}/100)\n")
        linhas.append(f"- **Palavras de poder:** {copy.get('total_palavras_poder', 0)}")
        if copy.get("palavras_poder"):
            for cat, count in copy["palavras_poder"].items():
                linhas.append(f"  - {cat}: {count}")
        linhas.append(f"- **CTAs encontrados:** {len(copy.get('ctas_encontrados', []))}")
        linhas.append(f"- **Perguntas:** {copy.get('perguntas', 0)}")
        linhas.append(f"- **Usa números:** {'Sim' if copy.get('usa_numeros') else 'Não'}")
        linhas.append(f"- **Linguagem direta:** {'Sim' if copy.get('linguagem_direta') else 'Não'}\n")

    # Palavras-chave
    if "palavras_chave" in resultados:
        linhas.append("## 🔑 Top Palavras-chave\n")
        linhas.append("| Palavra | Frequência |")
        linhas.append("|---------|------------|")
        for palavra, freq in resultados["palavras_chave"][:10]:
            linhas.append(f"| {palavra} | {freq} |")
        linhas.append("")

    # Sugestões
    todas_sugestoes = []
    for key in ["seo", "copywriting", "legibilidade"]:
        if key in resultados and "sugestoes" in resultados[key]:
            todas_sugestoes.extend(resultados[key]["sugestoes"])

    if todas_sugestoes:
        linhas.append("## 💡 Sugestões de Melhoria\n")
        for sug in todas_sugestoes:
            linhas.append(f"1. {sug}")

    return "\n".join(linhas)


def auditar_arquivo(caminho: str, tipo: Optional[str] = None, keyword: Optional[str] = None) -> Dict:
    """Executa auditoria completa em um arquivo."""
    conteudo, extensao = ler_arquivo(caminho)

    if conteudo is None:
        return {"erro": f"Não foi possível ler o arquivo: {caminho}"}

    resultados = {
        "arquivo": caminho,
        "extensao": extensao,
        "tipo_conteudo": tipo,
        "data_auditoria": datetime.now().isoformat()
    }

    # Métricas básicas
    n_palavras = contar_palavras(conteudo)
    resultados["metricas"] = {
        "palavras": n_palavras,
        "caracteres": contar_caracteres(conteudo),
        "tempo_leitura": calcular_tempo_leitura(n_palavras)
    }

    # Análises específicas por tipo
    if tipo == "social":
        resultados["social"] = analisar_social(conteudo)
    elif tipo == "email":
        resultados["email"] = analisar_email(conteudo)
    else:
        # Análise completa para blog/landing/geral
        resultados["legibilidade"] = analisar_legibilidade(conteudo)
        resultados["copywriting"] = analisar_copywriting(conteudo)
        resultados["palavras_chave"] = extrair_palavras_chave(conteudo)

        # Extrair título do primeiro H1
        titulo_match = re.search(r'^#\s+(.+)$', conteudo, re.MULTILINE)
        titulo = titulo_match.group(1) if titulo_match else None

        resultados["seo"] = analisar_seo(conteudo, titulo=titulo, keyword=keyword)

        if extensao in ['.md', '.markdown']:
            resultados["estrutura"] = analisar_estrutura_markdown(conteudo)

    # Calcular pontuação geral
    resultados["pontuacao_geral"] = calcular_pontuacao_geral(resultados)

    return resultados


def auditar_pasta(pasta: str, extensoes: List[str] = None) -> List[Dict]:
    """Audita todos os arquivos de uma pasta."""
    if extensoes is None:
        extensoes = ['.md', '.markdown', '.txt', '.html']

    resultados = []

    for root, dirs, files in os.walk(pasta):
        for file in files:
            _, ext = os.path.splitext(file)
            if ext.lower() in extensoes:
                caminho = os.path.join(root, file)
                resultado = auditar_arquivo(caminho)
                resultados.append(resultado)

    return resultados


def mostrar_ajuda():
    """Mostra mensagem de ajuda."""
    ajuda = """
╔══════════════════════════════════════════════════════════════════════╗
║                         CONTENT AUDIT                                 ║
║              Auditar conteúdo e sugerir melhorias                    ║
╚══════════════════════════════════════════════════════════════════════╝

USO:
    python content_audit.py <arquivo> [opções]
    python content_audit.py --pasta <diretório> [opções]

ARGUMENTOS:
    arquivo              Arquivo para auditar (.md, .txt, .html)
    --pasta <dir>        Auditar todos os arquivos de uma pasta

OPÇÕES:
    --tipo <tipo>        Tipo de conteúdo: blog, social, email, landing
    --keyword <palavra>  Keyword principal para análise SEO
    --formato <fmt>      Formato de saída: tabela, markdown, json
    --completo           Análise completa com todos os detalhes
    --salvar <arquivo>   Salvar resultado em arquivo
    -h, --help           Mostrar esta ajuda

EXEMPLOS:
    # Auditar artigo de blog
    python content_audit.py artigo.md --tipo blog

    # Auditar com keyword específica
    python content_audit.py post.md --keyword "marketing digital"

    # Auditar post de rede social
    python content_audit.py caption.txt --tipo social

    # Auditar pasta completa em formato markdown
    python content_audit.py --pasta ./conteudo --formato markdown

    # Salvar resultado em arquivo
    python content_audit.py artigo.md --salvar resultado.json --formato json

TIPOS DE CONTEÚDO:
    blog     - Artigos e posts de blog (análise SEO completa)
    social   - Posts para redes sociais (hashtags, limites)
    email    - Email marketing (spam score, personalização)
    landing  - Landing pages (conversão, CTAs)

MÉTRICAS ANALISADAS:
    • Legibilidade (Índice Flesch adaptado para português)
    • SEO (títulos, keywords, estrutura, links)
    • Copywriting (palavras de poder, CTAs, persuasão)
    • Estrutura (headings, listas, formatação)
    • Palavras-chave (frequência e relevância)
"""
    print(ajuda)


def main():
    """Função principal."""
    args = sys.argv[1:]

    if not args or '-h' in args or '--help' in args:
        mostrar_ajuda()
        return

    # Parsear argumentos
    arquivo = None
    pasta = None
    tipo = None
    keyword = None
    formato = "tabela"
    completo = False
    salvar = None

    i = 0
    while i < len(args):
        arg = args[i]

        if arg == '--pasta' and i + 1 < len(args):
            pasta = args[i + 1]
            i += 2
        elif arg == '--tipo' and i + 1 < len(args):
            tipo = args[i + 1]
            i += 2
        elif arg == '--keyword' and i + 1 < len(args):
            keyword = args[i + 1]
            i += 2
        elif arg == '--formato' and i + 1 < len(args):
            formato = args[i + 1]
            i += 2
        elif arg == '--salvar' and i + 1 < len(args):
            salvar = args[i + 1]
            i += 2
        elif arg == '--completo':
            completo = True
            i += 1
        elif not arg.startswith('--') and arquivo is None:
            arquivo = arg
            i += 1
        else:
            i += 1

    # Executar auditoria
    if pasta:
        if not os.path.isdir(pasta):
            print(f"❌ Pasta não encontrada: {pasta}")
            return

        print(f"📂 Auditando pasta: {pasta}")
        resultados = auditar_pasta(pasta)

        if not resultados:
            print("Nenhum arquivo encontrado para auditar.")
            return

        print(f"✓ {len(resultados)} arquivos analisados\n")

        # Resumo da pasta
        total_palavras = sum(r.get("metricas", {}).get("palavras", 0) for r in resultados)
        media_pontuacao = sum(r.get("pontuacao_geral", {}).get("total", 0) for r in resultados) / len(resultados)

        print(f"📊 Total de palavras: {total_palavras}")
        print(f"📈 Média de pontuação: {media_pontuacao:.1f}/100\n")

        # Listar arquivos por pontuação
        resultados_sorted = sorted(resultados, key=lambda x: x.get("pontuacao_geral", {}).get("total", 0), reverse=True)

        print("Ranking de conteúdo:")
        print("-" * 50)
        for r in resultados_sorted[:10]:
            nome = os.path.basename(r.get("arquivo", ""))
            pontos = r.get("pontuacao_geral", {}).get("total", 0)
            nivel = r.get("pontuacao_geral", {}).get("nivel", "")
            print(f"  {pontos:3}/100 | {nome[:35]:<35} | {nivel}")

    elif arquivo:
        if not os.path.isfile(arquivo):
            print(f"❌ Arquivo não encontrado: {arquivo}")
            return

        resultados = auditar_arquivo(arquivo, tipo=tipo, keyword=keyword)

        if "erro" in resultados:
            print(f"❌ {resultados['erro']}")
            return

        # Formatar saída
        if formato == "json":
            # Converter palavras_chave para formato serializável
            if "palavras_chave" in resultados:
                resultados["palavras_chave"] = [
                    {"palavra": p, "frequencia": f}
                    for p, f in resultados["palavras_chave"]
                ]
            saida = json.dumps(resultados, indent=2, ensure_ascii=False)
        elif formato == "markdown":
            saida = formatar_markdown(resultados, arquivo)
        else:
            saida = formatar_tabela(resultados, arquivo)

        # Salvar ou exibir
        if salvar:
            with open(salvar, 'w', encoding='utf-8') as f:
                f.write(saida)
            print(f"✓ Resultado salvo em: {salvar}")
        else:
            print(saida)

    else:
        print("❌ Especifique um arquivo ou pasta para auditar.")
        print("Use --help para ver as opções disponíveis.")


if __name__ == "__main__":
    main()