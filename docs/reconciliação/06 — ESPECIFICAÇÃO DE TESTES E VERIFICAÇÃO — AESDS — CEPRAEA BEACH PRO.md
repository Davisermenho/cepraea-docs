ESPECIFICAÇÃO DE TESTES E VERIFICAÇÃO — CEPRAEA BEACH PRO

AESDS 06 — Fundação v0.1

1\. OBJETIVO

Transformar critérios de aceitação em provas objetivas. A narrativa do agente nunca substitui um resultado verificável quando existe mecanismo determinístico disponível.

2\. MATRIZ DE PROVA

Para cada critério relevante registrar:

CRITÉRIO -> TIPO DE PROVA -> ARTEFATO/TESTE -> COMANDO -> RESULTADO ESPERADO -> EVIDÊNCIA.

3\. CAMADAS DE VERIFICAÇÃO

Static correctness: TypeScript strict, lint/formatter e validações estruturais.

Unit/domain: funções puras, mapeamentos, validações e estados.

Component/interaction: comportamento observável do componente.

Integration: fronteiras entre frontend e contratos/dados.

Authorization: ação permitida e ação recusada.

E2E/flow: tarefa completa quando custo/risco justificar.

Accessibility: automação + inspeção manual proporcional ao fluxo.

Runtime mobile: viewport, teclado, touch, conectividade, latência.

Human usability: compreensão do estado e conclusão da tarefa em fluxos críticos.

4\. PRINCÍPIO DE TESTE

Testar comportamento e contrato, não detalhes internos sem valor. O teste deve falhar quando o requisito for violado e permanecer estável diante de refatoração que preserve comportamento.

5\. EVIDÊNCIA MÍNIMA DA TASK

\- comandos realmente executados;

\- exit code/resultado;

\- testes relevantes e resultado;

\- limitações conhecidas;

\- itens não executados com motivo;

\- evidência de runtime quando o critério exigir.

6\. PASS / FAIL / BLOCKED

PASS: evidência satisfaz integralmente o critério.

FAIL: evidência demonstra violação ou implementação incompleta.

BLOCKED: prova não pode ser executada por dependência/ambiente/decisão ausente. BLOCKED nunca vira PASS narrativo.

7\. PRIMEIRA REVISÃO E META DE 90%

A taxa de primeira revisão mede a qualidade combinada da especificação + execução do agente.

Taxa = PASS / (PASS + FAIL) x 100.

BLOCKED é acompanhado separadamente.

Meta: >=90% na primeira revisão independente.

DONE: 100% dos CRITICAL/MUST PASS, zero CRITICAL/HIGH aberto e zero BLOCKED obrigatório.

8\. TESTES DE ESTADO

Cobrir transições válidas, transições inválidas e fronteiras temporais. Para estados mutuamente exclusivos, testar contra combinações contraditórias quando o tipo/contrato permitir risco.

9\. TESTES DE ERRO E RECUPERAÇÃO

Quando aplicável:

\- falha de API;

\- timeout/latência;

\- perda de conectividade;

\- dupla submissão;

\- resposta stale;

\- deadline encerrado;

\- autorização insuficiente;

\- erro após preenchimento de formulário;

\- retry.

10\. TESTES DE AUTORIZAÇÃO

Não basta verificar botão oculto. Quando possível, provar que a operação não autorizada é recusada pela camada autoritativa.

11\. TESTES MOBILE

Fluxos críticos devem ser validados em viewport representativo e, antes de serem considerados concluídos para uso real, em dispositivo real quando aplicável: touch, scroll, teclado, safe area, foco, rotação, contraste e feedback.

12\. ACESSIBILIDADE

Automação detecta parte dos problemas. Revisão manual deve cobrir navegação por foco, nome acessível, semântica, contraste, feedback não dependente de cor e ordem de leitura onde aplicável.

13\. PERFORMANCE

Definir hipótese/métrica antes de otimização. Usar profiler/auditoria apropriada e registrar antes/depois quando uma task for explicitamente de performance.

14\. REGRESSÃO

Toda correção de bug com risco razoável de recorrência deve produzir teste que falha antes da correção e passa depois, salvo quando o tipo de defeito não for automatizável de forma proporcional.

15\. PROPORCIONALIDADE

Nem toda task precisa de E2E completo. Escolher a prova mais barata capaz de refutar a implementação errada com confiança suficiente ao risco.

