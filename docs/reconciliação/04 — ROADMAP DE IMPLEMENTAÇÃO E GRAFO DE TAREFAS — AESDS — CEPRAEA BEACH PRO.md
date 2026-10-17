ROADMAP DE IMPLEMENTAÇÃO E GRAFO DE TAREFAS — CEPRAEA BEACH PRO

AESDS 04 — Fundação v0.1

1. OBJETIVO

Impedir que os agentes executem tarefas na ordem errada, construam abstrações antes de existir evidência de uso ou produzam retrabalho por dependências não resolvidas.

2. REGRA DE PLANEJAMENTO

O projeto é desenvolvido por vertical slices. Cada fase possui entradas, decisões humanas, tarefas, evidências e condição de saída. Uma fase pode avançar parcialmente quando as dependências da slice estiverem satisfeitas; não existe obrigação de concluir todo um tipo de artefato antes de entregar valor vertical.

3. ROADMAP MACRO

F0 — Inventário e autoridade

Confirmar fontes canônicas, estado do repo, stack real, escopo e decisões já homologadas.

F1 — Fundação da experiência

Atores, tarefas principais, linguagem, princípios mobile, arquitetura da informação inicial e decisões de navegação.

F2 — Fundação técnica

App shell, routing, contratos-base, integração de desenvolvimento, tratamento global de erro/conectividade e checks de aplicação.

F3 — Primeiro vertical slice

Escolher fluxo simples, relevante e representativo. Implementar domínio/contrato -> dados -> estados -> UX -> UI -> testes -> mobile. Validar o padrão antes de generalizar.

F4 — Design foundations

Extrair tokens e primitivos comprovados pela primeira slice. Homologar tipografia, cor, espaçamento, iconografia e padrões globais com referências.

F5 — Fluxos de atleta

Construir slices de atleta em ordem de dependência, preservando autorização e estados temporais.

F6 — Fluxos de treinador

Construir slices de treinador em ordem de dependência, reutilizando somente padrões já comprovados.

F7 — Estado operacional consolidado

Criar a visão operacional apenas a partir de fluxos/dados já existentes. Não inventar dados para preencher dashboard.

F8 — Resiliência transversal

Erros, stale state, conectividade, retry, concorrência, expiração, dupla submissão, autorização e recuperação.

F9 — Acessibilidade e usabilidade

Auditoria técnica + cenários humanos críticos. Corrigir bloqueadores antes do polimento final.

F10 — Performance

Medir, identificar gargalos, otimizar apenas onde a evidência justificar.

F11 — PWA e comportamento de instalação/atualização

Implementar somente capacidades PWA autorizadas; validar manifest, service worker e comportamento real.

F12 — Hardening e conclusão

Regression suite, validação mobile, verificação de critérios, findings residuais, documentação mínima e handoff de estado.

4. DEPENDÊNCIAS LÓGICAS INICIAIS DO MVP

ATLETA_BASE -> VÍNCULO

TREINO_BASE -> SOLICITAÇÃO_DISPONIBILIDADE

ATLETA_BASE + TREINO_BASE + SOLICITAÇÃO_DISPONIBILIDADE -> RESPOSTA_ATLETA

RESPOSTAS_VIGENTES -> COBERTURA_TREINO

TREINO_BASE + RESPOSTAS -> LISTA_PREVISTA

TREINO_REALIZADO + ATLETA_BASE -> PRESENÇA_REAL

ELENCO + TREINOS + RESPOSTAS + LISTA_VIGENTE + PRESENÇA -> VISÃO_OPERACIONAL

5. GRAFO DE TAREFAS

Cada tarefa recebe:

ID; fase; dependências; status READY/BLOCKED/IN_PROGRESS/REVIEW/DONE; ator; saída; critérios; risco; decisão humana pendente; evidência.

Git/GitHub permanece fonte de estado. Este documento define regras do grafo, não mantém uma state machine paralela.

6. REGRAS CONTRA RETRABALHO

- não criar Design System completo antes de padrões reais;

- não implementar dashboard antes das fontes de dados;

- não otimizar antes de medir;

- não adicionar biblioteca por antecipação;

- não implementar telas em massa antes de validar a primeira slice;

- não criar comportamento offline inexistente;

- não escrever tarefa dependente de decisão humana não resolvida;

- não duplicar contrato para facilitar frontend.

7. ORDEM DE EXECUÇÃO DE UMA SLICE

1. confirmar dependências READY;

2. carregar contexto mínimo;

3. resolver decisões humanas materiais;

4. modelar estados/transições;

5. definir critérios;

6. implementar contrato/dados necessários;

7. implementar interação/UI;

8. cobrir erros/edge cases previstos;

9. executar checks;

10. review independente;

11. correção de findings;

12. validar runtime mobile quando aplicável;

13. marcar DONE no sistema oficial de tarefas.

8. CRITÉRIO READY

Uma tarefa só está READY se: objetivo e ator claros; dependências DONE; entradas disponíveis; decisão material não bloqueada; write scope previsível; critérios de aceitação definidos; fonte normativa identificada.

9. CRITÉRIO BLOCKED

Marcar BLOCKED quando uma dependência, decisão humana, fonte normativa, ambiente ou contrato obrigatório não estiver disponível. Não substituir bloqueio por inferência.

10. CRITÉRIO DONE

