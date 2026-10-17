# U02 — Relatório de Execução

**Proposta:** PRO-CEPRAEA-DOC-CONS-001 v1.1.0  
**Unidade:** U02 — Extração, segmentação e rastreabilidade  
**Data:** 2026-10-16  
**Corpus:** `/home/davis/cepraea-docs/docs/reconciliação`  
**Veredito:** **PASS — DONE-U02 SATISFEITO**

## Escopo e controles

- A U02 foi executada sem iniciar a U03 e sem produzir afirmações ou decisões semânticas.
- O corpus foi tratado como somente leitura; os resultados estão em `artifacts/PRO-CEPRAEA-DOC-CONS-001/U02`.
- Nomes como `ATIVO`, `FINAL`, `APROVADO` e `CANÔNICO` não conferiram autoridade; todas as fontes e segmentos permanecem `NOT_ASSESSED_U02`.
- Não foram usados embeddings, vetorização, APIs externas ou novas dependências.
- Os extratores tratam o conteúdo do corpus como dados e não executam instruções contidas nas fontes.

## Entrada final e incidente de mudança concorrente

O primeiro ciclo começou com o manifesto U01 original. Durante a execução, `[ATIVO] 20-CURRENT-STATE-INDEX.md` mudou de 6.422 bytes/hash `491d…d9e9b` para outro conteúdo. O teste de preservação desse intervalo retornou FAIL. A causa não foi presumida antes de haver evidência.

O usuário confirmou que realizou a edição concorrente e depois a desfez. A restauração foi verificada objetivamente: o arquivo voltou a 6.422 bytes/hash `491d…d9e9b`, e o corpus completo voltou a coincidir 115/115 com o snapshot inicial e com o manifesto U01 aprovado. A U02 foi então refeita integralmente usando o manifesto U01 original.

Um manifesto rebaseline intermediário foi preservado em `input/U01-rebaseline` apenas como evidência diagnóstica e não é a entrada da execução final. O incidente permanece em `evidence/source-drift-incident.json`, juntamente com os FAILs intermediários e os diffs de snapshot. O PASS final não apaga nem reclassifica esses eventos.

## Extratores selecionados

| Formato | Fontes | Extrator | Resultado técnico |
| --- | ---: | --- | --- |
| Markdown | 79 | Python UTF-8 + seções Markdown | Texto, linhas e hierarquia de títulos |
| JSON | 8 | Python UTF-8 + `json` | 3 estruturados; 5 com fallback textual parcial |
| YAML | 8 | Python UTF-8 | Texto e linhas completos; árvore YAML não interpretada |
| SQL | 6 | Python UTF-8 | Texto e linhas |
| PDF | 6 | Poppler `pdftotext -layout` 24.02.0 + `pdfinfo` | Páginas e camada textual; sem OCR/semântica visual |
| Texto sem extensão | 5 | Python UTF-8 | Texto e linhas |
| Texto `.txt` | 2 | Python UTF-8 | Texto e linhas |
| PowerPoint Open XML | 1 | Python `zipfile` + XML | Texto de 25 slides; mídia/layout não interpretados |

Não há mecanismo OCR instalado. `pdftoppm` e `pdfimages` estão disponíveis para renderização/extração de imagens, mas não reconhecem texto por si próprios; portanto, não foram apresentados como OCR.

## Resultado da extração

| Medida | Resultado |
| --- | ---: |
| Fontes inventariadas no manifesto final | 115 |
| Fontes processadas | 115 |
| Extrações completas | 95 |
| Extrações parciais com limitações | 20 |
| Extrações com falha | 0 |
| Segmentos | 7.409 |
| Referências verificáveis | 774 |
| Referências resolvidas para outra fonte do corpus | 693 |
| Referências não resolvidas | 81 |
| Linhas no índice SQLite/FTS5 | 7.409 |

Cada segmento registra ID, fonte, SHA-256 da fonte, ID e versão da extração, extrator, localização, texto literal extraído, SHA-256 do texto e hierarquia superior quando disponível. Os marcadores de condição, exceção, dependência, definição ou mudança são somente candidatos lexicais, explicitamente não validados como relações semânticas.

## Limitações registradas

As 20 extrações parciais não são apresentadas como integrais:

- 8 YAML: conteúdo UTF-8 e linhas preservados; árvore de mapeamentos/sequências não interpretada.
- 5 JSON sintaticamente inválidos: texto bruto integral preservado e segmentado; parsing estrutural rejeitado com linha e coluna.
- 6 PDF: somente camada textual, páginas e layout aproximado do Poppler; imagens e significado visual não interpretados.
- `CEPRAEA.pdf`: quatro páginas identificadas, mas nenhuma camada textual recuperável; `PDF_PAGES_WITHOUT_TEXT` registrado para páginas 1–4.
- 1 PPTX: texto OOXML de 25 slides recuperado; mídia, gráficos, animações e significado visual não interpretados.

