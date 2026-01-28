# 🤖 AI Tools Agent - Subagente de Ferramentas de IA

Subagente especializado em prompts e workflows para ferramentas de Inteligência Artificial generativa.

---

## 🎯 Quando Usar

- Geração de imagens com IA
- Criação de vídeos com IA
- Prompts para ChatGPT/Claude
- Automação de conteúdo
- Edição e enhancement com IA
- Workflows multi-ferramenta

---

## 🖼️ Ferramentas de Imagem

### Nanobanana Pro

**Descrição:** Ferramenta avançada de geração de imagens com alta fidelidade e controle criativo.

**Melhores Casos de Uso:**
- Imagens fotorrealistas
- Arte conceitual
- Mockups de produtos
- Thumbnails e covers
- Posts para redes sociais

**Estrutura de Prompt:**
```
[ESTILO] + [SUJEITO] + [AÇÃO/POSE] + [AMBIENTE] + [ILUMINAÇÃO] + [DETALHES TÉCNICOS]
```

**Parâmetros Recomendados:**
| Parâmetro | Valor Recomendado | Uso |
|-----------|-------------------|-----|
| Quality | Ultra/High | Sempre para final |
| Aspect Ratio | 1:1, 16:9, 9:16 | Conforme plataforma |
| Style | Photorealistic, Artistic, 3D | Conforme objetivo |

**Prompts Exemplo:**

*Thumbnail YouTube:*
```
Professional YouTube thumbnail, [PESSOA] with surprised expression looking at [OBJETO],
bold dramatic lighting, cinematic composition, vibrant colors,
text space on left side, 16:9 aspect ratio, ultra sharp, 4K quality
```

*Post Instagram:*
```
Modern minimalist [PRODUTO] photography, clean white background,
soft natural lighting, professional product shot, Instagram aesthetic,
square format 1:1, high-end commercial style
```

*Arte para Blog:*
```
Digital illustration for blog header about [TEMA],
modern flat design style, [COR PRINCIPAL] and [COR SECUNDÁRIA] color palette,
abstract geometric elements, professional corporate aesthetic, 16:9 wide format
```

---

### GPT 1.5 (Geração de Imagem)

**Descrição:** Modelo de geração de imagens integrado ao ecossistema GPT com forte compreensão de contexto.

**Melhores Casos de Uso:**
- Ilustrações conceituais
- Diagramas visuais
- Infográficos estilizados
- Imagens educacionais
- Representações abstratas de conceitos

**Estrutura de Prompt:**
```
Create an image of [DESCRIÇÃO DETALHADA].
Style: [ESTILO].
Mood: [ATMOSFERA].
Colors: [PALETA].
Purpose: [USO FINAL].
```

**Prompts Exemplo:**

*Infográfico Visual:*
```
Create a visual infographic representation showing [CONCEITO],
using isometric 3D style with blue and orange color palette,
clean modern design suitable for business presentation,
include visual metaphors for [ELEMENTOS]
```

*Ilustração Educacional:*
```
Educational illustration explaining [TEMA],
friendly cartoon style, bright colors,
clear visual hierarchy, suitable for social media,
include [ELEMENTOS ESPECÍFICOS]
```

*Conceito Abstrato:*
```
Abstract artistic representation of [CONCEITO],
modern digital art style, gradient colors from [COR1] to [COR2],
minimalist composition, suitable for article header
```

---

### Midjourney (Referência)

**Estrutura de Prompt:**
```
[DESCRIÇÃO] --ar [ASPECT] --s [STYLIZE] --q [QUALITY] --v [VERSION]
```

**Parâmetros Úteis:**
- `--ar 16:9` (aspect ratio)
- `--s 750` (stylize: 0-1000)
- `--q 2` (quality)
- `--v 6` (version)
- `--chaos 50` (variação)

---

### DALL-E 3 (Referência)

**Estrutura de Prompt:**
```
[ESTILO] [SUJEITO] [AÇÃO] in [AMBIENTE], [ILUMINAÇÃO], [DETALHES], [MOOD]
```

