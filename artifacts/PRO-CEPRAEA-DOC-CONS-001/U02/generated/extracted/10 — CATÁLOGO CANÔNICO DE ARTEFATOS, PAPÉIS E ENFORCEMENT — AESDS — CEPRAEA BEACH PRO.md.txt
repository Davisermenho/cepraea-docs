00 — Visão geral

Catálogo canônico de artefatos do SDLC agêntico — CEPRAEA BEACH PRO

Finalidade

Este documento consolida, em uma única referência navegável, a definição, o papel, a autoridade, o path, a configuração, as relações e os critérios de verificação dos artefatos que materializam o desenvolvimento assistido por agentes do CEPRAEA BEACH PRO. Ele não substitui os arquivos do repositório. Sua função é explicar o que cada arquivo é, por que existe, qual camada do sistema de engenharia ocupa e como deve ser interpretado sem confundir documentação, política, procedimento, enforcement, observabilidade e evidência.

Escopo

O escopo é o SDLC agêntico utilizado no desenvolvimento do CEPRAEA BEACH PRO. O runtime utilizado por atletas e treinador permanece fora deste catálogo. Claude Code e Codex são tratados como agentes de desenvolvimento integrados ao VS Code; o produto continua concebido para operar sem dependência de LLM em produção.

Domínios de conhecimento envolvidos

A arquitetura cruza Engenharia de Software, Software Architecture, Requirements Engineering, Specification Engineering, Software Assurance, DevSecOps, Platform Engineering, Configuration Management, AI Governance, Human-in-the-Loop Governance, Zero-Trust/Least-Privilege e Observability. Nenhum desses subdomínios, isoladamente, explica todos os arquivos. A taxonomia adotada neste catálogo classifica cada artefato pela função dominante que exerce.

Classes de artefato

ARCHITECTURE: descreve estruturas, responsabilidades, limites e relações de alto nível.

GOVERNANCE_POLICY: define autoridade, invariantes, permissões conceituais e separação de funções.

ROLE_CONTRACT: especializa a política para um papel agêntico permanente.

TASK_SPECIFICATION: transforma intenção humana em contrato de trabalho verificável.

RUNBOOK: descreve procedimento reutilizável para uma classe de operação.

ENFORCEMENT: impede ou restringe tecnicamente uma ação.

ENVIRONMENT_AS_CODE: materializa a fronteira operacional do ambiente.

VERIFIER: mede propriedades observáveis e produz PASS/FAIL reproduzível.

OBSERVABILITY: registra eventos ou estado para inspeção posterior sem decidir autorização.

AUDIT_ANALYSIS: analisa evidências, identifica lacunas e recomenda mudanças; não se torna autoridade apenas por existir.

HISTORICAL_SNAPSHOT: preserva estado anterior para rastreabilidade e comparação.

Regra de precedência conceitual

Autoridade humana → política comum → fontes canônicas de domínio/arquitetura → contratos de papel → task/plan aprovado → runbook aplicável → execução concreta. Mecanismos técnicos de enforcement operam em paralelo à execução e materializam os limites que podem ser aplicados deterministicamente. Evidência observada nunca é substituída por narrativa do agente.

Regra epistemológica

DECIDIDO não significa IMPLANTADO. IMPLANTADO não significa VALIDADO. DOCUMENTADO não significa ENFORCED. RELATADO não significa COMPROVADO. PASS sem oráculo de aceitação ou sem evidência verificável não deve ser tratado como prova. UNKNOWN, MISSING e UNVERIFIED não equivalem a PASS.

Paths e vigência

Quando um path foi comprovado pelo material do repositório, ele é registrado como path canônico. Quando o arquivo recebido é um snapshot, um exemplo, um artefato histórico ou existe evidência de evolução posterior, a guia correspondente registra explicitamente essa condição. O objetivo é impedir que um nome de arquivo fora de contexto se transforme em falsa fonte de autoridade.

Relação com o SYMBOL_REGISTRY

O catálogo explica os arquivos; o SYMBOL_REGISTRY deverá explicar o vocabulário normativo usado por esses arquivos. Termos como TASK, EXECUTOR, REVIEWER, BASELINE, WRITE_SCOPE, EVIDENCE, READY_FOR_REVIEW, PASS, FAIL, BLOCKED e HUMAN_DECISION_REQUIRED devem possuir definição canônica única, tipo, semântica, origem, consumidores, predicados e mapeamento para ações verificáveis. O catálogo é a ontologia dos artefatos; o SYMBOL_REGISTRY será o léxico formal compartilhado entre eles.

Revisão de conformidade

STATUS DO ARTEFATO: REFERENCE_CATALOG / NON_NORMATIVE.

BASELINE AUDITADA: cepraea/beach-pro main @ ecef4f1be987471f23a9ed712597f701ad1b3f64.

Este Google Docs é canônico apenas como catálogo explicativo desta revisão; ele não supera AGENT_POLICY.md, fontes arquiteturais, decisões materiais, task/plan, runbooks ou arquivos de enforcement do repositório. A guia 25 registra findings e o status individual de cada guia.

01 — Arquitetura-mãe

Human-Governed Dual-Agent SDLC Architecture.md

Identidade

Path canônico comprovado: docs/arquiteturas/multi-agentes/Human-Governed Dual-Agent SDLC Architecture.md.

Classe: ARCHITECTURE.

Domínio principal: Software Architecture aplicada a Agentic Software Engineering.

Formato arquitetural declarado: arc42.

Autoridade: fonte arquitetural de alto nível do fluxo multiagente e do Dev Container; não é o runtime funcional do PWA.

Definição

É o documento que descreve a arquitetura-mãe do processo de desenvolvimento assistido por agentes. Ele estabelece os building blocks, responsabilidades, fronteiras de confiança, canais de handoff, princípios de qualidade, deployment view, runtime view do SDLC e restrições arquiteturais. Sua unidade de análise é o sistema de engenharia que produz o software, e não as funcionalidades de negócio utilizadas pelas atletas.

Objetivos

Preservar autoridade humana sobre domínio, decisões materiais, Git privilegiado, release e deploy; separar produção, revisão e aprovação; definir Claude Code como Executor e Codex como Reviewer independente; usar Git como estado operacional e handoff; exigir validações determinísticas antes do julgamento por LLM; limitar privilégios por papel; proteger fontes, secrets e control plane; manter o runtime do CEPRAEA independente dos agentes.

Esqueleto lógico

Introduction and Goals → Architecture Constraints → Context and Scope → Solution Strategy → Building Block View → Runtime View → Deployment View → Cross-cutting Concepts → decisões, riscos e propriedades operacionais. O valor do arquivo está na coerência entre essas visões: a mesma separação de funções precisa aparecer nos papéis, na infraestrutura e no fluxo de estados.

Papel na arquitetura

Este arquivo responde “qual sistema de desenvolvimento estamos construindo?”. Ele não deveria conter minúcia repetitiva de cada tarefa, nem substituir o contrato de papel do Claude/Codex, nem executar enforcement. Ele fornece as invariantes arquiteturais que os artefatos inferiores devem realizar.

Elementos canônicos extraídos

HUMAN = autoridade de domínio/release/Git privilegiado.

EXECUTOR = Claude Code, produtor de alterações.

REVIEWER = Codex, verificador independente.

Git = state machine operacional, diff de handoff, histórico e identidade material da mudança.

Deterministic validators = lint, typecheck, testes, schemas, referências, git diff --check e checks específicos.

Execution plane ≠ assurance plane ≠ approval authority.

Relações

AGENT_POLICY.md concretiza as invariantes comuns de governança. CLAUDE.md e AGENTS.md especializam os papéis. Runbooks acrescentam procedimentos por classe de operação. Dockerfile, Dev Containers, managed settings, requirements e guards materializam limites técnicos. Scripts de verificação testam propriedades do ambiente. A arquitetura é, portanto, uma fonte de desenho e restrição, não um log de execução.

O que este arquivo NÃO prova

A existência do documento não prova que o container está corretamente construído; não prova que o Claude esteja efetivamente bloqueado; não prova que o Codex esteja read-only; não prova que os testes tenham passado; não prova que o fluxo end-to-end esteja implantado. Essas propriedades exigem evidência de configuração e runtime.

Risco de interpretação incorreta

O risco central é confundir “arquitetura desejada/aprovada” com “estado operacional comprovado”. Outro risco é usar o documento como justificativa para decisões não registradas ou para criar infraestrutura adicional que contrarie o princípio de simplicidade do próprio desenho.

Mapeamento para SYMBOL_REGISTRY

É fonte primária para ROLE, ENTITY, RELATION, ARCHITECTURAL_CONSTRAINT e estados de alto nível. Símbolos derivados deste documento devem apontar para predicados verificáveis em artefatos inferiores; por exemplo, REVIEWER_READ_ONLY só é operacionalmente verdadeiro quando mapeado a configuração e teste concretos.

Revisão de conformidade — drift arquitetural identificado

STATUS: AJUSTE NECESSÁRIO NA FONTE ARQUITETURAL.

A revisão arquitetural auditada contém premissas que não coincidem com main: descreve .git como não montado read-only e o desenho anterior de um único Dev Container, enquanto o as-built possui .git read-only no Executor e um Dev Container dedicado ao Reviewer. DEC-CTR-013 e DEC-CTR-015 registram a intenção de superseder essas premissas, porém ambos estão com Status da decisão = PROPOSTA por ausência de artefato verificável de aprovação. Portanto, a implementação atual não deve ser usada para fingir que a arquitetura documental já foi formalmente reconciliada. Classificação correta: ARCHITECTURE_WITH_KNOWN_DRIFT + AS_BUILT_DIVERGENCE.

02 — Materialização

Arquivos-Human-Governed Dual-Agent SDLC Architecture.md

Identidade

Path canônico comprovado: docs/arquiteturas/multi-agentes/Arquivos-Human-Governed Dual-Agent SDLC Architecture.md.

Classe: ARCHITECTURE_REALIZATION / CONFIGURATION_BLUEPRINT.

Domínio principal: Architecture Realization, Configuration Architecture e DevSecOps design.

Definição

É o documento de materialização da arquitetura. Enquanto a arquitetura-mãe define responsabilidades e limites abstratos, este arquivo responde quais artefatos concretos devem existir para realizar essas responsabilidades. Ele faz a ponte entre “o sistema deve ter separação de funções e least privilege” e “quais arquivos, configurações, scripts e diretórios implementam isso”.

Objetivo

Transformar decisões arquiteturais em um inventário implementável de arquivos e responsabilidades sem fazer o erro de tratar documentação como enforcement. O documento separa explicitamente artefatos de comportamento/governança dos artefatos de enforcement/verificação técnica.

Estrutura conceitual

Governança: AGENT_POLICY.md.

Adaptadores de papel: CLAUDE.md e AGENTS.md.

Configuração do Reviewer: configuração Codex/requirements e Dev Container específico quando aplicável.

Configuração do Executor: managed settings, hooks e guard.

Fronteira de ambiente: Dockerfile e devcontainer.json.

Verificação: verify-agent-environment.sh e acceptance tests reais.

Runbooks: biblioteca compartilhada, executor e reviewer.

Papel na arquitetura

É o “mapa arquitetura → arquivos”. Ele deve permitir responder, para cada requisito arquitetural, qual artefato é responsável por defini-lo e qual artefato é responsável por aplicá-lo. Isso evita concentração indevida de responsabilidades e reduz duplicação normativa.

Regra de decomposição

Política define o que é permitido e quem tem autoridade. Contrato de papel define o comportamento transversal do agente. Runbook define o procedimento especializado. Enforcement aplica limites técnicos. Verificador observa propriedades. Relatório de auditoria interpreta evidências. Um arquivo não deve absorver funções de outro apenas por conveniência.

Paths relevantes consolidados

