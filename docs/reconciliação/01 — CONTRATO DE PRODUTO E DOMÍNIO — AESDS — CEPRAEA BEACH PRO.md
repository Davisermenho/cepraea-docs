Guia 1

CONTRATO DE PRODUTO E DOMÍNIO — CEPRAEA BEACH PRO

AESDS 01 — Fundação v0.1

1. OBJETIVO

Dar aos agentes o significado que deve ser preservado antes de qualquer decisão de frontend. Este documento não recria o Modelo Canônico; ele estabelece como o agente deve consumi-lo e transforma suas consequências em restrições operacionais.

2. AUTORIDADE

Autoridade humana: Davi.

Autoridade semântica: Modelo Canônico e decisões homologadas.

Autoridade executável: tipos, schemas, Domain Policies, contratos de API, constraints, RLS e testes compatíveis com a decisão canônica.

Autoridade operacional de tarefa: Git/GitHub e a tarefa corrente; o procedimento operacional aplicável é detalhado pelas políticas vigentes do repositório e pelos AESDS especializados.

Em conflito, o agente não escolhe silenciosamente. Deve identificar as fontes conflitantes e parar somente a decisão afetada. Durante a Camada de Planejamento, classificação e resolução de conflito seguem o CHATGPT_PLANNING_FLOW_INSTRUCTIONS.md (“Instruções Projetos”).

3. IDENTIDADE DO PRODUTO

CEPRAEA BEACH PRO é um PWA mobile de gestão esportiva voltado à operação da equipe feminina adulta CEPRAEA de handebol de praia. O frontend deve funcionar como projeção compreensível e operacional do estado do domínio para atletas e treinador.

4. PRINCÍPIOS DO PRODUTO

- uma fonte operacional de verdade por fato;

- semântica inequívoca;

- preservação histórica quando exigida pelo domínio;

- interface orientada à próxima ação;

- mobile-first real;

- previsibilidade e testabilidade;

- integridade maior que conveniência visual;

- simplicidade proporcional à escala;

- ausência de abstração genérica sem necessidade do CEPRAEA.

5. INVARIANTES QUE O FRONTEND DEVE PRESERVAR

- disponibilidade não é presença;

- lista prevista não é presença factual;

- não respondida não é resposta negativa;

- dado existente não implica permissão de leitura ou edição;

- informação vencida não pode parecer vigente;

- estado pendente não pode parecer persistência concluída;

- UI não substitui autorização, RLS nem enforcement do servidor;

- frontend não pode criar novo significado para resolver layout;

- estados críticos não dependem apenas de cor;

- identificadores técnicos não são conteúdo de atleta salvo requisito explícito.

6. REGRAS DE AUTONOMIA

O agente pode decidir autonomamente detalhes locais e reversíveis que não alterem comportamento observável, contrato, segurança, acessibilidade, semântica ou arquitetura material.

O agente deve solicitar decisão humana quando existir mais de uma alternativa material para: navegação, fluxo, informação visível, linguagem de domínio, dependência, arquitetura, identidade visual, persistência, autorização, privacidade ou comportamento de negócio.

Na Camada de Planejamento do ChatGPT, a identificação, recomendação, classificação e ratificação de decisões materiais seguem o CHATGPT_PLANNING_FLOW_INSTRUCTIONS.md (“Instruções Projetos”). Na execução pós-hand-off, autonomia e stop conditions seguem o AESDS 07 e as políticas operacionais vigentes do repositório.

7. REGRA DE PESQUISA PARA DECISÕES PENDENTES

A obrigação local é: decisão material não homologada não pode ser escolhida silenciosamente, e referência observada não vira regra automaticamente.

Durante a Camada de Planejamento, pesquisa, apresentação de alternativas, recomendação, trade-offs e ratificação seguem o CHATGPT_PLANNING_FLOW_INSTRUCTIONS.md (“Instruções Projetos”). Para pesquisa técnica e referências, aplique também o AESDS 08 — Catálogo de Referências e Protocolo de Pesquisa.

8. CLASSIFICAÇÃO E LIMITES DE DECISÃO

Estados de decisão e informação usados na Camada de Planejamento seguem o CHATGPT_PLANNING_FLOW_INSTRUCTIONS.md (“Instruções Projetos”); não mantenha uma taxonomia concorrente neste documento.

AUTONOMIA TÉCNICA: o agente pode resolver localmente apenas detalhes abrangidos pelo §6 e pelas políticas operacionais vigentes.

PROIBIDO: o agente não implementa decisão material não autorizada, mesmo que pareça conveniente.

Inferências devem permanecer explicitamente classificadas segundo a fonte normativa aplicável e nunca ser apresentadas como fatos observados.

9. DADOS E PRIVACIDADE

