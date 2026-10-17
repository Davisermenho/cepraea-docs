# SHARED UNDERSTANDING

> **ARTEFATO CANÔNICO — GATE B FINAL APROVADO**  
> `DOMAIN-MODEL = PASS`; `GATE-B-FINAL = APPROVED` e `Chat 04 — Requirements` está autorizado.

**Propósito:** representar o entendimento compartilhado atual entre humano e IA.  
**Regra:** este documento descreve o que acreditamos saber sobre produto e domínio; não produz Requirements nem autoriza Drivers, Alternatives/Options, ADRs, Architecture ou implementação.  
**Versão:** 0.9  
**Última atualização:** 2026-09-03  
**Origem principal:** `PRODUCT-DOMAIN-SPEC.md`, versão 2.10, com proveniência histórica em `Historico.json`.

**Nota de proveniência editorial:** IDs, títulos curtos e redações sintéticas introduzidos neste artefato são organização `INF`; o conteúdo substantivo somente é marcado como confirmado quando sustentado pelas declarações consolidadas do usuário.

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

A canonicalização foi aprovada, a reauditoria resultou em `PASS WITH RISKS`, `OPEN-001` foi fechado por decisão humana, a modelagem do domínio após regressão resultou em `PASS` e o Gate B final foi aprovado. `Chat 04 — Requirements = AUTHORIZED`; Drivers, Alternatives/Options, ADRs e Architecture permanecem `NOT_YET_AUTHORIZED`.

---

## 1. Objetivos confirmados

| ID | Objetivo | Por quê? | Prioridade | Status |
|---|---|---|---|---|
| OBJ-001 | Devolver tempo e atenção ao trabalho esportivo | A carga administrativa atual compete com planejamento, estudo, análise, avaliação, feedback e treino | [não formalizada] | confirmado |
| OBJ-002 | Operar a agenda por exceção e com previsibilidade | O fluxo normal deve resolver sessões sem acompanhamento administrativo semanal e antecipar falta de quórum | [não formalizada] | confirmado |
| OBJ-003 | Preservar informação e histórico confiáveis | Declarações, fatos e correções não podem ser misturados ou silenciosamente reescritos | [não formalizada] | confirmado |
| OBJ-004 | Aumentar a autonomia operacional das atletas | As atletas devem informar diretamente aquilo que depende delas e consultar sua próxima ação | [não formalizada] | confirmado |
| OBJ-005 | Apoiar decisões esportivas sem substituir o treinador | Cálculo, alerta e evidência devem reduzir trabalho mecânico mantendo julgamento técnico e humano | [não formalizada] | confirmado |

---

## 2. Atores

### ACT-001 — Treinador/Administrador

**Quem é:**  
Treinador do CEPRAEA e responsável atual pela gestão esportiva e operacional da equipe e pelo produto.

**Responsabilidades confirmadas:**  
- revisar e publicar a agenda;
- criar, editar proposta, remarcar ou cancelar sessões quando houver mudança real;
- acompanhar diagnóstico de quórum quando necessário;
- registrar ocorrência em nome de atleta quando possuir informação confiável;
- decidir sobre exceções de sessão já confirmada;
- cadastrar posição principal e secundária das atletas;
- apurar e consolidar presença e participação;
- retificar presença ou participação consolidada de forma auditável quando existir erro factual.

**Objetivos:**  
OBJ-001, OBJ-002, OBJ-003 e OBJ-005.

**Permissões aparentes confirmadas no produto:**  
Autoridade administrativa e esportiva necessária às responsabilidades acima. Detalhes técnicos de autorização permanecem não decididos.

**Situações críticas:**  
- sessão confirmada perde quórum;
- capacidade obrigatória deixa de ser preenchível;
- mudança de data/horário exige remarcar sessão publicada;
- presença ou participação consolidada precisa de retificação.

**Questões abertas técnicas relacionadas:**  
OPEN-TECH-003.

### ACT-002 — Atleta

**Quem é:**  
Integrante do elenco do CEPRAEA com papel autenticado `ATLETA`.

**Responsabilidades confirmadas:**  
- consultar agenda, estado simples do compromisso e próxima ação;
- declarar `DISPONÍVEL`, `INDISPONÍVEL` ou `TALVEZ` durante a janela ordinária;
- informar motivo curto associado à indisponibilidade quando aplicável;
- registrar `NÃO PODEREI COMPARECER` ou `AGORA POSSO PARTICIPAR` após o fechamento quando sua situação mudar.

**Objetivos:**  
OBJ-004 e contribuição para OBJ-002/OBJ-003.

**Permissões aparentes confirmadas no produto:**  
- manipula suas próprias declarações dentro do período permitido;
- não altera dados de outras atletas;
- não administra a equipe;
- não altera nem retifica presença ou participação consolidada;
- acessa seus dados individuais e apenas informações coletivas necessárias.

**Situações críticas:**  
- não respondeu antes de D-5;
- muda de disponibilidade depois do fechamento;
- está sem acesso ao aplicativo e treinador registra ocorrência em seu nome.

---

## 3. Conceitos do domínio

### CONCEPT-001 — Agenda de treinos

**Definição confirmada:**  
Conjunto de sessões planejadas, revisadas e publicadas para a equipe. O sistema gera proposta mensal baseada na recorrência conhecida; o treinador revisa por exceção e publica.

**Não significa:**  
Que sessões publicadas são imutáveis ou que quórum já está garantido.

**Relaciona-se com:**  
CONCEPT-002, CONCEPT-009, FLOW-001.

**Ambiguidades:**  
Nenhuma decisão de produto permanece aberta sobre o critério de feriado aplicável; detalhes de fonte e integração do calendário continuam técnicos e posteriores.

### CONCEPT-002 — Sessão de treino

**Definição confirmada:**  
Atividade esportiva com data, horário, local e ciclo próprio de planejamento/publicação/confirmação/cancelamento/realização.

**Estados confirmados do ciclo:**  
`PLANEJADO`, `PUBLICADO`, `CONFIRMADO`, `CANCELADO`, `REALIZADO`.

`CANCELADO` é terminal. Alterar data ou horário depois da publicação exige remarcação: a sessão original é cancelada com motivo `REMARCADO` e outra sessão é criada sem transportar disponibilidades.

**Não significa:**  
Que condições de quórum sejam estados do ciclo da sessão.

**Relaciona-se com:**  
CONCEPT-007, CONCEPT-012.

### CONCEPT-003 — Disponibilidade

**Definição confirmada:**  
Declaração anterior à sessão sobre possibilidade/intenção de participação.

**Valores confirmados:**  
`DISPONÍVEL`, `INDISPONÍVEL`, `TALVEZ`; `NÃO RESPONDEU` representa ausência de declaração.

**Não significa:**  
Presença factual nem participação esportiva.

**Relaciona-se com:**  
CONCEPT-004, CONCEPT-005, CONCEPT-006, CONCEPT-009.

### CONCEPT-004 — Presença

**Definição confirmada:**  
Fato de a atleta ter comparecido fisicamente à sessão.

**Estados exemplificados/confirmados:**  
`PRESENTE`, `AUSENTE`, `NÃO APURADO` conforme a apuração factual.

**Não significa:**  
Disponibilidade anterior nem participação integral.

**Autoridade final:**  
Treinador/Administrador após apuração e consolidação.

### CONCEPT-005 — Participação

**Definição confirmada:**  
Fato de a atleta ter realizado a atividade esportiva integralmente, parcialmente ou não ter realizado nenhuma parte, tenha comparecido ou não.

