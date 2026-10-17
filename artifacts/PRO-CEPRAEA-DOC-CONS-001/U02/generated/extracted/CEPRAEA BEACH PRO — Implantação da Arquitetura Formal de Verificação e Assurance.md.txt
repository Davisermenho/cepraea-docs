# CEPRAEA BEACH PRO — Implantação da Arquitetura Formal de Verificação e Assurance

STATUS: RASCUNHO
VERSÃO: 0.0.1

*Documento de governança operacional para reduzir risco, manter a autoridade humana informada e preservar rastreabilidade durante a implantação da nova arquitetura.*

## GUIA 0 — IDENTIFICAÇÃO, BASELINE E ESCOPO

**Repositório**
cepraea/beach-pro

Branch padrão
main

Branch de trabalho atualmente existente
feat/cepraea-domain-modeling

Branch destinada à implantação da nova arquitetura

PENDENTE DE DECISÃO HUMANA. Nenhuma branch nova foi criada por este documento. A política atual reserva criação, alteração e promoção de refs Git ao humano.

Recomendação não aprovada

Criar uma branch dedicada, separada da modelagem de domínio, por exemplo feat/formal-verification-control-plane. Essa recomendação só se torna decisão após aprovação explícita do humano.

Fontes de autoridade e evidência consultadas no repositório

• AGENT_POLICY.md
• CLAUDE.md
• AGENTS.md
• runbooks/README.md
• runbooks/shared/RB-SHARED-003-failure-states.md
• runbooks/reviewer/RB-REV-001-code-review.md
• runbooks/reviewer/RB-REV-004-evidence-review.md
• .ai/control/task-proposal.schema.json
• .ai/control/verification-plan.schema.json
• .ai/task-proposal.example.json
• .ai/task-approval.example.json
• .drive/FVR-1.0/IMPLEMENTATION_GUIDE.md
• .drive/FVR-1.0/CONFORMANCE_CERTIFICATE_NOT_ISSUED.json
• .devcontainer/Dockerfile
• .devcontainer/devcontainer.json
• docs/arquiteturas/multi-agentes/Human-Governed Dual-Agent SDLC Architecture.md

Observação de risco do baseline GitHub

No baseline consultado, a API do GitHub informou protected=false para main. Isso significa que a regra de controle humano existe na política do projeto, mas não está atualmente respaldada por branch protection do GitHub. Qualquer alteração dessa configuração exige decisão humana e deve ser tratada como mudança de controle.

Escopo deste documento

Este documento governa a implantação da camada formal de contrato e verificação no SDLC. Não altera o runtime do PWA, não substitui o Executor, não substitui o Reviewer e não concede autoridade de aprovação a agentes.

1 — Estado Atual

ESTADO ATUAL DA ARQUITETURA

1.1 Arquitetura operacional vigente

O fluxo atual é um Human-Governed Dual-Agent SDLC:

Humano → Claude Code EXECUTOR → validações determinísticas → working tree/git diff → Codex REVIEWER → Humano → Git.

A política comum estabelece:

• o humano é a autoridade final sobre domínio, decisões materiais, Git, release e deploy;

• Claude Code é o EXECUTOR;

• Codex é o REVIEWER independente;

• produção, revisão e aprovação são funções distintas;

• nenhum agente pode aprovar ou promover o próprio trabalho;

• operações Git que alteram refs, index, histórico ou remoto pertencem ao humano;

• restrições não podem ser contornadas; incapacidade legítima gera BLOCKED ou HUMAN_DECISION_REQUIRED.

1.2 Executor

O Executor:

• recebe a tarefa autorizada;

• lê o contexto necessário;

• identifica validadores aplicáveis;

• produz somente a mudança autorizada;

• executa validações determinísticas;

• corrige erros mecânicos;

• inspeciona git diff, git diff --check e git status;

• entrega READY_FOR_REVIEW ou BLOCKED.

