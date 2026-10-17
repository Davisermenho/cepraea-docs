FLUXO

FLUXO COMPLETO DE DESENVOLVIMENTO — CEPRAEA BEACH PRO

Fluxo de SDLC agêntico governado por humanos — HOMOLOGADO / BASELINE NORMATIVA VIGENTE

STATUS: RASCUNHO / HOMOLOGATED / CANONICAL — homologado por Davi Sermenho em 2026-08-14. Incorpora [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit) e [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit). Esta guia é a baseline normativa vigente do fluxo completo.

# 0. Autoridade documental e precedência

As guias de decisão APPROVED são a autoridade decisória deste fluxo. Esta guia FLUXO é a projeção consolidada dessas decisões.

Em caso de conflito entre esta guia e uma decisão APPROVED, prevalece a decisão APPROVED até nova reconciliação explícita.

Decisões vigentes: DEC-SDLC-001 — handoff Drive → repositório; DEC-SDLC-002 — workflow sem Git worktrees; DEC-SDLC-003 — identidade e estabilidade do objeto de review; DEC-SDLC-004 — fronteira da autonomia agêntica e integração Git humana; DEC-DOM-001 — cadeia de promoção e validação do domínio; DEC-SEC-001 — Source Corpus, privacidade e isolamento do Reviewer; DEC-SDLC-005 — contrato da tarefa, risco e assurance; DEC-SDLC-006 — estados, handoff e gates.

# 

# 1. Finalidade

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

O CEPRAEA BEACH PRO é desenvolvido por um SDLC humano-agente em que a modelagem do domínio, a implementação e o assurance são rastreáveis, enquanto a autoridade normativa, a promoção Git e o release permanecem humanos.

O runtime do produto é determinístico e não depende de LLM para decisões de negócio.

A fase de planejamento ocorre no Google Drive. Após o handoff, o trabalho de desenvolvimento ocorre no repositório local no VS Code. Claude Code atua como Executor e Codex como Reviewer independente.

# 2. Princípios globais

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

DOMAIN_AUTHORITY != CONTROL_AUTHORITY.

AGENT_POLICY.md != fonte de domínio.

Git != autoridade de domínio.

teste != verdade de domínio.

agente != autoridade.

SOURCE_CORPUS != EXECUTION_DOMAIN_BASELINE.

CAPABILITY != AUTHORITY.

AGENT_CONSENSUS != HUMAN_AUTHORITY.

NO_PAID_API != NO_GOVERNANCE.

DUAL_SSOT_AFTER_HANDOFF = forbidden.

GIT_WORKTREE_IN_WORKFLOW = false.

SIBLING_WORKTREE_REQUIRED = false.

SHARED_PHYSICAL_WORKING_TREE = true.

SOURCE_TO_LOGICAL_MODEL = forbidden.

SOURCE_TO_CANONICAL_RULE = forbidden.

INFERENCE_TO_VALIDATED_DOMAIN_ELEMENT = forbidden.

CODE_EXISTING_TO_DOMAIN_TRUTH = forbidden.

# 3. Planos de autoridade

## 3.1 Plano de domínio / produto

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

MUNDO REAL / FENÔMENO

↓

SOURCE CORPUS

↓

SRC

↓

EVD

↓

TERMO / REGRA

↓

CANDIDATO

↓

RECONCILIAÇÃO

↓

ELEMENTO DE DOMÍNIO PROPOSTO

↓

CODEX — SEMANTIC REVIEW

↓

DAVI — DOMAIN AUTHORITY

↓

VALIDADO | REJEITADO

↓

DOMAIN BASELINE

↓

MATURITY GATE

↓

MODELO LÓGICO

↓

INVARIANTES DE DOMÍNIO

↓

REQUISITOS DE DOMÍNIO

Antes da homologação humana, as asserções permanecem no ASSERTION_REGISTRY. O termo CANONICAL não é aplicado a conteúdo proposto, inferido, ambíguo, conflitante ou ainda não validado.

ASSERTION_KIND, EPISTEMIC_STATE e MATURITY_STATE são dimensões independentes:

ASSERTION_KIND = FATO | DECLARACAO | PLANO | DECISAO | DERIVACAO | INFERENCIA.

EPISTEMIC_STATE = OBSERVADO | INFERIDO | AMBIGUO | CONFLITANTE | VALIDADO | REJEITADO.

MATURITY_STATE = IMATURA | PARCIALMENTE_MADURA | MADURA_PARA_MODELO_LOGICO.

EPISTEMIC_STATE=VALIDADO exige aprovação humana real por Davi Sermenho. PASS do Codex não equivale a VALIDADO.

## 3.2 Plano de controle dos agentes

