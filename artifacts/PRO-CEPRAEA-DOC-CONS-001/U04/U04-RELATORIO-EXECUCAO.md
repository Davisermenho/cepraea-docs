# U04 — Relatório de execução

Data: `2026-10-17`  
Unidade: `U04 — Consolidação dos documentos candidatos`  
Veredito emitido pelo validador: `PASS`  
Publicação oficial: `NÃO AUTORIZADA`

## Entradas controladas

- 27 registros aceitos da U03-v2, hash do ENT-03: `fc29b447f31e314158188d56de3f2c995bab8b73e1d1db28123334af01d9d05c`.
- Decisões diretas do responsável, registradas como A2 em `input/DECISOES-RESPONSAVEL-2026-10-17.md`, SHA-256 `6755b853b12649a4f57bef8248341e12e1eef130729c31731679d554dd679e45`.
- Registro estruturado das decisões em `input/decision-registry.json`; A3 explicitamente ausente.
- Inspeção técnica somente leitura em `input/technical-inspection.json`, SHA-256 `c4fabb2927fbfab71ceed3a4bcfe4a4514fca4de347fa86f60b708740bd3829f`.
- Corpus original controlado pelo manifesto U01, com 115 arquivos.

## Resultado da inspeção autorizada

O repositório real identificado foi `Davisermenho/CEPRAEA`, branch `main`, commit `73462b6098dc89bc00fa55bea5f6f26980889173`. A inspeção estática confirmou uma base React 19, TypeScript, Vite, PWA, cliente Supabase, testes Vitest/Playwright e configuração Vercel. Isso sustenta apenas `VALIDADO_ESTATICAMENTE` para os arquivos observados; não sustenta execução local, implantação nem aceitação humana.

O projeto Supabase `fcnyjmrknqaomamdzabt` (`CEPRAEA`, `us-east-1`) foi localizado com estado `INACTIVE`. A leitura de tabelas e migrações terminou por timeout de conexão. Nenhuma restauração, migração, alteração de banco, implantação ou outra mutação foi executada. Resultados vazios de advisors não foram tratados como prova de ausência de problemas, pois o banco não pôde ser introspectado.

## Disposição das divergências da U03

| Questão | Disposição na U04 | Limite preservado |
| --- | --- | --- |
| Vigência da Constituição e do Current State Index | Resolvida quanto à regra de autoridade por `DEC-U04-001` | As versões exatas examinadas continuam `AGUARDANDO_APROVACAO`; não há precedência ativa |
| Estado real de implementação e infraestrutura | Parcialmente verificada e encaminhada | Repositório comprovado no commit; execução, esquema e alvo permanecem não verificados |
| Stack e capacidades técnicas | Requisitos e critérios resolvidos por `DEC-U04-003` | A escolha arquitetural definitiva permanece pendente de decisão humana |
| Autenticidade de B-01/B-02 e fluxo D-5 | A regra aplicável foi substituída pela decisão humana direta `DEC-U04-002` | A autenticidade histórica das transcrições anteriores não foi retroativamente declarada |

## Entregáveis

- `generated/ENT-06A-governanca-autoridade.candidato.md` — governança, autoridade e versões exatas.
- `generated/ENT-06B-requisitos-produto-d5.candidato.md` — requisitos e regra D-5 ratificada.
- `generated/ENT-06C-arquitetura-estado-tecnico.candidato.md` — comparação e limites do estado técnico.
- `generated/ENT-07-mapa-origem-destino.json` e `.md` — 14 afirmações e seus fundamentos.
- `generated/ENT-08-pendencias-revisao.json` e `.md` — cinco pendências preservadas.
- `generated/approval-registry.json` — registro único com versões e hashes atuais.
- `generated/U04-run-manifest.json` — hashes dos entregáveis e trava de publicação.

## Registro único de aprovação

| Documento | Versão | SHA-256 | Estado | Vigência/precedência |
| --- | --- | --- | --- | --- |
| Constituição do Projeto | v4.0.0 | `8f214ce8b63a21df5abecc5616ac3af5bd55dfa85a4dc6b475f39b3ef94168f5` | `AGUARDANDO_APROVACAO` | não ativa |
| Current State Index | v1.0.0 | `491d2defb50a33c6b247807b6538978ff1e669c6b2ab3ecc930497d6845d9e9b` | `AGUARDANDO_APROVACAO` | não ativa |

Os campos de responsável aprovador e data de vigência permanecem nulos. O papel declarado na mensagem autoriza as decisões A2 registradas, mas não aprova automaticamente estas versões nem concede A3.

## Testes e validação

Os resultados esperados foram registrados em `tests/u04/test_cases.json` antes da geração produtiva.

| Teste | Resultado final emitido pelo código |
| --- | --- |
| T08 — autoridade | `PASS` |
| T09 — contradição/pendência | `PASS` |
| T10 — rastreabilidade | `PASS` |
| T11 — publicação não autorizada | `PASS` |
| T13 — reexecução | `PASS` |
| T14 — interrupção e retomada | `PASS` |

O primeiro ciclo teve T14 `FAIL` por ordem incorreta de observação no próprio teste. A correção e ambos os resultados estão preservados em `evidence/U04-test-history.md`. O segundo ciclo terminou 6/6 `PASS`.

A validação final independente em `evidence/U04-final-validation.json` emitiu `PASS`: três candidatos, 14 afirmações, zero referência ausente, zero duplicação normativa, zero hash divergente, cinco pendências, A3 ausente e publicação bloqueada.

O corpus permaneceu íntegro: 115 arquivos verificados, zero alterado, zero ausente e zero inesperado.

## Pendências que não impedem DONE-U04

1. Aprovação formal das versões exatas da Constituição e do Current State Index.
2. Escolha humana da arquitetura definitiva.
3. Verificação atual do custo operacional contra a referência de R$ 50/mês.
4. Ativação autorizada ou disponibilização de um alvo para verificar esquema, migrações, testes e comportamento; nenhuma ativação foi autorizada nesta execução.
5. U05 e A3 para verificar e eventualmente aprovar versões exatas dos candidatos.

## Veredito de unidade

`DONE-U04 = SATISFEITO` no escopo da proposta: os documentos candidatos têm responsabilidades distintas, as 14 afirmações normativas possuem fundamento rastreável, decisões ainda pendentes continuam explicitamente pendentes e nenhuma saída aparece como oficial ou aprovada.

Este veredito não equivale a A3, não aprova arquitetura, não comprova funcionamento do produto e não autoriza publicação ou alteração de produção.
