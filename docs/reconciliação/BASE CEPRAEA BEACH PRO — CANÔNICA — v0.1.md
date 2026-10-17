**00 Controle**

**00.1 Escopo e Invariantes**

BASE DOCUMENTAL DERIVADA — ESCOPO E INVARIANTES

STATUS DA BASE: PROPOSED

CORPUS DE EVIDÊNCIA DE ORIGEM: Pesquisa CEPRAEA BEACH PRO — CANONICAL v1.0 / RESEARCH STATUS: DONE

ESCOPO: transformar evidência já promovida no corpus em interpretação aplicável e propostas de decisão local, sem alterar o corpus de pesquisa.

INVARIANTE EPISTÊMICO I-ED-001

EVIDÊNCIA OBSERVADA ≠ INTERPRETAÇÃO ≠ DECISÃO LOCAL DO PROJETO.

Para toda regra ou decisão derivada devem existir três registros distinguíveis:

1\. EVIDÊNCIA OBSERVADA — SOURCE-ID/EVIDENCE-ID e o claim realmente sustentado, incluindo limitações.

2\. INTERPRETAÇÃO APLICÁVEL — o que essa evidência permite concluir para o problema do CEPRAEA, sem ampliar o escopo da fonte.

3\. DECISÃO CEPRAEA — escolha de projeto criada localmente; não deve ser atribuída à fonte externa.

INVARIANTE I-ED-002 — Uma fonte externa não cria automaticamente uma regra local. A decisão local deve possuir DECISION-ID próprio.

INVARIANTE I-ED-003 — Nenhuma questão PARCIALMENTE\_FUNDAMENTADA pode ser promovida silenciosamente a FUNDAMENTADA ou a regra externa.

INVARIANTE I-ED-004 — Uma capability documentada para Codex, Claude Code, MCP ou outra ferramenta não deve ser generalizada para outra ferramenta sem evidência correspondente.

INVARIANTE I-ED-005 — A BASE é derivada. O registro de fontes/evidências permanece no corpus canônico de pesquisa; a BASE deve referenciá-lo, não reproduzi-lo como nova fonte de verdade.

INVARIANTE I-ED-006 — Conteúdo PROPOSED não é EFFECTIVE até aprovação humana explícita.

INVARIANTE I-ED-007 — Ausência de evidência suficiente deve permanecer visível como PARCIALMENTE\_FUNDAMENTADA, NÃO VERIFICADO, NÃO DOCUMENTADO ou DECISÃO\_DO\_PROJETO\_NECESSÁRIA, conforme o caso.

QUESTÕES AINDA PARCIAIS PRESERVADAS

Q-SE-02; Q-TR-01; Q-QL-01; Q-DR-01; Q-DR-02; Q-MC-02; Q-AG-01.

Essas questões não são reabertas nesta derivação e não recebem complemento por conhecimento geral.

**00.2 Autoridade e Estados**

REGISTRO DE DECISÕES LOCAIS DERIVADAS DO CORPUS

Estado inicial de todas as decisões abaixo: PROPOSED. O corpus concluiu que estas matérias exigem decisão local; ele não determina a escolha exata aqui proposta.

DEC-DOC-001 — Perfil local de metadados documentais

QUESTION: Q-ID-02 | EVIDENCE: E051–E055 | SOURCES: SRC-012, SRC-015, SRC-024, SRC-025 | GAP-11 COMPLETE

EVIDÊNCIA OBSERVADA: há fundamentos para elementos/contextos de metadados, responsabilidade, vocabulário reutilizável de identidade/evolução e proveniência; não existe no corpus uma política pronta de owner/state/domain/effectivity para o CEPRAEA.

INTERPRETAÇÃO: o projeto pode construir um application profile local reutilizando semânticas externas onde houver correspondência explícita.

DECISÃO CEPRAEA PROPOSTA: adotar DOCUMENT\_METADATA\_PROFILE v0.1 com os campos mínimos document\_id, title, document\_type, domain, owner, status, version, effective\_from, modified\_at, supersedes, source\_refs e decision\_refs. Os nomes e obrigatoriedades são escolhas locais; não são atribuídos a ISO/DCMI/PROV-O.

DEC-DOC-002 — Front matter e catálogo documental

QUESTION: Q-ST-02 | EVIDENCE: E056–E057 | SOURCES: SRC-024, SRC-052, SRC-053, SRC-059, SRC-060 | GAP-12 COMPLETE

EVIDÊNCIA OBSERVADA: Jekyll e GitHub Docs demonstram front matter/YAML em contextos próprios; não há padrão universal de front matter no corpus.

INTERPRETAÇÃO: front matter pode ser adotado como mecanismo local, desde que tratado como convenção do CEPRAEA e validado estruturalmente.

DECISÃO CEPRAEA PROPOSTA: usar YAML front matter nos documentos Markdown do repositório; validar o perfil local por schema; gerar índice/catálogo a partir dos metadados canônicos em vez de manter listas manuais concorrentes.

DEC-DOC-003 — Autoridade, ownership e precedência

QUESTION: Q-AU-01 | EVIDENCE: E053, E058 | SOURCES: SRC-011, SRC-016, SRC-035, SRC-036, SRC-061 | GAP-13 COMPLETE

EVIDÊNCIA OBSERVADA: existem fundamentos externos para responsabilidades, controles e configuration management; a precedência semântica entre artefatos do CEPRAEA não é definida externamente.

INTERPRETAÇÃO: a autoridade deve ser explícita e escopada por assunto, e a precedência precisa ser política local.

DECISÃO CEPRAEA PROPOSTA: aplicar “um assunto → um proprietário canônico”. O documento proprietário tem autoridade apenas no escopo declarado. Resumos, índices e instruções de agente são derivados e não podem sobrescrever o proprietário canônico. Promoção a EFFECTIVE exige owner e aprovação humana.

DEC-DOC-004 — Conflitos, effectivity e change control

QUESTION: Q-AU-02 | EVIDENCE: E058, E059 | SOURCES: SRC-036, SRC-055–057, SRC-061, SRC-074 | GAP-14 COMPLETE

EVIDÊNCIA OBSERVADA: configuration management sustenta controle de mudanças/status; state models de W3C/IETF/vendor são específicos de seus domínios; P828 não é um standard publicado vigente.

INTERPRETAÇÃO: o CEPRAEA necessita política própria de resolução de conflitos e vigência, sem importar state machines de outras organizações como norma local.

DECISÃO CEPRAEA PROPOSTA: conflito deve ser resolvido por escopo + owner + estado vigente + linhagem. Se duas autoridades efetivas permanecerem incompatíveis após essa análise, o conflito é BLOCKING e deve ser ESCALATE para decisão humana. Alteração de conteúdo EFFECTIVE gera nova versão/revisão com impacto e lineage; histórico não é sobrescrito silenciosamente.

DEC-DOC-005 — Estados documentais

QUESTION: Q-DS-01 | GAP-01 COMPLETE

EVIDÊNCIA OBSERVADA: a pesquisa concluiu que a state machine documental é decisão do projeto; não há no corpus uma máquina de estados universal a importar.

INTERPRETAÇÃO: os estados podem ser definidos localmente, desde que sua semântica e transições sejam explícitas.

DECISÃO CEPRAEA PROPOSTA: DRAFT → PROPOSED → REVIEWED → APPROVED → EFFECTIVE. A partir de EFFECTIVE, um documento pode tornar-se SUPERSEDED, DEPRECATED ou WITHDRAWN; ARCHIVED é estado de preservação histórica e não restaura vigência. APPROVED e EFFECTIVE permanecem distintos.

DEC-DOC-006 — Perfil de qualidade documental

QUESTION: Q-QL-02 | EVIDENCE: E060; E061 incidental | SOURCES: SRC-053, SRC-024, SRC-025, SRC-062 | GAP-15 COMPLETE

EVIDÊNCIA OBSERVADA: 26511 sustenta gestão de qualidade de informação e propriedades observadas como consistência, completude, precisão e usabilidade; o corpus não fornece o perfil completo nem thresholds de maintainability/currency do CEPRAEA.

INTERPRETAÇÃO: propriedades externas podem orientar um quality profile, mas os critérios de passagem são locais.

DECISÃO CEPRAEA PROPOSTA: antes de EFFECTIVE, exigir: metadados obrigatórios completos; zero conflito bloqueador não resolvido; zero afirmação normativa apresentada como externa sem evidence trace; referências de autoridade resolvidas; currentness verificada no escopo; um proprietário canônico por assunto; e rastreabilidade das decisões locais às evidências que as motivaram. Unambiguity e maintainability são critérios locais e não devem ser apresentados como integralmente derivados de E060/E061.

DEC-DOC-007 — Validação factual

QUESTION: Q-VA-03 | EVIDENCE: E065–E066 | SOURCES: SRC-065, SRC-066 | GAP-17 COMPLETE

EVIDÊNCIA OBSERVADA: V&V e processos de teste fornecem fundamento externo para verificar conformidade/intended use e usar análise, revisão, inspeção e testes; o corpus não define o mapping CEPRAEA claim→evidence.

INTERPRETAÇÃO: factual validation deve comparar afirmações documentais de estado atual com observações adequadas do sistema, sem confundir estado implementado com requisito desejado.

DECISÃO CEPRAEA PROPOSTA: classificar cada claim como factual-current-state, normative/desired-state ou local-decision; para claim factual, registrar objeto observado, método de verificação, evidência direta, revisão/versão/data e resultado. Código/runtime pode verificar estado factual, mas não sobrescreve silenciosamente um requisito normativo divergente.

DEC-AG-001 — Política comum ASK / STOP / UNKNOWN / ESCALATE

QUESTION: Q-AG-02 | EVIDENCE: E067–E070, E077 | SOURCES: SRC-042, SRC-046, SRC-067, SRC-068, SRC-070, SRC-072, SRC-073 | GAP-18 COMPLETE

EVIDÊNCIA OBSERVADA: Codex, Claude Code e MCP expõem mecanismos próprios de approval/input; nenhum deles define uma ontologia universal CEPRAEA.

INTERPRETAÇÃO: a semântica comum deve ser uma política local e cada ferramenta deve apenas adaptá-la às capabilities realmente documentadas.

DECISÃO CEPRAEA PROPOSTA: ASK = informação/decisão humana necessária antes de escolher entre alternativas materiais; STOP = prosseguir violaria hard constraint, autoridade ou gate; UNKNOWN = evidência insuficiente para afirmar, permitindo continuar apenas no que não depende da lacuna; ESCALATE = conflito entre autoridades, decisão fora da autoridade do agente ou bloqueio que exige owner humano. Adapters de Codex/Claude/MCP não podem ampliar essas capabilities por inferência.

DEC-AG-002 — Audit trail documental de agentes

QUESTION: Q-AG-03 | EVIDENCE: E071–E076 | SOURCES: SRC-025, SRC-044, SRC-069, SRC-071, SRC-072, SRC-075 | GAP-19 COMPLETE

EVIDÊNCIA OBSERVADA: existem eventos observáveis de execução, hooks/transcripts/tool I/O e modelos de proveniência; isso não fornece hidden reasoning nem prova correção das decisões do modelo. MCP Logging não deve ser presumido como primitive protocolar estável universal.

INTERPRETAÇÃO: auditoria deve registrar eventos e evidências observáveis, não chain-of-thought.

DECISÃO CEPRAEA PROPOSTA: adotar AUDIT\_EVENT\_PROFILE v0.1 com audit\_id, timestamp, task\_id, agent, tool\_or\_interface, action\_type, input\_ref, output\_ref, source\_refs, decision\_refs, artifact\_refs, result\_status, deviation\_or\_blocker, reviewer e retention\_class. O corpus não sustenta duração temporal específica de retenção; v0.1 define classes de retenção e deixa prazos quantitativos para decisão posterior.

OWNER-MAP v0.1 — ASSUNTO → OWNER ÚNICO — RECONCILIADO EM 2026-09-06

Regra de leitura: OWNER significa a autoridade resolvida para o assunto exato abaixo. Não existe um arquivo supremo para todos os assuntos. Delegações e projeções não ganham autoridade sobre o owner que lhes fornece semântica.

DOC-001 | Política documental geral, precedência, conflitos, redação, metadados universais, fontes, governança e validação documental | OWNER: Normas (SRC-DOC-016).

