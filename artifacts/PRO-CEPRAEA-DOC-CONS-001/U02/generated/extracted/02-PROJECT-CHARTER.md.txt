# PROJECT CHARTER

> **ARTEFATO CANÔNICO — GATE B FINAL APROVADO**  
> A modelagem e sua regressão foram aprovadas; `GATE-B-FINAL = APPROVED` e `Chat 04 — Requirements` está autorizado.

**Projeto:** CEPRAEA BEACH PRO  
**Forma de entrega da primeira versão:** PWA  
**Versão:** 0.9  
**Status:** Elicitação consolidada; reauditoria `PASS WITH RISKS`; modelagem do domínio `PASS`; Gate B final `APPROVED`; Requirements autorizado  
**Última atualização:** 2026-09-03  
**Origem principal:** `PRODUCT-DOMAIN-SPEC.md`, versão 2.10; proveniência histórica em `Historico.json`

**Nota de proveniência editorial:** IDs, títulos curtos e redações sintéticas introduzidos neste artefato são organização `INF`; o conteúdo substantivo somente é marcado como confirmado quando sustentado pelas declarações consolidadas do usuário.

---

## 1. Visão

O CEPRAEA BEACH PRO deve ser o ponto único, confiável e acionável para a operação esportiva cotidiana do CEPRAEA.

O produto deve reduzir a dependência de planilhas, WhatsApp, arquivos dispersos e conferências manuais; organizar a rotina; preservar fatos diferentes sem misturá-los; antecipar problemas operacionais; aumentar a autonomia das atletas; e devolver tempo e atenção do treinador ao trabalho esportivo.

A finalidade não é apenas digitalizar a gestão atual. É reduzir a burocracia que hoje depende do treinador e criar melhores condições para planejar, analisar, ensinar, avaliar e treinar.

**Status:** confirmado (`DECIDED`)  
**Origem:** Q-001, Q-002 e Q-003 da consolidação v2.6.

---

## 2. Problema

### PROBLEM-001 — Sobrecarga operacional e fragmentação da gestão do CEPRAEA

**Descrição:**  
A gestão atual do CEPRAEA depende de planilhas, WhatsApp, documentos, vídeos, arquivos e conferências manuais que não foram construídos para representar nem coordenar adequadamente a realidade operacional e esportiva da equipe. O treinador precisa integrar manualmente calendário, disponibilidade, composição, presença, alterações, comunicação e outras informações, tornando-se intermediário de grande parte da operação.

**Quem sofre o problema:**  
- primariamente, o treinador do CEPRAEA;
- diretamente, as atletas, que dependem da qualidade, previsibilidade e organização do trabalho esportivo.

**Quando ocorre:**  
De forma recorrente na organização mensal e semanal da equipe, especialmente na programação de treinos, solicitação e acompanhamento de disponibilidade, formação de quórum, alterações de última hora, apuração de presença e busca de informações operacionais.

**Consequência atual:**  
- carga administrativa e mental elevada para o treinador;
- necessidade de cobranças e conferências manuais;
- problemas descobertos tarde demais;
- histórico pouco confiável quando declaração e fato são misturados;
- menos tempo e atenção disponíveis para planejamento, análise, ensino, avaliação e treinamento;
- risco de falhas operacionais que afetam a execução do treino e a percepção de organização.

**Evidência disponível:**  
- aproximadamente dois anos de gestão baseada em planilhas;
- cobranças recorrentes de resposta de 19 atletas via WhatsApp;
- marcação incorreta de treino noturno em feriado;
- treino tático inviabilizado pela ausência de goleira, percebida somente na praia;
- possibilidade de respostas de disponibilidade serem alteradas após o treino;
- arquivos e comunicados importantes dispersos ou inacessíveis no WhatsApp.

**Status:** confirmado (`DECIDED`)  
**Origem:** Q-001 da consolidação v2.6.

---

## 3. Objetivos

### OBJ-001 — Devolver tempo e atenção ao trabalho esportivo

