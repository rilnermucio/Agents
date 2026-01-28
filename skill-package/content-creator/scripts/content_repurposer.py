#!/usr/bin/env python3
"""
Content Repurposer - Adapta conteúdo entre plataformas

Transforma um conteúdo original (ex: artigo de blog) em múltiplos formatos
para diferentes plataformas.

Uso:
    python content_repurposer.py --file artigo.txt --output todos
    python content_repurposer.py --file artigo.txt --output instagram
    python content_repurposer.py "Texto aqui" --output twitter
"""

import re
import sys
import argparse
from typing import Dict, List
from datetime import datetime


def extract_key_points(text: str, max_points: int = 7) -> List[str]:
    """Extrai pontos-chave do texto."""
    # Procura por listas numeradas ou com bullet points
    list_items = re.findall(r'(?:^|\n)\s*(?:\d+[.)]\s*|[-•*]\s*)(.+?)(?=\n|$)', text)

    if list_items:
        return list_items[:max_points]

    # Se não encontrar listas, divide em sentenças e pega as mais importantes
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 30]

    # Prioriza sentenças com palavras-chave importantes
    important_words = ["importante", "principal", "essencial", "fundamental",
                       "primeiro", "segundo", "terceiro", "dica", "segredo",
                       "aprenda", "descubra", "como", "por que"]

    scored = []
    for s in sentences:
        score = sum(1 for w in important_words if w.lower() in s.lower())
        scored.append((score, s))

    scored.sort(reverse=True)
    return [s for _, s in scored[:max_points]]


def extract_title(text: str) -> str:
    """Tenta extrair o título do texto."""
    lines = text.strip().split('\n')

    for line in lines[:5]:
        line = line.strip()
        # Procura por títulos com # ou linhas curtas no início
        if line.startswith('#'):
            return line.lstrip('#').strip()
        if len(line) < 100 and len(line) > 10 and not line.endswith('.'):
            return line

    # Se não encontrar, usa as primeiras palavras
    words = text.split()[:10]
    return ' '.join(words) + '...'


def estimate_read_time(text: str) -> int:
    """Estima tempo de leitura em minutos."""
    words = len(text.split())
    return max(1, round(words / 200))


def to_instagram_carousel(text: str, num_slides: int = 10) -> Dict:
    """Converte para carrossel do Instagram."""
    title = extract_title(text)
    points = extract_key_points(text, num_slides - 2)

    slides = []

    # Slide 1: Capa
    slides.append({
        "slide": 1,
        "type": "capa",
        "content": title,
        "notes": "Design impactante, fonte grande, parar o scroll"
    })

    # Slides de conteúdo
    for i, point in enumerate(points, 2):
        # Resumir se muito longo
        if len(point) > 150:
            point = point[:147] + "..."

        slides.append({
            "slide": i,
            "type": "conteudo",
            "content": point,
            "notes": "1 ideia por slide, fonte legível (24pt+)"
        })

    # Slide de resumo
    slides.append({
        "slide": len(slides) + 1,
        "type": "resumo",
        "content": "📌 Resumo:\n" + "\n".join([f"• {p[:50]}..." for p in points[:5]]),
        "notes": "Recap dos pontos principais"
    })

    # Slide CTA
    slides.append({
        "slide": len(slides) + 1,
        "type": "cta",
        "content": "💾 Salva esse post!\n📤 Compartilha com quem precisa\n👉 Segue pra mais dicas",
        "notes": "Call-to-action claro"
    })

    # Caption
    caption = f"""✨ {title}

{chr(10).join([f'{i+1}. {p[:80]}...' for i, p in enumerate(points[:5])])}

Qual desses pontos você vai aplicar primeiro? 👇

.
.
.
#dicasdeconteudo #marketingdigital #socialmedia #conteudo #dicas"""

    return {
        "platform": "Instagram Carrossel",
        "slides": slides,
        "total_slides": len(slides),
        "caption": caption,
        "hashtags_sugeridas": 15
    }


def to_instagram_reels(text: str) -> Dict:
    """Converte para roteiro de Reels."""
    title = extract_title(text)
    points = extract_key_points(text, 3)

    script = f"""🎬 ROTEIRO REELS (30-60s)

📍 HOOK (0-2s):
"{title[:50]}..."
[Texto grande na tela + olhar para câmera]

📍 SETUP (2-5s):
"Se você quer [benefício], presta atenção nisso:"

📍 PONTO 1 (5-15s):
"Primeiro, {points[0][:80] if points else 'ponto principal'}..."
[Demonstrar ou exemplificar]

📍 PONTO 2 (15-25s):
"Segundo, {points[1][:80] if len(points) > 1 else 'segundo ponto'}..."
[Demonstrar ou exemplificar]

📍 PONTO 3 (25-35s):
"E o mais importante: {points[2][:80] if len(points) > 2 else 'terceiro ponto'}..."

📍 CTA (35-40s):
"Salva esse vídeo e segue pra mais dicas!"
[Texto: 📌 SALVA + SEGUE]

---
📝 CAPTION:
{title}

Qual desses você já faz? 👇

#reels #dicas #viral
"""

    return {
        "platform": "Instagram Reels",
        "script": script,
        "duracao_sugerida": "30-45 segundos",
        "formato": "Vertical 9:16"
    }