DOC-002 | Taxonomia/seleção/estrutura/lifecycle de templates | OWNER: Templates/CATE (SRC-DOC-018) | DELEGAÇÃO: Normas.

DOC-003 | Perfil normativo de autoria/validação Markdown no repositório | OWNER: docs/linters/guia\_estilo\_documentação.md | SUBORDINAÇÃO: AGENT\_POLICY + Normas nos conflitos de autoridade.

MIG-001 | Inventário, classificação e linhagem da migração Drive→KB | OWNER: MANIFESTO CANÔNICO DE MIGRAÇÃO v1.8.

AG-001 | Política do SDLC agentivo, papéis, hierarquia, gates e estados externos | OWNER: AGENT\_POLICY.md.

AG-002 | Status das decisões agentivas humanas | OWNER: .ai/decisions/INDEX.md | CONTEÚDO: arquivo da decisão ACTIVE correspondente.

AG-003 | Contratos, schemas, validadores e oráculos executáveis do control plane | OWNER: .ai/control/\*\* por tipo de contrato.

AG-004 | Modos do control plane | OWNER: .ai/control/control-plane.json.

AG-005 | Mapeamento operation\_class → runbooks | OWNER: .ai/control/runbook-catalog.json.

AG-006 | Estado material de uma TASK específica | OWNER: .ai/tasks/<TASK-ID>/proposal.json + approval.json + execution-result.json conforme lifecycle e AGENT\_POLICY.

AG-007 | Adaptação Claude Planner/Executor | OWNER: CLAUDE.md | não redefine AG-001.

AG-008 | Adaptação Codex Reviewer | OWNER: AGENTS.md | não redefine AG-001.

PD-001 | Produto e regras do domínio do CEPRAEA BEACH PRO | OWNER: PRODUCT-DOMAIN-SPEC.md v2.10.

PD-002 | Charter: visão, objetivos, não objetivos, atores, escopo e primeira entrega | OWNER: 02-PROJECT-CHARTER.md.

PD-003 | Contrato lógico derivado do fluxo de treino | OWNER: TRAINING\_FLOW\_CONTRACT.md v1.6 | PD-001 prevalece semanticamente.

PD-004 | Guardrails de qualidade/currentness/gaps/gates do product lifecycle | OWNER: PRODUCT-QUALITY-GUARDRAILS.md.

UX-001 | Detalhamento de UX/interação ainda residente no AESDS | OWNER ATUAL TEMPORÁRIO: AESDS 02 | transferência futura exige consolidação validada.

ARCH-001 | Arquitetura técnica/contratos de frontend ainda residentes no AESDS | OWNER ATUAL TEMPORÁRIO: AESDS 03 | não substitui ADR/contrato executável que venha a ser promovido.

ROAD-001 | Roadmap documental/grafo de dependências | OWNER: AESDS 04 | TASK material específica é governada por AG-006.

TEST-001 | Estratégia documental geral de testes/verificação | OWNER ATUAL TEMPORÁRIO: AESDS 06 | resultado real pertence à execução observável do teste.

RES-001 | Catálogo/protocolo de pesquisa AESDS | OWNER ATUAL TEMPORÁRIO: AESDS 08.

MOD-001 | Roteamento, ordem de leitura e continuidade da Modelagem Canônica Drive | OWNER: README — MODELAGEM CANÔNICA.

MOD-002 | Inventário/proveniência das fontes de modelagem | OWNER: 01-MANIFESTO-DE-FONTES.

MOD-003 | Catálogo de regras extraídas/internalizadas | OWNER: 02-CATALOGO-DE-REGRAS.

MOD-004 | Baseline e decisões semânticas homologadas | OWNER: 09-REGISTRO-SEMANTICO-CANONICO + SGATE APPROVED aplicável.

MOD-005 | Projeção terminológica corrente | OWNER: 03-GLOSSARIO-CANONICO v3.1.1 | MOD-004 prevalece em divergência.

MOD-006 | Modelo conceitual corrente | OWNER: 04A-MODELO-CONCEITUAL.

MOD-007 | Modelo lógico corrente | OWNER: 04B-MODELO-LOGICO.

MOD-008 | Decisões internas de arquitetura de dados | OWNER: 08-REGISTRO-DE-DECISOES-ARQUITETURAIS — DADOS.

MOD-009 | Estado/linhagem corrente dos artefatos de modelagem | OWNER: 20-CURRENT-STATE-INDEX.

MOD-010 | Processo de reconstrução orientada por evidência no repositório | OWNER: docs/modelagem/PLANO\_CEPRAEA\_Modelo\_Canonico\_FINAL.md | não é owner do conteúdo corrente do modelo até promoção validada.

OPS-001 | Dados operacionais estruturados materializados e exports para frontend | OWNER: CEPRAEA DATABASE.

OPS-002 | Cadastro/função/posição primária da atleta | OWNER: CEPRAEA DATABASE / DB\_ATLETAS nos campos declarados como autoridade.

OPS-003 | Disponibilidade declarada materializada | OWNER: CEPRAEA DATABASE / DB\_DISPONIBILIDADE\_DECLARADA.

OPS-004 | Declarações de disponibilidade/compromisso de setembro de 2026 ainda não materializadas na OPS-003 | OWNER DA EVIDÊNCIA DE CAPTURA: CEPRAEA AGOSTO 2026 / aba SETEMBRO - 2026 | ESTADO: staging/capture, não SSOT materializada.

OPS-005 | Presença factual confirmada | OWNER: CEPRAEA DATABASE / DB\_PRESENCA.

OPS-006 | Configuração e declarações brutas Wellness Pré/Pós | OWNER: CEPRAEA — Wellness — Configuração e Respostas.

OPS-007 | Agenda/interface/histórico mensal apresentados pela planilha | OWNER DA APRESENTAÇÃO/INTERAÇÃO: CEPRAEA AGOSTO 2026 | campos importados continuam pertencendo à DATABASE.

BASE-001 | Mapa derivado de ownership, resultados dos gates e histórico desta consolidação | OWNER: esta BASE | autoridade derivada; não altera owners upstream.

RESULTADO DE UNICIDADE: nenhum SUBJECT-ID acima possui dois owners concorrentes no mesmo escopo e effectivity. Onde havia dois artefatos, a relação foi resolvida como delegação, projeção, adaptação, processo vs conteúdo, materialização vs captura, ou histórico vs vigente.

**00.3 Gates de Migração**

GATES DA DERIVAÇÃO CORPUS → DOCUMENTAÇÃO

G-DER-01 — EVIDENCE TRACE

PASS somente se a proposta referencia SOURCE-ID/EVIDENCE-ID ou registra explicitamente que a matéria é decisão local sem evidência externa determinante.

G-DER-02 — BOUNDARY CHECK

PASS somente se a interpretação não excede o claim observado nem ignora limitações registradas no corpus.

G-DER-03 — LOCAL DECISION ID

PASS somente se toda escolha criada pelo CEPRAEA possui DECISION-ID e não é redigida como se fosse obrigação da fonte externa.

G-DER-04 — CANONICAL OWNER

PASS somente se o assunto possui um único proprietário canônico; registros de navegação, índices e contexto apontam para ele sem duplicar a regra.

G-DER-05 — VALIDATION

PASS somente se o tipo de validação adequado foi executado: estrutural para schema/formato; semântica para constraints/regras modeladas; factual para claims sobre estado observável.

G-DER-06 — HUMAN APPROVAL

PASS somente com aprovação humana explícita do conteúdo local. Até então, status = PROPOSED.

G-DER-07 — EFFECTIVITY

PASS somente depois de G-DER-01..06. Somente então a decisão/documentação pode ser marcada EFFECTIVE.

ESTADO ATUAL DESTA BASE

G-DER-01: PASS para as nove decisões propostas, por rastreabilidade ao corpus ou declaração explícita de decisão local.

G-DER-02: PASS na redação inicial, preservando limitações do corpus.

G-DER-03: PASS — DEC-DOC-001..007 e DEC-AG-001..002 criados.

G-DER-04: PROPOSED — proprietários definidos por abas desta BASE; precisa ser validado contra o conjunto documental do repositório antes de EFFECTIVE.

G-DER-05: NOT EXECUTED.

G-DER-06: NOT EXECUTED.

G-DER-07: BLOCKED por G-DER-04..06.

OWNER-COLLISION CHECK — 2026-09-06

Resultado: G-DER-04 = BLOCKED\_PENDING\_RECONCILIATION.

Evidência observada no Drive: o “Guia de Processos de Engenharia — CEPRAEA Beach Pro” já declara docs/GLOSSARY.md como canonical owner do vocabulário; outros artefatos existentes também contêm claims de fonte canônica/precedência em seus domínios específicos.

Conclusão: a BASE não deve se autodeclarar EFFECTIVE nem substituir esses owners. É necessário reconciliar o mapa de owners existentes por assunto antes de G-DER-04 PASS.

ESTADO FINAL DESTA WAVE — OWNER RECONCILIATION + VALIDATION — 2026-09-06

Este bloco supersede, para o estado corrente, o OWNER-COLLISION CHECK provisório acima; o texto anterior é preservado como histórico auditável.

G-DER-01: PASS — mantido.

G-DER-02: PASS — mantido.

G-DER-03: PASS — mantido.

G-DER-04: PASS, escopo explícito = claims normativos/promovidos acessíveis e classificados no Drive/repositório. Owner-map v0.1 resolve cada assunto por escopo/effectivity e elimina colisões por status, delegação, especialização, adaptação, processo-vs-conteúdo e captura-vs-materialização. Este PASS não equivale ao fechamento do Gate 2 global do Manifesto v1.8; shortcuts sem target comprovado permanecem inelegíveis para owner.

G-DER-05: EXECUTED — FAIL. Validação estrutural e semântica passou; currentness operacional de disponibilidade falhou porque setembro existe na superfície de captura e não foi encontrado em DB\_DISPONIBILIDADE\_DECLARADA no intervalo validado.

G-DER-06: NOT EXECUTED — aprovação humana explícita ainda inexistente.

G-DER-07: BLOCKED por G-DER-05 FAIL e G-DER-06 NOT EXECUTED.

Consequência: a BASE continua PROPOSED. Nenhum conteúdo deste bloco autoriza EFFECTIVE, exclusão de fontes, fechamento do Gate 2 ou promoção de proposta contradita pela evidência.

**10 Navegação e Roteamento**

**10.1 Mapa de Perguntas**

MAPA DE PERGUNTAS — CORPUS → DECISÃO / ESTADO

Q-ID-02 → DEC-DOC-001 → PROPOSED → E051–E055 → GAP-11 COMPLETE.

Q-ST-02 → DEC-DOC-002 → PROPOSED → E056–E057 → GAP-12 COMPLETE.

Q-AU-01 → DEC-DOC-003 → PROPOSED → E053,E058 → GAP-13 COMPLETE.

Q-AU-02 → DEC-DOC-004 → PROPOSED → E058,E059 → GAP-14 COMPLETE.

Q-DS-01 → DEC-DOC-005 → PROPOSED → GAP-01 COMPLETE; state machine = escolha local.

Q-QL-02 → DEC-DOC-006 → PROPOSED → E060 (+E061 incidental) → GAP-15 COMPLETE.

Q-VA-03 → DEC-DOC-007 → PROPOSED → E065–E066 → GAP-17 COMPLETE.

Q-AG-02 → DEC-AG-001 → PROPOSED → E067–E070,E077 → GAP-18 COMPLETE.

Q-AG-03 → DEC-AG-002 → PROPOSED → E071–E076 → GAP-19 COMPLETE.

QUESTÕES PARCIAIS PRESERVADAS SEM PROMOÇÃO

Q-SE-02 — PARCIALMENTE\_FUNDAMENTADA — GAP-08 COMPLETE.

Q-TR-01 — PARCIALMENTE\_FUNDAMENTADA — GAP-03 COMPLETE.

Q-QL-01 — PARCIALMENTE\_FUNDAMENTADA — accuracy/completeness/consistency fortalecidas; unambiguity incompleta.

Q-DR-01 — PARCIALMENTE\_FUNDAMENTADA — GAP-06 COMPLETE.

Q-DR-02 — PARCIALMENTE\_FUNDAMENTADA — GAP-06 COMPLETE.

