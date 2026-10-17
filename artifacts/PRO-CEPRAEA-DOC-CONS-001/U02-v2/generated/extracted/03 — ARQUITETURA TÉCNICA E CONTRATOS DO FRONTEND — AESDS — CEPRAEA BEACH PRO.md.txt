# ARQUITETURA TÉCNICA E CONTRATOS DO FRONTEND — CEPRAEA BEACH PRO

AESDS 03 — Fundação v0.1

1. OBJETIVO

Definir como o frontend é implementado tecnicamente sem permitir que cada agente reinvente arquitetura, contratos ou padrões a cada tarefa.

2. ESTADO TÉCNICO DE REFERÊNCIA

No estado atualmente documentado do repositório de fundação: React 19 + TypeScript + Vite; integração prevista com Supabase PostgreSQL/Auth/Data API/RLS; PWA estática e online; service worker mínimo; sem cache offline de dados; Vitest, Testing Library e Oxlint; dados sintéticos durante a fundação.

Esse bloco é snapshot técnico e deve ser confrontado com o repositório antes de tarefas que dependam dele.

3. PRINCÍPIOS DE ARQUITETURA

- domínio e backend são autoridades das regras críticas;

- frontend representa, orienta e valida para experiência, sem substituir enforcement;

- contratos são reutilizados ou gerados da fonte quando possível;

- evitar segundo dicionário manual de campos;

- uma fonte de verdade por informação;

- derived state em vez de duplicação quando seguro;

- efeitos somente para sincronização externa quando render/handler determinístico resolve;

- estados impossíveis devem ser difíceis de representar por tipos;

- dependências novas exigem decisão humana quando alteram arquitetura, bundle, segurança, manutenção ou lock-in.

4. CAMADAS CONCEITUAIS

App Shell/Routes: navegação e composição global.

Feature/Vertical Slice: unidade funcional orientada à tarefa.

UI/Design System: primitivos e componentes reutilizáveis.

Domain Presentation: view models e adaptação semântica, sem redefinir domínio.

Data Access: chamadas tipadas e tratamento de resultados.

Contracts: tipos, schemas, comandos, respostas e erros.

A estrutura física exata deve ser validada contra o repositório e decidida uma vez; agentes não devem criar arquiteturas paralelas.

5. CONTRATOS DE DADOS

Fonte preferida: artefatos executáveis existentes no repositório, incluindo tipos, schemas, migrations e contratos de API. Google Drive funciona como documentação/registro, não como substituto de contrato executável.

Para cada operação, documentar quando aplicável:

input -> validação de apresentação -> command/request -> resposta -> erros possíveis -> atualização de estado -> feedback UI.

6. FORMULÁRIOS

Campos derivam de contrato/domínio. O frontend pode adicionar metadados puramente de apresentação, mas não deve inventar campo persistido. Validação do cliente melhora feedback; servidor continua autoridade.

7. NULLABILITY E ESTADOS

TypeScript strict deve tratar ausência e nulabilidade explicitamente. Não usar valores mágicos para representar ausência, erro ou não respondida quando o contrato possui estado próprio.

8. ERROS

Erros devem ser classificados no ponto de integração sem perder causa técnica para observabilidade nem expor detalhe indevido ao usuário. A UI recebe um estado compreensível e recuperável quando possível.

9. AUTORIZAÇÃO

Esconder ou desabilitar ação é UX. Autorização real permanece no backend/RLS. Testes devem cobrir tentativa não autorizada, não apenas ausência do botão.

10. PWA E CONECTIVIDADE

Não assumir offline-first ou persistência offline de dados enquanto isso não estiver autorizado e implementado. A interface deve representar perda/retorno de conexão sem afirmar que uma gravação inexistente foi concluída.

11. PERFORMANCE

Medir antes de otimizar. Memoização, virtualização, code splitting adicional ou outras técnicas devem ser introduzidas por evidência ou necessidade arquitetural, não ritual.

12. DEPENDÊNCIAS

Antes de adicionar dependência material, o agente deve apresentar: problema resolvido, alternativas, manutenção, licença, tamanho/impacto, segurança, compatibilidade, custo de remoção e recomendação. Se a necessidade puder ser resolvida com stack existente de forma simples, preferir não expandir.

