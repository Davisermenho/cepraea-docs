ESPECIFICAÇÃO DE EXPERIÊNCIA E INTERAÇÃO — CEPRAEA BEACH PRO

AESDS 02 — Fundação v0.1

1. OBJETIVO

Transformar regras e estados do domínio em tarefas, fluxos, interações, representações visuais e componentes mobile sem alterar o significado original.

2. FLUXO CANÔNICO DE PROJETO

REALIDADE ESPORTIVA -> MODELO CANÔNICO -> ATOR + OBJETIVO/TAREFA -> ESTADO DO DOMÍNIO -> PERMISSÃO + TEMPORALIDADE -> ESTADOS E TRANSIÇÕES DE INTERAÇÃO -> EDGE CASES -> USER FLOW -> INTERACTION DESIGN -> UI -> COMPONENTES -> IMPLEMENTAÇÃO -> TESTES -> RUNTIME.

Este é o único fluxo normativo desta especificação. Resumos ou diagramas futuros devem derivar dele.

3. TAXONOMIA DE ESTADO

DOMAIN STATE: fato de negócio ou estado canônico, por exemplo NÃO_RESPONDIDA, SIM, NÃO, INCERTA, VÍNCULO_ATIVO, PRESENÇA_REGISTRADA.

INTERACTION STATE: estado temporário da ação humana, por exemplo EDITING, DIRTY, SUBMITTING, CONFIRMING, RETRYING.

VIEW/DELIVERY STATE: condição de entrega da interface, por exemplo LOADING, EMPTY, ERROR, UNAVAILABLE, STALE.

O agente não deve misturar categorias. Loading não é estado de domínio; não respondida não é apenas aparência.

4. ESPECIFICAÇÃO MÍNIMA DE CADA FLUXO

- ator;

- objetivo;

- entry point;

- pré-condições;

- estado inicial;

- caminho principal;

- caminhos alternativos;

- ações permitidas;

- ações proibidas;

- estados de interação;

- estados de erro;

- expiração/temporalidade;

- autorização;

- recuperação;

- próxima ação;

- critérios de aceitação.

5. STATE-FIRST DESIGN

Nenhuma tela relevante deve ser desenhada antes de os estados e transições estarem identificados. A tela é uma projeção do estado, não a fonte da regra.

6. INFORMATION ARCHITECTURE

A navegação deve refletir tarefas da atleta e do treinador, não tabelas do banco. Entidade técnica não vira item de menu automaticamente. O agente deve justificar novos níveis de navegação por tarefa observável.

7. INTERACTION DESIGN

Toda ação relevante deve declarar: início, feedback imediato, pendência, sucesso, falha, retry, cancelamento quando aplicável e impacto da perda de conectividade. O usuário nunca deve ficar sem saber se a operação foi concluída.

8. MOBILE-FIRST REAL

Projetar e validar para:

- uso com uma mão;

- tela pequena;

- teclado virtual;

- viewport e safe areas;

- alvo de toque adequado;

- luz intensa;

- rede móvel instável;

- latência;

- retorno da conectividade;

- toque acidental;

- orientação e scroll.

9. ACESSIBILIDADE

Semântica HTML, foco, labels, nomes acessíveis, contraste, feedback textual/semântico e uso por toque devem nascer com o componente. O nível formal de conformidade WCAG permanece DECISÃO HUMANA PENDENTE até homologação explícita.

10. DESIGN SYSTEM

O Design System cresce de padrões validados em fluxos reais. Ordem: tokens -> primitivos -> componentes reutilizáveis -> componentes semânticos de domínio -> padrões de composição.

Não criar biblioteca extensa antes do primeiro vertical slice validado. Não abstrair diferenças semânticas apenas porque a aparência é semelhante.

11. COMPONENTES SEMÂNTICOS

Preferir interfaces que recebem conceitos do domínio, por exemplo AvailabilityStatus(status), em vez de componentes cuja semântica depende apenas de cor ou prop visual.

12. OPTIMISTIC UI

Só usar quando a ação for reversível, reconciliável e o estado pendente permanecer explícito. Fatos de alta integridade não devem ser apresentados como persistidos antes da confirmação autoritativa.

13. DECISÕES DE DESIGN

Antes de escolher silenciosamente padrão de navegação, direção visual, família tipográfica, paleta, iconografia, motion, biblioteca de componentes ou padrão de layout materialmente diferente, o agente deve pesquisar opções e apresentar referências para decisão humana.

14. USABILIDADE

Validação técnica em dispositivo não substitui validação humana de compreensão. Fluxos críticos devem possuir cenário de teste de usabilidade: tarefa, sucesso esperado, erro provável, entendimento do estado e entendimento da próxima ação.

15. FONTES EXISTENTES