Q-MC-02 — PARCIALMENTE\_FUNDAMENTADA — historical directed trace; sem GAP-ID formal.

Q-AG-01 — PARCIALMENTE\_FUNDAMENTADA — historical directed trace; sem GAP-ID formal.

REGRA DE RECUPERAÇÃO: uma pergunta parcial não deve ser respondida como totalmente resolvida apenas porque uma decisão local relacionada foi criada.

SÍNTESE SUBSTANTIVA DO CORPUS — 35 QUESTION-IDs — CURRENT CONTINUATION POINT

AUTORIDADE DE ORIGEM: Pesquisa CEPRAEA BEACH PRO — matriz final de cobertura pós-Phase B, corpus CANONICAL v1.0.

REGRA DE LEITURA: esta seção é a continuação canônica após o encerramento da pesquisa. Ela não apaga nem reescreve as propostas DEC-\*, OWNER-MAP ou G-DER já registradas nesta BASE; esses materiais permanecem históricos/PROPOSED. Nenhuma dessas propostas é usada como evidência para preencher esta síntese.

SEPARAÇÃO OBRIGATÓRIA POR QUESTION-ID:

EVIDÊNCIA OBSERVADA → LIMITE / NÃO SUSTENTA → INTERPRETAÇÃO APLICÁVEL → CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL → DECISÃO LOCAL NECESSÁRIA.

Nesta etapa não se decide nenhuma das nove políticas locais. Para questões classificadas DECISAO\_DO\_PROJETO\_NECESSARIA, registra-se somente a pergunta de decisão que deverá ser deliberada posteriormente.

Q-CR-01

PERGUNTA OPERACIONAL: Requisitos devem ser claros, não ambíguos e verificáveis?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-005, SRC-010 / E001, E004.

EVIDÊNCIA OBSERVADA: a evidência observada de ISO/IEC/IEEE 29148 sustenta características como necessidade, não ambiguidade e singularidade no escopo acessível; ISO/IEC/IEEE 15289 sustenta information items ao longo do ciclo de vida.

LIMITE / NÃO SUSTENTA: o corpus não verificou integralmente, em cláusulas pagas não acessíveis, uma lista completa de todas as características normativas de qualidade de requisito; 15289 não define o sistema documental de agentes do CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: existe fundamento externo suficiente para tratar clareza, não ambiguidade e verificabilidade como propriedades relevantes de requisitos, restrito ao que foi efetivamente observado.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: artefatos de requisitos podem ser avaliados com base nessas propriedades verificadas, sem ampliar o conjunto normativo por inferência.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-CR-02

PERGUNTA OPERACIONAL: Deve haver requisitos verificáveis, rastreáveis ou validados?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-007 / E002.

EVIDÊNCIA OBSERVADA: ISO 9001 sustenta manutenção e retenção de documented information como evidência de processos e resultados.

LIMITE / NÃO SUSTENTA: a fonte não define um grafo específico requirement→code→test nem um algoritmo de autoridade documental.

INTERPRETAÇÃO APLICÁVEL: há fundamento externo para controle e evidenciabilidade da informação documentada, mas não para um modelo completo de rastreabilidade técnica do CEPRAEA.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: usar a evidência como fundamento de controle documental; o modelo de rastreabilidade permanece tratado separadamente em Q-TR-01.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-CR-03

PERGUNTA OPERACIONAL: Há base para quality requirements e quality measures?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-009 / E003.

EVIDÊNCIA OBSERVADA: ISO/IEC 25010 fornece modelo de qualidade com características utilizáveis para especificar, medir e avaliar qualidade de produto.

LIMITE / NÃO SUSTENTA: a fonte não estabelece governança, lifecycle ou precedência da documentação do CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: existe base externa para quality requirements/measures no domínio de qualidade de produto, sem transformá-la em política documental geral.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: critérios de qualidade de produto podem referenciar esse fundamento quando aplicável; governança documental deve usar fundamentos próprios.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-ID-01

PERGUNTA OPERACIONAL: Como identificar documentos com metadata estruturada?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-024 / E011.

EVIDÊNCIA OBSERVADA: DCMI Metadata Terms fornece termos formais, definições, ranges e relações como version/modified/replacement utilizáveis em metadata estruturada.

LIMITE / NÃO SUSTENTA: DCMI não define um workflow universal de lifecycle documental nem garante consumo automático desses metadados por agentes.

INTERPRETAÇÃO APLICÁVEL: a identificação estruturada de documentos pode reutilizar vocabulários externos formalizados quando houver correspondência explícita.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: metadata futura pode mapear termos locais a vocabulários externos sem atribuir a eles semântica de workflow que não possuem.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-ID-02

PERGUNTA OPERACIONAL: Existe schema universal suficiente para todos os documentos?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-012, SRC-015, SRC-024, SRC-025 / E051–E055.

EVIDÊNCIA OBSERVADA: o corpus encontrou fundamentos externos para elementos de metadata, contexto, responsabilidade, proveniência e reutilização de vocabulários/application profiles.

LIMITE / NÃO SUSTENTA: nenhuma fonte observada fornece um schema pronto e universal que determine owner, state, domain, effectivity e todos os demais campos necessários ao CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: vocabulários externos podem compor um application profile local; a composição e obrigatoriedade desse perfil não são determinadas externamente.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: existe um input de decisão local, não uma política pronta.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual application profile local definirá owner, state, domain, effectivity e o uso dos vocabulários externos no CEPRAEA BEACH PRO?

Q-ST-01

PERGUNTA OPERACIONAL: Há convenções operacionais de estrutura documental?

ESTADO FINAL: FUNDAMENTADA\_POR\_FERRAMENTA.

SOURCE/EVIDENCE: SRC-051, SRC-052 / E043, E044.

EVIDÊNCIA OBSERVADA: o corpus verificou convenções operacionais de estrutura em documentação oficial das ferramentas analisadas.

LIMITE / NÃO SUSTENTA: essas convenções são específicas dos respectivos ambientes e não constituem padrão universal para todo o corpus documental.

INTERPRETAÇÃO APLICÁVEL: estruturas documentais podem seguir mecanismos oficiais da ferramenta quando aquela ferramenta for efetivamente adotada.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: distinguir convenção tool-specific de regra geral do CEPRAEA; não generalizar uma estrutura de uma ferramenta para todas as demais.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-ST-02

PERGUNTA OPERACIONAL: Existe schema formal e interoperável de frontmatter para o corpus?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-024, SRC-052, SRC-053, SRC-059, SRC-060 / E056, E057.

EVIDÊNCIA OBSERVADA: Jekyll documenta front matter; GitHub Docs utiliza YAML frontmatter para aspectos de navegação/renderização; o corpus também contém vocabulários externos reutilizáveis.

LIMITE / NÃO SUSTENTA: esses usos são tool-specific e não estabelecem um standard universal de front matter aplicável ao corpus do CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: front matter pode ser um mecanismo de implementação, mas seu schema, significado e interoperabilidade precisam ser definidos localmente caso seja adotado.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: a pesquisa produz o problema de design, não a escolha do schema.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual schema de front matter, índices/catálogos e navigation metadata será adotado pelo CEPRAEA BEACH PRO?

Q-SE-01

PERGUNTA OPERACIONAL: Como representar obrigações, recomendações, exemplos e evidências?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-027, SRC-028, SRC-029 / E014, E016.

EVIDÊNCIA OBSERVADA: JSON Schema fornece vocabulário/meta-schema/validação para dados JSON; Dublin Core fornece vocabulário formal de propriedades de metadata.

LIMITE / NÃO SUSTENTA: esses mecanismos não constituem uma semântica universal para linguagem natural nem validam a verdade factual de uma afirmação humana.

INTERPRETAÇÃO APLICÁVEL: representações machine-readable podem usar vocabulários e constraints formais, mantendo separada a semântica textual humana.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: quando uma propriedade for machine-readable, sua semântica deve ser vinculada ao vocabulário/schema aplicável; conteúdo humano não ganha formalidade apenas por estar em YAML/JSON.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-SE-02

PERGUNTA OPERACIONAL: Como selecionar semanticamente o documento autoritativo?

ESTADO FINAL: PARCIALMENTE\_FUNDAMENTADA.

SOURCE/EVIDENCE: SRC-007, SRC-009 / E002, E003; GAP-08 COMPLETE.

EVIDÊNCIA OBSERVADA: o corpus contém fundamentos de documented information e quality models relevantes para controle/qualidade.

LIMITE / NÃO SUSTENTA: não foi encontrada regra externa suficiente que determine um algoritmo universal de seleção semântica do documento autoritativo.

INTERPRETAÇÃO APLICÁVEL: os fundamentos ajudam a qualificar a informação, mas não resolvem automaticamente qual documento deve prevalecer semanticamente.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter esta questão como PARCIALMENTE\_FUNDAMENTADA; não alegar mecanismo universal de semantic authority/retrieval.

DECISÃO LOCAL NECESSÁRIA: NÃO — a pesquisa não converteu esta questão em DECISAO\_DO\_PROJETO\_NECESSARIA; o estado parcial deve ser preservado.

Q-SE-03

PERGUNTA OPERACIONAL: Como representar provenance e relações machine-readable?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-024, SRC-025, SRC-028 / E011, E012, E016.

EVIDÊNCIA OBSERVADA: DCMI e Dublin Core fornecem termos de metadata/relações; PROV-O fornece classes e propriedades para intercâmbio de provenance.

LIMITE / NÃO SUSTENTA: essas fontes não estabelecem workflow completo de lifecycle documental nem garantem que Codex/Claude produzam provenance automaticamente.

INTERPRETAÇÃO APLICÁVEL: relações e provenance machine-readable possuem fundamentos externos utilizáveis, desde que respeitado o domínio de cada vocabulário.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: futuras representações de provenance/relações podem referenciar esses modelos sem convertê-los em política de auditoria de agentes.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-AU-01

PERGUNTA OPERACIONAL: Há regra geral de source of truth e precedência entre requisitos, arquitetura, docs e código?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-011, SRC-016, SRC-035, SRC-036, SRC-061 / E053, E058.

EVIDÊNCIA OBSERVADA: ISO 15489-1 sustenta políticas, responsabilidades atribuídas e controles de records; ISO 10007 sustenta configuration management ao longo do lifecycle; mecanismos de repositório observados fornecem controles de mudança/revisão em seus escopos.

LIMITE / NÃO SUSTENTA: nenhuma dessas fontes determina uma precedência semântica universal requirement→architecture→docs→code nem uma source of truth global do CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: existe fundamento externo para accountability e configuration/change control, mas a autoridade semântica entre artefatos do projeto permanece escolha local.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: registrar a matéria como input de decisão; não converter mecanismos de Git/GitHub ou records management em hierarquia semântica universal.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual política de source-of-truth, ownership, approval e precedence entre artefatos será adotada pelo CEPRAEA BEACH PRO?

Q-AU-02

PERGUNTA OPERACIONAL: Como resolver conflitos entre documentos comuns?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-036, SRC-055, SRC-056, SRC-057, SRC-061, SRC-074 / E058, E059.

EVIDÊNCIA OBSERVADA: o corpus encontrou fundamentos de configuration/change control e modelos de status/lifecycle específicos de organizações/ferramentas; P828 foi observado como projeto ativo relacionado a configuration management, não como standard publicado vigente que determine a política do CEPRAEA.

LIMITE / NÃO SUSTENTA: não há regra externa universal que resolva conflitos semânticos entre documentos comuns, nem semântica universal de effectivity aplicável ao projeto.

INTERPRETAÇÃO APLICÁVEL: as fontes delimitam mecanismos e princípios de change control, mas não escolhem como o CEPRAEA resolverá conflitos de autoridade/conteúdo.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter uma pergunta de design explícita; não importar state models de outros domínios como política local.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual política de conflict resolution e quais semantics de effectivity/change control serão adotadas pelo CEPRAEA BEACH PRO?

Q-DS-01

PERGUNTA OPERACIONAL: Existe workflow normativo universal de estados documentais?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-055, SRC-056, SRC-057 / E046, E047; GAP-01 COMPLETE.

EVIDÊNCIA OBSERVADA: o corpus encontrou modelos/estados documentais ou de publicação em domínios específicos.