16\. REVIEWER

O reviewer deve desconfiar de testes que apenas reproduzem a implementação. Verificar se o teste corresponde ao critério e se existe caminho relevante não coberto.

17\. DONE DA VERIFICAÇÃO

A verificação está completa quando cada critério obrigatório possui status e evidência, nenhum PASS depende apenas de afirmação do executor e as limitações residuais estão explícitas.

18\. BASELINE DE PROVAS DO MVP — PLANOS / SPECS

Esta seção define obrigações de prova já deriváveis dos contratos do MVP. Comandos, paths e nomes de testes permanecem dependentes do grounding do repositório; não devem ser inventados neste documento.

18.1. INVARIANTES DE DOMÍNIO — PROVAS OBRIGATÓRIAS

PV-DOM-01 — provar que NÃO\_RESPONDIDA não é tratada como NÃO em apresentação, lógica derivada ou persistência.

PV-DOM-02 — provar que disponibilidade não cria presença factual.

PV-DOM-03 — provar que lista prevista/planejamento não cria presença factual.

PV-DOM-04 — provar que ausência de registro de presença não é apresentada como NONE/ausência factual.

PV-DOM-05 — provar que atleta de domínio e identidade de autenticação não são intercambiadas como o mesmo conceito.

PV-DOM-06 — provar que cadastro e vínculo temporal não são tratados como equivalentes.

PV-DOM-07 — provar que planejado e realizado permanecem distinguíveis na sessão.

PV-DOM-08 — provar que derivação/proposta não é apresentada como fato confirmado.

18.2. DISPONIBILIDADE

PV-AVAIL-01 — estado corrente é derivado da resposta vigente e histórico não é silenciosamente sobrescrito.

PV-AVAIL-02 — atleta não consegue editar resposta de outra atleta.

PV-AVAIL-03 — falha de submissão não produz confirmação falsa e mantém recuperação coerente.

PV-AVAIL-04 — dupla submissão/retry não deve gerar resultado contraditório ou confirmação duplicada indevida conforme o contrato executável.

