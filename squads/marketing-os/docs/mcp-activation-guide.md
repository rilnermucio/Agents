# Guia de Ativacao dos MCPs — Marketing OS

> Documentacao dos 9 MCPs existentes em `.aios-core/infrastructure/tools/mcp/` e sua relevancia para operacoes de marketing.

## Visao Geral

O AIOS possui 9 MCPs configurados. Destes, **5 sao diretamente relevantes** para o Marketing OS e **4 sao de infraestrutura/desenvolvimento**.

## Status dos MCPs

| MCP | Status | Relevancia Marketing | Prioridade |
|-----|--------|---------------------|------------|
| EXA | Ativo (Docker) | Alta | P0 |
| Context7 | Ativo (SSE) | Media | P1 |
| Browser | Ativo (Playwright) | Media | P1 |
| ClickUp | Configurado | Baixa | P2 |
| n8n | Configurado | Baixa | P2 |
| 21st Dev Magic | Configurado | Nenhuma | — |
| Desktop Commander | Ativo | Nenhuma | — |
| Google Workspace | Configurado | Potencial | P3 |
| Supabase | Configurado | Nenhuma | — |

## MCPs Relevantes para Marketing

### 1. EXA Web Search (Prioridade: P0)

**Arquivo:** `.aios-core/infrastructure/tools/mcp/exa.yaml`

**Funcionalidades:**
- Busca web com resultados configuráveis
- Pesquisa acadêmica (100M+ papers)
- Análise de empresas e concorrentes
- Crawling de URLs
- Busca no LinkedIn e GitHub

**Variáveis de ambiente necessárias:**
```bash
EXA_API_KEY=<sua-chave-exa>
```

**Health check:**
```bash
# Via Docker MCP
docker mcp tools call web_search_exa '{"query": "test"}'
```

**Agentes que mais se beneficiam:**
- Research Agent — pesquisa de mercado e tendências
- SEO Agent — análise de concorrentes e keywords
- Analytics Agent — dados de mercado
- Growth Agent — oportunidades de crescimento

---

### 2. Context7 Library Documentation (Prioridade: P1)

**Arquivo:** `.aios-core/infrastructure/tools/mcp/context7.yaml`

**Funcionalidades:**
- Documentação atualizada de qualquer biblioteca
- Filtro por tópico específico
- Controle de tokens na recuperação

**Variáveis de ambiente necessárias:**
- Nenhuma (serviço SSE público)

**Health check:**
```bash
# Testar resolução de biblioteca
curl -s "https://mcp.context7.com/sse"
```

**Agentes que mais se beneficiam:**
- AI Tools Agent — documentação de ferramentas de IA
- Email Agent — APIs de serviços de email
- Ads Agent — APIs do Meta/Google Ads

---

### 3. Browser / Playwright (Prioridade: P1)

**Arquivo:** `.aios-core/infrastructure/tools/mcp/browser.yaml`

**Funcionalidades:**
- Automação de browser
- Screenshots de páginas web
- Interação com websites
- Scraping de dados públicos

**Variáveis de ambiente necessárias:**
```bash
# Playwright é instalado como plugin MCP
npx playwright install
```

**Health check:**
```bash
# Verificar instalação do Playwright
npx playwright --version
```

**Agentes que mais se beneficiam:**
- Design Agent — screenshots para referência visual
- Research Agent — coleta de dados de concorrentes
- Funnel Agent — testes de landing pages

---

### 4. ClickUp (Prioridade: P2)

**Arquivo:** `.aios-core/infrastructure/tools/mcp/clickup.yaml`

**Funcionalidades:**
- Gestão de tarefas
- Integração com calendário editorial
- Rastreamento de projetos de marketing

**Variáveis de ambiente necessárias:**
```bash
CLICKUP_API_KEY=<sua-chave-clickup>
CLICKUP_TEAM_ID=<seu-team-id>
```

**Agentes que mais se beneficiam:**
- Launch Agent — gestão de lançamentos
- Social Agent — calendário editorial

---

### 5. n8n (Prioridade: P2)

**Arquivo:** `.aios-core/infrastructure/tools/mcp/n8n.yaml`

**Funcionalidades:**
- Automação de workflows
- Integração entre plataformas
- Triggers baseados em eventos

**Variáveis de ambiente necessárias:**
```bash
N8N_API_KEY=<sua-chave-n8n>
N8N_BASE_URL=<url-do-seu-n8n>
```

**Agentes que mais se beneficiam:**
- Email Agent — automação de sequences
- Growth Agent — automação de growth loops
- Funnel Agent — automação de funis

---

## MCPs Nao Relevantes para Marketing

| MCP | Motivo |
|-----|--------|
| 21st Dev Magic | Focado em desenvolvimento de UI/componentes |
| Desktop Commander | Gerenciamento de containers Docker |
| Supabase | Database, responsabilidade do @data-engineer |
| Google Workspace | Potencial futuro, sem configuração ativa |

## Como Ativar um MCP

### Passo 1: Verificar configuração

```bash
# Listar MCPs configurados
cat .aios-core/infrastructure/tools/mcp/<nome>.yaml
```

### Passo 2: Configurar variáveis de ambiente

```bash
# Adicionar ao .env ou exportar
export EXA_API_KEY="sua-chave"
```

### Passo 3: Verificar saúde do MCP

```bash
# Para MCPs via Docker
docker mcp tools ls

# Para MCPs nativos
# Executar health check específico do MCP
```

### Passo 4: Testar integração

```bash
# Testar com uma operação simples
# Exemplo para EXA:
docker mcp tools call web_search_exa '{"query": "marketing digital 2026"}'
```

## Regras de Governança

1. **@devops** é o único responsável por gerenciar MCPs
2. Subagentes são **consumidores**, não administradores de MCPs
3. Sempre preferir ferramentas nativas do Claude Code sobre MCPs
4. MCPs complementam, não substituem os subagentes
5. Consultar `marketing-mcp.yaml` para mapeamento agente→MCP

## Referências

- `.claude/rules/mcp-usage.md` — Regras gerais de uso de MCP
- `squads/marketing-os/config/marketing-mcp.yaml` — Configuração agregada
- `.aios-core/infrastructure/tools/mcp/` — Configurações individuais