LIMITE / NÃO SUSTENTA: nenhum deles foi demonstrado como workflow normativo universal para todos os documentos de um repositório de software nem como máquina de estados obrigatória do CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: a pesquisa delimita que uma state machine documental geral, caso necessária, será uma construção local e não uma importação normativa automática.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: a pesquisa encerra a questão externa e entrega apenas o problema decisório.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual state machine documental será adotada pelo CEPRAEA BEACH PRO?

Q-TR-01

PERGUNTA OPERACIONAL: Existe modelo de rastreabilidade suficiente de requirement→doc→code→test→evidence?

ESTADO FINAL: PARCIALMENTE\_FUNDAMENTADA.

SOURCE/EVIDENCE: SRC-007, SRC-009 / E002, E003; GAP-03 COMPLETE.

EVIDÊNCIA OBSERVADA: o corpus possui fundamentos externos para documented information/evidence e para modelos de qualidade.

LIMITE / NÃO SUSTENTA: essas fontes não definem integralmente um modelo único e bidirecional requirement→doc→code→test→evidence para o CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: existe fundamento para necessidade de controle/evidência, mas não para afirmar que o grafo completo de rastreabilidade já está especificado externamente.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: preservar o estado PARCIALMENTE\_FUNDAMENTADA e não apresentar um modelo local futuro como se fosse requisito de uma dessas fontes.

DECISÃO LOCAL NECESSÁRIA: NÃO — a pesquisa não converteu esta questão em DECISAO\_DO\_PROJETO\_NECESSARIA; o estado parcial deve ser preservado.

Q-QL-01

PERGUNTA OPERACIONAL: Quais critérios de qualidade documental possuem base verificável?

ESTADO FINAL: PARCIALMENTE\_FUNDAMENTADA.

SOURCE/EVIDENCE: SRC-021, SRC-022, SRC-062 / E061.

EVIDÊNCIA OBSERVADA: a extensão da Phase B fortaleceu, por E061, fundamentos observados para accuracy, completeness, consistency e processos de review/evaluation de informação.

LIMITE / NÃO SUSTENTA: unambiguity permaneceu incompletamente fundamentada e o conjunto observado não constitui perfil normativo completo de qualidade documental para o CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: somente as propriedades efetivamente sustentadas podem ser tratadas como externamente fundamentadas; critérios restantes não devem ser promovidos por associação.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter esta questão PARCIALMENTE\_FUNDAMENTADA e separar critérios observados de critérios locais futuros.

DECISÃO LOCAL NECESSÁRIA: NÃO — o corpus preserva a parcialidade; não há autorização para completar o perfil nesta etapa.

Q-QL-02

PERGUNTA OPERACIONAL: Há perfil completo e normativo de qualidade documental para o projeto?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-053, SRC-024, SRC-025, SRC-062 / E060; E061 incidental.

EVIDÊNCIA OBSERVADA: ISO/IEC/IEEE 26511, no escopo observado, sustenta gestão/avaliação de qualidade de information for users e propriedades como consistência, completude, precisão e usabilidade; outras fontes fornecem metadata/provenance/validation primitives.

LIMITE / NÃO SUSTENTA: o corpus não fornece o perfil completo nem thresholds específicos de maintainability/currency do CEPRAEA.

INTERPRETAÇÃO APLICÁVEL: propriedades externas podem fundamentar dimensões do quality profile, mas seleção de critérios e thresholds do projeto é local.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: produzir posteriormente uma decisão de quality profile; não criar thresholds nesta síntese.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual quality profile e quais thresholds de maintainability/currency, além da base externa observada, serão adotados pelo CEPRAEA BEACH PRO?

Q-VA-01

PERGUNTA OPERACIONAL: É possível validar estrutura/metadados/links por automação?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-026, SRC-048, SRC-050 / E013, E041, E042.

EVIDÊNCIA OBSERVADA: o corpus verificou mecanismos automatizáveis de validação estrutural/schema e checks aplicáveis a formatos/documentação; SHACL, especificamente, valida RDF graphs contra conditions/shapes e produz validation results.

LIMITE / NÃO SUSTENTA: validação estrutural não prova verdade factual, correção de requisito em linguagem natural nem ausência de semantic drift em qualquer representação.

INTERPRETAÇÃO APLICÁVEL: automação é fundamentada quando existe uma representação/constraint verificável pelo mecanismo correspondente.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: futuros validators devem declarar qual propriedade estrutural estão verificando e não rotular esse resultado como validação factual/semântica geral.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-VA-02

PERGUNTA OPERACIONAL: É possível validar semântica/regras por automação?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-026, SRC-063, SRC-064 / E062–E064; GAP-16 COMPLETE.

EVIDÊNCIA OBSERVADA: SHACL valida constraints sobre RDF; Schematron oferece validação XML baseada em regras; OCL oferece linguagem formal de constraints/invariants para modelos.

LIMITE / NÃO SUSTENTA: esses mecanismos não verificam universalmente a verdade factual do software nem qualquer regra de negócio expressa apenas em linguagem natural; cada um opera dentro de sua representação formal.

INTERPRETAÇÃO APLICÁVEL: validação semântica/regras é automatizável quando a regra foi formalizada em um mecanismo machine-checkable compatível.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: diferenciar semantic/rule validation formal de structural validation e de factual validation; não generalizar um validator para representações que ele não suporta.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-VA-03

PERGUNTA OPERACIONAL: É possível validar factualmente a documentação contra o software?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-065, SRC-066 / E065, E066; GAP-17 COMPLETE.

EVIDÊNCIA OBSERVADA: IEEE 1012 fornece fundamento de verification and validation por análise, revisão, inspeção, assessment e testing para conformidade/intended use; ISO/IEC/IEEE 29119-2 fornece processos genéricos de software testing.

LIMITE / NÃO SUSTENTA: nenhuma fonte observada define o mapping específico CEPRAEA claim documental→requirement/code/test/runtime evidence→review nem uma política universal de verdade documental.

INTERPRETAÇÃO APLICÁVEL: V&V e testes fornecem base externa para verificar afirmações observáveis, mas o protocolo que liga claims documentais às evidências do CEPRAEA é local.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: registrar um input de decisão de factual validation; não definir o protocolo agora.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual protocolo de factual validation mapeará claim→requirement/code/test/runtime evidence→review no CEPRAEA BEACH PRO?

Q-DR-01

PERGUNTA OPERACIONAL: Há mecanismo universal para detectar semantic drift documentação↔software?

ESTADO FINAL: PARCIALMENTE\_FUNDAMENTADA.

SOURCE/EVIDENCE: SRC-045, SRC-058 / E035, E048; GAP-06 COMPLETE.

EVIDÊNCIA OBSERVADA: o corpus registrou mecanismos e práticas relevantes para manter ou verificar relação entre documentação e artefatos técnicos em contextos específicos.

LIMITE / NÃO SUSTENTA: nenhuma evidência observada estabelece um detector universal de semantic drift entre documentação e software, independente de representação, ferramenta e política local.

INTERPRETAÇÃO APLICÁVEL: os mecanismos encontrados podem reduzir risco ou detectar classes específicas de divergência, mas não resolvem semantic drift em geral.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter esta questão como PARCIALMENTE\_FUNDAMENTADA; qualquer mecanismo futuro deve declarar exatamente qual divergência consegue observar.

DECISÃO LOCAL NECESSÁRIA: NÃO — a pesquisa não converteu esta questão em DECISAO\_DO\_PROJETO\_NECESSARIA; o estado parcial deve ser preservado.

Q-DR-02

PERGUNTA OPERACIONAL: Há synchronization de docs↔software sem políticas locais?

ESTADO FINAL: PARCIALMENTE\_FUNDAMENTADA.

SOURCE/EVIDENCE: SRC-048, SRC-050, SRC-058 / E041, E042, E048; GAP-06 COMPLETE.

EVIDÊNCIA OBSERVADA: o corpus encontrou mecanismos de automação, geração/validação e integração úteis para manter documentação e artefatos técnicos relacionados em escopos determinados.

LIMITE / NÃO SUSTENTA: não foi demonstrada sincronização universal e automática docs↔software que dispense decisões sobre fonte, direção da geração, conflitos, escopo e autoridade.

INTERPRETAÇÃO APLICÁVEL: automação pode sincronizar representações específicas quando existe relação formalizada, mas não elimina governança local.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: preservar o status parcial e não tratar geração ou CI como prova de sincronização semântica completa.

DECISÃO LOCAL NECESSÁRIA: NÃO — a pesquisa não converteu esta questão em DECISAO\_DO\_PROJETO\_NECESSARIA; o estado parcial deve ser preservado.

Q-VE-01

PERGUNTA OPERACIONAL: Como preservar histórico e autoria?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-030, SRC-031 / E015.

EVIDÊNCIA OBSERVADA: o corpus classificou as fontes verificadas como fundamento externo suficiente para preservação de histórico/revisões e autoria no escopo técnico observado.

LIMITE / NÃO SUSTENTA: histórico técnico e autoria registrados não determinam, por si, autoridade semântica, approval ou versão vigente de uma regra.

INTERPRETAÇÃO APLICÁVEL: preservação de histórico/autoria pode apoiar auditabilidade e reconstrução de mudanças sem ser confundida com precedência documental.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter revision history e autoria como dimensões próprias; decisões de vigência/autoridade devem permanecer separadas.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-VE-02

PERGUNTA OPERACIONAL: Há base externa suficiente para versionamento/evolução?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-019, SRC-020 / E009, E010; GAP-04/05 historical.

EVIDÊNCIA OBSERVADA: Git sustenta histórico distribuído e integridade do histórico; GitHub fornece mecanismos de proteção/revisão de mudanças em branches.

LIMITE / NÃO SUSTENTA: versionamento técnico e branch protection não definem automaticamente autoridade semântica, data efetiva, supersessão ou política de lifecycle documental.

INTERPRETAÇÃO APLICÁVEL: há fundamento externo suficiente para versionamento/histórico técnico e controles de mudança, mas sem ampliar esses mecanismos para semântica documental não documentada.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: usar versionamento e change controls em seus escopos técnicos; tratar vigência/supersessão como questão distinta quando aplicável.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-PU-01

PERGUNTA OPERACIONAL: Há publicação/armazenamento com mecanismos reproduzíveis?

ESTADO FINAL: FUNDAMENTADA\_POR\_FERRAMENTA.

SOURCE/EVIDENCE: SRC-030, SRC-033, SRC-034, SRC-058 / E015, E017, E018, E048.

EVIDÊNCIA OBSERVADA: o corpus verificou mecanismos oficiais de ferramentas/repositório para workflows automatizados, publicação e controles associados.

LIMITE / NÃO SUSTENTA: esses mecanismos são tool-specific e não definem a autoridade semântica da documentação publicada nem uma arquitetura universal de armazenamento.

INTERPRETAÇÃO APLICÁVEL: publicação e automação reproduzível podem ser sustentadas pelas ferramentas efetivamente escolhidas, dentro de seus contratos documentados.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: distinguir fonte controlada, processo de build/publicação e superfície publicada; publicação não transforma conteúdo em autoritativo por si só.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-PU-02

PERGUNTA OPERACIONAL: É possível gerar/documentar publicação a partir de fonte controlada?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-052, SRC-053 / E044, E045.

EVIDÊNCIA OBSERVADA: o corpus encontrou fundamento suficiente para geração/publicação derivada de fonte controlada nos mecanismos analisados.

LIMITE / NÃO SUSTENTA: isso não define todo o lifecycle, approval, authority ou semantic currentness da documentação gerada.

INTERPRETAÇÃO APLICÁVEL: fonte controlada pode alimentar publicação derivada de forma reproduzível, desde que a relação source→output seja explícita.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter separadas a fonte autoritativa e suas projeções/publicações geradas; o output derivado não ganha autoridade adicional automaticamente.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-OA-01

PERGUNTA OPERACIONAL: Codex possui mecanismo oficial de descoberta de instrução?

ESTADO FINAL: FUNDAMENTADA\_POR\_FERRAMENTA.

SOURCE/EVIDENCE: SRC-037 / E021–E023.

EVIDÊNCIA OBSERVADA: documentação oficial do Codex sustenta descoberta/uso de AGENTS.md e mecanismos relacionados de instrução no ambiente Codex.