**Estados confirmados por cenário:**  
`COMPLETA`, `PARCIAL`, `NÃO PARTICIPOU`, `NÃO APURADA`.

**Não significa:**  
Presença física.

### CONCEPT-006 — Ocorrência pós-fechamento

**Definição confirmada:**  
Novo fato registrado depois de D-5 que complementa a declaração original sem reescrevê-la.

**Ações e efeitos confirmados:**  
- `NÃO PODEREI COMPARECER` retira imediatamente a atleta da composição atual;
- `AGORA POSSO PARTICIPAR` inclui imediatamente a atleta como candidata conforme seu perfil esportivo;
- ambos recalculam o quórum sem reescrever a declaração original.

**Propriedades confirmadas:**  
Autoria real, motivo curto e data/hora são preservados; treinador pode registrar em nome da atleta quando necessário.

### CONCEPT-007 — Quórum operacional

**Definição confirmada:**  
Condição necessária para confirmação automática de qualquer sessão publicada com D-5 futuro, seja recorrente ou excepcional.

**Mínimo confirmado:**

```text
Defesa = 4 atletas
Ataque = 4 atletas
Atletas distintas = 8
Goleira >= 1 entre as 4 atletas alocadas na Defesa
```

**Não significa:**  
Número bruto de pessoas nem estado do ciclo da sessão.

### CONCEPT-008 — Capacidade tática e posição

**Definição confirmada:**  
A organização esportiva segue `Fase → Sistema → Posição`. Cada atleta possui na primeira entrega uma posição principal obrigatória e uma secundária opcional; a alocação efetiva numa sessão é contextual.

**Fases/sistemas/posições confirmados:**

**ATAQUE — 3x1**
- Central
- Pivô
- Lateral Esquerda
- Lateral Direita

**ATAQUE — 4x0**
- Lateral Esquerda
- Lateral Direita
- Central Esquerda
- Central Direita

**DEFESA — 3:0**
- Defensora Base
- Defensora Solta
- Defensora Cobertura
- Goleira

**DEFESA — 2:1**
- Defensora Avançada
- Defensora Solta
- Defensora Cobertura
- Goleira

**Não significa:**  
Que uma atleta possa ocupar duas vagas simultaneamente.

### CONCEPT-009 — D-5

**Definição confirmada:**

```text
D-5 = início_da_sessão − 120 horas
```

É o instante exato de fechamento da disponibilidade ordinária e resolução automática da sessão no fluxo normal.

### CONCEPT-011 — Retificação auditável

**Definição confirmada:**  
Mecanismo pelo qual o treinador/administrador corrige posteriormente um erro factual de presença ou participação consolidada sem sobrescrever o registro anterior. Se a correção de um eixo invalidar a combinação Presença × Participação, os dois são retificados juntos.

**Informações preservadas obrigatoriamente:**  
valor anterior, novo valor, motivo, autor, data e hora.

### CONCEPT-012 — Ciclo da sessão vs. condições/projeções

**Definição confirmada:**  
O ciclo programado da sessão e as condições operacionais de quórum são fatos distintos.

**Estados de sessão:**  
`PLANEJADO`, `PUBLICADO`, `CONFIRMADO`, `CANCELADO`, `REALIZADO`.

**Condições/projeções confirmadas:**  
`DISPONIBILIDADE_ABERTA`, `QUÓRUM_EM_FORMAÇÃO`, `QUÓRUM_GARANTIDO`, `FALTA_DE_QUÓRUM`, `QUÓRUM_COMPROMETIDO`.

**Não significa:**  
Que uma projeção seja fonte de verdade concorrente do ciclo da agenda ou dos fatos de participação.

### CONCEPT-013 — Participação Esportiva (termo conceitual do produto)

**Definição confirmada:**  
Área conceitual em que disponibilidade, justificativas/ocorrências, presença e participação possuem ciclos próprios e não se transformam automaticamente uns nos outros.

**Não significa:**  
Um Bounded Context, schema, serviço, módulo ou decisão de arquitetura já aprovada.

**Relaciona-se com:**  
CONCEPT-003–006 e CONCEPT-012.

---

## 4. Regras confirmadas

A categoria distingue semântica do domínio, comportamento do produto, política de acesso e apresentação. A classificação não transforma uma decisão de produto em lei do domínio.

