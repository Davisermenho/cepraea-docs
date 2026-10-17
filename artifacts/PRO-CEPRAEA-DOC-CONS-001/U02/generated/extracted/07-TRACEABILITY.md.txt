# TRACEABILITY

> **ARTEFATO CANÔNICO — GATE B FINAL APROVADO**  
> `DOMAIN-MODEL = PASS`; `GATE-B-FINAL = APPROVED` e a fase de Requirements está autorizada.

**Propósito:** manter a cadeia entre intenção, entendimento, requisito, driver, decisão, arquitetura e validação.  
**Estado atual:** rastreabilidade na entrada de Requirements; `Chat 04 — Requirements = AUTHORIZED`; `Proposta de Requirements.md` produzida e atualizada com FR-001..FR-025 / NFR-001..NFR-006 / CON-001..CON-010; Gate C não executado.  
**Versão:** 1.0.  
**Última atualização:** 2026-09-05.
**Fontes canônicas:** `PRODUCT-DOMAIN-SPEC.md` v2.10 e `TRAINING_FLOW_CONTRACT.md` v1.6; proveniência histórica preservada em `Historico.json`.

**Nota de proveniência editorial:** IDs e agrupamentos introduzidos neste artefato são organização `INF`; eles não criam decisões novas e somente apontam para conteúdo substantivo já confirmado ou explicitamente mantido como hipótese/risco/questão aberta.

---

## 0. Estado do processo

```text
GATE-B-KNOWLEDGE = READY_WITH_RISKS
GATE-B-CANONICALIZATION = APPROVED
GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS
ELICITATION-OPEN = NONE
GATE-B-DOMAIN-MODEL = PASS
GATE-B-FINAL = APPROVED
```

Neste estado, `ELICITATION-OPEN = NONE` significa que nenhuma decisão material de produto atualmente conhecida permanece aberta. Se uma fase posterior encontrar uma lacuna que exija nova intenção ou regra de produto, ela deve retornar à elicitação e à autoridade humana, sem ser preenchida por inferência.

Nenhum `FR`, `NFR`, `CON`, `DRV`, `OPT`, `ADR` ou componente arquitetural novo é criado por esta canonicalização.

---

## 1. Cadeia principal

```text
OBJ
 ↓
FACT / RULE / FLOW / CONST / HYP
 ↓
FR / NFR / CON              ← AUTHORIZED; AINDA NÃO FORMALIZADOS
 ↓
DRV
 ↓
OPT
 ↓
ADR
 ↓
COMPONENTE / CAMADA
 ↓
VAL
```

A cadeia abaixo de `FACT/RULE/FLOW/CONST/HYP` permanece deliberadamente vazia nesta etapa.

---

## 2. Matriz Objetivo → entendimento confirmado

| Objetivo | Problema/Fatos | Fluxos | Regras/Conceitos principais | Restrições/Riscos relevantes | Cobertura atual |
|---|---|---|---|---|---|
| OBJ-001 — Devolver tempo e atenção | PROBLEM-001, FACT-002 | FLOW-001 | RULE-009, RULE-010, RULE-020; SUCCESS-001 | CONST-004/005/009/011; RISK-001/002/003 | Suficiente para iniciar Requirements; ainda não convertido |
| OBJ-002 — Operar agenda por exceção e previsibilidade | PROBLEM-001, FACT-004/005 | FLOW-001 | CONCEPT-007/009/012; RULE-004–016, RULE-020–022, RULE-028/029/031 | CONST-004/005/010/011; RISK-001/006 | Suficiente para iniciar Requirements; ainda não convertido |
| OBJ-003 — Preservar informação e histórico confiáveis | PROBLEM-001 | FLOW-001, FLOW-002 | CONCEPT-003–006/011–013; RULE-001–003, RULE-012, RULE-017–019, RULE-022, RULE-027/028/030 | RISK-007/008/010 | Suficiente para iniciar Requirements; ainda não convertido |
| OBJ-004 — Aumentar autonomia das atletas | FACT-001 | FLOW-001 | ACT-002; RULE-002/005/012/023/024/025 | HYP-001; RISK-003/009/010 | Suficiente para conhecimento; risco de adoção aceito e validação prevista no piloto |
| OBJ-005 — Apoiar decisão sem substituir treinador | PROBLEM-001 | FLOW-001, FLOW-002 | DEC-003/013; RULE-013–018; CONCEPT-007/012 | RISK-008 | Suficiente para iniciar Requirements; ainda não convertido |

---

## 3. Matriz Objetivo → Critério de sucesso

| Objetivo | Critérios relacionados | Estado |
|---|---|---|
| OBJ-001 | SUCCESS-001, SUCCESS-005 | `SUCCESS-001` confirmado e permanece o critério principal do MVP; `SUCCESS-005` preserva faixas numéricas anteriores de 8–12 h/semana, podendo chegar a 15–20 h, e referências de impacto de 2–3 h/semana, até 4 h excepcionalmente, com recuperação mínima desejada de 6 h/semana. Essas faixas provêm de `Historico.json`, não constituem baseline ou meta vigente e serão validadas somente por medição real |
| OBJ-002 | SUCCESS-001, SUCCESS-002, SUCCESS-003 | Confirmados em nível de produto |
| OBJ-003 | SUCCESS-004 | Confirmado |
| OBJ-004 | SUCCESS-003 e evidências qualitativas de Q-004 | Confirmado sem métrica numérica adicional |
| OBJ-005 | Evidência de Q-004: automação não apresentada como decisão humana | Confirmado como critério qualitativo |

---

## 4. Matriz Fonte de produto → itens de entendimento