LIMITE / NÃO SUSTENTA: isso não demonstra como Claude Code opera, nem estabelece que documentos comuns do repositório sejam automaticamente carregados ou adquiram precedência semântica.

INTERPRETAÇÃO APLICÁVEL: instruções destinadas ao Codex devem respeitar o mecanismo oficial documentado para o próprio Codex.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: tratar AGENTS.md e mecanismos associados como superfície específica de instrução do Codex, separada da autoridade dos documentos comuns.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-OA-02

PERGUNTA OPERACIONAL: Codex possui discovery/precedence documentado?

ESTADO FINAL: FUNDAMENTADA\_POR\_FERRAMENTA.

SOURCE/EVIDENCE: SRC-037, SRC-038, SRC-039, SRC-040, SRC-041 / E021–E026.

EVIDÊNCIA OBSERVADA: o corpus verificou documentação oficial do Codex sobre escopo/hierarquia/precedência e mecanismos de instrução, incluindo comportamento específico de arquivos reconhecidos pelo produto.

LIMITE / NÃO SUSTENTA: a precedência documentada para instruções do Codex não constitui precedência geral entre requirements, ADRs, READMEs, código e outros documentos comuns; também não se aplica ao Claude Code.

INTERPRETAÇÃO APLICÁVEL: há fundamento tool-specific suficiente para roteamento de instruções do Codex dentro de seu contrato oficial.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: separar instruction precedence do Codex de semantic authority do sistema documental do projeto.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-AN-01

PERGUNTA OPERACIONAL: Claude Code possui mecanismo oficial de descoberta de instrução?

ESTADO FINAL: FUNDAMENTADA\_POR\_FERRAMENTA.

SOURCE/EVIDENCE: SRC-042 / E027–E032.

EVIDÊNCIA OBSERVADA: documentação oficial do Claude Code sustenta mecanismos próprios de descoberta/carregamento de instruções, incluindo CLAUDE.md e superfícies relacionadas documentadas no corpus.

LIMITE / NÃO SUSTENTA: esses mecanismos são específicos do Claude Code; não determinam o comportamento do Codex nem a autoridade semântica de documentos comuns do repositório.

INTERPRETAÇÃO APLICÁVEL: instruções destinadas ao Claude Code devem respeitar as superfícies e regras oficialmente documentadas para essa ferramenta.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter a camada de instruções do Claude Code distinta da camada documental autoritativa do projeto e distinta do Codex.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-AN-02

PERGUNTA OPERACIONAL: Claude Code possui discovery/precedence documentado?

ESTADO FINAL: FUNDAMENTADA\_POR\_FERRAMENTA.

SOURCE/EVIDENCE: SRC-042, SRC-043, SRC-044, SRC-045 / E027–E035.

EVIDÊNCIA OBSERVADA: o corpus verificou mecanismos oficiais do Claude Code relativos a carregamento, imports/rules/path scope e precedência no escopo de suas instruções.

LIMITE / NÃO SUSTENTA: essa precedência não é uma regra universal entre documentos comuns do CEPRAEA e não deve ser generalizada para Codex.

INTERPRETAÇÃO APLICÁVEL: existe fundamento tool-specific suficiente para estruturar instruções do Claude Code dentro do comportamento documentado da própria ferramenta.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: separar precedence de instruções Claude da semantic authority geral dos artefatos do projeto.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-MC-01

PERGUNTA OPERACIONAL: MCP oferece resource discovery/read machine-readable?

ESTADO FINAL: FUNDAMENTADA\_EXTERNAMENTE.

SOURCE/EVIDENCE: SRC-046 / E036–E039; GAP-07 residual já tratado no corpus.

EVIDÊNCIA OBSERVADA: a especificação/documentação MCP observada fornece primitives de Resources com identificação/URI e operações de discovery/list/read no escopo protocolar analisado.

LIMITE / NÃO SUSTENTA: MCP Resources não define governança dos documentos do repositório, autoridade semântica nem um algoritmo universal de retrieval relevante por tarefa.

INTERPRETAÇÃO APLICÁVEL: MCP oferece interface machine-readable para descoberta/leitura de resources quando implementada, mas não substitui arquitetura documental ou política de seleção.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: MCP pode ser tratado como uma interface de entrega/acesso, sem promovê-lo a source of truth ou motor universal de contexto.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

Q-MC-02

PERGUNTA OPERACIONAL: Existe semantic retrieval universal documentado?

ESTADO FINAL: PARCIALMENTE\_FUNDAMENTADA.

SOURCE/EVIDENCE: SRC-046, SRC-047 / E036–E040; historical directed trace reconciled; sem GAP-ID histórico formal inventado.

EVIDÊNCIA OBSERVADA: o corpus contém primitives de discovery/read e metadata/annotations aplicáveis a resources no ecossistema MCP analisado.

LIMITE / NÃO SUSTENTA: não foi demonstrado um algoritmo universal, vendor-neutral e semanticamente suficiente que selecione automaticamente o documento correto para qualquer tarefa.

INTERPRETAÇÃO APLICÁVEL: discovery/read são fundamentos úteis, mas não equivalem a semantic retrieval universal.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: preservar esta questão como PARCIALMENTE\_FUNDAMENTADA; não afirmar que MCP, metadata ou search resolvem por si a seleção semântica de contexto.

DECISÃO LOCAL NECESSÁRIA: NÃO — a pesquisa não converteu esta questão em DECISAO\_DO\_PROJETO\_NECESSARIA; o estado parcial deve ser preservado.

Q-AG-01

PERGUNTA OPERACIONAL: Há convenção nativa comum de instrução entre Codex e Claude?

ESTADO FINAL: PARCIALMENTE\_FUNDAMENTADA.

SOURCE/EVIDENCE: SRC-039, SRC-042, SRC-043, SRC-046 / E024, E027–E033, E036–E039; historical directed trace reconciled; sem GAP-ID histórico formal inventado.

EVIDÊNCIA OBSERVADA: Codex, Claude Code e MCP possuem mecanismos próprios e documentados de instrução/contexto/resources em seus respectivos escopos.

LIMITE / NÃO SUSTENTA: o corpus não encontrou uma convenção nativa única que Codex e Claude Code reconheçam com a mesma semântica e precedência.

INTERPRETAÇÃO APLICÁVEL: interoperabilidade não pode ser presumida apenas porque ambos consomem arquivos de texto/Markdown; diferenças de discovery e precedence devem ser preservadas.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter esta questão como PARCIALMENTE\_FUNDAMENTADA e não declarar um formato comum como capability nativa de ambas as ferramentas.

DECISÃO LOCAL NECESSÁRIA: NÃO — a pesquisa não converteu esta questão em DECISAO\_DO\_PROJETO\_NECESSARIA; o estado parcial deve ser preservado.

Q-AG-02

PERGUNTA OPERACIONAL: Há política universal ask/stop/unknown/escalate?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-042, SRC-046, SRC-067, SRC-068, SRC-070, SRC-072, SRC-073 / E067–E070, E077; GAP-18 COMPLETE.

EVIDÊNCIA OBSERVADA: Claude Code expõe mecanismos próprios de allow/ask/deny; Codex possui approval/gating modes; MCP possui input\_required em escopos documentados e extensões com negociação/suporte explícito.

LIMITE / NÃO SUSTENTA: nenhum desses mecanismos define uma ontologia universal comum ASK/STOP/UNKNOWN/ESCALATE para o CEPRAEA; capability de uma ferramenta não determina a política de governança do projeto.

INTERPRETAÇÃO APLICÁVEL: existem primitives específicas para input/approval/bloqueio, mas uma semântica comum entre agentes, se desejada, precisa ser decidida localmente e adaptada às capabilities reais.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: manter apenas o input decisório; não definir os significados ou transições desses termos nesta etapa.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual política comum de ASK / STOP / UNKNOWN / ESCALATE será adotada pelo CEPRAEA BEACH PRO, separada das capabilities específicas de Codex, Claude Code e MCP?

Q-AG-03

PERGUNTA OPERACIONAL: Há audit trail obrigatório de fontes consultadas e conflitos?

ESTADO FINAL: DECISAO\_DO\_PROJETO\_NECESSARIA.

SOURCE/EVIDENCE: SRC-025, SRC-044, SRC-069, SRC-071, SRC-072, SRC-075 / E071–E076; GAP-19 COMPLETE.

EVIDÊNCIA OBSERVADA: o corpus verificou eventos observáveis de execução, JSONL/tool events e hooks/transcript paths em ferramentas específicas, PROV-O para provenance e tracing/observability em implementações MCP analisadas.

LIMITE / NÃO SUSTENTA: essas primitives não fornecem hidden chain-of-thought, não provam correção das decisões do modelo e não constituem requisito protocolar universal de audit trail para todas as ferramentas; logging MCP observado possui limites/versionamento específicos.

INTERPRETAÇÃO APLICÁVEL: há base externa para registrar provenance e eventos observáveis, mas schema, campos obrigatórios e retenção do audit trail do CEPRAEA permanecem locais.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: registrar a necessidade de decisão sem criar o schema nem prazo de retenção agora.

DECISÃO LOCAL NECESSÁRIA: SIM.

PERGUNTA DE DECISÃO: Qual schema e qual retention policy serão adotados para o agent documentary audit trail do CEPRAEA BEACH PRO?

Q-GV-01

PERGUNTA OPERACIONAL: Há mecanismos oficiais de governança GitHub para ownership/change control?

ESTADO FINAL: FUNDAMENTADA\_POR\_FERRAMENTA.

SOURCE/EVIDENCE: SRC-030, SRC-033, SRC-034, SRC-035, SRC-036 / E015, E017, E018, E019, E020.

EVIDÊNCIA OBSERVADA: documentação oficial do GitHub sustenta mecanismos como Actions/workflows, CODEOWNERS, branch protection e rules/merge controls nos respectivos escopos.

LIMITE / NÃO SUSTENTA: esses mecanismos não estabelecem uma source of truth semântica universal nem resolvem, por si, conflitos de significado entre documentos.

INTERPRETAÇÃO APLICÁVEL: há fundamento tool-specific suficiente para ownership/review/change control operacional em repositórios GitHub.

CONSEQUÊNCIA PARA O SISTEMA DOCUMENTAL: mecanismos GitHub podem executar/enforce partes da governança escolhida, mas não devem ser confundidos com a política semântica que decidem executar.

DECISÃO LOCAL NECESSÁRIA: NÃO para fechar esta QUESTION-ID.

CONTAGEM DE CONTROLE DA SÍNTESE

FUNDAMENTADA\_EXTERNAMENTE: 12

FUNDAMENTADA\_POR\_FERRAMENTA: 7

PARCIALMENTE\_FUNDAMENTADA: 7

DECISAO\_DO\_PROJETO\_NECESSARIA: 9

NÃO\_VERIFICADO: 0

TOTAL QUESTION-IDs: 35

CHECK ARITMÉTICO: 12 + 7 + 7 + 9 = 35 — PASS.

NOVE INPUTS DE DECISÃO, SEM POLÍTICA DEFINIDA NESTA ETAPA:

Q-ID-02; Q-ST-02; Q-AU-01; Q-AU-02; Q-DS-01; Q-QL-02; Q-VA-03; Q-AG-02; Q-AG-03.

SETE QUESTÕES PARCIAIS PRESERVADAS SEM PROMOÇÃO:

Q-SE-02; Q-TR-01; Q-QL-01; Q-DR-01; Q-DR-02; Q-MC-02; Q-AG-01.

REGRA DE CONTINUAÇÃO: a próxima etapa só pode deliberar políticas locais a partir dos nove inputs de decisão acima, confrontando cada pergunta com suas evidências e limites. Propostas DEC-\*, OWNER-MAP e G-DER já existentes permanecem histórico/PROPOSED e não constituem respostas aprovadas para essas nove decisões.

**10.2 Contrato de Entrega de Contexto**

CONTRATO DE ENTREGA DE CONTEXTO PARA AGENTES

OBJETIVO: permitir que Claude Code, Codex ou outro executor encontre a autoridade correta sem carregar nem reinterpretar todo o histórico de pesquisa.

CD-01 — Antes de responder/editar, identificar a QUESTION/INTENT e o assunto canônico correspondente.