O documento “Modelagem de Domínio — Frontend CEPRAEA BEACH PRO” é fonte de conteúdo anterior desta área. Ao migrar decisões para esta especificação, eliminar duplicações e preservar somente uma formulação normativa.

16. DONE DE UM FLUXO DE UX/UI

Um fluxo só está pronto para implementação quando: estados conhecidos; transições conhecidas; permissões conhecidas; edge cases relevantes registrados; decisões visuais materiais homologadas; erros e recuperação definidos; critérios de aceitação observáveis existentes.

17. BASELINE DE FLUXOS MVP — PLANOS / SPECS

Esta seção instancia o contrato de experiência para os fluxos centrais já suportados por decisões canônicas. Ela não fixa navegação, direção visual ou detalhes ainda OPEN.

17.1. FLUXO F-MVP-01 — IDENTIDADE E VÍNCULO

Ator: atleta e treinador, conforme permissão.

Objetivo: representar a atleta correta e seu vínculo vigente com a equipe sem confundir domínio com autenticação.

Pré-condições: atleta identificada no domínio; eventual identidade de autenticação é mecanismo de acesso, não identidade esportiva.

Estado inicial: atleta conhecida/desconhecida e vínculo vigente/ausente/encerrado conforme fonte canônica.

Caminho principal: carregar atleta -> resolver vínculo aplicável ao contexto -> apresentar somente informações e ações autorizadas.

Ações proibidas: inferir vínculo apenas porque existe auth.user; tratar cadastro como vínculo ativo; expor identificador técnico sem requisito.

Erros/recuperação: ausência ou inconsistência de vínculo deve produzir estado explícito e não ser corrigida por invenção no frontend.

Próxima ação: seguir para tarefa operacional compatível com vínculo e autorização.

17.2. FLUXO F-MVP-02 — SESSÃO/TREINO

Ator: atleta e treinador, com capacidades distintas.

Objetivo: representar treino/sessão e distinguir planejamento de realização.

Pré-condições: sessão identificável e contexto temporal conhecido.

Estados de domínio mínimos: planejado e realizado devem permanecer semanticamente distinguíveis; outros estados somente quando definidos pela fonte canônica aplicável.

Caminho principal: localizar sessão -> apresentar estado/tempo relevantes -> expor a ação operacional permitida para o ator.

Ações proibidas: converter sessão planejada em realizada apenas por passagem de tempo; inventar realização para habilitar presença factual.

Erros/recuperação: estado temporal inconsistente ou fonte ausente deve permanecer explícito.

17.3. FLUXO F-MVP-03 — DISPONIBILIDADE DA ATLETA

Ator: atleta responde a própria disponibilidade; treinador consulta conforme autorização.

Objetivo: registrar e representar resposta de disponibilidade sem transformá-la em compromisso ou presença.

Estados de domínio: NÃO_RESPONDIDA, SIM, NÃO, INCERTA, ou equivalentes canônicos vigentes.

Estado inicial: resposta corrente derivada do histórico válido; ausência de resposta = NÃO_RESPONDIDA.

Caminho principal: abrir solicitação aplicável -> mostrar estado corrente -> atleta escolhe uma opção permitida -> interação entra em pendência explícita -> sucesso somente após confirmação autoritativa -> estado corrente é atualizado sem perder histórico.

Ações proibidas: tratar NÃO_RESPONDIDA como NÃO; editar resposta de outra atleta; inferir presença; mostrar gravação como concluída antes da confirmação.

Erros/recuperação: falha preserva a intenção/entrada quando seguro e permite retry sem afirmar persistência inexistente.

DECIDED-AVAIL-01 / DEC-DATA-046: cada solicitação de disponibilidade possui `deadline_at` explícito e não existe prazo global implícito. Enquanto a coleta estiver aberta e antes do deadline, a atleta pode criar ou alterar somente a própria declaração; cada alteração confirmada preserva histórico/versão e a última versão válida torna-se corrente. No deadline, a janela normal de self-service fecha: NÃO_RESPONDIDA permanece NÃO_RESPONDIDA e a última declaração válida continua corrente, sem receber semântica de “expirada”. Antes do início da sessão, ator autorizado pode reabrir explicitamente a coleta e alterar o prazo de modo auditável; após o início da sessão não há reabertura normal. A UI deve mostrar o prazo absoluto no contexto America/Sao_Paulo e, após o fechamento, indicar claramente “prazo encerrado” junto da resposta corrente ou “não respondida”. Retificações posteriores, quando autorizadas, permanecem históricas/auditáveis e não criam presença factual por inferência.

17.4. FLUXO F-MVP-04 — COBERTURA E PARTICIPAÇÃO PLANEJADA

Ator: treinador consulta cobertura e conduz planejamento; atleta pode consultar apenas o que sua autorização permitir.

