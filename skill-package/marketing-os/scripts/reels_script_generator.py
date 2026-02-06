#!/usr/bin/env python3
"""
Reels Script Generator
Gera roteiros completos para Reels com timestamps e direções de câmera.

Uso: python reels_script_generator.py "tema" duracao formato
Exemplo: python reels_script_generator.py "5 dicas de produtividade" 30 tutorial
"""

import sys
import random

# Estruturas por formato de Reels
ESTRUTURAS = {
    "tutorial": {
        "nome": "Tutorial/How-To",
        "estrutura": [
            {"tempo": "0-3s", "tipo": "HOOK", "descricao": "Promessa do resultado"},
            {"tempo": "3-7s", "tipo": "CONTEXTO", "descricao": "Por que isso importa"},
            {"tempo": "7-22s", "tipo": "CONTEÚDO", "descricao": "Passos do tutorial"},
            {"tempo": "22-27s", "tipo": "RESULTADO", "descricao": "Mostrar o resultado"},
            {"tempo": "27-30s", "tipo": "CTA", "descricao": "Chamada para ação"}
        ]
    },
    "listicle": {
        "nome": "Lista/Dicas",
        "estrutura": [
            {"tempo": "0-3s", "tipo": "HOOK", "descricao": "Número + promessa"},
            {"tempo": "3-8s", "tipo": "ITEM 1", "descricao": "Primeira dica + visual"},
            {"tempo": "8-13s", "tipo": "ITEM 2", "descricao": "Segunda dica + visual"},
            {"tempo": "13-18s", "tipo": "ITEM 3", "descricao": "Terceira dica + visual"},
            {"tempo": "18-23s", "tipo": "ITEM 4", "descricao": "Quarta dica + visual"},
            {"tempo": "23-28s", "tipo": "ITEM 5", "descricao": "Quinta dica + visual"},
            {"tempo": "28-30s", "tipo": "CTA", "descricao": "Salve para não esquecer"}
        ]
    },
    "storytime": {
        "nome": "Storytelling",
        "estrutura": [
            {"tempo": "0-3s", "tipo": "HOOK", "descricao": "Frase intrigante"},
            {"tempo": "3-10s", "tipo": "SETUP", "descricao": "Contexto da história"},
            {"tempo": "10-20s", "tipo": "CONFLITO", "descricao": "O problema/desafio"},
            {"tempo": "20-27s", "tipo": "RESOLUÇÃO", "descricao": "Como resolveu"},
            {"tempo": "27-30s", "tipo": "LIÇÃO/CTA", "descricao": "Aprendizado + CTA"}
        ]
    },
    "antes_depois": {
        "nome": "Antes e Depois",
        "estrutura": [
            {"tempo": "0-3s", "tipo": "HOOK", "descricao": "Teaser do resultado"},
            {"tempo": "3-10s", "tipo": "ANTES", "descricao": "Mostrar situação inicial"},
            {"tempo": "10-12s", "tipo": "TRANSIÇÃO", "descricao": "Efeito de transição"},
            {"tempo": "12-25s", "tipo": "DEPOIS", "descricao": "Resultado transformado"},
            {"tempo": "25-30s", "tipo": "CTA", "descricao": "Como conseguir também"}
        ]
    },
    "pov": {
        "nome": "POV (Point of View)",
        "estrutura": [
            {"tempo": "0-3s", "tipo": "SETUP POV", "descricao": "POV: [situação]"},
            {"tempo": "3-25s", "tipo": "CENA", "descricao": "Atuar a situação"},
            {"tempo": "25-30s", "tipo": "REAÇÃO/CTA", "descricao": "Reação final + CTA"}
        ]
    },
    "trend": {
        "nome": "Trend Adaptada",
        "estrutura": [
            {"tempo": "0-2s", "tipo": "SYNC", "descricao": "Sincronizar com áudio"},
            {"tempo": "2-25s", "tipo": "CONTEÚDO", "descricao": "Adaptar trend ao nicho"},
            {"tempo": "25-30s", "tipo": "TWIST/CTA", "descricao": "Plot twist ou CTA"}
        ]
    },
    "problema_solucao": {
        "nome": "Problema → Solução",
        "estrutura": [
            {"tempo": "0-3s", "tipo": "HOOK", "descricao": "Identificar a dor"},
            {"tempo": "3-10s", "tipo": "PROBLEMA", "descricao": "Aprofundar o problema"},
            {"tempo": "10-12s", "tipo": "VIRADA", "descricao": "Mas existe solução..."},
            {"tempo": "12-25s", "tipo": "SOLUÇÃO", "descricao": "Apresentar a solução"},
            {"tempo": "25-30s", "tipo": "CTA", "descricao": "Como acessar"}
        ]
    },
    "react": {
        "nome": "React/Dueto",
        "estrutura": [
            {"tempo": "0-2s", "tipo": "CONTEXTO", "descricao": "Mostrar o que vai reagir"},
            {"tempo": "2-20s", "tipo": "REAÇÃO", "descricao": "Sua reação autêntica"},
            {"tempo": "20-27s", "tipo": "OPINIÃO", "descricao": "Seu ponto de vista"},
            {"tempo": "27-30s", "tipo": "CTA", "descricao": "E você, concorda?"}
        ]
    }
}