**Objetivo:**  
Reduzir o trabalho administrativo rotineiro que depende do treinador para que sua capacidade de tempo e atenção seja direcionada ao trabalho esportivo e à vida pessoal quando apropriado.

**Motivação:**  
A burocracia atual compete diretamente com planejamento, estudo, análise, avaliação, feedback e treinamento.

**Como saberemos que foi alcançado:**  
O principal critério operacional da primeira entrega é `ações administrativas obrigatórias do treinador no fluxo semanal normal = 0` após a revisão e publicação mensal da agenda, ressalvadas exceções reais pós-confirmação que exijam julgamento esportivo.

**Prioridade:** [não formalizada]  
**Status:** confirmado

### OBJ-002 — Operar a agenda por exceção e com previsibilidade

**Objetivo:**  
Fazer com que sessões publicadas sejam acompanhadas e resolvidas automaticamente no fluxo normal, permitindo identificar antecipadamente se o treino será confirmado ou cancelado por falta de quórum e reservando intervenção humana para alterações e exceções reais.

**Motivação:**  
Evitar cobranças, contagens e interpretações manuais e impedir que problemas operacionais previsíveis sejam descobertos somente na praia.

**Como saberemos que foi alcançado:**  
Sessões publicadas percorrem o fluxo normal até D-5 sem ação administrativa semanal obrigatória do treinador e recebem resolução automática conforme o quórum.

**Prioridade:** [não formalizada]  
**Status:** confirmado

### OBJ-003 — Preservar informação e histórico confiáveis

**Objetivo:**  
Manter separados fatos e declarações diferentes, preservar autoria e histórico e impedir alterações silenciosas do passado.

**Motivação:**  
A gestão atual não distingue com segurança o que foi declarado antes do treino, o que mudou depois e o que efetivamente aconteceu.

**Como saberemos que foi alcançado:**  
Disponibilidade, ocorrência pós-fechamento, presença e participação permanecem distintos; sessões, presenças e participações consolidadas não são sobrescritas silenciosamente; correções preservam histórico e autoria.

**Prioridade:** [não formalizada]  
**Status:** confirmado

### OBJ-004 — Aumentar a autonomia operacional das atletas

**Objetivo:**  
Permitir que as atletas consultem e informem diretamente aquilo que depende delas sem o treinador funcionar como intermediário normal.

**Motivação:**  
Cobranças, transcrições e consultas via WhatsApp transferem trabalho operacional para o treinador e reduzem a autonomia das atletas.

**Como saberemos que foi alcançado:**  
As atletas registram diretamente disponibilidade e ocorrências e consultam sua próxima ação e o estado simples de seus compromissos no produto.

**Prioridade:** [não formalizada]  
**Status:** confirmado

### OBJ-005 — Apoiar decisões esportivas sem substituir a autoridade humana

**Objetivo:**  
Organizar, calcular, projetar, alertar e preparar evidências para decisão, mantendo sob autoridade do treinador decisões esportivas, liderança e consolidação factual quando aplicável.

**Motivação:**  
O produto deve retirar trabalho mecânico, não substituir julgamento técnico e humano.

**Como saberemos que foi alcançado:**  
Projeções e automações determinísticas permanecem distinguíveis de decisões humanas; situações pós-confirmação que exigem julgamento esportivo são apresentadas ao treinador sem produzir decisão automática indevida.

**Prioridade:** [não formalizada]  
**Status:** confirmado

---

## 4. Critérios de sucesso

### SUCCESS-001 — Zero ações administrativas obrigatórias no fluxo semanal normal

**Métrica ou evidência:**  
Quantidade de ações administrativas obrigatórias realizadas pelo treinador entre a publicação mensal e a resolução normal da sessão em D-5.

**Meta:**  
`0` por sessão dentro do fluxo normal.

**Horizonte:**  
Primeira entrega operacional / piloto iniciado após 2026-09-07.

**Status:** confirmado (`DECIDED`)  
**Origem:** Q-009 e Q-010.

### SUCCESS-002 — Resolução automática das sessões publicadas em D-5

