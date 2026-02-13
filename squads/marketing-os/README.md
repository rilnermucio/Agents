# Marketing OS Squad

> Sistema operacional completo de marketing digital com 17 subagentes especializados.

## Visao Geral

O Marketing OS e um squad AIOS que orquestra 17 subagentes para cobrir todo o ciclo de marketing digital: da pesquisa a execucao, da criacao a analise.

## Subagentes (17)

| Agente | Funcao Principal |
|--------|------------------|
| SEO Agent | Otimizacao para motores de busca |
| Copy Agent | Copywriting e textos persuasivos |
| Social Agent | Gestao de redes sociais |
| Video Agent | Producao de conteudo em video |
| Audio Agent | Producao de podcasts e audio |
| Email Agent | Email marketing e automacao |
| Ads Agent | Anuncios pagos (Meta, Google) |
| Analytics Agent | Metricas e analise de dados |
| Design Agent | Design grafico e visual |
| AI Tools Agent | Ferramentas de IA para marketing |
| Research Agent | Pesquisa de mercado e tendencias |
| Brand Agent | Branding e identidade de marca |
| Storytelling Agent | Narrativas e storytelling |
| Funnel Agent | Funis de vendas e conversao |
| Growth Agent | Growth hacking e crescimento |
| Launch Agent | Lancamento de produtos |
| Infoproduct Builder | Criacao de infoprodutos |

## Estrutura

```
squads/marketing-os/
├── squad.yaml           # Manifesto do squad
├── README.md            # Esta documentacao
├── config/
│   └── marketing-mcp.yaml   # Configuracao MCP para marketing
├── docs/
│   └── mcp-activation-guide.md   # Guia de ativacao dos MCPs
└── data/
    └── clones/          # Sistema de clones de experts
```

## Workflows Disponiveis

1. **Lancamento de Produto** - Workflow completo de go-to-market
2. **Calendario Mensal** - Planejamento editorial mensal
3. **Campanha de Conversao** - Campanhas focadas em conversao
4. **Batch Production** - Producao em lote de conteudo
5. **TikTok Trends** - Monitoramento de tendencias TikTok
6. **Parceria com Influencer** - Gestao de parcerias
7. **Funil de Vendas** - Construcao e otimizacao de funis

## Uso

```bash
# Listar squads
aios squad list

# Validar manifesto
aios squad validate squads/marketing-os

# Usar subagente via skill
/marketing-os
```

## Requisitos

- Node.js >= 18.0.0
- AIOS >= 2.1.0
- Python (para scripts auxiliares)

## Versao

v4.0.0 - Marketing OS Pro