| ID | Categoria | Regra | Origem | Exceções/observações | Status |
|---|---|---|---|---|---|
| RULE-001 | domínio | `Disponibilidade ≠ Presença ≠ Participação` | Q-010 | Nenhuma pode ser inferida silenciosamente da outra | confirmada |
| RULE-002 | domínio | `NÃO RESPONDEU` não é `INDISPONÍVEL` | Q-010 consolidada | Ausência de declaração permanece distinta | confirmada |
| RULE-003 | domínio | Ausência de apuração não é ausência | Q-010 consolidada | Presença/participação podem permanecer `NÃO APURADO/NÃO APURADA` | confirmada |
| RULE-004 | produto | D-5 = início da sessão − 120 horas | Q-012 | Substitui véspera/horário genérico | confirmada |
| RULE-005 | domínio | Apenas atleta `DISPONÍVEL` preenche vaga no quórum em D-5 | Q-010/Q-012 | `TALVEZ` e `NÃO RESPONDEU` não contam; participante convidada não existe no produto | confirmada |
| RULE-006 | domínio | Quórum mínimo = 4 Defesa + 4 Ataque + 8 atletas distintas + ≥1 Goleira na Defesa | Q-010/Q-011 | Piso para confirmação automática, não teto | confirmada |
| RULE-007 | domínio | Posição principal é obrigatória e secundária opcional; ambas podem ser usadas na alocação | Q-011 | Principal é preferência; secundária pode satisfazer déficit | confirmada |
| RULE-008 | domínio | Uma atleta ocupa uma única vaga no cálculo simultâneo | Q-011 | Não há dupla contagem | confirmada |
| RULE-009 | produto | Quórum satisfeito em D-5 produz `CONFIRMADO` automaticamente | Q-012 + aprovação da auditoria | Vale para toda sessão `PUBLICADO`, recorrente ou excepcional | confirmada |
| RULE-010 | produto | Quórum insuficiente em D-5 produz `CANCELADO — FALTA_DE_QUÓRUM` automaticamente | Q-012 + aprovação da auditoria | O cancelamento é terminal | confirmada |
| RULE-011 | produto | Quórum atingido antes de D-5 gera `QUÓRUM_GARANTIDO`, sem confirmação antecipada no fluxo normal | Q-010/Q-012 | A janela permanece aberta até D-5 | confirmada |
| RULE-012 | domínio | Após D-5, declaração ordinária não é reescrita; mudança vira ocorrência pós-fechamento | Q-013 | Vale para mudança negativa e positiva | confirmada |
| RULE-013 | produto | `NÃO PODEREI COMPARECER` retira imediatamente a atleta da composição atual e recalcula o quórum | Q-013 + aprovação da auditoria | Não exige aprovação para reconhecer o fato | confirmada |
| RULE-014 | produto | `AGORA POSSO PARTICIPAR` inclui imediatamente a atleta como candidata e recalcula o quórum | aprovação da auditoria | Respeita o perfil esportivo e pode encerrar alerta pendente | confirmada |
| RULE-015 | produto | Sessão confirmada nunca é cancelada automaticamente por ocorrência posterior | Q-012/Q-013 | Composição inválida gera somente `QUÓRUM_COMPROMETIDO` | confirmada |
| RULE-016 | produto | Diante de `QUÓRUM_COMPROMETIDO`, o treinador escolhe apenas `MANTER TREINO` ou `CANCELAR TREINO` | Q-013 + aprovação da auditoria | O sistema não pergunta como a solução esportiva será executada | confirmada |
| RULE-017 | acesso | Treinador pode registrar ocorrência em nome da atleta, preservando a autoria real | Q-013 | Sistema não atribui falsamente a ação à atleta | confirmada |
| RULE-018 | domínio | Presença e participação finais são consolidadas pelo treinador; evidências técnicas não substituem fatos | Q-010 | Wellness está fora da primeira entrega | confirmada |
| RULE-019 | domínio | Somente cinco combinações Presença × Participação são válidas: `PRESENTE+COMPLETA`, `PRESENTE+PARCIAL`, `PRESENTE+NÃO PARTICIPOU`, `AUSENTE+NÃO PARTICIPOU`, `NÃO APURADO+NÃO APURADA` | aprovação da auditoria | Demais combinações são inválidas | confirmada |
| RULE-020 | produto | Sistema gera proposta mensal; treinador revisa por exceção e publica | Q-010 consolidada | Sessões excepcionais continuam permitidas | confirmada |
| RULE-021 | produto | A proposta mensal inclui sessões possíveis nos feriados nacionais e nos feriados oficiais estaduais ou municipais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 | Q-010 consolidada + DEC-017 | Coincidência com recorrência normal produz uma única sugestão na data, no horário de feriado; publicação continua sujeita à revisão humana | confirmada |
| RULE-022 | produto | Data ou horário de sessão publicada só muda por `REMARCAR TREINO`: cancelar a original com `REMARCADO` e criar outra sem disponibilidades transportadas | aprovação da auditoria | Outros campos podem ter alteração auditável | confirmada |
| RULE-023 | acesso | Atleta não altera dados de outras atletas, administra a equipe ou altera fatos consolidados | Q-008 | Detalhes técnicos de autorização não decididos | confirmada |
| RULE-024 | acesso | Informações individuais são privadas; cada atleta acessa dados próprios e apenas informação coletiva necessária | Q-008 | Avaliação/feedback continuam `FUTURE` | confirmada |
| RULE-025 | apresentação | Para as atletas, estados são simples e não expõem a matemática interna do quórum | Q-004/Q-012 | Déficit exato é apresentado ao treinador | confirmada |
| RULE-026 | domínio | Treinos podem ocorrer em qualquer dia; na recorrência atual de dias úteis, ocorrem após 20h e terminam até 22h | Q-010 consolidada | FACT-009 registra a prática observada; esta regra contém a prescrição | confirmada |
| RULE-027 | organização conceitual | Agenda, disponibilidade, ocorrências, presença, participação e projeções preservam fatos e ciclos distintos | consolidação v2.9 | Não define Bounded Context, schema, serviço ou módulo | confirmada |
| RULE-028 | produto | Sessão `CANCELADO` é terminal: não reativa e não recebe novas ocorrências | aprovação da auditoria | Nova realização exige outra sessão | confirmada |
| RULE-029 | produto | Nova sessão cujo D-5 já passou exige `CONFIRMAR SESSÃO EXCEPCIONAL` explícito para entrar em `CONFIRMADO` | aprovação da auditoria | Não simula resolução automática retroativa | confirmada |
| RULE-030 | produto | Presença ou participação consolidada só é corrigida por retificação auditável do treinador; os dois eixos são corrigidos juntos quando necessário | Q-010 + aprovação da auditoria | Valor anterior permanece no histórico | confirmada |
| RULE-031 | escopo | Participante convidada não é cadastrada, representada nem considerada no cálculo de quórum | aprovação da auditoria | Solução externa do treinador não é registrada | confirmada |

---

## 5. Fluxos críticos

### FLOW-001 — Agenda → disponibilidade → D-5 → resolução → exceção → presença e participação factuais

**Ator principal:**  
ACT-001 — Treinador/Administrador.

**Atores participantes:**  
ACT-002 — Atletas.

**Objetivo:**  
Operar cada treino desde a proposta/publicação até a presença factual com previsibilidade, resolução automática no fluxo normal e intervenção humana apenas em mudanças e exceções reais.

**Pré-condições confirmadas:**  
- elenco e posições esportivas pertinentes estão disponíveis;
- sessão possui data, horário e local;
- agenda foi revisada e publicada;
- D-5 pode ser calculado como início −120h.

**Fluxo normal:**
1. O sistema gera a proposta mensal com recorrências conhecidas e sessões possíveis nos feriados nacionais e oficiais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 e sem duplicar uma recorrência coincidente.
2. O treinador revisa por exceção e publica.
3. As sessões publicadas geram pendências de disponibilidade para as atletas.
4. Durante a janela ordinária, atletas declaram/alteram `DISPONÍVEL`, `INDISPONÍVEL` ou `TALVEZ`; ausência de declaração permanece `NÃO RESPONDEU`.
5. O sistema acompanha e projeta quórum utilizando atletas `DISPONÍVEL`, posição principal/secundária e proibição de dupla contagem.
6. Antes de D-5, composição suficiente pode ser exibida como `QUÓRUM_GARANTIDO`, sem confirmar antecipadamente.
7. Em D-5, a janela ordinária de toda sessão publicada fecha, independentemente de sua origem.
8. Com quórum suficiente, a sessão passa automaticamente a `CONFIRMADO` e as atletas são comunicadas.
9. Sem quórum suficiente, a sessão passa automaticamente a `CANCELADO — FALTA_DE_QUÓRUM` e permanece no histórico.
10. Em sessão confirmada, `NÃO PODEREI COMPARECER` retira e `AGORA POSSO PARTICIPAR` inclui a atleta no cálculo atual, sem reescrever a declaração original.
11. Composição inválida gera `QUÓRUM_COMPROMETIDO` e mostra o déficit exato ao treinador; não cancela automaticamente.
12. O treinador escolhe somente `MANTER TREINO` ou `CANCELAR TREINO`.
13. Ao término, o treinador apura e consolida presença e participação, revisando apenas as exceções da lista provisória disponível.
14. Correção factual posterior de presença ou participação usa retificação auditável, nunca sobrescrita.

**Exceções confirmadas:**  
- data ou horário de sessão publicada muda por remarcação: a original é cancelada e outra é criada sem transportar disponibilidades;
- nova sessão é criada com D-5 já transcorrido e exige confirmação excepcional explícita;
- atleta informa indisponibilidade pós-fechamento;
- atleta antes indisponível torna-se disponível pós-fechamento;
- capacidade obrigatória deixa de ser preenchível após confirmação e aparece no diagnóstico de `QUÓRUM_COMPROMETIDO`;
- atleta comparece mas não participa, ou participa parcialmente;
- presença ou participação consolidada necessita retificação factual.

**O que não pode falhar conceitualmente:**  
- distinção entre disponibilidade, presença e participação;
- D-5 exato;
- ausência de dupla contagem;
- resolução determinística em D-5 no fluxo normal;
- preservação histórica e autoria;
- sessão confirmada não ser cancelada automaticamente por baixa posterior;
- sessão cancelada ser terminal;
- autoridade humana nas exceções esportivas e na consolidação factual.

**Consequência se falhar:**  
Retorno à cobrança e conferência manual, perda de previsibilidade, histórico não confiável e digitalização da burocracia que o produto pretende eliminar.

**Status:** confirmado como fluxo prioritário da primeira entrega.

