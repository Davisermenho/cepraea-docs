# U03 — Relatório de execução

**Proposta:** PRO-CEPRAEA-DOC-CONS-001 v1.1.0  
**Unidade:** U03 — Reconciliação das informações  
**Data da execução:** 2026-10-17  
**Corpus:** `/home/davis/cepraea-docs/docs/reconciliação`  
**Entrada:** artefatos finais da U02  
**Veredito:** `DONE-U03 SATISFEITO COM RESSALVAS E ENCAMINHAMENTOS`

## Resultado executivo

A U03 foi executada sem alterar os 115 arquivos do corpus e sem iniciar a U04. Foram preparados e validados 27 registros de afirmação; todos foram aceitos pelo contrato, nenhum foi rejeitado e nenhum foi promovido automaticamente a decisão humana vigente. O conjunto contém 10 relações e quatro grupos de divergência material, todos encaminhados para autenticação, verificação ou decisão humana.

O `PASS` da execução técnica não resolve os conflitos. Ele demonstra que os registros usados são estruturados, rastreáveis e limitados ao contexto declarado. As pendências permanecem visíveis no ENT-04 e condicionam qualquer consolidação futura das seções afetadas.

## Contrato, diagnóstico e recuperação

- Contrato versionado: `schemas/u03-claim.schema.json`, versão `1.1.0`.
- Implementação: `scripts/u03_reconcile.py` e verificação cruzada por `scripts/u03_verify.py`.
- Saída original preservada: `evidence/U03-agent-output-original.jsonl`, SHA-256 `3ca7bba8c49980df294988e2dd3aab7546a9cc1183029df22ebfbe6dcc1bb76d`.
- Limite ROP-002 definido antes da execução: no máximo **uma** tentativa automática de recuperação por registro.
- Execução real: 27 registros aceitos na tentativa 0; zero correções e zero rejeições.
- T15 controlado: JSON inválido, campo ausente, enum inválido, referência inexistente, registro corrigido e registro persistentemente inválido produziram os resultados esperados; o persistentemente inválido foi excluído.

Conformidade estrutural não foi tratada como prova semântica. A validação percorreu sintaxe, esquema, referências, evidência e autoridade; os resultados de cada estágio permanecem em `evidence/U03-validation-diagnostics.json`.

## Cobertura e suficiência contextual

| Dimensão | Resultado |
| --- | ---: |
| Fontes processadas na U02 | 115 |
| Estado U02 | 95 completas; 20 parciais |
| Fontes efetivamente selecionadas na U03 | 7 |
| Afirmações validadas | 27 |
| Segmentos U02 efetivamente usados | 18 |
| Locators de linha usados | 27 |
| Conclusões suficientes no escopo | 20 |
| Conclusões parciais | 7 |

A seleção foi dirigida às informações necessárias aos documentos candidatos e às divergências materiais identificadas. Ela não constitui varredura semântica infalível nem demonstra inexistência de relações não recuperadas.

Dois trechos anteriores ao primeiro título Markdown — `CLM-U03-0006` e `CLM-U03-0009` — constavam do conteúdo integral extraído pela U02, mas não receberam `segment_id` na segmentação Markdown. A U03 não inventou os segmentos: registrou a limitação e validou os trechos por hash da fonte, `extraction_id`, locator e linhas no conteúdo extraído. Essa lacuna da segmentação anterior é materialmente relevante, mas não bloqueia a rastreabilidade dos dois registros.

## Principais divergências encaminhadas

### DVG-U03-001 — Vigência da Constituição e do Current State Index

- A Constituição traz metadado `STATUS: RASCUNHO`, mas seu corpo reivindica autoridade soberana e precedência absoluta.
- O Current State Index traz `STATUS: RASCUNHO` no cabeçalho e registra o mesmo File ID como `ATIVO` no catálogo incorporado.
- Encaminhamento: decidir versões, status, ato de aprovação e precedência verificáveis. O prefixo `[ATIVO]` não foi aceito como prova de aprovação.

### DVG-U03-002 — Estado real de implementação e infraestrutura

- O PRD candidato declara o produto em concepção e nenhuma funcionalidade como implementada, testada, lançada ou operacional.
- O relatório de execução afirma publicação de dez artefatos e infraestrutura totalmente modelada, testada e pronta para implantação.
- Encaminhamento: identificar ambiente, commit, projeto Supabase e evidências observáveis antes de consolidar qualquer estado operacional. Relato e ausência de prova foram mantidos distintos.

### DVG-U03-003 — Stack e capacidades técnicas abertas