**Métrica ou evidência:**  
- quantidade de sessões publicadas;
- quantidade de sessões resolvidas automaticamente em D-5;
- quantidade confirmada automaticamente;
- quantidade cancelada automaticamente por `FALTA_DE_QUÓRUM`.

**Meta:**  
No fluxo normal, toda sessão publicada deve alcançar em D-5 uma resolução determinística conforme as regras vigentes, sem confirmação, cancelamento, cálculo ou comunicação administrativa manual do treinador.

**Horizonte:**  
Primeira entrega operacional.

**Status:** confirmado

### SUCCESS-003 — Operação sem dependência cotidiana do WhatsApp

**Métrica ou evidência:**  
Uso do WhatsApp deixa de ser necessário para cobrar disponibilidade, representar o estado da sessão ou registrar fatos que pertencem ao fluxo normal da primeira entrega.

**Meta:**  
Evidência qualitativa de que o WhatsApp não funciona como infraestrutura operacional cotidiana do fluxo coberto pelo MVP.

**Horizonte:**  
Primeiras semanas de uso.

**Status:** confirmado como evidência de sucesso; sem métrica numérica fechada.

### SUCCESS-004 — Histórico confiável e auditável

**Métrica ou evidência:**  
Capacidade de distinguir e rastrear declaração, ocorrência posterior, presença, participação, alterações de sessão e retificações.

**Meta:**  
Nenhum fato consolidado ou publicação histórica deve ser silenciosamente sobrescrito no fluxo coberto.

**Horizonte:**  
Desde a primeira entrega.

**Status:** confirmado

### SUCCESS-005 — Redução real de horas administrativas

**Métrica ou evidência:**  
Horas administrativas efetivamente medidas em uso real, comparadas às referências empíricas preservadas no registro histórico anterior.

**Evidência histórica anterior, não baseline vigente:**  
- aproximadamente `8–12 h/semana` em uma semana comum;
- podendo chegar a aproximadamente `15–20 h/semana` em semanas mais intensas.

**Referências de impacto declaradas:**  
- aproximadamente `2–3 h/semana` de administração rotineira;
- até aproximadamente `4 h/semana` em períodos excepcionais;
- recuperação mínima desejada de `6 h/semana`.

**Relação com o critério principal do MVP:**  
Essas faixas provêm de `Historico.json`, não da formulação vigente de Q-009 em `PRODUCT-DOMAIN-SPEC.md` v2.10. São evidência histórica secundária, não constituem baseline ou meta aprovada e não substituem `SUCCESS-001 — Zero ações administrativas obrigatórias no fluxo semanal normal`.

**Horizonte:**  
Validação empírica em uso real, quando existirem dados suficientes para comparar a carga observada com as referências declaradas.

**Status:** referência empírica secundária declarada; ainda não validada por medição real.

---

## 5. Não objetivos

| ID | Não estamos tentando | Motivo / limite confirmado | Status |
|---|---|---|---|
| NOT-001 | Ser uma plataforma esportiva genérica | O foco é a realidade do CEPRAEA no Handebol de Praia. | confirmado |
| NOT-002 | Atender Handebol Indoor | Não ampliar escopo para uma modalidade com necessidades diferentes. | confirmado |
| NOT-003 | Gerir campeonatos, federações ou arbitragem | O produto administra e desenvolve o CEPRAEA, não o evento externo. | confirmado |
| NOT-004 | Ser rede social pública ou plataforma de mídia para torcedores | O ambiente é prioritariamente interno e esportivo. | confirmado |
| NOT-005 | Operar streaming próprio | Vídeo pode apoiar trabalho esportivo futuro, sem criar plataforma pública de transmissão. | confirmado |
| NOT-006 | Ser prontuário, diagnosticar ou prescrever tratamento, medicamento ou dieta | Informações esportivas não substituem profissionais de saúde. | confirmado |
| NOT-007 | Ser editor profissional de vídeo ou simulador 3D | Recursos avançados de edição não pertencem ao problema principal. | confirmado |
| NOT-008 | Ser sistema contábil empresarial | Controles simples ligados à equipe podem existir no futuro, sem operação contábil completa. | confirmado |
| NOT-009 | Ser plataforma de recrutamento | Scout refere-se ao desempenho esportivo do elenco, não busca de atletas no mercado. | confirmado |
| NOT-010 | Substituir julgamento técnico, liderança ou relacionamento humano do treinador | O sistema apoia decisões; autoridade esportiva e humana permanece com o treinador. | confirmado |