Os identificadores Q-001–Q-013 apontam para as seções homônimas de `PRODUCT-DOMAIN-SPEC.md` v2.10. O registro anterior que originou a consolidação permanece em `Historico.json`; as correções posteriores estão identificadas como aprovação da auditoria e foram aprovadas explicitamente pelo usuário em 2026-09-02. Assim, a origem sintética e a evidência histórica podem ser auditadas separadamente.

| Origem | Itens derivados nesta canonicalização | Status |
|---|---|---|
| Q-001 | PROBLEM-001, FACT-002, RISK-002 | confirmado / risco preservado |
| Q-002 | STK/ACT-001, STK/ACT-002, OBJ-001, OBJ-005 | confirmado |
| Q-003 | Visão, OBJ-001–005 | confirmado |
| Q-004 | SUCCESS-001–004, QA-001/002/008, RISK-002/003/009 | confirmado ou risco explicitado |
| Q-005 | NOT-001–010, DEC-003 | confirmado |
| Q-006 | CONST-001–005, CONST-007–011, FACT-003/006/007/008, RISK-001/004/005/006 | confirmado / risco preservado |
| Q-007 | DEC-001, CONST-006/008 | confirmado |
| Q-008 | DEC-004, ACT-001/002, RULE-023/024/031, FACT-001 | confirmado |
| Q-009 | SUCCESS-001/002/005, HYP-003 | SUCCESS-001/002 confirmados; a formulação vigente de Q-009 não estabelece baseline numérica; as faixas de SUCCESS-005 vêm de `Historico.json` como evidência histórica secundária, não medida, e o efeito sobre horas permanece a validar empiricamente |
| Q-010 consolidada | FLOW-001/002, RULE-001–003, RULE-018–022, RULE-026/027/030, FACT-004/005/009, escopo da primeira entrega | confirmado |
| Q-011 | CONCEPT-008, RULE-006–008 | confirmado |
| Q-012 | CONCEPT-009/012, RULE-004/009/010/011 | confirmado |
| Q-013 | CONCEPT-006, RULE-012–017 | confirmado |
| Aprovação das correções da auditoria | DEC-009–016; RULE-009/010/013–016/019/022/028–031; fechamento de convidada, ocorrências, cancelamento, remarcação, retificação e hipóteses | confirmado pelo usuário |
| Reauditoria independente v2.6/1.2 | AUD-023–027; identificação inicial de `OPEN-DOMAIN-001`; `INF-TECH-001`; estado da auditoria | `PASS WITH RISKS`; resultado preservado como registro da rodada |
| Revisão semântica posterior | `OPEN-001`; ciclo terminal no diagrama; criação após cancelamento | decisão de produto reaberta; correções editoriais aplicadas; modelagem aguarda fechamento humano de `OPEN-001` |
| Fechamento de `OPEN-001` | DEC-017; RULE-020/021; agenda mensal; estado da elicitação | confirmado pelo usuário; modelagem do domínio novamente autorizada |
| Retificação processual posterior | Estados `GATE-B-*` | confirmado; substitui autorização anterior de Requirements |

---

## 5. Matriz decisão humana → origem/contexto

| Decisão | Origem principal | Objetivos/Restrições relacionados | Status |
|---|---|---|---|
| DEC-001 — PWA na primeira versão | Q-007 | CONST-003–009, OBJ-001 | confirmado |
| DEC-002 — primeira entrega separada de `FUTURE` | Q-004/Q-005/Q-006 e consolidação v2.6 | CONST-004/005/011, RISK-001 | confirmado |
| DEC-003 — autoridade esportiva/humana do treinador | Q-002/Q-004/Q-005/Q-010 | OBJ-005, RISK-008 | confirmado |
| DEC-004 — papéis autenticados iniciais treinador/atleta | Q-008 | FACT-001, CONST-011 | confirmado |
| DEC-005 — D-5 e resolução automática | Q-009/Q-010/Q-012 | OBJ-001/002, SUCCESS-001/002 | confirmado |
| DEC-006 — sessão confirmada não cancela automaticamente pós-fechamento | Q-012/Q-013 | OBJ-002/005, RULE-015/016 | confirmado |
| DEC-007 — retificação auditável de presença e participação | Q-010 consolidada + aprovação da auditoria | OBJ-003, SUCCESS-004 | confirmado |
| DEC-008 — proposta mensal + revisão por exceção | Q-010 consolidada | OBJ-001/002, SUCCESS-001 | confirmado |
| DEC-009 — D-5 para toda sessão publicada com prazo futuro | aprovação da auditoria | OBJ-001/002, SUCCESS-001/002 | confirmado |
| DEC-010 — participante convidada fora do produto e do quórum | aprovação da auditoria | OBJ-001/002, CONST-011 | confirmado |
| DEC-011 — ocorrências positivas e negativas alteram a composição atual | aprovação da auditoria | OBJ-002/003/004 | confirmado |
| DEC-012 — cancelamento terminal | aprovação da auditoria | OBJ-002/003, SUCCESS-004 | confirmado |
| DEC-013 — remarcação por cancelamento da original e criação de outra | aprovação da auditoria | OBJ-002/003, SUCCESS-004 | confirmado |
| DEC-014 — confirmação excepcional explícita quando o D-5 já transcorreu | aprovação da auditoria | OBJ-001/002 | confirmado |
| DEC-015 — uma condição pós-confirmação e duas decisões do treinador | aprovação da auditoria | OBJ-001/002/005, QA-001/008 | confirmado |
| DEC-016 — hipóteses HYP-001–003 aceitas como riscos do piloto | aprovação da auditoria | OBJ-001/004, SUCCESS-001/005, RISK-001/003 | confirmado; validar no piloto |
| DEC-017 — proposta mensal inclui sessões possíveis em feriados oficiais aplicáveis | fechamento de `OPEN-001` pelo usuário | OBJ-001/002, RULE-020/021 | confirmado |
| DEC-018 — disponibilidade binária (sem TALVEZ), política de lembrete único | elicitação Requirements 2026-09-04 | OBJ-002/004, FR-010/FR-020 | confirmado; formalizado em Proposta de Requirements.md |
| DEC-019 — consulta offline de agenda previamente conhecida | elicitação Requirements 2026-09-04 | OBJ-002/004, FR-023 | confirmado; formalizado em Proposta de Requirements.md |
| DEC-020 — consulta offline de estado e próxima ação | elicitação Requirements 2026-09-04 | OBJ-002/004, FR-024 | confirmado; formalizado em Proposta de Requirements.md |
| DEC-021 — intenção local de disponibilidade como AÇÃO LOCAL PENDENTE DE CONFIRMAÇÃO | elicitação Requirements 2026-09-04 | OBJ-002/004, FR-025 | confirmado; complementado por DEC-021-SUBGAP-001 resolvido |
| DEC-021-SUBGAP-001 — tentativa pendente expira em D-5, permanece evidência histórica não confirmada e não vira ocorrência pós-D-5 automaticamente | decisão humana explícita 2026-09-05 | OBJ-002/003/004, FR-025 | confirmado; formalizado em Proposta de Requirements.md |
| REQ-ELIC-002-TRANSVERSAL — nenhuma modificação de estado oficial é concluída sem confirmação | elicitação Requirements 2026-09-04 | OBJ-003/005, NFR-006 | HUMAN_EXPLICIT; formalizado em Proposta de Requirements.md |

