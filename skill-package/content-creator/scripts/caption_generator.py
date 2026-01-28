#!/usr/bin/env python3
"""
Caption Generator
Gera legendas otimizadas para Instagram por objetivo.

Uso: python caption_generator.py "tema" objetivo
Exemplo: python caption_generator.py "produtividade" engajamento
"""

import sys
import random

# Estruturas de legenda por objetivo
ESTRUTURAS = {
    "engajamento": {
        "nome": "Legenda para Engajamento",
        "formato": [
            "HOOK (primeira linha)",
            "CONTEXTO (2-3 linhas)",
            "PERGUNTA ENGAJADORA",
            "HASHTAGS"
        ],
        "tamanho": "curta-média (100-200 palavras)"
    },
    "educativo": {
        "nome": "Legenda Educativa",
        "formato": [
            "HOOK com promessa",
            "INTRODUÇÃO do problema",
            "CONTEÚDO (bullets ou lista)",
            "CONCLUSÃO com insight",
            "CTA para salvar",
            "HASHTAGS"
        ],
        "tamanho": "média-longa (200-400 palavras)"
    },
    "storytelling": {
        "nome": "Legenda Storytelling",
        "formato": [
            "HOOK emocional",
            "SETUP da história",
            "CONFLITO/DESAFIO",
            "VIRADA",
            "RESOLUÇÃO",
            "LIÇÃO/MORAL",
            "CTA emocional",
            "HASHTAGS"
        ],
        "tamanho": "longa (300-500 palavras)"
    },
    "vendas": {
        "nome": "Legenda de Vendas",
        "formato": [
            "HOOK com benefício",
            "IDENTIFICAÇÃO do problema",
            "AGITAÇÃO da dor",
            "SOLUÇÃO (produto)",
            "PROVA SOCIAL",
            "OFERTA + URGÊNCIA",
            "CTA direto",
            "HASHTAGS"
        ],
        "tamanho": "média (200-300 palavras)"
    },
    "autoridade": {
        "nome": "Legenda de Autoridade",
        "formato": [
            "HOOK controverso/opinião",
            "POSICIONAMENTO claro",
            "ARGUMENTOS/EVIDÊNCIAS",
            "EXPERIÊNCIA pessoal",
            "CONCLUSÃO forte",
            "CTA para debate",
            "HASHTAGS"
        ],
        "tamanho": "média (200-300 palavras)"
    },
    "conexao": {
        "nome": "Legenda de Conexão",
        "formato": [
            "HOOK vulnerável",
            "COMPARTILHAR experiência",
            "SENTIMENTOS/EMOÇÕES",
            "NORMALIZAR",
            "MENSAGEM de apoio",
            "PERGUNTA para conectar",
            "HASHTAGS"
        ],
        "tamanho": "média (150-250 palavras)"
    }
}