---

## 6. Escopo inicial

### Escopo obrigatório confirmado da primeira entrega (`DECIDED`)

- elenco atual e os papéis autenticados `TREINADOR_ADMINISTRADOR` e `ATLETA`;
- proposta mensal, revisão por exceção e publicação da agenda;
- declaração de disponibilidade com `DISPONÍVEL`, `INDISPONÍVEL`, `TALVEZ` e `NÃO RESPONDEU` semanticamente distintos;
- cálculo de quórum e resolução automática em D-5 para toda sessão publicada, recorrente ou excepcional;
- confirmação excepcional explícita quando uma nova sessão é criada com D-5 já transcorrido;
- ocorrências pós-D-5 `NÃO PODEREI COMPARECER` e `AGORA POSSO PARTICIPAR`, com efeito imediato no quórum atual;
- tratamento de `QUÓRUM_COMPROMETIDO` somente por `MANTER TREINO` ou `CANCELAR TREINO`;
- cancelamento terminal, sem reativação;
- `REMARCAR TREINO`, cancelando a original e criando outra sessão sem transportar disponibilidades;
- apuração de presença e participação pelas combinações válidas confirmadas;
- retificação auditável de presença e participação pelo treinador/administrador;
- próxima ação e visão operacional simples para treinador e atleta;
- histórico auditável das sessões, declarações, ocorrências, decisões e fatos.

Participantes convidadas não fazem parte do produto nem do cálculo de quórum.

### Fora da primeira entrega, mas parte da visão (`FUTURE`)

- Wellness Pré e Pós-Treino;
- planejamento de exercícios e de temporada;
- biblioteca de exercícios;
- publicação de conteúdo técnico e tático;
- vídeos, cortes e associação entre vídeo e eventos;
- scouts, relatórios e análise de desempenho;
- avaliações e feedbacks individuais;
- histórico de adversários e preparação de jogos;
- organização de materiais e responsabilidades logísticas;
- registros auxiliares de competições, resultados e classificações;
- controles financeiros simples ligados à rotina da equipe.

### Não constituem requisitos fechados

- gamificação;
- rankings;
- pontuações de disciplina;
- geração automática de materiais públicos;
- automação de substituições.

Esses itens não são decisões abertas da primeira entrega; permanecem sem requisito confirmado.

---

## 7. Stakeholders

| ID | Stakeholder | Interesse | Poder de decisão | Necessidades ainda desconhecidas |
|---|---|---|---|---|
| STK-001 | Treinador/Administrador do CEPRAEA | Reduzir carga operacional; operar agenda; acompanhar disponibilidade e quórum; consolidar fatos; tomar decisões esportivas | Alto — autoridade de produto e autoridade esportiva no contexto declarado | Detalhes técnicos de operação e implementação ainda dependem das fases posteriores |
| STK-002 | Atletas do CEPRAEA | Consultar agenda e próxima ação; declarar disponibilidade; informar ocorrências; acessar dados próprios e informações coletivas necessárias | Poder de decisão de produto não formalizado; possuem autoridade sobre suas próprias declarações dentro das regras | Adoção real, fricção aceitável e necessidades adicionais devem ser validadas em uso |

**Fato atual do elenco:** treinador + 19 atletas. Esse número descreve a equipe atual e não limita mudanças legítimas no elenco.

---

## 8. Restrições iniciais