CD-02 — Carregar primeiro o proprietário canônico da regra/decisão; usar índices apenas para roteamento.

CD-03 — Quando uma decisão local depender de fundamento externo, preservar a cadeia DECISION-ID → EVIDENCE-ID → SOURCE-ID. Não reescrever a evidência como opinião do agente.

CD-04 — Se o proprietário canônico não for identificável, usar UNKNOWN; não selecionar o documento mais parecido por conveniência.

CD-05 — Em conflito, aplicar a política DEC-DOC-003/004. Se o conflito persistir, ESCALATE e bloquear a promoção/alteração dependente.

CD-06 — Para falta de input humano necessário, aplicar DEC-AG-001. ASK não significa inventar a resposta provável.

CD-07 — Não generalizar capabilities entre Codex, Claude Code e MCP. Cada adapter deve citar a capability específica que realmente possui.

CD-08 — Resumos, CLAUDE.md, AGENTS.md, índices e briefs são mecanismos de descoberta/entrega de contexto; não adquirem autoridade sobre o conteúdo que resumem salvo decisão explícita de ownership.

CD-09 — Registrar, quando a execução for auditável, os eventos observáveis conforme DEC-AG-002; não exigir nem alegar captura de hidden chain-of-thought.

SAÍDA MÍNIMA DE UMA RESPOSTA DOCUMENTAL DO AGENTE

AUTHORITATIVE\_OWNER: <documento/section>

DECISION\_REFS: <IDs ou NONE>

EVIDENCE\_REFS: <IDs ou NONE>

STATE: <EFFECTIVE/PROPOSED/PARTIAL/UNKNOWN>

CONFLICT: <NONE ou descrição>

RESULT: <conteúdo>

**20 Conhecimento**

**20.1 Produto e Domínio**

**20.2 Modelagem Canônica**

**20.3 Governança Documental**

POLÍTICAS DOCUMENTAIS PROPOSTAS — DETALHAMENTO OPERACIONAL

1\. METADATA PROFILE — owner: DEC-DOC-001

Os campos mínimos propostos em DOCUMENT\_METADATA\_PROFILE v0.1 são locais. source\_refs aponta para evidência externa quando aplicável; decision\_refs aponta para escolhas locais que controlam o documento. supersedes deve ser usado apenas quando existir relação real de substituição.

2\. FRONT MATTER / CATALOG — owner: DEC-DOC-002

Markdown canônico usa YAML front matter conforme o perfil local. O catálogo deve ser derivado dos metadados; não deve tornar-se segunda cópia manual da mesma semântica. A validação estrutural do front matter deve ser automatizável por schema antes de promoção.

3\. QUALIDADE — owner: DEC-DOC-006

Quality gate mínimo proposto: 100% dos metadados obrigatórios presentes; 0 conflitos bloqueadores abertos; 0 claims apresentados como obrigação externa sem evidence trace; referências canônicas resolvidas; currentness verificada; um owner canônico declarado para o assunto. Critérios quantitativos são política local, não requisitos extraídos das fontes.

4\. FACTUAL VALIDATION — owner: DEC-DOC-007

Para claim factual de estado atual registrar: CLAIM-ID; objeto observado; fonte/artefato observado; revisão/versão; método de verificação; evidência; resultado; data; reviewer. Divergência entre requisito desejado e implementação deve gerar conflito explícito; não alterar o requisito para “bater” com o código.

5\. AUDIT EVENT PROFILE — owner: DEC-AG-002

O audit trail registra somente sinais observáveis. Não registrar ou exigir hidden reasoning. retention\_class inicial proposta: DECISION\_EVIDENCE, PROMOTION\_AUDIT, EXECUTION\_TRACE, TRANSIENT\_DEBUG. Prazos de retenção permanecem UNDECIDED nesta versão porque o corpus não os determina.

**30 Corpus Canônico**

**30.1 Registro de Fontes Wave 1**

REGISTRO DE REFERÊNCIA AO CORPUS CANÔNICO

OWNER DA EVIDÊNCIA: documento “Pesquisa CEPRAEA BEACH PRO”, corpus CANONICAL v1.0, pesquisa DONE.

TOTAL SUBSTANTIVE SOURCES: 71.

PROMOTION SUMMARY registrado no corpus: 34 CANONICAL; 19 CANONICAL\_VENDOR\_SPECIFIC; 9 REFERENCE\_ONLY; 9 MONITOR\_FOR\_UPDATE.

Esta aba NÃO replica as 71 fontes. Seu papel é registrar o vínculo da BASE com o corpus que permanece proprietário de SOURCE-ID, EVIDENCE-ID, appraisal, charting, search provenance e limitações.

SUBCONJUNTO CONSUMIDO PARA AS NOVE DECISÕES DESTA WAVE

Q-ID-02: SRC-012,015,024,025 / E051–E055.

Q-ST-02: SRC-024,052,053,059,060 / E056–E057.

Q-AU-01: SRC-011,016,035,036,061 / E053,E058.

Q-AU-02: SRC-036,055–057,061,074 / E058,E059.

Q-QL-02: SRC-053,024,025,062 / E060 (+E061 incidental).

Q-VA-03: SRC-065,066 / E065,E066.

Q-AG-02: SRC-042,046,067,068,070,072,073 / E067–E070,E077.

Q-AG-03: SRC-025,044,069,071,072,075 / E071–E076.

Q-DS-01: decisão local já identificada no corpus; não foi atribuída a uma fonte externa universal.

**30.2 Proveniência e Precedência**

PROVENIÊNCIA E PRECEDÊNCIA

CADEIA CANÔNICA DE DERIVAÇÃO

SOURCE-ID → EVIDENCE-ID → INTERPRETATION → DECISION-ID → DOCUMENT OWNER → VALIDATION EVIDENCE → APPROVAL → EFFECTIVE VERSION.

REGRAS

P-01 — SOURCE-ID/EVIDENCE-ID preservam o que foi observado externamente; não recebem texto criado para justificar decisão posterior.

P-02 — INTERPRETATION deve declarar limites de aplicabilidade e não pode converter DESCRIÇÃO\_TÉCNICA/EXEMPLO em obrigação normativa.

P-03 — DECISION-ID identifica semântica criada pelo CEPRAEA.

P-04 — DOCUMENT OWNER é a única localização autorizada a definir aquela regra; documentos derivados referenciam o owner.

P-05 — Evidência factual de implementação demonstra estado observado, mas não adquire automaticamente precedência sobre requisito/decisão que define estado desejado.

P-06 — Em substituição, registrar supersedes/superseded\_by e preservar a versão histórica.

PRECEDÊNCIA LOCAL PROPOSTA

Não existe uma única hierarquia global que permita um tipo de documento sobrescrever todos os demais. Primeiro resolve-se pelo assunto e owner. Para o mesmo assunto: versão EFFECTIVE vigente do owner > versão anterior/superseded do mesmo owner > documento derivado/resumo. Conflitos entre owners de escopos diferentes são analisados por fronteira semântica; se houver sobreposição real sem regra de precedência explícita, ESCALATE.

INVENTÁRIO DE CLAIMS DE CANONICAL OWNERSHIP — WAVE 2026-09-06

Critério de inclusão: claim explícito de fonte canônica, owner, SSOT, autoridade, precedência, contrato/oráculo, baseline homologado ou equivalente, limitado a artefatos acessíveis e classificados. Histórico, backup, rascunho, conteúdo derivado e shortcuts sem target comprovado são inventariados como claimants, mas não podem ser promovidos a owner.

CLM-001 | Normas / SRC-DOC-016 | claim: autoridade canônica por assunto para o sistema documental | estado: ATUAL/EM USO | disposição: OWNER no escopo documental geral.

CLM-002 | Templates/CATE / SRC-DOC-018 | claim: autoridade canônica delegada para taxonomia, seleção, estrutura, instanciação, validação específica, versão e lifecycle de templates | disposição: OWNER especializado, subordinado a Normas.

CLM-003 | Guia de Processos de Engenharia | claim histórico: docs/GLOSSARY.md como proprietário canônico absoluto do vocabulário | disposição: NÃO ELEGÍVEL para owner global; claim não prevalece sobre classificação/autoridade corrente.

CLM-004 | docs/linters/guia\_estilo\_documentação.md | claim: padrão normativo para Markdown do repositório | disposição: OWNER do perfil Markdown do repo, especialização subordinada à política do repositório e ao sistema documental.

CLM-005 | PRODUCT-DOMAIN-SPEC.md / SRC-ENG-019 | claim: especificação consolidada de produto e regras do domínio | estado: ATUAL/APROVADO v2.10 | disposição: OWNER de produto/domínio.

CLM-006 | 02-PROJECT-CHARTER.md / SRC-ENG-003 | claim: charter canônico de visão, objetivos, não objetivos, atores, escopo e primeira entrega | disposição: OWNER do charter; derivado de PRODUCT-DOMAIN-SPEC.

CLM-007 | TRAINING\_FLOW\_CONTRACT.md / SRC-ENG-020 | claim: contrato lógico canônico derivado do fluxo de treino | disposição: OWNER do contrato derivado; PRODUCT-DOMAIN-SPEC prevalece em conflito semântico.

CLM-008 | PRODUCT-QUALITY-GUARDRAILS.md / SRC-ENG-018 | claim: política ativa/human-approved de qualidade/currentness/gaps/gates/evidência/UX/canonicalização no PRODUCT\_LIFECYCLE | disposição: OWNER desse escopo.

CLM-009 | AESDS 01 | claim: contrato de produto/domínio para consumo por agentes | disposição: NÃO substitui o Modelo Canônico nem a fonte de produto; contrato de consumo subordinado.

CLM-010 | AESDS 02 | claim: especificação de UX/interação | disposição: OWNER temporário do detalhamento UX ainda não consolidado em owner sucessor.

CLM-011 | AESDS 03 | claim: arquitetura técnica/contratos de frontend | disposição: OWNER temporário desse escopo, até transferência explícita para arquitetura/ADRs sucessores.

CLM-012 | AESDS 04 | claim: roadmap/grafo de tarefas | disposição: OWNER do roadmap documental; TASK corrente do repositório prevalece para execução material específica.

CLM-013 | AESDS 05 | claim: padrão de tarefas atômicas/aceitação | disposição: não governa a TASK material atual quando AGENT\_POLICY/.ai definem contrato operacional vigente.

CLM-014 | AESDS 06 | claim: especificação geral de testes/verificação | disposição: OWNER temporário da estratégia documental geral; validadores/testes executáveis específicos prevalecem como evidência do seu próprio escopo.

CLM-015 | AESDS 07 | claim: protocolo de execução/review de agentes | disposição: SUPERADO operacionalmente pela política vigente do repositório; manter como referência até arquivamento.

CLM-016 | AESDS 08 | claim: catálogo de referências/protocolo de pesquisa | disposição: OWNER temporário desse escopo, salvo protocolo mais específico aprovado.

CLM-017 | AESDS 09 | claim: índice de runbooks/estado operacional | disposição: SUPERADO para roteamento executável pelo runbook-catalog e control-plane atuais do repositório.

CLM-018 | AESDS 10 | claim: catálogo canônico de artefatos/papéis/enforcement | disposição: SUPERADO para enforcement operacional por AGENT\_POLICY/.ai; referência histórica/explicativa até consolidação.

CLM-019 | AESDS 11 | claim: arquitetura de auditoria/assurance agêntico | disposição: referência arquitetural; contratos/evidência operacionais atuais pertencem a AGENT\_POLICY/.ai/control.

CLM-020 | AGENT\_POLICY.md | claim: política comum canônica do SDLC agentivo e hierarquia normativa | disposição: OWNER da política agentiva do repositório.

CLM-021 | .ai/decisions/INDEX.md + decisão ACTIVE | claim: registro de decisões humanas ativas | disposição: INDEX é owner do status; cada arquivo ACTIVE é owner do conteúdo da decisão identificada.

CLM-022 | .ai/control/\*\* | claim: contratos executáveis/oráculos | disposição: OWNER do control plane executável no seu tipo de contrato.

CLM-023 | .ai/control/control-plane.json | claim: fonte única dos modos do control plane | disposição: OWNER de bootstrap\_mode/fvr\_mode e demais modos declarados.

