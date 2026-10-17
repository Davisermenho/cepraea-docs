# U03 — Relatório de reprocessamento após U02 v1.1.0

**Data:** 2026-10-17  
**Entrada corrigida:** `artifacts/PRO-CEPRAEA-DOC-CONS-001/U02-v2/generated`  
**Saída histórica preservada:** `artifacts/PRO-CEPRAEA-DOC-CONS-001/U03`  
**Saída reprocessada:** `artifacts/PRO-CEPRAEA-DOC-CONS-001/U03-v2`  
**Veredito técnico:** **PASS**

## Dependências afetadas

A versão da extração passou de 1.0.0 para 1.1.0. Como o `extraction_id` incorpora essa versão e os IDs sequenciais foram substituídos, as referências técnicas das 27 afirmações ficaram obsoletas. Por isso, todas as 27 afirmações foram reconstruídas e revalidadas; nenhuma referência antiga foi reaproveitada automaticamente.

As duas afirmações que antes dependiam somente de locators de linha agora possuem segmentos U02 válidos:

- `CLM-U03-0006` — metadado anterior ao primeiro título de `[ATIVO] 20-CURRENT-STATE-INDEX.md`;
- `CLM-U03-0009` — estado do produto anterior ao primeiro título do PRD candidato.

As relações, os quatro grupos de divergência e o mapa de consolidação não dependiam dos IDs físicos para seu conteúdo lógico. Eles foram regenerados e verificados, mas não foram reinterpretados nem resolvidos.

## Resultado

| Medida | Resultado |
| --- | ---: |
| Afirmações preparadas/aceitas/rejeitadas | 27 / 27 / 0 |
| Relações | 10 |
| Grupos de divergência | 4 |
| Resoluções automáticas | 0 |
| Locators sem segmento U02 | 0 |
| IDs antigos de segmento reutilizados | 0 |
| Reexecução real equivalente | sim |

O ENT-03 mudou porque seus 27 registros agora apontam para a nova versão de extração e para IDs determinísticos. Os hashes do ENT-04 e do ENT-05 permaneceram idênticos à versão histórica, confirmando que a correção técnica não alterou relações, divergências ou instruções de consolidação.

## Verificação

- A suíte controlada da U03 emitiu `PASS` para T05, T06, T08, T09, T10, T13–T18.
- O pipeline foi executado duas vezes com as mesmas entradas; os hashes dos seis entregáveis foram idênticos.
- O verificador independente emitiu `PASS`, com 27 afirmações aceitas, zero diagnósticos, zero IDs duplicados, zero decisão humana não verificada e `publication_authorized=false`.
- O comparador entre versões emitiu `PASS`: nenhum hash de conteúdo extraído mudou, nenhuma afirmação desapareceu, os dois locators pendentes foram resolvidos por segmentos e nenhuma referência física obsoleta foi reutilizada.

## Limites preservados

O reprocessamento não decide as quatro divergências já encaminhadas, não aprova documentos, não escolhe arquitetura e não autoriza publicação. A cobertura textual integral da U02 não foi apresentada como cobertura semântica integral do corpus.

## Evidências principais

- `evidence/U03-controlled-test-results.json`
- `evidence/U03-run-summary-first.json`
- `evidence/U03-run-summary.json`
- `evidence/U03-final-validation.json`
- `evidence/U02-U03-version-comparison.json`
- `generated/U03-context-coverage.json`