PV-AVAIL-05 — provar que toda solicitação de disponibilidade possui \`deadline\_at\` explícito, sem default temporal global implícito, e que o prazo não pode ser posterior ao início planejado da sessão.

PV-AVAIL-06 — provar que, enquanto a coleta estiver aberta e antes do deadline, a atleta autorizada consegue criar/alterar somente a própria declaração; cada alteração preserva histórico/versão e a última versão válida torna-se corrente.

PV-AVAIL-07 — provar que, no deadline, o self-service normal fecha; NÃO\_RESPONDIDA permanece NÃO\_RESPONDIDA; a última declaração válida permanece corrente; o sistema não converte silêncio em NÃO nem marca a declaração como semanticamente expirada apenas pelo fechamento da coleta.

PV-AVAIL-08 — provar que reabertura antes do início da sessão exige ator autorizado e evento auditável; alteração de deadline preserva prazo anterior, ator, momento/proveniência e é rejeitada quando não autorizada.

PV-AVAIL-09 — provar que, após o início da sessão, não existe reabertura normal da coleta; retificações posteriores autorizadas permanecem históricas/auditáveis e não criam nem alteram presença factual por inferência.

PV-AVAIL-10 — provar que a interface apresenta o prazo absoluto e o estado de coleta de forma compreensível no contexto America/Sao\_Paulo, incluindo o estado “prazo encerrado” junto da resposta corrente ou de “não respondida”.

18.3. COBERTURA E PLANEJAMENTO

PV-PLAN-01 — cobertura deriva somente de fontes vigentes autorizadas e não é persistida/apresentada como fato quando for derivação.

PV-PLAN-02 — mudança de resposta vigente altera a derivação esperada sem converter histórico anterior em erro factual.

PV-PLAN-03 — provar que, por sessão, existe no máximo uma versão PUBLISHED vigente do Plano de Participação e que DRAFT não é projetado à atleta como composição decidida.

PV-PLAN-04 — provar que PUBLISHED é imutável e que publicar nova versão supersede atomicamente a anterior, preservando versão/histórico/proveniência da predecessora.

PV-PLAN-05 — provar que revisão material de composição cria nova versão; não existe edição in-place silenciosa da versão publicada.

PV-PLAN-06 — provar que mudança material em input autorizado pode recomputar cobertura/derivação e muda SOURCE\_ALIGNMENT para REVIEW\_REQUIRED sem alterar automaticamente a composição da última decisão humana vigente.

PV-PLAN-07 — provar que revisão após mudança material dos inputs, mesmo mantendo composição idêntica, produz nova versão PUBLISHED com proveniência atualizada e supersede a anterior.

PV-PLAN-08 — provar que CANCELLED exige evento autoritativo explícito, ausência de sucessora não equivale a cancelamento e CLOSED exige marco autoritativo da sessão; passagem do relógio isoladamente não cria CLOSED nem participação factual.

PV-PLAN-09 — provar que “lista prevista” é somente projeção da PUBLISHED vigente e que nenhuma transição do plano cria disponibilidade, compromisso da atleta, Convocação ou presença factual.

PV-PLAN-10 — provar que publicação e comunicação/notificação são eventos distintos: publicação torna a versão vigente sem exigir que delivery/comunicação seja modelado como estado obrigatório do lifecycle.

18.4. PRESENÇA FACTUAL

PV-ATT-01 — operação não autorizada de confirmar presença é rejeitada pela camada autoritativa quando o ambiente permitir prova de enforcement.

PV-ATT-02 — disponibilidade, lista prevista e Wellness não confirmam presença automaticamente.

PV-ATT-03 — PRESENCA\_PROPOSTA, quando aplicável, permanece derivada/transitória até confirmação autorizada.

PV-ATT-04 — FULL/PARTIAL/NONE representam extensão factual e não são usados para codificar justificativa clínica, atraso ou outro significado não canônico.

PV-ATT-05 — ausência de Wellness ou ausência de registro não gera ausência factual.

PV-ATT-06 — correção de presença preserva a auditabilidade/proveniência exigida pelo contrato autoritativo.

18.5. AUTORIZAÇÃO, PRIVACIDADE E PROVENIÊNCIA

PV-AUTH-01 — esconder/desabilitar controle na UI não é a única prova; tentativa não autorizada deve ser rejeitada pela autoridade quando testável.

PV-AUTH-02 — ator só acessa dados/ações permitidos para seu contexto.

PV-PRIV-01 — dados sintéticos são usados nos cenários de fundação enquanto a autorização vigente não mudar.

PV-PROV-01 — fatos/correções que exigem origem, autoridade ou timestamp preservam esses elementos no contrato executável e na evidência correspondente.

18.6. PWA, ERRO E CONECTIVIDADE

PV-PWA-01 — perda de conexão é apresentada como condição de entrega e não como sucesso de escrita.

PV-PWA-02 — não existe persistência/cache offline de dados ou fila offline como comportamento implícito sem decisão/autorização.

PV-PWA-03 — retorno de conectividade reconcilia estado pendente sem promover estado local a fato antes da confirmação autoritativa.

PV-ERR-01 — loading, empty, error, unavailable e stale não são confundidos com estados de domínio.

18.7. MOBILE E ACESSIBILIDADE

PV-MOB-01 — fluxos críticos devem ser verificados em viewport mobile representativo e, antes de uso real quando aplicável, em dispositivo real.

PV-MOB-02 — touch, teclado, foco, scroll, safe area e feedback durante pendência/erro devem ser observáveis.

PV-A11Y-01 — semântica, nome acessível, foco, ordem de leitura pertinente, contraste e feedback não dependente apenas de cor são requisitos de prova já válidos.

PV-A11Y-02 — a prova de conformidade a um nível formal WCAG permanece BLOCKED enquanto OPEN-A11Y-01 estiver OPEN.

18.8. MIGRAÇÃO E CUTOVER

PV-CUT-01 — não pode existir dual SSOT operacional concorrente para o mesmo fato durante promoção final.

PV-CUT-02 — cada transformação migratória deve conservar proveniência e permitir reconciliação conforme o mapping homologado.

PV-CUT-03 — validação de destino físico permanece BLOCKED enquanto BLOCKED-DATA-01 impedir o modelo físico final.

18.9. MATRIZ DE PROVA CONCRETA

Após grounding do repositório, cada PV-\* aplicável deve ser ligado a: critério da task -> tipo de prova -> arquivo/teste real -> comando real -> resultado esperado -> evidência. OPEN-REPO-01 impede preencher comandos ou paths por inferência; não impede especificar a obrigação de prova.