### FLOW-002 — Consolidação e retificação de presença e participação

**Ator principal:** ACT-001.

1. Sistema prepara lista provisória com evidências disponíveis da sessão.
2. Treinador revisa exceções e consolida presença/participação.
3. Registro consolidado passa a ser a leitura oficial corrente.
4. Se erro factual for descoberto posteriormente, treinador registra retificação com valor anterior, novo valor, motivo, autoria e timestamp.
5. Histórico conserva consolidação original e retificações posteriores.

**Status:** confirmado.

---

## 6. Fatos confirmados

| ID | Fato | Origem | Data/Contexto | Impacto |
|---|---|---|---|---|
| FACT-001 | O CEPRAEA possui atualmente um treinador e 19 atletas adultas de alto rendimento | Q-002/Q-008 | 2026-09-02 | Define usuários atuais; não congela tamanho futuro do elenco |
| FACT-002 | Gestão atual depende fortemente de planilhas e WhatsApp | Q-001 | Aproximadamente dois anos | Origina PROBLEM-001 |
| FACT-003 | Uso cotidiano ocorre predominantemente em smartphones | Q-006 | Contexto atual | Relevante para experiência e decisões técnicas futuras |
| FACT-004 | Treinos atuais recorrentes concentram-se em quinta 20h00–21h30 e domingo 07h30–09h00, em Copacabana, Posto 4 | Q-010 consolidada | Recorrência atual | Alimenta proposta mensal; não impede sessões em outros dias |
| FACT-005 | Na prática atual observada, sessão recorrente em feriado aplicável no Rio de Janeiro utiliza 07h30–09h00 | Q-010 consolidada | Operação atual | Evidência contextual; a prescrição vigente está em RULE-021 |
| FACT-006 | O treinador é atualmente o único responsável pelo desenvolvimento e não possuía experiência prévia de programação | Q-006 | Primeira entrega | Restrição forte de capacidade e manutenção |
| FACT-007 | Primeira versão foi definida para entrega até 2026-09-07 com aproximadamente 42h disponíveis | Q-006 | Primeira etapa | Pressiona escopo e reversibilidade |
| FACT-008 | A realidade de uso na praia inclui conectividade móvel potencialmente instável | Q-006 | Operação real | Contexto para decisões técnicas posteriores |
| FACT-009 | Na prática atual observada, treinos podem ocorrer em qualquer dia e a recorrência de dias úteis ocorre depois das 20h, terminando até 22h | Q-010 consolidada | Operação atual | Evidência contextual; a prescrição vigente está em RULE-026 |
| FACT-010 | `Historico.json` preserva faixas anteriores de aproximadamente 8–12 h/semana, 15–20 h/semana em semanas intensas, 2–3 h/semana, até 4 h excepcionalmente e recuperação mínima desejada de 6 h/semana | evidência histórica anterior em `Historico.json`; não deriva da formulação vigente de Q-009 v2.10 | Referências empíricas secundárias, não baseline ou meta vigente | Não substituem SUCCESS-001; SUCCESS-005 deverá receber baseline e meta somente após medição real |

---

## 7. Decisões humanas confirmadas

| ID | Decisão | Motivo | Autoridade | Impacto | Pode ser revista quando |
|---|---|---|---|---|---|
| DEC-001 | Entrega inicial como PWA | Compatibilidade com prazo, custo, desenvolvimento solo e smartphones | Usuário | [não formalizado] | Se necessidades/capacidade/orçamento futuros justificarem outra forma de entrega |
| DEC-002 | Separar primeira entrega de capacidades `FUTURE` | Evitar escopo inviável e overengineering funcional | Usuário | [não formalizado] | Inclusões futuras exigem descoberta e decisão próprias |
| DEC-003 | Julgamento técnico e decisões humanas permanecem sob autoridade do treinador | Produto apoia, não substitui liderança e decisão esportiva | Usuário | [não formalizado] | Somente nova decisão explícita de produto |
| DEC-004 | Apenas `TREINADOR_ADMINISTRADOR` e `ATLETA` são papéis autenticados iniciais | Reflete a operação real atual | Usuário | [não formalizado] | Quando novos papéis existirem de fato e responsabilidades forem definidas |
| DEC-005 | Resolução automática em D-5 conforme quórum | Eliminar ação administrativa semanal normal | Usuário | [não formalizado] | Nova decisão explícita de produto |
| DEC-006 | Sessão confirmada não cancela automaticamente após baixa | Compromisso já assumido; exceção exige julgamento | Usuário | [não formalizado] | Nova decisão explícita de produto |
| DEC-007 | Presença ou participação consolidada só é corrigida por retificação auditável do treinador; os dois eixos são corrigidos juntos quando necessário | Preservar combinações válidas e histórico factual | Usuário | [não formalizado] | Nova decisão explícita de produto |
| DEC-008 | Agenda mensal é proposta automaticamente e revisada por exceção | Reduzir trabalho recorrente de criação | Usuário | [não formalizado] | Mudança explícita da operação |
| DEC-009 | D-5 se aplica a toda sessão publicada com prazo futuro, recorrente ou excepcional | Manter um fluxo normal único | Usuário | Fecha alcance da automação | Nova decisão explícita de produto |
| DEC-010 | Participante convidada não faz parte do produto nem do quórum | Eliminar burocracia sem valor | Usuário | Remove ator, conceito e questão técnica | Nova decisão explícita de produto |
| DEC-011 | Ocorrências pós-D-5 positivas e negativas alteram imediatamente a composição atual | Fechar o efeito operacional de toda mudança | Usuário | Fecha recálculo pós-D-5 | Nova decisão explícita de produto |
| DEC-012 | Cancelamento é terminal | Evitar reativação e comunicação contraditória | Usuário | Fecha o ciclo da sessão | Nova decisão explícita de produto |
| DEC-013 | Mudança de data/horário usa remarcação com nova sessão sem disponibilidades anteriores | Preservar histórico e compromisso com a data correta | Usuário | Fecha edição temporal | Nova decisão explícita de produto |
| DEC-014 | Sessão criada após seu D-5 exige confirmação excepcional explícita | Não simular automação retroativa | Usuário | Fecha criação tardia | Nova decisão explícita de produto |
| DEC-015 | Exceção pós-confirmação usa somente `QUÓRUM_COMPROMETIDO` e as decisões `MANTER TREINO`/`CANCELAR TREINO` | Reduzir fricção do treinador | Usuário | Simplifica diagnóstico e decisão | Nova decisão explícita de produto |
| DEC-016 | HYP-001, HYP-002 e HYP-003 são riscos explicitamente aceitos do piloto | Encerrar a elicitação sem fingir validação empírica | Usuário | Atende tratamento humano exigido pelo Gate B | Reavaliar após dados do piloto |
| DEC-017 | A proposta mensal inclui sessões normais e sessões possíveis nos feriados nacionais e feriados oficiais estaduais ou municipais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 | Entregar ao treinador uma proposta mensal completa para revisão por exceção | Usuário | Fecha `OPEN-001` e a abrangência da regra de feriados | Nova decisão explícita de produto |

---

## 8. Hipóteses

### HYP-001 — Adoção direta pelas atletas

**Hipótese:**  
As atletas utilizarão diretamente as ações de disponibilidade e ocorrência com fricção suficientemente baixa para retirar do treinador a intermediação normal.

**Origem:** INF a partir dos objetivos e critérios de sucesso já declarados; já identificada durante a elicitação anterior.