AGENT_POLICY.md; CLAUDE.md; AGENTS.md; runbooks/**; docs/operacao/agent-workflow.md; docs/modelagem/**; .devcontainer/control-plane/**; .devcontainer/guards/**; .devcontainer/scripts/**; .devcontainer/devcontainer.json; .devcontainer/reviewer/devcontainer.json; .devcontainer/Dockerfile.

Relação com a realidade observada

O documento histórico de materialização cita nove arquivos nucleares e posteriormente incorpora a arquitetura de runbooks. Parte de seus exemplos conceituais foi adaptada no repositório real: o usuário efetivo é agent, os paths de control-plane e guards possuem nomes concretos e existe Dev Container específico de Reviewer. Portanto, exemplos internos não devem superar o estado real comprovado do repositório.

O que este arquivo NÃO é

Não é acceptance test. Não é prova de implantação. Não é o próprio managed settings. Não é o próprio guard. Não deve ser lido como se blocos de exemplo fossem automaticamente a configuração vigente.

Critério de correção

Uma afirmação de materialização só é forte quando existe correspondência entre requisito arquitetural, path real, conteúdo do arquivo e teste/observação compatível. Quando um desses elos faltar, o estado deve permanecer proposto, decidido ou pendente conforme o caso.

Mapeamento para SYMBOL_REGISTRY

É fonte para RESOURCE_BINDING e RUNTIME_MAPPING: relaciona um símbolo abstrato, como EXECUTOR_GIT_MUTATION_DENIED, aos artefatos que deveriam materializá-lo, como managed settings, pretool e fronteiras do container.

Revisão de conformidade

STATUS: PARTIALLY_SUPERSEDED_BLUEPRINT.

A afirmação original de “nove arquivos” é um baseline histórico de materialização, não o inventário vigente. main contém, além dos artefatos nucleares, dois Dev Containers, biblioteca runbooks/, .ai/control/, decisões .ai/decisions/, managed MCP e outros controles. O documento continua útil para rastrear intenção de realização arquitetural, mas paths e contagens devem ser confirmados no repositório corrente antes de qualquer execução.

03 — Implantação

Implantação-Human-Governed Dual-Agent SDLC Architecture.md

Identidade

Path canônico comprovado: docs/arquiteturas/multi-agentes/Implantação-Human-Governed Dual-Agent SDLC Archite.md.

Classe: ARCHITECTURE_TRANSITION / DEPLOYMENT_ACCEPTANCE_PLAN.

Domínio principal: Architecture Transition, Platform Deployment, Verification & Validation e Operational Readiness.

Definição

É o artefato que descreve como sair do desenho arquitetural aprovado e chegar a uma arquitetura realmente utilizável. Sua pergunta central não é “como deve ser?”, mas “quais ações e quais provas tornam legítimo dizer que está implantado?”.

Objetivo

Materializar arquivos, configurar os agentes reais, reconstruir o Dev Container quando necessário, executar verificações do perfil BASE, realizar testes comportamentais dos agentes e completar um fluxo end-to-end Claude → validações → Codex → decisão humana → Git.

Modelo de maturidade implícito

Documentado → materializado → configurado → executado → verificado → validado end-to-end. O arquivo enfatiza que presença de arquivo não equivale a funcionamento e que parte das propriedades só pode ser comprovada executando o processo real do agente.

Acceptance tests

O documento usa CTs para diferenciar propriedades estáticas, propriedades de ambiente e propriedades comportamentais. Exemplos de categorias: usuário não-root; Docker socket ausente; secrets ausentes; corpus read-only; humano capaz de editar e operar Git; Claude capaz de editar apenas targets autorizados; Claude bloqueado em control plane/Git privilegiado; Codex capaz de ler o diff e impedido de alterar o projeto; fluxo end-to-end comprovado.

Papel arquitetural

É a ponte entre Architecture Definition e Operational Evidence. Ele deveria produzir condições de readiness, não repetir toda a arquitetura. Seu valor está na Definition of Done e na identificação explícita de testes que scripts estáticos não podem substituir.

Risco de falso positivo

Marcar um CT como PASS por leitura de configuração quando o requisito exige comportamento real do agente. Exemplo: verificar que existe uma regra de deny não é igual a executar uma tentativa real e observar o bloqueio. A disciplina correta é associar cada CT a um oráculo adequado.

Relações

Consome a arquitetura-mãe e o blueprint de arquivos; depende de Dockerfile, devcontainers, managed settings, requirements, guards e verificadores; produz evidência para decidir se a arquitetura está operacional. Também registra migração do workflow antigo para Git como state machine e evita duas autoridades operacionais concorrentes.

Status e historicidade

O documento contém trechos historicamente superados e notas que registram que determinadas lacunas já foram fechadas. Esses trechos devem ser preservados como rastreabilidade, mas não usados como ordem atual quando uma decisão posterior e canônica os substituiu.

Mapeamento para SYMBOL_REGISTRY

É fonte para PRECONDITION, POSTCONDITION, ACCEPTANCE_ORACLE, EVIDENCE_REQUIREMENT e TRANSITION. Símbolos como BASE_READY ou DELIVERY_ELIGIBLE só devem ser definidos se seus predicados puderem ser avaliados por evidência real.

Revisão de conformidade — estado probatório registrado na própria fonte

STATUS: OPERATIONAL_READINESS_NOT_PROVEN_GLOBALLY.

No documento de implantação auditado, CT-01, CT-02, CT-03, CT-07, CT-08 e CT-11 aparecem como PASS; CT-10 é sustentado por leitura estática, não por tentativa ao vivo naquela sessão; CT-04 e CT-09 aparecem como FALHOU; CT-05, CT-06 e os testes Codex/fluxo end-to-end permanecem pendentes no registro. Esses resultados são históricos e devem ser reexecutados quando a configuração muda. Não converter presença de arquivos atuais em DoD global concluída.

04 — AGENT_POLICY.md

AGENT_POLICY.md

Identidade

Path canônico: AGENT_POLICY.md, na raiz do repositório.

Classe: GOVERNANCE_POLICY.

Domínio principal: AI Governance, Policy Engineering, Separation of Duties e Human-in-the-Loop Governance.

Autoridade: constituição comum do fluxo; subordinada à autoridade humana e às fontes canônicas de domínio/arquitetura, superior aos contratos específicos de papel e runbooks.

Definição

É a política normativa comum a Claude Code e Codex. Não descreve uma tarefa específica e não deve funcionar como manual detalhado de cada operação. Seu papel é fixar invariantes estáveis: quem pode decidir, quem executa, quem revisa, o que é Git privilegiado, quais áreas pertencem ao control plane, como tratar falta de permissão, como lidar com evidência e quando escalar ao humano.

Objetivos

Impedir autoaprovação; separar produção, revisão e aprovação; manter Davi como autoridade final; impedir avanço automático; limitar Git dos agentes à inspeção; proteger control plane, fontes operacionais e secrets; exigir deterministic first; proibir bypass; estabelecer estados de escalonamento; preservar evidência material sem criar uma state machine paralela ao Git.

Vocabulário operacional

EXECUTOR = Claude Code.

REVIEWER = Codex.

HUMAN = autoridade final sobre domínio, decisões materiais, Git, release e deploy.

READY_FOR_REVIEW/BLOCKED pertencem ao Executor.

PASS/FAIL/HUMAN_DECISION_REQUIRED pertencem ao Reviewer.

Git é state machine e mecanismo de handoff.

Autoridade sobre Git

Agentes podem inspecionar com operações como status, diff, log, show, rev-parse e ls-files. Operações que alterem index, refs, histórico ou estado remoto pertencem ao humano, incluindo add, commit, push, pull, merge, rebase, cherry-pick, reset, restore, checkout, switch, worktree, stash, clean, update-ref e equivalentes.

Control plane

AGENT_POLICY.md, CLAUDE.md, AGENTS.md, .devcontainer/**, .claude/**, .codex/**, workflows de CI, runbooks quando classificados como protegidos, scripts de CI, hooks, policies administradas, secrets e credenciais. Alterações nesses alvos exigem tarefa humana explicitamente direcionada a infraestrutura/política.

Natureza normativa versus técnica

A frase “Claude não pode fazer commit” é uma norma. O bloqueio efetivo deve ser materializado por managed settings, guard, mounts, isolamento de identidade e outros controles. AGENT_POLICY.md influencia comportamento e cria autoridade normativa, mas não é, sozinho, uma fronteira de segurança.

Relações

CLAUDE.md adapta a política ao Executor. AGENTS.md adapta a política ao Reviewer. runbooks/** especializam procedimentos. task_atomics.md usa a taxonomia de risco e o modelo de autoridade. Managed settings e codex requirements implementam parte das restrições. pretool fornece fail-fast. Verificadores produzem evidência de presença/estado.

O que NÃO deve conter

Detalhes efêmeros de uma task; listas enormes de comandos de uma única feature; resultados de um review específico; logs de cada interação; suposições de domínio não aprovadas; configurações técnicas voláteis que pertençam aos arquivos de enforcement.

Riscos de manutenção

Duplicação de regras nos adaptadores; divergência entre política e enforcement; regra normativa mais forte do que a capacidade técnica; listas de control plane desatualizadas; confusão entre read-only para integridade e confidencialidade de dados.

Mapeamento para SYMBOL_REGISTRY

É fonte normativa primária para ROLE, AUTHORITY, PROHIBITED_ACTION, ALLOWED_INSPECTION, CONTROL_PLANE, ESCALATION_STATE e GLOBAL_INVARIANT. Cada símbolo derivado deve apontar para os mecanismos que o aplicam e para o método que verifica a aplicação.

Revisão de conformidade — semântica atual da fonte

STATUS: CONFORME COM AJUSTE.

AGENT_POLICY.md atual afirma explicitamente que .drive/** não é fonte autoritativa por padrão; fontes controladas são as designadas pela tarefa ou pelo plano e são somente leitura. Portanto, expressões genéricas como “fontes operacionais” não devem ser interpretadas como todo o diretório .drive. Há ainda um defeito textual no Markdown atual da lista de control plane (`-- runbooks/**`), que aparenta ser um hífen duplicado e deve ser tratado como erro de forma, não como nova semântica.

05 — CLAUDE.md

CLAUDE.md

Identidade

Path canônico: CLAUDE.md, na raiz do repositório.

Classe: ROLE_CONTRACT / EXECUTOR_ADAPTER.

Domínio principal: Agent Specification, Instruction Architecture e Execution Governance.

Papel associado: EXECUTOR = Claude Code no VS Code.

Definição

É o contrato permanente de comportamento do Executor. Ele não substitui AGENT_POLICY.md; referencia a política e traduz invariantes comuns em um procedimento transversal que deve valer para qualquer tarefa executada pelo Claude Code no repositório.

Objetivos

Fazer o Executor identificar exatamente a tarefa, verificar a branch, inspecionar o estado do Git, carregar apenas contexto necessário, classificar risco, resolver o runbook_binding, limitar alvos, executar somente a alteração autorizada, rodar validadores determinísticos e produzir um handoff factual terminando em READY_FOR_REVIEW ou BLOCKED.

Sequência transversal

1. Identificar tarefa e autoridade.

2. Confirmar branch diferente de main/master.

3. Inspecionar git status.

4. Carregar política, fontes normativas e runbooks aplicáveis.

5. Classificar risco e decidir se proposta formal é obrigatória.

6. Classificar arquivos como target/reference/read_only/forbidden quando aplicável.

7. Implementar apenas o escopo autorizado.

8. Executar validators, git diff --check, git diff e git status.

9. Confirmar ausência de alteração fora do escopo.

10. Entregar handoff factual.

Entradas

TASK ou instrução humana autorizada; AGENT_POLICY.md; task/plan aprovado; runbook_binding; fontes normativas; estado observável do repositório; validadores aplicáveis.

Saídas

Working tree candidato; diff revisável; resultados de validação; lista factual de arquivos alterados; limitações e bloqueios; estado terminal READY_FOR_REVIEW ou BLOCKED.

Autonomia

O arquivo permite autonomia técnica apenas dentro do contrato da tarefa. Expansão material de escopo, decisão de produto, alteração de política, Git privilegiado, bypass de permissão e autoaprovação ficam fora da autoridade do Executor.

Relação com Plan Mode

A arquitetura admite proposal proporcional para mudanças simples e task_proposal completo para classes de maior risco/impacto. CLAUDE.md governa o comportamento permanente; o plano governa a instância específica de trabalho.

Relação com runbooks

CLAUDE.md não deve duplicar procedimento de code_change, database_change, documentation_change ou dependency_change. Quando runbook_binding existir, o Executor carrega somente shared/executor runbooks aplicáveis e bloqueia divergência material.

Enforcement associado

Managed settings, pretool, mounts read-only e identidade do container materializam parte das proibições descritas. A instrução textual continua necessária para comportamento que não é completamente enforceable pelo ambiente, como não inventar requisito ou não expandir escopo.

Critério de handoff correto

O handoff deve separar fatos observados de alegações; listar tarefa, arquivos, checks, resultados, limitações, bloqueios e pontos relevantes ao Reviewer. Narrativa confiante não substitui evidência.

Mapeamento para SYMBOL_REGISTRY

É consumidor direto de TASK, EXECUTOR, BRANCH_VALID, WRITE_SCOPE/WRITE_SET, RUNBOOK_BINDING, VALIDATOR_SET, EVIDENCE_SET, READY_FOR_REVIEW e BLOCKED. A especificação futura deve reduzir ambiguidades entre “arquivo autorizado”, “arquivo alvo” e “arquivo tecnicamente gravável”.

06 — AGENTS.md

AGENTS.md

Identidade

Path canônico: AGENTS.md, na raiz do repositório.

Classe: ROLE_CONTRACT / REVIEWER_ADAPTER.

Domínio principal: Software Assurance, Independent Review, Adversarial Verification e Agent Specification.

Papel associado: REVIEWER = Codex no VS Code.

Definição

É o contrato permanente de comportamento do Reviewer independente. Sua função é impedir que Codex seja tratado como um segundo Executor. O arquivo estabelece que review significa observar, confrontar, tentar refutar e emitir verdict; finding não deve ser silenciosamente corrigido pelo próprio Reviewer.

Objetivos

Garantir independência entre produção e assurance; definir a unidade sob revisão; padronizar procedimento, findings e verdicts; preservar projeto sem alterações durante o gate; detectar regressões, evidência insuficiente, extrapolação de escopo e decisões humanas simuladas.

Fonte do review

Tarefa autorizada; git status; git diff completo; arquivos untracked pertencentes à tarefa; critérios de aceite; task/plan aprovado; runbook_binding; artefatos relacionados; evidências materiais; fontes normativas aplicáveis.

Procedimento transversal

1. Confirmar exatamente a tarefa sob revisão.

2. Inspecionar estado e diff completo.

3. Identificar critérios de aceitação e oráculos.

4. Carregar runbooks shared/reviewer aplicáveis.

5. Reexecutar checks relevantes quando necessário e compatível com read-only.

6. Procurar regressões e alterações inesperadas.

7. Tentar refutar conclusões materiais do Executor.

8. Verificar suficiência, origem e rastreabilidade das evidências.

9. Procurar alegações mais fortes do que os fatos observados.

10. Confirmar preservação de escopo e autoridade humana.

Saídas válidas

PASS: nenhuma correção obrigatória encontrada dentro do contrato avaliado.

FAIL: existe correção obrigatória que pertence ao escopo do Executor.

HUMAN_DECISION_REQUIRED: a conclusão depende de decisão material que o Reviewer não possui autoridade para tomar.

Findings

A estrutura esperada separa Problema, Evidência, Impacto e Correção requerida, com severidade CRITICAL/HIGH/MEDIUM/LOW quando apropriado. A evidência deve apontar para fato observável, e não para preferência estilística apresentada como erro.

Independência

Durante review normal, o Reviewer não edita projeto, não aplica patch, não corrige finding, não altera Git, não faz commit e não avança de tarefa. Isso preserva a propriedade producer ≠ reviewer.

Enforcement associado

A independência comportamental é reforçada por configuração Codex e pelo Dev Container do Reviewer com workspace read-only. O arquivo AGENTS.md continua necessário para definir o método intelectual do review; filesystem read-only sozinho não ensina o agente a procurar evidência falsa, regressões ou claims superdimensionados.

Critério de PASS confiável

PASS exige ausência de finding obrigatório após comparação com critérios e evidências. O Reviewer não deve converter “não consegui reproduzir” em PASS, nem assumir que output apresentado pelo Executor é verdadeiro sem confrontá-lo quando a criticidade justificar.

Mapeamento para SYMBOL_REGISTRY

É consumidor de REVIEWER, CANDIDATE, EVIDENCE_SET, ACCEPTANCE_CRITERIA, FINDING, PASS, FAIL e HUMAN_DECISION_REQUIRED. O registry deve definir claramente a diferença entre PASS de um comando, PASS de um critério e PASS do review final.

07 — task_atomics.md

task_atomics.md

Identidade

Path canônico comprovado: docs/arquiteturas/task_atomics.md.

Classe: TASK_SPECIFICATION / SPECIFICATION_METAMODEL.

Domínio principal: Requirements Engineering, Specification Engineering, BDD, Contract-Based Development e Agentic Task Design.

Referência interna AESDS: padrão de tarefas atômicas e critérios de aceitação.

Definição

É o documento que define a menor unidade de trabalho suficientemente explícita para um agente implementar sem inventar requisito, alterar escopo ou depender de longa conversa externa. Ele especifica o metamodelo de task_proposal e os critérios de granularidade, risco, evidência, BDD e Definition of Done.

Objetivo

Transformar intenção humana em contrato verificável. A task deve conter informação suficiente para separar o problema da solução, delimitar contexto válido/inválido, declarar pré-condições, dependências, fontes normativas, regras, decisões, constraints, escopo, arquivos, ações permitidas/proibidas, stop conditions, critérios de aceitação, checks obrigatórios e evidência esperada.

Contrato verificável por máquina

O documento referencia .ai/control/task-proposal.schema.json como schema do contrato, .ai/task-proposal.example.json como exemplo canônico e .ai/control/validate-task-proposal.mjs como validador reproduzível. Portanto, task_atomics.md é a especificação humana do metamodelo; o JSON Schema é a materialização estrutural machine-checkable.

Gatilho de uso

O task_proposal completo é obrigatório para riscos amarelo, vermelho ou vermelho crítico; para alteração de regra de negócio/cálculo/decisão que afete atleta, treino, jogo ou dado pessoal; e para modelo de dados, RLS, autenticação, MFA ou auditoria. Mudança verde, local e fora dessas classes pode usar proposta proporcional mais leve conforme CLAUDE.md.

Ciclo de duas portas

Porta 1 — plano: Executor preenche a proposta e Reviewer avalia antes da implementação. PASS autoriza a execução.

Porta 2 — implementação: depois do plano aprovado, Executor implementa e Reviewer confronta o diff contra o contrato aprovado.

Os verdicts permanecem os mesmos; muda o objeto avaliado.

Campos essenciais

ID; título; instrução original; objetivo; problema; ator; contexto válido/inválido; preconditions; dependencies; normative_source; inputs_and_contracts; current_behavior; expected_behavior; relevant_states; in_scope; out_of_scope; included_edge_cases; three_amigos; business_rules; decisions; constraints; allowed_actions; prohibited_actions; allowed_technical_autonomy; files/path-role-operation; decisões humanas tomadas e pendentes; stop_conditions; acceptance_criteria; mandatory_checks; expected_evidence; definition_of_done; risk; runbook_binding; BDD quando aplicável.

Granularidade

Uma task deve ter um resultado verificável e um diff revisável integralmente. Deve ser dividida quando mistura resultados independentes, múltiplos fluxos não relacionados ou decisões humanas distintas. Não deve ser artificialmente microfragmentada quando a separação só cria handoff sem valor.

Oráculo de aceitação

Cada acceptance criterion deve declarar method e expected. Critério sem método de prova é incompleto quando a ambiguidade pode alterar o resultado. Métodos incluem teste automatizado, typecheck, build, inspeção de contrato, runtime, acessibilidade, dispositivo real e validação humana.

Relação com runbooks

A task diz O QUE e sob quais critérios. O runbook diz COMO conduzir a classe de operação. runbook_binding resolve apenas os runbooks aplicáveis; não cria runbook novo por task.

Relação com SYMBOL_REGISTRY

É um dos principais consumidores futuros do registry. Campos como actor, state, constraint, allowed_action, evidence e decision devem referenciar vocabulário semântico estável. O registry não substitui o task schema: ele reduz ambiguidade dos valores e conceitos usados pelo schema.

Revisão de conformidade — contrato machine-checkable

STATUS: CONFORME COM COMPLEMENTO.

O schema atual existe em .ai/control/task-proposal.schema.json e exige também metacampos que não estavam enumerados nesta guia: object_type, schema_version, proposal_id e revision. O validador .ai/control/validate-task-proposal.mjs existe e cobre exatamente o subconjunto de keywords usado pelo schema; o próprio código declara que não é um validador genérico/certificado de JSON Schema 2020-12. Logo, VALID produzido por esse script significa conformidade segundo o validador leve implementado, não certificação universal do schema.

08 — Runbooks.md

Runbooks.md

Identidade

Path canônico comprovado: docs/arquiteturas/multi-agentes/Runbooks.md.

Classe: RUNBOOK_ARCHITECTURE.

Domínio principal: Runbook Engineering, Procedural Knowledge, Operations Engineering e Software Assurance Procedures.

Definição

É o documento que define a arquitetura da biblioteca de runbooks do CEPRAEA BEACH PRO. Ele não é um runbook individual; é a especificação de como os runbooks são organizados, selecionados, especializados, relacionados à política e conectados ao enforcement.

Objetivo

Aumentar repetibilidade, previsibilidade e verificabilidade das operações recorrentes sem criar uma state machine paralela ao Git. O documento adota separação entre runbooks shared, executor e reviewer e preserva CLAUDE.md/AGENTS.md como adaptadores permanentes.

Estrutura canônica

runbooks/README.md = catálogo, seleção, aplicabilidade e precedência.

runbooks/shared/ = procedimentos realmente comuns.

runbooks/executor/ = procedimentos de execução por classe de mudança.

runbooks/reviewer/ = procedimentos de revisão por classe de mudança.

docs/operacao/agent-workflow.md = runbook humano do ciclo completo.

Classes de operação

code_change; database_change; documentation_change; dependency_change. A classe da operação determina o runbook. O número de agentes ou o número da task não determina criação de runbook.

Runbooks compartilhados

RB-SHARED-001-repository-baseline.md: baseline do repositório quando necessária.

RB-SHARED-002-evidence.md: forma mínima da evidência material.

RB-SHARED-003-failure-states.md: vocabulário comum de READY_FOR_REVIEW/BLOCKED e PASS/FAIL/HUMAN_DECISION_REQUIRED.

Executor

RB-EXEC-001-code-change.md: alterações de código.

RB-EXEC-002-database-change.md: schema, migration, constraints, índices e persistência.

RB-EXEC-003-documentation-change.md: Markdown e documentação.

RB-EXEC-004-dependency-change.md: dependências e lockfiles.

Reviewer

RB-REV-001-code-review.md: revisão de código.

RB-REV-002-database-review.md: revisão de schema/migration/integridade.

RB-REV-003-documentation-review.md: revisão documental.

RB-REV-004-evidence-review.md: suficiência e reprodutibilidade de evidência.

Há evidência posterior de expansão da biblioteca, como runbook específico de dependency review, devendo o catálogo real do repositório prevalecer sobre listas históricas.

Regra de precedência

Autoridade humana → AGENT_POLICY.md → fontes canônicas aplicáveis → CLAUDE.md/AGENTS.md → runbook especializado → procedimento concreto. Runbook não pode conceder autoridade negada pelas camadas superiores.

Relação com task/plan

Task/plan: objetivo, escopo, entregáveis, sequência particular, critérios.

Runbook: procedimento da classe, validações, evidências, estados de saída.

Uma variação única pertence ao plano. Um padrão recorrente e semanticamente estável pode justificar runbook reutilizável.

Relação com enforcement

Runbooks especificam procedimentos; Dev Container, permissions, sandbox, guards e validators aplicam limites técnicos. Um runbook não deve declarar “impossível editar X” se isso só é uma orientação e não existe controle correspondente; deve separar obrigação normativa de enforcement real.

Critério de criação de novo runbook

Repetição, risco material, procedimento especializado, decisões condicionais recorrentes, validações específicas, evidência própria ou necessidade clara de consistência. Evitar 1 TASK → 1 RUNBOOK exclusivo.

Mapeamento para SYMBOL_REGISTRY

É fonte e consumidor de OPERATION_CLASS, RUNBOOK_BINDING, BASELINE, EVIDENCE, FAILURE_STATE e HANDOFF. O registry deve permitir que operation_classes resolvam para runbooks sem inferência livre do agente.

Revisão de conformidade — inventário vigente

STATUS: CONFORME COM ATUALIZAÇÃO DE INVENTÁRIO.

runbooks/README.md é o catálogo normativo de seleção atual. O inventário de main contém 3 shared, 4 Executor e 5 Reviewer. Para dependency_change, a matriz vigente resolve RB-EXEC-004-dependency-change.md + RB-REV-005-dependency-review.md. RB-REV-004-evidence-review.md é complementar quando a suficiência da evidência é material. O documento arquitetural Runbooks.md ainda contém exemplos estruturais antigos de .devcontainer/security; esses exemplos não prevalecem sobre os paths atuais .devcontainer/control-plane e .devcontainer/guards.

09 — CONTAINER-RUNBOOK

CONTAINER-RUNBOOK-v0.3.md

Identidade

Path comprovado no conjunto enviado: docs/arquiteturas/multi-agentes/CONTAINER-RUNBOOK-v0.3.md.

Classe: INFRASTRUCTURE_RUNBOOK / OPERATIONAL_BASELINE.

Domínio principal: Platform Engineering, DevSecOps, Configuration Management, Operational Assurance e Security Boundary Engineering.

Status de interpretação: documento histórico/operacional rico em evidências; não deve ser automaticamente tratado como descrição vigente de toda a arquitetura posterior.

Definição

É um runbook técnico e baseline operacional do ambiente de agentes em container. Diferentemente de Runbooks.md, que especifica a arquitetura da biblioteca de procedimentos, este arquivo registra estado, decisões, testes, tentativas, rollback, incidentes e evidências relacionadas ao ambiente de execução.

Objetivo

Reduzir risco de agentes operarem com a mesma autoridade do humano; diminuir blast radius; separar credenciais e Docker; manter o plano de controle independente; preservar promoção humana; registrar o que foi decidido, implantado, validado, rejeitado ou substituído.

Vocabulário epistemológico

DECIDIDO = escolhido, sem provar implantação.

IMPLANTADO = aplicado, sem necessariamente provar funcionamento.

VALIDADO = testado com resultado compatível.

PENDENTE = evidência insuficiente.

REJEITADO = abordagem abandonada.

SUBSTITUÍDO = desenho antigo superado.

NÃO APLICÁVEL = fora do escopo.

Essa separação é central para impedir falsos estados de sucesso.

Regra anti-inferência

Configuração desejada, recomendada ou decidida não pode ser tratada como implantada/validada sem evidência. Quando evidência não existe, o estado permanece pendente.

Conteúdo típico

Baseline do projeto e Git; identidade humana e agente; estado do Dev Container; decisões arquiteturais; mounts e permissões; ausência de sudo/Docker/socket; credenciais; control plane root-owned; testes positivos e negativos; incidentes; abordagens rejeitadas; rollback; changelog.

Papel na arquitetura

Fornece memória operacional de infraestrutura e um modelo de como preservar baseline e evidência. O documento Runbooks.md posterior explicita que este CONTAINER_RUNBOOK deve ser tratado como exemplo de outro tipo de runbook e que seus estados históricos não constituem, sozinhos, evidência do estado atual da arquitetura consolidada.

Risco de autoridade fantasma

Um baseline válido em uma branch ou período pode deixar de ser válido depois de alteração de Dockerfile/devcontainer. Por isso, o arquivo deve sempre declarar a identidade temporal e de configuração da evidência. Nunca transportar um status VALIDADO para uma configuração diferente sem novo teste.

Relações

Consome Dockerfile, devcontainer, managed policies, codex requirements, guards, Git e scripts de verificação; produz conhecimento operacional para manutenção e troubleshooting. Não substitui o documento de arquitetura-mãe nem a política dos agentes.

O que NÃO garante

Não garante correção do código produzido pelo agente. Não garante que main esteja protegida, que CI seja obrigatório ou que qualquer controle não testado esteja ativo. A fronteira de segurança do container e a qualidade do software são problemas diferentes.

Uso recomendado no catálogo

Como fonte histórica de decisões, taxonomia de estado e práticas de evidência. Para estado vigente, confrontar sempre com arquivos reais do repositório e testes atuais.

Mapeamento para SYMBOL_REGISTRY

Fonte útil para EPISTEMIC_STATE: DECIDED, IMPLEMENTED, VALIDATED, PENDING, REJECTED, SUPERSEDED. Esses estados devem permanecer separados dos estados de workflow de task para evitar colisão semântica.

Revisão de conformidade — colisão de autoridade

STATUS: HISTORICAL_REFERENCE_IN_THIS_CATALOG.

O próprio CONTAINER-RUNBOOK declara ser “fonte de verdade operacional”, porém Runbooks.md determina explicitamente que o CONTAINER_RUNBOOK fornecido seja usado exclusivamente como referência estrutural e conceitual neste contexto e que o estado real seja determinado pelos documentos reais da arquitetura e evidências específicas de implantação. Esta colisão deve permanecer visível. Para este catálogo, o CONTAINER-RUNBOOK não é autoridade automática sobre o estado atual; seus estados só valem no baseline e evidência aos quais estão vinculados.

10 — Relatório multi-agentes

Relatorio Multi-Agentes.md

Identidade

Path canônico comprovado: docs/arquiteturas/multi-agentes/Relatorio Multi-Agentes.md.

Classe: AUDIT_ANALYSIS / ASSURANCE_REPORT.

Domínio principal: Software Assurance, Control Assessment, Gap Analysis e Security Review.

Definição

É um relatório analítico que confronta política declarada, configuração técnica e evidência disponível. Sua função é responder “o que está realmente protegido, o que está apenas documentado e quais gaps ainda existem?”.

Objetivo

Inspecionar mounts, managed settings, hooks, sandbox do Codex e demais controles; identificar divergências funcionais; justificar mudanças de política; distinguir proteção comportamental de enforcement técnico; produzir recomendações sustentadas por evidência.

Natureza da autoridade

O relatório não é uma policy, não é um runbook e não é enforcement. Uma conclusão registrada nele precisa ser promovida para a fonte normativa adequada se for virar regra. Uma recomendação de auditoria não pode adquirir autoridade apenas porque foi escrita por um agente ou porque contém linguagem assertiva.

Método

Fonte verificada → fato observado → interpretação → lacuna → impacto → recomendação. Esse encadeamento deve permitir rastrear cada claim importante para o arquivo/configuração ou teste que o sustenta.

Exemplo de uso correto

“managed settings negam comandos Git de mutação” deve ser sustentado pela leitura das deny rules. “Codex é read-only” deve ser sustentado pela configuração aplicável e, para alegação operacional forte, por teste real. “.drive está protegido” só pode ser afirmado se o mecanismo efetivo cobrir o path e a verificação confirmar a propriedade.

Papel no ciclo de assurance

Fornece análise de segunda ordem: não apenas testa uma feature, mas avalia se a própria arquitetura de controle tem lacunas. É útil para hardening, revisão de configuração e reconciliação entre documentação e estado real.

Riscos

Conclusão envelhecida depois de alteração de configuração; relatório virar shadow authority; inferência de runtime a partir de arquivo estático; confusão entre ausência de finding e prova de segurança; promoção de hipótese para fato.

Relação com outros arquivos

Lê AGENT_POLICY.md, CLAUDE.md, AGENTS.md, devcontainer, managed settings, pretool/posttool e codex requirements. Pode recomendar alterações nesses artefatos, mas não deve substituí-los. Findings materiais que exigem decisão arquitetural precisam ser registrados na fonte de decisão apropriada.

Critério de qualidade

Cada claim forte deve ter evidência verificável e escopo temporal/configuracional. O relatório deve separar: fato; inferência; recomendação; pendência; risco residual. A linguagem “está protegido” deve ser reservada para propriedade realmente sustentada.

Mapeamento para SYMBOL_REGISTRY

Principalmente consumidor do registry. A auditoria deve usar termos como ENFORCED, DOCUMENTED_ONLY, VERIFIED e PENDING com semântica única. Isso reduz relatórios em que a mesma palavra “validado” significa coisas diferentes em seções distintas.

Revisão de conformidade — validade temporal

STATUS: AUDIT_SNAPSHOT / REVALIDATION_REQUIRED.

O relatório contém claims sobre uma configuração observada em um momento específico. Desde então, o managed settings atual passou a conter deny de Read para .drive/CEPRAEA BEACH PRO/** e .drive/BEACH HANDBALL/**, embora isso não seja equivalente a um mount read-only nem a um deny genérico de escrita. Qualquer claim do relatório sobre “controle atual” deve ser confrontado com main antes de ser reutilizado.

11 — Claude managed settings

claude-managed-settings.json

Identidade

Path canônico do arquivo versionado: .devcontainer/control-plane/claude-managed-settings.json.

Path de instalação no runtime: /etc/claude-code/managed-settings.json.

Classe: ENFORCEMENT / MANAGED_AGENT_POLICY.

Domínio principal: Security Policy Enforcement, Least Privilege e Claude Code Administrative Configuration.

Definição

É a política gerenciada do Claude Code instalada fora do espaço normal de decisão do agente. Diferentemente de CLAUDE.md, que instrui o modelo, este JSON configura mecanismos de permissão e hooks usados pela própria ferramenta para negar ou solicitar autorização para capacidades específicas.

Objetivo

Materializar parte das restrições do EXECUTOR: impedir bypass de permissões; restringir comandos administrativos e Git de mutação; impedir leitura direta de conjuntos de credenciais; controlar operações que exigem confirmação; obrigar uso de hooks gerenciados; conectar pretool e posttool ao ciclo de ferramentas.

Configuração observada no arquivo enviado

allowManagedHooksOnly = true.

allowManagedPermissionRulesOnly = true.

disableBypassPermissionsMode = disable.

Deny inclui sudo, docker e operações Git como add, commit, push, pull, merge, rebase, cherry-pick, reset, restore, checkout, switch, worktree, clean, rm, stash e update-ref.

Deny de leitura cobre ~/.ssh, ~/.aws, configuração do gh e arquivos .env/secrets definidos.

Ask inclui npm install e npx.

sandbox.enabled = false no estado observado.

PreToolUse e PostToolUse são conectados a /usr/local/lib/cepraea-guards/pretool e /usr/local/lib/cepraea-guards/posttool.

Papel arquitetural

É um controle de primeira linha no plano do Executor. Converte parte de MUST NOT declarados em AGENT_POLICY.md em decisões aplicadas pela ferramenta. Deve ser instalado como arquivo administrado/root-owned para que o agente não possa reescrever a própria política durante execução comum.

Limite do controle

Permission rules de ferramenta não equivalem automaticamente a sandbox de sistema operacional. Um deny Bash ou Edit cobre as formas interpretadas pela ferramenta; subprocessos indiretos e capacidades equivalentes precisam de fronteiras complementares quando o risco exigir. O estado observado possui sandbox interna desabilitada, portanto o catálogo não deve alegar que esse JSON sozinho cria isolamento de filesystem completo.

Defense in depth

AGENT_POLICY define a norma; managed settings aplica regras da ferramenta; pretool faz fail-fast adicional; mounts/Dev Container protegem recursos em nível de ambiente; revisão humana e Codex detectam violações ou inconsistências remanescentes.

Riscos de configuração

Regra sintaticamente válida mas semanticamente ineficaz; path incorreto; deny incompleto; dependência excessiva de pattern matching; managed file instalado com ownership inadequado; divergência entre arquivo versionado e arquivo realmente instalado; assumir sandbox ativa quando enabled=false.

Verificação exigida

Validação JSON; presença no path de runtime; ownership/mode; leitura de /status ou mecanismo equivalente quando aplicável; testes negativos reais de operações proibidas; confirmação de que hooks são invocados; comparação hash/conteúdo entre fonte versionada e arquivo instalado quando necessário.

Mapeamento para SYMBOL_REGISTRY

Materializa predicados como CLAUDE_GIT_MUTATION_DENIED, CLAUDE_PRIVILEGED_COMMAND_DENIED, MANAGED_HOOKS_ONLY e CREDENTIAL_PATH_READ_DENIED. Cada predicado precisa listar a regra exata e um teste negativo que prove o comportamento.

Revisão de conformidade — delta encontrado

STATUS: CONFORME COM CORREÇÃO DE INVENTÁRIO.

O arquivo atual também contém duas regras deny não registradas anteriormente nesta guia: Read(./.drive/CEPRAEA BEACH PRO/**) e Read(./.drive/BEACH HANDBALL/**). Isso cria uma diferença relevante entre “fonte controlada read-only” e “fonte inacessível pela ferramenta Read”. A intenção arquitetural dessas regras deve ser reconciliada com tarefas que necessitem consultar esses corpora; não inferir que deny de leitura protege escrita no filesystem.

12 — Codex requirements

codex-requirements.toml

Identidade

Path canônico versionado: .devcontainer/control-plane/codex-requirements.toml.

Path de instalação/consumo sistêmico registrado: /etc/codex/requirements.toml.

Classe: ENFORCEMENT / REVIEWER_REQUIREMENTS.

Domínio principal: Software Assurance Isolation, Codex Security Configuration e Least Privilege.

Definição

É o arquivo que restringe a configuração admissível do Codex Reviewer. Ele estabelece limites administrados para approval policy, sandbox, hooks e capacidades de navegação/controle, reduzindo a possibilidade de o Reviewer abandonar o papel read-only previsto pela arquitetura.

Configuração observada no arquivo enviado

allowed_approval_policies = untrusted e on-request.

allowed_approvals_reviewers = user.

allowed_sandbox_modes = read-only.

allow_managed_hooks_only = true.

allow_remote_control = false.

allow_login_shell = false.

allowed_web_search_modes = cached e indexed.

features.computer_use = false.

features.browser_use_external = false.

features.browser_use_full_cdp_access = false.

O próprio arquivo registra que uma tentativa anterior com permission profile customizado não impôs a fronteira pretendida e que gates definitivos ainda estavam pendentes.

Objetivo

Impor um teto de permissões ao Reviewer e tornar incompatível com o contrato de assurance uma execução com workspace-write/danger-full-access no contexto avaliado. A configuração deve trabalhar em conjunto com o Dev Container do Reviewer, não substituir a fronteira read-only do workspace quando essa fronteira é necessária.

Papel arquitetural

É enforcement específico do assurance plane. AGENTS.md define como revisar; codex-requirements.toml restringe quais modos de execução são aceitáveis. A combinação comportamento + capacidade é mais robusta do que qualquer uma isoladamente.

Relação com Dev Container Reviewer

Existe path canônico .devcontainer/reviewer/devcontainer.json que monta ou configura o workspace do Reviewer como read-only. Essa fronteira de ambiente é particularmente importante quando versões/configurações do Codex mudam. Requirements e container devem ser validados juntos.

Limites

allowed_web_search_modes não é firewall de shell. read-only declarado não deve ser confundido com ausência de toda escrita efêmera necessária a ferramentas, dependendo da arquitetura vigente. Também não se deve assumir que uma opção TOML é reconhecida pela versão instalada sem teste.

Riscos

Versão do Codex incompatível com a chave; arquivo instalado diferente do versionado; configuração de projeto sobrepondo intenção; alteração posterior que reabilite workspace-write; teste feito em CLI diferente da extensão efetivamente usada.

Verificação

Parse TOML; confirmar arquivo instalado; identificar versão Codex; executar Codex real no perfil de review; provar leitura do diff; provar falha de escrita no workspace; provar ausência de elevação automática; verificar comportamento de temp/cache conforme a arquitetura vigente.

Mapeamento para SYMBOL_REGISTRY

Materializa REVIEWER_READ_ONLY, REVIEWER_APPROVAL_BOUNDARY e REVIEWER_CAPABILITY_DENY. O registry deve diferenciar “modo permitido pela configuração” de “propriedade comprovada no runtime”.

13 — pretool

pretool

Identidade

Path canônico versionado: .devcontainer/guards/pretool.

Path de execução: /usr/local/lib/cepraea-guards/pretool.

Classe: ENFORCEMENT_GUARD / PRE_TOOL_REFERENCE_MONITOR.

Domínio principal: Runtime Policy Enforcement, Guardrails e Fail-Fast Security Controls.

Definição

É um hook executado antes de determinadas tool calls do Claude Code. Recebe JSON via stdin, identifica tool_name e entradas relevantes e pode encerrar com exit code 2 para bloquear a operação antes que a ferramenta execute o efeito solicitado.

Objetivo

Fornecer fail-fast claro para operações proibidas e impedir violações óbvias do plano de controle. Também reforça regras de branch e cria uma exceção estreita para o Plan Mode nativo do Claude sem liberar a árvore .claude de forma ampla.

Comportamentos observados

Bloqueia ferramentas mutáveis quando a branch é main ou master.

Permite estritamente arquivos de plano em /home/agent/.claude/plans/*.md sob condições defensivas contra subpaths, symlink e traversal.

Bloqueia paths do plano de controle, incluindo .git, .devcontainer, workflows, scripts/ci, .claude, .codex, .mcp.json, AGENT_POLICY.md, CLAUDE.md, AGENTS.md e runbooks.

Para Bash, bloqueia sudo, docker e flags dangerously-* conhecidas.

Para Git, usa allowlist de subcomandos de inspeção: status, diff, log, show, rev-parse e ls-files; demais subcomandos reconhecidos são bloqueados.

Papel arquitetural

É uma barreira operacional preventiva no ciclo de ferramenta do Executor. Sua principal qualidade é fornecer decisão rápida e mensagem específica ao agente. Ele complementa managed settings e fronteiras do container.

O que NÃO é

Não é parser formal completo de shell. O próprio código reconhece que não cobre 100% de variáveis, encoding, wrappers e sintaxe indireta. Portanto, não deve ser descrito como sandbox “à prova de bypass”. Quando uma propriedade exige garantia estrutural contra subprocesso arbitrário, o controle precisa estar no filesystem/container/sandbox apropriado.

Fail-closed local

Para Git reconhecido, a abordagem é allowlist: se o subcomando não pertence ao conjunto de inspeção, bloqueia. Isso é mais seguro que manter apenas blacklist crescente de comandos mutáveis, embora ainda dependa do parser aproximado usado para localizar invocações Git.

Relação com Plan Mode

A exceção para /home/agent/.claude/plans é deliberadamente estreita e valida basename, ausência de traversal, symlink e parent real. Isso preserva funcionalidade nativa sem transformar .claude em área geral de escrita.

Riscos

Pattern bypass; path recebido em campo diferente do esperado; comando composto não reconhecido; regra de path desatualizada; divergência entre hook instalado e versionado; confiança indevida no guard como única fronteira.

Verificação

Teste unitário/fixture de payloads; tentativas reais de Edit/Write/Bash; casos positivos permitidos; casos negativos; branch main/master; paths control-plane; Git allowlist; wrappers adversariais; confirmação do exit 2; comparação do arquivo instalado.

Mapeamento para SYMBOL_REGISTRY

Materializa PRE_TOOL_ALLOWED, PRE_TOOL_BLOCKED, CONTROL_PLANE_WRITE_DENIED, MAIN_BRANCH_MUTATION_DENIED e GIT_INSPECTION_ONLY. A semântica do símbolo BLOCKED do workflow não deve ser confundida com exit code 2 do hook; o hook produz um evento de bloqueio que o Executor traduz para estado operacional quando impede a task.

14 — posttool

posttool

Identidade

Path canônico versionado: .devcontainer/guards/posttool.

Path de execução: /usr/local/lib/cepraea-guards/posttool.

Classe: OBSERVABILITY_HOOK.

Domínio principal: Observability, Audit Telemetry e Agent Tooling Instrumentation.

Definição

É um hook executado depois de tool calls selecionadas. No arquivo observado, lê o payload, identifica tool_name e acrescenta um registro JSONL com timestamp UTC e nome da ferramenta em /home/agent/.local/state/cepraea-guards/events.jsonl.

Objetivo

Registrar que uma ferramenta foi observada depois da execução. Serve como trilha operacional leve e mecanismo de observabilidade, não como autorização prévia e não como prova suficiente de que o efeito da ferramenta foi correto.

Papel arquitetural

Complementa o pretool. pretool decide antes e pode bloquear; posttool observa depois. Essa diferença deve permanecer explícita:

PRETOOL = preventive control.

POSTTOOL = detective/observability control.

Saída

Evento JSONL contendo observado_em e tool. O formato é simples, append-only no estado local do agente. O arquivo não registra, na versão observada, todos os argumentos, resultado, exit code ou hash do efeito; portanto seu valor probatório é limitado ao evento que de fato captura.

Limites

Não impede ação indevida; não valida sucesso; não prova que o conteúdo alterado está correto; não substitui Git diff; não deve ser tratado como ledger de assurance ou state machine do workflow.

Risco de excesso de confiança

“Existe evento posttool” significa que o hook registrou uma tool call, não que a ação foi autorizada, correta ou completa. Se o evento for usado em auditoria, sua semântica deve permanecer restrita ao que o payload realmente contém.

Relação com política de persistência

A arquitetura evita logs obrigatórios de cada interação como estado do workflow. Este arquivo produz observabilidade local leve; sua existência não autoriza criar burocracia paralela ao Git nem transformar events.jsonl em autoridade de promoção.

Verificação

Executar tool elegível; confirmar criação/append do JSONL; validar JSON por linha; verificar timestamp e tool; confirmar que erro do hook não é silenciosamente interpretado como prova positiva.

Mapeamento para SYMBOL_REGISTRY

Pode materializar TOOL_CALL_OBSERVED, mas não ACTION_VERIFIED. Essa distinção é importante: observação de evento e evidência de propriedade são classes semânticas diferentes.

15 — gitconfig-agent

gitconfig-agent

Identidade

Path canônico: .devcontainer/control-plane/gitconfig-agent.

Mounts observados: /etc/gitconfig, /home/agent/.gitconfig e /home/agent/.config/git/config, em modo read-only em configurações do ambiente.

Classe: IDENTITY_ISOLATION / CREDENTIAL_BOUNDARY_CONFIG.

Domínio principal: Configuration Management, Git Identity Isolation e Credential Hygiene.

Definição

É uma configuração Git deliberadamente vazia. O conteúdo declara que agentes não devem receber identidade de usuário, credential helpers ou configuração de signing. O valor do arquivo está precisamente na ausência controlada de configurações que poderiam herdar autoridade humana.

Objetivo

Impedir que processos de agente reutilizem nome/e-mail, helper de credenciais, signing key ou outras configurações pessoais do operador como consequência acidental de mounts ou da configuração global do host.

Papel arquitetural

Contribui para a separação entre identidade humana e identidade do agente. O Dev Container pode montar esse arquivo em múltiplos locais de configuração Git e também definir GIT_CONFIG_GLOBAL=/dev/null e variáveis relacionadas, criando defense in depth contra herança de configuração.

O que NÃO faz

Não torna .git read-only; não bloqueia subcomandos Git; não impede toda forma possível de autenticação; não substitui a remoção de tokens, SSH agent, gh config ou credenciais de ambiente. Ele cobre especificamente configuração Git global/pessoal.

Propriedade desejada

AGENT_GIT_IDENTITY ≠ HUMAN_GIT_IDENTITY e HUMAN_CREDENTIAL_HELPERS_ABSENT_FROM_AGENT_CONTEXT. A ausência é uma propriedade verificável: git config --list --show-origin no ambiente do agente não deve revelar configurações pessoais proibidas.

Riscos

Outro arquivo de configuração ser carregado; variável de ambiente reintroduzir helper; HOME inesperado; mount ausente; sistema Git ignorar o path pretendido devido a GIT_CONFIG_NOSYSTEM/GIT_CONFIG_GLOBAL; ferramenta externa autenticar fora do Git config.

Verificação

Inspecionar git config --list --show-origin; verificar env; verificar mounts; procurar credential.helper, user.name, user.email, signingkey e include/includeIf; confirmar que tokens/SSH_AUTH_SOCK também estão ausentes conforme controles complementares.

Mapeamento para SYMBOL_REGISTRY

Materializa parte de AGENT_IDENTITY_ISOLATED e HUMAN_GIT_CREDENTIALS_NOT_INHERITED. O registry deve decompor essa propriedade por mecanismo, em vez de usar um único booleano genérico “sem credenciais”.

16 — managed MCP

claude-managed-mcp.json

Identidade

Path canônico: .devcontainer/control-plane/claude-managed-mcp.json.

Path de instalação observado no Dockerfile: /etc/claude-code/managed-mcp.json.

Classe: CAPABILITY_CONTROL / MANAGED_INTEGRATION_CONFIG.

Domínio principal: MCP Governance, Capability Security e Agent Integration Management.

Definição

É a configuração administrada da superfície MCP disponível ao Claude Code. No arquivo observado, mcpServers é um objeto vazio, portanto nenhuma integração MCP gerenciada é declarada por esse artefato.

Objetivo

Controlar explicitamente a introdução de servidores MCP e impedir que integrações externas sejam tratadas como capacidade implícita ou casual do Executor. Uma superfície MCP adiciona ferramentas, dados, permissões e novas fronteiras de confiança; por isso deve ser governada separadamente.

Papel arquitetural

É parte do control plane. O arquivo permite que a arquitetura diga não apenas “o agente não deve usar integração X”, mas mantenha uma fonte gerenciada sobre quais servidores são autorizados. No estado observado, a política efetiva representada pelo arquivo é ausência de MCP gerenciado.

Interpretação correta do objeto vazio

mcpServers = {} significa que este arquivo não provisiona servidor MCP. Não prova, isoladamente, que nenhuma outra fonte/configuração da ferramenta possa fornecer MCP; a verificação completa deve considerar precedência e locais de configuração reconhecidos pela versão do Claude Code.

Riscos

Servidor MCP configurado em nível diferente; arquivo administrado não instalado; mudança não revisada que adiciona servidor com acesso sensível; credenciais embutidas; assumir que “MCP vazio” equivale a “nenhuma capacidade externa do agente”.

Critério para introdução futura

Qualquer novo servidor deve declarar finalidade, autoridade, dados acessíveis, operações de leitura/escrita, credenciais, rede, risco, owner, necessidade no SDLC, forma de revogação e acceptance tests. Deve existir decisão humana quando a capacidade altera materialmente o threat model.

Verificação

Confirmar arquivo instalado; listar MCPs reconhecidos pela ferramenta; comparar com a configuração versionada; testar que servidores não autorizados não aparecem; verificar ausência de secrets dentro do JSON.

Mapeamento para SYMBOL_REGISTRY

Relaciona MCP_CAPABILITY_SET e MANAGED_MCP_SERVER. O estado vazio deve ser representado como conjunto vazio comprovado no escopo desta configuração, não como negação universal de toda integração externa.

17 — Dockerfile

Dockerfile

Identidade

Path canônico: .devcontainer/Dockerfile.

Classe: ENVIRONMENT_AS_CODE / IMAGE_BUILD_SPECIFICATION.

Domínio principal: Platform Engineering, Dev Containers, Infrastructure as Code e Supply-Chain/Runtime Hardening.

Definição

É a especificação de build da imagem utilizada pelo ambiente de desenvolvimento agêntico. Materializa dependências de sistema, identidade Linux do agente, diretórios de estado, arquivos administrativos do Claude/Codex, guards e instalação das ferramentas de agente.

Base observada

FROM node:22-bookworm-slim. O build instala bash, bubblewrap, ca-certificates, curl, git, jq, less, passwd, procps e socat. A imagem Node é adaptada para que UID/GID 1000 passem a usar a identidade agent, sem conceder sudo.

Identidade e filesystem

O Dockerfile renomeia node/group para agent, move HOME para /home/agent e cria diretórios de cache, .claude, .codex, configuração Git/GH e estado dos guards. Cria também /etc/claude-code, /etc/codex e /usr/local/lib/cepraea-guards sob root.

Control plane instalado

Copia .devcontainer/control-plane/claude-managed-settings.json → /etc/claude-code/managed-settings.json.

Copia claude-managed-mcp.json → /etc/claude-code/managed-mcp.json.

Copia codex-requirements.toml → /etc/codex/requirements.toml.

Copia .devcontainer/guards/ → /usr/local/lib/cepraea-guards/.

Aplica ownership root e modos de leitura/execução definidos no build.

Ferramentas

Instala Codex e Claude no ambiente e verifica versões durante o build. Depois retorna para USER agent e WORKDIR /workspaces/cepraea-beach-pro.

Papel arquitetural

É a base comum da fronteira local dos agentes. Ele não decide sozinho quais paths do workspace são read-only; isso pertence principalmente à configuração de runtime/mount do Dev Container. Sua função é preparar uma imagem com identidade não-root e control plane instalado fora da autoridade normal do agente.

Defense in depth

A imagem contém bubblewrap/socat no estado observado, mas a presença do pacote não prova que uma sandbox específica está ativa. Instalar uma ferramenta e habilitar um controle são fatos diferentes. A configuração efetiva precisa ser verificada no runtime.

Riscos

Latest/unpinned installer remoto; mudança de versão das ferramentas; build bem-sucedido com política instalada em path errado; ownership/mode inadequado; dependências adicionais aumentando superfície; pacote instalado interpretado como controle ativo; reconstrução alterando comportamento sem atualização das evidências.

Verificação

docker/devcontainer build; claude --version; codex --version; id/whoami; ownership/mode dos arquivos administrativos; ausência de sudo; inspeção dos paths instalados; hash quando necessário; teste de que agent não pode modificar control plane instalado.

Mapeamento para SYMBOL_REGISTRY

Materializa AGENT_LINUX_IDENTITY, CONTROL_PLANE_INSTALLED, CLAUDE_POLICY_RUNTIME_PATH, CODEX_REQUIREMENTS_RUNTIME_PATH e GUARD_RUNTIME_PATH. Esses símbolos precisam distinguir build-time presence de runtime effectiveness.

18 — Dev Container Executor

devcontainer.json — ambiente do Executor

Identidade

Path canônico: .devcontainer/devcontainer.json.

Classe: ENVIRONMENT_AS_CODE / EXECUTION_BOUNDARY_CONFIG.

Domínio principal: Dev Container Engineering, Least Privilege, Filesystem Isolation e Development Environment as Code.

Nome observado: CEPRAEA Agent.

Definição

É a configuração de runtime do Dev Container principal, usado como ambiente do agente escritor/Executor. Define como o repositório é montado, qual usuário executa, quais capacidades Linux são removidas, quais paths recebem mounts read-only, quais credenciais são neutralizadas e quais extensões/settings do VS Code são carregadas.

Workspace

workspaceFolder = /workspaces/cepraea-beach-pro.

remoteUser/containerUser = agent.

updateRemoteUserUID = false.

O workspace base é bind-mounted, e paths sensíveis são sobrepostos como mounts read-only no estado observado.

Hardening de runtime

runArgs inclui no-new-privileges:true e cap-drop=ALL. Não há Docker socket declarado. Variáveis como GITHUB_TOKEN, GH_TOKEN, SSH_AUTH_SOCK e DOCKER_HOST são esvaziadas; Git authentication do VS Code é desativada em settings observados.

Mounts read-only observados

.git; .devcontainer; .github/workflows; .claude; .codex; .mcp.json; CLAUDE.md; AGENTS.md; scripts/ci; AGENT_POLICY.md; runbooks; além dos mounts de gitconfig-agent em paths de configuração. Volumes separados são usados para estado de Claude, Codex e npm.

Papel arquitetural

É a fronteira operacional do Execution Plane. A distinção é importante: o workspace é gravável onde a implementação deve ocorrer, mas componentes de controle e Git são protegidos contra escrita pelo processo do agente. O humano opera fora/através de uma autoridade diferente para as transições privilegiadas.

Relação com pretool e managed settings

Mount read-only é controle de filesystem; managed settings governa tool calls; pretool fornece fail-fast; gitconfig/vars reduzem herança de identidade/credenciais. Uma tentativa deve atravessar várias camadas, não depender de uma única regra textual.

Limite de fidelidade temporal

Há evidências de que a arquitetura do Dev Container passou por evoluções posteriores, inclusive experimentos com compose/egress em branches específicas. Esta guia documenta o arquivo enviado/observado e o path canônico; para declarar estado atual em uma branch futura, deve-se reler o arquivo real daquela branch.

Riscos

Mount ausente ou sobreposto incorretamente; symlink/path alternativo; credencial reintroduzida por extensão; agente executado fora do container; human DevEx acidentalmente bloqueada; assumptions sobre .drive que não correspondam ao mount real; drift entre Dev Container do Executor e Reviewer.

Verificação

Dev Container real; id; mount/findmnt; test -w em paths protegidos; tentativa negativa; env; ausência de Docker socket; git config origins; testes do verify-agent-environment; inspeção de extensão/processo efetivamente conectado ao container.

Mapeamento para SYMBOL_REGISTRY

Materializa EXECUTOR_WORKSPACE, EXECUTOR_WRITABLE_SCOPE, CONTROL_PLANE_READ_ONLY, GIT_FS_READ_ONLY, AGENT_NON_ROOT, CAPABILITIES_DROPPED e HUMAN_CREDENTIALS_ABSENT. Cada símbolo deve declarar escopo exato e mecanismo.

Revisão de conformidade — as-built versus arquitetura

STATUS AS-BUILT: CONFIRMADO EM main.

STATUS DE CONFORMIDADE ARQUITETURAL: DRIFT CONHECIDO.

O devcontainer atual realmente monta .git como readonly. Isso é coerente com o modelo técnico hoje implementado, mas contradiz a premissa anterior da revisão arquitetural que mantinha .git gravável dentro do container. DEC-CTR-013 documenta a mudança, porém está PROPOSTA no plano de governança. Portanto, registrar separadamente: IMPLEMENTATION=.git_RO; GOVERNANCE_RATIFICATION=PENDING_EVIDENCE.

19 — Dev Container Reviewer

devcontainer.json — ambiente do Reviewer

Identidade

Path canônico comprovado: .devcontainer/reviewer/devcontainer.json.

Classe: ENVIRONMENT_AS_CODE / ASSURANCE_ISOLATION_BOUNDARY.

Domínio principal: Independent Review Environment, Software Assurance Isolation e Least Privilege.

Nome observado: CEPRAEA Codex Reviewer.

Definição

É a configuração de Dev Container dedicada ao Reviewer Codex. Sua diferença arquitetural essencial em relação ao ambiente do Executor é o workspace do projeto em modo read-only. O Reviewer precisa conseguir inspecionar o candidato sem possuir capacidade normal de modificá-lo.

Configuração observada no arquivo enviado

Reutiliza ../Dockerfile com contexto ../... workspaceMount monta localWorkspaceFolder em /workspaces/cepraea-beach-pro com readonly. remoteUser e containerUser são agent. Aplica no-new-privileges e cap-drop=ALL. Mantém volume próprio para /home/agent/.codex e monta gitconfig-agent read-only em múltiplos paths. Esvazia tokens e SSH_AUTH_SOCK. Desativa integração Git/autenticação do VS Code. Carrega extensão OpenAI. postStartCommand verifica usuário agent e ausência de write no workspace e em .git.

Objetivo

Garantir Separation of Duties em nível de ambiente: o agente que decide PASS/FAIL não deve ser capaz de corrigir silenciosamente o objeto sob revisão. Isso torna a independência do review uma propriedade estrutural, e não apenas uma instrução em AGENTS.md.

Papel arquitetural

É a fronteira do Assurance Plane. Deve permitir leitura do repositório, diff e artefatos necessários, execução de checks compatíveis e estado efêmero próprio do Codex, mantendo a working tree/candidate imutável sob o Reviewer.

Relação com codex-requirements.toml

O Dev Container aplica read-only em nível de workspace; requirements restringe modos/capacidades do Codex. A defesa é complementar. Se uma versão do Codex mudar o comportamento de sandbox, o workspace read-only continua sendo uma fronteira externa relevante.

Escrita efêmera

A arquitetura pode permitir escrita fora do workspace para estado/caches necessários, desde que isso não altere o candidato sob revisão. O volume /home/agent/.codex é exemplo de estado separado. Qualquer cache adicional deve ser autorizado explicitamente e testado.

Evolução observada

Há evidência histórica de uma branch em que este arquivo foi alterado para usar dockerComposeFile/service reviewer. Isso demonstra que o path é canônico, mas o conteúdo pode variar por evolução arquitetural. O catálogo não congela uma versão antiga como verdade eterna.

Riscos

Abrir o Codex na janela/Dev Container errado; workspace read-only sem tools necessárias; uma ferramenta escrever fora do workspace e depois influenciar review; credencial reaparecer; alteração de compose quebrar isolamento; PASS emitido sem confirmar identidade do ambiente de review.

Verificação

Abrir explicitamente o Reviewer container; whoami; test ! -w workspace/.git; tentar escrita real; ler diff completo; executar check que precise de temp; confirmar ausência de Git mutation e tokens; verificar requirements instalado; provar que nenhum patch altera candidate.

Mapeamento para SYMBOL_REGISTRY

Materializa REVIEWER_ENVIRONMENT, CANDIDATE_READ_ONLY_TO_REVIEWER, REVIEWER_STATE_SEPARATE e REVIEWER_CREDENTIALS_ABSENT. O símbolo REVIEWER_READ_ONLY deve apontar para teste de filesystem e não apenas para instrução textual.

Revisão de conformidade — estado atual

STATUS AS-BUILT: CONFIRMADO EM main.

O Reviewer possui workspace read-only, identidade agent, volume próprio de Codex, credenciais neutralizadas e postStartCommand que verifica ausência de escrita. DEC-CTR-015 descreve essa separação em dois contextos, mas seu status de decisão está PROPOSTA por falta de lastro auditável de aprovação. Assim, a boundary técnica existe; a ratificação de governança não deve ser promovida implicitamente para RATIFICADA.

20 — verify-agent-environment

verify-agent-environment.sh

Identidade

Path canônico: .devcontainer/scripts/verify-agent-environment.sh.

Classe: VERIFIER / PRECONDITION_CHECKER.

Domínio principal: Verification & Validation, Operational Readiness e Environment Conformance Testing.

Definição

É um script Bash de verificação do perfil BASE do ambiente de agentes. Ele observa propriedades concretas do container e retorna um resultado binário agregado: BASE_CONTAINER_CHECK=PASS com exit 0 ou BASE_CONTAINER_CHECK=FAIL com exit 1, mantendo warnings separados.

Objetivo

Detectar rapidamente se pré-condições básicas da arquitetura estão presentes antes de confiar no ambiente: processo não-root; ausência do Docker socket; repositório acessível e reconhecido como Git; SOURCE_ROOT presente e protegido conforme o teste; managed settings instalados; guard presente; configuração Codex disponível; credenciais privilegiadas óbvias ausentes.

Entradas

Estado real do filesystem/container; comandos id, test, git rev-parse, findmnt, stat; variáveis de ambiente; paths canônicos definidos no próprio script.

Saídas

Linhas PASS/WARN/FAIL por check; contadores FAILURES/WARNINGS; exit code final; marcador BASE_CONTAINER_CHECK.

Papel arquitetural

É um verificador, não uma fronteira de segurança. Ele mede se determinados controles existem ou parecem configurados. Se o script for apagado, os mounts continuam sendo mounts; se o script passa erroneamente, isso não torna a propriedade verdadeira. O controle e o teste do controle são camadas distintas.

Checks observados

id -u != 0.

/var/run/docker.sock não é socket.

cd no repositório e git rev-parse funcionam.

SOURCE_ROOT existe e é avaliado via findmnt/permission fallback.

/etc/claude-code/managed-settings.json existe e pertence a root; mode é comparado a conjunto aceitável.

/usr/local/lib/cepraea-guards/pretool existe/executável.

.codex/config.toml pode gerar WARN se ausente; /etc/codex/requirements.toml é obrigatório no estado observado.

GITHUB_TOKEN, GH_TOKEN, SUPABASE_SERVICE_ROLE_KEY e VERCEL_TOKEN devem estar vazios/ausentes.

Limites probatórios

O script não prova que Claude não consegue commit apenas porque managed settings existe; não prova que Codex não edita apenas porque requirements existe; não prova fluxo end-to-end. Propriedades comportamentais dos agentes exigem testes reais do agente.

Riscos de falso PASS

Testar proxy inadequado para a propriedade; path diferente do runtime real; check de permissões superficial; variável de credencial com nome não listado; configuração presente mas não carregada pela ferramenta; script executado fora do Dev Container esperado.

Critério de desenho

Cada check deve ter um oráculo explícito, mensagem inequívoca e exit semantics estáveis. Um WARN não pode ser interpretado como FAIL nem um PASS parcial como homologação global.

Relação com README

README.md em .devcontainer/scripts documenta a especificação do verificador, caminhos, critérios e BDD. Script = implementação do verificador; README = especificação/documentação do comportamento esperado.

Mapeamento para SYMBOL_REGISTRY

É implementação de predicados como NON_ROOT, DOCKER_SOCKET_ABSENT, REPOSITORY_ACCESSIBLE, SOURCE_ROOT_PROTECTED, CLAUDE_POLICY_INSTALLED e PRIVILEGED_ENV_CREDENTIALS_ABSENT. BASE_CONTAINER_CHECK deve ser definido como conjunção dos checks classificados como FAIL-blocking, não como sinônimo de arquitetura inteira validada.

Revisão de conformidade — resultado versus definição

STATUS DO CÓDIGO: CONFIRMADO.

STATUS DO AMBIENTE CORRENTE: NÃO INFERIDO NESTA REVISÃO.

O script continua exigindo SOURCE_ROOT=/workspaces/cepraea-beach-pro/.drive/CEPRAEA BEACH PRO e tenta provar read-only via findmnt/fallback. O Dev Container Executor atual não declara um mount readonly específico para .drive, e o documento de implantação já registrou CT-04 como falha em uma execução anterior. Portanto, BASE_CONTAINER_CHECK só pode receber PASS após nova execução; a existência do script não autoriza marcar SOURCE_ROOT_PROTECTED como verdadeiro.

21 — README do verificador

README.md — scripts de verificação

Identidade

Path canônico comprovado: .devcontainer/scripts/README.md.

Classe: VERIFIER_SPECIFICATION / TECHNICAL_DOCUMENTATION.

Domínio principal: Test Specification, Verification Documentation e BDD for Infrastructure Controls.

Definição

É a documentação formal do verify-agent-environment.sh. Explica identidade do script, objetivo, papel arquitetural, caminhos verificados, variáveis, regras PASS/WARN/FAIL, exit codes, fluxos e cenários BDD.

Objetivo

Tornar o comportamento do verificador compreensível e auditável sem exigir leitura direta do Bash. Funciona como contrato humano do script: para cada propriedade, descreve condição de sucesso, condição de falha e efeito no resultado agregado.

Relação especificação → implementação

README declara o comportamento esperado.

verify-agent-environment.sh implementa esse comportamento.

Um desvio entre os dois é defeito de documentação ou implementação e deve ser resolvido por evidência, não escolhendo arbitrariamente o texto mais conveniente.

Conteúdo observado

Identidade/path/perfil; distinção explícita de que o script é verificador e não fronteira; tabela de paths; tabela de credenciais; semântica de PASS/WARN/FAIL; resultado final; diagramas de fluxo; BDD para usuário, Docker socket, Git, SOURCE_ROOT, managed settings, guard, Codex requirements, credenciais e resultado agregado.

Papel arquitetural

É uma camada de explicabilidade para um controle determinístico. Também fornece critérios reutilizáveis para o Reviewer auditar se o script está testando aquilo que afirma testar.

Vantagem metodológica

Transforma shell procedural em requisitos testáveis. Um cenário “processo root → FAIL” é semanticamente mais claro do que inferir intenção a partir de um if. Essa separação ajuda a detectar bugs onde o script executa mas o oráculo está errado.

Riscos

README ficar desatualizado; BDD descrever check inexistente; exemplos virarem fatos sobre o estado atual; documentar mode/path diferente do runtime; duplicar fonte normativa sem regra de precedência.

Critério de qualidade

Cada afirmação sobre comportamento do script deve ser verificável lendo o Bash ou executando fixture/runtime. A documentação deve diferenciar “o script verifica X” de “X está verdadeiro neste momento”.

Mapeamento para SYMBOL_REGISTRY

É fonte de definição para os predicados implementados pelo script e para a semântica de BASE_CONTAINER_CHECK. O registry deve referenciar README e implementação, preservando a distinção entre SPECIFIED_CHECK e OBSERVED_RESULT.

Revisão de conformidade — drift entre especificação e integração

STATUS: DOCUMENTATION_DRIFT.

O README atual informa “Manual ou via postStartCommand do devcontainer”. Contudo, .devcontainer/devcontainer.json em main possui postStartCommand dedicado apenas à criação/verificação de /home/agent/.claude/plans e não chama verify-agent-environment.sh. Portanto, o modo “via postStartCommand” não está materializado no Executor atual. A documentação deve ser lida como possibilidade/intenção, não como integração vigente comprovada.

22 — Snapshot anterior

devcontainer.json.before-git-auth-boundary-20260807T111848Z

Identidade

Path comprovado: .devcontainer/devcontainer.json.before-git-auth-boundary-20260807T111848Z.

Classe: HISTORICAL_SNAPSHOT / CONFIGURATION_BASELINE.

Domínio principal: Configuration Management, Change Traceability e Forensic Comparison.

Definição

É um snapshot preservado de uma versão anterior do devcontainer.json antes de uma mudança de fronteira relacionada a Git/autorização. O sufixo temporal no nome serve para identificar a posição histórica da configuração.

Objetivo

Permitir comparação BEFORE/AFTER, reconstruir decisões, diagnosticar regressões e comprovar quais controles foram adicionados ou alterados. Ele não deve ser carregado automaticamente como configuração ativa.

Papel arquitetural

É evidência histórica. Seu valor vem da comparação com o arquivo canônico .devcontainer/devcontainer.json e com commits/diffs correspondentes. Ajuda a responder “o que mudou?” sem depender da memória do agente ou de narrativa posterior.

Conteúdo observado

Mantém identidade CEPRAEA Agent, build, workspace, agent user, no-new-privileges, cap-drop, mounts de vários paths e neutralização de credenciais. A diferença material deve ser analisada contra a versão posterior, não assumida pelo nome do arquivo.

Autoridade

Nenhuma autoridade operacional corrente. Se houver divergência com devcontainer.json atual, o snapshot perde por definição como configuração vigente. Só pode ser fonte de fato histórico: “nesta versão preservada, o arquivo continha X”.

Riscos

Agente localizar o arquivo por glob e tratá-lo como config ativa; copiar trechos antigos para corrigir problema atual; usar estado histórico como prova de controle presente; acumular snapshots sem referência ao commit/decisão correspondente.

Boa prática

Snapshots devem permanecer claramente nomeados, excluídos de mecanismos automáticos que procurem devcontainer.json e vinculados a uma mudança/decisão quando seu valor histórico justificar manutenção. Git normalmente já fornece histórico; arquivo snapshot separado só deve existir quando há razão operacional concreta.

Mapeamento para SYMBOL_REGISTRY

Não deve definir símbolos normativos. Pode participar de provenance: CONFIG_SNAPSHOT, PREVIOUS_STATE e CHANGE_EVIDENCE. Símbolos de runtime devem apontar sempre para configuração vigente.

23 — Taxonomia e precedência

Taxonomia, precedência e responsabilidades

Objetivo

Estabelecer uma taxonomia única para interpretar todos os arquivos do catálogo e impedir que responsabilidades de camadas distintas sejam misturadas.

Taxonomia funcional

ARCHITECTURE — define desenho, blocos, relações, restrições e quality goals.

ARCHITECTURE_REALIZATION — mapeia desenho para arquivos concretos.

ARCHITECTURE_TRANSITION — define como implantar e provar readiness.

GOVERNANCE_POLICY — define autoridade e invariantes comuns.

ROLE_CONTRACT — define comportamento transversal de um papel.

TASK_SPECIFICATION — define contrato de uma unidade de trabalho.

RUNBOOK_ARCHITECTURE — define catálogo/seleção de procedimentos.

RUNBOOK_INSTANCE — procedimento reutilizável de uma classe de operação.

ENVIRONMENT_AS_CODE — materializa runtime e fronteiras do ambiente.

MANAGED_POLICY/REQUIREMENTS — restringe capacidades específicas da ferramenta.

GUARD — decide/bloqueia antes de um efeito.

OBSERVABILITY_HOOK — registra depois do evento.

VERIFIER — testa predicados observáveis.

VERIFIER_SPECIFICATION — documenta os oráculos do verificador.

AUDIT_ANALYSIS — interpreta evidências e identifica gaps.

HISTORICAL_SNAPSHOT — preserva estado anterior.

Precedência normativa

1. Autoridade humana e decisões materiais registradas.

2. AGENT_POLICY.md para invariantes e autoridade operacional comuns.

3. Fontes canônicas de domínio e arquitetura aplicáveis.

4. CLAUDE.md ou AGENTS.md conforme o papel.

5. task/plan aprovado e seus critérios.

6. runbook_binding e runbooks aplicáveis.

7. procedimento concreto.

Enforcement não é uma camada “abaixo” que possa redefinir a norma. Ele materializa a norma que é tecnicamente aplicável. Se um enforcement permitir algo que a política proíbe, existe gap. Se um enforcement proibir algo que a política permite e a task necessita, existe incompatibilidade operacional. Ambos precisam de correção explícita.

Matriz de perguntas

Arquitetura: por que e como o sistema é dividido?

Policy: quem pode fazer o quê?

Role contract: como esse agente deve se comportar sempre?

Task: o que deve ser feito agora e como provar DONE?

Runbook: como executar/revisar esta classe de operação?

Enforcement: o ambiente permite ou bloqueia a capacidade?

Verifier: a propriedade está realmente presente?

Audit report: o conjunto é coerente e suficiente?

Snapshot: como era antes?

Taxonomia de estados

Workflow Executor: READY_FOR_REVIEW | BLOCKED.

Workflow Reviewer: PASS | FAIL | HUMAN_DECISION_REQUIRED.

Estado epistemológico de infraestrutura: DECIDIDO | IMPLANTADO | VALIDADO | PENDENTE | REJEITADO | SUBSTITUÍDO | NÃO APLICÁVEL.

Resultado de command/check: PASS/FAIL + exit code e output.

Esses espaços de estado não devem ser colapsados. “PASS do lint” não é “PASS do Reviewer”; “VALIDADO o container” não significa “task aprovada”.

Taxonomia de evidência

Configuration evidence: conteúdo/hash/path/ownership.

Runtime evidence: efeito observado durante execução real.

Behavioral agent evidence: tentativa real via Claude/Codex.

Git evidence: status, diff, SHA, histórico.

Test evidence: comando, exit code, output reproduzível.

Human decision evidence: decisão explícita e, quando material, registro canônico.

Observability event: registro de ocorrência, sem inferir correção.

Regra de responsabilidade única

Cada arquivo deve possuir uma função dominante. Duplicação mínima pode existir para defense in depth e clareza, mas não deve criar duas fontes concorrentes. A política pode declarar uma proibição que o guard também aplica; isso é coerente porque uma é norma e outra enforcement. Duas policies diferentes definindo autoridades incompatíveis são incoerência.

Regra para linguagem futura

Usar verbos tecnicamente diferenciados: DEFINE, REQUIRES, ALLOWS, DENIES, OBSERVES, VERIFIES, PROVES, RECORDS, REVIEWS, APPROVES. Evitar “garante” quando o artefato apenas instrui ou observa.

Revisão de conformidade — precedência corrigida por concern

STATUS: MODELO DE PRECEDÊNCIA REFINADO.

Para governança operacional dos agentes, a sequência compatível com runbooks/README.md é: HUMAN_AUTHORITY → AGENT_POLICY → CANONICAL_DOMAIN_AND_ARCHITECTURE_SOURCES → ROLE_CONTRACT → APPROVED_TASK/PLAN → RUNBOOK_BINDING/RUNBOOKS → EXECUTION. Isso não significa que AGENT_POLICY possa redefinir fatos do domínio; significa que ela governa a autoridade operacional com que agentes consomem as fontes. Quando duas fontes de camadas superiores contradizem materialmente uma execução, a regra não é escolher silenciosamente uma: Executor=BLOCKED; Reviewer=HUMAN_DECISION_REQUIRED.

24 — Integração SYMBOL_REGISTRY

Integração futura com SYMBOL_REGISTRY

Status

O SYMBOL_REGISTRY ainda deve ser tratado como especificação em construção, não como enforcement ativo do CEPRAEA BEACH PRO. Esta guia define sua posição correta em relação aos arquivos documentados.

Problema que o registry resolve

Os mesmos conceitos aparecem em vários artefatos: TASK, EXECUTOR, REVIEWER, PASS, FAIL, BLOCKED, READY_FOR_REVIEW, BASELINE, WRITE_SCOPE, EVIDENCE, VALIDATED, HUMAN_DECISION_REQUIRED. Sem definição canônica, agentes podem interpretar a mesma palavra de maneiras diferentes conforme o arquivo lido.

Papel correto

O SYMBOL_REGISTRY deve ser léxico semântico e mapeamento símbolo → tipo → autoridade → ação/predicado → mecanismo → evidência. Ele não substitui arquitetura, policy, task schema, runbook nem test suite. Ele fornece identidade semântica compartilhada entre essas camadas.

Estrutura mínima por símbolo

SYMBOL_ID.

Canonical name.

Class: ENTITY | ROLE | STATE | ACTION | RELATION | CONSTRAINT | PREDICATE | EVIDENCE | DECISION | FAILURE.

Type/domain.

Definition.

Source of authority.

Allowed consumers.

Inputs/outputs quando aplicável.

Preconditions.

Semantics/action.

Postconditions.

Evidence oracle.

Failure semantics.

Runtime binding.

STATUS: RASCUNHO | DEFINED | BOUND | VERIFIED.

Exemplo de decomposição

REVIEWER_READ_ONLY não deve significar apenas “AGENTS.md diz que Codex não edita”.

Definition: Reviewer não possui capacidade de modificar o candidate/workspace durante review normal.

Normative source: arquitetura + AGENT_POLICY/AGENTS.

Runtime binding: .devcontainer/reviewer/devcontainer.json + codex-requirements.toml.

Oracle: tentativa de escrita pelo processo real retorna falha; candidate/diff permanece inalterado.

Evidence: comando/tentativa, resultado, git diff/status antes/depois.

Outro exemplo

BASE_CONTAINER_CHECK não significa “arquitetura inteira validada”.

Definition: conjunção dos checks blocking implementados por verify-agent-environment.sh.

Implementation source: script.

Specification source: README.

Output: PASS/FAIL.

Scope: somente propriedades cobertas pelo script.

Explicit non-implication: não prova CTs comportamentais dos agentes nem fluxo end-to-end.

Regras de design

1. Um símbolo canônico = um significado.

2. Um significado normativo não deve possuir alias ambíguo sem registro.

3. Símbolos de espaços de estado diferentes devem ser qualificados quando houver colisão, por exemplo REVIEW_PASS versus CHECK_PASS.

4. Símbolo sem runtime binding não pode ser descrito como enforced.

5. Símbolo sem evidence oracle não pode ser descrito como verified.

6. UNKNOWN/MISSING/UNVERIFIED nunca se convertem implicitamente em PASS.

7. Exemplos e snapshots não definem símbolos normativos.

Integração com task_atomics

O task schema pode referenciar símbolos/enum canônicos para estados, roles, operation_classes e failure semantics. Isso reduz prosa, mas não deve transformar todas as regras de negócio do produto em abreviações opacas.

Integração com CLAUDE.md/AGENTS.md

Os adaptadores devem usar nomes canônicos para outputs e boundaries. O objetivo não é tornar prompts “matemáticos”; é eliminar ambiguidade operacional.

Integração com enforcement

Managed settings, requirements, guards e containers devem aparecer como bindings de símbolos, não como definições semânticas primárias. Um path pode mudar sem mudar o conceito; o registry registra a ligação vigente.

Critério para ativação

O registry só deve controlar execução quando: todos os símbolos obrigatórios estiverem definidos; aliases/colisões resolvidos; bindings de runtime confirmados; oráculos definidos; falhas testadas; consumidores atualizados; humano aprovar a versão. Até lá, sua função é specification-only.

25 — Revisão de conformidade

Revisão de conformidade do catálogo

# Baseline auditada

Repositório: cepraea/beach-pro

Branch: main

HEAD auditado: ecef4f1be987471f23a9ed712597f701ad1b3f64

Método: confronto entre cada guia do catálogo, arquivos atuais de main, documentos arquiteturais, decisões versionadas e relações de enforcement/verificação.

# Legenda

CONFORME = descrição do catálogo compatível com a fonte atual auditada.

AJUSTE_APLICADO = a descrição principal continua útil, mas recebeu nota de revisão por omissão, drift, conflito ou atualização factual.

HISTÓRICO = artefato válido como evidência/registro temporal, sem autoridade operacional corrente automática.

SPEC_ONLY = proposta/especificação ainda não ativa como enforcement.

NÃO_COMPROVADO = propriedade que requer runtime ou evidência adicional.

# Findings materiais

F-01 — Architecture vs as-built Git boundary. A revisão arquitetural descreve .git gravável/não montado read-only, mas main monta .git read-only no Dev Container do Executor. O registro DEC-CTR-013 descreve a supersessão, porém seu próprio status de governança está PROPOSTA por ausência de artefato verificável de aprovação. Resultado: enforcement as-built e arquitetura documental não estão plenamente reconciliados.

F-02 — Dois contextos de Dev Container. main possui Executor e Reviewer separados; DEC-CTR-015 documenta essa evolução, mas também permanece PROPOSTA no plano de governança. O boundary técnico existe; a ratificação documental permanece incompleta.

F-03 — SOURCE_ROOT/.drive possui semântica conflitante. AGENT_POLICY atual declara que .drive/** não é fonte autoritativa por padrão e que fontes controladas são designadas por tarefa/plano. Managed settings atual nega Read para .drive/CEPRAEA BEACH PRO/** e .drive/BEACH HANDBALL/**. O verificador, porém, ainda exige SOURCE_ROOT existente e read-only, e o Dev Container Executor não possui mount read-only específico para .drive. Não declarar SOURCE_ROOT_PROTECTED ou SOURCE_ROOT_READABLE como verdade global sem reconciliar esses mecanismos e reexecutar os testes.

F-04 — Biblioteca de runbooks evoluiu. O inventário atual contém quatro runbooks do Executor, três shared e cinco do Reviewer. dependency_change resolve para RB-REV-005-dependency-review.md; RB-REV-004 permanece complementar para revisão de evidência.

F-05 — README do verificador contém drift de integração. Ele afirma execução manual ou via postStartCommand do devcontainer, mas o devcontainer Executor atual usa postStartCommand apenas para preparar /home/agent/.claude/plans; não chama verify-agent-environment.sh.

F-06 — Branch main não está protegida no baseline auditado. A API do repositório reporta protected=false e required status checks desabilitados. Isso não invalida os arquivos revisados, mas é um gap relevante de governança/repository assurance.

F-07 — CONTAINER-RUNBOOK possui colisão de autoridade. O próprio arquivo se chama fonte de verdade operacional, enquanto Runbooks.md determina que ele seja usado exclusivamente como referência estrutural e conceitual neste contexto. A interpretação do catálogo segue Runbooks.md e trata o CONTAINER-RUNBOOK como referência/histórico, não como autoridade automática sobre o estado corrente.

# Revisão individual das guias

00 — Visão geral: AJUSTE_APLICADO — explicitada natureza não normativa do catálogo e baseline auditada.

01 — Arquitetura-mãe: AJUSTE_APLICADO — drift de .git e dois contextos registrado; governança de supersessão ainda não ratificada no repositório.

02 — Materialização: AJUSTE_APLICADO — “nove arquivos” classificado como baseline histórico, não inventário atual.

03 — Implantação: AJUSTE_APLICADO — incorporado estado probatório dos CTs registrado na própria fonte; DoD global não deve ser inferido como concluído.

04 — AGENT_POLICY.md: AJUSTE_APLICADO — corrigida semântica atual de .drive/fontes controladas e registrado pequeno defeito textual na lista do control plane.

05 — CLAUDE.md: CONFORME.

06 — AGENTS.md: CONFORME.

07 — task_atomics.md: AJUSTE_APLICADO — adicionados metacampos obrigatórios do schema e limite do validador leve.

08 — Runbooks.md: AJUSTE_APLICADO — inventário atual inclui RB-REV-005 e runbooks/README.md é o catálogo normativo de seleção.

09 — CONTAINER-RUNBOOK: AJUSTE_APLICADO / HISTÓRICO — colisão de autoridade explicitada.

10 — Relatório multi-agentes: AJUSTE_APLICADO — classificado como snapshot analítico temporal; claims precisam ser revalidados contra configuração atual.

11 — Claude managed settings: AJUSTE_APLICADO — incluídos deny atuais para leitura de dois corpora .drive.

12 — Codex requirements: CONFORME quanto ao conteúdo estático; efetividade de runtime continua NÃO_COMPROVADA sem teste real.

13 — pretool: CONFORME quanto ao código atual e aos limites já declarados.

14 — posttool: CONFORME.

15 — gitconfig-agent: CONFORME.

16 — managed MCP: CONFORME; mcpServers={} não prova ausência universal de MCP em todas as camadas.

17 — Dockerfile: CONFORME quanto ao build spec atual; efetividade depende do runtime construído.

18 — Dev Container Executor: AJUSTE_APLICADO — as-built validado contra main e drift arquitetural de .git explicitado.

19 — Dev Container Reviewer: AJUSTE_APLICADO — configuração atual confirmada; separação técnica existe, ratificação de DEC-CTR-015 permanece PROPOSTA.

20 — verify-agent-environment: AJUSTE_APLICADO — definição do verificador confirmada, mas resultado corrente não foi inferido; SOURCE_ROOT exige reconciliação/rerun.

21 — README do verificador: AJUSTE_APLICADO — drift do postStartCommand registrado.

22 — Snapshot anterior: CONFORME / HISTÓRICO — arquivo existe e não possui autoridade operacional corrente.

23 — Taxonomia e precedência: AJUSTE_APLICADO — precedência operacional harmonizada com runbooks/README.md e separada por concern.

24 — Integração SYMBOL_REGISTRY: CONFORME / SPEC_ONLY — continua corretamente fora do enforcement ativo.

# Conclusão

O catálogo permanece tecnicamente útil, mas não deve ser chamado de prova de conformidade do SDLC. Ele é um catálogo de referência auditado. As principais pendências reais estão na reconciliação entre arquitetura documental e enforcement as-built, na governança das decisões DEC-CTR-013/015, na semântica de SOURCE_ROOT/.drive, no rerun dos testes de ambiente/agentes e na ausência de proteção da branch main.