---

## 6. Matriz `FUTURE` → objetivo potencial

Esta matriz preserva visão futura sem criar requisito.

| FUTURE | Capacidade | Objetivo/intenção relacionada | Estado |
|---|---|---|---|
| FUTURE-001 | Wellness Pré/Pós | OBJ-005 / melhores evidências esportivas | FUTURE — fora da primeira entrega |
| FUTURE-002 | Planejamento de exercícios/temporada | OBJ-001/005 | FUTURE |
| FUTURE-003 | Biblioteca de exercícios | OBJ-001/005 | FUTURE |
| FUTURE-004 | Conteúdo técnico/tático | OBJ-005 | FUTURE |
| FUTURE-005 | Vídeo e cortes | OBJ-001/005 | FUTURE |
| FUTURE-006 | Scouts/relatórios/análise | OBJ-001/005 | FUTURE |
| FUTURE-007 | Avaliações/feedbacks | OBJ-005 | FUTURE |
| FUTURE-008 | Adversários/preparação de jogos | OBJ-005 | FUTURE |
| FUTURE-009 | Materiais/logística | OBJ-001/002 | FUTURE |
| FUTURE-010 | Competições/resultados/classificações auxiliares | OBJ-003/005 | FUTURE |
| FUTURE-011 | Controles financeiros simples | OBJ-001/003 | FUTURE |

Gamificação, rankings, disciplina, geração automática de materiais públicos e automação de substituições permanecem sem requisito confirmado e não são promovidos a `FUTURE` obrigatório por esta matriz.

---

## 7. Matriz Objetivo → Requisito

**Estado:** `AUTHORIZED — Chat 04 — Requirements`; `Proposta de Requirements.md` produzida; Gate C não executado; FR/NFR/CON são `PROPOSED_NON_CANONICAL`.

| Objetivo | Requisitos relacionados | Cobertura suficiente? | Observação |
|---|---|---|---|
| OBJ-001 | FR-003/004/011/012/020/022; NFR-001; CON-001/003–009 | Alta (proposta) | Gate C não executado; pendente validação formal |
| OBJ-002 | FR-002–015/019–025; NFR-001; CON-010 | Alta (proposta) | Inclui FR-023/024/025 de comportamento offline |
| OBJ-003 | FR-001/006–010/013/016–018/021/022; NFR-002/003/004/006 | Alta (proposta) | NFR-006 (REQ-ELIC-002-TRANSVERSAL) transversal |
| OBJ-004 | FR-001/010/013/019/020/023–025; NFR-003/005/006; CON-002 | Boa (proposta); risco empírico HYP-001 | Gate C não executado |
| OBJ-005 | FR-001/002/009/011/014/015/017/019; NFR-002/005/006 | Alta (proposta) | Gate C não executado |

---

## 8. Matriz Requisito → Driver

**Estado:** `NOT_YET_AUTHORIZED` para Drivers. Requirements está autorizado, mas nenhum requisito foi formalizado nesta canonicalização.

| Requisito | É driver? | Driver | Motivo |
|---|---|---|---|
| — | — | — | Drivers não autorizados antes do Gate C de Requirements |

---

## 9. Matriz Driver → ADR

**Estado:** `NOT_YET_AUTHORIZED`. Nenhum Driver, Alternative/Option ou ADR é criado nesta canonicalização.

| Driver | ADRs relacionados | Cobertura | Conflitos |
|---|---|---|---|
| — | — | — | Drivers, Alternatives/Options e ADRs ainda não autorizados |

---

## 10. Matriz ADR → Arquitetura

**Estado:** `NOT_YET_AUTHORIZED`. Este artefato não assume ADRs vigentes nem cria componentes/camadas.

| ADR | Componente/camada afetada | Manifestação concreta |
|---|---|---|
| — | — | — |

---

## 11. Matriz Arquitetura → Validação

**Estado:** `NOT_YET_AUTHORIZED`; permanece posterior a Requirements, Drivers, Options/ADRs e Architecture.

| Componente/decisão | Cenários de validação | Resultado atual |
|---|---|---|
| — | — | — |

---