13. PADRÃO DE IMPLEMENTAÇÃO

Cada feature relevante deve ser uma vertical slice concluída ponta a ponta: contrato -> acesso -> estado -> UI -> erros -> testes -> validação mobile. Evitar construir todas as telas vazias antes de validar um fluxo completo.

14. CHECKS DE APLICAÇÃO

A validação da aplicação deve reutilizar os comandos já definidos no repositório, atualmente incluindo a intenção de lint, typecheck, testes e build. Não criar gate documental novo para uma feature comum.

15. STOP CONDITIONS

Parar se a implementação exigir arquitetura não definida, nova dependência material, alteração de contrato não prevista, mudança de autorização, segredo no cliente, comportamento offline não autorizado ou duplicação de fonte de verdade.

16. DONE TÉCNICO

Uma slice técnica só está pronta quando contratos estão coerentes, TypeScript/checks aplicáveis passam, erros e autorização estão cobertos proporcionalmente ao risco, não há estado impossível conhecido e o comportamento foi comprovado pelos critérios da tarefa.

17. BASELINE TÉCNICA DO MVP — PLANOS / SPECS

Esta seção define fronteiras técnicas lógicas necessárias para tornar os fluxos MVP implementáveis sem antecipar nomes de tabelas, endpoints, arquivos, migrations ou estrutura física ainda não verificados.

17.1. AUTORIDADE E FRONTEIRA FÍSICA

- regras críticas de domínio e autorização permanecem na camada autoritativa; o frontend não promove validação de apresentação a enforcement;

- contratos executáveis do repositório, quando existentes e compatíveis com decisões canônicas, são a fonte preferida para tipos/schemas/API;

- o gate físico de dados está vigente e bloqueia alterações de modelo físico, SQL, schema e migrations; este documento não libera DEL-10 para execução física;

- qualquer snapshot de stack ou estrutura deve ser confrontado com o repositório real antes de originar tarefa executável.

17.2. CONTRATOS LÓGICOS POR CAPACIDADE

C-ID — Identidade e vínculo.

Entrada lógica: identidade/contexto autorizado suficiente para resolver a atleta de domínio e o vínculo aplicável.

Saída lógica: atleta de domínio + vínculo temporal relevante + capacidades autorizadas para o contexto.

Invariantes: atleta != auth.user; cadastro != vínculo; existência do dado != permissão.

Falhas mínimas: identidade de domínio não resolvida; vínculo ausente/incompatível; não autorizado; contrato inconsistente.

C-SESSION — Sessão/treino.

Entrada lógica: referência de sessão + contexto autorizado.

Saída lógica: sessão com estado temporal necessário ao fluxo, preservando distinção entre planejado e realizado.

Invariantes: passagem de tempo não cria realização factual; presença factual exige sessão realizada quando o contrato canônico assim exigir.

Falhas mínimas: sessão inexistente/inacessível; estado temporal inconsistente; contrato stale/incompatível.

C-AVAIL — Disponibilidade.

Consulta: sessão/solicitação aplicável + atleta autorizada -> resposta corrente derivada do histórico válido, incluindo NÃO_RESPONDIDA quando não existe resposta, + `deadline_at` explícito + condição temporal da coleta (aberta/fechada por prazo/reaberta de forma autorizada).

Comando lógico: atleta autorizada + solicitação aplicável + opção canônica + coleta aberta dentro do prazo, ou reabertura autorizada ainda anterior ao início da sessão -> confirmação autoritativa ou erro tipado. O comando normal deve rejeitar escrita após fechamento do self-service.

Invariantes: resposta é explícita; histórico/versionamento é preservado; corrente deriva da versão vigente; NÃO_RESPONDIDA != NÃO; disponibilidade não cria presença; toda solicitação possui `deadline_at` explícito; não existe default temporal global; `deadline_at` não pode ultrapassar o início planejado da sessão; chegada do deadline fecha a janela normal de edição sem apagar nem “expirar” semanticamente a declaração corrente; reabertura antes do início da sessão exige ato autorizado/auditável; após o início não há reabertura normal.

