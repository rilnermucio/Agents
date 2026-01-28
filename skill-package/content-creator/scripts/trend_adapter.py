#!/usr/bin/env python3
"""
Trend Adapter
Adapta trends virais para diferentes nichos de conteúdo.

Uso: python trend_adapter.py "trend" nicho
Exemplo: python trend_adapter.py "get ready with me" marketing
"""

import sys
import random

# Trends adaptáveis com estrutura
TRENDS = {
    "get_ready_with_me": {
        "nome": "Get Ready With Me (GRWM)",
        "original": "Mostrar rotina de preparação enquanto conversa",
        "estrutura": ["Setup (ambiente)", "Ação (se preparando)", "Conversa paralela", "Resultado final"],
        "duracao": "60-90 segundos",
        "audio": "Música trending ou voiceover"
    },
    "day_in_my_life": {
        "nome": "Day in My Life",
        "original": "Mostrar um dia típico na sua rotina",
        "estrutura": ["Manhã", "Trabalho/atividade principal", "Tarde/pausa", "Noite", "Reflexão"],
        "duracao": "60-90 segundos",
        "audio": "Música aesthetic ou narração"
    },
    "things_i_wish": {
        "nome": "Things I Wish I Knew",
        "original": "Compartilhar aprendizados tardios",
        "estrutura": ["Hook: 'Coisas que eu queria ter sabido...'", "Lista de insights", "Conclusão"],
        "duracao": "30-60 segundos",
        "audio": "Música emocional ou voiceover"
    },
    "hot_takes": {
        "nome": "Hot Takes / Opiniões Impopulares",
        "original": "Compartilhar opinião controversa",
        "estrutura": ["Statement forte", "Justificativa", "Prova/exemplo", "CTA para debate"],
        "duracao": "15-30 segundos",
        "audio": "Som trending de 'hot take'"
    },
    "pov": {
        "nome": "POV (Point of View)",
        "original": "Encenar situação do ponto de vista do viewer",
        "estrutura": ["Setup: 'POV: você...'", "Cena/reação", "Plot twist (opcional)"],
        "duracao": "15-30 segundos",
        "audio": "Som específico do POV"
    },
    "expectativa_realidade": {
        "nome": "Expectativa vs Realidade",
        "original": "Comparar idealização com realidade",
        "estrutura": ["Expectativa (glamour)", "Transição", "Realidade (humor)"],
        "duracao": "15-30 segundos",
        "audio": "Som de transição"
    },
    "storytime": {
        "nome": "Storytime",
        "original": "Contar história envolvente",
        "estrutura": ["Hook dramático", "Contexto", "Conflito", "Clímax", "Resolução"],
        "duracao": "60-180 segundos",
        "audio": "Voiceover com música de fundo"
    },
    "tutorial_rapido": {
        "nome": "Tutorial Rápido",
        "original": "Ensinar algo de forma rápida e dinâmica",
        "estrutura": ["Resultado primeiro", "Passo a passo rápido", "Resultado de novo"],
        "duracao": "15-30 segundos",
        "audio": "Som trending upbeat"
    },
    "antes_depois": {
        "nome": "Antes e Depois",
        "original": "Mostrar transformação",
        "estrutura": ["Antes (problema)", "Transição mágica", "Depois (resultado)"],
        "duracao": "15-30 segundos",
        "audio": "Som de transição épico"
    },
    "react": {
        "nome": "React / Dueto",
        "original": "Reagir a outro conteúdo",
        "estrutura": ["Mostrar conteúdo original", "Sua reação/opinião", "Comentário final"],
        "duracao": "30-60 segundos",
        "audio": "Original do vídeo + sua voz"
    },
    "ranking": {
        "nome": "Ranking / Tier List",
        "original": "Classificar itens de melhor a pior",
        "estrutura": ["Apresentar categorias", "Classificar cada item", "Justificar posições", "Pedir opinião"],
        "duracao": "30-60 segundos",
        "audio": "Música ou voiceover"
    },
    "silent_vlog": {
        "nome": "Silent Vlog",
        "original": "Vlog sem narração, apenas visual e música",
        "estrutura": ["Sequência de clips estéticos", "Momentos do dia", "Visual satisfatório"],
        "duracao": "60-90 segundos",
        "audio": "Música lo-fi ou aesthetic"
    }
}