# Hooks por objetivo
HOOKS = {
    "engajamento": [
        "Isso vai gerar polêmica, mas preciso falar...",
        "Me conta se você também passa por isso 👇",
        "Vou te contar um segredo que pouca gente sabe...",
        "Você concorda ou discorda?",
        "Isso mudou completamente minha perspectiva sobre {tema}",
        "A verdade que ninguém quer admitir sobre {tema}",
        "Se você {situação}, precisa ler isso até o final"
    ],
    "educativo": [
        "{Número} coisas sobre {tema} que vão mudar sua vida",
        "O guia definitivo de {tema} em {tempo}",
        "Aprenda {tema} de uma vez por todas",
        "Os erros que 90% das pessoas cometem com {tema}",
        "O que eu queria ter aprendido antes sobre {tema}",
        "O método que transformou meu {área}",
        "Se você quer {resultado}, leia isso:"
    ],
    "storytelling": [
        "Tudo começou quando...",
        "Eu nunca tinha contado isso, mas...",
        "O dia em que tudo mudou",
        "Eu quase desisti de {tema}. Deixa eu te contar...",
        "Há {tempo} atrás, eu estava {situação difícil}",
        "Essa história me ensinou a lição mais importante da minha vida",
        "Hoje eu preciso compartilhar algo com vocês..."
    ],
    "vendas": [
        "Cansado(a) de {problema}? Tenho a solução.",
        "O que separa quem {resultado} de quem não consegue",
        "Imagine se você pudesse {benefício}...",
        "Eu estava exatamente onde você está agora",
        "Finalmente: {solução} que realmente funciona",
        "{Número} pessoas já {resultado} com isso",
        "Se {problema} está te impedindo de {objetivo}, leia isso:"
    ],
    "autoridade": [
        "Opinião impopular sobre {tema}:",
        "Depois de {tempo} trabalhando com {área}, posso afirmar:",
        "A maioria dos 'experts' está errada sobre isso",
        "Vou te contar o que {anos} de experiência me ensinaram",
        "Essa é a verdade que o mercado não quer que você saiba",
        "Por que eu discordo de {crença comum}",
        "{Número} anos fazendo {atividade} me mostraram que..."
    ],
    "conexao": [
        "Preciso ser honesto(a) com vocês...",
        "Hoje não está sendo um dia fácil...",
        "Quem mais já se sentiu assim?",
        "Isso é algo que eu demorei pra aceitar...",
        "Se você está passando por isso, quero que saiba que...",
        "Às vezes a gente precisa ouvir que tá tudo bem não estar bem",
        "Uma coisa que eu gostaria de ter ouvido antes..."
    ]
}

# CTAs por objetivo
CTAS = {
    "engajamento": [
        "Me conta nos comentários: {pergunta}",
        "Concorda? Comenta 🙋 ou 🙅",
        "Marca alguém que precisa ver isso!",
        "Qual foi sua maior sacada? Comenta aqui 👇",
        "Deixa um 🔥 se você se identificou",
        "Compartilha com quem precisa ouvir isso",
        "E você, como lida com isso? Quero saber!"
    ],
    "educativo": [
        "Salva esse post para consultar depois 📌",
        "Qual dessas dicas você vai aplicar primeiro?",
        "Quer mais conteúdo assim? Me segue!",
        "Compartilha com alguém que está começando em {tema}",
        "Salva e compartilha para ajudar mais pessoas!",
        "Tem dúvidas? Comenta aqui que eu respondo",
        "Quer o passo a passo completo? Link na bio!"
    ],
    "storytelling": [
        "Você já passou por algo parecido? Me conta...",
        "O que essa história te fez pensar?",
        "Se isso tocou você, compartilha com alguém que precisa ler",
        "Qual lição você tira disso?",
        "Comenta um 💜 se você se conectou com essa história",
        "Às vezes a gente precisa compartilhar... obrigado por ler",
        "Se quiser mais histórias assim, me segue!"
    ],
    "vendas": [
        "Link na bio para saber mais!",
        "Comenta '{palavra}' que eu te mando os detalhes",
        "Vagas limitadas! Garanta a sua no link da bio",
        "Clica no link e aproveita a oferta especial",
        "Quer transformar seu {área}? Me chama no direct",
        "⚡ Oferta válida até {data}! Link na bio",
        "Já são +{número} pessoas transformadas. Você é o(a) próximo(a)?"
    ],
    "autoridade": [
        "Concorda ou discorda? Vamos debater nos comentários",
        "Qual sua opinião sobre isso? Quero saber!",
        "Se você pensa diferente, me conta o porquê",
        "Compartilha com alguém que precisa de outra perspectiva",
        "Comenta sua visão sobre {tema}",
        "Isso é só o começo... siga para mais insights",
        "Quer aprofundar? Link do artigo completo na bio"
    ],
    "conexao": [
        "Se você se identificou, deixa um 💙",
        "Me conta: como você lida com isso?",
        "Compartilha com alguém que precisa ler isso hoje",
        "Você não está sozinho(a). Comenta aqui 🤝",
        "Obrigado(a) por fazer parte da minha jornada",
        "Se precisar conversar, meu direct está aberto",
        "Juntos somos mais fortes. Deixa seu comentário!"
    ]
}