## 12. Auditoria de elementos órfãos — entrada autorizada em Requirements

### Requisitos sem objetivo
- Não aplicável: Requirements está autorizado, mas ainda não foi produzido.

### Drivers sem origem
- Não aplicável: drivers ainda não foram formalizados.

### ADRs sem driver/requisito/restrição
- Nenhuma ADR é assumida por esta canonicalização.

### Componentes sem ADR ou necessidade rastreável
- Nenhum componente arquitetural é introduzido.

### Objetivos sem entendimento de origem
- Nenhum objetivo identificado está órfão; OBJ-001–005 possuem origem em Q-001–Q-005/Q-009/Q-010 e relações acima.

### Decisões sem cenário de validação
- Cenários arquiteturais persistentes ainda pertencem a fases posteriores. Os critérios de sucesso e fluxos de produto estão preservados, mas não são convertidos em `VAL-*` nesta etapa para não antecipar Requirements/arquitetura.

---

## 13. Registro de impacto de mudança

### CHANGE-001 — Consolidação de produto v2.4 e retificação do Gate B

**Nova informação:**  
A consolidação `CEPRAEA BEACH PRO — Arquitetura de Produto e Especificação de Domínio`, versão 2.4, fecha as decisões de produto Q-001–Q-013, explicita `SUPERSEDED-001..013`, separa a primeira entrega de `FUTURE` e é seguida por retificação processual que impede interpretar o conhecimento como aprovação formal do Gate B.

**Itens invalidados ou modificados:**  
- formulações históricas `SUPERSEDED-001..013`;
- entendimento anterior de D-5;
- papel de Wellness na primeira entrega;
- quórum operacional anterior;
- tratamento de falta de quórum em D-5;
- uso das estimativas de horas como critério principal de sucesso; `SUCCESS-001` passou a ser o critério principal, preservando as faixas de `Historico.json` somente como evidência histórica secundária de `SUCCESS-005`, sem baseline ou meta vigente;
- formulação processual anterior que poderia autorizar Requirements.

**Requisitos afetados:**  
Nenhum requisito canônico existe ainda; Requirements está bloqueado.

**Drivers afetados:**  
Nenhum driver canônico existe ainda.

**ADRs afetados:**  
Nenhuma ADR é assumida nesta canonicalização. Se existir ADR externo aos artefatos fornecidos, deve ser auditado separadamente e não é alterado por inferência aqui.

**Arquitetura afetada:**  
Nenhuma arquitetura é atualizada nesta etapa.

**Validações a repetir:**  
- auditoria independente do entendimento;
- modelagem do domínio no Chat 03;
- avaliação final formal do Gate B.

**Decisão humana:**  
Canonicalização aprovada. Não existe aprovação residual pendente para considerar `02-PROJECT-CHARTER`, `03-SHARED-UNDERSTANDING` e `07-TRACEABILITY` canônicos.

### CHANGE-002 — Correções da auditoria e fechamento do fluxo v2.6

**Nova informação:**  
O usuário aprovou um único fluxo simples: participante convidada fora do produto; D-5 para toda sessão publicada; ocorrências negativas e positivas com efeito imediato; cancelamento terminal; remarcação por cancelamento da original e criação de outra; uma única condição `QUÓRUM_COMPROMETIDO`; decisões `MANTER TREINO`/`CANCELAR TREINO`; retificação de presença e participação; e aceitação explícita das hipóteses HYP-001–003 como riscos do piloto.

**Itens modificados:**  
ACT-001/002; CONCEPT-002/005/006/007/011/012; RULE-005/009/010/012–031; FLOW-001/002; DEC-007/009–016; HYP-001–003; SUPERSEDED-007/013–015; escopo obrigatório e estados do Gate B.

**Artefatos reconciliados:**  
`PRODUCT-DOMAIN-SPEC.md` v2.6, `TRAINING_FLOW_CONTRACT.md` v1.2, `02-PROJECT-CHARTER.md` v0.3, `03-SHARED-UNDERSTANDING.md` v0.3 e este documento.

**Validações a repetir:**  
- auditoria independente das correções;
- modelagem do domínio no Chat 03;
- avaliação final formal do Gate B.

**Decisão humana necessária:**  
Nenhuma decisão de produto permanece aberta nesta rodada. A reauditoria pode devolver somente conflitos efetivamente não resolvidos.

### CHANGE-003 — Glossários normativos e reauditoria `PASS WITH RISKS`

**Nova informação:**  
`PRODUCT-DOMAIN-SPEC.md` v2.7 passou a ser a fonte única das definições canônicas de produto e domínio. `TRAINING_FLOW_CONTRACT.md` v1.3 herda esse vocabulário e define somente os termos específicos do contrato lógico. A reauditoria independente da base v2.6/1.2 concluiu `PASS WITH RISKS` e autorizou a modelagem do domínio, sem aprovar o Gate B final nem Requirements.

**Achados incorporados:**  
- `AUD-023`: as faixas numéricas de horas foram identificadas como evidência histórica de `Historico.json`, não como baseline ou meta vigente de Q-009;
- `AUD-024`: “feriado aplicável no Rio de Janeiro” foi registrado em `OPEN-DOMAIN-001` para teste na modelagem do domínio, sem criação de política por inferência;
- `AUD-025`: “situação operacional” foi removida do contrato por falta de sustentação na fonte de produto;
- `AUD-026`: reprocessamento/idempotência do checkpoint D-5 deixou de ser invariável confirmada e foi preservado como candidato técnico `INF-TECH-001` para Requirements/Drivers;
- `AUD-027`: a sequência processual foi corrigida para modelagem do domínio → Gate B final → Requirements.