# Adaptações por nicho
ADAPTACOES = {
    "marketing": {
        "get_ready_with_me": "GRWM para criar uma campanha / preparar uma reunião com cliente",
        "day_in_my_life": "Um dia na vida de um profissional de marketing digital",
        "things_i_wish": "Coisas que eu queria saber antes de começar no marketing",
        "hot_takes": "Opinião impopular: [estratégia controversa] funciona melhor",
        "pov": "POV: seu cliente pediu um viral 'igual aquele do TikTok'",
        "expectativa_realidade": "Expectativa de trabalhar com marketing vs realidade",
        "storytime": "Como um erro de campanha quase me custou o cliente",
        "tutorial_rapido": "Como criar uma copy que converte em 30 segundos",
        "antes_depois": "Antes e depois de otimizar os ads do cliente",
        "react": "Reagindo a anúncios famosos / erros de marketing",
        "ranking": "Ranking das melhores ferramentas de marketing",
        "silent_vlog": "Um dia de trabalho remoto em marketing"
    },
    "empreendedorismo": {
        "get_ready_with_me": "GRWM para pitch com investidor / reunião importante",
        "day_in_my_life": "Um dia na vida de um empreendedor",
        "things_i_wish": "O que eu gostaria de saber antes de abrir meu negócio",
        "hot_takes": "Opinião impopular sobre empreendedorismo",
        "pov": "POV: você acabou de receber seu primeiro cliente",
        "expectativa_realidade": "Expectativa de empreender vs realidade",
        "storytime": "Como quase falei no primeiro ano de empresa",
        "tutorial_rapido": "Como validar uma ideia de negócio em 30 segundos",
        "antes_depois": "Antes e depois de pivotar o modelo de negócio",
        "react": "Reagindo a erros clássicos de empreendedores",
        "ranking": "Ranking de habilidades essenciais para empreender",
        "silent_vlog": "Rotina de trabalho como empreendedor"
    },
    "produtividade": {
        "get_ready_with_me": "GRWM para um dia super produtivo",
        "day_in_my_life": "Um dia seguindo minha rotina de alta performance",
        "things_i_wish": "Hacks de produtividade que eu queria ter descoberto antes",
        "hot_takes": "Opinião impopular: [técnica famosa] não funciona",
        "pov": "POV: você finalmente encontrou sua rotina ideal",
        "expectativa_realidade": "Expectativa do trabalho remoto vs realidade",
        "storytime": "Como eu saí de procrastinador para produtivo",
        "tutorial_rapido": "Como organizar sua semana em 30 segundos",
        "antes_depois": "Antes e depois de implementar time blocking",
        "react": "Reagindo a rotinas virais de produtividade",
        "ranking": "Ranking das melhores técnicas de produtividade",
        "silent_vlog": "Minha rotina matinal de alta performance"
    },
    "tech": {
        "get_ready_with_me": "GRWM para codar um projeto novo",
        "day_in_my_life": "Um dia na vida de um dev/tech lead",
        "things_i_wish": "O que eu queria saber antes de entrar em tech",
        "hot_takes": "Opinião impopular: [tecnologia] está supervalorizada",
        "pov": "POV: o bug era um ponto e vírgula",
        "expectativa_realidade": "Expectativa de trabalhar com tech vs realidade",
        "storytime": "O bug que me fez ficar 3 dias sem dormir",
        "tutorial_rapido": "Dica de código que vai mudar sua vida",
        "antes_depois": "Antes e depois de refatorar o código",
        "react": "Reagindo a código de iniciantes / código legado",
        "ranking": "Ranking das melhores linguagens para 2024",
        "silent_vlog": "Coding session aesthetic"
    },
    "financas": {
        "get_ready_with_me": "GRWM para revisar minhas finanças do mês",
        "day_in_my_life": "Um dia gerenciando investimentos",
        "things_i_wish": "O que eu queria saber sobre dinheiro aos 20",
        "hot_takes": "Opinião impopular sobre investimentos",
        "pov": "POV: você finalmente zerou suas dívidas",
        "expectativa_realidade": "Expectativa de investir vs realidade",
        "storytime": "Como eu saí das dívidas para a reserva de emergência",
        "tutorial_rapido": "Como fazer um orçamento em 30 segundos",
        "antes_depois": "Antes e depois de organizar as finanças",
        "react": "Reagindo a dicas financeiras da internet",
        "ranking": "Ranking dos melhores investimentos para iniciantes",
        "silent_vlog": "Minha rotina de controle financeiro"
    },
    "lifestyle": {
        "get_ready_with_me": "GRWM clássico com dicas de skincare/moda",
        "day_in_my_life": "Um dia na minha vida [aesthetic]",
        "things_i_wish": "Coisas que eu queria ter aprendido antes",
        "hot_takes": "Opinião impopular sobre [tendência]",
        "pov": "POV: quando você finalmente tem sua rotina perfeita",
        "expectativa_realidade": "Expectativa de vida adulta vs realidade",
        "storytime": "A história mais louca que já aconteceu comigo",
        "tutorial_rapido": "Hack de organização que mudou minha vida",
        "antes_depois": "Transformação do quarto/casa/rotina",
        "react": "Reagindo a trends de lifestyle",
        "ranking": "Ranking das minhas coisas favoritas do momento",
        "silent_vlog": "Um dia aesthetic na minha vida"
    },
    "educacao": {
        "get_ready_with_me": "GRWM para estudar / preparar aula",
        "day_in_my_life": "Um dia na vida de professor/estudante",
        "things_i_wish": "O que eu queria saber antes de começar a estudar [área]",
        "hot_takes": "Opinião impopular sobre educação/estudos",
        "pov": "POV: você finalmente entendeu aquele conceito difícil",
        "expectativa_realidade": "Expectativa de estudar vs realidade",
        "storytime": "Como eu passei em [prova difícil]",
        "tutorial_rapido": "Técnica de estudo em 30 segundos",
        "antes_depois": "Antes e depois do método de estudo",
        "react": "Reagindo a métodos de estudo virais",
        "ranking": "Ranking das melhores técnicas de memorização",
        "silent_vlog": "Study with me"
    }
}

