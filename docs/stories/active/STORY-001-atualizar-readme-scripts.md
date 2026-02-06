# STORY-001: Atualizar README com todos os 19 scripts Python

## Metadata

| Campo | Valor |
|-------|-------|
| **ID** | STORY-001 |
| **Tipo** | Docs |
| **Prioridade** | P1 - Alta |
| **Estimativa** | P (Pequeno) |
| **Status** | Active |
| **Criado em** | 2026-02-02 |

---

## Descricao

O README.md atualmente documenta apenas 9 scripts, mas o projeto possui 19 scripts Python funcionais. Esta story visa atualizar a documentacao para refletir todos os scripts disponiveis.

## Contexto

Scripts documentados atualmente:
- seo_analyzer.py
- hashtag_generator.py
- content_calendar.py
- ab_generator.py
- headline_scorer.py
- readability_checker.py
- content_repurposer.py
- hook_generator.py
- content_idea_generator.py

Scripts NAO documentados:
- caption_generator.py
- carousel_structure_generator.py
- competitor_analyzer.py
- content_audit.py
- hook_variant_generator.py
- instagram_hashtag_research.py
- reels_script_generator.py
- tiktok_trends_scraper.py
- trend_adapter.py
- trend_tracker.py

---

## Acceptance Criteria

- [ ] Todos os 19 scripts listados na seção "Scripts de Automação" do README
- [ ] Cada script com descrição e comando de uso
- [ ] Tabela formatada consistentemente
- [ ] Skill.md também atualizado com a mesma informação

---

## Tasks

- [ ] Analisar cada script não documentado para entender funcionalidade
- [ ] Escrever descrição para cada script
- [ ] Documentar comando de uso para cada script
- [ ] Atualizar tabela no README.md
- [ ] Atualizar Skill.md com as mesmas informações
- [ ] Verificar links e formatacao

---

## Files to Modify

- `README.md`
- `Skill.md`

---

## Notes

Os scripts parecem seguir um padrao consistente de CLI usando argparse ou argumentos posicionais.

---

## Definition of Done

- [ ] README atualizado com todos os 19 scripts
- [ ] Skill.md sincronizado
- [ ] Revisado por outro agente (@qa)
- [ ] Commit feito com mensagem descritiva