| ID | Restrição | Origem | Impacto | Confirmada? |
|---|---|---|---|---|
| CONST-001 | Desenvolvimento e manutenção sob responsabilidade de uma única pessoa sem experiência prévia de programação | Q-006 | [não formalizado] | Sim |
| CONST-002 | Desenvolvimento intensivamente assistido por agentes de IA; acesso aos modelos de desenvolvimento por assinaturas mensais previsíveis, sem depender de cobrança variável de API por tokens | Q-006 | [não formalizado] | Sim |
| CONST-003 | Custo operacional recorrente em torno de R$ 50/mês; custo próximo de R$ 200/mês é incompatível | Q-006 | [não formalizado] | Sim |
| CONST-004 | Primeira versão definida para entrega até 2026-09-07 | Q-006 | [não formalizado] | Sim |
| CONST-005 | Aproximadamente 42 horas disponíveis para a primeira etapa | Q-006 | [não formalizado] | Sim |
| CONST-006 | Primeira versão entregue como PWA | Q-007 | [não formalizado] | Sim |
| CONST-007 | Uso cotidiano predominantemente em smartphones; produto mobile first, leve e legível | Q-006/Q-007 | [não formalizado] | Sim |
| CONST-008 | Primeira entrega não depende de publicação em lojas nativas | Q-006/Q-007 | [não formalizado] | Sim |
| CONST-009 | Após o lançamento, a capacidade de operação, manutenção e suporte técnico contínuo é muito baixa | Q-006 | [não formalizado] | Sim |
| CONST-010 | Contexto real inclui conectividade móvel instável; a estratégia técnica de offline/sincronização permanece não decidida | Q-006 | [não formalizado] | Sim quanto ao contexto; mecanismo técnico não decidido |
| CONST-011 | Escopo da primeira entrega deve permanecer proporcional ao prazo, esforço, orçamento e equipe atuais | Q-006 | [não formalizado] | Sim |

### Consequências que **não** constituem decisões técnicas fechadas

As restrições acima favorecem baixo custo, baixa manutenção, pouco suporte operacional e tolerância razoável a conectividade instável, mas não fecham provedor, banco, hospedagem, serverless, autenticação, login social, magic link, offline, sincronização, notificações, schemas, serviços, APIs ou módulos.

---

## 9. Premissas iniciais

| ID | Hipótese | Evidência | Impacto se falsa | Status |
|---|---|---|---|---|
| HYP-001 | As atletas utilizarão diretamente o produto para declarações e ocorrências com fricção suficientemente baixa para reduzir a intermediação do treinador | Intenção de produto e critério de sucesso; ainda sem dados reais de adoção | Alto: baixa adoção mantém treinador e WhatsApp como intermediários | aceita explicitamente como risco do piloto; medir adoção e fricção em uso real |
| HYP-002 | O escopo definido para a primeira entrega é tecnicamente realizável dentro de aproximadamente 42 horas com desenvolvimento solo assistido por IA | Restrições de prazo/esforço; nenhuma execução ou auditoria técnica concluída | Alto: atraso ou redução da primeira entrega | aceita explicitamente como risco do piloto; manter escopo obrigatório reduzido e não incorporar `FUTURE` |
| HYP-003 | A operação por exceção e o indicador de zero ações administrativas semanais resultarão em redução material de horas administrativas no uso real | Relação causal esperada pelo produto; `Historico.json` preserva faixas numéricas anteriores como evidência histórica, sem baseline ou meta vigente; Q-009 v2.10 exige medição real futura | Alto: o produto pode funcionar sem devolver tempo material ao treinador | aceita explicitamente como risco do piloto; medir ações e horas reais após o uso |

---

## 10. Riscos iniciais