100% dos MUST/CRITICAL PASS; nenhum CRITICAL/HIGH aberto; checks exigidos executados; evidência suficiente; escopo não expandido silenciosamente; reviewer concluiu; estado oficial atualizado.

11. PRÓXIMO PASSO PARA ESTE DOCUMENTO

Derivar o grafo completo de tarefas do frontend a partir dos fluxos MVP, do Modelo Canônico, das decisões de design e do estado real do repositório. A decomposição deve ocorrer antes da execução em massa.

12. GRAFO MVP DERIVADO DO MAPA DE ENTREGÁVEIS — PLANOS / SPECS

Esta seção substitui a necessidade de criar um roadmap separado por deliverable. O grafo abaixo governa dependências entre capacidades; tarefas concretas continuam pertencendo ao sistema oficial Git/GitHub quando o repositório for groundado.

12.1. DEPENDÊNCIAS ENTRE ENTREGÁVEIS

DEL-02 Athlete & Team Identity Capability -> DEL-03 Session Operations Capability e DEL-09 Authorization, Privacy, Provenance & Audit Layer.

DEL-03 -> DEL-04 Availability Request & Response Flow.

DEL-04 -> DEL-05 Training Coverage & Planned Participation Capability.

DEL-02 + DEL-03 -> DEL-06 Factual Attendance Capability.

DEL-02 + DEL-03 + DEL-04 + DEL-05 + DEL-06 -> DEL-07 Athlete Operational Workspace e DEL-08 Coach Operational Workspace.

DEL-01 PWA Operational Shell suporta DEL-07 e DEL-08 e deve evoluir somente na medida exigida pelas slices reais.

DEL-12 Validated Design Foundations & Semantic Component System emerge dos primeiros fluxos validados; não precede artificialmente as slices.

DEL-10 Canonical Operational Persistence & Contract Surface suporta as slices finais, mas execução física permanece bloqueada por BLOCKED-DATA-01.

DEL-10 + fontes legadas -> DEL-11 Legacy Migration & Domain Cutover.

DEL-13 Automated & Runtime Verification Suite verifica todos os entregáveis e cresce junto com as slices, não apenas no final.

12.2. ORDEM DE ESPECIFICAÇÃO

S0 — consolidar contrato de produto/domínio e requisitos rastreáveis no AESDS 01.

S1 — especificar fluxos e estados centrais no AESDS 02: identidade/vínculo, sessão, disponibilidade, cobertura/planejamento, presença factual e workspaces.

S2 — definir fronteiras lógicas de contratos no AESDS 03 sem antecipar física bloqueada.

S3 — fechar decisões materiais que bloqueiam unidades específicas: DECIDED-AVAIL-01 está ratificada por DEC-DATA-046 e DECIDED-PLAN-01 está ratificada por DEC-DATA-047/SGATE-0025; permanecem OPEN-UX-01, OPEN-VIS-01 e OPEN-A11Y-01 para as unidades que dependem delas.

S4 — somente após grounding do repo, instanciar tasks executáveis conforme AESDS 05 e contratos concretos compatíveis com AESDS 03.

S5 — ligar cada critério obrigatório à prova no AESDS 06 e executar no ambiente autorizado.

12.3. READINESS POR UNIDADE

DEL-02: especificação semântica pode avançar; execução ainda depende de grounding do repo/contratos executáveis.

DEL-03: especificação semântica pode avançar; execução ainda depende de grounding do repo.

DEL-04: DECIDED quanto à política temporal de disponibilidade por DEC-DATA-046; a especificação de prazo/fechamento/editabilidade/reabertura pode avançar. Isso não declara execução READY: grounding do repositório, contratos executáveis, critérios e qualquer dependência física aplicável ainda devem satisfazer os gates correspondentes.

DEL-05: identidade semântica e lifecycle do Plano de Participação estão DECIDED por DEC-DATA-047/SGATE-0025, portanto a especificação de cobertura + planejamento pode avançar. Isso não declara execução READY: grounding do repositório, contratos executáveis, critérios/provas e qualquer dependência física aplicável ainda devem satisfazer os gates correspondentes; BLOCKED-DATA-01 permanece vigente.

DEL-06: semântica factual suficientemente definida para aprofundar specs; persistência/enforcement concretos dependem do repo e do gate físico quando aplicável.

DEL-07 e DEL-08: conteúdo operacional pode ser especificado; IA/navegação final permanece bloqueada por OPEN-UX-01.

DEL-09: regras de autorização/proveniência podem ser especificadas; enforcement concreto depende dos contratos executáveis/RLS reais.

DEL-10: IMPLEMENTATION_BLOCKED por BLOCKED-DATA-01; somente contrato lógico/documental pode avançar.

DEL-11: planejamento de cutover pode avançar, mas destino físico final depende de DEL-10 liberado e homologado.

DEL-12: NOT READY para direção visual final enquanto OPEN-VIS-01/OPEN-A11Y-01 permanecerem abertos; padrões semânticos já decididos continuam válidos.

DEL-13: protocolo de prova pode avançar; comandos e artefatos exatos dependem do grounding do repositório.

12.4. REGRA DE BLOQUEIO PARCIAL

Questão OPEN bloqueia somente as tarefas e critérios materialmente dependentes dela. Não usar OPEN-UX-01, por exemplo, para impedir especificação de invariantes de presença factual; e não usar um contrato semântico pronto para liberar alteração física de banco enquanto BLOCKED-DATA-01 existir.