O Executor não possui autoridade para declarar a entrega homologada.

1.3 Reviewer

O Reviewer:

• opera de forma independente;

• inspeciona diff, status, arquivos-alvo, critérios e evidências;

• procura regressões;

• tenta refutar conclusões materiais;

• verifica rastreabilidade e suficiência de evidência;

• reexecuta checks proporcionalmente ao risco;

• não corrige findings nem altera os artefatos sob revisão;

• emite PASS, FAIL ou HUMAN_DECISION_REQUIRED.

O Reviewer continua obrigatório na arquitetura vigente.

1.4 Validação determinística existente

Já existem validadores determinísticos e uma estrutura FVR. O verification-plan suporta operações como file.exists, file.sha256, git.diff, git.diff_names e process.run em sandbox, além de assertions identificadas por AC-NNN e INV-NNN.

Entretanto, o task-proposal ainda representa critérios de aceite principalmente por strings humanas: condição, método e esperado. Portanto, existe um gap entre a tarefa textual e as assertions formais.

1.5 Estado do FVR

O pacote FVR existente se declara implementation candidate. A conformidade não é concedida apenas porque o runner executa.

O certificado disponível registra NOT_ISSUED / HARNESS_INVALID. Logo, não existe evidência suficiente, no baseline atual, para tratar o runner FVR como verificador conformante de produção do fluxo.

1.6 Gap principal

Estado atual:

Task Proposal textual → Executor → validadores → Reviewer.

Gap:

não existe ainda uma camada normativa completa que faça a transformação:

requisito humano → propriedade formal tipada → observação determinística → assertion → PASS/FAIL/BLOCKED.

1.7 Riscos atuais relevantes para a implantação

R-001 — Critérios de aceite textuais permitem interpretação diferente entre Executor e Reviewer.

R-002 — Um validador pode ser determinístico e ainda implementar uma regra formal incorreta.

R-003 — O FVR ainda não possui conformidade comprovada no ambiente atual.

R-004 — Ausência de ligação completa por hash entre proposta, contrato, plano e resultado pode permitir drift.

R-005 — Reviewer ainda precisa recalcular fatos que poderiam ser decididos mecanicamente.

R-006 — Uma propriedade formal incompleta pode produzir PASS técnico sem representar toda a intenção humana.

R-007 — A branch main aparece sem branch protection no baseline observado.

R-008 — Alterar simultaneamente policy, schemas, runner, container e runbooks ampliaria excessivamente o blast radius.

2 — Arquitetura Final

ESTADO PRETENDIDO COM A ARQUITETURA FINAL

2.1 Arquitetura final pretendida

Autoridade Humana

↓

Task Proposal

↓

Task Contract formal

↓

Verification Plan

↓

Aprovação humana vinculada por hashes

↓

Claude Code — Executor

↓

Artefato candidato

↓

Verifier determinístico

↓

PASS | FAIL | BLOCKED

↓

Codex — Reviewer independente

↓

PASS | FAIL | HUMAN_DECISION_REQUIRED

↓

Homologação humana

↓

Git / promoção

2.2 Separação de funções

Executor ≠ Verifier ≠ Reviewer ≠ Autoridade Humana.

Executor

Produz e corrige o artefato candidato.

Verifier

Calcula propriedades formalizadas a partir de observações reproduzíveis.

Reviewer

Realiza assurance independente sobre semântica residual, regressões, completude, adequação de testes, suficiência de evidência, overclaims e possíveis lacunas do contrato.

Humano

Define significado, autoriza contrato e escopo, resolve decisões materiais, homologa e executa transições Git privilegiadas.

2.3 Regra matemática de decisão formal

Cada propriedade Pi assume exatamente um dos estados:

TRUE, FALSE ou UNKNOWN.

FAIL se existir pelo menos uma propriedade FALSE.

BLOCKED se não existir FALSE e existir pelo menos uma propriedade UNKNOWN.

