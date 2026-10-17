CEPRAEA BEACH PRO — Arquitetura de Auditoria e Assurance Agêntico

Protocolo de implantação e execução para Claude Code e Codex no VS Code

**Status:** especificação operacional para implantação R0. Este documento define o protocolo de auditoria local baseado em evidência. Ele não autoriza alterações no repositório, não substitui decisão humana e não declara a arquitetura implementada enquanto os critérios de implantação não forem verificados.

# 1. Objetivo

O objetivo é tornar análises, auditorias e avaliações realizadas por agentes de IA suficientemente confiáveis para apoiar decisões de desenvolvimento do CEPRAEA BEACH PRO sem tratar a afirmação de um modelo como fato por si só.

A arquitetura não promete auditoria universalmente 100% correta. O objetivo operacional é impedir PASS silencioso sem evidência, tornar omissões visíveis, exigir reprodução das verificações relevantes e separar claramente fatos, observações, inferências, recomendações e decisões humanas.

Regra central: NO EVIDENCE → NO VERIFIED PASS. Ausência de evidência não significa FAIL; significa UNVERIFIED, salvo quando a própria ausência de uma pré-condição obrigatória constitui uma falha formalmente definida.

# 2. Não objetivos

Esta arquitetura não tenta expor ou registrar chain-of-thought privado de Claude ou Codex. O objeto auditável é a trilha externa de auditoria: alvo, escopo, fontes, comandos, observações, evidências, contraexemplos, limitações e verdicts.

Também não pretende substituir testes por revisão de LLM, transformar concordância entre dois modelos em prova, maximizar governança independentemente de custo, nem introduzir candidate_digest, state machines extensas ou artefatos criptográficos sem risco concreto que os justifique.

# 3. Princípios arquiteturais

P1 — Claim não é evidência. Uma frase como “está correto”, “os testes passaram” ou “não há regressão” é apenas uma afirmação até estar ligada a uma observação verificável.

P2 — Evidência deve ser rastreável ao alvo auditado. Toda evidência precisa identificar a versão, o diretório, o comando ou artefato e a propriedade que pretende sustentar.

P3 — Verificação determinística tem precedência sobre julgamento probabilístico quando a propriedade pode ser formalizada.

P4 — Revisão independente reduz autoavaliação, mas não transforma opinião em prova. Codex Reviewer deve avaliar evidências e requisitos, não apenas concordar ou discordar de Claude.

P5 — Auditoria é read-only por padrão. O agente que audita não deve alterar silenciosamente o objeto auditado.

P6 — Configuração declarada não prova comportamento efetivo. Arquivos, hooks, permissions e sandbox precisam ser confrontados com verificação compatível com a propriedade afirmada.

P7 — Teste existente não é automaticamente teste efetivo. Controles positivos, negativos e, quando necessário, fault injection demonstram sensibilidade do verificador.

P8 — Rigor é proporcional ao risco. Controles adicionais entram no R0 somente quando protegem uma propriedade obrigatória ou mitigam uma falha concreta.

# 4. Componentes e papéis

## 4.1 Humano responsável

Define o objetivo da auditoria, aprova critérios e limites, resolve HUMAN_DECISION_REQUIRED, decide se evidência é suficiente para uma decisão de produto e autoriza qualquer transição para execução ou merge.

## 4.2 Claude Code — Executor ou Auditor

Quando Executor, implementa apenas o trabalho autorizado e produz evidências. Quando Auditor, atua em sessão separada e read-only, executando o protocolo deste documento. Em nenhum dos papéis seu autorrelato equivale a PASS verificado.

## 4.3 Codex — Reviewer independente

Opera em contexto independente e, preferencialmente, read-only. Revisa requisitos, diff, evidências, cobertura, riscos e inconsistências. Findings precisam ser sustentados por fonte, evidência ou procedimento reproduzível; finding sem sustentação permanece hipótese de revisão.

## 4.4 Mecanismos determinísticos

Incluem scripts, linters, typecheck, testes, validação de schema, comandos Git de inspeção, verificações de filesystem, hooks command e outros checks que produzam resultados reproduzíveis. Esses mecanismos verificam propriedades específicas; não homologam semanticamente o produto.

