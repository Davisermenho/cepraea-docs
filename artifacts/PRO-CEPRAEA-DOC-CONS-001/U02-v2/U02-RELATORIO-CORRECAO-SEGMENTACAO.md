# U02 v1.1.0 — Relatório de correção da segmentação

**Data:** 2026-10-17  
**Corpus:** `/home/davis/cepraea-docs/docs/reconciliação`  
**Entrada:** manifesto aprovado da U01, com 115 fontes  
**Saída histórica preservada:** `artifacts/PRO-CEPRAEA-DOC-CONS-001/U02`  
**Saída corrigida:** `artifacts/PRO-CEPRAEA-DOC-CONS-001/U02-v2`  
**Veredito técnico:** **PASS**

## Causa corrigida

A implementação anterior redefinia o início da seção ao encontrar o primeiro título Markdown sem antes emitir o intervalo entre o início do texto e esse título. Títulos aparentes dentro de blocos cercados de código também eram interpretados como títulos documentais. Além disso, não existia uma verificação global que exigisse reconstrução integral de cada unidade, e os IDs `SEG-NNNNNNNN` dependiam da ordem total de processamento.

A versão 1.1.0 corrige essas condições na origem:

- todo texto não vazio é dividido em intervalos contíguos `[início, fim)`;
- offsets representam índices de caracteres Unicode do `str` Python, declarados como `UNICODE_CODE_POINT`, nunca bytes UTF-8;
- o preâmbulo anterior ao primeiro título forma um segmento com hierarquia vazia;
- cercas Markdown com crases ou tis não produzem títulos internos;
- separadores, espaços e quebras de linha pertencem a algum intervalo;
- a subdivisão respeita 12.000 caracteres sem descartar conteúdo;
- o ID do segmento é o SHA-256 determinístico da fonte, extração, unidade, intervalo e conteúdo;
- a execução é interrompida antes dos entregáveis finais se a partição falhar.

## Reprodução anterior à correção

Os resultados esperados foram declarados em `tests/u02/test_cases.json` antes da execução discriminante. A execução da implementação anterior foi preservada em `evidence/U02-tests-before-fix.json` e emitiu `FAIL` geral. Falharam os casos de preâmbulo, título após bloco longo, título aparente em bloco de código, partição na reexecução com preâmbulo, independência dos IDs e convenção explícita de offsets.

A comparação posterior sobre o corpus mostrou que a saída histórica tinha 34 de 175 unidades sem reconstrução exata, somando 101.661 posições de caracteres ausentes do índice de segmentos. Esses caracteres continuavam preservados nos textos extraídos; a falha estava na segmentação e na recuperação, não na extração bruta.

## Testes após a correção

O executor `tests/u02/test_u02_extract.py` emitiu `all_passed=true` para 20 casos. Os novos casos T20–T30 cobriram:

- Markdown com preâmbulo;
- documento sem título;
- documento iniciado por título;
- múltiplos títulos e hierarquia;
- título após bloco com mais de 12.000 caracteres;
- título aparente dentro de bloco cercado de código;
- entrada vazia;
- comprimentos 11.999, 12.000, 12.001 e 24.000;
- reexecução com entrada idêntica;
- estabilidade do ID diante da inserção de outra fonte;
- offsets com caracteres multibyte em UTF-8.

O `PASS` foi emitido pelo código e está em `evidence/U02-controlled-test-results.json`.

## Reprocessamento do corpus

| Medida | Resultado |
| --- | ---: |
| Fontes inventariadas/processadas | 115 / 115 |
| Extrações completas/parciais/falhas | 95 / 20 / 0 |
| Unidades textuais verificadas | 175 |
| Unidades não vazias/vazias | 171 / 4 |
| Segmentos corrigidos | 7.388 |
| Unidades com lacuna ou sobreposição | 0 |
| IDs duplicados | 0 |
| Referências | 773 |

O validador independente `scripts/u02_verify.py` emitiu `PASS`. Para cada unidade, verificou início em zero, adjacência exata, término no comprimento do texto, reconstrução literal, unicidade dos IDs e limite de tamanho. O registro completo está em `generated/U02-segmentation-validation.json`; a verificação cruzada está em `evidence/U02-final-validation.json`.

## Comparação com a versão histórica

- 7.314 segmentos mantiveram a mesma fonte, unidade, intervalo e hash de conteúdo, recebendo IDs determinísticos novos.
- 95 intervalos lógicos antigos deixaram de existir e 74 intervalos corrigidos foram criados; a redução líquida decorre principalmente de títulos aparentes em blocos de código que antes fragmentavam conteúdo.
- 38 fontes tiveram alguma mudança de limites; a lista integral está no comparador versionado.
- Os hashes dos 115 conteúdos extraídos permaneceram iguais entre as versões.
- As referências passaram de 774 para 773. Não houve perda de chave semântica: uma mesma referência `vscode-webview` não resolvida, repetida em `Alinhamento-de-IA.md`, passou de duas ocorrências indexadas em segmentos distintos para uma chave deduplicada dentro de um único segmento.

## Preservação e limites

O teste de preservação real emitiu `PASS`: 115 arquivos inalterados, sem adições, remoções ou mudanças no corpus. Os cinco JSON inválidos permanecem inalterados e continuam registrados como extrações parciais. Nenhum documento foi aprovado, nenhum requisito de produto foi alterado e nenhuma migração, deploy ou escolha de arquitetura foi realizada.

Este `PASS` comprova cobertura textual integral das 175 unidades extraídas nesta execução. Ele não comprova cobertura semântica integral dos 115 documentos, nem recupera conteúdo visual que os extratores já classificaram como limitação.

## Evidências principais

- `evidence/U02-tests-before-fix.json` — reprodução do defeito.
- `evidence/U02-controlled-test-results.json` — testes após a correção.
- `generated/U02-segmentation-validation.json` — invariantes por unidade.
- `evidence/U02-final-validation.json` — verificação cruzada final.
- `evidence/T04-corpus-preservation.json` — preservação dos originais.
- `../U03-v2/evidence/U02-U03-version-comparison.json` — comparação integral entre versões e impacto na U03.