**Artefatos reconciliados:**  
`PRODUCT-DOMAIN-SPEC.md` v2.7, `TRAINING_FLOW_CONTRACT.md` v1.3, `02-PROJECT-CHARTER.md` v0.4, `03-SHARED-UNDERSTANDING.md` v0.4 e este documento v0.4.

**Efeito processual:**  
`GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS`; `GATE-B-DOMAIN-MODEL = PENDING`; `GATE-B-FINAL = NOT_YET_APPROVED`. Requirements permanece bloqueado.

### CHANGE-004 — Correções do ciclo terminal e reabertura de `OPEN-001`

**Nova informação:**  
A revisão semântica posterior confirmou que o Diagrama 1 admitia leitura visual de `CANCELADO → REALIZADO`, que a elicitação ainda associava indevidamente remarcação a uma sessão já cancelada e que a abrangência de “feriado aplicável” exige decisão humana de produto.

**Correções aplicadas:**  
- o diagrama passou a mostrar `PUBLICADO / CONFIRMADO → CANCELADO [terminal]`, sem caminho de `CANCELADO` para `REALIZADO`;
- depois de um cancelamento, uma eventual realização futura exige criação de nova sessão;
- `OPEN-DOMAIN-001` foi substituído por `OPEN-001 — Critério de feriado aplicável`, sob autoridade da elicitação;
- a modelagem do domínio não está autorizada a escolher quais categorias de calendário acionam a regra.

**Artefatos reconciliados:**  
`PRODUCT-DOMAIN-SPEC.md` v2.8, `TRAINING_FLOW_CONTRACT.md` v1.4, `02-PROJECT-CHARTER.md` v0.5, `03-SHARED-UNDERSTANDING.md` v0.5 e este documento v0.5.

**Efeito processual:**  
`ELICITATION-OPEN = OPEN-001`. O resultado anterior da reauditoria permanece registrado, mas a modelagem do domínio aguarda o fechamento e a reconciliação dessa decisão.

### CHANGE-005 — Fechamento de `OPEN-001`

**Decisão humana:**  
A proposta mensal automática entrega as sessões normais e também sessões possíveis nos feriados nacionais e nos feriados oficiais estaduais ou municipais aplicáveis à cidade do Rio de Janeiro. As sugestões de feriado usam 07h30–09h00 e permanecem sujeitas à revisão humana antes da publicação.

**Regra de não duplicação:**  
Quando um feriado coincidir com uma recorrência normal, a proposta contém uma única sessão para a data, no horário de feriado.

**Itens modificados:**  
Glossário canônico; RULE-020/021; FLOW-001; DEC-017; RISK-011; `OPEN-001`; estado da elicitação e sequência de gates.

**Artefatos reconciliados:**  
`PRODUCT-DOMAIN-SPEC.md` v2.9, `TRAINING_FLOW_CONTRACT.md` v1.5, `02-PROJECT-CHARTER.md` v0.6, `03-SHARED-UNDERSTANDING.md` v0.6 e este documento v0.6.

**Efeito processual:**  
`ELICITATION-OPEN = NONE`; a modelagem do domínio é a próxima fase autorizada. Requirements permanece bloqueado.

### CHANGE-006 — Nome canônico e proveniência `DECIDED`/`DERIVED`

**Correções de governança documental:**  
- a fonte de produto e domínio passa a ser identificada inequivocamente como `PRODUCT-DOMAIN-SPEC.md`, sem sugerir que contém arquitetura técnica;
- `NONE` passa a significar ausência de decisões de produto abertas atualmente conhecidas, sem impedir que fases posteriores devolvam à elicitação uma nova lacuna material;
- o contrato lógico recebe o status `CANONICAL_DERIVED`, distinguindo decisões substantivas humanas `DECIDED` de formalizações `DERIVED`;
- uma derivação não pode ampliar sua origem; em conflito semântico, `PRODUCT-DOMAIN-SPEC.md` prevalece e o contrato deve ser corrigido.

**Artefatos reconciliados:**  
`PRODUCT-DOMAIN-SPEC.md` v2.10, `TRAINING_FLOW_CONTRACT.md` v1.6, `02-PROJECT-CHARTER.md` v0.7, `03-SHARED-UNDERSTANDING.md` v0.7 e este documento v0.7.

**Efeito processual:**  
Não há nova decisão substantiva de produto. `ELICITATION-OPEN = NONE` conserva seu significado processual atual; modelagem do domínio continua sendo a próxima fase autorizada e Requirements permanece bloqueado.


### CHANGE-007 — Canonicalização da modelagem e validação de regressão

**Decisão humana:**  
A modelagem conceitual do Chat 03 foi aprovada inicialmente como `PASS_WITH_RISKS`; após regressão contra `PRODUCT-DOMAIN-SPEC.md` v2.10 e `TRAINING_FLOW_CONTRACT.md` v1.6, o usuário aprovou `DOMAIN-MODEL = PASS` e `DOMAIN-MODEL-REGRESSION = PASS`.

**Impacto semântico:**  
- nenhuma semântica central de Sessão, Agenda, Disponibilidade, Ocorrência pós-D-5, Perfil esportivo, Alocação da sessão, Quórum, D-5, Presença, Participação, Retificação, estado × projeção, terminalidade de `CANCELADO` ou remarcação foi invalidada;
- `Perfil esportivo` e `Alocação da sessão` passam a ter suporte canônico direto no glossário v2.10;
- `DM-INV-007` e `DM-INV-009` são `DECIDED-supported`;
- `DM-INV-010` e `DM-INV-015` permanecem `INF-DERIVED`;
- `OPEN-DOMAIN-001`, `DM-FIND-005` e `CAN-DM-005` permanecem somente como histórico, superados pelo fechamento de `OPEN-001` por `DEC-017`;
- o resultado histórico `DOMAIN-MODEL = PASS_WITH_RISKS` é preservado, mas o estado corrente da modelagem passa a `PASS`.