| ID | Risco | Probabilidade | Impacto | Mitigação inicial / tratamento atual |
|---|---|---|---|---|
| RISK-001 | Escopo da primeira entrega exceder as ~42 horas disponíveis | [não formalizada] | [não formalizado] | Manter separação rígida entre primeira entrega e `FUTURE`; não incorporar novas capacidades silenciosamente |
| RISK-002 | O produto apenas digitalizar a burocracia existente | [não formalizada] | [não formalizado] | Critério de sucesso exige zero ações administrativas semanais obrigatórias no fluxo normal |
| RISK-003 | Baixa adoção das atletas manter o treinador como intermediário e o WhatsApp como infraestrutura | [não formalizada] | [não formalizado] | Validar adoção e fricção no uso real; não assumir sucesso apenas por funcionamento técnico |
| RISK-004 | Custos recorrentes crescerem além do orçamento sustentável | [não formalizada] | [não formalizado] | Avaliar decisões técnicas futuras contra CONST-003; nenhuma escolha de provedor foi fechada |
| RISK-005 | Solução exigir manutenção/suporte incompatíveis com a disponibilidade do treinador | [não formalizada] | [não formalizado] | Avaliar decisões técnicas futuras contra CONST-001 e CONST-009 |
| RISK-006 | Conectividade instável prejudicar fluxos essenciais na praia | [não formalizada] | [não formalizado] | Contexto registrado; estratégia técnica permanece para fase posterior |
| RISK-007 | Falhas de integridade histórica misturarem declaração, presença, participação ou retificação | [não formalizada] | [não formalizado] | Regras de não sobrescrita e retificação auditável já confirmadas no entendimento |
| RISK-008 | Automação/projeção ser confundida com decisão esportiva humana | [não formalizada] | [não formalizado] | Preservar autoridade humana e diferenciar projeções, fatos e decisões |
| RISK-009 | Alertas excessivos reduzirem atenção ao canal | [não formalizada] | [não formalizado] | Evidência de fracasso explicitada; desenho de notificações permanece decisão posterior |
| RISK-010 | Exposição indevida de informações individuais das atletas | [não formalizada] | [não formalizado] | Privacidade individual confirmada como necessidade; mecanismo técnico ainda não decidido |

---

## 11. Decisões já tomadas

| ID | Decisão | Autoridade | Motivo | Reversibilidade |
|---|---|---|---|---|
| DEC-001 | A primeira versão será entregue como PWA | Usuário | Prazo, custo, distribuição, desenvolvimento solo e uso móvel | Reavaliação futura permitida se necessidades, orçamento ou capacidade mudarem; classificação de reversibilidade não formalizada |
| DEC-002 | Primeira entrega e visão completa possuem escopos distintos; capacidades listadas como `FUTURE` não entram implicitamente no MVP | Usuário | Controlar escopo e preservar viabilidade da primeira entrega | Capacidades futuras podem ser descobertas/decididas depois; classificação de reversibilidade não formalizada |
| DEC-003 | Decisões esportivas e humanas permanecem sob autoridade do treinador | Usuário | Automação deve apoiar, não substituir julgamento humano | [classificação de reversibilidade não formalizada] |
| DEC-004 | No horizonte inicial existem dois papéis autenticados: `TREINADOR_ADMINISTRADOR` e `ATLETA` | Usuário | Reflete os usuários reais atuais e evita complexidade hipotética | Pode ser revista quando novos papéis existirem na operação real; classificação não formalizada |
| DEC-005 | D-5 é exatamente `início_da_sessão − 120 horas`; em D-5 quórum suficiente confirma automaticamente e quórum insuficiente cancela automaticamente por `FALTA_DE_QUÓRUM` | Usuário | Operação semanal por exceção e sem ação administrativa normal do treinador | [classificação de reversibilidade não formalizada] |
| DEC-006 | Uma sessão já confirmada nunca é cancelada automaticamente por perda posterior de quórum; cancelamento posterior exige decisão explícita do treinador | Usuário | Preservar compromisso assumido e autoridade sobre exceções reais | [classificação de reversibilidade não formalizada] |
| DEC-007 | Presença ou participação consolidada só pode ser corrigida por retificação auditável realizada pelo treinador/administrador; se necessário, os dois eixos são corrigidos juntos | Usuário | Preservar realidade factual, combinações válidas, autoria e histórico | [classificação de reversibilidade não formalizada] |
| DEC-008 | O sistema gera proposta mensal de agenda; o treinador revisa por exceção e publica | Usuário | Reduzir criação e acompanhamento manual recorrente | [classificação de reversibilidade não formalizada] |
| DEC-009 | Toda sessão publicada com D-5 futuro segue a mesma resolução automática, inclusive sessão excepcional | Usuário | Eliminar ambiguidade e manter um único fluxo normal | [classificação de reversibilidade não formalizada] |
| DEC-010 | Participantes convidadas não são cadastradas, representadas nem contadas no quórum | Usuário | Evitar burocracia sem valor; diante de exceção, basta o treinador manter ou cancelar | [classificação de reversibilidade não formalizada] |
| DEC-011 | Depois de D-5, `NÃO PODEREI COMPARECER` retira e `AGORA POSSO PARTICIPAR` inclui imediatamente a atleta no cálculo atual | Usuário | Fechar o efeito operacional de ocorrências positivas e negativas | [classificação de reversibilidade não formalizada] |
| DEC-012 | Uma sessão cancelada é terminal e não pode ser reativada | Usuário | Evitar estados ambíguos e comunicação contraditória | [classificação de reversibilidade não formalizada] |
| DEC-013 | Alterar data ou horário de sessão publicada exige `REMARCAR TREINO`: cancelar a original e criar outra sem disponibilidades anteriores | Usuário | Preservar histórico e solicitar compromisso para a data correta | [classificação de reversibilidade não formalizada] |
| DEC-014 | Nova sessão com D-5 já transcorrido exige `CONFIRMAR SESSÃO EXCEPCIONAL` explícito do treinador | Usuário | Não simular um checkpoint automático que não ocorreu | [classificação de reversibilidade não formalizada] |
| DEC-015 | Depois da confirmação existe somente `QUÓRUM_COMPROMETIDO`; o déficit exato é diagnóstico, e o treinador escolhe somente `MANTER TREINO` ou `CANCELAR TREINO` | Usuário | Reduzir classificações e decisões burocráticas | [classificação de reversibilidade não formalizada] |
| DEC-016 | HYP-001, HYP-002 e HYP-003 são aceitas explicitamente como riscos do piloto até validação empírica | Usuário | Permitir encerramento da elicitação sem promover hipóteses a fatos | Reavaliar com dados do piloto |
| DEC-017 | A proposta mensal inclui sessões normais e sessões possíveis nos feriados nacionais e feriados oficiais estaduais ou municipais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 | Usuário | Entregar uma agenda mensal pronta para revisão, incluindo oportunidades de treino em feriados | Revisável por nova decisão explícita de produto |

