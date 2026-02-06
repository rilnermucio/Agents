# Biblioteca de Prompts para Geracao de Imagem IA

Prompts otimizados para Midjourney, DALL-E, e outras ferramentas de geracao de imagem.

---

## Estrutura Base

```
[SUJEITO] + [ACAO] + [AMBIENTE] + [ESTILO] + [ILUMINACAO] + [CAMERA] + [QUALIDADE]
```

---

## Prompts por Tipo de Conteudo

### Feed Post - Lifestyle Profissional

```
MIDJOURNEY:
Brazilian professional woman in her 30s, working on laptop
in modern minimalist home office, indoor plants, natural
window light, lifestyle editorial photography, Canon EOS R5,
85mm lens, shallow depth of field, 8k resolution
--ar 4:5 --v 6 --style raw

DALL-E:
Create a lifestyle photograph of a Brazilian professional
woman in her 30s working on a MacBook in a modern minimalist
home office. The space has white walls, a wooden desk, and
green indoor plants. Natural light comes through a large
window creating soft shadows. The image should look like
editorial photography with a shallow depth of field.
Professional quality, high resolution.
```

### Feed Post - Flat Lay

```
MIDJOURNEY:
flat lay photography, workspace essentials on marble surface,
MacBook laptop, coffee cup, notebook, pen, succulent plant,
minimalist aesthetic, soft overhead lighting, product
photography style, 8k resolution, clean organized composition
--ar 1:1 --v 6 --style raw

DALL-E:
Create a flat lay photograph shot from directly above showing
a minimalist workspace on a white marble surface. Include a
MacBook laptop, a cup of coffee, a leather notebook, a gold
pen, and a small succulent plant. The items should be
arranged in a balanced, aesthetically pleasing composition.
Soft, even lighting with minimal shadows. Product photography
style, high resolution.
```

### Stories/Reels - Behind the Scenes

```
MIDJOURNEY:
candid photo of content creator woman preparing for video,
ring light visible, camera equipment, messy creative
workspace, authentic documentary style, warm indoor lighting,
natural unposed moment, iPhone quality aesthetic
--ar 9:16 --v 6 --style raw

DALL-E:
Create a candid behind-the-scenes photograph of a female
content creator preparing for a video shoot. Show her
adjusting a ring light with camera equipment visible on
her desk. The workspace should look creative but slightly
messy. Warm indoor lighting. The image should feel authentic
and unposed, like a documentary moment. Vertical format
for Instagram Stories.
```

### Thumbnail YouTube

```
MIDJOURNEY:
surprised young woman pointing at empty text space on right,
bright solid yellow background, exaggerated facial expression
with wide eyes and open mouth, YouTube thumbnail style,
high contrast vibrant colors, clean professional studio
lighting, sharp focus on face, bold dynamic composition
--ar 16:9 --v 6

DALL-E:
Create a YouTube thumbnail showing a surprised young woman
on the left side pointing toward empty space on the right
(for text overlay). She has an exaggerated expression with
wide eyes and open mouth. The background is solid bright
yellow. The image should be high contrast with vibrant
colors, sharp focus on the face, shot in a professional
studio with clean lighting. Landscape format 16:9.
```

### Carrossel - Ilustracao Educativa

```
MIDJOURNEY:
minimal line art illustration, abstract business concept,
geometric shapes, soft pastel colors, flat design style,
clean white background, vector art aesthetic, modern
minimalist infographic style
--ar 4:5 --v 6 --style raw

DALL-E:
Create a minimalist illustration with simple line art
representing a business concept. Use geometric shapes
in soft pastel colors (light blue, coral, mint) on a
clean white background. The style should be flat design,
similar to modern vector illustrations used in apps and
infographics. Simple, clean, and professional.
```

---

## Prompts por Nicho

### Marketing Digital

```
MIDJOURNEY:
digital marketing professional analyzing data on multiple
screens, modern tech office, blue accent lighting, futuristic
corporate aesthetic, cinematic lighting, wide angle shot,
tech startup atmosphere, 8k resolution
--ar 4:5 --v 6 --style raw
```

### Empreendedorismo Feminino