# 5. Modelo mínimo de assurance

A cadeia obrigatória é:

**REQUIREMENT → PROPERTY → CLAIM → SOURCE → EVIDENCE → VERIFICATION → COUNTEREXAMPLE SEARCH → VERDICT → HUMAN DECISION.**

**Para cada conclusão importante, o auditor deve produzir:** Claim; Source; Evidence; Method; Reproduction; Expected; Observed; Limitation; Classification; Verdict.

Classification aceita: FACT, OBSERVATION, INFERENCE, RECOMMENDATION. Uma recomendação nunca pode ser apresentada como fato atual do repositório.

# 6. Taxonomia de verdicts

PASS — existe evidência suficiente e reproduzível sustentando a propriedade definida.

FAIL — existe evidência suficiente demonstrando violação da propriedade definida.

UNVERIFIED — a evidência é insuficiente para decidir PASS ou FAIL.

BLOCKED — a verificação necessária não pôde ser executada por ausência de pré-condição, permissão, ambiente, dependência ou informação obrigatória.

NOT_APPLICABLE — a propriedade foi analisada e não pertence ao alvo auditado.

Nenhum AC obrigatório pode ser considerado atendido por mera ausência de findings.

# 7. Fluxo canônico de auditoria

G0 — TARGET FREEZE. Registrar repository root, branch, HEAD, working-tree status, objetivo, escopo declarado, exclusões e fontes de instrução/configuração aplicáveis.

G1 — SCOPE INVENTORY. Inventariar o universo candidato antes da análise substantiva, incluindo arquivos versionados, não ignorados relevantes, configurações, scripts, workflows, hooks e decisões arquiteturais relacionadas ao alvo.

G2 — DETERMINISTIC DEPENDENCY CLOSURE. Inventariar tipos de arquivo, selecionar parser determinístico aplicável, extrair referências estruturais, resolvê-las com o resolver nativo/configurado quando existir, registrar proveniência das arestas e repetir o processo até ponto fixo. Toda referência não resolvida deve permanecer explícita como STATIC_UNRESOLVED, DYNAMIC_UNRESOLVED, DECLARED_EXTERNAL ou DECLARED_OUT_OF_SCOPE; nunca como unknown silencioso.

G3 — REQUIREMENT MAP. Converter requisitos, invariantes, AC e DoD em propriedades verificáveis, com método e evidência exigidos.

G4 — STATIC ANALYSIS. Ler configuração e código sem confundir declaração estática com prova de runtime.

G5 — EXECUTABLE VERIFICATION. Executar verificações determinísticas aplicáveis e registrar comandos, cwd, exit code, esperado e observado.

G6 — ADVERSARIAL VERIFICATION. Tentar falsificar os PASS propostos, buscando bypasses, caminhos alternativos, configurações externas, dependências não resolvidas e testes inefetivos.

G7 — EVIDENCE-BASED VERDICT. Emitir verdict somente depois de consolidar cobertura, evidências, limitações e itens UNVERIFIED/BLOCKED.

# 8. Captura e fechamento do escopo

Defina S0 como o conjunto inicial de artefatos descobertos para o alvo. Defina Refs(x) como os arquivos, scripts, hooks, mounts, workflows ou configurações referenciados por x. Calcule S(n+1) = Sn ∪ Refs(Sn) até que S(n+1) = Sn. O resultado S* é o fechamento das dependências descobertas.

Toda aresta encontrada deve ser classificada como RESOLVED_IN_SCOPE, DECLARED_EXTERNAL, DECLARED_OUT_OF_SCOPE ou UNRESOLVED. Se houver dependência obrigatória UNRESOLVED, SCOPE_COMPLETE não pode ser TRUE.