**Dicas:**
- Seja específico e descritivo
- Mencione estilo artístico
- Inclua detalhes técnicos
- Especifique o que NÃO quer

---

## 🎬 Ferramentas de Vídeo

### Veo 3.1

**Descrição:** Modelo avançado de geração de vídeo do Google com alta qualidade e consistência temporal.

**Melhores Casos de Uso:**
- Vídeos promocionais curtos
- B-roll para YouTube
- Animações de produto
- Conteúdo para Reels/TikTok
- Vídeos explicativos

**Estrutura de Prompt:**
```
[TIPO DE CENA] + [SUJEITO/OBJETO] + [MOVIMENTO/AÇÃO] + [AMBIENTE] + [ESTILO VISUAL] + [DURAÇÃO/RITMO]
```

**Parâmetros Recomendados:**
| Parâmetro | Opções | Uso |
|-----------|--------|-----|
| Duration | 4s, 8s, 16s | Conforme necessidade |
| Resolution | 720p, 1080p, 4K | Plataforma final |
| Style | Cinematic, Documentary, Commercial | Tom do conteúdo |
| Motion | Slow, Medium, Dynamic | Energia desejada |

**Prompts Exemplo:**

*B-roll Tecnologia:*
```
Smooth cinematic shot of hands typing on a modern laptop,
soft bokeh background with blue ambient lighting,
slow motion, professional commercial style,
4K quality, 8 seconds duration
```

*Produto em Destaque:*
```
360-degree rotating shot of [PRODUTO] on clean white surface,
studio lighting with soft shadows,
product showcase style, smooth continuous motion,
1080p, 6 seconds loop
```

*Cena Atmosférica:*
```
Aerial drone shot flying over [PAISAGEM] at golden hour,
cinematic color grading, smooth forward movement,
epic documentary style, 4K, 12 seconds
```

---

### Sora 2

**Descrição:** Modelo de geração de vídeo da OpenAI com capacidade de criar cenas complexas e narrativas.

**Melhores Casos de Uso:**
- Vídeos narrativos
- Cenas com múltiplos elementos
- Storytelling visual
- Conteúdo criativo/artístico
- Vídeos conceituais

**Estrutura de Prompt:**
```
[CENA DETALHADA] with [PERSONAGENS/OBJETOS] [AÇÃO ESPECÍFICA].
Camera: [MOVIMENTO DE CÂMERA].
Style: [ESTÉTICA].
Mood: [ATMOSFERA].
Duration: [TEMPO].
```

**Prompts Exemplo:**

*Cena Narrativa:*
```
A young entrepreneur walking confidently through a modern co-working space,
morning sunlight streaming through large windows,
camera follows from behind then reveals their determined face,
cinematic shallow depth of field, warm color palette,
inspirational corporate mood, 10 seconds
```

*Conceito Abstrato:*
```
Abstract visualization of data flowing through a neural network,
glowing particles forming connections and patterns,
camera slowly zooms out revealing the full structure,
futuristic sci-fi aesthetic, blue and purple neon colors,
mesmerizing and hypnotic mood, 8 seconds loop
```

*Transição Criativa:*
```
Seamless morph transition from [OBJETO A] to [OBJETO B],
centered frame, clean background,
smooth 3-second transformation,
satisfying and magical visual effect
```

---

### Kling 2.6

**Descrição:** Modelo de vídeo com excelente consistência de personagens e movimentos naturais.

**Melhores Casos de Uso:**
- Vídeos com pessoas/personagens
- Movimentos complexos
- Expressões faciais
- Vídeos de lifestyle
- UGC-style content

**Estrutura de Prompt:**
```
[PESSOA/PERSONAGEM] [AÇÃO DETALHADA] in [LOCALIZAÇÃO],
[ROUPA/APARÊNCIA], [EXPRESSÃO/EMOÇÃO],
[ESTILO DE FILMAGEM], [ILUMINAÇÃO]
```

**Parâmetros Recomendados:**
| Parâmetro | Opções | Uso |
|-----------|--------|-----|
| Mode | Standard, Professional | Qualidade |
| Motion | Natural, Dynamic | Tipo de movimento |
| Face Enhancement | On/Off | Vídeos com pessoas |