**Por que acreditamos nisso:**  
É condição implícita para que OBJ-004 e SUCCESS-001 produzam valor, mas ainda não existem dados reais do produto em uso.

**Confiança:** ainda não mensurada.  
**Impacto se falsa:** alto — treinador e WhatsApp continuam como intermediários.  
**Como validar:** uso real/piloto após primeira entrega.  
**Status:** não validada empiricamente; aceita explicitamente pelo usuário como risco do piloto.

### HYP-002 — Viabilidade da primeira entrega em ~42 horas

**Hipótese:**  
O escopo vigente poderá ser implementado e validado dentro do esforço declarado.

**Origem:** INF sobre CONST-004/CONST-005 e o escopo `DECIDED`.

**Confiança:** ainda não mensurada.  
**Impacto se falsa:** alto — atraso ou redução da primeira entrega.  
**Como validar:** planejamento técnico posterior e execução.  
**Status:** não validada empiricamente; aceita explicitamente pelo usuário como risco do piloto.

### HYP-003 — Redução material de horas administrativas

**Hipótese:**  
Atingir a operação por exceção e zero ações semanais obrigatórias no fluxo normal produzirá redução material das horas administrativas do treinador.

**Origem:** intenção do usuário + INF causal.  
**Evidência/referências declaradas:** `Historico.json` preserva faixas numéricas anteriores, não medidas. A formulação vigente de Q-009 v2.10 não as adota como baseline ou meta; exige medição real futura e mantém `SUCCESS-001` como critério principal.

**Confiança:** ainda não mensurada.  
**Impacto se falsa:** alto — o produto pode funcionar sem devolver tempo material ao treinador.  
**Como validar:** medição empírica em uso real, comparando a carga observada com as referências declaradas.  
**Status:** não validada empiricamente; aceita explicitamente pelo usuário como risco do piloto.

---

## 9. Ambiguidades e decisões não tomadas

### AMB-001 — Questões de produto Q-001–Q-013

**Status:** resolvida; as questões originais Q-001–Q-013 e `OPEN-001` estão fechadas.

### OPEN-001 — Critério de feriado aplicável

**Entendimento atual:**  
Além das sessões normais, a proposta mensal inclui sessões possíveis nos feriados nacionais e nos feriados oficiais estaduais ou municipais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 e sujeitas à revisão humana antes da publicação.

**Regra complementar:**  
Quando um feriado coincidir com uma recorrência normal, existe uma única sugestão para a data, no horário de feriado. Ponto facultativo, feriado exclusivamente bancário e data comemorativa não são incluídos, salvo se também forem feriado oficial aplicável.

**Status:** fechada por `DEC-017`.

### OPEN-TECH-002 — Persistência/hospedagem/execução

**O que permanece não decidido:**  
Provedor, banco, hospedagem, serverless ou equivalente.

**Status:** aberta tecnicamente; não é decisão de produto.

### OPEN-TECH-003 — Autenticação

**O que permanece não decidido:**  
Método de autenticação, login social, magic link ou equivalente.

**Status:** aberta tecnicamente; não é decisão de produto.

### OPEN-TECH-004 — Conectividade/offline/sincronização

**O que permanece não decidido:**  
Estratégia concreta de tolerância a conectividade, offline e sincronização.

**Status:** aberta tecnicamente; não é decisão de produto.

### OPEN-TECH-005 — Comunicação/notificações

**O que permanece não decidido:**  
Tecnologia e estratégia física de lembretes/comunicações/alertas.

**Status:** aberta tecnicamente; não é decisão de produto.

---

## 10. Restrições

| ID | Restrição | Tipo | Origem | Impacto | Status |
|---|---|---|---|---|---|
| CONST-001 | Desenvolvimento/manutenção por uma pessoa sem experiência prévia de programação | equipe | Q-006 | [não formalizado] | confirmada |
| CONST-002 | Desenvolvimento assistido por IA via assinaturas mensais previsíveis; sem dependência de consumo de API por tokens para desenvolvimento | custo/equipe | Q-006 | [não formalizado] | confirmada |
| CONST-003 | Custo operacional ~R$50/mês; ~R$200/mês incompatível | custo | Q-006 | [não formalizado] | confirmada |
| CONST-004 | Primeira entrega até 2026-09-07 | tempo | Q-006 | [não formalizado] | confirmada |
| CONST-005 | Aproximadamente 42 horas para primeira etapa | tempo/equipe | Q-006 | [não formalizado] | confirmada |
| CONST-006 | Primeira versão PWA | técnica decidida pelo usuário | Q-007 | [não formalizado] | confirmada |
| CONST-007 | Mobile first e uso predominante em smartphone | uso/técnica de produto | Q-006/Q-007 | [não formalizado] | confirmada |
| CONST-008 | Sem dependência de publicação em lojas nativas na primeira entrega | operação/distribuição | Q-006/Q-007 | [não formalizado] | confirmada |
| CONST-009 | Baixa capacidade de manutenção e suporte após lançamento | operação/equipe | Q-006 | [não formalizado] | confirmada |
| CONST-010 | Conectividade móvel pode ser instável na praia | ambiente | Q-006 | [não formalizado] | confirmada quanto ao contexto |
| CONST-011 | Escopo precisa permanecer proporcional a tempo, orçamento, equipe e operação do CEPRAEA | escopo | Q-006 | [não formalizado] | confirmada |

---

## 11. Atributos de qualidade desejados

Estes itens permanecem entendimento de qualidade; sua eventual formalização como NFR pertence a `Chat 04 — Requirements`, agora autorizado, e não é executada neste artefato.

| ID | Qualidade | Significado neste contexto | Prioridade | Evidência |
|---|---|---|---|---|
| QA-001 | Usabilidade / baixa fricção | Ações cotidianas simples, poucos passos, uso com polegar e compreensão rápida da próxima ação | [não formalizada] | Q-004/Q-006 |
| QA-002 | Confiabilidade informacional | Declarações, fatos, autoria, publicação e retificação preservados sem sobrescrita silenciosa | [não formalizada] | Q-004/Q-010–Q-013 |
| QA-003 | Privacidade / segurança adequada ao contexto | Dados individuais não ficam indiscriminadamente acessíveis e atleta não altera dados alheios ou fatos consolidados | [não formalizada] | Q-008 |
| QA-004 | Leveza/desempenho percebido | Uso em smartphones novos e antigos dentro de limites razoáveis, sem interfaces pesadas desnecessárias | [não formalizada] | Q-006 |
| QA-005 | Tolerância a conectividade instável | Fluxos reais ocorrem na praia e não podem assumir internet excelente; estratégia concreta ainda não decidida | [não formalizada] | Q-006 |
| QA-006 | Baixa operabilidade/manutenção | Sistema deve exigir pouca intervenção técnica cotidiana do treinador após lançamento | [não formalizada] | Q-006 |
| QA-007 | Economia operacional | Execução precisa permanecer compatível com orçamento recorrente muito baixo | [não formalizada] | Q-006 |
| QA-008 | Sinalização por exceção | Sistema chama atenção principalmente quando existe problema real, evitando alertas excessivos | [não formalizada] | Q-004/Q-013 |

---

## 12. Riscos