CLM-024 | .ai/control/runbook-catalog.json | claim: resolução operation\_class → runbooks | disposição: OWNER dessa matriz.

CLM-025 | CLAUDE.md | claim implícito/adaptador do Planner/Executor | disposição: OWNER somente da adaptação de papel Claude; não redefine AGENT\_POLICY.

CLM-026 | AGENTS.md | claim implícito/adaptador do Reviewer | disposição: OWNER somente da adaptação de papel Codex; não redefine AGENT\_POLICY.

CLM-027 | README — MODELAGEM CANÔNICA / SRC-MOD-001 | claim: roteador/hierarquia/cadeia de leitura da pasta de modelagem | disposição: OWNER do roteamento e continuidade da modelagem Drive.

CLM-028 | 01-MANIFESTO-DE-FONTES | claim: inventário/proveniência de fontes | disposição: OWNER do registro de proveniência; não cria autoridade da fonte.

CLM-029 | 02-CATALOGO-DE-REGRAS | claim: catálogo rastreável de regras | disposição: OWNER do catálogo; a regra material continua pertencendo à fonte/decisão autorizada.

CLM-030 | 09-REGISTRO-SEMANTICO-CANONICO + SGATEs APPROVED | claim: baseline semântico homologado | disposição: OWNER da baseline/decisões semânticas aprovadas.

CLM-031 | 03-GLOSSARIO-CANONICO v3.1.1 | claim: projeção semântica corrente | disposição: OWNER da projeção terminológica; 09/SGATE prevalece em divergência.

CLM-032 | 04A-MODELO-CONCEITUAL | claim: modelo conceitual vigente | disposição: OWNER do modelo conceitual.

CLM-033 | 04B-MODELO-LOGICO | claim: modelo lógico vigente agnóstico de SGBD | disposição: OWNER do modelo lógico.

CLM-034 | 08-REGISTRO-DE-DECISOES-ARQUITETURAIS — DADOS | claim: decisões internas de arquitetura de dados | disposição: OWNER desse registro decisório.

CLM-035 | 20-CURRENT-STATE-INDEX | claim: estado/linhagem corrente dos artefatos de modelagem | disposição: OWNER somente de estado/linhagem, não de semântica.

CLM-036 | docs/modelagem/PLANO\_CEPRAEA\_Modelo\_Canonico\_FINAL.md | claim: plano normativo da fase de reconstrução no repo | disposição: OWNER do processo/fase; NÃO substitui o modelo corrente do Drive enquanto a promoção AC-029 não existir.

CLM-037 | docs/modelagem/dominio/modelo\_canonico\_dominio.md | claim: futuro produto intelectual principal da fase | estado factual observado: ainda sem consolidação real/sem CTX promovidos | disposição: NÃO ELEGÍVEL para substituir o modelo corrente do Drive neste estado.

CLM-038 | CEPRAEA DATABASE / SRC-OPS-002 | claim: DATABASE / SSOT OPERACIONAL; DB\_DISPONIBILIDADE\_DECLARADA canônica; DB\_PRESENCA SSOT factual | disposição: OWNER dos registros estruturados materializados nos datasets declarados.

CLM-039 | CEPRAEA AGOSTO 2026 / SRC-OPS-001 | claim: fonte operacional principal para agenda/histórico/disponibilidade/interface | disposição: OWNER da superfície operacional e das entradas humanas ainda não materializadas; campos importados da DATABASE são projeções, não nova autoridade.

CLM-040 | Wellness — Configuração e Respostas / SRC-OPS-003 | claim: sistema operacional Wellness | disposição: OWNER das declarações/configuração Wellness brutas no escopo observado.

CLM-041 | MANIFESTO CANÔNICO DE MIGRAÇÃO v1.8 | claim: registro de migração/classificação/linhagem para a nova KB | disposição: OWNER do inventário de migração; não promove autoridade de conteúdo.

CLM-042 | BASE CEPRAEA BEACH PRO — CANÔNICA — v0.1 | claim implícito pela denominação | disposição: OWNER apenas deste mapa derivado, gates e histórico da derivação; não substitui owners upstream enquanto PROPOSED.

Nota de fechamento de inventário: o Manifesto v1.8 registra que 27/27 shortcutDetails.targetId ainda não estão comprovados. Shortcuts são ponteiros e não são considerados owners; seus targets não podem ser promovidos por inferência. Esta limitação permanece no Gate 2 de migração e não é apagada por este mapa.

**40 Estado e Conflitos**

**40.1 Currentness e Linhagem**

CURRENTNESS E LINHAGEM — POLÍTICA PROPOSTA

Estados propostos em DEC-DOC-005:

DRAFT → PROPOSED → REVIEWED → APPROVED → EFFECTIVE → {SUPERSEDED | DEPRECATED | WITHDRAWN}; ARCHIVED preserva histórico.

SEMÂNTICA LOCAL

DRAFT: em elaboração, sem autoridade normativa.

PROPOSED: candidata formal, aguardando revisão/decisão.

REVIEWED: revisão concluída, ainda sem aprovação.

APPROVED: conteúdo aprovado, mas ainda pode depender de data/gate para vigência.

EFFECTIVE: versão vigente e autorizada no seu escopo.

SUPERSEDED: substituída por versão/documento identificado.

DEPRECATED: ainda existente, mas uso novo é desencorajado por decisão explícita; não implica substituto automaticamente.

WITHDRAWN: retirada de vigência sem autoridade para uso corrente.

ARCHIVED: preservada para histórico; não é sinônimo de EFFECTIVE.

CURRENTNESS CHECK proposto antes de EFFECTIVE ou revisão periódica:

1\. confirmar owner e versão;

2\. verificar se há supersedes/superseded\_by;

3\. verificar external source status quando a decisão depender de fonte externa corrente;

4\. verificar conflitos com decisões EFFECTIVE relacionadas;

5\. registrar data e evidência da checagem.

**40.2 Bloqueios e Conflitos**

BLOQUEIOS, CONFLITOS E ESCALAÇÃO

POLÍTICA LOCAL — DEC-AG-001

ASK — falta input humano necessário para escolher entre alternativas materiais ou para executar ação que requer autorização.

STOP — hard constraint, gate, segurança, integridade ou autoridade seria violada ao prosseguir.

UNKNOWN — a evidência disponível não permite afirmar o ponto. O agente pode continuar apenas nas partes independentes da lacuna.

ESCALATE — há conflito entre autoridades, decisão fora da autoridade delegada ou bloqueio que requer owner humano.

CONFLICT RESOLUTION — DEC-DOC-004

1\. identificar os dois claims em conflito;

2\. identificar owner, escopo, status, versão e lineage de cada um;

3\. testar se o conflito é real ou apenas escopos distintos;

4\. aplicar a precedência do mesmo owner quando cabível;

5\. se houver sobreposição entre owners sem precedência decidida, marcar BLOCKING\_CONFLICT;

6\. ESCALATE ao owner humano; não escolher silenciosamente um lado;

7\. registrar decisão de resolução e atualizar lineage/impacted refs.

PROIBIÇÃO

A existência de uma capability de approval/ask em uma ferramenta não resolve semanticamente o conflito. Capability da ferramenta é mecanismo; ASK/STOP/UNKNOWN/ESCALATE é política local.

OWNER COLLISION REGISTER — PRIMEIRO ACHADO

OC-001 — Assunto: vocabulário de domínio.

Existing claimant: Guia de Processos de Engenharia — CEPRAEA Beach Pro → docs/GLOSSARY.md como canonical owner.

Relação com DEC-DOC-003: COMPATÍVEL EM PRINCÍPIO com “um assunto → um owner”; a BASE não redefine o vocabulário. Deve registrar GLOSSARY.md como owner efetivo/proposto somente após validar o estado real do repositório e a autoridade desse guia.

Status: PENDING\_RECONCILIATION; não é conflito resolvido.

REGRA DE SEGURANÇA DA MIGRAÇÃO

Um owner encontrado em documento legado não é automaticamente aceito nem descartado. Deve ser reconciliado contra estado, vigência, escopo, decisões posteriores e realidade do repositório.

RECONCILIAÇÃO DE COLISÕES DE OWNERSHIP — 2026-09-06

C-OWN-001 — Guia de Processos de Engenharia × owner global de vocabulário.

Claim: docs/GLOSSARY.md como proprietário canônico absoluto.

Resultado: FALSO CONFLITO / CLAIM NÃO ELEGÍVEL. O documento não prevalece sobre a classificação corrente; a semântica global de modelagem é governada por 09/SGATEs e projetada em 03 v3.1.1. PRODUCT-DOMAIN-SPEC possui glossário apenas no seu escopo contratual.

C-OWN-002 — PRODUCT-DOMAIN-SPEC × AESDS 01.

Resultado: SEM COLISÃO. O próprio AESDS 01 declara que não recria o Modelo Canônico e deve ser usado como regra de consumo/execução, nunca como substituto da fonte canônica. PD-001 permanece owner.

C-OWN-003 — AGENT\_POLICY/.ai × AESDS 07/09/10/11.

Resultado: COLISÃO OPERACIONAL RESOLVIDA. A política atual do repositório e o control plane executável governam papéis, estados, runbooks, contratos, evidência e enforcement. AESDS 07/09/10/11 ficam como referência/arquitetura durante a migração; não podem redefinir estados ou paths operacionais.

C-OWN-004 — Normas × guia Markdown do repositório.

Resultado: SOBREPOSIÇÃO HIERÁRQUICA, não colisão. Normas governa política documental geral; docs/linters/guia\_estilo\_documentação.md especializa autoria/validação de .md no repo e permanece subordinado à política/regras superiores.

C-OWN-005 — Modelagem Canônica Drive × docs/modelagem do repositório.

Resultado: ESCOPO/ESTÁGIO DIFERENTE. O Drive mantém baseline/modelos aprovados correntes (09/03/04A/04B). O repo contém a fase de reconstrução; o próprio modelo\_canonico\_dominio.md informa que ainda não há consolidação real nem CTX promovidos. Logo o repo não substitui factualmente o modelo Drive neste estado.

C-OWN-006 — CEPRAEA DATABASE × CEPRAEA AGOSTO 2026.

Resultado DE OWNERSHIP: RESOLVIDO POR PAPEL. DATABASE é registro estruturado/SSOT materializado; AGOSTO é frontend operacional, histórico e superfície de entrada/apresentação. As abas \_IMPORT\_DATABASE e \_IMPORT\_AGENDA\_DB observadas usam IMPORTRANGE da DATABASE, provando derivação para os campos importados.

Finding de currentness separado: DB\_DISPONIBILIDADE\_DECLARADA não possui 2026\_09 no intervalo inspecionado, mas SETEMBRO - 2026 contém declarações manuais atuais. Isso não cria segundo SSOT canônico; cria drift de materialização a ser tratado em G-DER-05.

C-OWN-007 — Propostas DEC-DOC/DEC-AG desta BASE × owners já existentes.

Resultado: BASE NÃO PROMOVE DUPLICATAS.

\- DEC-DOC-001: NARROW\_TO\_DERIVED\_CANDIDATE; metadados universais pertencem a Normas/CATE.

\- DEC-DOC-002: NARROW\_TO\_REPOSITORY\_IMPLEMENTATION\_PROPOSAL; front matter não ganha autoridade global por esta BASE.

\- DEC-DOC-003: DERIVED\_ALIAS / DO\_NOT\_PROMOTE; autoridade por assunto já é governada por Normas e políticas específicas.

\- DEC-DOC-004: DERIVED\_ALIAS / DO\_NOT\_PROMOTE como política global; conflitos/change control já possuem owners.

\- DEC-DOC-005: CONTRADITO PELA EVIDÊNCIA como state machine documental universal; não promover. Normas possui estados documentais e o SDLC agentivo possui estados externos fechados distintos.

\- DEC-DOC-006: DERIVED\_VALIDATION\_CHECKLIST; não cria novo owner de qualidade.

\- DEC-DOC-007: DERIVED\_VALIDATION\_CHECKLIST; não substitui fontes/SSOTs nem protocolos executáveis.

\- DEC-AG-001: CONTRADITO PELA EVIDÊNCIA se tratado como ontologia operacional comum. ASK/STOP/UNKNOWN/ESCALATE pode existir apenas como vocabulário auxiliar; estados externos operacionais são os definidos em AGENT\_POLICY/control plane.