Objetivo: derivar visão de cobertura a partir de respostas vigentes e representar participação planejada sem confundi-la com presença factual.

Pré-condições: sessão existente e respostas vigentes disponíveis.

Caminho principal: carregar sessão + respostas vigentes -> derivar cobertura -> produzir/consultar representação planejada conforme contrato aprovado.

Invariantes: derivação não é fato; lista prevista não é presença; mudança em resposta vigente pode alterar derivação sem reescrever história.

Ações proibidas: registrar presença factual a partir da lista; tratar lista prevista como confirmação da atleta; esconder incerteza relevante.

DECIDED-PLAN-01 / DEC-DATA-047: o Plano de Participação da Sessão é PLANO prospectivo humano e versionado; “lista prevista” é a projeção operacional da versão PUBLISHED vigente. Lifecycle: DRAFT -> PUBLISHED -> SUPERSEDED | CANCELLED | CLOSED, com no máximo uma PUBLISHED vigente por sessão. DRAFT não é lista decidida para consumo da atleta. PUBLISHED é imutável; revisão material cria nova versão e sua publicação supersede atomicamente a anterior, preservando histórico. `SOURCE_ALIGNMENT = CONSISTENT | REVIEW_REQUIRED` é condição ortogonal ao lifecycle e não se confunde com STALE de entrega/view. Mudança material de inputs pode recomputar cobertura e deve produzir REVIEW_REQUIRED sem reescrever automaticamente a composição humana. Se o treinador revisar e mantiver a mesma composição após mudança material, deve existir nova versão publicada para atualizar decisão/proveniência. CANCELLED exige evento autoritativo explícito; CLOSED exige marco autoritativo da sessão e não decorre da passagem do relógio isoladamente. Publicação torna a versão vigente; comunicação/notificação é evento separado. Nenhuma transição cria disponibilidade, compromisso da atleta ou presença factual.

17.5. FLUXO F-MVP-05 — PRESENÇA FACTUAL

Ator: treinador ou outra autoridade explicitamente autorizada pela fonte canônica.

Objetivo: registrar fato de participação realizado sem promovê-lo a partir de disponibilidade, lista prevista ou Wellness.

Pré-condições: sessão realizada identificada; atleta identificada; autoridade de escrita válida.

Estados/fatos: presença factual pode distinguir participação FULL/PARTIAL/NONE quando essa classificação estiver definida pela fonte canônica; ausência de registro permanece NÃO_APURADO/sem fato, nunca ausência automática.

Caminho principal: abrir sessão realizada -> selecionar atleta -> consultar contexto permitido -> confirmar fato de presença explicitamente -> persistir pela camada autoritativa -> refletir confirmação.

Wellness: quando autorizado, pode originar somente proposta derivada/transitória de presença; a proposta não é fato e exige confirmação autorizada.

Correção: correções de presença factual devem preservar auditabilidade/proveniência; não substituir silenciosamente o fato anterior sem mecanismo canônico.

Ações proibidas: inferir presença por disponibilidade; inferir ausência por falta de Wellness ou falta de registro; permitir confirmação factual sem autorização.

17.6. FLUXO F-MVP-06 — WORKSPACES OPERACIONAIS

Ator atleta: visualizar estado próprio, pendências, sessões relevantes e próxima ação permitida.

Ator treinador: visualizar estado consolidado necessário à operação, distinguindo fato, planejamento, derivação e pendência.

Fonte: somente informações produzidas pelos fluxos e contratos anteriores; não inventar dados para preencher dashboard/workspace.

Estado de entrega: LOADING/EMPTY/ERROR/UNAVAILABLE/STALE devem ser distinguíveis dos estados de domínio.

OPEN-UX-01: arquitetura da informação e padrão material de navegação permanecem OPEN. Portanto, a organização final de rotas/menu não é decidida por esta seção.

OPEN-VIS-01 e OPEN-A11Y-01: direção visual e nível formal WCAG permanecem OPEN; semântica, foco, labels, contraste e feedback não dependente apenas de cor continuam obrigatórios independentemente dessas decisões.

17.7. REGRA DE PRONTIDÃO DOS FLUXOS

Um fluxo desta baseline pode avançar para especificação executável somente quando suas decisões materiais aplicáveis estiverem DECIDED e entradas, saídas, permissões, erros, edge cases, critérios de aceitação e expectativas de teste estiverem suficientemente determinadas. DECIDED-AVAIL-01/DEC-DATA-046 removeu o blocker temporal específico do F-MVP-03 e DECIDED-PLAN-01/DEC-DATA-047 removeu o blocker semântico/lifecycle específico do F-MVP-04. OPEN-UX-01, OPEN-VIS-01 e OPEN-A11Y-01 continuam bloqueando apenas as unidades que dependem materialmente dessas decisões; grounding do repositório e contratos executáveis permanecem requisitos independentes.