Até alteração explícita da autorização vigente do projeto, desenvolvimento e validação devem usar dados sintéticos. Informações médicas, diagnósticos ou justificativas sensíveis não devem ser introduzidos em fluxos que não os autorizem.

10. SAÍDA ESPERADA PARA CADA FEATURE

Antes da implementação, o agente deve conseguir responder:

- quem é o ator;

- qual tarefa está sendo realizada;

- qual fato do domínio é representado;

- qual é o estado inicial;

- quais transições são válidas;

- quais ações são proibidas;

- quais informações o ator pode ver/editar;

- quais critérios provam correção.

O detalhamento de fluxos e estados pertence ao AESDS 02; tarefas e critérios de aceitação ao AESDS 05; provas e verificação ao AESDS 06; contratos técnicos e enforcement ao AESDS 03 e às fontes executáveis aplicáveis.

11. STOP CONDITIONS

Parar a decisão afetada se: regra ausente; fontes normativas conflitantes; nova dependência material; alteração de schema/contrato não prevista; mudança de autorização/privacidade; necessidade de inventar comportamento; mudança de escopo.

Não parar por: nome de helper, organização interna de função, import, pequena refatoração local, formatação ou outro detalhe sem impacto observável.

Na Camada de Planejamento, classificação de estados, conflitos, blockers, reabertura e avanço de gate seguem o CHATGPT_PLANNING_FLOW_INSTRUCTIONS.md (“Instruções Projetos”). Após o hand-off, o procedimento operacional de stop/reopen segue o AESDS 07 e as políticas vigentes do repositório.

12. FONTES A CONSULTAR

- Modelo Canônico e seu índice existente no Drive/repositório;

- decisões canônicas aplicáveis;

- tarefa/issue atual;

- schemas e contratos executáveis relacionados;

- este AESDS somente como regra de consumo e execução, nunca como substituto da fonte canônica;

- na Camada de Planejamento, CHATGPT_PLANNING_FLOW_INSTRUCTIONS.md (“Instruções Projetos”) para estados, decisões, recomendações, gates, preservação de invariantes, stress-test, readiness e hand-off;

- AESDS 02, 03, 05, 06, 07, 08 e 09 conforme a responsabilidade documental aplicável.

13. BASELINE MVP E RASTREABILIDADE DE REQUISITOS

Esta seção inicia a fase PLANOS / SPECS consolidando somente requisitos e decisões já ratificados. Itens ainda não decididos permanecem OPEN e não podem ser convertidos em comportamento por conveniência de implementação.

13.1. REQUISITOS-FONTE DO MVP

SR-01 — O produto deve ser um PWA operacional mobile-first que mostre estado atual e próxima ação para atletas e treinador.

SR-02 — O frontend deve preservar semântica, temporalidade, autorização e state-first design; UI não é autoridade de regra crítica.

SR-03 — O MVP deve respeitar a cadeia lógica identidade/vínculo -> treino -> solicitação/resposta de disponibilidade -> cobertura/lista prevista -> presença factual -> visões operacionais.

SR-04 — Deve existir uma única fonte de verdade por fato, distinguindo disponibilidade, compromisso/planejamento, lista prevista e presença factual.

SR-05 — Presença factual exige confirmação autorizada. Wellness pode, quando permitido pela fonte canônica, gerar proposta derivada/transitória, nunca fato; ausência de registro não equivale a ausência da atleta.

SR-06 — Autorização real pertence ao backend/RLS. O PWA é online; persistência/cache offline de dados não é requisito autorizado.

SR-07 — A implementação deve avançar por vertical slices antes de generalizações arquiteturais ou Design System amplo.

SR-08 — A transição Drive -> PWA exige cutover explícito e não admite duas SSOT operacionais concorrentes para o mesmo fato.

SR-09 — O modelo físico Supabase permanece sujeito ao gate físico vigente; este contrato não autoriza SQL, schema, migration ou execução física enquanto o gate não for liberado pela autoridade competente.

SR-10 — Cada unidade implementável deve possuir critérios objetivos, provas e correção/reabertura quando implementação e contrato divergirem.

13.2. BASELINE DE DOMÍNIO QUE O MVP DEVE PRESERVAR

- atleta é conceito de domínio independente de identidade de autenticação;

- cadastro de atleta não equivale a vínculo temporal com equipe;

- disponibilidade, compromisso/planejamento e presença factual são conceitos distintos;

- não respondida não equivale a NÃO;

- lista prevista não equivale a presença factual;

- treino planejado e treino realizado são distinguíveis;

- respostas de disponibilidade preservam histórico/versão e o estado corrente deriva da versão vigente;

- cada solicitação de disponibilidade possui `deadline_at` explícito definido por ator autorizado; não existe prazo global implícito; a atleta pode criar/alterar somente a própria declaração enquanto a coleta estiver aberta; o deadline fecha o self-service sem converter NÃO_RESPONDIDA em NÃO nem apagar/expirar a última declaração válida; reabertura antes do início da sessão exige ato autorizado e auditável; após o início não há reabertura normal; retificações posteriores não criam presença factual por inferência;