| ID | Risco | Origem | Probabilidade | Impacto | Relações |
|---|---|---|---|---|---|
| RISK-001 | Escopo exceder as ~42h da primeira etapa | USR + INF | [não formalizada] | [não formalizado] | CONST-004/005/011, DEC-002 |
| RISK-002 | Digitalizar a burocracia sem reduzi-la | USR | [não formalizada] | [não formalizado] | OBJ-001, SUCCESS-001 |
| RISK-003 | Baixa adoção das atletas manter intermediação pelo treinador/WhatsApp | USR + INF | [não formalizada] | [não formalizado] | OBJ-004, HYP-001 |
| RISK-004 | Custo recorrente ultrapassar sustentabilidade | USR + INF | [não formalizada] | [não formalizado] | CONST-003 |
| RISK-005 | Manutenção/suporte tornarem-se nova carga permanente | USR + INF | [não formalizada] | [não formalizado] | CONST-001/009 |
| RISK-006 | Conectividade instável comprometer uso real | USR | [não formalizada] | [não formalizado] | CONST-010, OPEN-TECH-004 |
| RISK-007 | Mistura ou sobrescrita de disponibilidade, presença, participação e histórico | USR | [não formalizada] | [não formalizado] | RULE-001/018/019/030 |
| RISK-008 | Projeção/automação ser interpretada como decisão humana | USR | [não formalizada] | [não formalizado] | OBJ-005, DEC-003 |
| RISK-009 | Excesso de alertas reduzir atenção ao canal | USR | [não formalizada] | [não formalizado] | QA-008, OPEN-TECH-005 |
| RISK-010 | Informação individual ser exposta além do necessário | USR + INF | [não formalizada] | [não formalizado] | RULE-024, QA-003 |
| RISK-011 | Abrangência de “feriado aplicável” produzir propostas de agenda diferentes | auditoria independente `AUD-024` + revisão semântica posterior | não aplicável após tratamento | material antes do tratamento | Resolvido por DEC-017 e RULE-021; resta somente a escolha técnica futura da fonte de calendário |

---

## 13. Questões em aberto

### Questões de produto abertas conhecidas

`NONE` — `OPEN-001` foi fechado por `DEC-017`.

Nenhuma questão material de produto atualmente conhecida permanece aberta neste escopo. Se uma fase posterior revelar uma lacuna que não possa ser resolvida sem criar nova intenção ou regra de produto, ela deve retornar à elicitação e à autoridade humana.

### Questões técnicas explicitamente adiadas

| ID | Questão | Categoria | Impacto | Incerteza | Valor de informação | Bloqueadora? |
|---|---|---|---|---|---|---|
| OPEN-TECH-002 | Persistência/hospedagem/execução | técnica/arquitetural futura | [não formalizado] | [não formalizada] | [não formalizado] | Não agora |
| OPEN-TECH-003 | Método de autenticação | técnica/arquitetural futura | [não formalizado] | [não formalizada] | [não formalizado] | Não agora |
| OPEN-TECH-004 | Offline/conectividade/sincronização | técnica/arquitetural futura | [não formalizado] | [não formalizada] | [não formalizado] | Não agora |
| OPEN-TECH-005 | Mecanismo de lembretes/comunicações/alertas | técnica/arquitetural futura | [não formalizado] | [não formalizada] | [não formalizado] | Não agora |

### Estado processual após aprovação do Gate B

- `GATE-B-CANONICALIZATION = APPROVED`;
- `GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS`;
- `GATE-B-DOMAIN-MODEL = PASS`;
- `GATE-B-FINAL = APPROVED`;
- `Chat 04 — Requirements = AUTHORIZED`;
- `Drivers = NOT_YET_AUTHORIZED`;
- `Alternatives/Options = NOT_YET_AUTHORIZED`;
- `ADRs = NOT_YET_AUTHORIZED`;
- `Architecture = NOT_YET_AUTHORIZED`.

---

## 14. Contradições conhecidas e formulações substituídas

Não há contradição ativa declarada entre decisões de produto vigentes. As formulações históricas abaixo foram explicitamente substituídas e devem permanecer rastreáveis.

| ID | Formulação histórica | Status | Resolução vigente |
|---|---|---|---|
| SUPERSEDED-001 | Fechamento na véspera/24h/horário genérico | substituída | D-5 = início −120h |
| SUPERSEDED-002 | Wellness determina presença | substituída | Wellness é evidência futura; treinador consolida presença/participação |
| SUPERSEDED-003 | Treinador cria todos os treinos | substituída | Proposta mensal automática + revisão por exceção |
| SUPERSEDED-004 | Quórum `1G + 3D + 4A` | substituída | 4 Ataque + 4 Defesa + 8 distintas + ≥1 Goleira na Defesa |
| SUPERSEDED-005 | Papéis genéricos Atacante/Defensora/Goleira bastam | substituída | `Fase → Sistema → Posição` |
| SUPERSEDED-006 | Declaração antecipada pode ser presença | substituída | Disponibilidade, presença e participação são distintas |
| SUPERSEDED-007 | Número de baixas ou classe separada de falha crítica define a exceção | substituída | Toda composição inválida pós-confirmação é `QUÓRUM_COMPROMETIDO`; o déficit exato é diagnóstico |
| SUPERSEDED-008 | Produto completo e MVP têm mesmo escopo | substituída | Primeira entrega separada de `FUTURE` |
| SUPERSEDED-009 | Quórum antecipado permite confirmação manual normal | substituída | Apenas `QUÓRUM_GARANTIDO`; confirmação ocorre em D-5 |
| SUPERSEDED-010 | D-5 sem quórum exige decisão do treinador | substituída | Cancelamento automático por `FALTA_DE_QUÓRUM` |
| SUPERSEDED-011 | Apenas quinta recorrente ajusta feriado | substituída | A proposta mensal inclui sessões possíveis nos feriados nacionais e oficiais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 |
| SUPERSEDED-012 | Horas estimadas são critério principal do MVP | substituída | Zero ações administrativas obrigatórias no fluxo semanal normal; as faixas de `Historico.json` permanecem somente como evidência histórica secundária de SUCCESS-005, sem baseline ou meta vigente |
| SUPERSEDED-013 | Presença consolidada sem correção fechada | substituída | Retificação auditável de presença e participação pelo treinador, sem sobrescrita |
| SUPERSEDED-014 | Participante convidada era cadastrada e podia contar no quórum | substituída | Não faz parte do produto nem do cálculo; o treinador apenas mantém ou cancela diante da exceção |
| SUPERSEDED-015 | Data/horário de sessão publicada podiam ser substituídos por edição | substituída | Remarcação cancela a original e cria outra sessão sem transportar disponibilidades |

---

## 15. Mudanças de entendimento