PASS somente se todas as propriedades forem TRUE.

Ausência de evidência nunca é convertida em PASS.

2.4 Regra de precedência

FormalResult != PASS implica que o Reviewer não pode emitir PASS sobre a tarefa.

FormalResult == PASS não obriga Reviewer PASS.

Uma decisão humana que considere o contrato incorreto deve gerar revisão do contrato, nova aprovação e nova verificação. Não deve existir bypass narrativo que converta uma propriedade formal falsa em verdadeira.

2.5 Contrato formal da tarefa

Cada Task Contract deve possuir, no mínimo:

• contract_id e versão;

• task_id e vínculo com a proposta;

• baseline Git;

• read-set;

• write-set;

• forbidden-set;

• invariantes;

• critérios de aceite;

• propriedades formais;

• propriedades residuais de review;

• procedimentos de observação;

• bindings de evidência;

• política fail-closed;

• hashes de integridade.

2.6 Álgebra mínima de propriedades

A primeira versão deve ser pequena e auditável. Operadores recomendados:

exists

equals

not_equals

subset

disjoint

count_eq

count_le

unique

regex_match

sha256_equals

git_ref_equals

changed_paths_subset

exit_code_equals

json_schema_valid

no_orphan_references

Não introduzir linguagem arbitrária de script dentro do contrato quando um operador fechado puder representar a regra.

2.7 Verification Package

O verifier deve produzir resultado estruturado com:

• contract_id;

• hashes do contrato, plano e runner;

• baseline observado;

• resultado global;

• resultado de cada assertion;

• observações;

• contraexemplos para propriedades falsas quando disponíveis;

• causas de UNKNOWN/BLOCKED;

• integridade do package.

2.8 Objetivo de segurança

A correção da entrega deve depender progressivamente menos da confiança no texto produzido por LLMs e mais de:

• propriedades formalizadas;

• execução determinística;

• isolamento;

• evidência reproduzível;

• revisão independente;

• homologação humana.

3 — Decisões Humanas

REGISTRO DAS DECISÕES HUMANAS

3.1 Decisões confirmadas

HDEC-001 — Autoridade humana final

Status: CONFIRMADA.

Decisão: o humano permanece autoridade final sobre domínio, decisões materiais, Git privilegiado, release, deploy e homologação.

HDEC-002 — Manutenção do Executor

Status: CONFIRMADA.

Decisão: Claude Code permanece como EXECUTOR.

HDEC-003 — Manutenção do Reviewer

Status: CONFIRMADA.

Decisão: Codex permanece como REVIEWER independente. A nova camada formal não elimina o Reviewer.

HDEC-004 — Separação de funções

Status: CONFIRMADA.

Decisão: produção, verificação, revisão e homologação permanecem funções distintas; nenhum agente aprova o próprio trabalho.

HDEC-005 — Objetivo da nova arquitetura

Status: CONFIRMADA.

Decisão: a implantação deve diminuir riscos, manter o humano informado e preservar rastreabilidade do trabalho.

HDEC-006 — Verificação determinística antes do review

Status: CONFIRMADA PELO DIRECIONAMENTO DA NOVA ARQUITETURA.

Decisão: uma camada formal/determinística deve avaliar propriedades verificáveis antes do Reviewer.

HDEC-007 — Preservação de fail-closed

Status: CONFIRMADA PELO FLUXO VIGENTE E PELO OBJETIVO DE RISCO.

Decisão: ausência ou insuficiência de evidência não autoriza PASS; deve resultar em BLOCKED, FAIL ou decisão humana conforme a causa.

HDEC-008 — Plano em tasks atômicas

Status: CONFIRMADA.

Decisão: a implantação deve ser decomposta em tasks atômicas, com escopo limitado, critérios observáveis e handoff rastreável.

HDEC-009 — Runbook de implantação

Status: CONFIRMADA.