Falhas mínimas: não autorizado; solicitação inexistente; `deadline_at` ausente/inválido; tentativa de prazo posterior ao início planejado da sessão; coleta fechada; reabertura não autorizada; sessão já iniciada para tentativa de reabertura normal; conflito/stale; validação de opção.

DECIDED-AVAIL-01 / DEC-DATA-046 fecha o contrato temporal lógico de prazo, fechamento, editabilidade e reabertura. A representação física de timestamp, endpoint, schema e mecanismo de enforcement continua dependente das fontes executáveis do repositório e do gate físico aplicável; nenhuma implementação pode criar default temporal concorrente.

C-COVERAGE — Cobertura e planejamento.

Entrada lógica: sessão + respostas vigentes autorizadas.

Saída lógica: cobertura derivada e, quando houver contrato aprovado, representação de participação planejada.

Invariantes: derivação != fato; lista prevista != presença; mudança de fonte pode recomputar derivação sem reescrever fatos históricos.

DECIDED-PLAN-01 / DEC-DATA-047 define o contrato lógico do Plano de Participação da Sessão: objeto PLANO humano/versionado, com projeção “lista prevista” derivada da única versão PUBLISHED vigente; lifecycle DRAFT -> PUBLISHED -> SUPERSEDED | CANCELLED | CLOSED; PUBLISHED imutável; revisão/revalidação material cria nova versão; `SOURCE_ALIGNMENT = CONSISTENT | REVIEW_REQUIRED` é eixo ortogonal; mudança material dos inputs pode recomputar derivações e exige revisão, mas nunca reescreve automaticamente a composição humana. Operações lógicas aplicáveis incluem criar draft, publicar versão, revisar/revalidar via nova versão, cancelar e encerrar por ator autorizado; nomes de endpoint, storage e representação física dependem do grounding do repositório e permanecem fora desta decisão. BLOCKED-DATA-01 continua proibindo SQL/schema/migration/RLS física.

C-ATTEND — Presença factual.

Entrada de comando lógico: sessão realizada + atleta + extensão factual FULL/PARTIAL/NONE + principal/autoridade autorizada + proveniência exigida.

Saída lógica: fato confirmado pela camada autoritativa ou erro tipado; ausência de fato permanece distinta de NONE.

Invariantes: FULL/PARTIAL/NONE descrevem extensão factual, não justificativa; disponibilidade/lista/Wellness não viram presença automaticamente; PRESENCA_PROPOSTA, quando aplicável, é derivada/transitória e não fato; correções devem preservar auditabilidade/proveniência.

Falhas mínimas: não autorizado; sessão não realizada/incompatível; atleta/contexto inválido; conflito de versão; contrato físico indisponível.

C-WORKSPACE — Projeções operacionais.

Entrada lógica: contratos anteriores autorizados.

Saída lógica: estado corrente + pendências + próxima ação, distinguindo fato, planejamento, derivação e ausência de informação.

Invariantes: workspace/dashboard não cria nova verdade; estados LOADING/EMPTY/ERROR/STALE são condições de entrega e não estados do domínio.

17.3. AUTORIZAÇÃO, PRIVACIDADE E PROVENIÊNCIA

Toda operação deve separar capacidade de visualização na UI da autorização real. Escritas sensíveis exigem rejeição autoritativa quando não autorizadas. Dados sintéticos permanecem obrigatórios na fundação enquanto a autorização vigente não mudar. Proveniência necessária para fatos e correções deve ser preservada pelo contrato executável correspondente.

17.4. PWA E CONECTIVIDADE

Baseline autorizada: experiência online. Perda de conexão pode produzir estado de entrega e retry, mas não autoriza cache offline de dados, fila persistente offline ou confirmação fictícia de escrita. Retorno de conectividade deve reconciliar estado sem promover pendência local a fato.

17.5. PRÉ-CONDIÇÕES PARA CONTRATO EXECUTÁVEL

Antes de transformar C-ID/C-SESSION/C-AVAIL/C-COVERAGE/C-ATTEND/C-WORKSPACE em tipos, schemas, requests, endpoints ou arquivos concretos, o agente de IDE deve inspecionar o repositório e identificar fontes executáveis existentes. Se a implementação exigir criação/alteração física de banco, BLOCKED-DATA-01 permanece aplicável até liberação explícita do gate físico.