\- DEC-AG-002: NARROW\_TO\_DERIVED\_AUDIT\_PROFILE; não substitui o evidence model/control plane vigente.

C-OWN-008 — shortcuts não resolvidos do Manifesto v1.8.

Resultado: NÃO PROMOVIDOS. Shortcut é ponteiro, não conteúdo autoritativo. Targets sem targetId comprovado não recebem owner status por inferência. O Gate 2 global da migração continua bloqueado e é independente do G-DER-04 semântico desta BASE.

C-OWN-009 — PRODUCT-DOMAIN-SPEC glossary × 03-GLOSSARIO-CANONICO.

Resultado: FALSO CONFLITO POR ESCOPO. O glossário do Product Domain Spec governa termos do contrato de produto; 03 é a projeção terminológica da cadeia de modelagem, subordinada à baseline 09/SGATEs.

**80 Testes de Recuperação**

**80.1 Casos RT-001..016**

CASOS DE TESTE DE RECUPERAÇÃO — WAVE DE DERIVAÇÃO

RT-001 — Pergunta: “Quem define os estados documentais?” Esperado: recuperar DEC-DOC-005 / 00.2 e 40.1; não recuperar W3C/IETF state models como regra CEPRAEA.

RT-002 — Pergunta: “YAML front matter é obrigatório por um standard?” Esperado: responder NÃO; recuperar E056/E057 e DEC-DOC-002, distinguindo exemplo/tool-specific de decisão local.

RT-003 — Pergunta: “Qual documento vence um conflito?” Esperado: recuperar DEC-DOC-003/004 e resolver primeiro por assunto/owner; não aplicar hierarquia global inventada.

RT-004 — Pergunta: “O código atual contradiz o requisito; qual é a verdade?” Esperado: recuperar DEC-DOC-007; separar factual current-state de normative desired-state e registrar conflito.

RT-005 — Pergunta: “Claude Code pode usar a política do Codex?” Esperado: recuperar I-ED-004 e DEC-AG-001; capability não pode ser generalizada.

RT-006 — Pergunta: “Precisamos guardar chain-of-thought para auditoria?” Esperado: recuperar DEC-AG-002; audit trail usa eventos observáveis e não exige hidden reasoning.

RT-007 — Pergunta sobre Q-QL-01 unambiguity como fato plenamente externo. Esperado: manter PARCIALMENTE\_FUNDAMENTADA; não promover por inferência.

RT-008 — Pergunta sobre Q-MC-02. Esperado: preservar status parcial e historical directed trace; não inventar GAP-ID.

RT-009 — Pergunta sobre vigência de documento APPROVED. Esperado: APPROVED ≠ EFFECTIVE.

RT-010 — Pergunta sobre documento SUPERSEDED. Esperado: seguir lineage para replacement EFFECTIVE e preservar histórico.

RT-011 — Pergunta sem owner identificável. Esperado: UNKNOWN, não escolher arquivo similar.

RT-012 — Dois owners EFFECTIVE com overlap real. Esperado: BLOCKING\_CONFLICT + ESCALATE.

RT-013 — Claim externo sem EVIDENCE-ID. Esperado: falhar G-DER-01 para promoção.

RT-014 — Escolha local atribuída a ISO/DCMI sem base. Esperado: falhar G-DER-02/03.

RT-015 — Documento derivado tenta sobrescrever owner. Esperado: rejeitar por P-04.

RT-016 — Pedido para marcar esta BASE EFFECTIVE sem aprovação humana. Esperado: bloquear em G-DER-06.

**80.2 Resultados e Evidências**

RESULTADOS DOS TESTES DE RECUPERAÇÃO

STATUS: NOT EXECUTED.

Nenhum RT-001..016 é marcado PASS nesta fase porque os casos foram apenas definidos. Os resultados devem ser preenchidos somente após execução observável contra o mecanismo real de recuperação/context delivery que será usado por humanos/Codex/Claude Code.

Campos de resultado exigidos: TEST-ID; executor; data; query/input; contexto efetivamente recuperado; owner esperado; owner recuperado; decision/evidence refs recuperadas; resultado PASS/FAIL; desvio; evidência da execução.

G-DER-05 — EXECUÇÃO DE VALIDAÇÃO DO OWNER-MAP v0.1 — 2026-09-06

V-OWN-001 — STRUCTURAL / completude do registro.

Método: inspeção do mapa derivado e inventário de claims.

Critério: cada SUBJECT-ID deve possuir assunto delimitado, owner resolvido e relação de precedência/delegação quando aplicável.

Resultado: PASS.

V-OWN-002 — STRUCTURAL / unicidade.

Método: comparação por SUBJECT-ID e escopo/effectivity.

Critério: zero SUBJECT-ID com dois owners concorrentes no mesmo escopo.

Resultado: PASS.

V-OWN-003 — SEMANTIC / elegibilidade por estado.

Método: confrontar claims com classificação do Manifesto v1.8 e documentos-fonte.

Critério: histórico, backup, rascunho, conteúdo derivado e shortcut sem target comprovado não podem vencer owner vigente.

Resultado: PASS.

V-OWN-004 — SEMANTIC / delegação e precedência.

Casos verificados: Normas→CATE; Normas/AGENT\_POLICY→guia Markdown; PRODUCT-DOMAIN-SPEC→TRAINING\_FLOW\_CONTRACT/AESDS 01; AGENT\_POLICY→.ai/control/adapters; 09/SGATE→03→04A/04B.

Critério: especialização/adaptação não amplia autoridade do owner pai.

Resultado: PASS.

V-OWN-005 — FACTUAL-CURRENT-STATE / control plane do repositório.

Evidência observada: main contém AGENT\_POLICY, .ai/control, .ai/decisions, .ai/tasks e manifest.json; runbook-catalog resolve operation\_class; control-plane é declarado fonte única dos modos.

Resultado: PASS no escopo agentivo.

V-OWN-006 — FACTUAL-CURRENT-STATE / modelagem repo versus Drive.

Evidência observada: docs/modelagem/dominio/modelo\_canonico\_dominio.md declara ausência de consolidação real e bounded\_contexts.md declara nenhum Bounded Context promovido; a Modelagem Drive registra 09/03/04A/04B correntes/aprovados.

Resultado: PASS para a resolução de owner: Drive permanece current model owner; repo permanece owner do processo de reconstrução.

V-OWN-007 — FACTUAL-CURRENT-STATE / linhagem operacional DATABASE→AGOSTO.

Evidência observada: \_IMPORT\_DATABASE usa IMPORTRANGE de DB\_EXPORT\_FRONTEND; \_IMPORT\_AGENDA\_DB usa IMPORTRANGE de DB\_EXPORT\_AGENDA. DB\_CONFIG declara DATABASE/SSOT OPERACIONAL, DB\_DISPONIBILIDADE\_DECLARADA como canonical\_availability\_sheet e DB\_PRESENCA como canonical\_factual\_presence\_sheet.

Resultado de ownership: PASS.

Resultado de currentness: FAIL. Busca limitada a DB\_DISPONIBILIDADE\_DECLARADA!A1:M1000 encontrou zero registro 2026\_09; inspeção de SETEMBRO - 2026 mostra declarações manuais atuais SIM/NAO/TALVEZ. Portanto, o SSOT materializado de disponibilidade está atrasado em relação à captura de setembro.

V-OWN-008 — SEMANTIC / colisões criadas pela própria BASE.

Método: comparar DEC-DOC-001..007 e DEC-AG-001..002 com owners atuais.

Resultado: PASS após disposição explícita DO\_NOT\_PROMOTE/NARROW/DERIVED para propostas que duplicavam ou contradiziam owners existentes.

CONCLUSÃO G-DER-05

EXECUTED — FAIL.

Motivo bloqueante observado: currentness de disponibilidade declarada de setembro não está materializada no dataset canônico DB\_DISPONIBILIDADE\_DECLARADA no intervalo verificado.

Classificação da validação: SUSTENTADO PARCIALMENTE — estrutura, unicidade, delegação, agent control plane e model owner foram validados; currentness operacional de disponibilidade falhou.

Este resultado NÃO altera os RT-001..016, que permanecem NOT EXECUTED. Também NÃO fecha o Gate 2 do Manifesto v1.8 relativo a shortcutDetails.targetId.

**90 Histórico Auditável**

**90.1 Histórico da Migração**

HISTÓRICO DA DERIVAÇÃO

MIG-001 — 2026-09-06 — CORPUS CANÔNICO → BASE DOCUMENTAL DERIVADA

ORIGEM: Pesquisa CEPRAEA BEACH PRO — CANONICAL v1.0; RESEARCH STATUS DONE; blocking NC = 0.

AÇÃO: consumidas as nove questões classificadas como DECISÃO\_DO\_PROJETO\_NECESSÁRIA e materializada uma primeira camada de decisões locais PROPOSED.

DECISIONS CREATED: DEC-DOC-001..007; DEC-AG-001..002.

PRESERVAÇÃO: SOURCE-ID/EVIDENCE-ID permanecem no documento de pesquisa; esta BASE referencia, não reescreve, o corpus.

QUESTÕES PARCIAIS PRESERVADAS: Q-SE-02, Q-TR-01, Q-QL-01, Q-DR-01, Q-DR-02, Q-MC-02, Q-AG-01.

GATE: G-DER-01..03 PASS; G-DER-04 PROPOSED; G-DER-05 NOT EXECUTED; G-DER-06 NOT EXECUTED; G-DER-07 BLOCKED.

RESULTADO: documentação derivada criada sem declarar as decisões EFFECTIVE.

MIG-002 — 2026-09-06 — OWNER-COLLISION SCAN INICIAL

Busca dirigida no Drive encontrou claim pré-existente de canonical ownership para vocabulário: docs/GLOSSARY.md no Guia de Processos de Engenharia. Também foram observados claims canônicos específicos em outros domínios.

Efeito: G-DER-04 reclassificado operacionalmente para BLOCKED\_PENDING\_RECONCILIATION. Nenhum owner legado foi automaticamente promovido ou sobrescrito.

2026-09-06 — WAVE OWNER-RECONCILIATION / G-DER-04 / G-DER-05

1\. Inventariados claims explícitos de ownership/SSOT/canonicalidade no Manifesto v1.8, fontes Drive atuais e main do repositório.

2\. Separados ativos normativos atuais de histórico, backup, derived/reference, rascunho e shortcuts não comprovados.

3\. Construído OWNER-MAP v0.1 por assunto atômico.

4\. Reconciliadas colisões: GLOSSARY histórico, ProductDomain×AESDS, agent policy×AESDS, Normas×guia Markdown, Drive model×repo rebuild, DATABASE×AGOSTO e propostas da própria BASE.

5\. G-DER-04 promovido a PASS no escopo explicitamente auditado.

6\. G-DER-05 executado com checks V-OWN-001..008.

7\. Finding factual: disponibilidade de setembro observada em CEPRAEA AGOSTO 2026 não foi encontrada em DB\_DISPONIBILIDADE\_DECLARADA!A1:M1000; G-DER-05 = FAIL.

8\. G-DER-06 permanece NOT EXECUTED; G-DER-07 permanece BLOCKED.

9\. Nenhuma fonte foi excluída, nenhum shortcut foi promovido e nenhum RT-001..016 foi marcado PASS.

**90.2 Atalhos e Targets Descobertos**

ATALHOS E TARGETS DESCOBERTOS

EVIDENCE OWNER

Pesquisa CEPRAEA BEACH PRO

https://docs.google.com/document/d/1vjPQZNRjRlnd2yodz6DNNajnKyjDlVCblyuLdnsW87k

Papel: proprietário de SOURCE-ID, EVIDENCE-ID, search provenance, appraisal, coverage e limitações da revisão.

DERIVED DOCUMENTATION TARGET

BASE CEPRAEA BEACH PRO — CANÔNICA — v0.1

https://docs.google.com/document/d/1xUuZwffsJx4x4bSbCAXGV2ALdYGeB7WZDS15LBr8fsU

Papel: camada derivada de interpretação, decisões locais, roteamento, gates e testes. Estado atual: PROPOSED.

REGRA: não criar um terceiro documento concorrente para redefinir as mesmas decisões sem primeiro estabelecer explicitamente novo owner/supersession.