**Achados preservados:**  
- `AUD-025`: conceito “situação operacional” rejeitado;
- `AUD-026 → INF-TECH-001`: candidato técnico futuro, sem promoção a regra de domínio;
- `AUD-023`: correção de proveniência;
- `AUD-027`: correção processual.

**Efeito processual:**  
`GATE-B-DOMAIN-MODEL = PASS`; `GATE-B-FINAL = NOT_YET_APPROVED`. Requirements permanece bloqueado. A próxima ação é a revisão formal final do Gate B no Chat 02.


### CHANGE-008 — Aprovação formal final do Gate B

**Decisão humana:**  
O usuário aprovou explicitamente `GATE-B-FINAL = APPROVED` após a revisão formal final do Gate B.

**Escopo desta canonicalização:**  
Somente sincronização processual. Nenhuma decisão de produto, regra de domínio, modelo, hipótese, risco, item `SUPERSEDED`/`RESOLVED` ou proveniência `DECIDED` / `DECIDED-supported` / `DERIVED` / `INF-DERIVED` é alterada.

**Estado processual resultante:**

```text
GATE-B-KNOWLEDGE = READY_WITH_RISKS
GATE-B-CANONICALIZATION = APPROVED
GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS
ELICITATION-OPEN = NONE
GATE-B-DOMAIN-MODEL = PASS
GATE-B-FINAL = APPROVED
```

**Consequência processual:**
- `Chat 04 — Requirements = AUTHORIZED`;
- `Drivers = NOT_YET_AUTHORIZED`;
- `Alternatives/Options = NOT_YET_AUTHORIZED`;
- `ADRs = NOT_YET_AUTHORIZED`;
- `Architecture = NOT_YET_AUTHORIZED`.

`FR/NFR/CON` permanecem vazios nesta canonicalização; a autorização não equivale à sua produção. Os resultados anteriores de assurance e todas as questões/riscos preservados mantêm seu estado vigente.

### CHANGE-009 — Propagação de DEC-018..021 e REQ-ELIC-002-TRANSVERSAL a Proposta de Requirements.md

**Decisões humanas propagadas:**

- `DEC-018` (disponibilidade binária, remoção de TALVEZ, política de lembrete único): formaliza FR-010 (formulação binária, cenários sem TALVEZ) e FR-020 (política de lembrete às 19:00 do 2º dia civil anterior ao D-5, `America/Sao_Paulo`, máximo um por atleta/sessão).
- `DEC-019` (agenda offline sem currentness): formaliza FR-023.
- `DEC-020` (estado e próxima ação offline): formaliza FR-024.
- `DEC-021` (intenção local pendente de confirmação): formaliza FR-025; `DEC-021-SUBGAP-001` permanece `OPEN`.
- `REQ-ELIC-002-TRANSVERSAL` (HUMAN_EXPLICIT, 2026-09-04): formaliza NFR-006.

**Gaps fechados ou parcialmente fechados:**

- `GAP-REQ-001`: fechado por DEC-018; residual técnico `OPEN-TECH-005`.
- `GAP-REQ-002`: porção semântica fechada por DEC-019/020/021; `OPEN-TECH-004` permanece aberto.
- `AUTH-REQ-001`: parcialmente respondida por DEC-019/020/021.
- `AUTH-REQ-003`: respondida por DEC-018.

**Artefatos modificados:**

- `Proposta de Requirements.md` (PROPOSED_NON_CANONICAL): FR-010/020 atualizados; FR-023/024/025 adicionados; NFR-006 adicionado; GAP-REQ-001 fechado; GAP-REQ-002 parcialmente fechado; seção 7 atualizada; matrizes 4.1/4.2 atualizadas.
- `governance/PENDING-PROPAGATION.md` v1.1: REQ-ELIC-002-TRANSVERSAL atualizado para `semantic_status: CURRENT, propagation_status: PENDING, authority: HUMAN_EXPLICIT`.
- Este documento v1.0: seções 5/7 e cabeçalho atualizados.

**Artefatos não alterados (escopo proibido):**

- `PRODUCT-DOMAIN-SPEC.md` v2.10: contém TALVEZ em Q-010; tratado como `SUPERSEDED_PENDING_PROPAGATION` para DEC-018 — não alterado por esta tarefa.
- `TRAINING_FLOW_CONTRACT.md` v1.6: contém TALVEZ; mesmo tratamento.

**Gate C:** não executado. `FR/NFR/CON` permanecem `PROPOSED_NON_CANONICAL`.

**Estado processual resultante:**

```text
GATE-B-FINAL = APPROVED
GATE-C = NOT_EXECUTED
DEC-018 = PROPAGATED (Proposta de Requirements.md)
DEC-019 = PROPAGATED (Proposta de Requirements.md)
DEC-020 = PROPAGATED (Proposta de Requirements.md)
DEC-021 = PROPAGATED (Proposta de Requirements.md); DEC-021-SUBGAP-001 = OPEN
REQ-ELIC-002-TRANSVERSAL = PROPAGATED (Proposta de Requirements.md / NFR-006)
POST-D5-OFFLINE-OCCURRENCE = PROPOSED_NOT_CONFIRMED (não propagada)
```

---

### CHANGE-010 — Fechamento de DEC-021-SUBGAP-001

**Decisão humana:**
Quando D-5 ocorrer, uma tentativa local ainda pendente expira sem alterar qualquer
estado oficial ou quórum e permanece registrada apenas como evidência histórica de
uma tentativa não confirmada. Ela não é convertida automaticamente em ocorrência
pós-D-5.