def to_twitter_thread(text: str) -> Dict:
    """Converte para thread do Twitter/X."""
    title = extract_title(text)
    points = extract_key_points(text, 7)

    tweets = []

    # Tweet 1: Hook
    tweets.append({
        "number": 1,
        "content": f"{title}\n\n🧵👇",
        "chars": len(f"{title}\n\n🧵👇")
    })

    # Tweet 2: Contexto
    tweets.append({
        "number": 2,
        "content": f"Muita gente não sabe, mas isso pode mudar completamente seus resultados.\n\nVou explicar:",
        "chars": 95
    })

    # Tweets de conteúdo
    for i, point in enumerate(points, 3):
        # Limitar a 280 caracteres
        content = f"{i-2}/ {point}"
        if len(content) > 270:
            content = content[:267] + "..."

        tweets.append({
            "number": i,
            "content": content,
            "chars": len(content)
        })

    # Tweet de resumo
    tweets.append({
        "number": len(tweets) + 1,
        "content": f"Resumindo:\n\n" + "\n".join([f"✅ {p[:40]}..." for p in points[:5]]),
        "chars": 0  # Calcular depois
    })

    # Tweet CTA
    tweets.append({
        "number": len(tweets) + 1,
        "content": "Se essa thread foi útil:\n\n1. RT o primeiro tweet\n2. Me segue pra mais\n\nQual desses você vai aplicar? 👇",
        "chars": 105
    })

    return {
        "platform": "Twitter/X Thread",
        "tweets": tweets,
        "total_tweets": len(tweets),
        "nota": "Postar com 1-2 min de intervalo entre tweets"
    }


def to_linkedin_post(text: str) -> Dict:
    """Converte para post do LinkedIn."""
    title = extract_title(text)
    points = extract_key_points(text, 5)

    hook_options = [
        f"Isso mudou minha perspectiva sobre {title.lower()[:30]}.",
        f"Depois de anos estudando isso, aprendi que...",
        f"A maioria ignora isso, mas faz toda diferença:"
    ]

    post = f"""{hook_options[0]}

↓

{chr(10).join([f'→ {p[:100]}' for p in points])}

---

O que eu aprendi com isso:

Não existe atalho. Existe método.

E o método começa com entender esses fundamentos.

Qual desses pontos ressoou mais com você?

#carreira #desenvolvimento #aprendizado"""

    return {
        "platform": "LinkedIn",
        "post": post,
        "chars": len(post),
        "max_chars": 3000,
        "dica": "Postar entre 7h-8h ou 17h-18h (dias úteis)"
    }


def to_email_newsletter(text: str) -> Dict:
    """Converte para newsletter por email."""
    title = extract_title(text)
    points = extract_key_points(text, 5)
    read_time = estimate_read_time(text)

    email = f"""Assunto: {title}

Pré-header: {points[0][:80] if points else 'Confira as dicas'}...

---

Olá, [NOME]!

{points[0] if points else 'Introdução do conteúdo...'}

Hoje quero compartilhar com você algumas reflexões sobre isso.

**O que você vai aprender:**

{chr(10).join([f'✓ {p[:80]}' for p in points])}

---

**Vamos aos pontos:**

{chr(10).join([f'**{i+1}. {p[:150]}**{chr(10)}[Expandir com 2-3 parágrafos]{chr(10)}' for i, p in enumerate(points)])}

---

**Para você aplicar hoje:**

1. [Ação prática 1]
2. [Ação prática 2]
3. [Ação prática 3]

---

O que achou desse conteúdo? Responde esse email, adoro ouvir de você!

Abraço,
[SEU NOME]

P.S.: Se conhece alguém que precisa ler isso, encaminha esse email!

---
⏱️ Tempo de leitura: {read_time} min"""

    return {
        "platform": "Email Newsletter",
        "email": email,
        "subject_options": [
            title,
            f"[Novo] {title}",
            f"Sobre {title.lower()[:30]}...",
        ],
        "tempo_leitura": f"{read_time} min"
    }