O inventário deve considerar, conforme aplicável: Dockerfile*, .devcontainer/**, CLAUDE.md, CLAUDE.local.md, .claude/**, managed settings efetivos, .mcp.json, AGENTS.md, AGENTS.override.md, .codex/config.toml, configurações de usuário relevantes, .github/workflows/**, scripts invocados, manifests, schemas, hooks e ADRs/documentos normativos que governem o comportamento auditado.

Arquivos UNKNOWN não são descartados silenciosamente; devem ser investigados ou explicitamente classificados como fora de escopo com justificativa.

# 9. Instruções de raciocínio observável

Não solicitar chain-of-thought privado.

Solicitar uma trilha externa e verificável.

O agente deve:

1.  primeiro estabelecer fatos do ambiente;
2.  depois mapear dependências;
3.  depois formular propriedades;
4.  depois verificar;
5.  por fim buscar contraexemplos
6.  emitir verdict.

O agente deve distinguir o que foi lido do que foi inferido.

Deve declarar quando uma conclusão depende de hipótese.

Deve preferir comando ou teste reproduzível a avaliação por aparência.

Deve registrar limitações antes de emitir PASS global.

# 10. Antipadrões proibidos

P-01 — concluir pela aparência do arquivo.

P-02 — usar “parece correto” como PASS.

P-03 — usar existência de teste como evidência de efetividade.

P-04 — usar comentário, documentação, CLAUDE.md ou AGENTS.md como prova de enforcement técnico.

P-05 — inferir conteúdo de arquivo não lido ou configuração não carregada.

P-06 — omitir dependência externa silenciosamente.

P-07 — confundir configuração declarada com comportamento efetivo.

P-08 — confundir exit code 0 com cobertura integral do requisito.

P-09 — tratar ausência de finding como prova de ausência de defeito.

P-10 — transformar recomendação do agente em fato arquitetural.

P-11 — alterar o objeto auditado durante auditoria read-only.

P-12 — adicionar novo requisito durante auditoria de conformidade sem decisão humana.

P-13 — declarar DONE se qualquer AC obrigatório estiver UNVERIFIED ou BLOCKED.

P-14 — declarar “nenhuma regressão” sem definir e executar a superfície de regressão verificada.

# 11. Efetividade dos testes

Para controles críticos, um teste deve demonstrar sensibilidade.

Exigir, quando viável, um POSITIVE CONTROL conhecido como válido e um NEGATIVE CONTROL conhecido como inválido.

Exemplo:

Uma política deve bloquear sudo.

-   **Controle positivo:** comando permitido esperado → execução permitida.
-   **Controle negativo:** sudo controlado esperado → bloqueio observável.

Se o detector retorna PASS nos dois casos, o teste é INEFFECTIVE para a propriedade.

Para validadores críticos:

-   usar *fault injection* ou *mutation testing* em fixture/cópia controlada quando a simples execução não demonstra que o verificador detectaria o defeito relevante.

Evidência de terminal deve registrar, no mínimo:

-   EVIDENCE_ID
-   target/HEAD
-   command
-   cwd
-   exit_code
-   expected
-   observed
-   resumo stdout/stderr
-   result.

# 12. Edge cases e análise de risco

Edge cases devem ser derivados sistematicamente de:

-   BOUNDARIES,
-   STATE TRANSITIONS,
-   TRUST BOUNDARIES,
-   DEPENDENCY EDGES e
-   FAILURE MODES.

Evitar listas livres de cenários imagináveis sem ligação demonstrada com a arquitetura.

Para cada risco registrar:

-   ativo/propriedade afetada,
-   condição causal,
-   mecanismo de falha,
-   evidência atual,
-   probabilidade segundo rubrica predefinida,
-   impacto segundo rubrica predefinida,
-   mitigação direta,
-   verificação da mitigação
-   risco residual.

Quando severidade ou aceitabilidade não puderem ser resolvidas objetivamente pela rubrica, usar HUMAN_DECISION_REQUIRED em vez de inventar precisão matemática.

# 13. AC, DoD e matriz de cobertura

Antes de DONE, produzir a matriz:

AC_ID | PROPERTY | METHOD | EVIDENCE | RESULT.

Cada AC obrigatório precisa apontar para uma propriedade observável, um método de verificação e a evidência correspondente.

DoD = PASS somente se todo AC obrigatório tiver resultado PASS ou NOT_APPLICABLE previamente aceito pelo humano. Qualquer UNVERIFIED ou BLOCKED obrigatório implica DONE = FALSE.

# 14. Governança prática no VS Code

Camada 1 — Instructions: CLAUDE.md, AGENTS.md e o protocolo canônico de auditoria. Servem para orientar comportamento; não constituem, sozinhos, enforcement.

Camada 2 — Technical Boundaries: permissions, sandbox, mounts read-only, políticas de aprovação e managed settings. Servem para limitar tecnicamente o que o agente pode fazer.

Camada 3 — Deterministic Verifiers: scripts, testes, schemas, lint, typecheck, negative controls e hooks do tipo command para propriedades que precisam de execução obrigatória.

Camada 4 — Independent Review: Codex em contexto independente/read-only, revisão das evidências e decisão humana final.

Regra: instruction by prompt não deve ser descrita como enforcement. Tool deny não deve ser descrito como OS-level deny sem verificação da fronteira efetiva.

# 15. Artefatos mínimos para implantação R0

A-01 — docs/assurance/AUDIT_PROTOCOL.md: SSOT do protocolo definido neste documento.

A-02 — CLAUDE.md: referência curta ao protocolo, regras NO EVIDENCE → UNVERIFIED e READ-ONLY para auditorias.

A-03 — AGENTS.md: referência equivalente para Codex e exigência de findings sustentados por evidência.

A-04 — scripts/audit/: verificadores determinísticos mínimos para target identity, scope inventory, config validation, parsing estrutural, extração de referências, resolução de dependências e checks críticos já conhecidos.

A-05 — tests/audit-fixtures/: casos conhecidos válidos e inválidos para provar sensibilidade dos verificadores.

A-06 — configuração de permissions/sandbox/hooks somente onde exista propriedade obrigatória que precise de enforcement.

A-07 — template de AUDIT_RESULT com verdicts, evidências, cobertura e limitações.

Observação: paths são proposta de implantação e devem ser reconciliados com os paths canônicos já existentes no repositório antes de criação. Não criar duplicatas se artefato equivalente já existir.

# 16. Plano de implantação R0

TASK-R0-01 — inventariar artefatos já existentes relacionados a auditoria, execução, review, testes e enforcement. Saída: mapa AS-IS sem mutação.

TASK-R0-02 — comparar o AS-IS com os sete gates G0–G7 e registrar somente gaps necessários ao R0.

TASK-R0-03 — escolher ou confirmar o path canônico do AUDIT_PROTOCOL, evitando duplicidade documental.

TASK-R0-04 — adaptar CLAUDE.md e AGENTS.md para apontar ao protocolo e manter instruções curtas.

TASK-R0-05 — implementar o pipeline determinístico mínimo de descoberta estrutural: inventário → classificação de arquivos → parsing → extração de referências → resolução → grafo com proveniência → fechamento em ponto fixo, além dos verificadores das propriedades críticas já aprovadas.

TASK-R0-06 — criar controles positivos e negativos para cada verificador crítico.

TASK-R0-07 — configurar enforcement técnico apenas onde instrução não seja suficiente e exista risco concreto.

TASK-R0-08 — executar uma auditoria piloto com Claude em sessão nova/read-only.

TASK-R0-09 — executar revisão independente do mesmo alvo com Codex read-only.

TASK-R0-10 — comparar findings com evidências, medir falsos positivos/negativos em casos conhecidos e ajustar o protocolo.

TASK-R0-11 — homologação humana do R0 somente após os critérios de aceitação da implantação passarem.

# 17. Runbook de execução de uma auditoria

PASSO 1 — abrir sessão nova do agente auditor. Não carregar conclusões de auditoria anterior como fatos.

PASSO 2 — declarar AUDIT MODE — READ ONLY e o objetivo exato.

PASSO 3 — executar G0 e registrar root, branch, HEAD e working tree.

PASSO 4 — executar G1 e G2 antes de qualquer conclusão substantiva. Em G2, o agente deve invocar parsers/resolvers aprovados quando existirem; leitura direta por LLM não substitui parsing determinístico como evidência de cobertura estrutural.

PASSO 5 — montar mapa Requirement → Property → Method → Evidence.

PASSO 6 — executar análise estática e verificações determinísticas aplicáveis.

PASSO 7 — executar controles negativos/positivos dos verificadores críticos.

PASSO 8 — executar counterexample search sobre cada PASS importante.

PASSO 9 — emitir resultados apenas na taxonomia definida.

PASSO 10 — abrir revisão independente no Codex com o alvo e as evidências, não com a conclusão final do primeiro auditor como premissa.

PASSO 11 — humano resolve divergências e itens HUMAN_DECISION_REQUIRED.

PASSO 12 — somente depois disso usar o resultado para decisão de implementação, correção ou aprovação.

# 18. Prompt canônico — Claude Code Auditor

AUDIT MODE — READ ONLY

Objective: <objetivo específico>.

Target: current repository and current working tree.

Do not modify files. Do not perform Git mutation. Do not redesign the architecture. Do not treat prior-chat conclusions as facts.

Execute mandatory phases in order:

G0 TARGET FREEZE

G1 SCOPE INVENTORY

G2 DETERMINISTIC DEPENDENCY CLOSURE

G3 REQUIREMENT MAP

G4 STATIC ANALYSIS

G5 EXECUTABLE VERIFICATION

G6 ADVERSARIAL VERIFICATION

G7 EVIDENCE-BASED VERDICT

For every mandatory property, report:

Claim; Classification; Source; Evidence; Reproduction; Expected; Observed; Limitation; Verdict.

Allowed verdicts only:

PASS, FAIL, UNVERIFIED, BLOCKED, NOT_APPLICABLE.

PASS requires reproducible supporting evidence.

No evidence means UNVERIFIED, never PASS.

Static configuration is not runtime proof.

Test existence is not test effectiveness.

Do not emit DONE/APPROVED if a mandatory property is UNVERIFIED or BLOCKED.

# 19. Prompt canônico — Codex Reviewer

REVIEW MODE — READ ONLY

Review the declared audit target independently.

Do not modify the repository.

Do not accept the first auditor's conclusion as a premise.

Verify the scope map, parser/resolver outputs, dependency graph provenance, unresolved edges, evidence, commands, AC coverage, negative controls and limitations.

For each challenged claim:

identify the exact requirement/property;

cite the repository evidence or executable reproduction;

state expected versus observed;

classify the finding as FACT, INFERENCE or RECOMMENDATION;

emit PASS, FAIL, UNVERIFIED, BLOCKED or NOT_APPLICABLE.

A finding without supporting evidence is a REVIEW_HYPOTHESIS and cannot by itself produce FAIL.

Do not add new architecture requirements during conformity review. New hardening ideas go to DEFER unless they demonstrate violation of an already approved R0 property.

# 20. Validação do próprio auditor

A qualidade do protocolo deve ser medida em um corpus de casos conhecidos. Criar fixtures com casos corretos e defeitos deliberados, sem revelar ao auditor qual caso está quebrado.

Registrar TP = defeito existente detectado; FP = defeito inexistente reportado; FN = defeito existente não detectado; TN = caso correto corretamente não reportado. Calcular precision = TP/(TP+FP) e recall = TP/(TP+FN).

Falsos negativos silenciosos não podem ser estimados de forma séria sem casos cuja verdade de referência seja conhecida. Concordância Claude + Codex não substitui esse corpus.

# 21. Critérios de aceitação da implantação

AC-R0-01 — existe um protocolo canônico único e referenciado por Claude e Codex.

AC-R0-02 — auditoria pode identificar root, branch, HEAD e working tree antes da análise.

AC-R0-03 — inventário de escopo e fechamento de dependências usam parsing/resolução determinística quando aplicável, registram proveniência das arestas e produzem referências não resolvidas explicitamente, sem unknown silencioso.

AC-R0-04 — todo PASS obrigatório possui evidência e método de reprodução.

AC-R0-05 — controles críticos possuem pelo menos um negative control quando tecnicamente viável.

AC-R0-06 — configuração declarada e comportamento de runtime são reportados separadamente.

AC-R0-07 — Claude Auditor e Codex Reviewer operam em contextos independentes e sem mutação durante auditoria.

AC-R0-08 — nenhum AC obrigatório UNVERIFIED/BLOCKED permite DONE.

AC-R0-09 — protocolo foi testado contra casos conhecidos e métricas básicas de FP/FN foram produzidas.

AC-R0-10 — novas sugestões de hardening não entram automaticamente no R0; exigem risco concreto ou decisão humana.

# 22. Limites e itens deferidos

O R0 não exige identidade criptográfica própria do candidate, manifests customizados, JCS, governed state extensivo, reexecução tripla de verificadores ou state machine ampla. Esses mecanismos só devem ser considerados quando uma propriedade aprovada não puder ser protegida com os controles mínimos ou quando um incidente concreto demonstrar a necessidade.

O protocolo também não prova ausência universal de defeitos. Seu verdict aplica-se apenas ao alvo, escopo, propriedades e métodos explicitamente auditados.

# 23. Regra operacional final

O CEPRAEA BEACH PRO deve tratar modelos de IA como produtores de hipóteses, implementações, análises e reviews; a autoridade de um resultado vem da combinação apropriada de evidência, verificação reproduzível, revisão independente e decisão humana.

Fórmula operacional: CLAIM ≠ FACT; MODEL AGREEMENT ≠ PROOF; NO EVIDENCE → UNVERIFIED; REPRODUCIBLE CONTRADICTION → FAIL; VERIFIED PROPERTY + TRACEABLE EVIDENCE → PASS FOR THAT PROPERTY.

# 24. Análise sintática determinística e grafo de dependências

A leitura direta do repositório pelo LLM permanece útil para interpretação semântica, mas não é evidência suficiente de cobertura estrutural quando existe parser determinístico aplicável. O R0 passa a exigir que propriedades estruturais sejam derivadas de ferramentas determinísticas antes de serem interpretadas pelo agente.

## 24.1 Objetivo

O objetivo não é substituir Claude ou Codex por AST. O objetivo é retirar do modelo a responsabilidade de descobrir por inspeção visual aquilo que pode ser extraído deterministicamente: arquivos existentes, estrutura sintática, referências, imports, includes, scripts executados, workflows, mounts e outras relações formalizáveis.

A formula operacional passa a ser: MACHINE DISCOVERS → LLM INTERPRETS → MACHINE VERIFIES → INDEPENDENT REVIEW CHALLENGES.

## 24.2 Parser não é resolver

Um parser demonstra a estrutura sintática do artefato e pode extrair uma referência. Ele não prova automaticamente qual recurso essa referência resolve no ambiente efetivo. Portanto: PARSER EVIDENCE prova que uma referência existe; RESOLVER EVIDENCE prova, quando possível, qual é o alvo resolvido.

Exemplo: um import TypeScript com specifier "@/domain/foo" deve ser extraído sintaticamente e depois resolvido segundo a configuração efetiva do projeto. Tree-sitter pode ser usado para extração estrutural, mas o resolver do TypeScript deve ser preferido para semântica de resolução TypeScript quando aplicável.

## 24.3 Pipeline determinístico obrigatório de G2

O fluxo mínimo é: FILESYSTEM/GIT INVENTORY → FILE CLASSIFICATION → APPROVED PARSER → REFERENCE EXTRACTION → APPLICABLE RESOLVER → EDGE PROVENANCE → DEPENDENCY GRAPH → FIXED-POINT CLOSURE → UNRESOLVED REGISTER → LLM ANALYSIS.

O agente não deve escolher arquivos relevantes exclusivamente por leitura manual. O inventário inicial deve ser produzido por Git/filesystem e cada tipo de arquivo deve ser enviado ao parser/resolver aplicável conforme o registry aprovado.

## 24.4 Parser registry

A implantação deve possuir uma tabela ou configuração equivalente que relacione classe de artefato, parser, extractor e resolver. O formato físico ainda deve ser reconciliado com o AS-IS antes da criação para evitar duplicidade.

Classes mínimas a avaliar: TypeScript/TSX, JavaScript/JSX/MJS, JSON, YAML, TOML, shell, Dockerfile, Markdown normativo e demais formatos de infraestrutura encontrados no inventário.

Para TypeScript, preferir o TypeScript Compiler/Program e seu mecanismo de module resolution quando a propriedade depende da configuração real de tsconfig/package/moduleResolution. Para JavaScript/ESLint, AST pode apoiar regras estruturais e escopo. Tree-sitter é apropriado como parser estrutural multi-linguagem, mas não deve ser promovido sozinho a resolvedor universal de dependências.

## 24.5 Modelo formal do grafo

Defina G = (V, E), onde V é o conjunto de artefatos classificados e E é o conjunto de relações demonstradas. Cada aresta deve carregar proveniência mínima: from, to ou unresolved target, relation, discovered_by, resolved_by quando aplicável e evidence/specifier/origin.

Uma aresta não pode ser registrada como RESOLVED apenas porque o LLM inferiu o destino provável. A resolução precisa vir do resolver aplicável ou permanecer explicitamente não resolvida.

## 24.6 Fechamento em ponto fixo

Defina S0 como o conjunto inicial descoberto. Para cada artefato v em Sn, Parse/Extract produz Ref(v). Resolve(Ref(v)) adiciona novos artefatos e arestas. Calcule S(n+1) = Sn ∪ Resolve(Ref(Sn)) até S(n+1) = Sn.

O ponto fixo demonstra somente fechamento relativo aos parsers, extractors, resolvers e fontes de configuração definidos. Ele não prova ausência universal de dependências de runtime.

## 24.7 Taxonomia de resolução

Toda referência detectada deve terminar em um estado explícito: RESOLVED_IN_SCOPE; RESOLVED_EXTERNAL; DECLARED_OUT_OF_SCOPE; STATIC_UNRESOLVED; DYNAMIC_UNRESOLVED; UNSUPPORTED_EXPLICIT.

É proibido o estado implícito UNKNOWN_SILENT. Uma referência dinâmica como import(variable) ou source "$DIR/$PROFILE.sh" não deve ser adivinhada. Deve permanecer DYNAMIC_UNRESOLVED até que evidência de runtime ou configuração permita resolução.

## 24.8 Regras normativas

DET-PARSE-001 — Para artefato in-scope com parser determinístico aprovado, conclusões estruturais substantivas MUST derivar da saída do parser. Leitura direta pelo LLM MAY complementar interpretação semântica, mas MUST NOT substituir parsing como evidência de cobertura estrutural.

DET-RESOLVE-001 — Referência sintaticamente extraída MUST NOT ser reportada como dependência resolvida até que resolver aplicável a resolva. Ausência de resolver implica estado unresolved explícito.

DET-GRAPH-001 — Toda aresta resolvida MUST registrar proveniência suficiente para outra parte reproduzir como foi descoberta e resolvida.

DET-CLOSURE-001 — DEPENDENCY_CLOSURE = PASS somente quando toda aresta descoberta estiver classificada. Aresta não resolvida obrigatória impede SCOPE_COMPLETE = TRUE.

DET-LLM-001 — Claude/Codex MUST NOT criar aresta factual apenas por interpretação textual. Relações sem evidência determinística devem ser INFERENCE ou REVIEW_HYPOTHESIS.

DET-FAIL-001 — Falha de parsing de artefato obrigatório, erro do resolver ou formato sem suporte MUST ser visível como BLOCKED/UNVERIFIED/UNSUPPORTED_EXPLICIT conforme a propriedade, nunca omitido.

## 24.9 Tipos de relação do grafo

O grafo deve distinguir relações, quando detectáveis, como IMPORTS, RE_EXPORTS, EXECUTES, SOURCES, EXTENDS_CONFIG, USES_WORKFLOW, USES_ACTION, BUILDS_FROM, COPIES_FROM, MOUNTS, LOADS_CONFIG, REFERENCES_SCHEMA e outras relações aprovadas a partir de casos reais do repositório.

A taxonomia não deve crescer preventivamente. Novo tipo de aresta entra somente quando um artefato real exige representá-lo.

## 24.10 Evidência de parsing e resolução

Cada execução determinística deve registrar target/HEAD, ferramenta e versão, comando ou entrypoint, configuração utilizada, arquivos processados, parse failures, número de referências extraídas, número de arestas resolvidas e lista de unresolved edges.

O resultado recomendado do G2 é um artefato lógico equivalente a DEPENDENCY_GRAPH + DEPENDENCY_COVERAGE_REPORT. O formato físico ainda é decisão de implantação e não deve ser criado em duplicidade se mecanismo equivalente já existir.

## 24.11 Uso do TypeScript no CEPRAEA BEACH PRO

Para a superfície TypeScript, a auditoria deve usar a configuração efetiva do projeto. Quando disponível e adequado, comandos/funções do compilador equivalentes a showConfig, listFiles/explainFiles e traceResolution podem fornecer evidência sobre arquivos incluídos e resolução de módulos. AST genérica não substitui essas regras quando a pergunta é "para qual módulo este specifier resolve sob a configuração do projeto?".

## 24.12 Relação com ESLint e Tree-sitter

ESLint AST é apropriado para propriedades sintáticas, escopo, padrões proibidos e regras arquiteturais expressáveis por AST. Tree-sitter é apropriado para parsing estrutural e queries multi-linguagem. Nenhuma dessas ferramentas, isoladamente, deve ser descrita como prova completa do grafo real de runtime do repositório.

## 24.13 Limite da afirmação de completude

A formula proibida é: "a árvore de dependências real e matematicamente comprovada de todo o repositório".

A formula aceita é: "grafo de dependências produzido deterministicamente, com proveniência, resolvido até o fechamento possível pelos parsers e resolvers definidos, com toda aresta não resolvível explicitamente classificada".

A propriedade de assurance buscada é NO SILENT UNKNOWN: nenhuma referência detectada pelos mecanismos aprovados pode desaparecer silenciosamente do resultado.

## 24.14 Nova divisão de responsabilidades

Deterministic tools respondem: o que existe; qual é a sintaxe; quais referências aparecem; quais alvos resolvem; qual configuração foi usada; quais arestas permanecem unresolved.

LLM responde: o que essas relações significam arquiteturalmente; quais trust boundaries são afetadas; quais invariantes podem estar em conflito; quais hipóteses e riscos merecem verificação.

Deterministic verification responde: a hipótese semanticamente formulada pode ser confirmada ou refutada por teste, comando ou check reproduzível?

Reviewer independente responde: o grafo, a evidência, as limitações e as conclusões estão coerentes e sustentadas?

# 25. Impacto na implantação R0

A-08 — parser/resolver registry ou mecanismo equivalente, reconciliado com o path canônico do repositório.

A-09 — dependency graph e coverage/unresolved report como saídas determinísticas do G2; podem ser artefatos transitórios ou persistidos conforme decisão posterior, mas sua geração deve ser reproduzível.

TASK-R0-05A — provar em fixture que o pipeline encontra uma dependência válida conhecida e classifica corretamente uma referência inválida/dinâmica sem inventar destino.

TASK-R0-05B — validar separadamente pelo menos uma cadeia cross-format real do repositório, por exemplo configuração → script → outro artefato, antes de declarar G2 implantado.

AC-R0-11 — para cada classe de arquivo in-scope com parser aprovado, existe evidência de parsing ou classificação explícita de unsupported/out-of-scope.

AC-R0-12 — toda aresta do grafo possui proveniência; unresolved edges são explicitamente listadas.

AC-R0-13 — um negative fixture com referência deliberadamente quebrada não pode resultar em SCOPE_COMPLETE = TRUE.

AC-R0-14 — o mesmo input, configuração e versão das ferramentas produzem representação estrutural equivalente, salvo campos explicitamente não determinísticos.

AC-R0-15 — o LLM recebe o grafo/coverage report como evidência de entrada e não é a fonte primária de descoberta de dependências formalizáveis.