**Impacto propagado:**

- `governance/PENDING-PROPAGATION.md`: subgap marcado como resolvido e decisão
  registrada com autoridade humana explícita;
- `Proposta de Requirements.md`: FR-025, GAP-REQ-002, AUTH-REQ-001 e matriz de
  origem atualizados;
- matriz de decisões desta rastreabilidade atualizada.

**Estado resultante:**

```text
DEC-021-SUBGAP-001 = RESOLVED
ELICITATION-OPEN = NONE
GATE-C = NOT_EXECUTED
OPEN-TECH-004 = OPEN (decisão técnica adiada)
```

Esta decisão não aprova Requirements, não executa Gate C e não autoriza Drivers,
Options, ADRs, Architecture ou implementação.

---

## 14. Histórico `SUPERSEDED`

| ID | Formulação substituída | Vigente | Origem da substituição |
|---|---|---|---|
| SUPERSEDED-001 | Fechamento na véspera/24h/genérico | D-5 = −120h | consolidação v2.4 |
| SUPERSEDED-002 | Wellness determina presença | Wellness `FUTURE`; presença consolidada pelo treinador | consolidação v2.4 |
| SUPERSEDED-003 | Treinador cria todos os treinos | proposta mensal + revisão por exceção | consolidação v2.4 |
| SUPERSEDED-004 | 1G+3D+4A | 4 Ataque + 4 Defesa + 8 distintas + ≥1 Goleira defensiva | consolidação v2.4 |
| SUPERSEDED-005 | categorias genéricas bastam | Fase → Sistema → Posição | consolidação v2.4 |
| SUPERSEDED-006 | resposta antecipada pode ser presença | disponibilidade ≠ presença ≠ participação | consolidação v2.4 |
| SUPERSEDED-007 | quantidade bruta ou classe separada de falha crítica define a exceção | `QUÓRUM_COMPROMETIDO`; déficit exato como diagnóstico | consolidação v2.6 |
| SUPERSEDED-008 | produto completo = MVP | primeira entrega ≠ `FUTURE` | consolidação v2.4 |
| SUPERSEDED-009 | confirmação antecipada manual normal | `QUÓRUM_GARANTIDO` antes; confirmação em D-5 | consolidação v2.4 |
| SUPERSEDED-010 | falta de quórum em D-5 requer decisão | cancelamento automático por `FALTA_DE_QUÓRUM` | consolidação v2.4 |
| SUPERSEDED-011 | só quinta ajusta feriado | proposta mensal inclui sessões possíveis nos feriados nacionais e oficiais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 | consolidação v2.4 + DEC-017 |
| SUPERSEDED-012 | horas estimadas = critério principal | `SUCCESS-001` = zero ações administrativas semanais normais; as faixas de `Historico.json` permanecem somente como evidência histórica secundária de `SUCCESS-005`, sem baseline ou meta vigente | consolidação v2.4 + correção de canonicalização + `AUD-023` |
| SUPERSEDED-013 | correção de presença não fechada | retificação auditável de presença e participação sem sobrescrita | consolidação v2.6 |
| SUPERSEDED-014 | convidada cadastrada e contada no quórum | convidada fora do produto; treinador mantém ou cancela | consolidação v2.6 |
| SUPERSEDED-015 | edição substitui data/horário de sessão publicada | remarcação cancela a original e cria outra sem disponibilidades | consolidação v2.6 |

---

## 15. Decisões e questões deliberadamente não fechadas

| ID | Informação confirmada | O que continua aberto | Destino futuro |
|---|---|---|---|
| INF-TECH-001 | O fluxo normal de D-5 possui uma única resolução operacional | tratamento idempotente e reprocessamento técnico do mesmo checkpoint | Requirements/Drivers; candidato `INF`, não regra de domínio confirmada |
| OPEN-TECH-002 | Custo e manutenção precisam ser muito baixos | provedor, banco, hosting, serverless etc. | drivers/opções/ADR quando autorizado |
| OPEN-TECH-003 | Há dados privados e baixa capacidade de suporte | mecanismo de autenticação | Requirements/Drivers/ADR posteriormente |
| OPEN-TECH-004 | Conectividade da praia é instável | offline/sincronização concreta | Requirements/Drivers/ADR posteriormente |
| OPEN-TECH-005 | Fluxo precisa lembrar/comunicar e alertar exceções | tecnologia de notificações/comunicação | Requirements/Drivers/ADR posteriormente |

---

## 16. Perguntas de auditoria

- Cada objetivo está efetivamente sustentado pelas declarações Q-001–Q-013 consolidadas?
- Alguma regra marcada como confirmada extrapola a consolidação vigente ou a aprovação explícita das correções?
- Algum item `FUTURE` foi acidentalmente promovido à primeira entrega?
- Algum item `SUPERSEDED` ainda aparece como vigente em outro artefato?
- Há contradição entre os estados da sessão e as condições/projeções de quórum?
- Disponibilidade, presença e participação permanecem rastreáveis como fatos distintos?
- Alguma questão técnica aberta foi silenciosamente tratada como decisão?
- A modelagem de domínio no Chat 03 revela conceitos, limites ou conflitos que exigem impacto de mudança?
- Após canonicalização, auditoria e modelagem, o Gate B final pode ser aprovado sem questão de alto impacto + alta incerteza não tratada?

---

## 17. Próxima ação — somente registro de processo

1. `04 — Requirements`.

`Chat 04 — Requirements = AUTHORIZED`. Drivers, Alternatives/Options, ADRs e Architecture permanecem `NOT_YET_AUTHORIZED`.


---

## 18. Rastreabilidade da modelagem do domínio

### 18.1 Resultado corrente e histórico

