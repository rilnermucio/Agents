# Instalação da Skill "Marketing OS" no Cowork

## Arquivos Criados

| Arquivo | Descricao |
|---------|-----------|
| `marketing-os.skill` | Pacote da skill (arquivo ZIP) |
| `skill-package/marketing-os/` | Pasta descompactada da skill |

---

## Metodo 1: Usar Diretamente no Cowork (Recomendado)

A forma mais simples e funciona **imediatamente**:

1. Abra o **Cowork** no Claude Desktop
2. Selecione a pasta `Marketing OS` como sua pasta de trabalho
3. O Claude automaticamente reconhecera o `Skill.md` e tera acesso a todas as funcionalidades

**Por que funciona:** O Cowork le o arquivo `Skill.md` da pasta selecionada e carrega as instrucoes do agente.

---

## Metodo 2: Instalar como Skill Global

Para ter a skill disponivel em **qualquer** pasta do Cowork:

### macOS

```bash
# 1. Abra o Terminal

# 2. Navegue até a pasta do agente
cd ~/caminho/para/Marketing\ OS

# 3. Descompacte o .skill (que e um ZIP)
unzip marketing-os.skill -d ~/Library/Application\ Support/Claude/skills/

# 4. Renomeie a pasta extraida (se necessario)
mv ~/Library/Application\ Support/Claude/skills/sessions*/marketing-os \
   ~/Library/Application\ Support/Claude/skills/marketing-os
```

### Windows

```powershell
# 1. Abra o PowerShell

# 2. Navegue até a pasta do agente
cd C:\caminho\para\Marketing OS

# 3. Descompacte o .skill
Expand-Archive -Path marketing-os.skill -DestinationPath "$env:APPDATA\Claude\skills\"

# 4. Renomeie a pasta extraida (se necessario)
```

### Verificar Instalacao

Apos instalar, reinicie o Claude Desktop. A skill deve aparecer na lista de skills disponiveis.

---

## Metodo 3: Instalacao Manual

1. Copie a pasta `skill-package/marketing-os/` para o diretorio de skills:
   - **macOS:** `~/Library/Application Support/Claude/skills/`
   - **Windows:** `%APPDATA%\Claude\skills\`
   - **Linux:** `~/.config/claude/skills/`

2. Certifique-se de que a estrutura fique assim:
   ```
   skills/
   └── marketing-os/
       ├── SKILL.md
       ├── scripts/
       ├── assets/
       ├── references/
       ├── subagents/
       └── workflows/
   ```

3. Reinicie o Claude Desktop

---

## Estrutura da Skill

```
marketing-os/
├── SKILL.md              # Arquivo principal da skill
├── scripts/              # 19 scripts Python
│   ├── seo_analyzer.py
│   ├── hashtag_generator.py
│   ├── hook_generator.py
│   ├── reels_script_generator.py
│   ├── tiktok_trends_scraper.py
│   └── ... (14 mais)
├── assets/
│   ├── templates/        # 26 templates de conteúdo
│   ├── swipe-files/      # 8 swipe files com exemplos
│   ├── personas/         # Templates de persona
│   ├── frameworks/       # Frameworks de crescimento
│   └── checklists/       # Checklists de qualidade
├── references/           # 7 guias de referencia
│   ├── social-media.md
│   ├── blog-seo.md
│   ├── email-marketing.md
│   └── ... (4 mais)
├── subagents/            # 10 subagentes especializados
│   ├── video-agent.md
│   ├── copy-agent.md
│   ├── seo-agent.md
│   └── ... (7 mais)
└── workflows/            # 7 workflows completos
    ├── lancamento-produto.md
    ├── calendario-mensal.md
    ├── tiktok-trends-chrome.md
    └── ... (4 mais)
```

---

## Triggers da Skill

A skill será acionada automaticamente quando você mencionar:

**Palavras-chave:** conteúdo, marketing, post, blog, SEO, newsletter, copy, landing page, campanha, anuncio, Instagram, LinkedIn, TikTok, YouTube, Reels, podcast, VSL, carrossel, stories, email marketing, calendario editorial

**Nichos:** Marketing Digital, IA, Desenvolvimento Pessoal, Empreendedorismo, Financas, Saude, Tecnologia, Produtividade

---

## Dependencias Python

Para usar os scripts, instale as dependencias:

```bash
pip install requests beautifulsoup4 pandas python-dotenv
```

Opcional (para TikTok scraper):
```bash
pip install TikTokApi playwright
playwright install
```

---

## Suporte

Se tiver problemas:
1. Verifique se o arquivo SKILL.md esta no local correto
2. Reinicie o Claude Desktop
3. Tente o Metodo 1 (usar diretamente na pasta)