---

## 12. Questões abertas

### Questões de produto abertas conhecidas

`NONE` — `OPEN-001` foi fechado por `DEC-017`.

Nenhuma questão material de produto atualmente conhecida permanece aberta neste escopo. Se uma fase posterior revelar uma lacuna que não possa ser resolvida sem criar nova intenção ou regra de produto, ela deve retornar à elicitação e à autoridade humana.

### Questões técnicas/arquiteturais explicitamente não decididas

| ID | Questão | Impacto | Incerteza | Bloqueia próxima fase? |
|---|---|---|---|---|
| OPEN-TECH-002 | Qual provedor/estrutura de persistência, hospedagem e execução atende custo e manutenção? | [não formalizado] | [não formalizada] | Não é decisão de produto; tratar somente após Gate B e drivers |
| OPEN-TECH-003 | Qual mecanismo de autenticação satisfaz privacidade e baixa carga de suporte? | [não formalizado] | [não formalizada] | Não é decisão de produto; tratar somente após Gate B e drivers |
| OPEN-TECH-004 | Qual estratégia de conectividade/offline/sincronização é necessária e proporcional? | [não formalizado] | [não formalizada] | Não é decisão de produto; tratar somente após Gate B e drivers |
| OPEN-TECH-005 | Como implementar lembretes, comunicações e alertas sem assumir tecnologia de notificação prematuramente? | [não formalizado] | [não formalizada] | Não é decisão de produto; tratar posteriormente |

### Pendências de processo

```text
GATE-B-KNOWLEDGE = READY_WITH_RISKS
GATE-B-CANONICALIZATION = APPROVED
GATE-B-INDEPENDENT-AUDIT = PASS_WITH_RISKS
ELICITATION-OPEN = NONE
GATE-B-DOMAIN-MODEL = PASS
GATE-B-FINAL = APPROVED
```