# Hashtags por nicho
HASHTAGS = {
    "geral": ["#conteudo", "#dicas", "#aprendizado", "#conhecimento", "#desenvolvimento"],
    "marketing": ["#marketingdigital", "#socialmedia", "#marketing", "#empreendedorismo", "#negocios"],
    "produtividade": ["#produtividade", "#gestaodotempo", "#foco", "#organizacao", "#habitos"],
    "carreira": ["#carreira", "#trabalho", "#emprego", "#profissional", "#crescimento"],
    "mindset": ["#mindset", "#mentalidade", "#motivacao", "#autoconhecimento", "#evolucao"],
    "financas": ["#financas", "#investimentos", "#dinheiro", "#educacaofinanceira", "#renda"],
    "saude": ["#saude", "#bemestar", "#vidasaudavel", "#qualidadedevida", "#equilibrio"],
    "tech": ["#tecnologia", "#inovacao", "#ia", "#futuro", "#digital"]
}

def gerar_legenda(tema: str, objetivo: str) -> dict:
    """Gera legenda completa baseada no objetivo."""

    if objetivo not in ESTRUTURAS:
        objetivo = "engajamento"

    estrutura = ESTRUTURAS[objetivo]

    # Selecionar hook e CTA
    hook = random.choice(HOOKS[objetivo]).format(
        tema=tema,
        Número=random.choice(["3", "5", "7", "10"]),
        tempo=random.choice(["30 dias", "1 semana", "6 meses"]),
        situação=f"lutando com {tema}",
        resultado="ter sucesso",
        área=tema,
        benefício=f"dominar {tema}",
        problema=f"dificuldade com {tema}",
        objetivo="seus objetivos",
        solução="a solução",
        anos=random.choice(["3", "5", "8", "10"]),
        atividade=tema,
        crença_comum="a maioria"
    )

    cta = random.choice(CTAS[objetivo]).format(
        pergunta=f"qual sua experiência com {tema}?",
        tema=tema,
        palavra="EU QUERO",
        área=tema,
        data="sexta-feira",
        número=random.choice(["500", "1.000", "5.000"])
    )

    # Selecionar hashtags
    nicho = "geral"
    for key in HASHTAGS:
        if key in tema.lower():
            nicho = key
            break

    hashtags_selecionadas = random.sample(HASHTAGS[nicho], 3) + random.sample(HASHTAGS["geral"], 2)

    resultado = {
        "tema": tema,
        "objetivo": objetivo,
        "estrutura": estrutura,
        "hook": hook,
        "cta": cta,
        "hashtags": hashtags_selecionadas
    }

    return resultado

