# Guia Completo de Uso - Marketing OS

Este guia apresenta todas as funcionalidades do Marketing OS e como utiliza-las de forma eficiente para criar conteúdo estrategico de alta qualidade.

---

## Indice

1. [Introducao](#introducao)
2. [Instalacao e Configuracao](#instalacao-e-configuracao)
3. [Como Funciona](#como-funciona)
4. [Os 11 Subagentes Especializados](#os-11-subagentes-especializados)
5. [Como Usar na Pratica](#como-usar-na-pratica)
6. [Scripts Python de Automacao](#scripts-python-de-automacao)
7. [Templates Disponiveis](#templates-disponiveis)
8. [Workflows de Campanha](#workflows-de-campanha)
9. [Recursos Adicionais](#recursos-adicionais)
10. [Referencia Rapida de Comandos](#referencia-rapida-de-comandos)
11. [Dicas e Melhores Praticas](#dicas-e-melhores-praticas)
12. [Troubleshooting](#troubleshooting)

---

## Introducao

O **Marketing OS** é um sistema operacional de marketing digital composto por 16 subagentes especializados que trabalham em conjunto para criar conteúdo estrategico. Ele foi projetado para funcionar como uma skill do Claude (Cowork/Claude Code).

### O que você pode fazer com este agente:

- Criar posts para redes sociais (Instagram, LinkedIn, Twitter/X, TikTok, YouTube, Pinterest, Facebook)
- Escrever artigos otimizados para SEO
- Desenvolver campanhas de email marketing
- Criar roteiros de video (YouTube, Reels, TikTok, VSL)
- Planejar podcasts e conteúdo de audio
- Gerar copy para anuncios (Meta Ads, Google Ads, TikTok Ads)
- Desenvolver landing pages e paginas de vendas
- Criar prompts para geracao de imagens e videos com IA
- Planejar calendarios editoriais completos
- Executar campanhas de lancamento

### Nichos Suportados:

| Nicho | Foco Principal | Tom Sugerido |
|-------|----------------|--------------|
| Inteligencia Artificial | Ferramentas, tutoriais, tendencias | Educativo, acessivel |
| Desenvolvimento Pessoal | Mindset, habitos, proposito | Inspiracional, empatico |
| Desenvolvimento Profissional | Carreira, skills, lideranca | Profissional, pratico |
| Tecnologia/Programacao | Codigo, tutoriais, carreira tech | Tecnico, didatico |
| Empreendedorismo | Negocios, vendas, escala | Motivador, estrategico |
| Financas Pessoais | Investimentos, renda, organizacao | Educativo, confiavel |
| Saude e Bem-Estar | Exercicio, nutricao, saude mental | Acolhedor, motivador |
| Educacao | Estudos, aprendizado, concursos | Didatico, encorajador |
| Produtividade | Tempo, foco, ferramentas | Pratico, direto |
| Marketing Digital | Estrategias, ferramentas, metricas | Autoridade, data-driven |

---

## Instalacao e Configuracao

### Metodo 1: Uso Direto no Cowork (Recomendado)

A forma mais simples - funciona imediatamente:

1. Abra o **Cowork** no Claude Desktop
2. Selecione a pasta `Marketing OS` como sua pasta de trabalho
3. Pronto! O Claude reconhecera automaticamente o `Skill.md`

### Metodo 2: Instalacao como Skill Global

Para ter o agente disponivel em qualquer pasta:

**macOS:**
```bash
cd ~/caminho/para/Agente\ Criador\ de\ Conteudo
unzip marketing-os.skill -d ~/Library/Application\ Support/Claude/skills/
```

**Windows:**
```powershell
cd C:\caminho\para\Marketing OS
Expand-Archive -Path marketing-os.skill -DestinationPath "$env:APPDATA\Claude\skills\"
```

**Linux:**
```bash
cd ~/caminho/para/Agente\ Criador\ de\ Conteudo
unzip marketing-os.skill -d ~/.config/claude/skills/
```

### Dependencias Python (Opcional)

Para usar os scripts de automacao:

```bash
pip install requests beautifulsoup4 pandas python-dotenv
```

Para o TikTok Trends Scraper (opcional):
```bash
pip install TikTokApi playwright
playwright install
```

---

## Como Funciona

### Arquitetura do Sistema

```
MARKETING OS (Agente Principal)
|
+-- RESEARCH AGENT      - Pesquisa de tendencias, concorrencia, keywords
+-- COPY AGENT          - Headlines, CTAs, copy persuasivo, variacoes A/B
+-- SEO AGENT           - Otimizacao on-page, estruturacao, E-E-A-T
+-- SOCIAL AGENT        - Posts por plataforma, hashtags, timing
+-- VIDEO AGENT         - Scripts YouTube, Reels, TikTok, VSL
+-- AI TOOLS AGENT      - Prompts para imagem e video com IA
+-- DESIGN AGENT        - Direcao criativa, paletas, layouts
+-- ANALYTICS AGENT     - Metricas, relatorios, testes A/B
+-- AUDIO AGENT         - Podcasts, roteiros de audio, spots
+-- EMAIL AGENT         - Sequencias de email, newsletters
+-- ADS AGENT           - Copy de anuncios Meta/Google/TikTok/LinkedIn
```

### Workflow Principal

1. **Entender o briefing** - Nicho, objetivo, publico-alvo, tom de voz
2. **Pesquisar** - Research Agent analisa tendencias e concorrencia
3. **Selecionar subagente** - Baseado no tipo de conteúdo
4. **Criar copy** - Copy Agent desenvolve textos persuasivos
5. **Definir visual** - Design Agent cria direcao criativa
6. **Otimizar** - SEO, hashtags, formatos
7. **Entregar** - Conteúdo formatado com variacoes A/B

### Triggers Automaticos

O agente e acionado quando você menciona palavras como:
- **Formatos:** post, blog, artigo, video, podcast, newsletter, landing page, carrossel, stories, reels
- **Plataformas:** Instagram, LinkedIn, Twitter/X, TikTok, YouTube, Pinterest
- **Acoes:** criar conteúdo, campanha, anuncio, copy, SEO, calendario editorial

---

## Os 11 Subagentes Especializados

### 1. Research Agent
**Arquivo:** `subagents/research-agent.md`

**Funcao:** Pesquisa de tendencias, analise de concorrencia, keyword research, mapeamento de audiencia.

**Quando usar:**
- Inicio de projeto com novo cliente/nicho
- Necessidade de dados atualizados
- Planejamento estrategico

**Exemplo de solicitacao:**
> "Pesquise as principais tendencias de conteúdo sobre IA em 2025"

---

### 2. Copy Agent
**Arquivo:** `subagents/copy-agent.md`

**Funcao:** Headlines, hooks, CTAs otimizados, copy de vendas, variacoes A/B.

**Frameworks disponíveis:**
- **AIDA** - Atencao > Interesse > Desejo > Acao
- **PAS** - Problema > Agitar > Solucao
- **BAB** - Antes > Depois > Ponte
- **4Ps** - Promessa > Imagem > Prova > Empurrao
- **QUEST** - Qualificar > Entender > Educar > Estimular > Transicionar

**Exemplo de solicitacao:**
> "Crie 5 variacoes de headline para um curso de produtividade"

---

### 3. SEO Agent
**Arquivo:** `subagents/seo-agent.md`

**Funcao:** Otimizacao on-page, estruturacao de conteúdo, meta tags, featured snippets, E-E-A-T.

**Quando usar:**
- Artigos de blog
- Landing pages
- Conteúdo web em geral

**Exemplo de solicitacao:**
> "Otimize este artigo para a keyword 'produtividade no trabalho remoto'"

---

### 4. Social Agent
**Arquivo:** `subagents/social-agent.md`

**Funcao:** Posts por plataforma, adaptacao cross-platform, hashtags, timing, calendario social.

**Plataformas:**
- Instagram (Feed, Carrossel, Reels, Stories)
- LinkedIn (Posts, Artigos, Newsletter)
- Twitter/X (Tweets, Threads)
- TikTok (Videos, Lives)
- Facebook (Posts, Stories, Grupos)
- Pinterest (Pins, Idea Pins)

**Exemplo de solicitacao:**
> "Crie um post para LinkedIn sobre lideranca remota"

---

### 5. Video Agent
**Arquivo:** `subagents/video-agent.md`

**Funcao:** Scripts YouTube (long-form), Reels/TikTok/Shorts, VSL (Video Sales Letter), hooks de retencao.

**Formatos:**
- Videos longos (YouTube)
- Videos curtos (15s, 30s, 60s)
- VSL completo
- Estruturas de storytelling

**Exemplo de solicitacao:**
> "Crie um roteiro de Reels de 30 segundos sobre habitos matinais"

---

### 6. AI Tools Agent
**Arquivo:** `subagents/ai-tools-agent.md`

**Funcao:** Prompts otimizados para geracao de imagens e videos com IA.

**Ferramentas de Imagem:**
- Nano Banana Pro
- GPT Image 1.5
- Midjourney
- DALL-E 3
- Flux 2 Pro
- Seedream 4.5

**Ferramentas de Video:**
- Veo 3.1
- Sora 2
- Kling 2.6 / Kling O1
- Seedance

**Exemplo de solicitacao:**
> "Crie um prompt para Midjourney de uma thumbnail de YouTube sobre IA"

---

### 7. Design Agent
**Arquivo:** `subagents/design-agent.md`

**Funcao:** Direcao criativa, moodboards, specs tecnicos por plataforma, paletas de cores, tipografia, prompts de imagem, posts prontos.

**Recursos:**
- Paletas por nicho e emocao
- Specs de dimensoes por plataforma
- Templates visuais
- Prompts para posts prontos (Nano Banana Pro)

**Exemplo de solicitacao:**
> "Defina a direcao criativa visual para uma marca de produtividade"

---

### 8. Analytics Agent
**Arquivo:** `subagents/analytics-agent.md`

**Funcao:** Metricas por plataforma, relatorios semanais/mensais, analise de performance, testes A/B.

**Metricas rastreadas:**
- Engajamento (likes, comentarios, shares)
- Alcance e impressoes
- Taxa de conversao
- CTR (Click-through rate)
- Tempo de visualizacao

**Exemplo de solicitacao:**
> "Defina os KPIs para uma campanha de lancamento de curso"

---

### 9. Audio Agent
**Arquivo:** `subagents/audio-agent.md`

**Funcao:** Roteiros de podcast (solo, entrevista, co-host), estruturas de episodio, scripts de spots/ads, audiobooks.

**Formatos:**
- Podcast solo
- Podcast entrevista
- Podcast co-host
- Spots publicitarios
- Narracoes

**Exemplo de solicitacao:**
> "Crie um roteiro de podcast de 20 minutos sobre IA para iniciantes"

---

### 10. Email Agent
**Arquivo:** `subagents/email-agent.md`

**Funcao:** Sequencias de email, newsletters, automacoes de marketing.

**Tipos de email:**
- Welcome sequence
- Launch sequence
- Nurturing sequence
- Re-engagement
- Newsletter regular

**Exemplo de solicitacao:**
> "Crie uma sequencia de 5 emails para lancamento de produto"

---

### 11. Ads Agent
**Arquivo:** `subagents/ads-agent.md`

**Funcao:** Copy de anuncios Meta/Google/TikTok/LinkedIn, estratégia de ads.

**Plataformas:**
- Meta Ads (Facebook/Instagram)
- Google Ads (Search/Display)
- TikTok Ads
- LinkedIn Ads

**Exemplo de solicitacao:**
> "Crie 3 variacoes de anuncio para Meta Ads promovendo um ebook"

---

## Como Usar na Pratica

### Exemplo 1: Criar um Post de Instagram

**Sua solicitacao:**
> "Crie um carrossel para Instagram sobre 5 ferramentas de IA para produtividade"

**O que acontece:**
1. O agente identifica: Nicho (IA + Produtividade), Formato (Carrossel), Plataforma (Instagram)
2. Social Agent formata para Instagram
3. Copy Agent cria headlines e CTAs
4. Design Agent sugere visual
5. Entrega com hashtags e variacoes A/B

---

### Exemplo 2: Criar um Artigo SEO

**Sua solicitacao:**
> "Escreva um artigo otimizado para SEO sobre 'como usar ChatGPT para estudar'"

**O que acontece:**
1. Research Agent pesquisa keywords relacionadas
2. SEO Agent estrutura o artigo (H1, H2s, H3s)
3. Copy Agent escreve o conteúdo
4. Entrega com meta title, meta description, keywords

---

### Exemplo 3: Campanha de Lancamento

**Sua solicitacao:**
> "Planeje uma campanha completa de lancamento para um curso de marketing digital"

**O que acontece:**
1. Consulta `workflows/lancamento-produto.md`
2. Research Agent analisa mercado
3. Video Agent cria roteiros (VSL, Reels)
4. Social Agent planeja calendario
5. Email Agent cria sequencia de lancamento
6. Ads Agent desenvolve anuncios
7. Entrega pacote completo com timeline de 30 dias

---

### Exemplo 4: Roteiro de Video

**Sua solicitacao:**
> "Crie um roteiro de YouTube de 10 minutos sobre '7 habitos de pessoas produtivas'"

**O que acontece:**
1. Video Agent seleciona template `assets/templates/youtube-script.md`
2. Copy Agent cria hooks e CTAs
3. Estrutura com intro, segmentos, CTA, outro
4. Entrega com timestamps e indicacoes visuais

---

### Exemplo 5: Geracao de Imagem com IA

**Sua solicitacao:**
> "Crie um prompt para Midjourney de uma thumbnail atraente para video sobre investimentos"

**O que acontece:**
1. AI Tools Agent consulta biblioteca de prompts
2. Design Agent define estilo visual
3. Entrega prompt otimizado com parametros

---

## Scripts Python de Automacao

Execute os scripts no terminal para automatizar tarefas:

### Analise e Otimizacao

| Script | Comando | Descricao |
|--------|---------|-----------|
| `seo_analyzer.py` | `python scripts/seo_analyzer.py arquivo.md "keyword"` | Analisa SEO (score 0-100) |
| `headline_scorer.py` | `python scripts/headline_scorer.py "Sua headline"` | Pontua headlines |
| `readability_checker.py` | `python scripts/readability_checker.py --file artigo.txt` | Analisa legibilidade |
| `content_audit.py` | `python scripts/content_audit.py arquivo.md --tipo blog` | Audita conteúdo |

### Geracao de Conteúdo

| Script | Comando | Descricao |
|--------|---------|-----------|
| `hashtag_generator.py` | `python scripts/hashtag_generator.py nicho plataforma` | Gera hashtags |
| `hook_generator.py` | `python scripts/hook_generator.py "tema" reels 10` | Gera hooks virais |
| `ab_generator.py` | `python scripts/ab_generator.py headline "texto"` | Cria variacoes A/B |
| `content_idea_generator.py` | `python scripts/content_idea_generator.py nicho 20` | Gera ideias |

### Instagram Especifico

| Script | Comando | Descricao |
|--------|---------|-----------|
| `instagram_hashtag_research.py` | `python scripts/instagram_hashtag_research.py "nicho" --objetivo alcance` | Pesquisa hashtags |
| `hook_variant_generator.py` | `python scripts/hook_variant_generator.py "tema" --formato reels` | Variantes de hooks |
| `reels_script_generator.py` | `python scripts/reels_script_generator.py "tema" 30 tutorial` | Scripts de Reels |
| `carousel_structure_generator.py` | `python scripts/carousel_structure_generator.py "tema" educativo 7` | Estruturas de carrossel |
| `caption_generator.py` | `python scripts/caption_generator.py "tema" engajamento` | Gera legendas |

### Tendencias e Analise

| Script | Comando | Descricao |
|--------|---------|-----------|
| `trend_tracker.py` | `python scripts/trend_tracker.py "termo" google youtube` | Monitora tendencias |
| `trend_adapter.py` | `python scripts/trend_adapter.py "GRWM" marketing` | Adapta trends |
| `competitor_analyzer.py` | `python scripts/competitor_analyzer.py "@perfil1" "@perfil2"` | Analisa concorrentes |
| `tiktok_trends_scraper.py` | `python scripts/tiktok_trends_scraper.py --hashtag "marketing"` | Busca trends TikTok |

### Planejamento

| Script | Comando | Descricao |
|--------|---------|-----------|
| `content_calendar.py` | `python scripts/content_calendar.py 2026-02-01 4 instagram linkedin` | Cria calendario |
| `content_repurposer.py` | `python scripts/content_repurposer.py --file artigo.txt --output todos` | Adapta conteúdo |

---

## Templates Disponiveis

Localizados em `assets/templates/`:

### Redes Sociais

| Template | Arquivo | Uso |
|----------|---------|-----|
| Post Instagram Carrossel | `post-instagram-carrossel.md` | Carrosseis educativos/vendas |
| Instagram Feed Post | `instagram-feed-post.md` | Posts de feed |
| Instagram Stories | `instagram-stories.md` | Sequencias de stories |
| Post LinkedIn | `post-linkedin.md` | Posts profissionais |
| Twitter Thread | `twitter-thread.md` | Threads virais |
| Pinterest Pins | `pinterest-pins.md` | Pins e boards |

### Video

| Template | Arquivo | Uso |
|----------|---------|-----|
| YouTube Script | `youtube-script.md` | Videos longos |
| YouTube Shorts | `youtube-shorts.md` | Shorts |
| Reels/TikTok Script | `reels-tiktok-script.md` | Videos curtos |
| VSL Script | `vsl-script.md` | Video Sales Letter |
| Webinar Script | `webinar-script.md` | Lives de vendas |

### Texto/Blog

| Template | Arquivo | Uso |
|----------|---------|-----|
| Artigo SEO | `artigo-seo.md` | Artigos otimizados |
| Press Release | `press-release.md` | Comunicados |
| Case Study | `case-study.md` | Estudos de caso |
| Whitepaper | `whitepaper.md` | Conteúdo B2B |

### Marketing

| Template | Arquivo | Uso |
|----------|---------|-----|
| Email Newsletter | `email-newsletter.md` | Newsletters |
| Sales Page | `sales-page.md` | Paginas de vendas |
| Lead Magnet | `lead-magnet.md` | Iscas digitais |
| UGC Brief | `ugc-brief.md` | Briefing para criadores |

### Audio

| Template | Arquivo | Uso |
|----------|---------|-----|
| Podcast Episode | `podcast-episode.md` | Estrutura de episodio |
| Podcast Ad Reads | `podcast-ad-reads.md` | Anuncios em podcast |

---

## Workflows de Campanha

Localizados em `workflows/`:

### Lancamento de Produto
**Arquivo:** `lancamento-produto.md`

Timeline de 30 dias completo com:
- Fase de aquecimento (Dias 1-10)
- Fase de lancamento (Dias 11-20)
- Fase de conversao (Dias 21-30)
- Checklist de assets necessarios

### Calendario Mensal
**Arquivo:** `calendario-mensal.md`

Planejamento editorial mensal incluindo:
- Pilares de conteúdo
- Frequencia por plataforma
- Temas semanais
- Datas comemorativas

### Campanha de Conversao
**Arquivo:** `campanha-conversao.md`

Para promocoes e flash sales:
- Estrutura de urgencia
- Sequencia de emails
- Posts sociais
- Remarketing

### Funil de Vendas
**Arquivo:** `funil-vendas.md`

Processo completo TOFU > MOFU > BOFU:
- Conteúdo por etapa
- Ofertas escalonadas
- Automacoes

### Parceria com Influencer
**Arquivo:** `parceria-influencer.md`

De ponta a ponta:
- Prospeccao
- Briefing
- Gestao
- Medicao de resultados

### Producao em Lote
**Arquivo:** `batch-production-workflow.md`

Para criar muito conteúdo rapidamente:
- Cronograma de batching
- Templates de producao
- Checklists

### TikTok Trends Chrome
**Arquivo:** `tiktok-trends-chrome.md`

Busca manual de videos virais:
- Workflow de pesquisa
- Templates de coleta
- Analise de tendencias

---

## Recursos Adicionais

### Swipe Files (Banco de Referencias)
Localizados em `assets/swipe-files/`:

| Arquivo | Conteúdo |
|---------|----------|
| `headlines-virais.md` | 100+ estruturas de titulos |
| `hooks-reels.md` | Hooks para videos curtos |
| `ctas-conversao.md` | Chamadas para acao |
| `emails-conversao.md` | Templates de email |
| `copy-carrossel.md` | Estruturas de carrosséis |
| `bios-instagram.md` | Bios por nicho |
| `transicoes-reels.md` | Transicoes criativas |
| `trends-adaptaveis.md` | 12 trends para adaptar |
| `paletas-cores.md` | Paletas por nicho |

### Guias de Referencia
Localizados em `references/`:

| Arquivo | Conteúdo |
|---------|----------|
| `niches.md` | Personas, pilares, hashtags por nicho |
| `strategy.md` | Frameworks de estratégia |
| `social-media.md` | Guia por plataforma |
| `blog-seo.md` | Otimizacao de artigos |
| `email-marketing.md` | Best practices de email |
| `landing-pages.md` | Estruturas de conversao |
| `ads-copy.md` | Copy de anuncios |
| `design-specs.md` | Dimensoes por plataforma |

### Personas
Localizadas em `assets/personas/`:

| Arquivo | Conteúdo |
|---------|----------|
| `persona-template.md` | Template para criar novas |
| `personas-por-nicho.md` | Personas pre-definidas |

### Prompts de IA
Localizados em `assets/prompts/`:

| Arquivo | Conteúdo |
|---------|----------|
| `prompt-biblioteca.md` | Biblioteca geral |
| `prompts-imagem-ia.md` | Prompts para geracao de imagem |
| `prompts-post-pronto.md` | Posts prontos (Nano Banana Pro) |

---

## Referencia Rapida de Comandos

### Solicitacoes Comuns

```
# Posts de Redes Sociais
"Crie um post para Instagram sobre [tema]"
"Faca um carrossel de [X] slides sobre [tema]"
"Crie uma thread para Twitter sobre [tema]"
"Escreva um post LinkedIn sobre [tema]"

# Videos
"Crie um roteiro de Reels de [X] segundos sobre [tema]"
"Faca um script de YouTube de [X] minutos sobre [tema]"
"Crie um VSL para [produto]"

# Artigos/Blog
"Escreva um artigo SEO sobre [tema] com keyword [X]"
"Otimize este texto para SEO"

# Email Marketing
"Crie uma sequencia de [X] emails para [objetivo]"
"Escreva uma newsletter sobre [tema]"

# Anuncios
"Crie anuncios para Meta Ads sobre [produto]"
"Faca copy de Google Ads para [servico]"

# Planejamento
"Monte um calendario editorial de [X] semanas para [plataformas]"
"Planeje uma campanha de lancamento para [produto]"

# IA Generativa
"Crie um prompt para [ferramenta] de [descricao]"
"Gere ideias de thumbnail para [video]"
```

### Scripts Python Mais Usados

```bash
# Gerar hashtags
python scripts/hashtag_generator.py marketing_digital instagram

# Criar calendario
python scripts/content_calendar.py 2026-02-01 4 instagram linkedin

# Analisar headline
python scripts/headline_scorer.py "7 segredos de produtividade"

# Gerar hooks
python scripts/hook_generator.py "produtividade" reels 10

# Gerar ideias
python scripts/content_idea_generator.py tecnologia 20

# Analisar SEO
python scripts/seo_analyzer.py artigo.md "marketing digital"
```

---

## Dicas e Melhores Praticas

### 1. Seja Especifico no Briefing

**Ruim:**
> "Crie um post sobre IA"

**Bom:**
> "Crie um carrossel de 7 slides para Instagram sobre 5 ferramentas de IA para produtividade, tom educativo e acessivel, publico: profissionais de 25-40 anos, CTA: seguir o perfil"

### 2. Aproveite os Nichos Pre-Configurados

O agente tem conhecimento especifico de 10 nichos. Mencione o nicho para obter:
- Personas adequadas
- Pilares de conteúdo
- Hashtags relevantes
- Tom de voz correto

### 3. Peca Variacoes A/B

Sempre solicite variacoes para testar:
> "Crie 3 variacoes de headline para testar"

### 4. Use os Templates

Os templates em `assets/templates/` sao estruturas otimizadas. Peca para usar:
> "Use o template de VSL para criar um script de vendas"

### 5. Combine Subagentes

Para projetos complexos, combine especialidades:
> "Quero um artigo SEO (SEO Agent) com copy persuasivo (Copy Agent) e prompts para imagens (AI Tools Agent)"

### 6. Execute os Scripts Regularmente

Use os scripts Python para:
- Verificar qualidade do conteúdo
- Gerar ideias em lote
- Manter calendario atualizado
- Pesquisar tendencias

### 7. Consulte os Swipe Files

Antes de criar, olhe as referencias em `assets/swipe-files/` para inspiracao testada.

### 8. Siga os Workflows

Para campanhas complexas, siga os workflows em `workflows/` - eles tem checklists e timelines prontos.

---

## Troubleshooting

### O agente não está sendo acionado

**Solucao:**
1. Verifique se a pasta selecionada no Cowork e `Marketing OS`
2. Use palavras-chave trigger: "conteúdo", "post", "marketing", "Instagram", etc.
3. Reinicie o Claude Desktop

### Scripts Python não funcionam

**Solucao:**
1. Instale as dependencias: `pip install requests beautifulsoup4 pandas python-dotenv`
2. Verifique a versao do Python (3.8+)
3. Execute da pasta correta: `cd Agente\ Criador\ de\ Conteudo`

### Conteúdo não está no formato correto

**Solucao:**
1. Especifique a plataforma claramente
2. Mencione limites de caracteres se necessario
3. Peca para formatar especificamente: "Formate para Instagram Stories"

### Quero um nicho que não está na lista

**Solucao:**
1. Descreva o nicho detalhadamente
2. Faca um briefing completo de persona
3. O agente pode criar personas customizadas usando `assets/personas/persona-template.md`

### Preciso de mais variacoes

**Solucao:**
1. Peca explicitamente: "Quero 5 variacoes diferentes"
2. Use o script `ab_generator.py` para gerar automaticamente
3. Especifique o tipo de variacao: "variacoes de tom", "variacoes de hook"

---

## Conclusao

O Marketing OS é uma ferramenta poderosa para criar conteúdo estrategico de forma eficiente. Com 16 subagentes especializados, 19+ scripts Python, 20+ templates e workflows completos, você tem tudo que precisa para:

- Criar conteúdo de alta qualidade rapidamente
- Manter consistencia entre plataformas
- Otimizar para engajamento e conversao
- Escalar sua producao de conteúdo

**Dica Final:** Quanto mais contexto você fornecer (nicho, publico, objetivo, tom), melhor será o resultado. Use este guia como referencia e explore todos os recursos disponiveis!

---

*Desenvolvido por rilnermucio | Versao 4.0*