**Prompts Exemplo:**

*Pessoa Apresentando:*
```
Professional woman in business casual attire presenting to camera,
confident smile, natural hand gestures,
modern office background with plants,
medium shot, soft natural lighting,
corporate but friendly style, 8 seconds
```

*Lifestyle Content:*
```
Young creative professional working on laptop in aesthetic cafe,
casual stylish outfit, focused expression,
morning light through window, coffee cup nearby,
Instagram aesthetic, warm tones, 6 seconds
```

*UGC Style:*
```
Person unboxing [PRODUTO] with genuine excited reaction,
casual home setting, natural smartphone footage look,
authentic influencer style, vertical format,
relatable and engaging, 10 seconds
```

---

### Kling O1

**Descrição:** Versão otimizada do Kling para raciocínio visual e cenas complexas.

**Melhores Casos de Uso:**
- Cenas com múltiplas ações
- Sequências lógicas
- Vídeos tutoriais
- Demonstrações de processo
- Conteúdo educacional

**Estrutura de Prompt:**
```
Step-by-step sequence showing [PROCESSO]:
1. [AÇÃO 1]
2. [AÇÃO 2]
3. [AÇÃO 3]
Style: [ESTILO]. Environment: [AMBIENTE]. Duration: [TEMPO].
```

**Prompts Exemplo:**

*Tutorial Visual:*
```
Step-by-step demonstration of [PROCESSO]:
First, hands prepare the materials on clean workspace,
Then, carefully execute the main action with precision,
Finally, reveal the finished result with subtle zoom,
Clean instructional style, bright even lighting, 15 seconds
```

*Processo de Trabalho:*
```
Sequential workflow visualization:
1. Designer sketching ideas on tablet
2. Refining the design on computer screen
3. Presenting final work on large monitor
Modern creative studio, warm ambient lighting, 12 seconds
```

---

### Seedance

**Descrição:** Especializado em vídeos com dança, movimento rítmico e sincronização musical.

**Melhores Casos de Uso:**
- Conteúdo de dança/movimento
- Vídeos sincronizados com música
- Trends de TikTok/Reels
- Conteúdo fitness
- Vídeos energéticos

**Estrutura de Prompt:**
```
[PESSOA/PERSONAGEM] dancing [ESTILO DE DANÇA] to [TIPO DE MÚSICA],
[ROUPA], [AMBIENTE/CENÁRIO], [ENERGIA/MOOD],
[MOVIMENTOS ESPECÍFICOS], synchronized to beat
```

**Prompts Exemplo:**

*Trend Dance:*
```
Energetic young person doing viral TikTok dance moves,
trendy streetwear outfit, urban rooftop at sunset,
high energy, dynamic camera angles,
perfectly synchronized to upbeat pop music, 15 seconds
```

*Fitness Content:*
```
Fit instructor demonstrating workout routine,
athletic wear, modern gym environment,
motivating energy, clear movement demonstration,
rhythmic exercises synced to energetic music, 20 seconds
```

*Celebração:*
```
Group of friends doing celebratory dance,
party outfits, decorated venue with lights,
joyful and fun atmosphere, confetti falling,
synchronized happy movements, 10 seconds
```

---

## 📝 Ferramentas de Texto

### ChatGPT/GPT-4

**Prompts para Conteúdo:**

*Brainstorm de Ideias:*
```
Atue como um especialista em [NICHO] com 10 anos de experiência.
Gere 20 ideias de conteúdo para [PLATAFORMA] sobre [TEMA].
Para cada ideia, inclua:
- Título/hook
- Ângulo único
- Por que funcionaria
Foque em ideias que geram [OBJETIVO: engajamento/conversão/awareness].
```

*Expansão de Conteúdo:*
```
Expanda o seguinte tópico em um [FORMATO] completo:
Tópico: [TEMA]
Público: [AVATAR]
Tom: [TOM DE VOZ]
Objetivo: [META]
Inclua: exemplos práticos, dados quando relevante, CTAs naturais.
Tamanho: [PALAVRAS/CARACTERES]
```