`Chat 04 — Requirements = AUTHORIZED`. Drivers, Alternatives/Options, ADRs e Architecture permanecem `NOT_YET_AUTHORIZED`.

---

## 13. Formulações históricas substituídas (`SUPERSEDED`)

| ID | Formulação substituída | Decisão vigente |
|---|---|---|
| SUPERSEDED-001 | Fechamento às 20h da véspera, 24 horas antes ou em horário genérico de D-5 | D-5 = `início_da_sessão − 120 horas` |
| SUPERSEDED-002 | Wellness Pré + Pós determina presença | Wellness é evidência futura; treinador consolida presença e participação |
| SUPERSEDED-003 | Treinador cria todos os treinos | Sistema gera proposta mensal; treinador revisa por exceção |
| SUPERSEDED-004 | Mínimo operacional `1G + 3D + 4A` | Oito atletas distintas: 4 Ataque + 4 Defesa, com ≥1 Goleira na Defesa |
| SUPERSEDED-005 | Atacante, Defensora e Goleira bastam como modelo | Taxonomia `Fase → Sistema → Posição` |
| SUPERSEDED-006 | Resposta antecipada pode ser presença factual | Disponibilidade, presença e participação são fatos distintos |
| SUPERSEDED-007 | Número bruto de baixas ou uma classe separada de falha crítica define a exceção | Toda composição inválida pós-confirmação produz `QUÓRUM_COMPROMETIDO`; o déficit exato aparece como diagnóstico |
| SUPERSEDED-008 | Produto completo e MVP possuem o mesmo escopo | Primeira entrega separada das capacidades `FUTURE` |
| SUPERSEDED-009 | Quórum garantido antes de D-5 permite confirmação antecipada manual | Antes de D-5 apenas `QUÓRUM_GARANTIDO`; confirmação normal ocorre no fechamento |
| SUPERSEDED-010 | Quórum insuficiente em D-5 exige decisão do treinador | Em D-5 produz `CANCELADO — FALTA_DE_QUÓRUM` automaticamente |
| SUPERSEDED-011 | Apenas quinta-feira recorrente recebe ajuste de feriado | A proposta mensal inclui sessões possíveis nos feriados nacionais e oficiais aplicáveis à cidade do Rio de Janeiro, sugeridas para 07h30–09h00 |
| SUPERSEDED-012 | Faixas estimadas de horas são o principal critério do MVP | Critério principal = zero ações administrativas obrigatórias no fluxo semanal normal; as faixas de `Historico.json` permanecem somente como evidência histórica secundária de SUCCESS-005, sem baseline ou meta vigente |
| SUPERSEDED-013 | Presença consolidada não possuía mecanismo fechado de correção | Retificação auditável, sem sobrescrita, somente pelo treinador/administrador |
| SUPERSEDED-014 | Participante convidada precisava ser cadastrada com posição válida para contar no quórum | Participante convidada não faz parte do produto nem do cálculo; o treinador apenas mantém ou cancela diante de quórum comprometido |
| SUPERSEDED-015 | Data ou horário de sessão publicada podiam ser substituídos por edição | `REMARCAR TREINO` cancela a original e cria outra sessão, sem transportar disponibilidades |

---

## 14. Critério para sair do Charter

O Charter está suficientemente maduro para iniciar elicitação profunda quando:

- [x] problema principal está compreendido;
- [x] objetivos iniciais foram explicitados;
- [x] principais stakeholders foram identificados;
- [x] não objetivos iniciais foram registrados;
- [x] restrições críticas conhecidas foram registradas;
- [x] hipóteses perigosas foram explicitadas;
- [x] questões desconhecidas estão visíveis, não escondidas.

**Avaliação:** o conhecimento de intenção ultrapassou o Gate A, foi aprofundado por Q-001–Q-013, a modelagem do domínio foi validada com `PASS` e `GATE-B-FINAL = APPROVED`. `Chat 04 — Requirements` está autorizado. Drivers, Alternatives/Options, ADRs e Architecture permanecem não autorizados.