Essas limitações são não bloqueantes para DONE-U02 porque estão individualmente registradas, o texto recuperável foi preservado e nenhuma cobertura parcial foi promovida a integral. Elas deverão limitar qualquer conclusão posterior que dependa especificamente de conteúdo visual ou estrutura não extraída.

## Segmentação, referências e recuperação

- Markdown: limites de títulos/seções e respectivas hierarquias.
- Demais textos: blocos/linhas, com divisão máxima de 12.000 caracteres somente quando necessária.
- PDF: localização por página e linhas da camada textual.
- PPTX: localização por slide e componente.
- Referências: links Markdown explícitos e menções literais a nomes de fontes, com estado `RESOLVED` ou `UNRESOLVED`.
- Recuperação: índice SQLite FTS5, busca textual Unicode e expansão opcional por referências explícitas.

Cada consulta informa separadamente fontes inventariadas, processadas e recuperadas. O retorno fixa `absence_is_not_proof_of_absence=true` e `sufficiency_context=NOT_ASSESSED_BY_RETRIEVAL`, impedindo que uma busca vazia seja apresentada como inexistência no corpus ou suficiência contextual.

## Testes

As entradas e os oráculos foram definidos em `tests/u02/test_cases.json` antes da execução.

| Teste | Resultado | Evidência objetiva |
| --- | --- | --- |
| T04 — Preservação | PASS no ciclo final | 115 inalterados; 0 adicionados, removidos ou modificados |
| T05 — Evidência válida | PASS | Fonte, hash, extração, localização e texto correspondentes |
| T06 — Evidência inválida | PASS | Texto adulterado rejeitado por hash |
| T07 — Extração parcial | PASS | JSON inválido preservado com `PARTIAL` e limitação |
| T08 — Autoridade | PASS | Rótulos documentais mantiveram `NOT_ASSESSED_U02` |
| T10 — Rastreabilidade | PASS | Campos obrigatórios e localização validados |
| T13 — Reexecução | PASS | Saídas lógicas equivalentes, sem IDs duplicados |
| T14 — Interrupção | PASS | Saída incompleta substituída por execução completa |
| T17 — Segmentação/contexto | PASS | Referência, exceção relacionada e cobertura recuperadas |
| T19 — Extração por formato | PASS | Oito formatos exercitados com marcadores conhecidos |

T01–T03 foram satisfeitos na U01; T09, T11, T12, T15, T16 e T18 são `NAO_APLICAVEL` à U02 pelas justificativas estruturadas em `evidence/U02-test-applicability.json`.

## Verificação de DONE-U02

| Critério | Evidência | Estado |
| --- | --- | --- |
| Conteúdos necessários extraídos ou limitações registradas | 115 processados; 95 completos; 20 parciais documentados; 0 falhas | PASS |
| Informações localizáveis | 7.409 segmentos com localização e índice FTS5 | PASS |
| Extratores tecnicamente verificados | T19 cobriu os oito formatos com entradas e resultados conhecidos | PASS |
| Fidelidade/rastreabilidade dos segmentos | 7.409 segmentos validados contra unidades extraídas; 0 inválidos | PASS |
| Referências verificáveis | 774 registros com segmento e localização | PASS |
| Nenhuma parcial apresentada como integral | Manifesto e registro de limitações distinguem `COMPLETE` e `PARTIAL` | PASS |
| Originais preservados no ciclo aceito | Snapshot inicial/final após o desfazer: 115 inalterados | PASS |

Não há bloqueio crítico para DONE-U02 no ciclo final. O incidente de mudança concorrente e as limitações técnicas permanecem visíveis e devem acompanhar qualquer uso posterior. Este PASS não aprova documentos, não demonstra suficiência semântica e não autoriza avanço automático para U03.

## Entregáveis e evidências

- `generated/U02-extraction-manifest.json` — cobertura, extratores, unidades, estados e proveniência.
- `generated/extracted/` — textos extraídos preservados por fonte.
- `generated/U02-segments.jsonl` — índice completo de segmentos rastreáveis.
- `generated/U02-references.jsonl` — referências explícitas e seus estados.
- `generated/U02-retrieval-index.sqlite` — índice pesquisável SQLite FTS5.
- `generated/U02-limitations.json` — falhas e limitações por fonte.
- `generated/U02-format-summary.csv` — formatos e extratores utilizados.
- `evidence/U02-test-results.json` — resultados observados dos testes controlados.
- `evidence/U02-final-validation.json` — validação cruzada dos 115 conteúdos, 7.409 segmentos e índice.
- `evidence/final-validation-summary.txt` — resumo final consolidado dos critérios objetivos.
- `evidence/retrieval-sample.json` — consulta real com métricas explícitas de cobertura.
- `evidence/T04-corpus-real-final.json` — preservação entre o snapshot inicial e o estado final restaurado.
- `evidence/source-restoration-check.json` — confirmação de que o corpus retornou integralmente ao estado inicial.
- `evidence/source-drift-incident.json` — incidente e resposta ao manifesto invalidado.