| Data | Item | Entendimento anterior | Novo entendimento | Motivo | Impactados |
|---|---|---|---|---|---|
| 2026-09-02 | D-5 | Véspera/horários anteriores | Exatamente −120h | consolidação v2.4 | FLOW-001, RULE-004/009/010 |
| 2026-09-02 | Wellness | Parte da presença no MVP | `FUTURE`; não determina presença | consolidação v2.4 | CONCEPT-004/005, escopo |
| 2026-09-02 | Agenda | Criação manual de treinos | Proposta mensal automática + revisão por exceção | consolidação v2.4 | FLOW-001, RULE-020 |
| 2026-09-02 | Quórum | 1G+3D+4A | 4 Ataque + 4 Defesa + 8 distintas + ≥1 Goleira defensiva | consolidação v2.4 | CONCEPT-007, RULE-006 |
| 2026-09-02 | D-5 sem quórum | Decisão humana requerida | Cancelamento automático | consolidação v2.4 | RULE-010, FLOW-001 |
| 2026-09-02 | Sucesso MVP | Horas estimadas eram tratadas como critério principal | `SUCCESS-001` passa a ser zero ações administrativas semanais obrigatórias no fluxo normal; as faixas registradas em `Historico.json` permanecem somente como evidência histórica secundária de `SUCCESS-005`, sem baseline ou meta vigente | consolidação v2.4 + `AUD-023` | OBJ-001, SUCCESS-001, SUCCESS-005, FACT-010 |
| 2026-09-02 | Presença consolidada | Correção não fechada | Retificação auditável sem sobrescrita | consolidação v2.4 | CONCEPT-011, RULE-018 |
| 2026-09-02 | Estado do Gate B | Formulação anterior podia sugerir avanço a Requirements | Conhecimento pronto com riscos; canonicalização/auditoria/modelo de domínio pendentes; final não aprovado | retificação processual explícita | processo, Requirements |
| 2026-09-02 | Correções da auditoria | Exceções, remarcação, convidada, retificação e riscos possuíam lacunas | Fluxo simples aprovado na versão 2.6 e hipóteses de alto impacto aceitas como riscos do piloto | decisão explícita do usuário | atores, conceitos, regras, fluxos, Gate B |
| 2026-09-02 | Reauditoria independente | Correções aplicadas aguardavam reauditoria | `GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS`; modelagem do domínio autorizada, Gate B final e Requirements ainda pendentes | reauditoria v2.6/1.2 | processo, OPEN-DOMAIN-001, RISK-011 |
| 2026-09-02 | Vocabulário normativo | Termos sensíveis podiam receber interpretações arquiteturais não autorizadas | `PRODUCT-DOMAIN-SPEC.md` v2.7 define o vocabulário canônico de produto/domínio; o contrato v1.3 apenas o herda e define termos contratuais próprios | restrição semântica editorial | conceitos, contrato lógico, agentes consumidores |
| 2026-09-02 | Critério de feriado aplicável | A abrangência seria testada pela modelagem como risco não bloqueador | `OPEN-001` é decisão de produto material e deve ser fechada por autoridade humana antes da modelagem do domínio | revisão semântica posterior | RULE-021, FACT-005, RISK-011, processo |
| 2026-09-02 | Fechamento de `OPEN-001` | Categorias de feriado aplicável permaneciam abertas | A proposta mensal inclui sessões possíveis em feriados nacionais e feriados oficiais estaduais ou municipais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 | decisão explícita do usuário | DEC-017, RULE-021, RISK-011, processo |

---

## 16. Capacidades futuras (`FUTURE`)

| ID | Capacidade | Status |
|---|---|---|
| FUTURE-001 | Wellness Pré e Pós-Treino | FUTURE |
| FUTURE-002 | Planejamento de exercícios e temporada | FUTURE |
| FUTURE-003 | Biblioteca de exercícios | FUTURE |
| FUTURE-004 | Publicação de conteúdo técnico/tático | FUTURE |
| FUTURE-005 | Vídeos, cortes e associação vídeo-eventos | FUTURE |
| FUTURE-006 | Scouts, relatórios e análise de desempenho | FUTURE |
| FUTURE-007 | Avaliações e feedbacks individuais | FUTURE |
| FUTURE-008 | Histórico de adversários e preparação de jogos | FUTURE |
| FUTURE-009 | Materiais e responsabilidades logísticas | FUTURE |
| FUTURE-010 | Registros auxiliares de competições, resultados e classificações | FUTURE |
| FUTURE-011 | Controles financeiros simples da rotina | FUTURE |

**Não fechados como requisito:** gamificação, rankings, pontuações de disciplina, geração automática de materiais públicos e automação de substituições.

---

## 17. Resumo executivo do entendimento atual

### Sabemos

- o problema central e os beneficiários principais;
- a primeira entrega e as capacidades futuras explicitamente separadas;
- o fluxo prioritário de agenda até presença factual;
- os dois papéis autenticados iniciais;
- a semântica de disponibilidade, presença e participação;
- o D-5 exato;
- o quórum operacional da primeira entrega;
- o comportamento determinístico de confirmação/cancelamento em D-5;
- a separação conceitual entre estado programado da Agenda Esportiva, ciclos próprios de Participação Esportiva e projeções de quórum/déficit/próxima ação;
- o tratamento de ocorrência pós-fechamento;
- a autoridade humana nas exceções esportivas e consolidação factual;
- a regra de retificação auditável;
- as principais restrições de prazo, esforço, custo, dispositivo e manutenção.

### Aceitamos como riscos do piloto, ainda sem validação empírica

- que as atletas adotarão suficientemente o autoatendimento;
- que o escopo cabe tecnicamente em ~42h;
- que a operação por exceção produzirá redução material de horas administrativas; `Historico.json` preserva faixas numéricas anteriores somente como evidência histórica, sem baseline ou meta vigente, e o impacto será validado por medição real.

### Não sabemos / não foi decidido tecnicamente

- provedor/estrutura de persistência e execução;
- método de autenticação;
- estratégia offline/sincronização;
- tecnologia de lembretes/comunicação/notificações;
- schemas, APIs, serviços, módulos ou outras estruturas de implementação.

### Autorização para Requirements

Nenhuma decisão de produto atualmente conhecida permanece aberta, `OPEN-001` está fechado, a modelagem do domínio foi validada com `PASS` e `GATE-B-FINAL = APPROVED`. `Chat 04 — Requirements` está autorizado; esta canonicalização não produz requisitos.

---

## 18. Gate para transformar entendimento em requisitos

### Prontidão do conhecimento

- [x] principais objetivos estão confirmados;
- [x] principais atores foram explorados no nível necessário ao entendimento atual;
- [x] fluxo crítico prioritário foi percorrido;
- [x] conceitos de domínio críticos identificados na elicitação estão explicitados;
- [x] regras críticas identificadas na elicitação estão registradas;
- [x] restrições críticas estão explícitas;
- [x] hipóteses de alto impacto foram explicitamente aceitas pelo usuário como riscos do piloto, com impacto e validação posterior registrados;
- [x] `OPEN-001` — critério de feriado aplicável — foi decidido pela autoridade humana e reconciliado;
- [x] ambiguidades originais de produto Q-001–Q-013 foram resolvidas;
- [x] contradições históricas conhecidas foram tratadas como `SUPERSEDED`;
- [x] questões técnicas não decididas estão visíveis e não foram convertidas em decisões de produto.

### Estado formal

```text
GATE-B-KNOWLEDGE = READY_WITH_RISKS
GATE-B-CANONICALIZATION = APPROVED
GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS
ELICITATION-OPEN = NONE
GATE-B-DOMAIN-MODEL = PASS
GATE-B-FINAL = APPROVED
```

**Conclusão:** este documento registra o fechamento de `OPEN-001`, a modelagem do domínio validada com `PASS` e `GATE-B-FINAL = APPROVED`. A próxima fase autorizada é `04 — Requirements`; Drivers, Alternatives/Options, ADRs e Architecture permanecem não autorizados.


---

## 19. Modelagem do domínio — estado canônico

### 19.1 Resultado formal

```text
DOMAIN-MODEL = PASS
DOMAIN-MODEL-REGRESSION = PASS
```

O resultado inicial `DOMAIN-MODEL = PASS_WITH_RISKS` permanece apenas como histórico da primeira rodada de modelagem. A validação de regressão contra `PRODUCT-DOMAIN-SPEC.md` v2.10 e `TRAINING_FLOW_CONTRACT.md` v1.6 concluiu que nenhuma semântica central foi invalidada e que o risco semântico de feriados foi encerrado por `DEC-017`.

### 19.2 Refinamentos conceituais consolidados

