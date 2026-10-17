# Histórico de execução dos testes U04

## Ciclo 1 — bloqueado

- Resultado emitido pelo código: `FAIL`.
- Casos: 5 `PASS`, 1 `FAIL`.
- Falha: T14, campo `interrupted_not_published` observado como `false`, esperado `true`.
- Diagnóstico: o teste consultava a inexistência do diretório de publicação depois de executar a retomada limpa, que legitimamente já havia criado o diretório.
- Correção: capturar o estado posterior à interrupção antes da reexecução limpa. O oráculo e o código produtivo não foram alterados.

## Ciclo 2 — aceito

- Resultado emitido pelo código: `PASS`.
- Casos: 6/6 `PASS` (`T08`, `T09`, `T10`, `T11`, `T13`, `T14`).
- Evidência estruturada: `U04-controlled-test-results.json`.

## Execução produtiva e reexecução

- Primeira geração: `PASS`, `published=true`, `equivalent_existing=false`.
- Reexecução com as mesmas entradas: `PASS`, `published=true`, `equivalent_existing=true`.
- Nenhum arquivo existente divergente foi sobrescrito.

## Validação final independente

- Resultado emitido por `scripts/u04_verify.py`: `PASS`.
- Erros: nenhum.
- Evidência estruturada: `U04-final-validation.json`.
