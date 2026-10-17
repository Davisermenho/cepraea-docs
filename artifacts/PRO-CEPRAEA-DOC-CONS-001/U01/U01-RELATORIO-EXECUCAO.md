# U01 — Relatório de Execução

**Proposta:** PRO-CEPRAEA-DOC-CONS-001 v1.1.0  
**Unidade:** U01 — Inventário e Identificação  
**Data:** 2026-10-16  
**Corpus:** `/home/davis/cepraea-docs/docs/reconciliação`  
**Veredito:** **PASS — DONE-U01 SATISFEITO**

## Limites da execução

- A aprovação A1 foi considerada concedida conforme instrução do responsável.
- A execução limitou-se à U01; U02 não foi iniciada.
- Nenhum rótulo ou nome de arquivo foi usado para atribuir autoridade documental.
- Os arquivos do corpus foram abertos somente para leitura.
- Todos os resultados foram gravados fora do corpus, em `artifacts/PRO-CEPRAEA-DOC-CONS-001/U01`.
- `SUPPORTED` no manifesto significa identificação técnica na U01; não significa que um extrator foi homologado para a U02.

## Inspeção do código existente

A busca por arquivos Python e por nomes relacionados a `U01`, `inventory` e `inventário` não encontrou código de inventário no projeto acessível. O diretório `.git` está vazio neste ambiente e, portanto, não forneceu histórico recuperável. Foi criada uma implementação mínima, sem dependências externas, em `scripts/u01_inventory.py`, acompanhada dos testes em `tests/u01`.

## Resultado do corpus

| Medida | Resultado |
| --- | ---: |
| Entradas de arquivo registradas | 115 |
| Arquivos legíveis e com SHA-256 | 115 |
| Arquivos inacessíveis | 0 |
| Exclusões | 0 |
| Diretórios registrados | 1 (raiz do corpus) |
| Subdiretórios encontrados | 0 |
| Bytes legíveis | 50.566.245 |
| Formatos pendentes/desconhecidos | 0 |
| Erros de validação de formato | 5 |
| Grupos de duplicatas binárias | 0 |
| Arquivos integrantes de grupos duplicados | 0 |

### Distribuição de formatos

| Formato identificado | Arquivos |
| --- | ---: |
| Markdown | 79 |
| JSON | 8 |
| YAML | 8 |
| SQL | 6 |
| PDF | 6 |
| Texto sem extensão detectado como UTF-8 | 5 |
| Texto `.txt` | 2 |
| PowerPoint Open XML | 1 |

### Erros e pendências registrados

Cinco arquivos são legíveis e possuem tamanho e SHA-256, mas falharam na validação sintática JSON. Os originais não foram corrigidos:

| Fonte | Diagnóstico |
| --- | --- |
| `Contêineres-de-desenvolvimento (3).json` | `JSONDecodeError`, linha 39, coluna 1935 |
| `HISTÓRICO-Chat-00-—-Intake-e-objetivos (1).json` | `JSONDecodeError`, linha 114, coluna 3748 |
| `HISTÓRICO-Chat-01-—-Elicitação.json` | `JSONDecodeError`, linha 689, coluna 12595 |
| `HISTÓRICO-Chat-04-—-Requisitos.json` | `JSONDecodeError`, linha 15, coluna 1386 |
| `Verificar-afirmações-da-IA.json` | `JSONDecodeError`, linha 39, coluna 2556 |

Essas falhas estão registradas individualmente como `REGISTERED_WITH_FORMAT_ERROR` no ENT-01. Elas não impedem a identificação física exigida pela U01, mas deverão ser consideradas antes de qualquer alegação de extração integral na U02.

## Testes aplicáveis

As entradas e os resultados esperados foram definidos em `tests/u01/test_cases.json` antes da execução.

| Teste | Entrada controlada e oráculo | Resultado |
| --- | --- | --- |
| T01 — Inventário | Dois arquivos, incluindo um em subdiretório; esperados dois caminhos e zero erros de leitura | PASS |
| T02 — Integridade | Bytes UTF-8 `abc`; SHA-256 esperado `ba7816bf...15ad` | PASS |
| T03 — Duplicatas | Dois arquivos idênticos e um diferente; esperado um grupo contendo apenas os dois idênticos | PASS |
| T04 — Preservação | Dois arquivos; esperadas listas vazias de adições, remoções e alterações | PASS |
| T04 — corpus real | Snapshots antes/depois dos 115 arquivos; esperadas listas vazias de adições, remoções e alterações | PASS |
| T13 — Reexecução | Duas gerações com entradas imutáveis; esperado conteúdo equivalente e quatro saídas sem duplicação | PASS |
| T14 — Interrupção | Manifesto parcial inválido seguido de reexecução; esperada substituição por quatro saídas completas e manifesto válido | PASS |

T05–T12 e T15–T19 foram avaliados como `NAO_APLICAVEL` à U01: seus oráculos dependem de evidências semânticas, publicação, contrato de afirmações, normalização, segmentação, recuperação, divergências ou extração, que pertencem às unidades posteriores. O PASS dos testes executados comprova somente os comportamentos objetivos exercitados. O resultado detalhado está em `evidence/U01-test-results.json`; a comparação do corpus real está em `evidence/T04-corpus-real.json`.

## Avaliação de DONE-U01

| Critério | Evidência | Estado |
| --- | --- | --- |
| Todos os arquivos no escopo possuem registro ou exclusão justificada | 115 entradas no ENT-01; 115 legíveis; 0 exclusões | PASS |
| Caminho relativo, formato, tamanho e SHA-256 registrados | ENT-01 JSON/CSV com campos preenchidos para 115 arquivos | PASS |
| Falhas de leitura, erros e formatos pendentes registrados | 0 falhas de leitura; 5 erros de sintaxe JSON registrados; 0 formatos desconhecidos | PASS |
| Duplicatas binárias identificadas sem eliminação | Comparação byte a byte após agrupamento por tamanho e SHA-256; nenhum grupo encontrado | PASS |
| Originais preservados | Snapshot anterior e posterior: 0 adicionados, 0 removidos, 0 alterados, 115 inalterados | PASS |
| Saídas separadas dos originais | Saídas em `artifacts/PRO-CEPRAEA-DOC-CONS-001/U01` | PASS |

Não há bloqueio crítico para DONE-U01. Os cinco JSON sintaticamente inválidos permanecem como pendências explícitas para eventual processamento posterior. Este veredito não aprova documentos, não estabelece vigência e não autoriza avanço automático para U02.

## Entregáveis e evidências

- `ENT-01-manifesto-corpus.json` — manifesto estruturado, resumo, diretórios, arquivos, erros, exclusões e grupos duplicados.
- `ENT-01-manifesto-corpus.csv` — visão tabular do manifesto.
- `ENT-02-indice-fontes.md` — índice humano das 115 fontes.
- `ENT-02-indice-fontes.csv` — índice tabular reutilizável.
- `evidence/corpus-before.json` e `evidence/corpus-after.json` — snapshots de preservação.
- `evidence/U01-test-results.json` — entradas esperadas e resultados observados dos testes aplicáveis.
- `evidence/U01-test-applicability.json` — avaliação estruturada de aplicabilidade de T01–T19.
- `evidence/T01-T04-results.json` — registro da primeira execução isolada de T01–T04.
- `evidence/T04-corpus-real.json` — resultado da preservação do corpus real.
- `evidence/final-validation.txt` — checagem cruzada final entre manifesto, CSV, índice, snapshot e testes.
- `evidence/*-stdout.txt` — saídas preservadas dos scripts.