# Hooks por categoria
HOOKS = {
    "curiosidade": [
        "Você não vai acreditar no que eu descobri sobre {tema}",
        "Isso mudou completamente minha visão sobre {tema}",
        "Por que ninguém fala sobre isso?",
        "O segredo que {especialistas} não contam",
        "Eu estava fazendo {tema} completamente errado"
    ],
    "promessa": [
        "Em {tempo} você vai dominar {tema}",
        "{Número} passos para {resultado}",
        "Como eu {resultado} em apenas {tempo}",
        "O método que me fez {resultado}",
        "Aprenda {tema} de uma vez por todas"
    ],
    "controversia": [
        "Opinião impopular sobre {tema}",
        "Por que eu discordo de {crença comum}",
        "A verdade que ninguém quer ouvir sobre {tema}",
        "Isso vai irritar muita gente, mas...",
        "{Crença popular} está completamente errada"
    ],
    "identificacao": [
        "Se você {situação}, assiste até o final",
        "Isso é para você que {problema}",
        "Só entende quem {situação}",
        "Você também passa por isso?",
        "POV: você finalmente descobriu {solução}"
    ],
    "resultado": [
        "Foi assim que eu {resultado impressionante}",
        "De {antes} para {depois} em {tempo}",
        "O antes e depois que ninguém esperava",
        "Olha o que aconteceu quando eu {ação}",
        "Esse é o resultado de {período} de {ação}"
    ]
}

# CTAs por objetivo
CTAS = {
    "engajamento": [
        "Comenta aqui qual foi sua favorita 👇",
        "Marca alguém que precisa ver isso",
        "Concorda? Comenta SIM ou NÃO",
        "Qual dica você vai aplicar primeiro?",
        "Me conta nos comentários sua experiência"
    ],
    "salvamento": [
        "Salva pra não esquecer 📌",
        "Guarda esse vídeo pra consultar depois",
        "Salva e compartilha com quem precisa",
        "Esse vídeo é pra salvar e rever",
        "Salva antes que suma do feed"
    ],
    "seguidores": [
        "Segue pra mais conteúdo sobre {tema}",
        "Me segue pra não perder as próximas dicas",
        "Se foi útil, me segue ✓",
        "Sigo postando sobre {tema}, me acompanha",
        "Segue e ativa o sininho 🔔"
    ],
    "conversao": [
        "Link na bio pra saber mais",
        "Quer o passo a passo completo? Link na bio",
        "Comenta '{palavra}' que eu te mando",
        "Clica no link da bio e garante o seu",
        "Me chama no direct pra saber mais"
    ]
}

# Direções de câmera
DIRECOES_CAMERA = [
    "🎬 Close no rosto falando para câmera",
    "🎬 Plano médio mostrando gesticulação",
    "🎬 Plano aberto mostrando ambiente",
    "🎬 Insert/B-roll do produto/tela",
    "🎬 Transição com movimento de câmera",
    "🎬 Selfie casual/autêntica",
    "🎬 Time-lapse do processo",
    "🎬 Slow motion no momento chave",
    "🎬 Split screen antes/depois",
    "🎬 Texto na tela com narração"
]