def adaptar_trend(trend_key: str, nicho: str) -> dict:
    """Adapta uma trend para o nicho especificado."""

    if trend_key not in TRENDS:
        # Tentar encontrar trend similar
        for key in TRENDS:
            if trend_key.lower() in key or key in trend_key.lower():
                trend_key = key
                break
        else:
            trend_key = "tutorial_rapido"  # Default

    if nicho not in ADAPTACOES:
        nicho = "lifestyle"  # Default

    trend = TRENDS[trend_key]
    adaptacao = ADAPTACOES[nicho].get(trend_key, f"Adapte '{trend['nome']}' para seu nicho")

    resultado = {
        "trend": trend,
        "nicho": nicho,
        "adaptacao": adaptacao,
        "ideias_adicionais": gerar_ideias_adicionais(trend_key, nicho)
    }

    return resultado

def gerar_ideias_adicionais(trend_key: str, nicho: str) -> list:
    """Gera ideias adicionais de adaptação."""

    ideias_base = {
        "get_ready_with_me": [
            f"GRWM para evento importante do seu nicho",
            f"GRWM mostrando ferramentas que usa no trabalho",
            f"GRWM com dicas rápidas enquanto se prepara"
        ],
        "day_in_my_life": [
            f"Versão 'caótica' vs versão 'organizada'",
            f"Comparar dias diferentes (segunda vs sexta)",
            f"Focar em um aspecto específico do dia"
        ],
        "things_i_wish": [
            f"Versão por 'idade' (aos 20, aos 25, aos 30)",
            f"Focar em erros específicos que cometeu",
            f"Coisas que ninguém te conta sobre [área]"
        ],
        "hot_takes": [
            f"Responder hot takes populares do nicho",
            f"Hot takes que mudaram de opinião",
            f"Hot takes vs realidade"
        ],
        "pov": [
            f"POV de diferentes personas do nicho",
            f"POV de situações engraçadas/relatable",
            f"POV de conquistas/momentos especiais"
        ]
    }

    return ideias_base.get(trend_key, [
        f"Adicione seu toque único de {nicho}",
        "Combine com outra trend popular",
        "Faça versão em série (parte 1, 2, 3)"
    ])

def formatar_saida(resultado: dict) -> str:
    """Formata o resultado para exibição."""

    trend = resultado["trend"]

    saida = f"""
╔══════════════════════════════════════════════════════════════════╗
║              🎯 TREND ADAPTER                                     ║
╠══════════════════════════════════════════════════════════════════╣
║ Trend: {trend['nome']}
║ Nicho: {resultado['nicho'].capitalize()}
╚══════════════════════════════════════════════════════════════════╝

📌 SOBRE A TREND:
{trend['original']}

⏱️  Duração recomendada: {trend['duracao']}
🎵 Áudio: {trend['audio']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ESTRUTURA:

"""

    for i, parte in enumerate(trend["estrutura"], 1):
        saida += f"  {i}. {parte}\n"

    saida += f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎨 ADAPTAÇÃO PARA {resultado['nicho'].upper()}:

"{resultado['adaptacao']}"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 IDEIAS ADICIONAIS:

"""

    for ideia in resultado["ideias_adicionais"]:
        saida += f"  • {ideia}\n"

    saida += f"""

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 DICAS PARA VIRALIZAR:

• Faça nas primeiras 24-48h da trend estar em alta
• Adicione seu twist único - não copie, adapte
• Use o áudio original da trend (aumenta distribuição)
• Mantenha a estrutura, mude o conteúdo
• Engaje com outros criadores usando a mesma trend
• Poste no horário de maior engajamento do seu perfil

📱 ONDE ENCONTRAR TRENDS:
• TikTok → Aba "Descobrir"
• Instagram → Aba "Reels"
• YouTube → "Shorts em alta"
• Google Trends
• Observar criadores do seu nicho

"""

    return saida

def listar_trends():
    """Lista todas as trends disponíveis."""

    print("\n📚 TRENDS DISPONÍVEIS:\n")
    for key, value in TRENDS.items():
        print(f"  • {key}: {value['nome']}")
    print()

def listar_nichos():
    """Lista todos os nichos disponíveis."""

    print("\n🎯 NICHOS DISPONÍVEIS:\n")
    for nicho in ADAPTACOES.keys():
        print(f"  • {nicho}")
    print()

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        listar_trends()
        listar_nichos()
        return

    if sys.argv[1] == "--trends":
        listar_trends()
        return

    if sys.argv[1] == "--nichos":
        listar_nichos()
        return

    trend_input = sys.argv[1].lower().replace(" ", "_").replace("-", "_")
    nicho = sys.argv[2].lower() if len(sys.argv) > 2 else "lifestyle"

    resultado = adaptar_trend(trend_input, nicho)
    print(formatar_saida(resultado))

if __name__ == "__main__":
    main()