- Next.js/Vercel/Supabase aparece como proposta ou histórico.
- React/TypeScript/Vite/Supabase aparece como snapshot sem autoridade final verificada.
- Offline, autenticação, notificações e implantação permanecem sem solução física eleita pelo PRD.
- Encaminhamento: decisão humana de arquitetura; nenhuma stack foi escolhida pela U03.

### DVG-U03-004 — Autenticidade e escopo de B-01/B-02

- B-01 e B-02 foram localizadas como transcrições no PRD.
- A fonte primária indicada para B-01 não foi localizada no corpus processado; o próprio PRD declara B-02 não autenticada independentemente.
- Encaminhamento: preservar/autenticar as fontes primárias e confirmar os limites entre checkpoint D-5 normal e perda de quórum pós-confirmação.
- Resultado epistemológico: as transcrições foram aceitas como `REGRA_DOCUMENTADA`; nenhuma foi promovida a `DECISÃO_HUMANA` verificada.

## Entregáveis

| Entregável | Arquivo principal | SHA-256 |
| --- | --- | --- |
| ENT-03 — Registro de evidências e afirmações | `ENT-03-registro-evidencias-afirmacoes.jsonl` | `1b4a14be24777175ea92897228b9d983f151ea2e929879f855d42c733f35a54e` |
| ENT-04 — Divergências e decisões | `ENT-04-divergencias-decisoes.json` | `059acad66a692658778754040aa5efa410e5a6fd2f5a572b5ba2c0e6dab05386` |
| ENT-05 — Mapa de consolidação | `ENT-05-mapa-consolidacao.json` | `d9bb7e6754db01ece68f470fe150871f28dedb189ba421483b0cdfee6c29fc4e` |

Cada entregável também possui uma visualização Markdown. O ENT-05 declara `publication_authorized=false` e serve apenas como mapa para uma eventual U04 autorizada e condicionada às pendências.

## Testes e evidências

| Teste | Resultado | Evidência principal |
| --- | --- | --- |
| T04 — Preservação | PASS | 115/115 arquivos inalterados no ciclo e contra o baseline U01 |
| T05 — Evidência válida | PASS | Caso controlado e 27/27 registros reais validados |
| T06 — Evidência inválida | PASS | Trecho adulterado rejeitado com `EVIDENCE_MISMATCH` |
| T08 — Autoridade | PASS | Sem aprovação automática; zero decisões humanas não verificadas aceitas |
| T09 — Contradição | PASS | Quatro grupos preservados e encaminhados |
| T10 — Rastreabilidade | PASS | 27/27 registros; zero referências ausentes |
| T11 — Publicação não autorizada | PASS | `publication_authorized=false`; U04 não iniciada |
| T13 — Reexecução | PASS | Reexecução real equivalente; hashes idênticos; IDs únicos |
| T14 — Interrupção | PASS | Caso controlado impede falso PASS parcial |
| T15 — Contrato/recuperação | PASS | Parada finita em uma tentativa; originais e diagnósticos preservados |
| T16 — Normalização | PASS | Exato, normalizado e diferença semântica distinguidos |
| T17 — Contexto | PASS com limitação explícita | Coberturas separadas; dois locators sem `segment_id` documentados |
| T18 — Agrupamento | PASS | Questões agrupadas sem fundir evidências nem resolver conflitos |

T01–T03 pertencem à U01. T07 e T19 foram executados na U02 e seus resultados/limitações foram herdados. T12 não se aplica porque não houve autorização de publicação. O detalhamento está em `evidence/U03-controlled-test-results.json`, `evidence/U03-test-applicability.json`, `evidence/U03-final-validation.json` e nos dois registros de T04.

## Avaliação de DONE-U03

| Critério | Avaliação |
| --- | --- |
| Informações necessárias identificadas e rastreáveis | SATISFEITO no escopo declarado; 27 registros e mapa de consolidação |
| Registros usados cumprem o contrato | SATISFEITO; 27 aceitos, zero rejeitados |
| Falhas estruturais tratadas ou excluídas | SATISFEITO; mecanismo verificado; nenhuma falha na execução real |
| Divergências materiais resolvidas ou encaminhadas | SATISFEITO por encaminhamento explícito de quatro grupos |
| Conclusões não excedem o contexto | SATISFEITO com sete classificações `PARCIAL` e limitações registradas |
| Nenhuma interpretação promovida automaticamente | SATISFEITO; zero resolução automática e zero decisão humana não verificada aceita |

Assim, `DONE-U03` está satisfeito **com ressalvas e encaminhamentos**. Isso não aprova documentos, não resolve as quatro decisões pendentes e não autoriza publicação. A U04 não foi executada.