- derivação, projeção ou proposta não se tornam fato sem a autoridade exigida pelo domínio;

- estado operacional deve expor significado e próxima ação sem inventar semântica ausente.

13.3. RASTREABILIDADE REQUISITO -> ENTREGÁVEL

SR-01 -> DEL-01 PWA Operational Shell; DEL-07 Athlete Operational Workspace; DEL-08 Coach Operational Workspace.

SR-02 -> DEL-01 a DEL-10, com enforcement concentrado em DEL-09 e contratos em DEL-10.

SR-03 -> DEL-02 Identity; DEL-03 Session; DEL-04 Availability; DEL-05 Coverage/Planned Participation; DEL-06 Factual Attendance; DEL-07/08 Workspaces.

SR-04 -> DEL-04, DEL-05, DEL-06, DEL-10 e DEL-11.

SR-05 -> DEL-06, DEL-09, DEL-10 e DEL-13.

SR-06 -> DEL-01, DEL-09, DEL-10 e DEL-13.

SR-07 -> DEL-01, DEL-02 a DEL-08, DEL-12 e DEL-13.

SR-08 -> DEL-11 Legacy Migration & Domain Cutover, com suporte de DEL-10 e DEL-13.

SR-09 -> DEL-10 Canonical Operational Persistence & Contract Surface e DEL-11.

SR-10 -> DEL-13 Automated & Runtime Verification Suite e critérios de todos os demais entregáveis.

13.4. ESTADO DAS QUESTÕES E BLOQUEIOS DE PLANEJAMENTO

OPEN-UX-01 — arquitetura de informação e padrão material de navegação.

OPEN-VIS-01 — direção visual, tipografia, paleta, iconografia e motion.

OPEN-A11Y-01 — nível formal de conformidade WCAG.

DECIDED-AVAIL-01 — prazo, fechamento da coleta, editabilidade e reabertura da disponibilidade estão ratificados por DEC-DATA-046; nenhuma fonte downstream pode criar default temporal concorrente.

DECIDED-PLAN-01 / DEC-DATA-047 — Plano de Participação da Sessão é PLANO prospectivo humano e versionado; “lista prevista” é a projeção da versão PUBLISHED vigente. Lifecycle: DRAFT -> PUBLISHED -> SUPERSEDED | CANCELLED | CLOSED. `SOURCE_ALIGNMENT = CONSISTENT | REVIEW_REQUIRED` é eixo ortogonal; mudanças materiais de fonte exigem revisão sem reescrever automaticamente a decisão. Versões PUBLISHED são imutáveis; revisão/revalidação material cria nova versão e preserva histórico/proveniência.

OPEN-REPO-01 — stack, estrutura física, comandos e contratos executáveis devem ser confrontados com o repositório real antes de tarefas dependentes.

BLOCKED-DATA-01 — alterações físicas de banco/SQL/schema/migrations permanecem bloqueadas pelo gate físico vigente.

Nenhum item OPEN/BLOCKED desta seção pode ser tratado como DECIDED por um documento downstream ou pelo executor.

Guia 2

REFERÊNCIA — PLANNING FLOW

Esta guia não define produto, domínio, stack, tarefas, testes, schemas, BDD, critérios de aceitação, DONE, metodologia de planejamento ou estrutura editorial concorrente.

A Camada de Planejamento do ChatGPT é regida pelo CHATGPT_PLANNING_FLOW_INSTRUCTIONS.md (“Instruções Projetos”), que governa fases, estados, decisões, recomendações, gates, preservação de invariantes, completude, stress-test, readiness e hand-off.

O conteúdo de produto e domínio é regido pela Guia 1 deste AESDS e pelas fontes canônicas que ela referencia. Stack e contratos técnicos pertencem ao AESDS 03 e às fontes executáveis vigentes. Tarefas, critérios e BDD pertencem ao AESDS 05; testes e verificação ao AESDS 06; execução e review ao AESDS 07; pesquisa ao AESDS 08; runbooks e estado operacional ao AESDS 09.

Princípio preservado de completude: nenhuma obrigação válida, requisito, restrição, exceção, critério de aceitação, rastreabilidade, autoridade ou evidência necessária pode ser omitida durante consolidação ou reescrita. A completude deve ser demonstrada pelos gates e pela rastreabilidade das fontes aplicáveis, não por quantidade fixa de seções, métricas ou exemplos.

As instruções anteriores específicas desta guia sobre criação prévia de um plano separado no Google Drive, equivalência estrutural obrigatória com o plano do executor, cardinalidades fixas de métricas/problemas, paginação/editorial, system prompt duplicado e análise invertida foram removidas por decisão humana ratificada.