Decisão: a execução da mudança deve seguir um runbook explícito, com pré-condições, gates, evidências, estados de saída e rollback.

HDEC-010 — Registro no Google Drive

Status: CONFIRMADA.

Decisão: este Google Doc é o registro humano central para acompanhamento da implantação e das decisões materiais.

3.2 Decisões ainda pendentes de autoridade humana

PEND-001 — Nome e criação da branch dedicada de implantação.

Recomendação: feat/formal-verification-control-plane.

Não executar sem decisão humana.

PEND-002 — Estratégia de branch protection para main.

Fato de baseline: protected=false na API consultada.

Decisão necessária: habilitar ou manter sem proteção técnica externa.

PEND-003 — Local definitivo do runner/verifier.

Recomendação: scripts/ci/task-verifier/** ou outro caminho protegido equivalente.

Decisão humana necessária antes de alterar o control plane.

PEND-004 — Promoção do FVR candidate.

Decisão: somente considerar o FVR como autoridade operacional após conformance harness CONFORMANT e todos os vetores obrigatórios PASS.

PEND-005 — Momento em que o novo gate deixa de ser piloto e se torna obrigatório.

Recomendação: após fixtures negativas, piloto real, review independente e homologação humana.

PEND-006 — Política de compatibilidade/migração de task-proposal v1.0.

Opções: migração in-place para v2.0 ou coexistência temporária v1/v2.

PEND-007 — Assinatura/attestation humana.

Decisão necessária sobre uso real de assinatura criptográfica, trusted UI ou somente digest/handoff humano no MVP.

3.3 Regra de manutenção deste registro

Toda decisão pendente transformada em decisão final deve receber:

• ID estável;

• status;

• decisão literal;

• autor humano;

• artefatos afetados;

• motivo;

• efeito sobre tasks já executadas;

• necessidade ou não de reexecução.

Não substituir silenciosamente uma decisão antiga. Registrar supersessão explícita.

4 — Plano de Tasks

PLANO COMPLETO EM TASKS ATÔMICAS

Princípio

Uma task atômica deve produzir um único resultado verificável, não misturar decisões humanas com implementação mecânica e não avançar automaticamente quando sua pós-condição falhar.

FASE A — GOVERNANÇA E BASELINE

TASK-ARCH-001 — Homologar o escopo da mudança arquitetural

Owner: Humano.

Entrada: este documento e arquitetura vigente.

Ação: confirmar quais componentes de control plane podem ser alterados.

Saída: decisão humana explícita.

Gate: sem aprovação, nenhuma task de escrita do control plane inicia.

TASK-ARCH-002 — Definir a branch de implantação

Owner: Humano.

Ação: escolher nome, base e política de integração.

Saída: branch autorizada.

Gate: branch diferente de main para execução por agentes.

TASK-ARCH-003 — Capturar baseline imutável da execução

Owner: Executor, somente inspeção.

Ação: registrar HEAD da branch, HEAD de main, git status e hashes dos arquivos de controle relevantes.

Saída: baseline verificável.

Gate: working tree e refs coerentes com a tarefa aprovada.

TASK-ARCH-004 — Definir critérios de rollout

Owner: Humano + Reviewer.

Ação: fixar condições que diferenciam PILOT, READY e MANDATORY.

Saída: critérios binários de promoção.

Gate: critérios não podem depender de opinião narrativa indefinida.

TASK-ARCH-005 — Decidir branch protection

Owner: Humano.

Ação: avaliar risco de main sem proteção e decidir configuração.

Saída: decisão registrada; alteração de GitHub somente se autorizada.

FASE B — MODELO FORMAL DO CONTRATO

TASK-ARCH-006 — Criar task-contract.schema.json

Owner: Executor.

Ação: definir estrutura normativa do Task Contract.

Saída: schema válido.

Gate: additionalProperties controlado, IDs e hashes tipados.

TASK-ARCH-007 — Criar assertion.schema.json

Owner: Executor.

Ação: definir a estrutura de uma propriedade verificável.

Saída: schema com domain, operator, operands, expected e observation binding.

Gate: nenhuma assertion aceita lógica textual arbitrária como autoridade.

TASK-ARCH-008 — Criar verification-result.schema.json

Owner: Executor.

Ação: definir PASS, FAIL e BLOCKED e a estrutura das evidências/violações.

Saída: schema validável.

Gate: resultado global derivável dos resultados individuais.

TASK-ARCH-009 — Criar task-approval.schema.json

Owner: Executor.

Ação: transformar o example de aprovação em schema normativo.

Saída: approval vinculada por digest à proposta, contrato, plano e baseline.

Gate: alteração de qualquer artefato vinculado invalida approval anterior.

TASK-ARCH-010 — Evoluir task-proposal

Owner: Executor.

Ação: adicionar IDs estáveis de critérios e classificação formal/reviewer.

Saída: schema de proposta atualizado ou nova versão.

Gate: compatibilidade decidida pela PEND-006.

TASK-ARCH-011 — Criar catálogo fechado de operadores v1

Owner: Executor + Reviewer.

Ação: especificar semântica exata dos operadores mínimos.

Saída: catálogo normativo testável.

Gate: cada operador deve ter truth table ou regra computável.

TASK-ARCH-012 — Criar fixtures de schemas

Owner: Executor.

Ação: produzir casos ACCEPT/REJECT para proposta, contrato, assertion, approval e resultado.

Saída: suíte de fixtures.

Gate: ao menos um caso negativo por invariante estrutural material.

TASK-ARCH-013 — Verificar cobertura Proposal → Contract → Plan

Owner: Reviewer.

Ação: tentar encontrar critérios que desapareçam na transformação.

Saída: finding ou PASS.

Gate: conjunto de IDs materiais preservado sem órfãos.

FASE C — VERIFIER DETERMINÍSTICO

TASK-ARCH-014 — Definir modelo de observações

Owner: Executor.

Ação: mapear cada operador para observações reproduzíveis.

Saída: contrato de observation types.

TASK-ARCH-015 — Implementar avaliação ternária

Owner: Executor.

Ação: implementar TRUE/FALSE/UNKNOWN e agregação global.

Saída: evaluator determinístico.

Gate: FAIL tem precedência sobre UNKNOWN; UNKNOWN sem FALSE resulta BLOCKED.

TASK-ARCH-016 — Implementar changed_paths e conjuntos de arquivos

Owner: Executor.

Ação: suportar subset/disjoint sobre paths observados.

Saída: verificação de write-set e forbidden-set.

TASK-ARCH-017 — Implementar integridade por SHA-256

Owner: Executor.

Ação: verificar contrato, plano, runner e fontes read-only pinadas.

Saída: checks de digest.

TASK-ARCH-018 — Implementar checks de processo

Owner: Executor.

Ação: executar ferramentas permitidas em sandbox e capturar exit code/stdout/stderr como evidência.

Saída: observações processuais estruturadas.

TASK-ARCH-019 — Implementar validação de schema e referências

Owner: Executor.

Ação: integrar json_schema_valid e no_orphan_references.

Saída: assertions estruturais.

TASK-ARCH-020 — Implementar verification package

Owner: Executor.

Ação: publicar atomicamente resultado, observações, hashes e violações.

Saída: package imutável por run_id.

TASK-ARCH-021 — Proteger o verifier contra autoalteração

Owner: Humano + Executor.

Ação: colocar runner e schemas normativos em caminho protegido/read-only para o Executor em tarefas comuns.

Saída: enforcement técnico.

Gate: tarefa normal não pode editar o mecanismo que a julga.

FASE D — CONFORMIDADE E AMBIENTE

TASK-ARCH-022 — Inventariar requisitos reais do FVR

Owner: Reviewer.

Ação: comparar SYSTEM_REQUIREMENTS, Dockerfile e harness.

Saída: matriz instalado/faltante/incompatível.

TASK-ARCH-023 — Completar dependências do ambiente

Owner: Executor, somente após autorização vermelho-crítico.

Ação: instalar/pinar somente dependências exigidas.

Saída: Dev Container reproduzível.

TASK-ARCH-024 — Executar conformance harness

Owner: Executor.

Ação: executar harness completo.

Saída: relatório de conformidade.

TASK-ARCH-025 — Revisar independentemente a conformidade

Owner: Reviewer.

Ação: reproduzir checks críticos e tentar refutar o resultado.

Saída: PASS/FAIL/HUMAN_DECISION_REQUIRED.

TASK-ARCH-026 — Homologar promoção do verifier

Owner: Humano.

Gate: somente se harness CONFORMANT e todos os vetores mandatórios PASS.

Saída: autorização para uso piloto.

FASE E — INTEGRAÇÃO COM EXECUTOR

TASK-ARCH-027 — Atualizar AGENT_POLICY.md

Owner: Executor, com autorização explícita de control plane.

Ação: registrar Executor ≠ Verifier ≠ Reviewer ≠ Humano e precedência do FormalResult.

Saída: política comum atualizada.

TASK-ARCH-028 — Atualizar CLAUDE.md

Owner: Executor.

Ação: exigir Formal PASS antes de READY_FOR_REVIEW quando task usar o novo contrato.

Saída: protocolo de handoff atualizado.

TASK-ARCH-029 — Atualizar runbooks shared

Owner: Executor.

Ação: incorporar verification package, estados formais e evidências.

Saída: runbooks compartilhados consistentes.

TASK-ARCH-030 — Atualizar runbooks do Executor

Owner: Executor.

Ação: definir sequência contract → execute → verify → correct/block → handoff.

Saída: procedimentos por operation_class.

FASE F — INTEGRAÇÃO COM REVIEWER

TASK-ARCH-031 — Atualizar AGENTS.md

Owner: Executor para a alteração; Codex revisa, não edita.

Ação: impedir PASS quando FormalResult != PASS.

Saída: política do Reviewer atualizada.

TASK-ARCH-032 — Atualizar runbooks do Reviewer

Owner: Executor.

Ação: incluir validação do verification package antes do assurance residual.

Saída: procedimentos reviewer atualizados.

TASK-ARCH-033 — Definir matriz de propriedades formais versus residuais

Owner: Reviewer + Humano.

Ação: classificar o que é decidido pelo verifier e o que permanece em review.

Saída: fronteira explícita.

Gate: nenhuma propriedade material pode ficar sem owner de verificação.

TASK-ARCH-034 — Testar tentativa de bypass

Owner: Reviewer.

Ação: usar fixture Formal FAIL e verificar que Reviewer PASS é rejeitado pelo fluxo.

Saída: evidência fail-closed.

FASE G — DOCUMENTAÇÃO CANÔNICA

TASK-ARCH-035 — Atualizar arquitetura Human-Governed Dual-Agent SDLC

Owner: Executor.

Ação: adicionar Contract Plane e Formal Verification Plane sem remover Execution/Assurance Plane.

Saída: arquitetura final versionada.

TASK-ARCH-036 — Atualizar diagramas e precedência

Owner: Executor.

Ação: documentar estados, transições, autoridade e canais de handoff.

Saída: diagramas coerentes com policies e runbooks.

TASK-ARCH-037 — Revisar consistência documental

Owner: Reviewer.

Ação: comparar arquitetura, policies, schemas e runbooks.

Saída: nenhuma contradição material.

FASE H — PILOTO E PROMOÇÃO

TASK-ARCH-038 — Selecionar tarefa piloto

Owner: Humano.

Critério: pequena, reversível, baixa ambiguidade e propriedades observáveis.

TASK-ARCH-039 — Escrever contrato do piloto

Owner: Executor; humano aprova.

Saída: proposal + contract + verification plan + approval bindings.

TASK-ARCH-040 — Executar piloto

Owner: Claude Code.

Saída: artefato candidato.

TASK-ARCH-041 — Verificar piloto

Owner: Verifier.

Saída: PASS/FAIL/BLOCKED + package.

TASK-ARCH-042 — Revisar piloto

Owner: Codex.

Saída: PASS/FAIL/HUMAN_DECISION_REQUIRED.

TASK-ARCH-043 — Executar failure injection

Owner: Reviewer/Executor conforme fixture.

Casos mínimos: path não autorizado; hash alterado; assertion FALSE; evidência ausente; UNKNOWN; tentativa de alterar verifier; contrato alterado após approval.

TASK-ARCH-044 — Homologar resultado do piloto

Owner: Humano.

Saída: decisão de corrigir, repetir ou promover.

TASK-ARCH-045 — Tornar gate obrigatório

Owner: Humano.

Pré-condição: somente após critérios de rollout atendidos.

Saída: estado MANDATORY.

TASK-ARCH-046 — Encerrar implantação

Owner: Humano + Reviewer.

Ação: confirmar rastreabilidade, decisões finais, artefatos e ausência de pendências bloqueantes.

Saída: arquitetura implantada e homologada.

5 — Runbook

RUNBOOK DE IMPLEMENTAÇÃO

5.1 Objetivo

Executar a implantação da arquitetura formal com blast radius controlado, fail-closed, evidência reproduzível e autoridade humana em todos os pontos materiais.

5.2 Aplicabilidade

Aplicar às TASK-ARCH-001 até TASK-ARCH-046.

5.3 Autoridade e papéis

Humano

Autoriza tasks, branch, mudanças de control plane, Git privilegiado, promoção do verifier e rollout obrigatório.

Claude Code — Executor

Implementa somente a task atômica autorizada e não executa transições Git privilegiadas.

Verifier

Avalia somente propriedades formalizadas. Não interpreta intenção humana.

Codex — Reviewer

Opera read-only sobre artefatos sob revisão, tenta refutar a entrega e não corrige findings.

5.4 Pré-condições obrigatórias antes de cada task

1. Existe uma task ID autorizada.

2. A branch autorizada não é main.

3. git status foi inspecionado.

4. baseline da task foi capturado.

5. arquivos alvo, referência, read-only e proibidos estão identificados.

6. risco foi classificado.

7. runbooks aplicáveis foram carregados.

8. mudanças de control plane possuem autorização humana explícita.

9. nenhuma decisão pendente necessária à task está sendo inferida por agente.

Falha em qualquer pré-condição material → BLOCKED.

5.5 Procedimento padrão por task

PASSO 1 — Baseline

Capturar HEAD, main, status, diff inicial e hashes relevantes.

PASSO 2 — Scope lock

Resolver write-set, read-set e forbidden-set.

PASSO 3 — Implementação mínima

Alterar somente o necessário à task atual.

PASSO 4 — Autoinspeção do Executor

Executar validadores aplicáveis, git diff --check, git diff e git status.

PASSO 5 — Verificação formal

Quando a task já estiver coberta pelo novo mecanismo, executar o verifier sobre o contrato aprovado.

PASSO 6 — Decisão formal

Formal FAIL → corrigir somente dentro do escopo e verificar novamente.

Formal BLOCKED → parar e escalar ao humano.

Formal PASS → preparar handoff.

PASSO 7 — Handoff

Entregar arquivos alterados, validações, verification package, limitações e pontos de review.

PASSO 8 — Review independente

Codex verifica integridade do package, diff, regressões, evidências e residual semântico.

PASSO 9 — Tratamento do verdict

Reviewer FAIL → retorna ao Executor com findings.

Reviewer HUMAN_DECISION_REQUIRED → humano decide.

Reviewer PASS → elegível para homologação humana.

PASSO 10 — Git

Somente o humano executa add/commit/push/merge/rebase ou demais transições privilegiadas.

5.6 Gates de implantação

GATE G0 — GOVERNANCE_READY

Todas as decisões indispensáveis à próxima fase estão explícitas.

GATE G1 — CONTRACT_MODEL_READY

Schemas e operadores possuem fixtures positivas e negativas; coverage Proposal → Contract → Plan não possui órfãos.

GATE G2 — VERIFIER_READY

Evaluator ternário, hashes, observations e package funcionam deterministicamente.

GATE G3 — CONFORMANCE_READY

Harness CONFORMANT e vetores mandatórios PASS.

GATE G4 — DUAL_AGENT_INTEGRATED

Claude exige formal gate; Codex reconhece e respeita precedência formal; runbooks coerentes.

GATE G5 — PILOT_PASS

Piloto real e failure injection completos sem bypass.

GATE G6 — HUMAN_HOMOLOGATED

Humano autoriza MANDATORY.

Nenhum gate pode ser inferido como aprovado por ausência de finding.

5.7 Evidências mínimas por task

• task ID;

• baseline SHA;

• lista de arquivos alterados;

• diff;

• comandos/checks executados;

• exit codes;

• resultados de schemas/testes;

• hashes quando aplicáveis;

• verification package quando aplicável;

• verdict do Reviewer;

• decisão humana quando material;

• commit resultante somente após ação humana.

5.8 Estados de saída

Executor

READY_FOR_REVIEW ou BLOCKED.

Verifier

PASS, FAIL ou BLOCKED.

Reviewer

PASS, FAIL ou HUMAN_DECISION_REQUIRED.

Implantação

PILOT, READY ou MANDATORY, exclusivamente por decisão humana após gates.

5.9 Regras de fail-closed

• UNKNOWN nunca equivale a TRUE.

• Ausência de evidência nunca equivale a PASS.

• Formal FAIL não pode ser convertido em Reviewer PASS.

• Formal PASS não substitui review independente.

• Reviewer PASS não substitui homologação humana.

• Mudança de contrato após approval invalida approval.

• Mudança de runner após hash pinado invalida o run.

• Tentativa de alterar verifier para fazer uma task passar é violação de control plane.

• Contradição entre normas gera HUMAN_DECISION_REQUIRED/BLOCKED, não inferência.

5.10 Rollback

Se uma task introduzir regressão no control plane:

1. parar a sequência;

2. preservar evidência do estado falho;

3. não avançar para task seguinte;

4. humano executa rollback Git ou restauração autorizada;

5. recapturar baseline;

6. corrigir a task em nova execução;

7. repetir verifier e review.

Não realizar rollback silencioso por agente.

5.11 Regra de atualização deste Google Doc

Após cada decisão material ou gate:

• atualizar o ID correspondente;

• registrar estado atual;

• registrar evidência/commit relacionado;

• manter pendências abertas visíveis;

• não apagar histórico decisório; usar supersessão explícita.

5.12 Critério final de conclusão

A implantação só está concluída quando:

• schemas normativos estão válidos;

• Proposal → Contract → Plan possui cobertura integral de IDs materiais;

• verifier possui conformidade comprovada;

• fixtures positivas e negativas passam como esperado;

• fail-closed foi demonstrado por failure injection;

• Executor está integrado ao gate;

• Reviewer está integrado ao gate;

• arquitetura e runbooks estão consistentes;

• piloto foi concluído;

• humano homologou estado MANDATORY;

• rastreabilidade final aponta para decisões, evidências e commits.

Fórmula operacional:

ArchitectureReady =

ContractModelReady

AND VerifierConformant

AND FailClosedProven

AND ExecutorIntegrated

AND ReviewerIntegrated

AND PilotPass

AND HumanHomologated.