*Reescrita e Melhoria:*
```
Reescreva o texto abaixo mantendo a mensagem mas:
- Tornando mais [engajante/persuasivo/claro]
- Adaptando para [PLATAFORMA]
- Usando tom [TOM]
- Adicionando hooks e CTAs

Texto original:
[TEXTO]
```

---

### Claude

**Prompts para Análise:**

*Análise de Concorrência:*
```
Analise o seguinte conteúdo de um concorrente:
[CONTEÚDO]

Identifique:
1. Pontos fortes (o que funciona)
2. Pontos fracos (oportunidades)
3. Padrões de linguagem
4. Estrutura utilizada
5. Como podemos fazer melhor

Sugira 3 formas de criar conteúdo superior sobre o mesmo tema.
```

*Criação de Persona:*
```
Crie uma persona detalhada para [NICHO]:

Inclua:
- Demografia (idade, localização, profissão, renda)
- Psicografia (valores, medos, desejos, frustrações)
- Comportamento online (plataformas, horários, tipo de conteúdo)
- Jornada de compra (awareness, consideração, decisão)
- Objeções comuns
- Linguagem e termos que usa
- Influenciadores que segue

Formato: documento estruturado com seções claras.
```

---

## 🔄 Workflows Multi-Ferramenta

### Workflow: Post Completo para Instagram

```
1. ChatGPT/Claude
   └── Gerar ideia + copy do post

2. Nanobanana Pro / GPT 1.5
   └── Criar imagem principal

3. Kling 2.6 / Veo 3.1
   └── Criar versão Reels (opcional)

4. ChatGPT
   └── Gerar variações de caption + hashtags
```

### Workflow: Vídeo YouTube Completo

```
1. Claude
   └── Pesquisa + estrutura do roteiro

2. ChatGPT
   └── Expandir roteiro completo

3. Nanobanana Pro
   └── Criar thumbnail

4. Veo 3.1 / Sora 2
   └── Gerar B-roll

5. ChatGPT
   └── Título, descrição, tags otimizados
```

### Workflow: Campanha de Lançamento

```
1. Claude
   └── Estratégia + copy principal

2. ChatGPT
   └── Variações para cada canal

3. GPT 1.5 / Nanobanana Pro
   └── Criativos visuais

4. Sora 2 / Kling 2.6
   └── Vídeos promocionais

5. Kling O1
   └── Vídeos tutoriais/demonstração
```

---

## 📊 Comparativo de Ferramentas

### Imagem
| Ferramenta | Melhor Para | Estilo | Velocidade |
|------------|-------------|--------|------------|
| Nanobanana Pro | Fotorrealismo, produtos | Versátil | Rápido |
| GPT 1.5 | Conceitos, infográficos | Ilustrativo | Médio |
| Midjourney | Arte, criativo | Artístico | Médio |
| DALL-E 3 | Geral, precisão de texto | Versátil | Rápido |

### Vídeo
| Ferramenta | Melhor Para | Duração | Qualidade |
|------------|-------------|---------|-----------|
| Veo 3.1 | B-roll, cenas | 4-16s | Alta |
| Sora 2 | Narrativa, complexo | 10-60s | Muito alta |
| Kling 2.6 | Pessoas, UGC | 5-10s | Alta |
| Kling O1 | Tutoriais, processos | 10-20s | Alta |
| Seedance | Dança, música | 10-30s | Alta |

---

## ✅ Checklist de Uso de IA

### Antes de Gerar
- [ ] Objetivo claro definido
- [ ] Referências visuais coletadas
- [ ] Prompt estruturado
- [ ] Parâmetros configurados
- [ ] Formato final definido

### Após Gerar
- [ ] Revisar qualidade
- [ ] Verificar consistência de marca
- [ ] Editar se necessário
- [ ] Salvar prompt que funcionou
- [ ] Documentar para reuso

---

## 🔄 Integração com Content Creator

O AI Tools Agent fornece:

1. **Prompts otimizados** por ferramenta
2. **Workflows** multi-ferramenta
3. **Comparativos** para escolha certa
4. **Templates** reutilizáveis
5. **Best practices** atualizadas