def to_youtube_script(text: str) -> Dict:
    """Converte para roteiro de YouTube."""
    title = extract_title(text)
    points = extract_key_points(text, 5)

    script = f"""📹 ROTEIRO YOUTUBE: {title}

═══════════════════════════════════════════
DADOS DO VÍDEO
═══════════════════════════════════════════
Título sugerido: {title}
Duração estimada: {len(points) * 3 + 5} minutos
Público: [definir]

═══════════════════════════════════════════
HOOK (0:00 - 0:30)
═══════════════════════════════════════════
"{title}. E se eu te dissesse que a maioria das pessoas faz isso completamente errado?

Nos próximos minutos, vou te mostrar exatamente [promessa].

Fica até o final que tem [bônus/dica especial]."

═══════════════════════════════════════════
INTRO (0:30 - 2:00)
═══════════════════════════════════════════
[Apresentação + contexto do tema]

"Se você [situação do viewer], esse vídeo é pra você.

Hoje você vai aprender:
{chr(10).join([f'• {p[:50]}...' for p in points])}

Se inscreve e ativa o sininho pra não perder."

═══════════════════════════════════════════
CONTEÚDO
═══════════════════════════════════════════

{chr(10).join([f'''
--- PONTO {i+1} ({(i*3)+2}:00 - {(i*3)+5}:00) ---
Título: {p[:60]}

[Explicar conceito]

[Dar exemplo prático]

[Mostrar aplicação]

[Transição para próximo ponto]
''' for i, p in enumerate(points)])}

═══════════════════════════════════════════
FECHAMENTO
═══════════════════════════════════════════
"Então, pra resumir:
{chr(10).join([f'{i+1}. {p[:40]}...' for i, p in enumerate(points)])}

Se gostou, deixa o like e se inscreve.

Assiste esse vídeo aqui que complementa [apontar para card]."

═══════════════════════════════════════════
NOTAS DE PRODUÇÃO
═══════════════════════════════════════════
- Thumbnail: [ideia]
- B-roll necessário: [lista]
- Gráficos/textos: [lista]
"""

    return {
        "platform": "YouTube",
        "script": script,
        "duracao_estimada": f"{len(points) * 3 + 5} minutos",
        "estrutura": f"Hook + Intro + {len(points)} pontos + Fechamento"
    }


def repurpose_all(text: str) -> Dict:
    """Gera todas as versões."""
    return {
        "original": {
            "title": extract_title(text),
            "key_points": extract_key_points(text),
            "read_time": estimate_read_time(text)
        },
        "instagram_carousel": to_instagram_carousel(text),
        "instagram_reels": to_instagram_reels(text),
        "twitter_thread": to_twitter_thread(text),
        "linkedin": to_linkedin_post(text),
        "email": to_email_newsletter(text),
        "youtube": to_youtube_script(text)
    }


def print_output(result: Dict, platform: str = None):
    """Imprime o resultado formatado."""
    print("\n" + "="*60)
    print("📦 CONTENT REPURPOSER")
    print("="*60)

    if platform and platform != "todos":
        # Mostrar apenas uma plataforma
        data = result.get(platform, result.get(f"instagram_{platform}"))
        if data:
            print(f"\n📱 {data.get('platform', platform.upper())}")
            print("-"*60)

            if "slides" in data:
                for slide in data["slides"]:
                    print(f"\n[Slide {slide['slide']} - {slide['type'].upper()}]")
                    print(slide["content"])
                print(f"\n📝 CAPTION:\n{data['caption']}")

            elif "script" in data:
                print(data["script"])

            elif "tweets" in data:
                for tweet in data["tweets"]:
                    print(f"\n[Tweet {tweet['number']}] ({tweet['chars']} chars)")
                    print(tweet["content"])

            elif "post" in data:
                print(data["post"])

            elif "email" in data:
                print(data["email"])

    else:
        # Mostrar resumo de todos
        print(f"\n📝 CONTEÚDO ORIGINAL:")
        print(f"   Título: {result['original']['title']}")
        print(f"   Pontos-chave: {len(result['original']['key_points'])}")
        print(f"   Tempo de leitura: {result['original']['read_time']} min")

        print("\n📱 VERSÕES GERADAS:")
        print("-"*60)

        platforms = [
            ("instagram_carousel", "Instagram Carrossel", f"{result['instagram_carousel']['total_slides']} slides"),
            ("instagram_reels", "Instagram Reels", result['instagram_reels']['duracao_sugerida']),
            ("twitter_thread", "Twitter/X Thread", f"{result['twitter_thread']['total_tweets']} tweets"),
            ("linkedin", "LinkedIn Post", f"{result['linkedin']['chars']} chars"),
            ("email", "Email Newsletter", result['email']['tempo_leitura']),
            ("youtube", "YouTube Script", result['youtube']['duracao_estimada'])
        ]

        for key, name, detail in platforms:
            print(f"   ✅ {name}: {detail}")

        print("\n💡 Use --output [plataforma] para ver versão específica")
        print("   Opções: carousel, reels, twitter, linkedin, email, youtube")

    print("\n" + "="*60)


def main():
    parser = argparse.ArgumentParser(description="Adapta conteúdo entre plataformas")
    parser.add_argument("text", nargs="*", help="Texto para adaptar")
    parser.add_argument("--file", "-f", help="Arquivo de texto")
    parser.add_argument("--output", "-o", default="todos",
                        help="Plataforma: carousel, reels, twitter, linkedin, email, youtube, todos")

    args = parser.parse_args()

    text = ""

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif args.text:
        text = " ".join(args.text)
    else:
        print("Uso: python content_repurposer.py --file artigo.txt --output todos")
        print("     python content_repurposer.py \"Texto aqui\" --output twitter")
        sys.exit(1)

    if len(text) < 100:
        print("❌ Texto muito curto (mínimo 100 caracteres)")
        sys.exit(1)

    result = repurpose_all(text)
    print_output(result, args.output)


if __name__ == "__main__":
    main()