Decisões aplicáveis: [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

CONTROL AUTHORITY HUMANA

↓

AGENT_POLICY.md

↓

CLAUDE.md / AGENTS.md

AGENT_POLICY.md materializa a Control Authority. CLAUDE.md adapta o papel do Executor. AGENTS.md adapta o papel do Reviewer. Nenhum desses arquivos cria regra esportiva ou regra semântica do produto.

## 3.3 Convergência

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

EXECUTION_DOMAIN_BASELINE + CONTROL POLICY + TASK CONTRACT

↓

CLAUDE CODE — EXECUTOR

↓

EVIDENCE

↓

CODEX — INDEPENDENT ASSURANCE

↓

READY_FOR_HUMAN_INTEGRATION

↓

DAVI — GIT / RELEASE AUTHORITY

# 4. Papéis e limites

## 4.1 Davi Sermenho

Decisões aplicáveis: [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Davi exerce DOMAIN AUTHORITY, CONTROL AUTHORITY, EXCEPTION AUTHORITY, GIT AUTHORITY e RELEASE AUTHORITY nos pontos definidos neste fluxo.

Somente Davi pode criar ou selecionar branch de trabalho para a tarefa, executar commit, push, merge, rebase, tag, deploy, manipulação de secrets e promoção de release.

## 4.2 Claude Code — Executor

Decisões aplicáveis: [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Claude Code é o único agente escritor da branch de trabalho.

Claude só escreve dentro do WRITE_SCOPE autorizado e somente depois de TASK CONTRACT definido e estado AUTHORIZED.

Claude não cria branch, não altera refs, não executa git worktree, commit, push, merge, rebase, tag, deploy ou manipulação de secrets.

Seu resultado normal é uma working tree não commitada em READY_FOR_REVIEW.

## 4.3 Codex — Reviewer

Decisões aplicáveis: [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Codex é Reviewer independente e read-only.

CODEX_WRITE_SCOPE = ∅.

O ambiente do Reviewer deve demonstrar: leitura de arquivo = ALLOWED; git status/diff = ALLOWED; escrita no filesystem = DENIED; mutação Git = DENIED.

Se esse enforcement não puder ser demonstrado, VERIFICATION_STATUS=ENVIRONMENT_INSUFFICIENT e PASS é proibido.

Codex não modifica o objeto que avalia e não promove estado semântico para VALIDADO.

## 4.4 Challenger externo

Decisões aplicáveis: [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

ChatGPT ou Gemini podem ser usados para análise challenger ou mediação. Não substituem Codex, não substituem Davi e não integram o runtime.

## 4.5 Topologia da shared working tree

Decisões aplicáveis: [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

GIT_WORKTREE_IN_WORKFLOW=false; SIBLING_WORKTREE_REQUIRED=false; SHARED_PHYSICAL_WORKING_TREE=true.

Claude Code e Codex observam a mesma working tree física.

MESMA WORKING TREE

├─ Claude Code / Executor: RW somente dentro do WRITE_SCOPE

└─ Codex / Reviewer: read-only, CODEX_WRITE_SCOPE=∅

A superfície de review é: git status + tracked diff + staged diff + UNTRACKED_CONTENT_MANIFEST + evidência requerida. `git diff` isoladamente não representa o objeto completo.

A independência entre Executor e Reviewer é garantida por papel, permissões, freeze, REVIEW_TARGET_ID e autoridade, não por checkout Git separado.

# 5. Boundary planejamento → desenvolvimento

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

A sequência oficial do handoff é única:

GOOGLE DRIVE

↓

SELEÇÃO HUMANA DE FONTES

↓

CÓPIA PARA .drive/**

↓

SOURCE_CORPUS_MANIFEST

↓

HASH / PROVENANCE VALIDATION

↓

SENSITIVITY CHECK

↓

HUMAN VALIDATION

↓

SOURCE_CORPUS_READY

.drive/BEACHHANDBALL/** é o corpus externo do domínio: regras da modalidade e literatura técnico-científica.

.drive/CEPRAEA-BEACH-PRO/** é o corpus interno da realidade operacional do CEPRAEA: planilhas, agenda, disponibilidade, feedback e documentos operacionais.

Presença em .drive/** significa seleção para inspeção; não significa autoridade normativa.

O Google Drive deixa de ser dependência operacional do caminho crítico após SOURCE_CORPUS_READY.

# 6. Source Corpus Manifest e integridade

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

SOURCE_CORPUS_MANIFEST deve registrar, por arquivo: source_corpus_id, relative_path, source_id/origin, sha256, size, mime/type, captured_at, selected_by e sensitivity_class.

Antes de uma tarefa que dependa do corpus, o estado local é validado contra o manifesto.

ACTUAL_CORPUS_HASH == MANIFEST_HASH é condição de continuidade.

Se houver divergência: SOURCE_CORPUS_CHANGED → REVALIDATION_REQUIRED → HUMAN VALIDATION antes de nova modelagem dependente do corpus.

.drive/** pertence ao READ_SCOPE da tarefa fundacional e permanece fora do WRITE_SCOPE. As fontes não são reescritas pelos agentes.

# 7. Tarefa fundacional de modelagem

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

SOURCE_CORPUS_READY não autoriza escrita automaticamente.

Davi cria ou seleciona WORK_BRANCH e fixa BASE_COMMIT_SHA.

Em seguida:

FOUNDATIONAL_DOMAIN_MODELING_TASK

↓

TASK DEFINITION

↓

RISK CLASSIFICATION

↓

READ_SCOPE + WRITE_SCOPE

↓

AUTHORIZED

↓

CONTEXT_LOADING

↓

REPOSITORY + CORPUS INSPECTION

↓

DOMAIN_DISCOVERY_IN_PROGRESS

↓

DOMAIN MODELING

Para essa tarefa, DOMAIN_BASELINE_REF = NOT_APPLICABLE_FOUNDATIONAL e SOURCE_CORPUS_ID é obrigatório.

# 8. Cadeia de promoção da modelagem

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

A modelagem fundacional segue obrigatoriamente:

SOURCE CORPUS

↓

SRC

↓

EVD

↓

TERMO / REGRA

↓

CANDIDATO

↓

RECONCILIAÇÃO

↓

ELEMENTO DE DOMÍNIO PROPOSTO

↓

MODEL_PROPOSAL_READY_FOR_REVIEW

↓

MODEL_IN_REVIEW

↓

CODEX — SEMANTIC REVIEW

├─ FAIL → MODEL_CORRECTION_REQUIRED → Claude corrige → novo MODEL_PROPOSAL_READY_FOR_REVIEW

├─ HUMAN_DECISION_REQUIRED → HUMAN DECISION → MODEL_CORRECTION_REQUIRED | MODEL_READY_FOR_HUMAN_VALIDATION | REJECTED

└─ PASS → MODEL_READY_FOR_HUMAN_VALIDATION

↓

DAVI

↓

VALIDADO | REJEITADO

Somente elementos VALIDADO podem compor DOMAIN BASELINE.

O pacote MODEL_PROPOSAL_READY_FOR_REVIEW deve conter, ainda em estado PROPOSED, todos os artefatos semânticos que se pretende promover: elementos de domínio e, quando já derivados, propostas de modelo lógico, invariantes e requisitos. O review semântico usa o mesmo protocolo REVIEW_TARGET_ID + EXECUTOR_WRITE_FREEZE das seções 18–20.

Após a decisão humana:

MATURITY GATE

├─ IMATURA → não promover ao modelo lógico

├─ PARCIALMENTE_MADURA → não promover ao modelo lógico

└─ MADURA_PARA_MODELO_LOGICO → promoção permitida

↓

MODELO LÓGICO

↓

INVARIANTES DE DOMÍNIO

↓

REQUISITOS DE DOMÍNIO

↓

READY_FOR_HUMAN_INTEGRATION

↓

DAVI — COMMIT / CONTENT EQUIVALENCE / CI conforme política

↓

EXECUTION_DOMAIN_BASELINE_READY

A homologação humana não autoriza introdução de novo conteúdo sem review. Se a materialização de VALIDADO, a derivação lógica, as invariantes, os requisitos ou qualquer registro de homologação alterarem a working tree após o review semântico, REVIEW_TARGET_ID muda e um novo review do estado final é obrigatório antes da integração Git. EXECUTION_DOMAIN_BASELINE_READY somente existe após homologação humana, review válido do estado final e integração Git humana da baseline.

Conflito estrutural pendente impede MATURITY_STATE=MADURA_PARA_MODELO_LOGICO.

CEPRAEA_REALITY_ATOM permanece PROPOSED_PROCESS_REPRESENTATION e não é gate obrigatório. Pode ser usado apenas como técnica auxiliar enquanto não houver homologação específica.

# 9. Contrato mínimo da tarefa

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Nenhuma escrita do Executor começa sem TASK CONTRACT definido.

Campos mínimos:

TASK_ID

TASK_TYPE

OBJECTIVE

RISK_LEVEL

WORK_BRANCH

BASE_COMMIT_SHA

READ_SCOPE

WRITE_SCOPE

FORBIDDEN_OPERATIONS

EXECUTOR

REVIEWER

DOMAIN_BASELINE_REF

REQUIREMENTS[]

INVARIANTS[]

ACCEPTANCE_CRITERIA[]

EXPECTED_EVIDENCE[]

SOURCE_CORPUS_ID, quando TASK_TYPE=DOMAIN_MODELING.

A tarefa sai de REQUESTED para DEFINED somente quando todos os campos obrigatórios aplicáveis estiverem presentes e sem conflito. AUTHORIZED é estado posterior.

# 10. Classificação de risco

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

RISK_LEVEL = GREEN | YELLOW | RED | RED_CRITICAL.

AGENT_POLICY.md é a única autoridade de controle para a matriz que resolve, por RISK_LEVEL:

PLAN_REQUIRED

HUMAN_PRE_GATE_REQUIRED

CODEX_REVIEW_REQUIRED

REQUIRED_TEST_CLASSES

REQUIRED_EVIDENCE

WRITE_SCOPE_POLICY

CONTROL_PLANE_GATE

RELEASE_GATE

O TASK CONTRACT materializa os valores resolvidos dessa matriz.

Se AGENT_POLICY.md estiver ausente, inacessível ou sem regra capaz de resolver um campo obrigatório da matriz: CONTROL_POLICY_UNRESOLVED → BLOCKED. Se duas regras normativas aplicáveis entrarem em conflito e exigirem escolha de autoridade: HUMAN_DECISION_REQUIRED. CODEX_REVIEW_REQUIRED=false sem uma transição alternativa explicitamente definida pela própria política produz CONTROL_POLICY_UNRESOLVED → BLOCKED; o fluxo não inventa um bypass de assurance.

Expressões como “proporcional ao risco”, “evidência suficiente”, “testes adequados”, “mudança material” ou “invariante crítica” não constituem gates por si mesmas.

# 11. Physical Stop Gate

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Imediatamente após a classificação da tarefa:

PHYSICAL_IMPACT?

├─ NO → continuar

└─ YES

↓

PHYSICAL_STOP_GATE

├─ CLOSED → BLOCKED

└─ OPEN

↓

inspect actual schema/version

↓

physical planning

Enquanto PHYSICAL_STOP_GATE=CLOSED, é proibido gerar ou executar SQL, DDL, migration, RLS, índice, trigger ou alteração de schema físico.

A decisão de abertura é humana. Nenhum plano, agente, teste ou conveniência técnica abre o gate implicitamente.

# 12. Carregamento de contexto

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Control Context = AGENT_POLICY.md + adapter do papel.

Task Context = TASK CONTRACT autorizado.

Domain Context, em tarefas posteriores à modelagem = EXECUTION_DOMAIN_BASELINE e invariantes aplicáveis.

Model Context, na tarefa fundacional = SOURCE_CORPUS_MANIFEST + corpus permitido por READ_SCOPE; não existe modelo anterior obrigatório.

Repository Context = arquivos, configuração, testes, schemas, migrations e demais objetos que o READ_SCOPE exigir.

KNOWN e UNKNOWN UNTIL INSPECTION permanecem distintos.

# 13. Inspeção da realidade

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Antes de planejar mudança, o Executor inspeciona: WORK_BRANCH, BASE_COMMIT_SHA, git status, working tree, staged state, untracked relevantes, arquivos existentes, arquitetura, dependências, schemas, migrations, testes, CI e comportamento implementado.

Na modelagem fundacional, também inspeciona o corpus e valida SOURCE_CORPUS_MANIFEST.

Se git status revelar alteração preexistente fora do WRITE_SCOPE e fora dos objetos explicitamente declarados como read-only no TASK CONTRACT, o estado é BASELINE_CONFLICT → BLOCKED até Davi resolver o estado ou revisar explicitamente o contrato. Claude não pode stash, reset, checkout, clean ou alterar essa mudança para contornar o conflito.

UNKNOWN, MISSING, CONFLICTED, OUT_OF_SCOPE, UNAUTHORIZED, BASELINE_CONFLICT e ENVIRONMENT_INSUFFICIENT não são convertidos em conformidade narrativa.

# 14. Requisitos, invariantes e controles

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Em tarefas posteriores à modelagem:

REQUEST

↓

REQUIREMENT

↓

APPLICABLE INVARIANTS

↓

ACCEPTANCE CRITERIA

Durante a modelagem fundacional, DOMAIN BASELINE → MATURITY GATE → MODELO LÓGICO → INVARIANTES DE DOMÍNIO → REQUISITOS DE DOMÍNIO é uma cadeia distinta.

Regras de domínio, regras de controle dos agentes, implementação existente e testes permanecem categorias separadas.

POLICY_EVALUATION_RESULT = PASS | FAIL | INDETERMINATE é resultado de uma Domain Policy e não é ASSURANCE_VERDICT.

UNKNOWN, MISSING, CONFLICTED, INDETERMINATE e ERROR não produzem POLICY_EVALUATION_RESULT=PASS em operação protegida.

# 15. Plano de implementação e gate humano

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Se PLAN_REQUIRED=true, o plano descreve: arquivos/áreas a alterar, ordem, invariantes, testes, riscos, evidências e critérios de conclusão.

Se PLAN_REQUIRED=false, a ausência de plano é permitida apenas porque a matriz de AGENT_POLICY.md assim resolveu.

Se HUMAN_PRE_GATE_REQUIRED=true, a execução fica BLOCKED até decisão humana.

O agente não amplia escopo, não troca tecnologia e não inclui refatoração fora do WRITE_SCOPE sem nova autorização.

# 16. Execução pelo Claude Code

Decisões aplicáveis: [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Pré-condições:

WORK_ITEM_STATE=AUTHORIZED.

WRITE_SCOPE definido.

FORBIDDEN_OPERATIONS definido.

PHYSICAL_STOP_GATE compatível com a tarefa.

HUMAN_PRE_GATE resolvido quando requerido.

Claude altera somente paths dentro de WRITE_SCOPE.

Cada alteração produzida pelo Executor deve mapear para pelo menos um REQUIREMENT[] e seus ACCEPTANCE_CRITERIA[] no TASK CONTRACT. Alteração sem esse mapeamento é OUT_OF_SCOPE. Qualquer expansão exige novo TASK CONTRACT ou revisão explícita do contrato existente antes da escrita correspondente.

Saída esperada: working tree não commitada.

# 17. Shift-Left e evidência

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

A validação local executa apenas as classes de teste e controles resolvidos por REQUIRED_TEST_CLASSES e REQUIRED_EVIDENCE.

O Executor registra TESTS_EXECUTED, EXIT_CODES, FILES_CHANGED, KNOWN_LIMITATIONS e evidência de cada ACCEPTANCE_CRITERION.

Ausência de erro observado != evidência positiva.

Self-check do Executor != independent assurance.

# 18. Identidade do objeto de review

Decisões aplicáveis: [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

REVIEW_TARGET_SHA não é usado antes do commit.

REVIEW_TARGET_ID identifica a mesma working tree não commitada que Codex revisará.

REVIEW_TARGET_ID = SHA-256 de uma representação canônica contendo:

BASE_COMMIT_SHA

TRACKED_DIFF_HASH

STAGED_DIFF_HASH

UNTRACKED_CONTENT_MANIFEST_HASH

SOURCE_CORPUS_MANIFEST_HASH, obrigatório quando SOURCE_CORPUS_ID estiver presente no TASK CONTRACT.

UNTRACKED_CONTENT_MANIFEST_HASH deve cobrir todo conteúdo não representado pelos diffs que influencia o objeto revisado, incluindo arquivos untracked e arquivos ignored explicitamente declarados como relevantes para a tarefa.

Se uma dependência ignored influenciar teste ou comportamento e não estiver declarada na evidência, PASS é proibido.

# 19. READY_FOR_REVIEW e freeze

Decisões aplicáveis: [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

READY_FOR_REVIEW exige:

escopo autorizado implementado;

validações locais requeridas concluídas;

evidências requeridas materializadas;

REVIEW_TARGET_ID calculado;

git status, tracked diff, staged diff e conteúdo não rastreado relevante conhecidos.

Transição:

READY_FOR_REVIEW

↓

EXECUTOR_WRITE_FREEZE

↓

IN_REVIEW

↓

CODEX REVIEW

↓

recalcular REVIEW_TARGET_ID

REVIEW_TARGET_ID_BEFORE == REVIEW_TARGET_ID_AFTER → review permanece válido.

REVIEW_TARGET_ID_BEFORE != REVIEW_TARGET_ID_AFTER → REVIEW_INVALIDATED.

Qualquer mutação por Claude, Davi, hook, formatter, ferramenta ou outro processo invalida o review em curso.

Durante EXECUTOR_WRITE_FREEZE, nenhuma escrita sobre o objeto revisado é permitida. O freeze não exige nova Git worktree nem remount dinâmico: a validade é determinística pela igualdade REVIEW_TARGET_ID_BEFORE == REVIEW_TARGET_ID_AFTER; qualquer mutação detectada invalida o review.

# 20. Assurance independente

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Codex recebe TASK CONTRACT, controles normativos, BASE_COMMIT_SHA, REVIEW_TARGET_ID, working tree, git status, diffs, manifesto de conteúdo não rastreado e evidências.

O review verifica requisitos, invariantes, escopo, regressões, bypasses, segurança, cobertura de teste requerida, evidência e mutações não autorizadas.

O review é adversarial e inclui, quando aplicável pela matriz de testes: NULL, boundaries, rota alternativa, concorrência, estado legado, fail-open e constraint ausente.

VERIFICATION_STATUS = COMPLETED | BLOCKED | UNVERIFIABLE | ENVIRONMENT_INSUFFICIENT.

ASSURANCE_VERDICT = PASS | FAIL | HUMAN_DECISION_REQUIRED.

PASS somente pode ser emitido quando:

verification_status=COMPLETED;

todos os ACCEPTANCE_CRITERIA requeridos=DEMONSTRATED;

todas as invariantes aplicáveis=PRESERVED;

unauthorized_change_count=0;

review_target_unchanged=true.

Se existir claim obrigatório não verificado, PASS é proibido.

FAIL é emitido quando evidência demonstra bug, regressão, violação de invariante, mudança fora de WRITE_SCOPE, controle exigido ausente ou falha de processo que impeça conformidade.

HUMAN_DECISION_REQUIRED é emitido para lacuna normativa, conflito de autoridade, exceção ou decisão reservada ao humano.

# 21. Loop de correção e invalidação

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

FAIL:

IN_REVIEW

↓

CORRECTION_REQUIRED

↓

remover freeze

↓

CLAUDE CODE

↓

Shift-Left

↓

novo REVIEW_TARGET_ID

↓

READY_FOR_REVIEW

↓

novo review

REVIEW_INVALIDATED:

IN_REVIEW

↓

REVIEW_INVALIDATED

↓

remover freeze

↓

reconciliar mutação

↓

Shift-Left

↓

novo REVIEW_TARGET_ID

↓

READY_FOR_REVIEW

↓

novo review

HUMAN_DECISION_REQUIRED:

IN_REVIEW

↓

HUMAN_DECISION_REQUIRED

↓

DAVI — HUMAN DECISION

├─ REJECTED → WORK_ITEM_STATE=REJECTED

├─ CORRECTION_REQUIRED ou qualquer mutação do objeto → novo REVIEW_TARGET_ID → novo review

└─ AUTHORIZED_TO_CONTINUE com REVIEW_TARGET_ID inalterado e sem FAIL técnico pendente → READY_FOR_HUMAN_INTEGRATION

FAIL nunca é convertido diretamente em READY_FOR_HUMAN_INTEGRATION por decisão humana; exige correção e novo review. Nenhum PASS é transferido para REVIEW_TARGET_ID diferente.

# 22. Fronteira da autonomia agêntica

Decisões aplicáveis: [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

READY_FOR_HUMAN_INTEGRATION pode ser alcançado por um de dois caminhos:

1) ASSURANCE_VERDICT=PASS válido; ou

2) ASSURANCE_VERDICT=HUMAN_DECISION_REQUIRED resolvido por Davi como AUTHORIZED_TO_CONTINUE, com REVIEW_TARGET_ID inalterado e sem FAIL técnico pendente.

READY_FOR_HUMAN_INTEGRATION

════════ FIM DA AUTONOMIA AGÊNTICA ════════

Claude Code e Codex não executam operações de promoção Git ou release a partir desse estado.

# 23. Integração Git humana

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

DAVI

↓

COMMIT

↓

VERIFY COMMITTED_CONTENT == REVIEWED_CONTENT

├─ NO → REVIEW_REQUIRED_AGAIN

└─ YES

↓

PUSH

↓

CI

├─ FAIL → não integrar

└─ PASS

↓

MERGE POR DAVI

↓

POST-MERGE BUILD / VERIFICATION

↓

READY_FOR_RELEASE

COMMITTED_CONTENT == REVIEWED_CONTENT deve ser demonstrado por comparação do conteúdo do commit com o conjunto de conteúdo identificado pelo REVIEW_TARGET_ID. Se a comparação falhar, a promoção para antes do push é interrompida; o commit não possui cobertura do PASS anterior. Davi restaura/prepara o estado correto ou altera o commit por operação humana permitida, e o conteúdo resultante passa por novo review antes de push/merge.

Commit, push, merge, rebase e tag permanecem operações humanas.

# 24. CI, release e pós-release

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

CI executa em checkout limpo os controles definidos pela política do projeto e pela tarefa: instalação controlada, typecheck, lint, testes, análise estática, verificações de segurança e build quando configurados.

CI FAIL impede integração ou promoção.

RELEASE_GATE é resolvido pela matriz de risco e pela política do projeto.

Davi autoriza e executa deploy/release.

O artefato publicado deve corresponder ao artefato verificado; divergência invalida a promoção.

Após publicação, verificar carregamento do PWA, fluxos críticos, integridade de dados, migrations autorizadas e propriedades offline-first aplicáveis.

Falha pós-release gera contenção, rollback quando definido e nova tarefa de engenharia.

# 25. Segurança, PII e Secrets

Decisões aplicáveis: [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

SECRETS_IN_AGENT_CONTEXT = forbidden.

Credenciais, tokens, chaves privadas e equivalentes nunca entram no contexto dos agentes.

PII operacional pode ser lida somente quando o READ_SCOPE autorizado a inclui e o TASK CONTRACT referencia o OBJECTIVE ou REQUIREMENT que exige essa leitura.

PII fora do READ_SCOPE é proibida. PII sem vínculo explícito ao OBJECTIVE/REQUIREMENT deve ser minimizada ou pseudonimizada antes do consumo pelo agente.

Dados Wellness são classificados como sensíveis e seguem minimização e READ_SCOPE explícito.

REAL_OPERATIONAL_DATA_IN_TESTS = forbidden.

TEST_DATA = SYNTHETIC | MOCK.

Incidente: DETECT → CONTAIN → BLOCK FURTHER PROCESSING → REMOVE ACCESS → ROTATE/REVOKE SECRET quando houver → ASSESS HISTORY/LOGS → SANITIZE → VERIFY PREVENTION.

# 26. Requisitos offline-first

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Quando um requisito envolver operação offline, a tarefa deve declarar os estados e invariantes de armazenamento local, retry, idempotência, stale data, sincronização e conflitos de reconexão.

Estados como LOCAL_PENDING, SYNCED, CONFLICT e FAILED só são introduzidos quando definidos por requisito/invariante.

Sincronização não pode criar duas fontes autoritativas concorrentes.

# 27. Máquinas de estado

## 27.1 PROCESS_PHASE

Decisões aplicáveis: [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

HANDOFF

TASK_DEFINITION

RISK_CLASSIFICATION

CONTEXT_LOADING

REPOSITORY_INSPECTION

DOMAIN_DISCOVERY

DOMAIN_MODELING

REQUIREMENT_RESOLUTION

PHYSICAL_GATE_EVALUATION

PLANNING

IMPLEMENTATION

LOCAL_VERIFICATION

EVIDENCE_MATERIALIZATION

INDEPENDENT_REVIEW

HUMAN_INTEGRATION

CI_VERIFICATION

RELEASE_VERIFICATION

## 27.2 MODELING_STATE

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

SOURCE_CORPUS_READY

DOMAIN_DISCOVERY_IN_PROGRESS

MODEL_PROPOSAL_READY_FOR_REVIEW

MODEL_IN_REVIEW

MODEL_CORRECTION_REQUIRED

MODEL_READY_FOR_HUMAN_VALIDATION

EXECUTION_DOMAIN_BASELINE_READY

## 27.3 WORK_ITEM_STATE

Decisões aplicáveis: [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

REQUESTED

DEFINED

AUTHORIZED

IN_EXECUTION

READY_FOR_REVIEW

IN_REVIEW

CORRECTION_REQUIRED

REVIEW_INVALIDATED

READY_FOR_HUMAN_INTEGRATION

INTEGRATED

READY_FOR_RELEASE

RELEASED

BLOCKED

REJECTED

INTEGRATED = HUMAN_ONLY.

READY_FOR_RELEASE = HUMAN_CONTROLLED.

RELEASED = HUMAN_ONLY.

## 27.4 EPISTEMIC_STATE

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

OBSERVADO

INFERIDO

AMBIGUO

CONFLITANTE

VALIDADO

REJEITADO

## 27.5 MATURITY_STATE

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

IMATURA

PARCIALMENTE_MADURA

MADURA_PARA_MODELO_LOGICO

## 27.6 VERIFICATION_STATUS

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

COMPLETED

BLOCKED

UNVERIFIABLE

ENVIRONMENT_INSUFFICIENT

## 27.7 ASSURANCE_VERDICT

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

PASS

FAIL

HUMAN_DECISION_REQUIRED

## 27.8 POLICY_EVALUATION_RESULT

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

PASS

FAIL

INDETERMINATE

As dimensões acima não são intercambiáveis.

# 28. Estados de exceção e fail-closed

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Estados de exceção incluem UNKNOWN, MISSING, CONFLICTED, OUT_OF_SCOPE, UNAUTHORIZED, BLOCKED, UNVERIFIABLE e ENVIRONMENT_INSUFFICIENT.

Condições/marcadores de transição, e não novas dimensões de estado: BASELINE_CONFLICT, CONTROL_POLICY_UNRESOLVED, SOURCE_CORPUS_CHANGED, REVALIDATION_REQUIRED e REVIEW_REQUIRED_AGAIN. Cada marcador conduz ao WORK_ITEM_STATE, MODELING_STATE ou VERIFICATION_STATUS explicitamente indicado na seção que o utiliza.

Nenhum estado de exceção ou marcador é convertido narrativamente em PASS.

Tratamento: DETECT → CLASSIFY → CONTAIN → PRESERVE EVIDENCE → IDENTIFY AUTHORITY → RESOLVE ROOT CAUSE → REPAIR → VERIFY → INDEPENDENT REVIEW → RESTORE FLOW.

# 29. Definition of Done

Decisões aplicáveis: [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

EXECUTOR_DONE:

implementação da tarefa dentro do WRITE_SCOPE;

Shift-Left requerido concluído;

EXPECTED_EVIDENCE materializada;

READY_FOR_REVIEW alcançado.

AGENTIC_TASK_DONE:

review Codex concluído;

PASS válido ou decisão humana requerida resolvida;

REVIEW_TARGET_ID preservado;

READY_FOR_HUMAN_INTEGRATION alcançado.

CHANGE_INTEGRATED:

commit humano;

COMMITTED_CONTENT == REVIEWED_CONTENT;

CI PASS;

merge humano.

RELEASE_DONE:

RELEASE_GATE satisfeito;

deploy/release humano;

verificação pós-release concluída conforme critérios definidos.

# 30. Rastreabilidade ponta a ponta

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Modelagem fundacional:

SOURCE_CORPUS_MANIFEST

→ SRC

→ EVD

→ TERMO / REGRA

→ CANDIDATO

→ RECONCILIAÇÃO

→ ELEMENTO DE DOMÍNIO PROPOSTO

→ CODEX SEMANTIC REVIEW

→ DAVI VALIDATION

→ DOMAIN BASELINE

→ MATURITY GATE

→ MODELO LÓGICO

→ INVARIANTES

→ REQUISITOS

→ EXECUTION_DOMAIN_BASELINE_READY

Implementação:

TASK

→ REQUIREMENT

→ INVARIANT

→ ACCEPTANCE_CRITERION

→ WRITE_SCOPE

→ BASE_COMMIT_SHA

→ CHANGE

→ TEST

→ EVIDENCE

→ REVIEW_TARGET_ID

→ CODEX VERDICT

→ READY_FOR_HUMAN_INTEGRATION

→ HUMAN COMMIT

→ COMMITTED_CONTENT == REVIEWED_CONTENT

→ CI

→ HUMAN MERGE

→ RELEASE

Git contribui para proveniência operacional, mas não demonstra sozinho qual agente produziu a alteração nem substitui a evidência de REVIEW_TARGET_ID.

# 31. Fluxos especiais

## 31.1 Mudança de domínio

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Nova evidência → SOURCE/SRC/EVD → TERMO/REGRA → CANDIDATO → RECONCILIAÇÃO → CODEX SEMANTIC REVIEW → DAVI VALIDATION → DOMAIN BASELINE → MATURITY GATE → modelo lógico afetado → invariantes/requisitos → nova tarefa de engenharia.

É proibido alterar primeiro o código e reescrever retroativamente decisão normativa para justificar a implementação.

## 31.2 Mudança do Control Plane

Decisões aplicáveis: [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Alteração de AGENT_POLICY.md, CLAUDE.md, AGENTS.md, sandbox, permissões, CI ou verificadores segue TASK CONTRACT próprio e a matriz de risco vigente.

Se CONTROL_PLANE_GATE exigir aprovação humana, a mudança permanece BLOCKED até decisão.

O controle alterado deve ser testado antes de ser considerado efetivo.

## 31.3 Mudança física de banco

Decisões aplicáveis: [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Qualquer impacto físico passa pelo PHYSICAL_STOP_GATE da seção 11 antes de planejamento físico.

Gate CLOSED mantém SQL, DDL, migrations, RLS, índices, triggers e alterações de schema bloqueados.

## 31.4 Mudança do Source Corpus

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Qualquer diferença de hash entre corpus e SOURCE_CORPUS_MANIFEST gera SOURCE_CORPUS_CHANGED → REVALIDATION_REQUIRED. Nenhuma modelagem dependente do corpus prossegue antes da validação humana.

# 32. Exemplos não normativos

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Os exemplos desta seção ilustram somente a mecânica epistemológica. NON_NORMATIVE_EXAMPLE = true. NO_EXECUTION_AUTHORITY = true.

## 32.1 Declaração de disponibilidade

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Uma atleta declarar disponibilidade é ASSERTION_KIND=DECLARACAO. A declaração não prova presença factual, participação integral, convocação ou aptidão física.

Regra ilustrativa: DECLAROU QUE IRIA != FOI.

## 32.2 Sessão planejada

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Um calendário pode sustentar ASSERTION_KIND=PLANO para uma sessão. Passagem do tempo não transforma PLANO em fato de realização.

Regra ilustrativa: PLANO + PASSAGEM DO TEMPO != FATO DE REALIZACAO.

## 32.3 Wellness

Decisões aplicáveis: [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Qualquer exemplo anterior de Wellness permanece histórico e não normativo até que a nova cadeia SRC → EVD → TERMO/REGRA → CANDIDATO → CODEX → DAVI produza elemento VALIDADO na nova modelagem do repositório.

Nenhuma regra WELLNESS_POS_REQUIRES_FACTUAL_ATTENDANCE é presumida por este fluxo.

# 33. Regras finais anti-regressão

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

1. REVIEW_TARGET_SHA antes do commit = forbidden.

2. REVIEW_TARGET_ID é obrigatório para review de working tree não commitada.

3. Mudança de REVIEW_TARGET_ID invalida o review anterior.

4. Git worktrees não integram este workflow.

5. Claude Code é o único agente escritor; Codex é Reviewer read-only.

6. CODEX_WRITE_SCOPE = ∅ e o enforcement read-only deve ser demonstrado.

7. Agentes não criam branch e não executam commit, push, merge, rebase, tag, deploy ou manipulação de secrets.

8. READY_FOR_HUMAN_INTEGRATION é o limite da autonomia agêntica.

9. SOURCE → LOGICAL_MODEL é proibido.

10. VALIDADO exige aprovação humana de Davi.

11. ASSERTION_REGISTRY precede qualquer baseline normativa.

12. SOURCE_CORPUS_READY não autoriza escrita; FOUNDATIONAL_DOMAIN_MODELING_TASK autorizada é obrigatória.

13. .drive/** é READ_SCOPE e permanece fora do WRITE_SCOPE nas tarefas de modelagem.

14. Secrets nunca entram no contexto dos agentes.

15. PII operacional requer READ_SCOPE explícito; testes usam apenas dados sintéticos/mock.

16. PASS exige VERIFICATION_STATUS=COMPLETED, todos AC requeridos DEMONSTRATED, invariantes PRESERVED, unauthorized_change_count=0 e review_target_unchanged=true.

17. Termos subjetivos não constituem gates sem resolução pela matriz de risco do AGENT_POLICY.md.

18. PHYSICAL_STOP_GATE é avaliado imediatamente após classificação quando PHYSICAL_IMPACT=YES.

19. PROCESS_PHASE, MODELING_STATE, WORK_ITEM_STATE, EPISTEMIC_STATE, MATURITY_STATE, VERIFICATION_STATUS, ASSURANCE_VERDICT e POLICY_EVALUATION_RESULT são dimensões distintas.

20. COMMITTED_CONTENT deve corresponder ao REVIEWED_CONTENT para preservar cobertura do review.

21. DUAL_SSOT_AFTER_HANDOFF = forbidden.

22. Exemplos de domínio nesta guia são não normativos.

23. CEPRAEA_REALITY_ATOM não é gate obrigatório enquanto permanecer PROPOSED_PROCESS_REPRESENTATION.

24. Nenhuma decisão APPROVED é reescrita retroativamente para justificar código existente.

25. O PHYSICAL_STOP_GATE permanece fechado até decisão humana explícita que o abra.

26. O fluxo completo está HOMOLOGATED / CANONICAL. Alteração normativa posterior exige nova decisão humana ou nova revisão/homologação conforme o escopo afetado.

# 34. Homologação do fluxo

Decisões aplicáveis: [DEC-SDLC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-002](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-003](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-004](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-DOM-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SEC-001](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-005](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit), [DEC-SDLC-006](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit).

Homologação concluída por Davi Sermenho em 2026-08-14. Esta versão adquiriu status CANONICAL após verificação dos seguintes critérios:

nenhum texto conflitante com DEC-SDLC-001..006, DEC-DOM-001 ou DEC-SEC-001 permanecer;

nenhum estado usado no macrofluxo estiver sem definição;

nenhum gate obrigatório definido pelas decisões ou pela matriz de risco depender de termo subjetivo sem predicado resolvido;

nenhum caminho alternativo permitir operação reservada a agente;

a varredura anti-regressão confirmar ausência dos padrões proibidos da seção 33.

.

DEC-SDLC-001

DEC-SDLC-001 — HANDOFF DE PLANEJAMENTO DRIVE → GIT E EXECUÇÃO LOCAL NO VS CODE

STATUS: RASCUNHO

Decision authority: Davi

Decision class: SDLC / AUTHORITY TOPOLOGY / EXECUTION ENVIRONMENT

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Contexto

A fase atual no Google Drive é exclusivamente de planejamento: levantamento, seleção de fontes, decisões, requisitos, definição do fluxo e homologações necessárias ao handoff. O CEPRAEA BEACH PRO será desenvolvido posteriormente no VS Code por Claude Code e Codex, utilizados como extensões, sem dependência de API paga para o fluxo de desenvolvimento. A modelagem do domínio que governará a implementação será feita novamente no repositório.

2. Decisão

O Google Drive NÃO fará parte da arquitetura operacional diária do desenvolvimento após o encerramento da fase de planejamento.

A transição entre planejamento e desenvolvimento será realizada por um HANDOFF CONTROLADO. O handoff transporta fontes e evidências selecionadas, não uma modelagem semântica pronta. No repositório local existem dois corpora de entrada:

.drive/BEACHHANDBALL/** = corpus externo do domínio, contendo regras do handebol de praia e literatura técnico-científica, incluindo sistemas defensivos, sistemas ofensivos, treinamento de goleiros, análise de desempenho em shoot-out e temas correlatos.

.drive/CEPRAEA-BEACH-PRO/** = corpus interno do CEPRAEA, contendo planilhas, agenda, disponibilidade, feedback e documentos com informações operacionais da equipe.

A inclusão de um arquivo nesses corpora significa relevância para inspeção/modelagem, não autoridade normativa automática.

Fluxo do handoff:

GOOGLE DRIVE — PLANEJAMENTO

↓

REVISÃO FINAL

↓

HOMOLOGAÇÃO HUMANA

↓

SOURCE CORPUS SELECTION APPROVED

↓

CÓPIA CONTROLADA DAS FONTES ESSENCIAIS PARA `.drive/**`

↓

SOURCE_CORPUS_MANIFEST + PROVENIÊNCIA

↓

VALIDAÇÃO HUMANA DO CORPUS COPIADO

↓

SOURCE_CORPUS_READY

↓

VS CODE + REPOSITÓRIO GIT — DESENVOLVIMENTO

3. Autoridade após o handoff

Durante o planejamento, o Google Drive funciona como ambiente de elaboração, evidência e registro de decisões. Modelagens semânticas preexistentes no Drive não serão usadas como autoridade nem como base obrigatória da nova modelagem deste SDLC.

Após o handoff aprovado, o repositório Git passa a ser o contexto executável e a fonte de verdade operacional do desenvolvimento. O handoff transporta o corpus local selecionado e sua proveniência. A modelagem de domínio é refeita no repositório, no VS Code, a partir de `.drive/BEACHHANDBALL/**`, `.drive/CEPRAEA-BEACH-PRO/**` e da inspeção da realidade local.

Um artefato como docs/02-domain/CEPRAEA_DOMAIN.md, se criado durante a nova modelagem no repositório, somente adquire papel de EXECUTION_DOMAIN_AUTHORITY após review independente e homologação humana explícita dessa nova modelagem.

4. Agentes e ambiente

Claude Code: EXECUTOR PLANE no VS Code.

Codex: ASSURANCE / REVIEWER PLANE independente no VS Code.

Humano: autoridade de domínio, controle, exceção, integração e release nos pontos reservados.

O mecanismo de coordenação entre os agentes é artefatual, por filesystem e Git. Não é necessária API agente-a-agente, orquestrador LLM, message broker, prompt server, vector service ou backend específico para comunicação entre Claude Code e Codex.

Fluxo operacional:

CLAUDE CODE

↓

código + testes + diff + evidência

↓

FILESYSTEM / GIT

↓

CODEX

↓

VERIFICATION_STATUS + ASSURANCE_VERDICT

↓

AUTORIDADE HUMANA, quando aplicável

↓

GIT / INTEGRAÇÃO / RELEASE

5. Regras de não duplicação de autoridade

Google Drive = planejamento, homologação e evidência histórica da fase de planejamento.

Git = contexto executável e estado operacional do desenvolvimento após o handoff.

AGENT_POLICY.md = Control Authority materializada para agentes.

CLAUDE.md = adapter do Executor.

AGENTS.md = adapter do Reviewer.

CEPRAEA_DOMAIN.md, se criado e homologado = autoridade normativa de execução produzida pela nova modelagem no repositório a partir do corpus local `.drive/**`.

É proibido exigir que Claude Code ou Codex conciliem rotineiramente versões concorrentes entre Drive e Git durante o desenvolvimento.

6. Proveniência mínima do handoff

A promoção deve preservar, no mínimo:

- source_corpus_id;

- arquivos selecionados para `.drive/BEACHHANDBALL/**` e `.drive/CEPRAEA-BEACH-PRO/**`;

- origem e identificadores das fontes, quando disponíveis;

- versão/status da fonte;

- caminho local exato em `.drive/**`;

- hash quando aplicável;

- autoridade humana de seleção/handoff;

- decisão de homologação e commit/tag dos futuros artefatos normativos da nova modelagem, separados do corpus de entrada.

7. Impacto no fluxo

Antes do handoff: Drive governa o planejamento.

Depois do handoff: agentes operam sobre o repositório local/Git no VS Code.

O Drive deixa de ser dependência operacional do caminho crítico de desenvolvimento.

O runtime do produto continua independente de LLMs/agentes.

A inexistência de API paga não reduz os requisitos de evidência, review independente, gates humanos ou enforcement determinístico.

8. Invariantes

DRIVE_PLANNING != GIT_EXECUTION_STATE

PLANNING_SOURCE != EXECUTION_SSOT

SOURCE_CORPUS != EXECUTION_DOMAIN_MODEL

PRESENCE_IN_DOT_DRIVE != NORMATIVE_AUTHORITY

CAPABILITY != AUTHORITY

CLAUDE_EXECUTION != CODEX_ASSURANCE

AGENT_CONSENSUS != HUMAN_AUTHORITY

NO_PAID_API != NO_GOVERNANCE

HANDOFF_REQUIRES_HUMAN_APPROVAL = true

DUAL_SSOT_AFTER_HANDOFF = forbidden

9. Estado

APPROVED. Esta decisão está incorporada ao próprio FLUXO COMPLETO DE DESENVOLVIMENTO — CEPRAEA BEACH PRO. O handoff entrega ao repositório o corpus local `.drive/**`; a nova modelagem de domínio será realizada no VS Code, revisada pelo Codex e somente depois homologada pela autoridade humana.

10. Refinamento posterior

DEC-SDLC-006 APPROVED refina, sem invalidar esta decisão, a ordem operacional do handoff. A sequência vigente na guia FLUXO é: SELEÇÃO HUMANA DE FONTES → CÓPIA PARA .drive/** → SOURCE_CORPUS_MANIFEST → HASH / PROVENANCE VALIDATION → SENSITIVITY CHECK → HUMAN VALIDATION → SOURCE_CORPUS_READY. Em caso de divergência de ordem, DEC-SDLC-006 prevalece. DEC-SDLC-003 e DEC-SDLC-004 refinam a etapa posterior de review e integração: o objeto revisado é identificado por REVIEW_TARGET_ID sobre a working tree não commitada; a autonomia dos agentes termina em READY_FOR_HUMAN_INTEGRATION; operações Git mutantes e release permanecem sob autoridade exclusiva de Davi. Nenhum diagrama genérico desta decisão autoriza Claude Code ou Codex a executar commit, push, merge, rebase, tag ou deploy.

DEC-SDLC-002

DEC-SDLC-002 — WORKFLOW DUAL-AGENT SEM GIT WORKTREES

STATUS: RASCUNHO

Decision authority: Davi Sermenho

Decision class: SDLC / GIT TOPOLOGY / DEV CONTAINER / REVIEW ARCHITECTURE

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Decisão

O fluxo do CEPRAEA BEACH PRO não utilizará Git worktrees como mecanismo de isolamento entre Claude Code e Codex. Em particular, não será criada nem exigida uma worktree irmã para o Reviewer.

Esta decisão é específica ao workflow atual:

1 Executor escritor — Claude Code

+

1 Reviewer read-only — Codex

+

1 autoridade humana de promoção Git — Davi Sermenho

Ela não declara Git worktrees inadequadas em qualquer arquitetura. Worktrees continuam sendo uma técnica válida em cenários com múltiplos agentes escritores paralelos, mas não integram este fluxo.

2. Distinção obrigatória de termos

GIT WORKTREE = checkout adicional criado e administrado por `git worktree`.

WORKING TREE = árvore de trabalho corrente do repositório, contendo inclusive alterações ainda não commitadas.

A decisão proíbe o uso de Git worktrees no workflow. Ela NÃO elimina a working tree. A working tree única e compartilhada é precisamente o objeto produzido pelo Executor e revisado pelo Reviewer.

3. Evidência histórica — falha na criação da worktree irmã

O desenho anterior exigia uma operação equivalente a:

`git worktree add -b feat/cepraea-domain-modeling ../cepraea-modelagem-canonica <BASE_SHA>`

Essa operação não modifica apenas arquivos de projeto. Ela cria branch/ref e altera metadados dentro de `.git`.

No Dev Container, `.git/refs/heads` estava read-only. Como `git worktree add -b` exige mutação de `.git`, Claude Code não possuía autoridade nem capacidade para executar a operação.

Sequência observada:

Claude Code

→ `git worktree add`

→ requer escrita em `.git`

→ `.git` read-only

→ BLOCKED

Alterar refs manualmente, liberar escrita em `.git` ou contornar a fronteira de permissões seria bypass do Control Plane e permanece proibido.

4. Evidência histórica — worktree criada pelo humano, mas invisível ao container

Davi criou corretamente a branch e a worktree no host. A topologia resultante era equivalente a:

`/home/davis/projetos/cepraea-beach-pro/`

`/home/davis/projetos/cepraea-modelagem-canonica/`

O Dev Container, porém, montava somente:

`/home/davis/projetos/cepraea-beach-pro`

→ `/workspaces/cepraea-beach-pro`

O diretório pai `/home/davis/projetos/` não era montado integralmente. Assim, a worktree irmã existia no host, mas não era alcançável pelas ferramentas do Executor dentro do container.

Corrigir esse desenho exigiria adicionar mount específico ou ampliar o mount do Dev Container, reabrindo alterações em `.devcontainer/**` e aumentando a superfície do Control Plane.

Sequência histórica:

worktree irmã obrigatória

→ Claude tenta criar

→ BLOCKED por `.git` read-only

→ Davi cria no host

→ worktree existe

→ sibling path não está montado no container

→ seria necessário alterar mounts / Control Plane

→ complexidade maior que o benefício

→ remover worktree irmã do workflow

5. Razão arquitetural principal

Mesmo que a limitação de mount fosse eliminada, uma segunda Git worktree não é o mecanismo adequado para o modelo dual-agent atual.

Claude Code deve produzir alterações ainda não commitadas. Codex deve revisar exatamente esse mesmo estado:

working tree

+

`git diff`

Uma segunda Git worktree baseada no mesmo HEAD não recebe automaticamente as alterações não commitadas da primeira.

Exemplo:

Working tree compartilhada pelo Executor:

`arquivo.ts` modificado, ainda sem commit.

Worktree Git separada baseada no mesmo HEAD:

`arquivo.ts` original.

Para sincronizar o estado seria necessário introduzir pelo menos um mecanismo adicional, como commit provisório, patch, rsync/cópia ou outra sincronização explícita. Esses mecanismos criariam estado intermediário, nova proveniência operacional e uma state machine adicional sem benefício proporcional para este workflow.

6. Topologia adotada

Claude Code e Codex observam a mesma árvore física do repositório.

MESMA WORKING TREE

├─ Claude Code / contexto Executor: workspace RW dentro do WRITE_SCOPE autorizado

└─ Codex / contexto Reviewer: workspace read-only para o objeto revisado

As alterações reais do Executor permanecem imediatamente visíveis ao Reviewer pelo mesmo filesystem e pelo `git diff`, sem commit intermediário e sem cópia entre checkouts.

Fluxo:

Claude Code

→ modifica a working tree autorizada

→ executa Shift-Left

→ produz evidência

→ entrega estado revisável

→ Codex lê a mesma working tree

→ inspeciona `git diff` e evidências

→ PASS | FAIL | HUMAN_DECISION_REQUIRED

→ Davi decide e executa as operações Git reservadas

7. Autoridade Git

A remoção de worktrees não amplia a autoridade dos agentes.

Claude Code não recebe autoridade para criar branch, alterar refs, executar `git worktree`, commit, push, merge ou rebase.

Codex permanece Reviewer read-only e não modifica silenciosamente o objeto avaliado.

Operações Git mutantes reservadas continuam sob autoridade de Davi Sermenho conforme o Control Plane.

8. Invariantes

GIT_WORKTREE_IN_WORKFLOW = false

SIBLING_WORKTREE_REQUIRED = false

SHARED_PHYSICAL_WORKING_TREE = true

CLAUDE_WRITER = true

CODEX_REVIEWER_READ_ONLY = true

REVIEW_TARGET = SAME_UNCOMMITTED_WORKING_TREE

TEMPORARY_COMMIT_FOR_REVIEW = forbidden

PATCH_SYNC_FOR_REVIEW = not_required

RSYNC_SYNC_FOR_REVIEW = not_required

AGENT_GIT_REF_MUTATION = forbidden

CONTROL_PLANE_BYPASS = forbidden

9. Consequências

O workflow fica menor e mais verificável porque elimina:

- criação e manutenção de worktree irmã;

- mount adicional para sibling path;

- sincronização de alterações não commitadas entre checkouts;

- commit provisório apenas para transporte ao Reviewer;

- patch/cópia como mecanismo de handoff;

- estado intermediário adicional de sincronização.

A independência entre Executor e Reviewer é preservada por separação de papel, permissões e autoridade, não por checkout Git separado.

10. Estado

APPROVED. Esta decisão deve ser refletida na guia FLUXO. Qualquer futura introdução de Git worktrees neste workflow constitui mudança material de topologia do SDLC e requer nova decisão humana explícita.

DEC-SDLC-003

DEC-SDLC-003 — IDENTIDADE E ESTABILIDADE DO OBJETO DE REVIEW

STATUS: RASCUNHO

Decision authority: Davi Sermenho

Decision class: SDLC / ASSURANCE / REVIEW INTEGRITY

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Decisão

O objeto revisado pelo Codex é a mesma working tree não commitada produzida pelo Claude Code, conforme DEC-SDLC-002. REVIEW_TARGET_SHA não identifica esse estado e deixa de ser utilizado como identidade do objeto antes do commit.

A identidade do estado revisável é REVIEW_TARGET_ID, derivada deterministicamente de:

BASE_COMMIT_SHA

+ TRACKED_DIFF_HASH

+ STAGED_DIFF_HASH

+ UNTRACKED_CONTENT_MANIFEST_HASH

+ SOURCE_CORPUS_MANIFEST_HASH, quando a tarefa depender do corpus.

2. Freeze de review

READY_FOR_REVIEW

↓

calcular REVIEW_TARGET_ID

↓

EXECUTOR_WRITE_FREEZE

↓

CODEX REVIEW

↓

recalcular REVIEW_TARGET_ID

REVIEW_TARGET_ID_BEFORE == REVIEW_TARGET_ID_AFTER → review válido.

REVIEW_TARGET_ID_BEFORE != REVIEW_TARGET_ID_AFTER → REVIEW_INVALIDATED.

A invalidação se aplica a qualquer mutação do objeto revisado, independentemente de ter sido produzida por Claude Code, Davi, formatter, hook ou outro processo.

3. Preservação na promoção Git

Após o PASS e antes de preservar a cobertura do review sobre o commit, deve ser demonstrável que COMMITTED_CONTENT == REVIEWED_CONTENT. Se o conteúdo efetivamente commitado divergir do conteúdo revisado, o review anterior não cobre o novo estado e REVIEW_REQUIRED_AGAIN.

4. Invariantes

REVIEW_TARGET = SAME_UNCOMMITTED_WORKING_TREE

REVIEW_TARGET_SHA_BEFORE_COMMIT = forbidden

REVIEW_TARGET_ID_REQUIRED = true

REVIEW_MUTATION_DURING_REVIEW = forbidden

CHANGED_REVIEW_TARGET_INVALIDATES_PASS = true

COMMITTED_CONTENT_MUST_EQUAL_REVIEWED_CONTENT = true

5. Precedência

Enquanto a guia FLUXO não estiver reconciliada, esta decisão APPROVED prevalece sobre qualquer redação anterior conflitante relativa a REVIEW_TARGET_SHA, identidade do estado revisado ou preservação da cobertura do review.

DEC-SDLC-004

DEC-SDLC-004 — FRONTEIRA DA AUTONOMIA AGÊNTICA E INTEGRAÇÃO GIT HUMANA

STATUS: RASCUNHO

Decision authority: Davi Sermenho

Decision class: SDLC / AUTHORITY / GIT / LIFECYCLE

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Decisão

Claude Code e Codex não integram alterações ao Git. A autonomia dos agentes termina em READY_FOR_HUMAN_INTEGRATION.

Claude Code = Executor e único agente escritor.

Codex = Reviewer read-only.

Davi Sermenho = autoridade exclusiva de promoção Git e release.

2. Operações reservadas a Davi

branch creation

commit

push

merge

rebase

tag

deploy

secret manipulation

release promotion

3. Sequência de integração

CODEX PASS

↓

READY_FOR_HUMAN_INTEGRATION

FIM DA AUTONOMIA AGÊNTICA

DAVI

↓

COMMIT

↓

VERIFY COMMITTED_CONTENT == REVIEWED_CONTENT

↓

PUSH

↓

CI

↓

CI PASS

↓

MERGE

↓

POST-MERGE VERIFICATION / BUILD

↓

DEPLOY / RELEASE

4. Definition of Done em camadas

EXECUTOR_DONE = implementação concluída + Shift-Left concluído + evidência materializada + READY_FOR_REVIEW.

AGENTIC_TASK_DONE = review Codex concluído + PASS ou decisão humana requerida resolvida + REVIEW_TARGET preservado + READY_FOR_HUMAN_INTEGRATION.

CHANGE_INTEGRATED = commit humano + preservação do conteúdo revisado + CI PASS + merge humano.

RELEASE_DONE = release autorizado + deploy + verificação pós-release.

5. Invariantes

AGENT_BRANCH_CREATE = forbidden

AGENT_COMMIT = forbidden

AGENT_PUSH = forbidden

AGENT_MERGE = forbidden

AGENT_REBASE = forbidden

AGENT_DEPLOY = forbidden

AGENT_AUTONOMY_END = READY_FOR_HUMAN_INTEGRATION

6. Precedência

Enquanto a guia FLUXO não estiver reconciliada, esta decisão APPROVED prevalece sobre redação anterior que atribua integração Git, commit, push, merge, rebase, deploy ou promoção de release aos agentes.

DEC-DOM-001

DEC-DOM-001 — CADEIA DE PROMOÇÃO E VALIDAÇÃO DO DOMÍNIO

STATUS: RASCUNHO

Decision authority: Davi Sermenho

Decision class: DOMAIN MODELING / EPISTEMOLOGY / DDD

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Decisão

A nova modelagem do CEPRAEA BEACH PRO será construída no repositório a partir do corpus local, sem promoção direta de fonte para modelo lógico ou regra canônica.

Cadeia obrigatória:

SOURCE CORPUS

↓

SRC

↓

EVD

↓

TERMO / REGRA

↓

CANDIDATO

↓

RECONCILIAÇÃO

↓

ELEMENTO DE DOMÍNIO PROPOSTO

↓

CODEX — SEMANTIC REVIEW

↓

DAVI

↓

VALIDADO | REJEITADO

↓

DOMAIN BASELINE

↓

MATURITY GATE

↓

MODELO LÓGICO

↓

INVARIANTES

↓

REQUISITOS

2. Promoções proibidas

SOURCE → LOGICAL_MODEL = forbidden

SOURCE → CANONICAL_RULE = forbidden

INFERENCE → VALIDATED_DOMAIN_ELEMENT = forbidden

CODE_EXISTING → DOMAIN_TRUTH = forbidden

3. Eixos semânticos independentes

ASSERTION_KIND = FATO | DECLARACAO | PLANO | DECISAO | DERIVACAO | INFERENCIA.

EPISTEMIC_STATE = OBSERVADO | INFERIDO | AMBIGUO | CONFLITANTE | VALIDADO | REJEITADO.

MATURITY_STATE = IMATURA | PARCIALMENTE_MADURA | MADURA_PARA_MODELO_LOGICO.

EPISTEMIC_STATE = VALIDADO requer aprovação humana real por Davi Sermenho. PASS do Codex não equivale a VALIDADO.

4. Canonicalidade

Antes da homologação humana, as asserções permanecem no ASSERTION_REGISTRY. Somente o resultado homologado da modelagem pode formar a EXECUTION_DOMAIN_BASELINE. O termo CANONICAL não deve ser aplicado antecipadamente a conteúdo ainda proposto ou não validado.

5. Precedência

Enquanto a guia FLUXO não estiver reconciliada, esta decisão APPROVED prevalece sobre sequências anteriores que permitam asserção/fonte → modelo lógico antes da validação humana e do maturity gate.

DEC-SEC-001

DEC-SEC-001 — SOURCE CORPUS, PRIVACIDADE E ISOLAMENTO DO REVIEWER

STATUS: RASCUNHO

Decision authority: Davi Sermenho

Decision class: SECURITY / PRIVACY / SOURCE GOVERNANCE / REVIEW ISOLATION

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Source Corpus

.drive/BEACHHANDBALL/** = corpus externo do domínio.

.drive/CEPRAEA-BEACH-PRO/** = corpus interno da realidade operacional.

A presença em .drive/** significa seleção para inspeção/modelagem, não autoridade normativa automática.

2. Secrets

SECRETS_IN_AGENT_CONTEXT = forbidden.

Credenciais, tokens, chaves privadas e equivalentes não podem integrar o contexto dos agentes.

3. PII operacional

PII operacional pode ser consumida somente quando necessária para a tarefa, dentro do READ_SCOPE autorizado e quando não existir alternativa menos sensível suficiente para cumprir a finalidade. Informação pessoal que não contribui para a tarefa deve ser minimizada ou pseudonimizada.

Wellness e outros dados sensíveis devem possuir classificação explícita de sensibilidade e obedecer ao princípio de minimização.

4. Testes

REAL_OPERATIONAL_DATA_IN_TESTS = forbidden.

TEST_DATA = SYNTHETIC / MOCK.

5. Integridade do corpus

O corpus é acompanhado por SOURCE_CORPUS_MANIFEST contendo, no mínimo:

source_corpus_id

relative_path

source_id/origin

sha256

size

mime/type

captured_at

selected_by

sensitivity_class

Antes da modelagem, a integridade do corpus deve ser validada contra o manifesto. Divergência produz SOURCE_CORPUS_CHANGED → REVALIDATION_REQUIRED.

6. Codex read-only

CODEX_WRITE_SCOPE = ∅.

O estado read-only deve ser tecnicamente demonstrável, não apenas instruído linguisticamente. Controles mínimos devem demonstrar:

read file → allowed

git diff/status → allowed

write file → denied

git mutation → denied

7. Precedência

Enquanto a guia FLUXO não estiver reconciliada, esta decisão APPROVED prevalece sobre redação anterior que proíba indiscriminadamente toda PII operacional do contexto dos agentes ou que trate o read-only do Reviewer apenas como recomendação narrativa.

DEC-SDLC-005

DEC-SDLC-005 — CONTRATO DA TAREFA, RISCO E CRITÉRIOS OBJETIVOS DE ASSURANCE

STATUS: RASCUNHO

Decision authority: Davi Sermenho

Decision class: SDLC / TASK GOVERNANCE / RISK / ASSURANCE

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Contrato mínimo da tarefa

Nenhum trabalho de escrita do Claude Code começa sem contrato de tarefa definido.

Campos mínimos:

TASK_ID

TASK_TYPE

OBJECTIVE

RISK_LEVEL

WORK_BRANCH

BASE_COMMIT_SHA

READ_SCOPE

WRITE_SCOPE

FORBIDDEN_OPERATIONS

EXECUTOR

REVIEWER

DOMAIN_BASELINE_REF

REQUIREMENTS[]

INVARIANTS[]

ACCEPTANCE_CRITERIA[]

EXPECTED_EVIDENCE[]

Para modelagem fundacional, SOURCE_CORPUS_ID também é obrigatório.

2. Matriz de risco

RISK_LEVEL = GREEN | YELLOW | RED | RED_CRITICAL.

Expressões como “proporcional ao risco”, “evidência suficiente”, “testes adequados”, “mudança material” e “invariante crítica” não podem depender de interpretação livre do agente. A matriz de risco deve determinar, por nível:

PLAN_REQUIRED

HUMAN_PRE_GATE_REQUIRED

CODEX_REVIEW_REQUIRED

REQUIRED_TEST_CLASSES

REQUIRED_EVIDENCE

WRITE_SCOPE_POLICY

CONTROL_PLANE_GATE

RELEASE_GATE

3. Semântica objetiva de PASS

PASS somente pode ser emitido quando:

verification_status = COMPLETED;

todos os acceptance criteria requeridos estiverem DEMONSTRATED;

todas as invariantes aplicáveis estiverem PRESERVED;

unauthorized_change_count = 0;

review_target_unchanged = true.

absence_of_detected_error != PASS.

Se existir claim obrigatório não verificado, PASS é proibido.

4. Precedência

Enquanto a guia FLUXO não estiver reconciliada, esta decisão APPROVED prevalece sobre redação anterior que permita iniciar escrita sem WRITE_SCOPE ou que faça gates/verdicts dependerem apenas de termos subjetivos não vinculados à matriz de risco.

DEC-SDLC-006

DEC-SDLC-006 — MÁQUINA DE ESTADOS, HANDOFF E GATES DE EXECUÇÃO

STATUS: RASCUNHO

Decision authority: Davi Sermenho

Decision class: SDLC / PROCESS MODEL / STATE MACHINE / EXECUTION GATES

← [FLUXO](https://docs.google.com/document/d/1PNpn_oCCFGlsvuDd-KsvzeL4hoGpvM5IlQ91d2In3o8/edit)

1. Dimensões de estado

O fluxo distingue explicitamente:

PROCESS_PHASE

WORK_ITEM_STATE

MODELING_STATE

EPISTEMIC_STATE

MATURITY_STATE

VERIFICATION_STATUS

ASSURANCE_VERDICT

POLICY_EVALUATION_RESULT

Essas dimensões não são intercambiáveis.

2. Sequência oficial do handoff

GOOGLE DRIVE

↓

SELEÇÃO HUMANA DE FONTES

↓

CÓPIA PARA .drive/**

↓

SOURCE_CORPUS_MANIFEST

↓

HASH / PROVENANCE VALIDATION

↓

SENSITIVITY CHECK

↓

HUMAN VALIDATION

↓

SOURCE_CORPUS_READY

Outras variantes de ordem devem ser removidas do FLUXO.

3. Tarefa fundacional obrigatória

SOURCE_CORPUS_READY não autoriza escrita automaticamente.

SOURCE_CORPUS_READY

↓

FOUNDATIONAL_DOMAIN_MODELING_TASK

↓

TASK DEFINITION

↓

RISK CLASSIFICATION

↓

READ_SCOPE + WRITE_SCOPE

↓

AUTHORIZED

↓

CONTEXT_LOADING

↓

REPOSITORY + CORPUS INSPECTION

↓

DOMAIN MODELING

4. MODELING_STATE

SOURCE_CORPUS_READY

DOMAIN_DISCOVERY_IN_PROGRESS

MODEL_PROPOSAL_READY_FOR_REVIEW

MODEL_IN_REVIEW

MODEL_CORRECTION_REQUIRED

MODEL_READY_FOR_HUMAN_VALIDATION

EXECUTION_DOMAIN_BASELINE_READY

5. WORK_ITEM_STATE

REQUESTED

DEFINED

AUTHORIZED

IN_EXECUTION

READY_FOR_REVIEW

IN_REVIEW

CORRECTION_REQUIRED

REVIEW_INVALIDATED

READY_FOR_HUMAN_INTEGRATION

INTEGRATED

READY_FOR_RELEASE

RELEASED

BLOCKED

REJECTED

INTEGRATED = HUMAN_ONLY.

READY_FOR_RELEASE = HUMAN_CONTROLLED.

RELEASED = HUMAN_ONLY.

6. Physical Stop Gate

Após a classificação da tarefa:

PHYSICAL_IMPACT?

├─ NO → continuar

└─ YES

↓

PHYSICAL_STOP_GATE

├─ CLOSED → BLOCKED

└─ OPEN

↓

inspect actual schema

↓

physical planning

O agente não pode abrir implicitamente o PHYSICAL_STOP_GATE.

7. Precedência

Enquanto a guia FLUXO não estiver reconciliada, esta decisão APPROVED prevalece sobre sequências de handoff, estados ou posicionamento de gates incompatíveis com esta decisão.