| Elemento | Estado canônico da modelagem | Proveniência |
|---|---|---|
| `Agenda Esportiva` | agrupamento conceitual das regras de compromissos e ciclo das sessões; não foi introduzida identidade ou ciclo autônomo adicional | conceito `DECIDED`; ausência de identidade/ciclo adicional `INF-DERIVED` |
| `Sessão de treino` | compromisso com identidade conceitual e ciclo `PLANEJADO → PUBLICADO → CONFIRMADO/CANCELADO → REALIZADO`, respeitando as transições confirmadas | `DECIDED-supported` |
| `Disponibilidade` | declaração anterior à sessão, semanticamente distinta de presença e participação | `DECIDED-supported` |
| `Ocorrência pós-fechamento` | fato posterior a D-5 que complementa a declaração sem reescrevê-la | `DECIDED-supported` |
| `Perfil esportivo` | posição principal obrigatória + posição secundária opcional, organizadas por `Fase → Sistema → Posição` | `DECIDED-supported` |
| `Alocação da sessão` | distribuição contextual de atletas distintas nas vagas de Ataque e Defesa para verificar executabilidade | `DECIDED-supported` |
| `Quórum operacional` | existência de alocação válida com 4 Ataque + 4 Defesa + 8 atletas distintas + ≥1 Goleira na Defesa | `DECIDED-supported` |
| `D-5` | instante `início_da_sessão − 120 horas`; política temporal da primeira entrega | `DECIDED-supported` |
| `Presença` | fato consolidado sobre comparecimento | `DECIDED-supported` |
| `Participação` | fato consolidado sobre realização integral, parcial ou nula da atividade | `DECIDED-supported` |
| `Retificação auditável` | correção factual sem sobrescrita, preservando valor anterior, novo valor, motivo, autor e data/hora | `DECIDED-supported` |
| Estado da sessão × condição/projeção | dimensões semanticamente distintas; projeção não é estado nem fonte de verdade | `DECIDED-supported` |
| `CANCELADO` | estado terminal; não reativa e não recebe novas ocorrências | `DECIDED-supported` |
| Remarcação | cancela a original com `REMARCADO` e cria outra sessão sem transportar disponibilidades | `DECIDED-supported` |
| Feriado aplicável no Rio de Janeiro | feriado nacional ou oficial estadual/municipal aplicável à cidade do Rio; exclui ponto facultativo, exclusivamente bancário e mera data comemorativa sem feriado oficial aplicável | `DECIDED`, origem `DEC-017` / `RULE-021` |

### 19.3 Invariantes da modelagem e proveniência

`DECIDED-supported` significa que o conteúdo está diretamente sustentado por decisão, regra ou definição canônica substantiva. `INF-DERIVED` identifica formalização lógica da modelagem que não constitui nova declaração humana independente.

| ID | Invariante | Proveniência | Origem rastreável |
|---|---|---|---|
| DM-INV-001 | `Disponibilidade ≠ Presença ≠ Participação` | `DECIDED-supported` | RULE-001; CONCEPT-003/004/005 |
| DM-INV-002 | `NÃO RESPONDEU ≠ INDISPONÍVEL` | `DECIDED-supported` | RULE-002; CONCEPT-003 |
| DM-INV-003 | ausência de apuração não equivale a ausência nem a não participação | `DECIDED-supported` | RULE-003; CONCEPT-004/005 |
| DM-INV-004 | somente as cinco combinações confirmadas Presença × Participação são válidas | `DECIDED-supported` | RULE-019; CONCEPT-004/005 |
| DM-INV-005 | quórum exige 4 Ataque + 4 Defesa + 8 atletas distintas + ≥1 Goleira na Defesa | `DECIDED-supported` | RULE-006; CONCEPT-007 |
| DM-INV-006 | uma atleta não satisfaz duas vagas simultaneamente | `DECIDED-supported` | RULE-008; CONCEPT-008 |
| DM-INV-007 | perfil esportivo e alocação contextual são distintos; alocação não altera o perfil | `DECIDED-supported` | glossário `Perfil esportivo` / `Alocação da sessão`; RULE-007/008 |
| DM-INV-008 | ocorrência pós-D-5 não reescreve disponibilidade anterior | `DECIDED-supported` | RULE-012; CONCEPT-006 |
| DM-INV-009 | projeção de quórum não substitui fatos de origem nem decisão humana | `DECIDED-supported` | glossário `Projeção de quórum`; OBJ-005; DEC-003 |
| DM-INV-010 | realização da sessão não implica automaticamente presença ou participação individuais | `INF-DERIVED` | RULE-003/018/027; CONCEPT-002/004/005 |
| DM-INV-011 | remarcação preserva a sessão original e cria outra | `DECIDED-supported` | DEC-013; RULE-022 |
| DM-INV-012 | disponibilidades da sessão original não são transportadas para a remarcada | `DECIDED-supported` | DEC-013; RULE-022 |
| DM-INV-013 | fato consolidado incorreto é corrigido por retificação, não sobrescrita | `DECIDED-supported` | DEC-007; RULE-030; CONCEPT-011 |
| DM-INV-014 | retificação preserva valor anterior, novo valor, motivo, autor e momento | `DECIDED-supported` | CONCEPT-011; RULE-030 |
| DM-INV-015 | toda retificação deve resultar em combinação válida de Presença × Participação | `INF-DERIVED` | RULE-019 + RULE-030 + CONCEPT-011 |

Nenhum `DM-INV-001..015` foi invalidado pela regressão.

### 19.4 Itens históricos ou superados pela regressão

| Item | Estado | Resolução vigente |
|---|---|---|
| `OPEN-DOMAIN-001` | histórico / superado | foi convertido em `OPEN-001` e fechado por `DEC-017` |
| `DM-FIND-005` — feriado poderia permanecer predicado aberto | histórico / `SUPERSEDED_BY_DEC-017` | a definição de feriado aplicável está fechada no glossário canônico |
| `CAN-DM-005` — preservar `OPEN-DOMAIN-001` como risco | histórico / superado | substituído pela canonicalização de `DEC-017` / `RULE-021` |
| `DOMAIN-MODEL = PASS_WITH_RISKS` | histórico | substituído, após regressão, por `DOMAIN-MODEL = PASS` |

### 19.5 Rejeições e destinos preservados

- `AUD-025`: “situação operacional” permanece conceito rejeitado por falta de sustentação canônica; não criar estados derivados desse termo.
- `AUD-026 → INF-TECH-001`: idempotência/reprocessamento do checkpoint D-5 permanece candidato técnico futuro, fora do modelo de domínio confirmado.
- `AUD-023`: permanece correção de proveniência das referências de horas; não cria conceito de domínio.
- `AUD-027`: permanece correção processual; não cria conceito de domínio.
- participante convidada permanece fora da primeira entrega e do cálculo de quórum.
- quórum não é estado da sessão; ausência de capacidade obrigatória é diagnóstico, não novo estado.

### 19.6 Avaliação de prontidão da modelagem

A modelagem do domínio não possui questão de produto atualmente conhecida que exija retorno à elicitação. `ELICITATION-OPEN = NONE` mantém significado estritamente atual: se nova lacuna material surgir em fase posterior e exigir nova intenção ou regra humana, deverá retornar à elicitação sem preenchimento por inferência.

A modelagem está `PASS` e `GATE-B-FINAL = APPROVED`. `04 — Requirements` é a próxima fase autorizada; nenhuma fase arquitetural posterior foi autorizada por esta decisão.