| Item | Estado | Observação |
|---|---|---|
| `DOMAIN-MODEL = PASS_WITH_RISKS` | histórico | resultado da primeira rodada do Chat 03; preservado sem vigência atual |
| `DOMAIN-MODEL = PASS` | vigente | aprovado após regressão contra fontes v2.10/v1.6 |
| `DOMAIN-MODEL-REGRESSION = PASS` | vigente | nenhuma semântica central invalidada |

### 18.2 Matriz conceito → origem → regra → status

| Conceito/modelagem | Origem principal | Regras/decisões relacionadas | Status/proveniência |
|---|---|---|---|
| Agenda Esportiva | glossário v2.10; CONCEPT-001 | RULE-020/021/027 | conceito `DECIDED`; ausência de identidade/ciclo autônomo adicional `INF-DERIVED` |
| Sessão de treino | glossário v2.10; CONCEPT-002 | RULE-009/010/015/022/028/029 | `DECIDED-supported` |
| Disponibilidade | glossário v2.10; CONCEPT-003 | RULE-001/002/005/012 | `DECIDED-supported` |
| Ocorrência pós-fechamento | glossário v2.10; CONCEPT-006 | RULE-012–017 | `DECIDED-supported` |
| Perfil esportivo | glossário v2.10; CONCEPT-008 | RULE-007/008 | `DECIDED-supported` |
| Alocação da sessão | glossário v2.10; Q-010/Q-011 | RULE-006–008 | `DECIDED-supported` |
| Quórum operacional | glossário v2.10; CONCEPT-007 | RULE-005–008 | `DECIDED-supported` |
| D-5 | glossário v2.10; CONCEPT-009 | RULE-004/009–012; DEC-005/009/014 | `DECIDED-supported` |
| Presença | glossário v2.10; CONCEPT-004 | RULE-001/003/018/019/030 | `DECIDED-supported` |
| Participação | glossário v2.10; CONCEPT-005 | RULE-001/003/018/019/030 | `DECIDED-supported` |
| Retificação auditável | glossário v2.10; CONCEPT-011 | RULE-030; DEC-007 | `DECIDED-supported` |
| Estado da sessão × condição/projeção | glossário v2.10; CONCEPT-012 | RULE-011/013–016/027 | `DECIDED-supported` |
| Feriado aplicável no Rio de Janeiro | glossário v2.10 | DEC-017; RULE-021 | `DECIDED`; risco semântico encerrado |
| `INF-TECH-001` | AUD-026 | — | `INF` técnico futuro; fora do domínio confirmado |

### 18.3 Matriz de proveniência dos invariantes

| DM-INV | Proveniência | Origem rastreável |
|---|---|---|
| DM-INV-001 | `DECIDED-supported` | RULE-001; CONCEPT-003/004/005 |
| DM-INV-002 | `DECIDED-supported` | RULE-002; CONCEPT-003 |
| DM-INV-003 | `DECIDED-supported` | RULE-003; CONCEPT-004/005 |
| DM-INV-004 | `DECIDED-supported` | RULE-019; CONCEPT-004/005 |
| DM-INV-005 | `DECIDED-supported` | RULE-006; CONCEPT-007 |
| DM-INV-006 | `DECIDED-supported` | RULE-008; CONCEPT-008 |
| DM-INV-007 | `DECIDED-supported` | glossário Perfil esportivo / Alocação; RULE-007/008 |
| DM-INV-008 | `DECIDED-supported` | RULE-012; CONCEPT-006 |
| DM-INV-009 | `DECIDED-supported` | glossário Projeção de quórum; OBJ-005; DEC-003 |
| DM-INV-010 | `INF-DERIVED` | RULE-003/018/027; CONCEPT-002/004/005 |
| DM-INV-011 | `DECIDED-supported` | DEC-013; RULE-022 |
| DM-INV-012 | `DECIDED-supported` | DEC-013; RULE-022 |
| DM-INV-013 | `DECIDED-supported` | DEC-007; RULE-030; CONCEPT-011 |
| DM-INV-014 | `DECIDED-supported` | CONCEPT-011; RULE-030 |
| DM-INV-015 | `INF-DERIVED` | RULE-019 + RULE-030 + CONCEPT-011 |

Nenhum `DM-INV-001..015` foi invalidado pela regressão.

### 18.4 Cadeia de resolução de `AUD-024`

```text
AUD-024
→ OPEN-DOMAIN-001
→ OPEN-001
→ DEC-017
→ RULE-021
→ RESOLVED
```

`OPEN-DOMAIN-001`, `DM-FIND-005` e `CAN-DM-005` permanecem somente como histórico. Não constituem risco ou recomendação vigentes.

### 18.5 Achados preservados sem criação de conceito

- `AUD-025` → “situação operacional” permanece conceito rejeitado por falta de sustentação.
- `AUD-026` → `INF-TECH-001`; idempotência/reprocessamento permanece candidato técnico futuro.
- `AUD-023` → correção de proveniência das referências históricas de horas.
- `AUD-027` → correção processual da ordem modelagem → Gate B final → Requirements.

### 18.6 Estado processual após a canonicalização

```text
GATE-B-KNOWLEDGE = READY_WITH_RISKS
GATE-B-CANONICALIZATION = APPROVED
GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS
ELICITATION-OPEN = NONE
GATE-B-DOMAIN-MODEL = PASS
GATE-B-FINAL = APPROVED
```

A cadeia `OBJ → FACT/RULE/FLOW/CONST/HYP` permanece a última camada atualmente preenchida. `FR/NFR/CON` estão autorizados para formalização em `04 — Requirements`, mas permanecem vazios nesta canonicalização. Drivers, Alternatives/Options, ADRs, Architecture e VAL permanecem não produzidos/não autorizados.