def gerar_roteiro(tema: str, duracao: int, formato: str) -> dict:
    """Gera roteiro completo para Reels."""

    if formato not in ESTRUTURAS:
        formato = "tutorial"  # Default

    estrutura = ESTRUTURAS[formato]

    # Selecionar hooks e CTAs
    categoria_hook = random.choice(list(HOOKS.keys()))
    hook = random.choice(HOOKS[categoria_hook]).format(
        tema=tema,
        tempo="30 segundos",
        resultado="transformar sua rotina",
        especialistas="os experts",
        crença_comum="todo mundo",
        situação="luta com isso",
        problema="enfrenta esse desafio",
        solução="a solução",
        antes="0",
        depois="100",
        ação="aplicar isso",
        período="30 dias",
        Número="5"
    )

    categoria_cta = random.choice(list(CTAS.keys()))
    cta = random.choice(CTAS[categoria_cta]).format(tema=tema, palavra="EU QUERO")

    # Montar roteiro
    roteiro = {
        "tema": tema,
        "formato": estrutura["nome"],
        "duracao": f"{duracao} segundos",
        "estrutura": [],
        "hook_sugerido": hook,
        "cta_sugerido": cta,
        "direcoes_camera": random.sample(DIRECOES_CAMERA, min(5, len(estrutura["estrutura"])))
    }

    # Ajustar tempos baseado na duração
    fator = duracao / 30  # Base é 30 segundos

    for i, parte in enumerate(estrutura["estrutura"]):
        # Parse tempo original
        tempo_original = parte["tempo"]

        roteiro["estrutura"].append({
            "tempo": tempo_original,
            "tipo": parte["tipo"],
            "descricao": parte["descricao"],
            "direcao": roteiro["direcoes_camera"][i] if i < len(roteiro["direcoes_camera"]) else "🎬 Plano à escolha"
        })

    return roteiro

def formatar_saida(roteiro: dict) -> str:
    """Formata o roteiro para exibição."""

    saida = f"""
╔══════════════════════════════════════════════════════════════╗
║              🎬 ROTEIRO PARA REELS                           ║
╠══════════════════════════════════════════════════════════════╣
║ Tema: {roteiro['tema'][:50]}
║ Formato: {roteiro['formato']}
║ Duração: {roteiro['duracao']}
╚══════════════════════════════════════════════════════════════╝

📌 HOOK SUGERIDO:
"{roteiro['hook_sugerido']}"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ESTRUTURA DO ROTEIRO:

"""

    for parte in roteiro["estrutura"]:
        saida += f"""┌─ [{parte['tempo']}] {parte['tipo']}
│  📝 {parte['descricao']}
│  {parte['direcao']}
└──────────────────────────────────────────

"""

    saida += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 CTA SUGERIDO:
"{roteiro['cta_sugerido']}"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 DICAS DE GRAVAÇÃO:
• Grave na vertical (9:16)
• Use boa iluminação (luz natural é ideal)
• Áudio limpo (use microfone se possível)
• Adicione legendas (85% assiste sem som)
• Mantenha energia alta nos primeiros 3 segundos
• Use transições dinâmicas entre partes

🎵 SUGESTÃO DE ÁUDIO:
• Para {roteiro['formato']}: Use áudio trending ou narração própria
• Verifique músicas em alta no Instagram

"""

    return saida

def listar_formatos():
    """Lista todos os formatos disponíveis."""

    print("\n📚 FORMATOS DE REELS DISPONÍVEIS:\n")
    for key, value in ESTRUTURAS.items():
        print(f"  • {key}: {value['nome']}")
    print()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        listar_formatos()
        return

    if sys.argv[1] == "--formatos":
        listar_formatos()
        return

    tema = sys.argv[1]
    duracao = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    formato = sys.argv[3] if len(sys.argv) > 3 else "tutorial"

    # Validar duração
    if duracao not in [15, 30, 60, 90]:
        print("⚠️  Durações recomendadas: 15, 30, 60 ou 90 segundos")
        duracao = 30

    roteiro = gerar_roteiro(tema, duracao, formato)
    print(formatar_saida(roteiro))

if __name__ == "__main__":
    main()