```
MIDJOURNEY:
confident Brazilian businesswoman in elegant outfit,
modern office with rose gold accents, natural lighting,
empowering portrait, editorial fashion photography,
soft bokeh background, Canon 85mm f/1.4, warm tones
--ar 4:5 --v 6 --style raw
```

### Financas Pessoais

```
MIDJOURNEY:
professional financial advisor at desk, organized workspace
with calculator and documents, trust-inspiring portrait,
corporate photography, neutral color palette with green
accents, natural window light, business editorial style
--ar 4:5 --v 6 --style raw
```

### Desenvolvimento Pessoal

```
MIDJOURNEY:
person meditating at sunrise, peaceful outdoor setting,
warm golden hour lighting, mindfulness and wellness concept,
lifestyle photography, soft ethereal atmosphere, calm
serene mood, inspirational self-care imagery
--ar 4:5 --v 6 --style raw
```

### Fitness/Saude

```
MIDJOURNEY:
athletic woman in dynamic workout pose, modern gym
environment, dramatic action shot, high energy fitness
photography, strong directional lighting, sweat and
motion blur, Nike advertisement style, powerful inspiring
--ar 4:5 --v 6 --style raw
```

### Tech/Programacao

```
MIDJOURNEY:
software developer coding on ultrawide monitor, dark
room with RGB lighting, code on screen, cyberpunk tech
aesthetic, atmospheric moody lighting, programmer at
work, futuristic workspace, 8k cinematic
--ar 4:5 --v 6 --style raw
```

---

## Elementos de Prompt

### Sujeitos
```
- Brazilian woman/man, [age]s
- Professional/entrepreneur
- Content creator
- [profession] at work
- Hands holding [object]
- Close-up of [object]
```

### Ambientes
```
- Modern home office
- Minimalist studio
- Cozy coffee shop
- Urban outdoor setting
- Nature/outdoor
- Professional office
- Creative workspace
```

### Estilos Fotograficos
```
- Editorial photography
- Lifestyle photography
- Product photography
- Portrait photography
- Documentary style
- Fashion editorial
- Corporate headshot
```

### Iluminacao
```
- Natural window light
- Golden hour
- Studio softbox
- Dramatic side lighting
- Backlit/rim light
- Moody atmospheric
- Bright and airy
```

### Camera/Lente
```
- Canon 5D Mark IV, 85mm
- Sony A7III, 35mm
- iPhone quality
- Hasselblad medium format
- Wide angle lens
- Macro close-up
- Portrait lens f/1.4
```

### Qualidade
```
- 8k resolution
- Ultra detailed
- Professional photo
- RAW unedited
- Sharp focus
- High resolution
- Magazine quality
```

---

## Negative Prompts

### Geral
```
cartoon, illustration, 3d render, anime, drawing,
painting, artificial, fake, stock photo feeling,
oversaturated, blurry, low quality, watermark,
text, logo, signature
```

### Para Pessoas
```
deformed, ugly, mutilated, disfigured, extra limbs,
extra fingers, fused fingers, bad anatomy, bad
proportions, gross proportions, malformed limbs,
missing arms, missing legs, extra arms, extra legs
```

### Para Produtos
```
distorted, warped, unnatural colors, unrealistic
shadows, floating objects, impossible physics,
cluttered, messy, unprofessional
```

---

## Parametros Midjourney

```
--ar [ratio]     Aspect ratio (1:1, 4:5, 9:16, 16:9)
--v 6            Versao do modelo (usar mais recente)
--style raw      Menos estilizado, mais fotografico
--q 2            Qualidade maxima
--s [0-1000]     Stylize (baixo = mais literal)
--c [0-100]      Chaos (variacao)
--no [item]      Excluir elemento
--seed [numero]  Reproduzir resultado
```

---

## Fluxo de Iteracao

```
1. PROMPT INICIAL
   └── Gerar 4 variacoes

2. AVALIAR RESULTADOS
   ├── Composicao ok?
   ├── Iluminacao ok?
   ├── Sujeito ok?
   └── Estilo ok?

3. REFINAR
   ├── Adicionar detalhes faltantes
   ├── Remover elementos indesejados (--no)
   └── Ajustar parametros

4. UPSCALE
   └── Selecionar melhor e aumentar resolucao

5. POS-PRODUCAO
   └── Ajustes finais em editor (se necessario)
```