def gerar_exemplo_completo(legenda: dict) -> str:
    """Gera um exemplo de legenda completa."""

    tema = legenda["tema"]
    objetivo = legenda["objetivo"]

    exemplos = {
        "engajamento": f"""{legenda['hook']}

Sério, isso é algo que eu penso muito...

{tema.capitalize()} é um assunto que divide opiniões, e eu entendo os dois lados. Mas depois de muito estudar e experimentar, cheguei a algumas conclusões que talvez te surpreendam.

O mais interessante é que a maioria das pessoas nem considera essa perspectiva...

{legenda['cta']}

.
.
.
{' '.join(legenda['hashtags'])}""",

        "educativo": f"""{legenda['hook']}

Vou compartilhar o que realmente funciona:

1️⃣ [Primeira dica/conceito sobre {tema}]
   → Por que funciona: [explicação breve]

2️⃣ [Segunda dica/conceito]
   → Aplicação prática: [exemplo]

3️⃣ [Terceira dica/conceito]
   → Erro comum: [o que evitar]

💡 Dica bônus: [insight adicional]

O segredo é consistência. Comece aplicando uma dessas dicas hoje mesmo.

{legenda['cta']}

.
.
.
{' '.join(legenda['hashtags'])}""",

        "storytelling": f"""{legenda['hook']}

Era 2019 e eu estava completamente perdido(a) com {tema}.

Tentava de tudo: cursos, livros, mentorias... Nada funcionava.

Um dia, aconteceu algo que mudou tudo. [momento da virada]

Percebi que o problema não era falta de conhecimento, era [insight].

Hoje, depois de aplicar isso consistentemente, [resultado].

A lição mais importante? [moral da história]

{legenda['cta']}

.
.
.
{' '.join(legenda['hashtags'])}""",

        "vendas": f"""{legenda['hook']}

Se você está cansado(a) de:
❌ [Dor 1 relacionada a {tema}]
❌ [Dor 2]
❌ [Dor 3]

Eu te entendo. Passei por tudo isso também.

Foi por isso que criei [produto/serviço].

✅ [Benefício 1]
✅ [Benefício 2]
✅ [Benefício 3]

Já são +[número] pessoas transformando seu [área] com isso.

🔥 E agora você tem a chance de fazer parte!

{legenda['cta']}

.
.
.
{' '.join(legenda['hashtags'])}""",

        "autoridade": f"""{legenda['hook']}

E vou te explicar o porquê.

Depois de [tempo] trabalhando com {tema}, percebi um padrão que poucos enxergam:

[Argumento 1 com evidência]

[Argumento 2 com experiência pessoal]

[Argumento 3 com dado/estatística]

Não estou dizendo que [contra-argumento], mas é fundamental considerar [ponto principal].

O que você acha?

{legenda['cta']}

.
.
.
{' '.join(legenda['hashtags'])}""",

        "conexao": f"""{legenda['hook']}

Esses últimos dias não têm sido fáceis com {tema}.

E eu sei que muitos de vocês também passam por isso.

Aquela sensação de [sentimento]...
De não saber se está no caminho certo...
De se perguntar "será que só eu?"

Não. Você não está sozinho(a).

Todo mundo que você admira já passou por isso em algum momento.

E tá tudo bem não ter todas as respostas agora.

O importante é não desistir. ❤️

{legenda['cta']}

.
.
.
{' '.join(legenda['hashtags'])}"""
    }

    return exemplos.get(objetivo, exemplos["engajamento"])

def formatar_saida(legenda: dict) -> str:
    """Formata a legenda para exibição."""

    saida = f"""
╔══════════════════════════════════════════════════════════════════╗
║              📝 GERADOR DE LEGENDAS                               ║
╠══════════════════════════════════════════════════════════════════╣
║ Tema: {legenda['tema'][:50]}
║ Objetivo: {legenda['estrutura']['nome']}
║ Tamanho ideal: {legenda['estrutura']['tamanho']}
╚══════════════════════════════════════════════════════════════════╝

📋 ESTRUTURA DA LEGENDA:

"""

    for i, parte in enumerate(legenda["estrutura"]["formato"], 1):
        saida += f"  {i}. {parte}\n"

    saida += f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎣 HOOK SUGERIDO:
"{legenda['hook']}"

🎯 CTA SUGERIDO:
"{legenda['cta']}"

#️⃣ HASHTAGS:
{' '.join(legenda['hashtags'])}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 EXEMPLO DE LEGENDA COMPLETA:

{gerar_exemplo_completo(legenda)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 DICAS:

• Primeira linha é o hook - tem que parar o scroll
• Use espaçamento para facilitar leitura
• Emojis com moderação (3-5 por legenda)
• Hashtags no final, separadas por pontos
• Limite: 2.200 caracteres (mas menos é mais)
• Use quebras de linha estratégicas
• Terminar sempre com pergunta aumenta comentários

"""

    return saida

def listar_objetivos():
    """Lista todos os objetivos disponíveis."""

    print("\n📚 OBJETIVOS DE LEGENDA DISPONÍVEIS:\n")
    for key, value in ESTRUTURAS.items():
        print(f"  • {key}: {value['nome']}")
    print()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        listar_objetivos()
        return

    if sys.argv[1] == "--objetivos":
        listar_objetivos()
        return

    tema = sys.argv[1]
    objetivo = sys.argv[2] if len(sys.argv) > 2 else "engajamento"

    legenda = gerar_legenda(tema, objetivo)
    print(formatar_saida(legenda))

if __name__ == "__main__":
    main()
