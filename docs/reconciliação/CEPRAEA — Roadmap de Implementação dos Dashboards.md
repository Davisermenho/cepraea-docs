Roadmap de Implementação dos Dashboards

CEPRAEA — Roadmap de Implementação dos Dashboards

Versão 2.3 — 25/08/2026

## NORTE DO ROADMAP

Construir e colocar em operação um único aplicativo CEPRAEA, com experiências separadas para ATLETA e TREINADOR, sem dependência de repositório Git. O Vercel será a camada de aplicação e deploy; o Supabase será responsável por autenticação e identidade; as planilhas CEPRAEA permanecerão como fonte operacional durante a transição, acessadas somente por API server-side.

## RESULTADO FINAL ESPERADO

A atleta entra com sua própria conta, vê apenas seus dados, consulta agenda e treinos e declara SIM, NAO ou TALVEZ sem editar planilha. O treinador entra no seu painel, vê agenda, próximo treino, respostas, composição, competições, resultados e qualidade dos dados. A identidade dos dados é baseada em IDs estáveis: evento\_id, athlete\_id e evento\_id + athlete\_id.

## PRINCÍPIOS NÃO NEGOCIÁVEIS

-   Uma única aplicação com autorização por perfil.
-   athlete\_id nunca é escolhido pelo frontend; é resolvido no servidor pela sessão autenticada.
-   Nenhum segredo do Google ou do Supabase é enviado ao navegador.
-   O frontend não depende de posição de linha/coluna.
-   Eventos usam evento\_id; atletas usam athlete\_id; disponibilidade usa evento\_id + athlete\_id.
-   Dados individuais sensíveis de Wellness e questionários não são expostos no painel da atleta por padrão.
-   Novas telas usam “treinador” no singular.
-   Nenhuma versão vai para produção sem gate de validação, backup e rollback.
-   Sem Git, cada release é versionada e arquivada no Google Drive.
-   Disponibilidade declarada e presença factual são conceitos separados; nenhuma disponibilidade comprova presença.
-   A projeção atual de disponibilidade nunca apaga o histórico de versões.
-   Convocação para competição não equivale a participação em cada jogo.
-   Ausência de dado ou SEM\_RESPOSTA nunca é convertida automaticamente em NAO.
-   Status do evento e status de publicação do conteúdo são dimensões independentes.

# CONTRATOS EXPLÍCITOS DE NEGÓCIO E COMPORTAMENTO

## Regra de interpretação

Os contratos abaixo são normativos para produto, API, migração, testes e interfaces. Eles registram comportamentos já existentes nas planilhas CEPRAEA para que deixem de depender de conhecimento implícito. Quando duas fontes divergirem, o aplicativo não deve escolher silenciosamente uma interpretação: deve aplicar a precedência documentada quando houver e, caso contrário, sinalizar qualidade de dados e bloquear inferências destrutivas.

## A. CEPRAEA DATABASE — contrato canônico

-   \- CNTR-DB-001 — Fonte canônica e precedência: a DATABASE é a fonte operacional canônica durante a transição. Entrada manual válida deve ser preservada; export, fórmula, cache ou rotina derivada não pode sobrescrevê-la sem regra explícita e rastreável.
-   \- CNTR-DB-002 — Identidade: atleta, evento, treino, competição, jogo, convocação e adversário devem possuir identidade estável independente de posição física em planilha.
-   \- CNTR-DB-003 — Disponibilidade não é presença: SIM, NAO, TALVEZ e SEM\_RESPOSTA são declarações anteriores ao evento e nunca comprovam presença ou ausência factual.
-   \- CNTR-DB-004 — Presença factual: presença integral, ausência factual, falta justificada ou participação parcial pertencem a fluxo próprio, posterior ao início da sessão. Nenhum cálculo, trigger ou tela pode converter disponibilidade em presença automaticamente.
-   \- CNTR-DB-005 — Sem resposta não é NÃO: célula vazia, ausência de registro ou SEM\_RESPOSTA não pode ser normalizada para NAO.
-   \- CNTR-DB-006 — Ciclo de vida do treino: PLANEJADO, CONFIRMADO quando aplicável, REALIZADO, CANCELADO e ENCERRADO\_SEM\_CONFIRMACAO são estados semanticamente distintos. Treino passado não vira REALIZADO apenas pela passagem do tempo.
-   \- CNTR-DB-007 — Estado do evento não é estado de publicação: um treino pode existir e aceitar disponibilidade mesmo com objetivo, metas ou atividade ainda não publicados. Conteúdo interno pendente nunca deve aparecer literalmente para a atleta.
-   \- CNTR-DB-008 — Participação do CEPRAEA: competição preservada por histórico/auditoria pode permanecer na base mesmo quando o CEPRAEA não participar; nesse caso não entra na agenda normal da atleta nem gera ação de disponibilidade sem regra específica.
-   \- CNTR-DB-009 — Aviso vazio é válido: ausência de aviso em DB\_AVISOS ou estrutura equivalente significa que não existe aviso a publicar; o aplicativo não fabrica alerta para preencher espaço.
-   \- CNTR-DB-010 — Função INDEFINIDA é válida: composição e filtros devem suportar atleta sem função tática definida, sem forçar classificação artificial.
-   \- CNTR-DB-011 — Convocação não é participação em jogo: convocação para competição, inclusão nominal na convocação e participação efetiva em cada jogo são fatos distintos e devem permanecer separados em dados, API e métricas.
-   \- CNTR-DB-012 — Estrutura tática: sistemas, posições táticas, posições secundárias e disponibilidade por posição devem ser preservados como domínio próprio. A contagem Goleira/Defesa/Ataque é uma visão resumida, não o modelo completo.
-   \- CNTR-DB-013 — Cobertura tática: quando houver dados suficientes, o treinador pode consultar cobertura/insuficiência por sistema e posição; ausência de dados não autoriza o aplicativo a presumir cobertura.
-   \- CNTR-DB-014 — Disponibilidade versionada: cada alteração de resposta cria uma nova versão imutável. O par evento\_id + athlete\_id mantém uma projeção atual para consulta rápida, mas versões anteriores não são apagadas nem reescritas.
-   \- CNTR-DB-015 — Proveniência e idempotência: cada versão de disponibilidade registra momento, origem controlada, ator quando aplicável e chave de idempotência; reenvio da mesma operação não cria versão duplicada.
-   \- CNTR-DB-016 — Resultado de jogo: jogo concluído deve possuir segmentos suficientes e coerentes para sustentar o vencedor final. Resultado incompleto é qualidade de dados, não autorização para inferir placares.
-   \- CNTR-DB-017 — Adversário estável: adversário deve ser tratado como entidade identificável; variações textuais de nome não devem criar automaticamente adversários diferentes.
-   \- CNTR-DB-018 — Preservação histórica: registros migrados mantêm referência à fonte legada; correções não apagam o caminho de origem.

## B. CEPRAEA AGOSTO 2026 — contrato operacional e de transição

-   \- CNTR-AGO-001 — Agenda operacional: competição/evento pode possuir prazo de inscrição, prazo de lista nominal, pendência, criticidade, ação necessária e risco de composição. A agenda do treinador deve conseguir representar “o que precisa ser resolvido”, não apenas data e local.
-   \- CNTR-AGO-002 — Planejamento técnico: competição-alvo pode orientar ciclo, foco tático, exercício, indicador, decisão e observação. Esses campos são conteúdo interno do treinador até que exista regra explícita de publicação.
-   \- CNTR-AGO-003 — Matriz mensal após cutover: depois da Fase 8, AGENDA MENSAL/DISPONIBILIDADE antiga é somente leitura, histórico ou contingência. Ela não volta a ser fonte concorrente de escrita enquanto o dashboard for o canal oficial.
-   \- CNTR-AGO-004 — Próximo treino: validade do evento, disponibilidade e publicação do conteúdo são eixos independentes. Placeholder interno, conteúdo pendente ou instrução administrativa não pode ser exposto como plano da atleta.
-   \- CNTR-AGO-005 — Modo Dia do Jogo: competição possui contexto ANTES, DURANTE e DEPOIS. Antes prioriza programação/convocação/reunião; durante prioriza último resultado, próximo jogo, fase e ação; depois prioriza campanha, resultado final, pendências e próximo ciclo.
-   \- CNTR-AGO-006 — Análise por adversário: resultados podem ser agregados por competição e por adversário estável.
-   \- CNTR-AGO-007 — Camada de consumo: telas de produção não consomem diretamente abas visuais/analíticas como ANÁLISE JOGOS; consomem API/export canônico validado.
-   \- CNTR-AGO-008 — Teste de contrato DB→UI: campos críticos de tela devem possuir verificação fonte esperada → valor canônico → payload/API → valor exibido, equivalente ao princípio de \_VALIDACAO\_DB.
-   \- CNTR-AGO-009 — Registries legados: R\_STATUS, R\_FUNCOES, R\_MONTHS, R\_DATES, R\_META e estruturas equivalentes são fontes auxiliares/legadas. Quando houver conflito, prevalece configuração canônica vigente; conflito sem regra de precedência vira alerta de qualidade, não decisão silenciosa.
-   \- CNTR-AGO-010 — Feedback individual: o módulo de agendamento individual é MÓDULO FUTURO CONHECIDO, fora do caminho crítico da V1. Quando reativado, deve controlar slot, reagendamento/cancelamento e histórico de conclusão; somente metadados operacionais podem ser persistidos, não o conteúdo da conversa.

## C. Implementação — Pesquisa de Treinos CEPRAEA 2026

-   \- CNTR-PESQ-001 — Pesquisa de horário é apoio à decisão: slots candidatos, restrições de duração/horário, disponibilidade nominal, composição e compatibilidade tática podem gerar recomendação, mas não alteram automaticamente o calendário.
-   \- CNTR-PESQ-002 — Gate humano: mudança de horário, criação de sessão recorrente ou adoção de slot recomendado exige decisão explícita do treinador.
-   \- CNTR-PESQ-003 — Nominal e anônimo são domínios distintos: pesquisa nominal pode apoiar viabilidade operacional; pesquisa anônima representa percepção coletiva e não deve ser reidentificada ou misturada ao histórico nominal.
-   \- CNTR-PESQ-004 — Classificação de publicação: conteúdo classificado como TREINO\_PUBLICO pode chegar à atleta; TECNICO\_INTERNO e INTERNO\_NAO\_PUBLICAR permanecem no escopo do treinador.
-   \- CNTR-PESQ-005 — Escopo: o módulo de otimização/pesquisa de horários é MÓDULO FUTURO CONHECIDO; suas regras devem ser preservadas na modelagem mesmo quando a UI não fizer parte da V1.

## D. CEPRAEA — Questionários de Competição

-   \- CNTR-QCOMP-001 — Três momentos distintos: ANTES DOS JOGOS, PÓS-JOGO e FECHAMENTO DA ETAPA possuem finalidade, perguntas e contexto próprios.
-   \- CNTR-QCOMP-002 — Contexto de jogo vem do sistema: em questionário pós-jogo, jogo\_id deve ser derivado do contexto/link/rota sempre que conhecido; a atleta não escolhe livremente um jogo que o sistema já determinou.
-   \- CNTR-QCOMP-003 — Uso entre jogos: o fluxo pode sustentar leitura rápida do treinador, pedido de conversa, definição de poucos ajustes e preparação para o jogo seguinte.
-   \- CNTR-QCOMP-004 — Privacidade: respostas individuais e pedidos de conversa são privados para o treinador. Para comunicação coletiva, usar somente tendências agregadas e não identificáveis.
-   \- CNTR-QCOMP-005 — Coleta incompleta não é regressão técnica: número de respostas abaixo do esperado gera alerta de cobertura de coleta; perda, duplicação, classificação incorreta ou normalização divergente gera erro técnico.
-   \- CNTR-QCOMP-006 — Escopo: questionários de competição são MÓDULO FUTURO CONHECIDO para integração ao painel do treinador; não entram na Home da atleta na V1.

## E. CEPRAEA — Wellness — Configuração e Respostas

-   \- CNTR-WELL-001 — Escopo V1: Wellness permanece FORA DO ESCOPO FUNCIONAL DA V1.0 do dashboard. A V1 não cria Home/relatório de Wellness para atleta nem mistura Wellness a disponibilidade, presença ou frequência.
-   \- CNTR-WELL-002 — Sensibilidade: dados de Wellness, dor, desconforto, sintomas, ciclo menstrual, metas pessoais e observações relacionadas são dados sensíveis e exigem autorização própria, armazenamento restrito e ausência em logs comuns.
-   \- CNTR-WELL-003 — Fluxo Pré→Pós: uma resposta Pré válida gera token/link Pós personalizado associado à mesma atleta, sessão e metas declaradas; o Pós avalia as metas daquele Pré.
-   \- CNTR-WELL-004 — Somente link contextual: link genérico de Pós não deve ser distribuído quando o fluxo exige token personalizado.
-   \- CNTR-WELL-005 — Participação autorreferida não é presença canônica: “completa/parcial” no Wellness Pós permanece dado do questionário e nunca confirma automaticamente presença factual.
-   \- CNTR-WELL-006 — Schema e histórico: versões de formulário, links superseded, testes E2E e falhas históricas devem ser preservados; migração não reescreve respostas históricas para parecerem produzidas pelo schema atual.
-   \- CNTR-WELL-007 — Identificadores técnicos não são rótulos humanos: ATH/TRN/CAL podem existir internamente, mas não devem aparecer como rótulo principal para a atleta quando houver nome/descrição humana adequada.
-   \- CNTR-WELL-008 — Integração futura: eventual módulo Wellness exige contrato de autorização separado e gate específico de segurança antes de entrar no produto.

## F. Glossário de Dados — CEPRAEA

-   \- CNTR-GLOSS-001 — Autoridade semântica: o Glossário é a referência de significado dos conceitos. Implementação não pode redefinir silenciosamente um termo por conveniência de tela.
-   \- CNTR-GLOSS-002 — Atleta ≠ usuário autenticado: identidade esportiva e conta de acesso são entidades relacionadas, não sinônimas.
-   \- CNTR-GLOSS-003 — Vínculo temporal: atleta/equipe possui período de vínculo com início e término opcional; vínculos sobrepostos para a mesma atleta/equipe são inválidos; inativação não apaga histórico.
-   \- CNTR-GLOSS-004 — Disponibilidade: compromisso, resposta, versão imutável e projeção atual são conceitos distintos e devem permanecer distinguíveis.
-   \- CNTR-GLOSS-005 — Presença: registro factual, estado e fonte são independentes da disponibilidade; observed\_at não pode anteceder o início da sessão.
-   \- CNTR-GLOSS-006 — Auditoria operacional: alterações relevantes devem produzir evento de auditoria com entidade, ação, ator, momento, estado anterior, estado novo e identificador de transação quando aplicável.
-   \- CNTR-GLOSS-007 — RLS: ao migrar para Supabase, autorização deve restringir linhas e operações por usuário, papel, vínculo e contexto; estar autenticado não basta.
-   \- CNTR-GLOSS-008 — Idempotência: operações mutáveis críticas, especialmente disponibilidade, devem possuir proteção contra repetição.
-   \- CNTR-GLOSS-009 — Fonte legada: toda migração relevante preserva legacy\_source\_ref ou equivalente suficiente para rastrear origem.
-   \- CNTR-GLOSS-010 — Fuso operacional: America/Sao\_Paulo é o fuso canônico das operações CEPRAEA até decisão formal de mudança; conversões para ISO não podem alterar o significado local de treino, jogo ou prazo.
-   \- CNTR-GLOSS-011 — Ciclo de vida dos termos: conceito não é apagado para corrigir semântica; quando substituído, deve ser marcado como obsoleto/sucedido com histórico correspondente.

## G. Autoavaliação – CEPRAEA

-   \- CNTR-AUTO-001 — Autoavaliação é domínio próprio: não é Wellness, disponibilidade, presença, participação em jogo nem questionário entre jogos.
-   \- CNTR-AUTO-002 — Caminhos condicionais: atleta que participou da etapa e atleta que não participou podem receber blocos de perguntas diferentes; o sistema deve preservar essa ramificação.
-   \- CNTR-AUTO-003 — Privacidade individual: respostas qualitativas e avaliações individuais são privadas para a própria atleta e o treinador quando houver autorização; uma atleta nunca consulta o texto de outra.
-   \- CNTR-AUTO-004 — Agregação: tendências coletivas podem ser exibidas apenas quando agregadas de forma que não exponham conteúdo individual.
-   \- CNTR-AUTO-005 — Escopo: Autoavaliação é MÓDULO FUTURO CONHECIDO e sensível; não bloqueia a V1, mas sua existência deve orientar modelo de dados, autorização e classificação de publicação.

## CONTRATOS TRANSVERSAIS OBRIGATÓRIOS

-   \- CNTR-X-001 — Toda informação deve declarar uma classe de publicação: ATLETA\_PUBLICO, TREINADOR\_INTERNO ou SENSIVEL\_RESTRITO, ou equivalente documentado.
-   \- CNTR-X-002 — exibir\_agenda, aceita\_resposta, participa\_cepraea, status\_evento e conteudo\_publicado são dimensões independentes; nenhuma deve ser inferida automaticamente a partir de outra.
-   \- CNTR-X-003 — nenhum dado ausente deve ser convertido em estado negativo, concluído ou factual sem regra explícita.
-   \- CNTR-X-004 — nenhuma interface pode depender de texto visual de uma aba quando existir ID canônico.
-   \- CNTR-X-005 — divergência entre fonte canônica e derivada é evento de qualidade de dados; não deve ser escondida por fallback silencioso.
-   \- CNTR-X-006 — telas, DTOs, migrations e testes devem referenciar estes contratos CNTR-\* como critérios de aceite.
-   \- CNTR-X-007 — módulos futuros conhecidos permanecem fora do escopo funcional da V1 quando indicado, mas não podem ser apagados do modelo nem tratados como descoberta futura inexistente.

# ROADMAP EXECUTIVO

-   Fase 0 — Fundação e governança
-   Fase 1 — Identidade, autenticação e autorização
-   Fase 2 — Contrato de dados e endurecimento das planilhas
-   Fase 3 — Dashboard individual da atleta em leitura
-   Fase 4 — Disponibilidade transacional
-   Fase 5 — Dashboard do treinador
-   Fase 6 — Validação, segurança e release gate
-   Fase 7 — Preview e piloto controlado
-   Fase 8 — Produção e cutover da agenda mensal
-   Fase 9 — Migração definitiva para Supabase-first

# 

## FASE 0 — FUNDAÇÃO E GOVERNANÇA

### Objetivo

Criar um projeto independente, reproduzível e versionado fora de Git, sem alterar o aplicativo atual durante o piloto.

### Ações

-   \- DASH-001: criar projeto React + TypeScript + Vite.
-   \- DASH-002: configurar TypeScript, lint, typecheck, testes e build.
-   \- DASH-003: aplicar identidade visual CEPRAEA.
-   \- DASH-004: configurar PWA, viewport mobile e safe areas.
-   \- DASH-005: separar development, preview e production.
-   \- DASH-006: criar .env.example sem segredos.
-   \- DASH-007: criar validate:dashboard.
-   \- Criar no Drive:
    -   DASHBOARD CEPRAEA/
    -   00\_DOCUMENTACAO,
    -   01\_CODIGO\_FONTE,
    -   02\_RELEASES,
    -   03\_VALIDACOES,
    -   04\_BACKUPS
    -   05\_DESIGN.

\- Definir versionamento: v0.1.0 fundação; v0.2.0 atleta; v0.3.0 disponibilidade; v0.4.0 treinador; v0.9.0 piloto; v1.0.0 produção.

### Entregáveis

Projeto inicial executável, estrutura de pastas no Drive, manifesto de release, modelo de backup e script de validação.

### Dependências

Nenhuma.

### Gate de saída

A versão v0.1.0 pode ser reconstruída apenas com o ZIP e o manifesto armazenados no Drive.

# FASE 1 — IDENTIDADE, AUTENTICAÇÃO E AUTORIZAÇÃO

### Objetivo

Garantir que cada sessão acesse somente o escopo autorizado.

### Ações

\- DASH-AUTH-001: reutilizar o projeto Supabase atual.

\- DASH-AUTH-002: definir os perfis ATLETA e TREINADOR.

\- DASH-AUTH-003: implementar GET /api/me.

\- DASH-AUTH-004: bloquear acesso quando não existir vínculo válido.

\- DASH-AUTH-005: rejeitar athlete\_id recebido do frontend como critério de autorização.

\- DASH-AUTH-006: implementar logout.

\- DASH-AUTH-007: manter redefinição de senha pelo Supabase.

\- DASH-AUTH-008: permitir primeiro acesso somente para e-mail previamente autorizado.

\- DASH-AUTH-009: testar acesso cruzado entre atletas.

\- DASH-AUTH-010: testar tentativa de atleta acessar endpoints do treinador.

### Entregáveis

Sessão autenticada, resolução segura de perfil e athlete\_id e guards de API.

### Dependências

Fase 0.

### Gate de saída

Uma atleta autenticada não consegue ler ou alterar dados de outra atleta por URL, query, body ou chamada direta de API.

## FASE 2 — CONTRATO DE DADOS E ENDURECIMENTO DAS PLANILHAS

### Objetivo

Criar uma camada de dados estável, sem dependência da posição física das células.

### Ações de dados

\- DASH-DATA-001 a 005: criar credencial Google exclusiva, conceder escopo mínimo, guardar segredos no Vercel e acessar Sheets somente no servidor.

\- DASH-DATA-006: definir DTOs de resposta.

\- DASH-DATA-007: normalizar datas no backend para ISO 8601.

\- DASH-DATA-008: evento\_id é a chave de evento.

\- DASH-DATA-009: athlete\_id é a chave de atleta.

\- DASH-DATA-010: evento\_id + athlete\_id é a chave de disponibilidade.

\- DASH-DATA-011: eliminar MATCH por dd/mm no aplicativo.

\- DASH-DATA-012: suportar múltiplos eventos na mesma data.

\- DASH-DATA-013: cache curto apenas para leitura não sensível.

\- DASH-DATA-014: timeout, retry limitado e tratamento de indisponibilidade.

\- DASH-DATA-015: estado de contingência amigável.

\- DASH-DATA-016: implementar classificação de publicação por campo e separar exibir\_agenda, aceita\_resposta, participa\_cepraea, status\_evento e conteudo\_publicado.

\- DASH-DATA-017: implementar proveniência, histórico imutável, idempotência e auditoria para operações mutáveis críticas.

\- DASH-DATA-018: manter presença factual separada de disponibilidade e impedir qualquer inferência automática entre os dois domínios.

\- DASH-DATA-019: modelar adversário como entidade estável e validar consistência de jogos/segmentos.

## Ações nas planilhas

\- DASH-SHEET-001: auditar DB\_EVENTOS.

\- DASH-SHEET-002: garantir evento\_id único.

\- DASH-SHEET-003: garantir chave evento\_id + athlete\_id única.

\- DASH-SHEET-004: reconciliar o histórico de agosto.

\- DASH-SHEET-005: testar múltiplos eventos na mesma data.

\- DASH-SHEET-006: validar próximo treino por ID.

\- DASH-SHEET-007: ampliar testes de integridade/regressão.

\- DASH-SHEET-008: manter a entrada antiga ativa até aceite do novo fluxo.

\- DASH-SHEET-009: documentar rollback.

\- Reestruturar DB\_EXPORT\_AGENDA para separar catálogo de atletas, catálogo de eventos e declarações.

\- Manter DB\_EXPORT\_FRONTEND com chaves estáveis para próximo treino, competições e indicadores.

\- Garantir que PRÓXIMO TREINO use NEXT\_TRAINING\_ID e não data como identidade.

### Contrato mínimo da API

\- GET /api/me

\- GET /api/athlete/dashboard

\- GET /api/athlete/events

\- GET /api/athlete/trainings/:eventoId

\- GET /api/athlete/competitions

\- GET /api/athlete/results

\- POST /api/athlete/availability

\- GET /api/coach/dashboard

\- GET /api/coach/events

\- GET /api/coach/trainings/:eventoId/composition

\- GET /api/coach/availability

\- GET /api/coach/competitions

\- GET /api/coach/results

\- GET /api/coach/data-quality

### Entregáveis

Camada server-side de Sheets, contratos de API e bases canônicas reconciliadas.

### Dependências

Fases 0 e 1.

### Gate de saída

Inserir, remover ou reordenar linhas/colunas não altera a identidade de atleta, evento ou declaração; dois eventos na mesma data permanecem distintos.

## FASE 3 — DASHBOARD INDIVIDUAL DA ATLETA EM LEITURA

### Objetivo

Entregar valor à atleta primeiro em modo somente leitura, antes de habilitar qualquer escrita.

### Telas

\- Início: saudação, próximo treino, horário, local, minha confirmação, próxima competição e pendências.

\- Agenda: treinos e competições por data/horário, inclusive múltiplos eventos no mesmo dia.

\- Treinos: próximos, histórico, detalhe e plano do treino quando publicado.

\- Competições: próximas competições, local, participação do CEPRAEA, convocação própria quando autorizada e resultados coletivos.

\- Perfil: nome, e-mail, dados esportivos apropriados, redefinição de senha e logout.

### Ações

\- DASH-ATH-001 a 005: layout mobile, home, agenda, cartões e detalhe de treino.

\- DASH-ATH-007 e 008: competições e perfil.

\- DASH-ATH-009: loading, empty e error states.

\- DASH-ATH-010: validar em iPhone e Android.

\- DASH-ATH-011: acessibilidade e contraste.

\- DASH-ATH-012: provar ausência de exposição cruzada.

**Não exibir**

Respostas de outras atletas, conteúdo individual sensível de Wellness, questionários individuais de outras atletas, observações internas do treinador, chaves DB\_\* ou controles de regressão.

**Entregáveis**

Dashboard individual navegável e seguro em modo leitura.

**Dependências**

Fases 1 e 2.

**Gate de saída**

A atleta vê somente o próprio contexto; próximo treino e agenda coincidem com a base canônica em desktop e celular.

# FASE 4 — DISPONIBILIDADE TRANSACIONAL

**Objetivo**

Permitir que a única ação operacional da atleta seja declarar SIM, NAO ou TALVEZ, gravando pelo ID correto.

**Fluxo**

1\. A atleta abre o evento.

2\. A API identifica athlete\_id pela sessão.

3\. O frontend envia apenas evento\_id + resposta.

4\. O servidor valida se o evento aceita declaração.

5\. O servidor cria nova versão append-only da resposta e atualiza a projeção atual do compromisso evento\_id + athlete\_id.

6\. A resposta final é devolvida ao dashboard.

7\. O painel do treinador passa a refletir a nova composição.

**Ações**

\- DASH-ATH-006: implementar confirmação.

\- DASH-AVL-001: definir estados válidos.

\- DASH-AVL-002: definir janela de edição.

\- DASH-AVL-003: definir comportamento para evento cancelado/encerrado.

\- DASH-AVL-004: implementar inserção idempotente de versão + atualização da projeção atual.

\- DASH-AVL-005: impedir duplicidade.

\- DASH-AVL-006: registrar atualizado\_em e origem.

\- DASH-AVL-007: mudança de resposta altera a projeção atual sem apagar, sobrescrever ou renumerar versões anteriores.

\- DASH-AVL-008: total SIM deve ser coerente com a composição por posição/função.

\- DASH-AVL-009: reconciliar com DB\_DISPONIBILIDADE\_DECLARADA durante a coexistência.

\- DASH-AVL-010: não desativar a entrada antiga antes da reconciliação final.

**Entregáveis**

Confirmação funcional no celular e atualização coerente do estado canônico.

**Dependências**

Fases 2 e 3.

**Gate de saída**

Reordenar atleta ou evento não desloca resposta; uma mudança SIM → TALVEZ → NAO permanece vinculada ao mesmo evento\_id + athlete\_id, preserva as três versões no histórico e expõe NAO apenas como projeção atual.

# FASE 5 — DASHBOARD DO TREINADOR

**Objetivo**

Concentrar a operação diária em uma Central de Comando, sem leitura manual da agenda mensal.

**Telas**

\- Central: próximo treino, SIM/NAO/TALVEZ/sem resposta, composição resumida, próxima competição, prazos/pendências operacionais e alertas prioritários.

\- Próximo Treino: lista nominal, goleiras, defesa, ataque, função INDEFINIDA quando existir, sem resposta, conteúdo publicado, histórico recente e cobertura tática quando os dados forem suficientes.

\- Agenda: treinos e competições por evento\_id.

\- Equipe: atletas ativas, posição/função, vínculo de acesso e frequência quando consolidada.

\- Competições e Resultados: calendário, jogos, vitórias, derrotas, aproveitamento, sets, shoot-outs, análise por competição e por adversário estável; quando habilitado, contexto Dia do Jogo ANTES/DURANTE/DEPOIS.

\- Qualidade dos dados: regressões técnicas, evento sem ID, declaração duplicada, resultado realizado incompleto, falha de sincronização, conflito entre fontes e cobertura de coleta incompleta apresentada separadamente de erro técnico.

**Ações**

\- DASH-COACH-001: Central de Comando.

\- DASH-COACH-002: composição do próximo treino.

\- DASH-COACH-003: painel de respostas.

\- DASH-COACH-004: agenda integrada.

\- DASH-COACH-005: visão da equipe.

\- DASH-COACH-006: competições.

\- DASH-COACH-007: resultados.

\- DASH-COACH-008: qualidade dos dados.

\- DASH-COACH-009: estados de contingência.

\- DASH-COACH-010: garantir separação total entre dados internos e perfil atleta.

**Entregáveis**

Painel operacional do treinador sincronizado com as mesmas fontes canônicas usadas pelo dashboard da atleta.

**Dependências**

Fases 2 e 4.

**Gate de saída**

Depois que uma atleta altera a resposta, o painel do treinador reflete o novo total e a nova composição sem ajuste manual de planilha.

# FASE 6 — VALIDAÇÃO, SEGURANÇA E RELEASE GATE

**Objetivo**

Substituir a ausência de CI por um processo obrigatório de validação local e registro no Drive.

**Gate técnico**

npm run validate:dashboard deve executar typecheck, lint, testes unitários, testes de integração, build, verificação de secrets e E2E quando configurado.

**Testes funcionais mínimos**

Login treinador, login atleta, primeiro acesso, redefinição de senha, logout, próximo treino, agenda, múltiplos eventos na mesma data, confirmação SIM, alteração de resposta, evento cancelado/encerrado, atualização do painel do treinador e resultados coletivos.

**Testes de segurança mínimos**

Atleta A tentando consultar atleta B; envio manual de athlete\_id de outra atleta; atleta chamando endpoint do treinador; usuário sem vínculo; token expirado; sessão revogada; request sem JWT; tentativa de acesso direto ao Google Sheets; ausência de segredos no bundle.

**Testes de regressão de dados**

evento\_id único; chave evento\_id + athlete\_id única; atleta ativa existente; evento existente; dois eventos na mesma data distintos; próximo treino igual ao canônico; total SIM coerente com a composição; nenhum #REF! em exports ativos; indicadores de jogos coerentes; nenhum payload de atleta com informação individual sensível indevida; SEM\_RESPOSTA não normalizado para NAO; disponibilidade não convertida em presença; versões anteriores de disponibilidade preservadas; convocação distinta de participação em jogo; conteúdo interno pendente não publicado; adversário resolvido por identidade estável; resultado concluído coerente com seus segmentos; testes de contrato fonte canônica → API → UI nos campos críticos.

**Testes de UX**

iPhone Safari, Android Chrome, modo retrato, teclado aberto, safe-area, rede lenta, refresh de página, sessão persistida e feedback imediato após confirmação.

**Entregáveis**

VALIDACAO\_DASHBOARD\_vX.Y.Z.txt e manifesto da release em 03\_VALIDACOES.

**Dependências**

Fases 3, 4 e 5.

**Gate de saída**

O relatório termina com RELEASE\_GATE=OK.

# FASE 7 — PREVIEW E PILOTO CONTROLADO

Objetivo

Validar uso real sem afetar o aplicativo atual nem desativar a agenda mensal.

**Ações**

\- DASH-DEP-001: criar projeto Vercel independente.

\- DASH-DEP-002: não alterar cepraea.vercel.app durante o piloto.

\- DASH-DEP-003: cadastrar variáveis de ambiente.

\- DASH-DEP-004: gerar Preview.

\- DASH-DEP-005: validar login.

\- DASH-DEP-006: validar APIs.

\- DASH-DEP-007: executar checklist mobile.

\- DASH-DEP-008: registrar URL e deployment ID no manifesto.

\- DASH-DEP-009: aprovar a versão para piloto.

**Escopo do piloto**

Treinador + grupo reduzido de atletas. Uso real para leitura e disponibilidade. Comparar dashboard e planilha após cada alteração relevante.

**Critérios do piloto**

Login funciona; cada atleta vê apenas seus dados; próximo treino coincide; confirmação coincide; composição do treinador está correta; nenhum evento é perdido/duplicado; múltiplos eventos na mesma data funcionam; nenhuma regressão é introduzida; experiência mobile aprovada.

**Entregáveis**

Preview aprovado e relatório do piloto.

**Dependências**

Fase 6.

**Gate de saída**

Piloto estável, sem divergência crítica entre dashboard e base canônica.

# FASE 8 — PRODUÇÃO E CUTOVER DA AGENDA MENSAL

**Objetivo**

Promover o dashboard a canal oficial de disponibilidade sem perda de histórico ou rollback.

**Pré-condições**

Todas as atletas ativas têm acesso funcional; disponibilidade grava por evento\_id + athlete\_id; painel do treinador reflete respostas; regressões estão OK; existe backup; rollback está documentado.

**Sequência de cutover**

1\. Fazer snapshot da agenda mensal.

2\. Reconciliar todas as respostas.

3\. Bloquear novas respostas na matriz antiga.

4\. Exibir aviso de migração.

5\. Ativar o dashboard como entrada oficial.

6\. Monitorar divergências diariamente no período inicial.

7\. Manter a planilha como visão/histórico durante estabilização, em modo somente leitura para disponibilidade; não reativá-la como fonte concorrente de escrita enquanto o dashboard for o canal oficial.

8\. Remover dependências antigas apenas após validação.

**Ações de deploy**

\- DASH-DEP-010: promover versão aprovada para produção.

\- DASH-DEP-011: manter deployment anterior disponível para rollback.

**Entregáveis**

Dashboard em produção e agenda mensal antiga fora do caminho crítico de entrada.

**Dependências**

Fase 7.

**Gate de saída**

Não é mais necessário editar a agenda mensal para declarar disponibilidade ou saber quem irá ao treino.

# FASE 9 — MIGRAÇÃO DEFINITIVA PARA SUPABASE-FIRST

Objetivo

Retirar Google Sheets do caminho crítico do aplicativo, mantendo as planilhas como exportação, análise ou contingência.

**Ações**

\- Mapear DB\_ATLETAS → athletes.

\- Mapear DB\_TREINOS/DB\_EVENTOS → trainings/events.

\- Mapear DB\_DISPONIBILIDADE\_DECLARADA → availability, preservando compromisso, versões append-only, projeção atual, origem, idempotência e referência legada.

\- Mapear presença factual → attendance em estrutura separada; nunca derivar attendance de availability.

\- Mapear competições, adversários, jogos e segmentos para tabelas operacionais com integridade referencial.

\- Mapear vínculos temporais de atleta/equipe sem sobreposição.

\- Criar audit\_events para alterações operacionais relevantes.

\- Preservar IDs ou criar crosswalk explícito.

\- Migrar e reconciliar.

\- Mudar APIs para Supabase.

\- Manter Sheets apenas como exportação/contingência.

\- Eliminar a credencial Google do caminho crítico quando possível.

**Entregáveis**

Aplicativo operacional Supabase-first.

**Dependências**

Fase 8 estabilizada.

**Gate de saída**

O dashboard continua operando mesmo se as planilhas estiverem temporariamente indisponíveis.

# CAMINHO CRÍTICO

Fundação → Auth/autorização → contrato de dados → atleta leitura → disponibilidade → treinador → validação → piloto → produção/cutover → Supabase-first.

# REGRAS DE SEGURANÇA

\- JWT obrigatório em todo endpoint privado.

\- athlete\_id derivado da sessão.

\- Service account Google apenas server-side e com privilégio mínimo.

\- Segredos apenas em variáveis de ambiente do Vercel.

\- Não registrar senhas, tokens completos, conteúdo sensível de Wellness ou segredos em logs.

\- Cache apenas para dados não sensíveis e com invalidação após escrita.

\- Logs usam IDs técnicos e códigos de erro.

# GOVERNANÇA SEM GIT

Cada versão deve gerar ZIP do código, manifesto com versão/data/hash/ambiente/URL do Preview/variáveis obrigatórias sem valores secretos/resultado dos testes, relatório de validação e backup anterior. Uma release só pode ser promovida se for reproduzível a partir dos artefatos do Drive.

# DEFINITION OF DONE — V1.0

\- Atleta e treinador autenticam com Supabase.

\- Cada atleta recebe dashboard individual derivado da própria sessão.

\- O treinador recebe dashboard agregado.

\- Próximo treino e agenda são identificados por IDs estáveis.

\- A atleta declara disponibilidade sem editar planilha.

\- A resposta corrente é consultável por evento\_id + athlete\_id, mas cada alteração é persistida como nova versão imutável com proveniência e idempotência.

\- O treinador vê composição atualizada sem converter disponibilidade em presença factual.

\- Dois eventos na mesma data não entram em conflito.

\- SEM\_RESPOSTA não é tratado como NAO.

\- Convocação e participação em jogo permanecem fatos distintos.

\- Conteúdo interno não publicado não aparece para a atleta.

\- A matriz mensal antiga permanece somente leitura após o cutover.

\- Os contratos CNTR-\* críticos possuem testes automatizados ou validação reproduzível registrada.

\- Não existe exposição cruzada de dados.

\- Mobile real aprovado.

\- Preview aprovado.

\- Release versionada e arquivada no Drive.

\- RELEASE\_GATE=OK.

\- Backup e rollback disponíveis.

\- Produção explicitamente aprovada.

# PRÓXIMOS MARCOS

Marco 1 — v0.1.0 Fundação reproduzível.

Marco 2 — v0.2.0 Dashboard da atleta em leitura.

Marco 3 — v0.3.0 Disponibilidade transacional.

Marco 4 — v0.4.0 Dashboard do treinador.

Marco 5 — v0.9.0 Preview e piloto.

Marco 6 — v1.0.0 Produção e cutover.

Marco 7 — Supabase-first após estabilização.

# REFERÊNCIAS OPEN SOURCE E ENGENHARIA REVERSA

# Objetivo

Usar projetos open source maduros como referência de arquitetura, navegação, componentes e organização de código, sem copiar identidade visual. Esta etapa existe para evitar que o CEPRAEA fique preso a uma única linguagem estética ou a padrões genéricos de fitness/dashboard.

## Princípio de uso

\- Reutilizar conceitos arquiteturais e padrões de componentes quando forem compatíveis com o Roadmap.

\- Adaptar os padrões ao domínio de handebol de praia, esporte coletivo, equipe, treino, competição e operação do treinador.

\- Não copiar branding, paleta, tipografia, iconografia ou composição visual de um template como identidade final do CEPRAEA.

\- Todo componente adotado deve ser reespecificado pelo Design System CEPRAEA.

\- O painel do treinador pode usar sidebar no desktop e navegação adaptada no mobile; a atleta permanece mobile-first e mais simples.

\- Não aceitar roxo dominante, neon forte, estética de corrida/fitness ou grade repetitiva de cards como padrão automático do produto.

# Repositórios prioritários para engenharia reversa

## 1\. satnaing/shadcn-admin — https://github.com/satnaing/shadcn-admin

Licença: MIT. Stack: React + TypeScript + Vite, Tailwind, TanStack Router/Query/Table, Radix, Lucide, Vitest e Playwright. Pontos de interesse: src/components/layout/app-sidebar.tsx, src/components/ui/sidebar.tsx, src/components/layout/data/sidebar-data.ts, src/context/layout-provider.tsx, src/features/dashboard, src/features/auth, src/routes/\_authenticated, src/styles/theme.css e package.json. Uso esperado no CEPRAEA: referência principal para arquitetura por features, shell do app, sidebar, providers, tokens e testes; não copiar a estética final.

## 2\. TailAdmin/free-react-tailwind-admin-dashboard — https://github.com/TailAdmin/free-react-tailwind-admin-dashboard

Licença: MIT. Stack: React + TypeScript + Vite, React Router, Tailwind e FullCalendar. Pontos de interesse: src/App.tsx, src/layout/AppLayout.tsx, src/layout/AppSidebar.tsx, src/layout/AppHeader.tsx, src/context/SidebarContext.tsx, páginas de Dashboard/Calendar/Tables/Auth e package.json. Uso esperado no CEPRAEA: referência para AppLayout, sidebar responsiva, rotas e agenda/calendário; adaptar sem transformar o produto em admin template genérico.

## 3\. design-sparx/antd-multipurpose-dashboard — https://github.com/design-sparx/antd-multipurpose-dashboard

Licença: MIT. Stack: React + TypeScript + Vite + Ant Design 5. Pontos de interesse: src/App.tsx, src/main.tsx, src/layouts/app/app.tsx, src/layouts/app/side-nav.tsx, src/components/shared/mobile-tab-bar/mobile-tab-bar.tsx, src/pages/home.tsx e layouts de conta/guest. Uso esperado no CEPRAEA: referência para a estratégia desktop com side navigation e mobile com tab bar; evitar dependência visual excessiva da identidade padrão do Ant Design.

## Referências complementares

\- tabler/tabler — referência visual e de UX para dashboards técnicos, tabelas, status, badges, densidade, navegação e linguagem clean; não é a base de stack do projeto.

\- tremorlabs/tremor — referência de componentes de dados, métricas, tabelas, trackers e visualizações compactas para o painel do treinador.

\- refinedev/refine — referência arquitetural para resources, autorização, queries, filtros e aplicações internas; não adotar o framework inteiro sem necessidade comprovada.

\- coreui/coreui-free-react-admin-template — referência clássica de shell operacional e navegação; não usar como identidade visual.

\- codescandy/dash-ui-react-vitejs-typescript — referência adicional para separação entre RootLayout, Sidebar e estilos de navegação.

## Ações adicionadas à Fase 0

\- DASH-OSS-001: executar engenharia reversa dos três repositórios prioritários, arquivo por arquivo.

\- DASH-OSS-002: produzir matriz “arquivo open source → função → equivalente CEPRAEA → reutilizar conceito / adaptar / não usar”.

\- DASH-OSS-003: identificar padrões recorrentes de App.tsx, main.tsx, router, layouts, sidebar, header, mobile navigation, feature folders, components, theme/tokens, auth e testes.

\- DASH-OSS-004: separar claramente arquitetura técnica de identidade visual.

\- DASH-OSS-005: propor a Árvore Oficial de Arquivos CEPRAEA v1.0 somente depois da matriz comparativa.

\- DASH-OSS-006: mapear cada arquivo oficial proposto a uma ação DASH-\* existente do Roadmap.

\- DASH-OSS-007: registrar quais conceitos serão adotados, adaptados ou rejeitados antes de iniciar a implementação v0.1.0.

## Gate de saída da pesquisa open source

A Fase 0 não fecha sua arquitetura de arquivos por mera preferência do assistente ou por cópia de um template. Antes da implementação oficial, deve existir uma matriz de engenharia reversa dos três repositórios prioritários e uma Árvore Oficial de Arquivos CEPRAEA aprovada, com justificativa para sidebar/layout, navegação mobile, estrutura de features, Design System e testes.

## Decisão de design associada

As referências open source servem para ampliar o espaço de soluções. O CEPRAEA deve ter identidade visual própria ligada a handebol de praia, equipe e competição. O design poderá combinar sidebar técnica para o treinador, superfícies claras ou escuras sem predominância obrigatória de roxo, tipografia própria, iconografia específica de handebol de praia, tabelas/listas/timelines/metric strips e componentes editoriais, evitando dependência excessiva de cards.

# 

# RESULTADO DA ENGENHARIA REVERSA — 25/08/2026

## Status

\- DASH-OSS-001: EXECUTADO — arquivos estruturais e de UX dos três repositórios prioritários foram lidos diretamente no GitHub.

\- DASH-OSS-002: EXECUTADO — matriz comparativa produzida no histórico do projeto.

\- DASH-OSS-003: EXECUTADO — padrões de entry point, providers, rotas, layouts, sidebar, navegação mobile, features, temas e testes foram identificados.

\- DASH-OSS-004: EXECUTADO — arquitetura técnica foi separada da identidade visual dos templates.

\- DASH-OSS-005: PENDENTE — próxima ação é propor a Árvore Oficial de Arquivos CEPRAEA v1.0 com base na matriz.

\- DASH-OSS-006: PENDENTE — depende da Árvore Oficial.

\- DASH-OSS-007: PENDENTE — depende da aprovação da Árvore Oficial e das decisões finais de adoção.

## Síntese técnica

\- Base arquitetural preferencial: organização por features, providers, rotas autenticadas e tokens inspirada conceitualmente em satnaing/shadcn-admin.

\- Shell do treinador: sidebar responsiva, header e outlet inspirados conceitualmente em Shadcn Admin e TailAdmin, sem copiar identidade visual.

\- Navegação responsiva: sidebar no desktop e navegação mobile própria, seguindo o padrão observado em design-sparx/antd-multipurpose-dashboard.

\- Agenda do treinador: avaliar FullCalendar como componente de apresentação, sempre alimentado por evento\_id canônico; não gerar IDs de evento no cliente.

\- Design System: usar tokens próprios CEPRAEA. Não importar paleta, fonte, radius, sombras, ícones ou estética padrão dos templates.

\- Iconografia: bibliotecas genéricas podem atender ações utilitárias, mas funções esportivas centrais devem ter iconografia CEPRAEA específica de handebol de praia.

\- Autenticação: manter Supabase conforme o Roadmap; não adotar Clerk, Redux ou qualquer solução de autenticação/estado dos templates apenas por semelhança arquitetural.

\- Testes: adotar o conceito de testes de interação e navegação observado em Shadcn Admin e integrá-lo ao validate:dashboard.

\- Dashboard: não copiar a grade genérica de cards dos templates. O conteúdo deve usar componentes coerentes com a tarefa: sidebar, listas, timeline, agenda, metric strips, tabelas, status, composição e blocos editoriais.

## Decisão provisória antes da Árvore Oficial

A engenharia reversa não escolheu um template único. O CEPRAEA deverá combinar padrões arquiteturais comprovados, mantendo implementação e identidade próprias. Nenhum arquivo open source será copiado integralmente para a base CEPRAEA sem revisão de licença, dependências, segurança, acessibilidade e adequação ao domínio.

Design dos Dashboards

Design dos Dashboards

Antes, estávamos tentando resolver a aparência enquanto ainda havia comportamentos importantes escondidos nas planilhas. Isso fazia o design nascer de referências visuais — roxo, fitness, cards, apps de corrida — em vez de nascer da operação real do CEPRAEA.

Com o Roadmap 2.3, isso mudou. Agora temos contratos explícitos para disponibilidade, presença, convocação, participação em jogo, publicação de conteúdo, Dia do Jogo, composição tática, privacidade, questionários, histórico e qualidade dos dados.

Isso permite desenhar cada elemento porque sabemos qual problema ele resolve.

# PRINCÍPIO DE GRANULARIDADE DO DESIGN

Granularidade é o nível mínimo de detalhe em que uma decisão deixa de ser apenas um conceito amplo e passa a ser especificável, comparável, prototipável e validável. Cada seção deve decompor seu conceito até o grão adequado à sua função — nem mais abstrato, nem mais detalhado do que o necessário.

## Escala de decomposição

### G0 — PRODUTO:

Propósito global do CEPRAEA e limites do produto.

### G1 — EXPERIÊNCIA/PERFIL:

Experiência ATLETA ou TREINADOR e seus jobs-to-be-done.

### G2 — FLUXO/CONTEXTO:

Sequência de uso, modo operacional ou contexto temporal.

### G3 — TELA/ROTA:

Uma tela identificável com função, entrada, saída e ação principal.

### G4 — BLOCO FUNCIONAL:

Unidade de informação/ação dentro de uma tela, como próximo treino, disponibilidade, convocação, agenda ou composição.

### G5 — COMPONENTE/INTERAÇÃO/ESTADO:

Controle manipulável ou estado observável, como SIM/TALVEZ/NÃO, linha de evento, seletor, expansão, confirmação, loading, vazio, erro e offline.

### G6 — TOKEN/ESPECIFICAÇÃO VISUAL:

Regra atômica reutilizável, como papel tipográfico, espaçamento, grid, ícone, stroke, radius, cor semântica ou motion token.

**Regra de parada**: cada seção deve chegar ao seu grão-alvo e parar antes de invadir o grão de outra seção ou detalhes de implementação. O design só avança quando o grão definido é suficiente para validar função, prioridade, comportamento e identidade.

## 

## 

## MAPA DE GRÃO POR SEÇÃO

### 1\. Arquitetura Mobile — grão-alvo G3: TELA/ROTA

-   **Decomposição obrigatória:** perfil → necessidade/job → fluxo → tela.
-   Para cada tela, registrar **nome, perfil autorizado, objetivo, gatilho de entrada, saída, ação primária, ações secundárias, domínios de dados usados e variações contextuais relevantes**.
-   A arquitetura deve responder quais telas existem e por quê.
-   **Ponto de parada**: não escolher ainda card, cor, tipografia ou estilo de componente.

### 2\. Hierarquia de informação — grão-alvo G4: BLOCO FUNCIONAL

-   **Decomposição obrigatória:** tela → blocos → informações/ações pertencentes ao bloco.
-   Cada bloco deve registrar propósito, prioridade relativa, fonte/contrato, visibilidade, ordem, relação com outros blocos e se possui ação. A hierarquia deve dizer o que domina, o que apoia, o que pode ser adiado e o que não aparece.
-   **Ponto de parada: não definir a aparência final do bloco.**

### 3\. Direções visuais — grão-alvo G4 visual: VOCABULÁRIO DE COMPOSIÇÃO

-   **Decomposição obrigatória:** direção → princípios de composição → tipos de superfície → ritmo espacial → contraste → uso de linhas/quadra/areia → tratamento de listas, faixas, timelines, placares e blocos editoriais → comportamento de imagem/textura/motion.
-   Cada direção deve produzir uma gramática visual reconhecível aplicada às mesmas funções, e não apenas uma paleta diferente.
-   **Ponto de parada: não fechar tokens atômicos antes da escolha da direção.**

### 4\. Tipografia — grão-alvo G6: TOKEN TIPOGRÁFICO SEMÂNTICO

-   **Decomposição obrigatória:** papel semântico → família → peso → tamanho → line-height → tracking → caixa → comportamento numérico → limite de linhas.
-   Devem existir papéis explícitos para display esportivo, título, seção, corpo, legenda, status, placar, data/hora e dado denso.
-   **Ponto de parada:** cada texto da interface deve conseguir apontar para um papel tipográfico; evite criar estilos avulsos por tela.

### 5\. Iconografia — grão-alvo G6: ÍCONE/ASSET SEMÂNTICO

-   **Decomposição obrigatória:** conceito/ação → metáfora visual → grid → stroke → geometria → terminais → variante ativa/inativa quando necessária → label acessível.
-   Cada função central de handebol de praia deve possuir semântica própria e consistente. Ícones utilitários genéricos só são aceitos para ações universais.
-   **Ponto de parada:** um ícone deve representar um único conceito sem depender de emoji, texto decorativo ou repertório de fitness.

### 6\. Estado da competição e contexto operacional — grão-alvo G3/G4: ESTADO CONTEXTUAL DE TELA

-   **Decomposição obrigatória:** contexto ROTINA / PRÉ-COMPETIÇÃO / DIA DO JOGO / PÓS-ETAPA → gatilho de entrada → gatilho de saída → blocos que sobem de prioridade → blocos que descem/ocultam → ações disponíveis → dados obrigatórios → fallback quando a informação estiver incompleta.
-   O mesmo Dashboard pode reorganizar sua hierarquia sem mudar de identidade.
-   **Ponto de parada: não duplicar quatro Homes independentes; prefira modelar estados da mesma experiência.**

### 7\. Especificação rigorosa por tela — grão-alvo G5: CONTRATO DE TELA E INTERAÇÃO

-   **Decomposição obrigatória:** tela → FUNÇÃO + DADO + AÇÃO + PRIORIDADE + PRIVACIDADE + ESTADOS + COMPOSIÇÃO; para cada bloco acionável, decompor ainda em estado inicial, ação, feedback, sucesso, erro, indisponibilidade e retorno.
-   Cada tela deve ter critérios de aceite verificáveis contra os contratos CNTR-\* e a fonte canônica.
-   **Ponto de parada: não descer para props, nomes de arquivos ou implementação React; isso pertence à guia Roadmap de Implementação.**

## Gate de granularidade do Design

Nenhum mockup de alta fidelidade deve ser tratado como candidato final antes de:

-   Arquitetura Mobile atingir G3;
-   Hierarquia atingir G4;
-   Estados contextuais atingirem G3/G4;
-   Cada tela crítica possuir contrato G5.
-   Direções visuais atingirem o grão G4 visual;
-   Tipografia e iconografia atingirem o grão G6 antes da consolidação do Design System.

# O processo

## 1\. Arquitetura Mobile

Definir exatamente quais telas existem para ATLETA e TREINADOR, qual função pertence a cada uma e quais informações aparecem primeiro, segundo e terceiro.

Não começamos por cor ou card.

Começamos por perguntas como:

-   O que a atleta precisa resolver em 10 segundos ao abrir o app?
-   O que o treinador precisa perceber imediatamente antes de um treino?
-   O que muda quando estamos em dia normal, pré-competição ou Dia do Jogo?

# EXECUÇÃO G3 — ARQUITETURA MOBILE

## Escopo desta execução

A arquitetura abaixo decompõe o produto mobile até TELA/ROTA. Ela define destinos, fluxos e responsabilidades de cada tela, mas não define cards, cores, fontes, ícones, radius ou componentes finais. Módulos classificados no Roadmap como futuros conhecidos — Wellness, Autoavaliação, Questionários de Competição, Pesquisa de Horários e Feedback Individual — não geram rotas funcionais da V1. Seus contratos permanecem preservados para evolução futura.

## Princípio de navegação G3

Uma função não precisa virar uma aba permanente para existir. O grão G3 separa DESTINO PRIMÁRIO, TELA SECUNDÁRIA e VARIANTE CONTEXTUAL. Disponibilidade é uma ação contextual; convocação própria é informação da competição; Dia do Jogo é um estado contextual; nenhum desses conceitos exige, por si só, uma rota principal independente.

## ARQUITETURA COMPARTILHADA — ENTRADA E SESSÃO

Fluxo compartilhado G2: abrir app → resolver sessão → autenticar quando necessário → resolver perfil autorizado no servidor → entrar na experiência ATLETA ou TREINADOR. athlete\_id nunca é escolhido no cliente.

### AUTH-G3-01 — LOGIN | rota /login

Perfil autorizado: público até autenticação. Objetivo: iniciar sessão com conta previamente autorizada. Entrada: app sem sessão válida ou sessão expirada. Saída: Home da atleta ou Central do treinador conforme perfil resolvido; recuperação de senha quando solicitada. Ação primária: autenticar. Ações secundárias: iniciar redefinição de senha. Domínios: autenticação Supabase, identidade de usuário e vínculo autorizado. Variante: credencial inválida ou usuário sem vínculo deve bloquear entrada sem revelar dados esportivos.

### AUTH-G3-02 — DEFINIR/REDEFINIR SENHA | rota /auth/password

Perfil autorizado: usuário em fluxo válido de primeiro acesso ou recuperação. Objetivo: concluir credencial de acesso. Entrada: link/contexto Supabase válido. Saída: Login ou experiência autenticada conforme sessão resultante. Ação primária: definir nova senha. Ações secundárias: voltar ao login. Domínios: autenticação; não acessa dados esportivos.

### AUTH-G3-03 — ACESSO NÃO AUTORIZADO | rota /access-denied

Perfil autorizado: usuário autenticado sem vínculo válido ou perfil incompatível. Objetivo: encerrar o fluxo de forma segura e explicar que aquela sessão não possui acesso ao produto. Entrada: resolução de sessão sem vínculo válido ou tentativa de acessar área de outro perfil. Saída: logout/login. Ação primária: sair da sessão. Domínios: identidade/autorização; não expõe dados da equipe.

## ATLETA — DECOMPOSIÇÃO G1 → G2 → G3

Jobs-to-be-done G1: saber o que vem agora; declarar a própria disponibilidade; consultar agenda e treinos; entender a própria situação em competições/convocações; acompanhar resultados coletivos; consultar o próprio perfil e encerrar a sessão.

### Fluxos G2 da atleta

A. Rotina diária: Login/sessão → Início → próximo compromisso → ação pendente quando existir.

B. Disponibilidade: Início ou Detalhe do Treino → responder SIM/TALVEZ/NAO se aceita\_resposta → permanecer no contexto do mesmo evento.

C. Agenda: Início → Agenda → selecionar evento → Detalhe do Treino ou Detalhe da Competição.

D. Treino: Início/Agenda/Treinos → Detalhe do Treino → consultar data, local, conteúdo publicado e própria resposta.

E. Competição: Início/Agenda/Competições → Detalhe da Competição → consultar participação do CEPRAEA, própria convocação quando autorizada e resultados coletivos.

F. Contexto competitivo: quando ROTINA muda para PRÉ-COMPETIÇÃO, DIA DO JOGO ou PÓS-ETAPA, Início e Detalhe da Competição reorganizam prioridade, sem criar Homes independentes.

G. Conta: qualquer destino primário → Perfil → redefinir senha ou logout.

### Navegação mobile da atleta no G3

Destinos primários: INÍCIO, AGENDA, COMPETIÇÕES e PERFIL. TREINOS permanece uma tela funcional secundária acessível por Início, Agenda e links contextuais. Essa decisão reduz destinos permanentes sem remover nenhuma função prevista no Roadmap.

### ATH-G3-01 — INÍCIO | rota /athlete

Perfil autorizado: ATLETA. Objetivo: responder em poucos segundos “o que vem agora e preciso fazer algo?”. Entrada: login válido, retomada do app ou retorno ao destino principal. Saídas: Agenda, Treinos/Detalhe do Treino, Competições/Detalhe da Competição e Perfil. Ação primária: responder disponibilidade quando houver evento elegível e resposta pendente/alterável; quando não houver ação, consultar o próximo compromisso. Ações secundárias: abrir agenda, competição/convocação ou último resultado coletivo. Domínios: eventos, treinos, projeção atual da própria disponibilidade, competições relevantes, própria convocação autorizada e resultados coletivos. Variantes: ROTINA, PRÉ-COMPETIÇÃO, DIA DO JOGO e PÓS-ETAPA alteram prioridade dos blocos, não a identidade da tela.

### ATH-G3-02 — AGENDA | rota /athlete/agenda

Perfil autorizado: ATLETA. Objetivo: consultar compromissos publicáveis em ordem temporal, suportando múltiplos eventos no mesmo dia. Entrada: navegação primária, Início ou retorno de detalhe. Saídas: Detalhe do Treino ou Detalhe da Competição; retorno ao Início. Ação primária: selecionar um evento. Ações secundárias: navegar no período quando necessário. Domínios: DB\_EVENTOS/contrato equivalente já filtrado por exibir\_agenda, participação do CEPRAEA e classe de publicação. Variante: evento pode aparecer sem aceitar resposta; exibir\_agenda e aceita\_resposta permanecem independentes.

### ATH-G3-03 — TREINOS | rota /athlete/trainings

Perfil autorizado: ATLETA. Objetivo: oferecer acesso organizado a próximos treinos e histórico permitido sem transformar a Home em arquivo completo. Entrada: Início, Agenda ou link contextual. Saídas: Detalhe do Treino; retorno ao destino anterior. Ação primária: abrir um treino. Ações secundárias: alternar entre próximos e histórico quando houver dados válidos. Domínios: treinos/eventos e estado publicável; não expõe observação técnica interna.

### ATH-G3-04 — DETALHE DO TREINO | rota /athlete/trainings/:eventoId

Perfil autorizado: ATLETA e somente contexto próprio. Objetivo: concentrar tudo que é publicável sobre um treino específico. Entrada: Início, Agenda ou Treinos. Saídas: origem anterior, Agenda ou Início. Ação primária: declarar/alterar SIM, TALVEZ ou NAO quando aceita\_resposta permitir. Ações secundárias: consultar data, horário, local, status e plano somente quando conteudo\_publicado estiver válido. Domínios: evento/treino por evento\_id, própria projeção de disponibilidade e conteúdo classificado ATLETA\_PUBLICO. Variantes: resposta pendente, resposta já registrada, janela encerrada, evento cancelado/encerrado e conteúdo ainda não publicado. Conteúdo interno pendente não é exibido como texto para a atleta.

### ATH-G3-05 — COMPETIÇÕES | rota /athlete/competitions

Perfil autorizado: ATLETA. Objetivo: consultar competições relevantes ao CEPRAEA e separar claramente participação, convite/a confirmar, classificação e histórico. Entrada: navegação primária, Início ou Agenda. Saídas: Detalhe da Competição; retorno ao Início. Ação primária: abrir competição. Ações secundárias: acessar competição anterior/próxima quando permitido. Domínios: competições publicáveis, situação da participação do CEPRAEA e resultados coletivos resumidos. Variante: competição preservada apenas para auditoria e em que o CEPRAEA não participa não entra na lista normal da atleta.

### ATH-G3-06 — DETALHE DA COMPETIÇÃO | rota /athlete/competitions/:competitionId

Perfil autorizado: ATLETA. Objetivo: explicar “qual é a situação desta competição para mim e para o CEPRAEA?”. Entrada: Competições, Agenda ou Início contextual. Saídas: Competições, Agenda ou Início. Ação primária: consultar situação atual; a V1 não cria ação administrativa de convocação para atleta. Ações secundárias: consultar própria convocação quando autorizada, programação publicável e resultados coletivos. Domínios: competição, participação CEPRAEA, própria convocação, jogos/segmentos/resultados coletivos publicáveis. Variantes: ANTES/PRÉ-COMPETIÇÃO, DURANTE/DIA DO JOGO e DEPOIS/PÓS-ETAPA. Convocação própria não vira tela separada; Dia do Jogo é variante desta experiência e pode também ganhar prioridade na Home.

### ATH-G3-07 — PERFIL | rota /athlete/profile

Perfil autorizado: ATLETA. Objetivo: consultar identidade e dados esportivos próprios apropriados e controlar a sessão. Entrada: navegação primária. Saídas: Início, fluxo de senha ou Login após logout. Ação primária: consultar/gerenciar conta disponível. Ações secundárias: redefinir senha e logout. Domínios: identidade autenticada e dados próprios autorizados de atleta. Não inclui Wellness, respostas individuais sensíveis, dados de outras atletas ou controles internos.

### Decisões G3 específicas da atleta

-   Disponibilidade NÃO é rota: é ação contextual em Início e Detalhe do Treino.
-   Minha Convocação NÃO é rota primária: pertence ao Detalhe da Competição e só mostra a própria situação.
-   Resultado coletivo NÃO exige rota própria na V1: entra em Competições/Detalhe da Competição; eventual detalhe de jogo só será criado se a Seção 2 demonstrar necessidade real.
-   Dia do Jogo NÃO cria uma segunda Home: altera a prioridade da Home e o estado do Detalhe da Competição.
-   Presença factual NÃO possui ação de escrita para atleta na V1 e nunca é inferida da disponibilidade.

## TREINADOR — DECOMPOSIÇÃO G1 → G2 → G3

Jobs-to-be-done G1: perceber o que exige atenção agora; operar o próximo treino; consultar lista nominal e composição; acompanhar agenda e prazos; consultar equipe; acompanhar competições, convocações e Dia do Jogo; analisar resultados; detectar problemas de qualidade de dados; controlar a própria sessão.

### Fluxos G2 do treinador

A. Operação diária: Login/sessão → Central → identificar atenção prioritária → abrir Próximo Treino, Agenda, Competição ou Qualidade.

B. Próximo treino: Central/Treino → Detalhe do Treino → consultar SIM/TALVEZ/NAO/SEM\_RESPOSTA → lista nominal → composição/cobertura tática quando disponível.

C. Agenda: Central → Agenda → selecionar evento → Detalhe do Treino ou Detalhe da Competição.

D. Equipe: Central/Equipe → lista de atletas → Detalhe da Atleta quando necessário → consultar função/posição, vínculo e frequência factual somente quando consolidada.

E. Competição: Central/Mais → Competições → Detalhe da Competição → prazos, participação, convocação, jogos e contexto operacional.

F. Dia do Jogo: Detalhe da Competição em estado DURANTE → último resultado, próximo jogo, fase, programação e pendências; não cria aplicação paralela.

G. Resultados: Mais/Competição → Resultados → análise por competição/adversário e qualidade dos segmentos.

H. Qualidade: Central/Mais → Qualidade dos Dados → identificar divergência → navegar ao domínio relacionado quando houver destino seguro.

I. Conta: Mais → Conta/Logout.

## 

## Navegação mobile do treinador no G3

**Destinos primários**: CENTRAL, TREINO, AGENDA, EQUIPE e MAIS.  
MAIS é um hub de navegação secundária para Competições, Resultados, Qualidade dos Dados e Conta.

Essa arquitetura preserva acesso rápido à operação diária sem tentar colocar todas as funções na navegação persistente.

### COACH-G3-01 — CENTRAL | rota /coach

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: responder “o que exige atenção agora?”.
-   **Entrada**: login válido, retomada do app ou retorno ao destino principal.
-   **Saídas**: Próximo Treino, Agenda, Equipe, Detalhe da Competição, Resultados, Qualidade ou Mais.
-   **Ação primária**: abrir a pendência/contexto operacional mais relevante.
-   **Ações secundárias**: consultar próximo treino, disponibilidade agregada, composição resumida, competição/prazo e indicadores coletivos.
-   **Domínios**: eventos, treinos, disponibilidade agregada, atletas/funções, competições/prazos, resultados coletivos e alertas de qualidade.
-   **Variante**: ROTINA, PRÉ-COMPETIÇÃO, DIA DO JOGO e PÓS-ETAPA reorganizam prioridade.

### COACH-G3-02 — PRÓXIMO TREINO / DETALHE DO TREINO | rota /coach/trainings/:eventoId

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: operar um treino por evento\_id sem depender da matriz mensal.
-   **Entrada**: Central, Agenda ou destino primário TREINO, que resolve o próximo treino canônico quando existir.
-   **Saídas**: Central, Agenda, Equipe/Detalhe da Atleta quando aplicável.
-   **Ação primária**: consultar composição operacional atual.
-   **Ações secundárias**: abrir grupos SIM/TALVEZ/NAO/SEM\_RESPOSTA, consultar lista nominal, função/posição, conteúdo do treino e cobertura tática quando os dados forem suficientes.
-   **Domínios**: treino/evento, disponibilidade atual por atleta, cadastro esportivo, posições/sistemas táticos e conteúdo técnico.
-   **Variantes**: treino sem respostas, função INDEFINIDA, conteúdo não publicado para atleta mas disponível internamente, evento encerrado/cancelado e cobertura tática insuficiente/indeterminada. Disponibilidade continua diferente de presença factual.

### COACH-G3-03 — AGENDA | rota /coach/agenda

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: consultar a operação temporal completa do CEPRAEA por evento, incluindo treinos, competições e prazos/pendências quando existentes.
-   **Entrada**: navegação primária ou Central.
-   **Saídas**: Detalhe do Treino ou Detalhe da Competição.
-   **Ação primária**: selecionar evento/compromisso.
-   **Ações secundárias**: navegar no período e localizar pendências.
-   **Domínios**: eventos, competições, prazos, participação CEPRAEA, criticidade/action necessária quando canônicas.
-   **Variantes**: múltiplos eventos no mesmo dia e registros históricos que não são exibidos à atleta.

### COACH-G3-04 — EQUIPE | rota /coach/team

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: consultar o elenco ativo e sua estrutura esportiva sem misturar disponibilidade com presença.
-   **Entrada**: navegação primária, Central ou Treino.
-   **Saídas**: Detalhe da Atleta; retorno à origem.
-   **Ação primária**: localizar/abrir atleta.
-   **Ações secundárias**: consultar função, posição e estado de vínculo; frequência apenas quando houver presença factual consolidada.
-   **Domínios**: atletas, vínculo temporal, função/posição e presença factual consolidada quando disponível. Não inclui interpretação automática de Wellness.

### COACH-G3-05 — DETALHE DA ATLETA | rota /coach/team/:athleteId

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: consultar contexto esportivo/operacional autorizado de uma atleta específica.
-   **Entrada**: Equipe ou lista nominal do Treino.
-   **Saídas**: Equipe ou Detalhe do Treino de origem.
-   **Ação primária**: consultar função/posição e vínculo operacional.
-   **Ações secundárias**: consultar posições secundárias e frequência factual quando consolidada.
-   **Domínios**: atleta, vínculo, função/posição e presença factual autorizada.

Wellness, Autoavaliação e questionários sensíveis permanecem fora desta tela na V1.

### COACH-G3-06 — MAIS | rota /coach/more

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: servir como hub mobile para destinos menos frequentes que não devem competir com a operação diária na navegação persistente.
-   **Entrada**: navegação primária.
-   **Saídas**: Competições, Resultados, Qualidade dos Dados, fluxo de Conta/Senha ou Logout.
-   **Ação primária**: escolher destino.
-   **Ações secundárias**: acessar configurações e conta.
-   **Domínios**: navegação/autorização; possui independência de dados operacionais próprios.

### COACH-G3-07 — COMPETIÇÕES | rota /coach/competitions

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: consultar calendário competitivo e situação operacional de cada competição.
-   **Entrada**: Mais, Central ou Agenda.
-   **Saídas**: Detalhe da Competição.
-   **Ação primária**: abrir competição.
-   **Ações secundárias**: distinguir próximas/realizadas e localizar pendências/prazos.
-   **Domínios**: competições, participação CEPRAEA, prazos e resumo de resultados.

### COACH-G3-08 — DETALHE DA COMPETIÇÃO | rota /coach/competitions/:competitionId

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: reunir o contexto operacional da competição sem misturar convocação com participação em jogo.
-   **Entrada**: Competições, Agenda ou Central contextual.
-   **Saídas**: origem, Resultados ou contexto relacionado.
-   **Ação primária**: consultar/operar a situação da competição conforme permissões da V1.
-   **Ações secundárias**: consultar prazos, convocação/lista nominal, programação, jogos, resultados e pendências.
-   **Domínios**: competição, participação CEPRAEA, convocação, atletas convocadas, jogos, adversários estáveis, segmentos/resultados e qualidade relacionada.
-   **Variantes**: ANTES, DURANTE/DIA DO JOGO e DEPOIS; durante, próximo jogo/último resultado/fase ganham prioridade. Participação em jogo continua fato distinto da convocação.

### COACH-G3-09 — RESULTADOS | rota /coach/results

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: consultar campanha coletiva validada e navegar por competição/adversário sem depender da aba visual ANÁLISE JOGOS.
-   **Entrada**: Mais, Central ou Detalhe da Competição.
-   **Saídas**: Detalhe da Competição ou Central.
-   **Ação primária**: consultar/filtrar análise.
-   **Ações secundárias**: alternar competição/adversário e identificar resultado com dados incompletos.
-   **Domínios**: jogos, segmentos, adversários, vitórias/derrotas, aproveitamento, sets e shoot-outs via API/export canônico. Dados individuais de participação permanecem fora enquanto a fonte carecer de reconciliação.

### COACH-G3-10 — QUALIDADE DOS DADOS | rota /coach/data-quality

-   **Perfil autorizado**: TREINADOR.
-   **Objetivo**: tornar divergências operacionais visíveis sem misturá-las com a interface da atleta.
-   **Entrada**: Mais ou alerta da Central.
-   **Saídas**: Central ou domínio relacionado quando houver link seguro.
-   **Ação primária**: identificar pendência/regressão.
-   **Ações secundárias**: distinguir erro técnico de coleta incompleta e abrir contexto afetado.
-   **Domínios**: validação/regressão, conflitos entre fontes, IDs ausentes/duplicados, resultados incompletos, falhas de sincronização e contratos DB→API→UI. Proíbe-se a invenção de fallback silencioso.

### Decisões G3 específicas do treinador

-   TREINO é destino primário, mas resolve um evento por evento\_id; não existe “treino por data” como identidade.
-   Disponibilidade nominal e composição pertencem ao Detalhe do Treino; não criam telas independentes na V1.
-   Convocação pertence ao Detalhe da Competição; não é confundida com participação em cada jogo.
-   Dia do Jogo é estado do Detalhe da Competição e da Central, não um aplicativo/tela paralela obrigatória.
-   Resultados possuem destino próprio porque a análise histórica por competição/adversário é uma tarefa distinta da operação de uma competição específica.
-   Qualidade dos Dados é exclusiva do treinador.
-   Presença/frequência só aparece quando sustentada por presença factual consolidada; não existe ação de “converter SIM em presença”.

## DECISÕES TRANSVERSAIS DE ARQUITETURA G3

1\. Uma única aplicação resolve o perfil após autenticação e encaminha para /athlete ou /coach.

2\. Rotas privadas respeitam perfil; navegação não é mecanismo de autorização.

3\. evento\_id identifica cada evento mesmo com datas iguais; competitionId, athleteId e demais IDs canônicos sustentam detalhes.

4\. A Home/Central é contextual, mas não se multiplica em quatro Homes para cada fase competitiva.

5\. Exibir um evento, aceitar resposta, participar da competição, status do evento e publicar conteúdo são decisões independentes.

6\. A arquitetura mobile não cria telas para dados ausentes apenas para preencher navegação; aviso vazio permanece ausência de aviso.

7\. Wellness, Autoavaliação, Questionários de Competição, Pesquisa de Horários e Feedback Individual permanecem sem rotas V1, conforme contratos de escopo já registrados.

8\. Nenhuma tela da atleta expõe respostas de outras atletas, observações internas, qualidade de dados ou dados sensíveis.

9\. Nenhuma tela de produção consome diretamente abas visuais/analíticas; os domínios descritos pressupõem API/export canônico validado.

## COBERTURA FUNCIONAL DO G3

-   Próximo treino → ATH-G3-01/04 e COACH-G3-01/02.
-   Disponibilidade → ação em ATH-G3-01/04; leitura agregada/nominal em COACH-G3-01/02.
-   Agenda e múltiplos eventos → ATH-G3-02 e COACH-G3-03.
-   Treinos/histórico/conteúdo → ATH-G3-03/04 e COACH-G3-02.
-   Equipe/função/posição → COACH-G3-04/05; atleta vê apenas o próprio contexto em ATH-G3-07.
-   Competições/participação → ATH-G3-05/06 e COACH-G3-07/08.
-   Convocação própria → ATH-G3-06; gestão/consulta do treinador → COACH-G3-08.
-   Dia do Jogo → variantes de ATH-G3-01/06 e COACH-G3-01/08.
-   Resultados coletivos → ATH-G3-05/06 e COACH-G3-09.
-   Qualidade dos dados → COACH-G3-10.
-   Conta/logout → ATH-G3-07, COACH-G3-06 e fluxos AUTH.

## GATE DE SAÍDA — SEÇÃO 1 / G3

A Arquitetura Mobile atinge G3 quando toda função V1 possui um destino ou contexto explícito, cada tela possui perfil autorizado, objetivo, entrada, saídas, ação principal/secundárias, domínios e variantes relevantes, e não existem funções órfãs nem telas criadas apenas por convenção visual. Status desta execução: G3 DEFINIDO PARA ATLETA E TREINADOR. A Seção 2 pode decompor essas telas em blocos G4 sem alterar silenciosamente as responsabilidades aqui estabelecidas.

## 2\. Hierarquia de informação

Por exemplo, para a **atleta,** provavelmente teremos algo próximo de:

### INÍCIO

Próximo compromisso

↓

Minha disponibilidade / ação pendente

↓

Próxima competição / convocação

↓

Agenda próxima

↓

Último resultado / campanha

Isso não significa cinco cards.

Pode ser uma composição editorial com:

-   grande bloco temporal;
-   faixa de ação;
-   timeline;
-   divisores;
-   tipografia;
-   status;
-   elementos gráficos;
-   superfícies abertas.

### Para o treinador

**CENTRAL**

O que exige atenção agora?

↓

Próximo treino

↓

Disponibilidade nominal

↓

Cobertura/composição

↓

Agenda e prazos

↓

Competição

↓

Resultados / qualidade

**Aqui o design pode ser mais técnico e denso.**

# EXECUÇÃO G4 — HIERARQUIA DE INFORMAÇÃO

## Escopo e regra de leitura

Esta execução decompõe exclusivamente as telas ATH-G3-\* e COACH-G3-\* aprovadas na Arquitetura Mobile. O grão G4 define blocos funcionais, ordem, prioridade, propósito, fonte/contrato, visibilidade, relação e ação. Não define card, cor, tipografia, ícone, radius, grid final nem componente React. AUTH-G3-\* permanece fora desta decomposição porque a solicitação desta seção é a hierarquia funcional dos dashboards ATLETA e TREINADOR.

## Escala de prioridade G4

-   P0 — AÇÃO/ATENÇÃO IMEDIATA: bloco que precisa dominar quando existe uma ação pendente, risco operacional ou contexto de jogo em andamento.
-   P1 — CONTEXTO PRINCIPAL: informação que responde à pergunta central da tela mesmo quando não existe ação pendente.
-   P2 — APOIO OPERACIONAL: informação necessária para decidir, navegar ou interpretar o P0/P1.
-   P3 — REFERÊNCIA/HISTÓRICO: informação útil, mas que não deve competir com a tarefa principal.
-   PC — CONDICIONAL: bloco que só existe quando fonte canônica, permissão, estado ou contexto o justificam.

Regra: prioridade não significa tamanho visual obrigatório. Ela determina precedência cognitiva e ordem de leitura. Um bloco P0 pode ser uma faixa, lista, linha de status ou outra composição; G4 não prescreve card.

## Regras transversais de hierarquia

1\. Nenhuma tela deve preencher espaço com dado inexistente. Bloco sem conteúdo canônico pode desaparecer ou assumir empty state útil; aviso vazio continua ausência de aviso.

2\. A mesma informação não deve competir com ela própria em dois blocos da mesma tela. Resumo pode apontar para detalhe, mas não repetir integralmente o detalhe.

3\. Ação pendente vem antes de histórico. Em contexto sem ação, o contexto principal assume a primeira posição.

4\. exibir\_agenda, aceita\_resposta, participa\_cepraea, status\_evento e conteudo\_publicado permanecem independentes na hierarquia.

5\. Conteúdo ATLETA\_PUBLICO, TREINADOR\_INTERNO e SENSIVEL\_RESTRITO nunca compartilha bloco sem regra explícita de autorização.

6\. Resultado incompleto, conflito de fonte ou coleta incompleta deve ser indicado como qualidade do dado; nunca preenchido por inferência.

7\. ROTINA, PRÉ-COMPETIÇÃO, DIA DO JOGO e PÓS-ETAPA podem reordenar blocos já existentes, mas não criam uma segunda arquitetura paralela.

## ATLETA — HIERARQUIA G4

### ATH-G4-01 — INÍCIO | deriva de ATH-G3-01

B1 — PRÓXIMO COMPROMISSO E AÇÃO PENDENTE.

Propósito: responder “o que vem agora e preciso fazer algo?”. Prioridade: P0 quando existir resposta pendente/alterável; P1 quando for apenas consulta. Ordem: 1. Fonte/contrato: eventos/treinos canônicos, projeção atual de disponibilidade; CNTR-DB-002, CNTR-DB-003, CNTR-DB-005, CNTR-DB-014, CNTR-X-002, CNTR-X-003. Visibilidade: ATLETA\_PUBLICO e somente contexto próprio. Relação: abre ATH-G4-04 ou ATH-G4-06 conforme tipo do evento. Ação: responder disponibilidade somente em treino elegível e quando aceita\_resposta permitir; caso contrário, abrir detalhe.

B2 — PRÓXIMA COMPETIÇÃO / SITUAÇÃO PESSOAL.

Propósito: antecipar o próximo compromisso competitivo relevante e, quando autorizado, sinalizar a própria convocação. Prioridade: P1 em PRÉ-COMPETIÇÃO; P2 em ROTINA; P0 apenas em DIA DO JOGO quando o contexto competitivo for o compromisso dominante. Ordem: 2, podendo subir para 1 por contexto. Fonte/contrato: competições, participação CEPRAEA e própria convocação; CNTR-DB-008, CNTR-DB-011, CNTR-AGO-005, CNTR-X-001, CNTR-X-002. Visibilidade: somente competições publicáveis/relevantes e convocação da própria atleta. Relação: abre ATH-G4-06. Ação: consultar detalhe.

B3 — AGENDA PRÓXIMA.

Propósito: dar continuidade temporal sem transformar a Home em agenda completa. Prioridade: P2. Ordem: 3. Fonte/contrato: eventos filtrados por publicação/visibilidade; CNTR-DB-002, CNTR-X-001, CNTR-X-002, CNTR-GLOSS-010. Visibilidade: ATLETA\_PUBLICO. Relação: resumo da ATH-G4-02. Ação: abrir evento ou Agenda.

B4 — ÚLTIMO RESULTADO / CAMPANHA COLETIVA.

Propósito: manter continuidade esportiva sem introduzir análise individual não reconciliada. Prioridade: P3 em ROTINA; P1/P2 em PÓS-ETAPA. Ordem: 4, podendo subir após encerramento de competição. Fonte/contrato: jogos/segmentos/resultados validados; CNTR-DB-016, CNTR-DB-017, CNTR-AGO-006, CNTR-AGO-007. Visibilidade: resultado coletivo publicável. Relação: abre ATH-G4-06 da competição correspondente. Ação: consultar campanha/detalhe.

Decisão ATH-DEC-01 — Home orientada à ação ou dashboard de resumo.

Explicação: a planilha operacional exige principalmente que a atleta saiba o próximo compromisso e declare disponibilidade; métricas gerais não são a tarefa dominante. Impacto UX: uma Home de resumo aumenta leitura e dispersa a única ação operacional da atleta; uma Home orientada à ação reduz tempo até a tarefa. Recomendação: ADOTAR hierarquia action-first, com B1 dominante quando existir pendência e sem grade fixa de métricas.

Decisão ATH-DEC-02 — Permanência do resultado na Home.

Explicação: resultado coletivo é relevante, mas não deve competir com compromisso e disponibilidade. Impacto UX: excesso de conteúdo esportivo histórico empurra a ação principal para baixo. Recomendação: MANTER B4 em P3 na rotina e promovê-lo apenas no PÓS-ETAPA.

### ATH-G4-02 — AGENDA | deriva de ATH-G3-02

B1 — PERÍODO / ORIENTAÇÃO TEMPORAL.

Propósito: deixar claro qual intervalo está sendo consultado e permitir avançar/retornar sem confundir datas. Prioridade: P1. Ordem: 1. Fonte/contrato: fuso e calendário canônicos; CNTR-GLOSS-010. Visibilidade: ATLETA\_PUBLICO. Relação: controla B2 sem alterar identidade dos eventos. Ação: mudar período.

B2 — LINHA TEMPORAL DE EVENTOS PUBLICÁVEIS.

Propósito: apresentar treinos e competições em ordem temporal, inclusive mais de um evento no mesmo dia. Prioridade: P1. Ordem: 2. Fonte/contrato: eventos por evento\_id; CNTR-DB-002, CNTR-DB-008, CNTR-X-001, CNTR-X-002. Visibilidade: somente exibir\_agenda/publicação aplicáveis à atleta.

Relação: cada item abre ATH-G4-04 ou ATH-G4-06.

Ação: selecionar evento.

B3 — ESTADO DO EVENTO / MINHA AÇÃO.

Propósito: mostrar no próprio item somente o status necessário para decidir se existe ação, sem transformar a lista em detalhe. Prioridade: P2/PC. Ordem: incorporado semanticamente a B2. Fonte/contrato: status\_evento, aceita\_resposta e própria projeção de disponibilidade; CNTR-DB-003, CNTR-DB-005, CNTR-DB-006, CNTR-X-002. Visibilidade: contexto próprio. Relação: antecipa B1 de ATH-G4-04. Ação: abrir detalhe; resposta pode ser oferecida apenas se o padrão de interação G5 validar ação inline sem prejudicar compreensão.

B4 — ESTADO VAZIO / INDISPONIBILIDADE DE DADOS.

Propósito: diferenciar “sem eventos no período” de falha de carregamento. Prioridade: PC. Ordem: substitui B2 quando necessário. Fonte/contrato: CNTR-DB-009, CNTR-X-003, CNTR-X-005. Ação: trocar período ou tentar novamente, conforme causa.

Decisão ATH-DEC-03 — Timeline/lista versus calendário mensal como padrão mobile.

Explicação: o requisito principal é ordem temporal com múltiplos eventos no mesmo dia; uma grade mensal reduz espaço para horário, local e estados. Impacto UX: timeline aumenta legibilidade e área de toque; calendário mensal favorece visão panorâmica, mas exige mais passos para interpretar eventos. Recomendação: ADOTAR lista/timeline como padrão da V1; calendário mensal pode ser alternativa futura se surgir necessidade real.

Decisão ATH-DEC-04 — Responder disponibilidade diretamente na Agenda.

Explicação: a ação poderia reduzir um toque, mas mistura navegação temporal com escrita transacional e aumenta risco de resposta no evento errado. Impacto UX: ação inline é rápida, porém pode gerar erro contextual em dias com múltiplos eventos. Recomendação: MANTER Agenda como seleção/consulta no G4; disponibilidade principal permanece no Início e no Detalhe do Treino. Reavaliar ação inline somente no G5 com identificação inequívoca do evento.

### ATH-G4-03 — TREINOS | deriva de ATH-G3-03

B1 — PRÓXIMOS TREINOS.

Propósito: permitir acesso organizado às sessões futuras sem duplicar a Agenda inteira. Prioridade: P1. Ordem: 1. Fonte/contrato: treinos/eventos canônicos; CNTR-DB-002, CNTR-DB-006, CNTR-AGO-004. Visibilidade: ATLETA\_PUBLICO. Relação: abre ATH-G4-04. Ação: abrir treino.

B2 — HISTÓRICO PERMITIDO.

Propósito: consultar sessões passadas com informação publicável. Prioridade: P3. Ordem: 2. Fonte/contrato: histórico de treino e publicação; CNTR-DB-006, CNTR-DB-007, CNTR-X-001. Visibilidade: somente conteúdo publicável; presença/frequência não é inferida. Relação: abre ATH-G4-04 em estado histórico. Ação: abrir treino anterior.

B3 — CONTROLE PRÓXIMOS / HISTÓRICO.

Propósito: evitar uma lista longa misturando temporalidades. Prioridade: P2. Ordem: antes de B1/B2 quando ambos existirem. Fonte/contrato: derivação de estado temporal no fuso canônico; CNTR-GLOSS-010. Ação: alternar conjunto.

Decisão ATH-DEC-05 — Manter Treinos como tela secundária ou absorver tudo na Agenda.

Explicação: G3 preservou Treinos como acesso organizado a conteúdo e histórico; Agenda resolve compromissos gerais. Impacto UX: fundir reduz rotas, mas torna a Agenda mais densa e dificulta encontrar plano/histórico de treino. Recomendação: MANTER Treinos como secundária, sem item obrigatório na navegação persistente.

### ATH-G4-04 — DETALHE DO TREINO | deriva de ATH-G3-04

B1 — IDENTIDADE E ESTADO DO TREINO.

Propósito: ancorar a ação no evento correto com data, horário, local e estado. Prioridade: P1. Ordem: 1. Fonte/contrato: evento\_id/treino, ciclo de vida e fuso; CNTR-DB-002, CNTR-DB-006, CNTR-GLOSS-010. Visibilidade: ATLETA\_PUBLICO. Relação: contexto obrigatório para todos os demais blocos. Ação: nenhuma além de navegação contextual.

B2 — MINHA DISPONIBILIDADE.

Propósito: permitir consultar e, quando elegível, declarar/alterar SIM, TALVEZ ou NAO. Prioridade: P0 quando pendente/alterável; P2 quando janela encerrada e apenas leitura. Ordem: 2, podendo ser visualmente o principal após a identidade. Fonte/contrato: disponibilidade própria; CNTR-DB-003, CNTR-DB-005, CNTR-DB-014, CNTR-DB-015, CNTR-GLOSS-004, CNTR-GLOSS-008. Visibilidade: somente da própria atleta. Relação: altera projeção atual e reflete composição do treinador sem produzir presença. Ação: responder/alterar quando aceita\_resposta.

B3 — PLANO PUBLICADO DO TREINO.

Propósito: mostrar objetivo, metas, atividade e orientação somente quando publicados para atleta. Prioridade: P2. Ordem: 3. Fonte/contrato: conteúdo do treino com classificação de publicação; CNTR-DB-007, CNTR-AGO-004, CNTR-PESQ-004, CNTR-X-001. Visibilidade: somente ATLETA\_PUBLICO. Relação: independente do status e da disponibilidade. Ação: leitura.

B4 — ESTADOS DE INDISPONIBILIDADE/ENCERRAMENTO.

Propósito: explicar cancelamento, janela de resposta encerrada ou conteúdo ainda não publicado sem expor texto interno. Prioridade: PC, substitui ou modifica B2/B3 conforme o caso. Fonte/contrato: CNTR-DB-006, CNTR-DB-007, CNTR-X-002, CNTR-X-003. Ação: nenhuma ou retorno.

Decisão ATH-DEC-06 — Disponibilidade antes ou depois do plano do treino.

Explicação: disponibilidade é a única escrita operacional da atleta e possui janela temporal; o plano é informativo. Impacto UX: colocar conteúdo antes da ação aumenta scroll e pode reduzir taxa/velocidade de resposta. Recomendação: COLOCAR B2 imediatamente após B1 quando houver ação possível; com janela encerrada, B3 pode ganhar precedência.

Decisão ATH-DEC-07 — Mostrar placeholder de conteúdo pendente.

Explicação: as planilhas possuem marcadores internos de conteúdo ainda não definido. Impacto UX: expor placeholder técnico parece falha e vaza processo interno. Recomendação: NÃO EXIBIR placeholder interno; usar ausência neutra apenas se for útil comunicar “Plano ainda não publicado”.

### ATH-G4-05 — COMPETIÇÕES | deriva de ATH-G3-05

B1 — COMPETIÇÕES ATUAIS/PRÓXIMAS RELEVANTES.

Propósito: mostrar o calendário competitivo que efetivamente diz respeito ao CEPRAEA. Prioridade: P1. Ordem: 1. Fonte/contrato: competições + participa\_cepraea + classificação de publicação; CNTR-DB-008, CNTR-X-001, CNTR-X-002. Visibilidade: ATLETA\_PUBLICO; registros somente de auditoria/não participação ficam fora da lista normal. Relação: abre ATH-G4-06. Ação: abrir competição.

B2 — ESTADO DE PARTICIPAÇÃO DO CEPRAEA.

Propósito: diferenciar classificado, convidado/a confirmar, participação a confirmar e demais estados canônicos sem promover incerteza a confirmação. Prioridade: P1/P2; incorporado ao item de B1. Fonte/contrato: estado canônico da competição; CNTR-DB-008, CNTR-X-003. Visibilidade: publicável. Ação: abrir detalhe.

B3 — HISTÓRICO / COMPETIÇÕES ENCERRADAS.

Propósito: dar acesso a campanhas e resultados anteriores. Prioridade: P3. Ordem: 2. Fonte/contrato: competições/jogos/resultados validados; CNTR-DB-016, CNTR-AGO-006, CNTR-AGO-007. Visibilidade: coletivo publicável. Relação: abre ATH-G4-06 em PÓS-ETAPA. Ação: consultar.

Decisão ATH-DEC-08 — Ordenar por cronologia pura ou por relevância operacional.

Explicação: uma competição futura em que o CEPRAEA não participa pode estar cronologicamente mais próxima do que uma competição relevante. Impacto UX: cronologia pura pode induzir a atleta a interpretar evento externo como compromisso da equipe. Recomendação: FILTRAR primeiro por relevância/participação publicável e ordenar cronologicamente dentro do conjunto resultante.

### ATH-G4-06 — DETALHE DA COMPETIÇÃO | deriva de ATH-G3-06

B1 — IDENTIDADE DA COMPETIÇÃO E SITUAÇÃO CEPRAEA.

Propósito: responder qual competição é e qual é o estado da equipe. Prioridade: P1. Ordem: 1. Fonte/contrato: competição/participação; CNTR-DB-008, CNTR-X-002, CNTR-X-003. Visibilidade: ATLETA\_PUBLICO. Relação: contextualiza todos os blocos.

B2 — MINHA CONVOCAÇÃO.

Propósito: informar somente a situação da atleta na convocação quando houver autorização/dado. Prioridade: P0/P1 em PRÉ-COMPETIÇÃO quando existir decisão nominal publicada; PC quando não aplicável. Ordem: 2 antes da competição; pode cair após o início. Fonte/contrato: convocação + atleta da sessão; CNTR-DB-011, CNTR-X-001. Visibilidade: somente própria situação. Relação: não determina participação em cada jogo. Ação: leitura na V1.

B3 — PROGRAMAÇÃO / PRÓXIMO JOGO.

Propósito: apresentar programação publicável e, em DIA DO JOGO, destacar próximo jogo/fase. Prioridade: P2 antes; P0 durante. Ordem: 3 antes; 2 durante. Fonte/contrato: jogos/adversários/segmentos e contexto; CNTR-DB-016, CNTR-DB-017, CNTR-AGO-005. Visibilidade: coletiva publicável. Relação: durante, conecta B4 último resultado.

B4 — RESULTADOS / CAMPANHA COLETIVA.

Propósito: mostrar jogos realizados e campanha validada. Prioridade: P3 antes, P1 durante, P1 no pós. Ordem: 4 antes; 3 durante; 2 no pós. Fonte/contrato: jogos/segmentos validados; CNTR-DB-016, CNTR-AGO-006, CNTR-AGO-007. Visibilidade: coletiva. Ação: consultar resultado.

B5 — PENDÊNCIA/QUALIDADE PUBLICÁVEL.

Propósito: evitar apresentação falsa de placar/segmento quando o resultado estiver incompleto, sem expor controles internos. Prioridade: PC. Fonte/contrato: CNTR-DB-016, CNTR-X-003, CNTR-X-005. Visibilidade: linguagem pública de indisponibilidade, nunca diagnóstico interno. Relação: modifica B4.

Decisão ATH-DEC-09 — Uma única ordem fixa ou hierarquia contextual ANTES/DURANTE/DEPOIS.

Explicação: a tarefa da atleta muda radicalmente no Dia do Jogo. Impacto UX: ordem fixa força scroll para chegar ao próximo jogo durante a competição e mantém convocação em destaque quando já perdeu prioridade. Recomendação: ADOTAR reordenação contextual dos mesmos blocos; detalhamento de gatilhos fica na Seção 6.

Decisão ATH-DEC-10 — Criar tela separada “Minha Convocação”.

Explicação: a convocação pertence semanticamente à competição e só faz sentido com o contexto dela. Impacto UX: rota própria aumenta navegação e fragmenta a compreensão. Recomendação: NÃO CRIAR rota separada na V1; manter B2 dentro do detalhe.

### ATH-G4-07 — PERFIL | deriva de ATH-G3-07

B1 — IDENTIDADE DA CONTA. Propósito: deixar claro quem está autenticado.

Prioridade: P1. Ordem: 1. Fonte/contrato: identidade Supabase + vínculo; CNTR-GLOSS-002, CNTR-GLOSS-003. Visibilidade: própria atleta. Relação: não substitui identidade esportiva.

B2 — PERFIL ESPORTIVO PRÓPRIO.

Propósito: mostrar nome esportivo e dados apropriados como função/posição quando disponíveis. Prioridade: P2. Ordem: 2. Fonte/contrato: atleta/vínculo/função; CNTR-DB-010, CNTR-DB-012, CNTR-GLOSS-003. Visibilidade: somente própria atleta. Ação: leitura na V1.

B3 — SEGURANÇA E SESSÃO.

Propósito: redefinir senha e encerrar sessão. Prioridade: P2. Ordem: 3. Fonte/contrato: autenticação/autorização. Visibilidade: própria conta. Ação: redefinir senha/logout.

B4 — DADOS EXCLUÍDOS.

Propósito normativo: Wellness, respostas individuais sensíveis, dados de outras atletas e controles internos não compõem a tela. Prioridade: não renderizar. Fonte/contrato: CNTR-WELL-001, CNTR-WELL-002, CNTR-AUTO-003, CNTR-X-001.

Decisão ATH-DEC-11 — Perfil esportivo ou configurações de conta como foco da tela.

Explicação: “Perfil” pode virar um menu técnico e perder identidade esportiva. Impacto UX: conta-first parece área administrativa; sport-first reforça pertencimento, mantendo segurança acessível. Recomendação: B1/B2 primeiro e ações de conta em B3, sem introduzir métricas pessoais não sustentadas.

## TREINADOR — HIERARQUIA G4

### COACH-G4-01 — CENTRAL | deriva de COACH-G3-01

B1 — FILA DE ATENÇÃO OPERACIONAL.

Propósito: responder “o que exige ação agora?”, reunindo apenas pendências acionáveis e críticas. Prioridade: P0 quando houver item; PC quando nada exigir ação. Ordem: 1. Fonte/contrato: prazos/pendências, respostas faltantes, conflitos relevantes e contexto competitivo; CNTR-AGO-001, CNTR-X-005. Visibilidade: TREINADOR\_INTERNO. Relação: cada item aponta para treino, competição, agenda ou qualidade. Ação: abrir contexto.

B2 — PRÓXIMO TREINO.

Propósito: dar acesso imediato ao evento operacional mais próximo e seu estado. Prioridade: P1; pode ser P0 quando não existe B1 e treino é o compromisso dominante. Ordem: 2. Fonte/contrato: NEXT\_TRAINING\_ID/evento canônico; CNTR-DB-002, CNTR-DB-006, CNTR-AGO-004. Visibilidade: TREINADOR\_INTERNO. Relação: abre COACH-G4-02. Ação: abrir treino.

B3 — DISPONIBILIDADE RESUMIDA.

Propósito: mostrar SIM/TALVEZ/NAO/SEM\_RESPOSTA sem substituir a lista nominal. Prioridade: P1/P2. Ordem: associado a B2. Fonte/contrato: projeções atuais; CNTR-DB-003, CNTR-DB-005, CNTR-DB-014. Visibilidade: TREINADOR\_INTERNO. Relação: drill-down em COACH-G4-02. Ação: abrir grupo/lista.

B4 — COMPOSIÇÃO RESUMIDA.

Propósito: mostrar cobertura operacional inicial por função sem apresentar a contagem resumida como modelo tático completo. Prioridade: P2. Ordem: após B3. Fonte/contrato: atletas/funções/disponibilidade; CNTR-DB-010, CNTR-DB-012, CNTR-DB-013. Visibilidade: TREINADOR\_INTERNO. Relação: detalhe em COACH-G4-02. Ação: abrir composição.

B5 — COMPETIÇÃO / PRAZO MAIS RELEVANTE.

Propósito: antecipar competição, inscrição/lista nominal ou ação necessária. Prioridade: P1 em PRÉ-COMPETIÇÃO; P2 em ROTINA; P0 no Dia do Jogo conforme contexto. Ordem: depois do treino em rotina; sobe por contexto. Fonte/contrato: CNTR-AGO-001, CNTR-AGO-005, CNTR-DB-008. Visibilidade: TREINADOR\_INTERNO. Relação: abre COACH-G4-08. Ação: abrir competição/prazo.

B6 — RESULTADO/CAMPANHA RESUMIDA.

Propósito: oferecer continuidade analítica sem transformar a Central em painel estatístico. Prioridade: P3 em rotina; P1 no pós-etapa. Ordem: inferior/contextual. Fonte/contrato: CNTR-DB-016, CNTR-AGO-006, CNTR-AGO-007.

Relação: abre COACH-G4-09.

B7 — ALERTA DE QUALIDADE.

Propósito: expor apenas problemas que afetam decisão operacional atual. Prioridade: P0 se bloqueante; P3/PC se informativo. Fonte/contrato: CNTR-X-005, CNTR-AGO-008. Relação: abre COACH-G4-10. Ação: abrir diagnóstico.

Decisão COACH-DEC-01 — Central como dashboard de métricas ou central de atenção.

Explicação: o papel do treinador é decidir/agir, não contemplar indicadores gerais. Impacto UX: grade de métricas aumenta densidade e esconde pendências; fila de atenção melhora escaneabilidade operacional. Recomendação: ADOTAR attention-first; métricas só entram quando respondem a uma decisão.

Decisão COACH-DEC-02 — Quantos blocos podem competir no primeiro viewport.

Explicação: treino, competição, resultados e qualidade podem estar ativos simultaneamente. Impacto UX: muitos P1 simultâneos anulam a hierarquia. Recomendação: limitar cognitivamente o topo a B1 + contexto dominante; os demais aparecem em sequência, sem regra visual de “cards iguais”.

### COACH-G4-02 — PRÓXIMO TREINO / DETALHE DO TREINO | deriva de COACH-G3-02

B1 — IDENTIDADE/ESTADO DO EVENTO.

Propósito: fixar evento\_id, data, horário, local e estado. Prioridade: P1. Ordem: 1. Fonte/contrato: CNTR-DB-002, CNTR-DB-006, CNTR-GLOSS-010. Visibilidade: TREINADOR\_INTERNO.

B2 — DISTRIBUIÇÃO DE DISPONIBILIDADE.

Propósito: responder rapidamente quantas atletas estão SIM, TALVEZ, NAO e SEM\_RESPOSTA. Prioridade: P1. Ordem: 2. Fonte/contrato: CNTR-DB-003, CNTR-DB-005, CNTR-DB-014. Relação: controla/filtra B3. Ação: selecionar estado.

B3 — LISTA NOMINAL.

Propósito: mostrar quem compõe cada estado de disponibilidade e função/posição necessária à operação.

Prioridade: P0/P1.

Ordem: 3.

Fonte/contrato: disponibilidade atual + atletas; CNTR-DB-003, CNTR-DB-010, CNTR-DB-012.

Visibilidade: TREINADOR\_INTERNO. Relação: abre COACH-G4-05 quando necessário. Ação: filtrar/abrir atleta.

B4 — COMPOSIÇÃO OPERACIONAL.

Propósito: sintetizar Goleiras/Defesa/Ataque e função INDEFINIDA sem confundir esse resumo com estrutura tática completa. Prioridade: P1/P2. Ordem: 4. Fonte/contrato: CNTR-DB-010, CNTR-DB-012. Relação: deriva das atletas disponíveis e alimenta B5.

B5 — COBERTURA TÁTICA.

Propósito: indicar cobertura/insuficiência por sistema/posição somente quando os dados permitirem. Prioridade: P2/PC. Ordem: 5. Fonte/contrato: CNTR-DB-012, CNTR-DB-013. Visibilidade: TREINADOR\_INTERNO. Relação: depende de B3/B4. Ação: leitura/inspeção.

B6 — CONTEÚDO DO TREINO E STATUS DE PUBLICAÇÃO.

Propósito: separar o conteúdo técnico interno do que está publicado para atleta. Prioridade: P2. Ordem: 6. Fonte/contrato: CNTR-DB-007, CNTR-AGO-002, CNTR-PESQ-004, CNTR-X-001. Visibilidade: TREINADOR\_INTERNO, com indicação explícita do que é publicável. Ação: consulta; G4 não presume edição.

B7 — HISTÓRICO RECENTE RELACIONADO.

Propósito: dar referência pontual sem deslocar a operação do treino atual. Prioridade: P3. Ordem: 7. Fonte/contrato: treinos/eventos anteriores. Ação: abrir histórico quando existir necessidade.

Decisão COACH-DEC-03 — Organizar a lista nominal por resposta ou por função.

Explicação: a pergunta operacional inicial é “quem vai?”, enquanto a pergunta seguinte é “qual composição tenho?”. Impacto UX: agrupar primeiro por função dificulta localizar pendências; agrupar por resposta facilita ação e a composição fica resolvida em bloco próprio. Recomendação: padrão por status de disponibilidade, com filtro/alternância por função se necessário.

Decisão COACH-DEC-04 — Exibir cobertura tática sempre.

Explicação: cobertura depende de dados suficientes e não pode ser inferida. Impacto UX: um painel tático vazio/indeterminado ocupa espaço e pode sugerir problema inexistente. Recomendação: B5 é condicional; exibir quando a fonte sustentar avaliação e usar estado “indeterminado” apenas quando isso for operacionalmente útil.

Decisão COACH-DEC-05 — Misturar plano técnico e composição no topo.

Explicação: composição responde à disponibilidade; conteúdo responde ao planejamento. Impacto UX: misturar os domínios aumenta carga cognitiva. Recomendação: manter B2–B5 como cadeia operacional de composição e B6 como bloco técnico separado.

### COACH-G4-03 — AGENDA | deriva de COACH-G3-03

B1 — PERÍODO / NAVEGAÇÃO TEMPORAL.

Propósito: orientar data/intervalo. Prioridade: P1. Ordem: 1. Fonte/contrato: CNTR-GLOSS-010. Ação: mudar período.

B2 — EVENTOS E COMPROMISSOS.

Propósito: listar treinos e competições por evento\_id, inclusive múltiplos eventos no mesmo dia. Prioridade: P1. Ordem: 2. Fonte/contrato: CNTR-DB-002, CNTR-X-002. Visibilidade: TREINADOR\_INTERNO. Ação: abrir evento.

B3 — PRAZOS / PENDÊNCIAS OPERACIONAIS.

Propósito: mostrar inscrição, lista nominal, criticidade e ação necessária ligadas ao tempo. Prioridade: P0/P1 quando próximos; P2 nos demais casos. Ordem: intercalada cronologicamente ou associada ao evento correspondente. Fonte/contrato: CNTR-AGO-001. Relação: abre COACH-G4-08 ou contexto aplicável.

B4 — FILTRO DE DOMÍNIO.

Propósito: reduzir densidade quando necessário sem ocultar o conjunto por padrão. Prioridade: P2. Ordem: antes de B2 quando a agenda crescer. Fonte: tipo de evento/compromisso. Ação: filtrar treinos/competições/prazos.

Decisão COACH-DEC-06 — Calendário visual versus agenda operacional.

Explicação: o treinador precisa ver horários, prazos e pendências, não apenas ocupação de dias. Impacto UX: calendário mensal dá visão panorâmica, mas comprime informações críticas no mobile. Recomendação: lista/agenda temporal como padrão; uma visão calendário pode ser adicionada como modo secundário após validação de necessidade.

### COACH-G4-04 — EQUIPE | deriva de COACH-G3-04

B1 — BUSCA/FILTROS DO ELENCO.

Propósito: localizar rapidamente atleta ou subconjunto por função/posição/estado de vínculo. Prioridade: P1/P2 conforme tamanho do elenco. Ordem: 1. Fonte/contrato: atletas/vínculos; CNTR-GLOSS-003, CNTR-DB-010, CNTR-DB-012. Ação: buscar/filtrar.

B2 — LISTA DE ATLETAS ATIVAS.

Propósito: apresentar o elenco atual com identidade esportiva essencial. Prioridade: P1. Ordem: 2. Fonte/contrato: atletas + vínculo temporal; CNTR-GLOSS-003. Visibilidade: TREINADOR\_INTERNO. Relação: abre COACH-G4-05.

B3 — ESTRUTURA POR FUNÇÃO/POSIÇÃO. Propósito: permitir leitura da distribuição do elenco sem transformar contagens em categorias mutuamente exclusivas quando não forem. Prioridade: P2. Ordem: 3 ou filtro derivado de B1/B2. Fonte/contrato: CNTR-DB-010, CNTR-DB-012. Ação: filtrar.

B4 — FREQUÊNCIA/PRESENÇA FACTUAL CONSOLIDADA.

Propósito: disponibilizar indicador somente quando sustentado pelo domínio de presença. Prioridade: P3/PC. Ordem: 4. Fonte/contrato: CNTR-DB-004, CNTR-GLOSS-005. Visibilidade: treinador. Relação: não deriva de disponibilidade.

Decisão COACH-DEC-07 — Ordenação padrão do elenco.

Explicação: por função ajuda análise de composição; alfabética ajuda encontrar uma atleta. Impacto UX: agrupamento fixo por função pode tornar a busca nominal lenta. Recomendação: ordem alfabética como padrão com filtros por função/posição; permitir agrupamento por função se a Seção 7 validar necessidade frequente.

Decisão COACH-DEC-08 — Exibir frequência como coluna/indicador padrão.

Explicação: presença factual ainda pode não estar consolidada. Impacto UX: um campo vazio ou derivado de disponibilidade cria falsa precisão. Recomendação: B4 somente quando o dado factual estiver consolidado; caso contrário, não ocupar espaço estrutural na lista.

### COACH-G4-05 — DETALHE DA ATLETA | deriva de COACH-G3-05

B1 — IDENTIDADE ESPORTIVA E VÍNCULO.

Propósito: confirmar atleta e estado do vínculo. Prioridade: P1. Ordem: 1. Fonte/contrato: CNTR-GLOSS-002, CNTR-GLOSS-003. Visibilidade: TREINADOR\_INTERNO.

B2 — FUNÇÃO, POSIÇÃO PRINCIPAL E POSIÇÕES SECUNDÁRIAS.

Propósito: representar o papel esportivo/tático sem forçar classificação inexistente. Prioridade: P1/P2. Ordem: 2. Fonte/contrato: CNTR-DB-010, CNTR-DB-012. Visibilidade: treinador.

B3 — PRESENÇA/FREQUÊNCIA FACTUAL.

Propósito: consultar histórico consolidado de presença quando houver fonte válida. Prioridade: P2/PC. Ordem: 3. Fonte/contrato: CNTR-DB-004, CNTR-GLOSS-005. Visibilidade: treinador. Relação: independente de disponibilidade futura.

B4 — LIMITES DE PRIVACIDADE.

Propósito normativo: Wellness, Autoavaliação e questionários sensíveis não entram nesta tela na V1. Prioridade: não renderizar. Fonte/contrato: CNTR-WELL-001, CNTR-WELL-002, CNTR-AUTO-003, CNTR-QCOMP-004.

Decisão COACH-DEC-09 — Transformar detalhe da atleta em “perfil 360°”.

Explicação: existem outros domínios individuais sensíveis, mas estão fora da V1 e possuem autorização própria. Impacto UX/segurança: concentrar tudo num perfil aumenta risco de exposição e cria expectativa de interpretação integrada não definida. Recomendação: manter detalhe estritamente esportivo/operacional na V1.

### COACH-G4-06 — MAIS | deriva de COACH-G3-06

B1 — DESTINOS OPERACIONAIS SECUNDÁRIOS. Propósito: acessar Competições, Resultados e Qualidade sem competir com a navegação diária. Prioridade: P1. Ordem: 1. Fonte: mapa de navegação/autorização. Visibilidade: treinador. Ação: navegar.

B2 — CONTA E SESSÃO. Propósito: acesso a senha/logout e informações básicas de conta. Prioridade: P2. Ordem: 2. Fonte: autenticação. Ação: redefinir senha/logout.

B3 — MÓDULOS FUTUROS. Propósito normativo: não criar atalhos inativos para Wellness, Autoavaliação, Pesquisa de Horários, Questionários ou Feedback apenas para “preencher” o menu. Prioridade: não renderizar até habilitação formal. Fonte/contrato: CNTR-X-007.

Decisão COACH-DEC-10 — “Mais” como mini-dashboard ou hub puro de navegação. Explicação: replicar métricas aqui duplicaria Central/Resultados/Qualidade. Impacto UX: duplicação gera dúvida sobre qual tela é autoritativa. Recomendação: manter “Mais” como hub simples de destinos e conta.

### COACH-G4-07 — COMPETIÇÕES | deriva de COACH-G3-07

B1 — COMPETIÇÕES ATIVAS/PRÓXIMAS.

Propósito: apresentar compromissos competitivos relevantes e seu estado operacional. Prioridade: P1. Ordem: 1. Fonte/contrato: CNTR-DB-008, CNTR-X-002. Ação: abrir competição.

B2 — PRAZOS E PENDÊNCIAS.

Propósito: destacar inscrição, lista nominal, confirmação e ações necessárias. Prioridade: P0/P1. Ordem: associado a B1 e pode preceder informação descritiva do item. Fonte/contrato: CNTR-AGO-001. Ação: abrir detalhe/contexto.

B3 — ESTADO DE PARTICIPAÇÃO CEPRAEA.

Propósito: diferenciar confirmado, classificado, convidado/a confirmar, não participa etc. Prioridade: P1/P2. Fonte/contrato: CNTR-DB-008, CNTR-X-003. Ação: leitura/detalhe.

B4 — COMPETIÇÕES REALIZADAS / HISTÓRICO.

Propósito: acesso a campanhas anteriores. Prioridade: P3. Ordem: 2. Fonte/contrato: jogos/resultados validados. Ação: abrir detalhe.

Decisão COACH-DEC-11 — Cronologia ou pendência como eixo principal.

Explicação: o treinador precisa agir sobre prazos mesmo quando outra competição é cronologicamente mais próxima. Impacto UX: cronologia pura pode esconder uma lista nominal vencendo antes. Recomendação: manter seções cronológicas, mas elevar pendências/próximos prazos dentro de cada competição e na Central.

### COACH-G4-08 — DETALHE DA COMPETIÇÃO | deriva de COACH-G3-08

B1 — IDENTIDADE / PARTICIPAÇÃO / ESTADO.

Propósito: estabelecer competição e situação operacional do CEPRAEA. Prioridade: P1. Ordem: 1. Fonte/contrato: CNTR-DB-008, CNTR-X-002.

B2 — PRAZOS E AÇÕES NECESSÁRIAS.

Propósito: tornar explícito o que precisa ser resolvido antes da competição. Prioridade: P0 antes do evento quando houver pendência. Ordem: 2 no pré. Fonte/contrato: CNTR-AGO-001. Ação: consultar/operar apenas se existir permissão V1 definida; G4 não presume edição.

B3 — CONVOCAÇÃO / LISTA NOMINAL.

Propósito: consultar quem está convocada e estado da lista sem confundir com participação em jogo. Prioridade: P1. Ordem: 3 no pré; P2 durante/depois. Fonte/contrato: CNTR-DB-011. Visibilidade: TREINADOR\_INTERNO. Ação: consulta; qualquer escrita exige contrato futuro/específico.

B4 — PROGRAMAÇÃO / PRÓXIMO JOGO.

Propósito: organizar jogos e, durante a competição, tornar próximo jogo/fase o centro operacional. Prioridade: P2 antes; P0 durante. Ordem: 4 antes; 2 durante. Fonte/contrato: CNTR-DB-016, CNTR-DB-017, CNTR-AGO-005.

B5 — ÚLTIMO RESULTADO / CAMPANHA.

Propósito: manter estado esportivo atual e pós-evento. Prioridade: P3 antes; P1 durante; P1 no pós. Fonte/contrato: CNTR-DB-016, CNTR-AGO-006, CNTR-AGO-007. Ação: abrir Resultados.

B6 — PENDÊNCIAS DE DADOS RELACIONADAS.

Propósito: indicar resultado/segmento incompleto ou conflito que afete a operação, sem misturar toda a área de qualidade. Prioridade: P0 se bloqueante, PC nos demais casos. Fonte/contrato: CNTR-X-005, CNTR-AGO-008. Relação: abre COACH-G4-10.

Decisão COACH-DEC-12 — Ordem fixa ou modo operacional contextual.

Explicação: antes, durante e depois da competição exigem tarefas diferentes. Impacto UX: ordem fixa reduz velocidade no Dia do Jogo e mantém prazos vencidos ocupando topo. Recomendação: reordenar os mesmos blocos por contexto; regras de gatilho ficam na Seção 6.

Decisão COACH-DEC-13 — Incluir edição de convocação/resultado no desenho G4.

Explicação: o Roadmap atual garante consulta/operação geral, mas não especifica contratos de escrita dessas entidades na V1. Impacto UX/produto: desenhar botões de edição agora cria requisito não aprovado e riscos de auditoria. Recomendação: NÃO presumir escrita; desenhar hierarquia de consulta e reservar ações mutáveis somente quando contratos e APIs forem formalizados.

### COACH-G4-09 — RESULTADOS | deriva de COACH-G3-09

#### **B1 — RESUMO DA CAMPANHA VALIDADA.**

-   Propósito: responder rapidamente jogos, vitórias, derrotas, aproveitamento, sets e shoot-outs com dados canônicos.
-   Prioridade: P1.
-   Ordem: 1.
-   Fonte/contrato: CNTR-DB-016, CNTR-AGO-007.
-   Visibilidade: TREINADOR\_INTERNO.

#### **B2 — FILTROS DE ANÁLISE.**

Propósito: alternar competição e adversário estável sem criar agregações ambíguas. Prioridade: P1/P2. Ordem: 2. Fonte/contrato: CNTR-DB-017, CNTR-AGO-006. Ação: filtrar.

#### **B3 — QUEBRA POR COMPETIÇÃO/ADVERSÁRIO.**

Propósito: comparar campanhas e recorrência contra adversários. Prioridade: P1/P2. Ordem: 3. Fonte/contrato: CNTR-AGO-006, CNTR-DB-017. Ação: expandir/selecionar.

#### **B4 — LISTA DE JOGOS E SEGMENTOS.**

-   Propósito: permitir rastreabilidade até partidas individuais e identificar dados incompletos. Prioridade: P2.
-   Ordem: 4.
-   Fonte/contrato: CNTR-DB-016, CNTR-AGO-007.
-   Ação: consultar jogo/detalhe quando definido.

#### **B5 — QUALIDADE / DADOS INCOMPLETOS.**

-   Propósito: marcar parciais/segmentos ausentes sem contaminar métricas como se fossem completos.
-   Prioridade: PC/P0 se comprometer a leitura.
-   Fonte/contrato: CNTR-DB-016, CNTR-X-005.
-   Relação: abre COACH-G4-10.

#### **Decisão COACH-DEC-14 — Gráficos como linguagem principal ou análise compacta.**

-   Explicação: o domínio atual é pequeno e operacional; gráficos decorativos podem ocupar mais espaço que listas/metric strips.
-   Impacto UX: gráficos ajudam tendência, mas prejudicam densidade quando não respondem a uma pergunta concreta.
-   Recomendação: começar com resumo compacto + filtros + listas/tabelas mobile; adicionar gráfico somente para uma pergunta analítica definida.

#### **Decisão COACH-DEC-15 — Exibir participação individual agora.**

-   Explicação: a fonte individual ainda possui inconsistências e o contrato de produto não a inclui na V1.
-   Impacto UX/dados: números individuais inconsistentes geram decisões erradas.
-   Recomendação: NÃO incluir bloco individual enquanto a base não estiver reconciliada e um contrato explícito for aprovado.

### COACH-G4-10 — QUALIDADE DOS DADOS | deriva de COACH-G3-10

#### **B1 — RESUMO POR SEVERIDADE/IMPACTO.**

Propósito: distinguir bloqueante, atenção e informativo sem transformar qualquer ausência em erro. Prioridade: P1. Ordem: 1. Fonte/contrato: CNTR-X-003, CNTR-X-005, CNTR-AGO-008.

#### **B2 — FILA DE PENDÊNCIAS TÉCNICAS.**

-   Propósito: listar IDs ausentes/duplicados, conflito de fonte, sincronização, resultado incompleto e regressões.
-   Prioridade: P0/P1 conforme impacto.
-   Ordem: 2.
-   Fonte/contrato: CNTR-AGO-008, CNTR-X-005.
-   Ação: abrir contexto afetado quando houver destino seguro.

#### **B3 — COBERTURA DE COLETA.**

Propósito: separar “faltam respostas/dados coletados” de erro técnico do sistema. Prioridade: P2. Ordem: 3. Fonte/contrato: CNTR-QCOMP-005 como princípio de distinção e CNTR-X-003; aplicar apenas aos domínios V1 pertinentes. Ação: consultar.

#### **B4 — CONTEXTO/RASTREABILIDADE.**

Propósito: mostrar entidade afetada, fonte esperada e caminho até o domínio correspondente sem expor segredos. Prioridade: P2. Ordem: após cada item ou detalhe. Fonte/contrato: CNTR-GLOSS-006, CNTR-AGO-008. Ação: navegar.

#### **B5 — ESTADO SEM PENDÊNCIAS.**

Propósito: comunicar integridade atual sem inventar indicadores. Prioridade: PC. Fonte/contrato: CNTR-DB-009, CNTR-X-003. Ação: nenhuma.

#### **Decisão COACH-DEC-16 — Qualidade dentro da Central ou área própria.**

Explicação: problemas críticos precisam ser visíveis na Central, mas a análise completa é especializada. Impacto UX: inserir todos os erros na Central gera ruído; esconder tudo na área própria atrasa percepção de falhas bloqueantes. Recomendação: Central recebe apenas alerta/resumo acionável; diagnóstico completo permanece nesta tela.

#### **Decisão COACH-DEC-17 — Misturar coleta incompleta com erro técnico.**

Explicação: poucas respostas podem ser um fato operacional, enquanto duplicidade/sincronização é falha do sistema.

Impacto UX: misturar os dois aumenta falsa urgência e dificulta priorização.

Recomendação: manter B2 e B3 semanticamente separados.

## DECISÕES TRANSVERSAIS G4

#### **G4-DEC-T01 — Quantidade de informação por primeira dobra.**

-   **Explicação:** mobile exige priorização, mas “primeira dobra” varia por dispositivo e não pode virar limite rígido de cards.
-   **Impacto UX:** projetar por quantidade fixa de containers recria o padrão genérico já rejeitado.
-   **Recomendação:** usar prioridade P0/P1 para garantir que a pergunta central e a ação principal apareçam antes de conteúdo P2/P3, sem fixar número de cards.

#### **G4-DEC-T02 — Resumo versus duplicação.**

-   **Explicação:** Home/Central podem resumir informações existentes em detalhes.
-   **Impacto UX:** repetir listas completas em vários lugares aumenta inconsistência e rolagem.
-   **Recomendação:** resumo sempre aponta para fonte/detalhe e contém apenas informação suficiente para decidir navegar ou agir.

#### **G4-DEC-T03 — Estado ausente versus bloco vazio.**

-   **Explicação:** alguns domínios podem não possuir dados canônicos.
-   **Impacto UX:** placeholders repetidos fazem o produto parecer incompleto e desviam atenção.
-   **Recomendação:** ocultar bloco opcional quando sua ausência não exige explicação; usar empty state quando a ausência muda a compreensão ou oferece próxima ação.

#### **G4-DEC-T04 — Navegação e ação no mesmo item.**

-   **Explicação:** disponibilidade, filtros e abertura de detalhe podem coexistir.
-   **Impacto UX:** múltiplos alvos em linha pequena aumentam toque acidental.
-   **Recomendação:** G4 mantém uma ação principal por bloco; G5 deve especificar secondary actions e áreas de toque sem ambiguidade.

#### **G4-DEC-T05 — Hierarquia contextual.**

-   **Explicação:** competição altera prioridade do mesmo conjunto de informações.
-   **Impacto UX:** criar Homes paralelas quebra memória espacial; não adaptar prioridade prejudica velocidade no Dia do Jogo.
-   **Recomendação:** manter identidade das telas e reordenar/promover blocos existentes. A Seção 6 definirá gatilhos e matriz de prioridade por contexto.

#### **G4-DEC-T06 — Dado técnico versus linguagem humana**

-   **Explicação:** IDs e códigos sustentam integridade, mas não são rótulos principais de interface.
-   **Impacto UX:** mostrar IDs/DB\_\* aumenta carga e aparência administrativa.
-   **Recomendação:** usar IDs somente para vínculo e diagnóstico interno; interface humana usa nomes, datas e estados sem perder rastreabilidade.

#### **G4-DEC-T07 — Indicador agregado versus interpretação.**

-   **Explicação:** contagens e métricas podem ser corretas sem autorizar inferência causal/tática.
-   **Impacto UX:** indicadores com aparência conclusiva podem induzir decisão indevida.
-   **Recomendação:** apresentar fatos canônicos; cobertura tática, presença e qualidade só recebem interpretação quando o contrato correspondente permitir.

## MATRIZ DE ORDEM G4 — RESUMO

### ATLETA

-   ATH-G4-01 Início: ação/próximo compromisso → competição/situação pessoal → agenda próxima → resultado/campanha.
-   ATH-G4-02 Agenda: período → timeline de eventos → estado/minha ação contextual → empty/error quando aplicável.
-   ATH-G4-03 Treinos: controle temporal → próximos treinos → histórico.
-   ATH-G4-04 Detalhe do Treino: identidade → minha disponibilidade → plano publicado → estados de encerramento/indisponibilidade.
-   ATH-G4-05 Competições: atuais/próximas relevantes + estado de participação → histórico.
-   ATH-G4-06 Detalhe da Competição: identidade → convocação/programação/resultados reordenados por contexto → qualidade pública quando necessária.
-   ATH-G4-07 Perfil: identidade → perfil esportivo → segurança/sessão.

### TREINADOR

-   COACH-G4-01 Central: atenção operacional → próximo treino + disponibilidade/composição → competição/prazo → resultado → qualidade crítica.
-   COACH-G4-02 Treino: identidade → distribuição → lista nominal → composição → cobertura tática → conteúdo → histórico.
-   COACH-G4-03 Agenda: período → eventos → prazos/pendências → filtros.
-   COACH-G4-04 Equipe: busca/filtros → elenco → estrutura por função → frequência factual quando consolidada.
-   COACH-G4-05 Detalhe da Atleta: identidade/vínculo → função/posições → presença factual quando consolidada.
-   COACH-G4-06 Mais: destinos secundários → conta/sessão.
-   COACH-G4-07 Competições: próximas/ativas → prazos → participação → histórico.
-   COACH-G4-08 Detalhe da Competição: identidade → prazos/convocação/programação/resultados reordenados por contexto → qualidade relacionada.
-   COACH-G4-09 Resultados: resumo → filtros → quebra por competição/adversário → jogos/segmentos → qualidade.
-   COACH-G4-10 Qualidade: severidade → pendências técnicas → cobertura de coleta → rastreabilidade → estado sem pendências.

## GATE DE SAÍDA — SEÇÃO 2 / G4

A Hierarquia de Informação atinge G4 quando cada tela ATH-G3-\* e COACH-G3-\* possui blocos funcionais explícitos, ordem e prioridade relativas, fonte/contrato, visibilidade, relação e ação; quando as decisões de hierarquia relevantes estão registradas com explicação, impacto UX e recomendação; e quando nenhum bloco depende de convenção visual, inferência de dado ausente ou exposição indevida. Status desta execução: G4 ESPECIFICADO PARA ATLETA E TREINADOR. Próxima dependência: Seção 6 — Estado da competição/contexto operacional, para transformar as recomendações contextuais em matriz de gatilhos e prioridade G3/G4; depois, Seção 7 — contratos G5 das telas críticas.

## 3\. Só então abrimos direções visuais

E desta vez eu **não faria variações da mesma tela**.

Criar quatro sistemas visuais realmente distintos usando **as mesmas funcionalidades**.

Por exemplo:

**A — Technical Court  
**Interface técnica inspirada em quadra, linhas, marcações, organização tática. Grafite, areia, branco, verde controlado. Tipografia condensada esportiva. Quase nenhum card tradicional.

**B — Beach Editorial  
**Muito espaço, fotografia/texture apenas quando pertinente, areia, branco quente, preto, azul oceano. Tipografia editorial forte. Mais artístico e premium.

**C — Team Operations  
**Mais sóbrio e operacional. Listas, status, blocos densos, divisores, tabelas mobile e navegação técnica. Para o treinador pode lembrar uma central de equipe profissional, não um fitness tracker.

**D — Modern Collective Sport  
**Mais contemporâneo, tipografia grande, composição assimétrica, superfícies geométricas e identidade esportiva própria. Mais arrojado sem virar gaming/neon.

O importante é que seriam **quatro arquiteturas visuais**, não quatro paletas aplicadas ao mesmo template.

# EXECUÇÃO G4 VISUAL — DIREÇÕES VISUAIS

## 

## Escopo, invariantes e regra de comparação

Esta execução desenvolve quatro Direções Visuais em G4 visual sobre a mesma arquitetura G3, a mesma hierarquia funcional G4, os mesmos contextos G3/G4 e os mesmos contratos G5. Nenhuma direção pode criar, remover, renomear ou reordenar funcionalmente telas, blocos, ações, permissões, prioridades ou estados para tornar sua estética mais conveniente. A diferença deve acontecer na composição, no ritmo, nas superfícies, na navegação visual, na densidade, na relação entre texto e dado e na linguagem gráfica.

Regra de equivalência: quando duas direções forem comparadas, o conteúdo textual, o dado canônico, o evento/competição selecionado, o perfil autorizado, o contexto ROTINA/PRÉ-COMPETIÇÃO/DIA DO JOGO/PÓS-ETAPA, a prioridade P0–P3/PC e o estado G5 devem ser idênticos. Se uma direção parecer melhor apenas porque recebeu menos conteúdo, mais informação ou outra tarefa, a comparação é inválida.

Regra de distinção: cada direção precisa continuar reconhecível sem depender da cor. Em teste monocromático, devem permanecer perceptíveis diferenças de estrutura, proporção, ritmo, navegação, densidade, divisores, uso de espaço, tratamento de listas, hierarquia tipográfica futura e comportamento das superfícies.

Regra de parada G4 visual: esta seção define gramática de composição e comportamento visual, mas não fecha família tipográfica, pesos, tamanhos, cores exatas, radius, stroke, grid atômico, ícones finais nem motion tokens. Esses elementos pertencem ao G6.

### Contrato visual comum às quatro direções

ARQUITETURA E CONTEÚDO INVARIÁVEIS — ATLETA mantém INÍCIO, AGENDA, COMPETIÇÕES e PERFIL como destinos primários, com TREINOS e detalhes como destinos secundários. TREINADOR mantém CENTRAL, TREINO, AGENDA, EQUIPE e MAIS como destinos primários, com Competições, Resultados, Qualidade e detalhes conforme G3. Nenhuma direção introduz nova rota porque “combina melhor” com a estética.

As telas mantêm exatamente os blocos G4 já definidos. ATH-G4-01 continua com próximo compromisso/ação pendente, próxima competição/situação pessoal, agenda próxima e último resultado/campanha. COACH-G4-01 continua com fila de atenção, próximo treino, disponibilidade, composição, competição/prazo, resultado e qualidade. O mesmo princípio vale para as demais 15 telas.

P0 deve dominar cognitivamente em qualquer direção. P1 organiza o contexto principal; P2 sustenta decisão; P3 permanece referência; PC só aparece quando o contrato permitir. A direção visual pode mudar posição espacial, largura, forma de agrupamento e densidade, mas não pode transformar P3 em protagonista ou esconder P0.

ESTADOS E FEEDBACK INVARIÁVEIS — LOADING, VAZIO, ERRO, OFFLINE, PENDÊNCIA, SUCESSO e INDISPONIBILIDADE conservam a semântica G5. As direções podem representar esses estados com linguagens diferentes, mas não podem alterar o que cada estado significa. Sucesso de escrita continua dependendo de confirmação canônica do servidor; offline continua sem fila silenciosa de escrita; indisponibilidade continua sem affordance falsa.

Falhas localizadas permanecem localizadas visualmente sempre que identidade e autorização da tela forem confiáveis. Nenhuma direção usa erro de página inteira por convenção quando apenas um bloco falhou.

RELAÇÃO ATLETA × TREINADOR — As duas experiências compartilham identidade de produto, mas não precisam compartilhar a mesma densidade. A experiência ATLETA privilegia leitura rápida, ação própria e orientação temporal. A experiência TREINADOR pode ser mais densa, comparativa e operacional. A direção escolhida deve possuir uma variação coerente para cada perfil sem virar dois produtos desconectados.

NAVEGAÇÃO VISUAL — A arquitetura permanece a mesma, mas sua expressão visual pode variar. No mobile, destinos primários continuam acessíveis sem exigir menu profundo. Em larguras maiores, o treinador pode receber expressão lateral/rail como adaptação responsiva, desde que isso não crie destinos nem altere autorização. A atleta continua mobile-first e não herda aparência de painel administrativo desktop.

IMAGEM, TEXTURA E IDENTIDADE ESPORTIVA — Imagem, textura de areia, linhas de quadra, marcações ou elementos gráficos só reforçam contexto; nunca substituem informação, estado ou ação. Fotografias só entram quando forem próprias/pertinentes e quando não reduzirem legibilidade. Nenhuma direção depende de fotografia decorativa de corrida, academia, wellness ou esporte genérico para parecer esportiva.

ANTIPADRÕES PROIBIDOS — roxo dominante por inércia; neon/glow constante; grade uniforme de cards arredondados; ícones genéricos de fitness como linguagem principal; números sem função decisória; gauges decorativos; fotografia de corrida; visual gaming; containers vazios apenas para preencher espaço; repetição integral da mesma informação em Home e detalhe.

## DIREÇÃO A — TECHNICAL COURT

IDEIA CENTRAL — Transformar a lógica espacial da quadra de beach handball em gramática de interface: linhas, zonas, eixos, áreas de decisão e relações entre blocos. A interface parece construída sobre um campo operacional, não sobre uma pilha de cartões. O repertório visual comunica precisão esportiva, leitura tática e disciplina de equipe.

COMPOSIÇÃO — Predominantemente ortogonal e aberta. Blocos P0/P1 ocupam zonas claras do campo visual, separados por linhas, mudanças de plano ou recortes de área em vez de containers arredondados repetidos. Informações relacionadas podem compartilhar uma mesma zona contínua; dados secundários alinham-se a bordas, eixos ou faixas laterais.

Na ATLETA, o próximo compromisso forma a zona principal, com disponibilidade integrada ao mesmo evento; agenda e competição aparecem como continuidade espacial, não como cartões independentes. No TREINADOR, Central e Treino usam uma malha modular semelhante a uma prancheta tática: atenção, disponibilidade nominal e composição se conectam por eixos visuais.

RITMO E DENSIDADE — Mais compacto no treinador e moderado na atleta. Espaços grandes separam fases decisórias, não funcionam como luxo editorial. Repetição ocorre por alinhamento e marcação de campo, não por caixas iguais. Números operacionais ganham escala somente quando respondem a uma pergunta real, como distribuição de disponibilidade ou placar.

SUPERFÍCIES E CONTRASTE — Predominam superfícies abertas e planas, com contraste entre fundo, faixas de operação e zonas de destaque. O campo cromático sugerido é grafite/areia/off-white com acento esportivo controlado, sem fixar tokens. Bordas e linhas têm função estrutural: eixo, separação, progresso ou agrupamento, nunca decoração.

NAVEGAÇÃO VISUAL — Comporta-se como borda funcional da quadra. No mobile, destinos primários aparecem em barra linear baixa, com seleção marcada por posição/linha e rótulo claro em vez de ícones soltos. No treinador em telas maiores, a mesma lógica pode se expandir para rail lateral técnico, mantendo as mesmas rotas. Voltar, aprofundar e filtrar parecem deslocamentos entre zonas, não mudanças de aplicativo.

LISTAS, AGENDA E TIMELINE — Agenda usa eixo temporal explícito, com eventos ancorados em linha/faixa longitudinal. Múltiplos eventos no mesmo dia compartilham a mesma marca temporal sem sobreposição. Listas nominais usam linhas firmes, agrupamento por status e leitura rápida de função/posição; divisores substituem cards individuais.

TREINO E COMPOSIÇÃO — No Detalhe do Treino da atleta, identidade do evento fixa o topo; disponibilidade entra como área de decisão conectada; plano publicado ocupa zona técnica abaixo. No treinador, distribuição → lista nominal → composição → cobertura tática forma cadeia espacial contínua. Cobertura tática, quando válida, pode usar representação abstrata de quadra/zonas, sem virar diagrama decorativo.

COMPETIÇÃO, PLACAR E DIA DO JOGO — No DIA DO JOGO, faixas fortes de programação e placar tornam próximo jogo o eixo dominante e último resultado seu apoio imediato. Placar é tipográfico e estrutural, evitando cards de estatística. No PRÉ, convocação/prazos ocupam zonas de preparação; no PÓS, campanha e resultado assumem o centro sem alterar a estrutura base.

ESTADOS G5 — Loading preserva linhas e zonas sem números fictícios. Vazio deixa a zona aberta com mensagem funcional curta. Erro rompe localmente a linha/faixa do domínio afetado. Offline mantém a superfície estável com indicação de snapshot. Pendência ganha precedência espacial. Sucesso se estabiliza no próprio eixo sem celebração invasiva. Indisponibilidade transforma área mutável em leitura ou remove-a, sem botão ativo.

ASSINATURA E RISCO — Precisão, quadra, alinhamento, técnica e leitura operacional. Risco: virar interface excessivamente militar/tática ou densa. Controle: usar geometria de quadra como estrutura abstrata, não como tema literal em toda tela, e preservar maior respiro na experiência da atleta.

APLICAÇÃO POR FAMÍLIAS — Home/Central: zonas de decisão conectadas. Agenda: eixo temporal. Treino: cadeia operacional. Competições: faixa de estado + cronologia. Detalhe de competição: programação/placar em linhas de jogo. Equipe: lista técnica com filtros. Resultados/Qualidade: tabelas e faixas diagnósticas. Perfil/Mais: composição simplificada com a mesma linguagem de eixos.

## DIREÇÃO B — BEACH EDITORIAL

IDEIA CENTRAL — Tratar o produto como publicação esportiva contemporânea e premium ligada ao ambiente da praia: grande hierarquia de informação, espaço negativo, ritmo de leitura, títulos fortes, regras editoriais e materialidade sutil. A interface pertence a uma equipe de beach handball, não a um app de wellness.

COMPOSIÇÃO — Vertical, narrativa e menos containerizada. Cada tela possui abertura editorial que responde à pergunta central e conduz a blocos separados por ritmo, títulos, filetes e mudanças de largura. Informações podem ocupar a largura inteira ou formar pares assimétricos; não há obrigação de alinhar tudo em grade de cards.

Na ATLETA, Início pode abrir com data/compromisso em grande escala, seguido por faixa de disponibilidade e sequência editorial de competição, agenda e resultado. No TREINADOR, Central usa abertura de atenção + seções operacionais densas abaixo, sem transformar a experiência inteira em revista.

RITMO E DENSIDADE — Mais arejado, alternando grandes pausas e trechos densos. A atleta recebe mais respiro e leitura de uma mão; o treinador preserva densidade em listas e tabelas com hierarquia editorial clara. Espaço vazio é parte da composição e não precisa ser preenchido por métricas.

SUPERFÍCIES E CONTRASTE — Superfícies tendem a papel/tela aberta, com poucas áreas fechadas. O campo cromático sugerido combina branco quente/areia, tinta escura, azul oceano ou verde controlado como acento, sem tokens fixos. Textura de areia, horizonte ou sombra pode aparecer de forma extremamente sutil e contextual; nunca como ruído atrás de texto.

NAVEGAÇÃO VISUAL — Tipográfica e discreta. No mobile, destinos primários funcionam como índice inferior de rótulos claros, com seleção indicada por peso, sublinhado ou régua, não por bolhas. Cabeçalhos de detalhe usam retorno e título como parte do fluxo editorial. No treinador em telas maiores, índice lateral leve pode substituir a barra inferior sem adquirir aparência de template administrativo.

LISTAS, AGENDA E TIMELINE — Agenda se comporta como agenda editorial: data como marco, eventos em sequência com hierarquia de horário, título, local e estado. Listas não precisam de bordas completas; filetes e alinhamento tipográfico organizam. Múltiplos eventos no mesmo dia são entradas sob o mesmo cabeçalho temporal.

TREINO E COMPOSIÇÃO — No treino da atleta, evento é apresentado como briefing de edição: quando/onde, ação de disponibilidade, depois plano publicado em linguagem de leitura. No treinador, composição e disponibilidade aparecem como seção técnica dentro da narrativa, usando listas, colunas e números editoriais; o estilo não pode reduzir velocidade operacional.

COMPETIÇÃO, PLACAR E DIA DO JOGO — Competições funcionam como capítulos. PRÉ apresenta competição, situação e convocação como abertura; DIA DO JOGO transforma programação e placar em manchete esportiva funcional; PÓS promove campanha e desfecho. Placar pode ganhar grande escala tipográfica, com sets/shoot-out em linha de apoio, evitando visual de cassino ou placar eletrônico genérico.

ESTADOS G5 — Loading preserva estrutura editorial com linhas neutras e sem conteúdo inventado. Vazio usa espaço negativo + frase orientadora. Erro vira nota localizada no bloco, sem alarmismo. Offline integra “última atualização” ao cabeçalho/rodapé da seção. Pendência funciona como chamada editorial de ação. Sucesso é breve e silencioso no fluxo. Indisponibilidade remove conteúdo não publicável; quando a ausência exige explicação, usa nota neutra.

ASSINATURA E RISCO — Praia, clube, publicação esportiva, refinamento e personalidade. Risco: estética bonita porém lenta para o treinador ou dependente de fotografia. Controle: manter dados operacionais em estruturas compactas quando necessário e garantir que a direção funcione sem nenhuma fotografia.

APLICAÇÃO POR FAMÍLIAS — Home/Central: abertura editorial + seções. Agenda: agenda cronológica. Treino: briefing esportivo. Competições: capítulos/edições. Detalhe de competição: narrativa temporal PRÉ/JOGO/PÓS. Equipe: roster editorial. Resultados: caderno de campanha com números e listas. Qualidade: notas técnicas sóbrias. Perfil/Mais: índice limpo e identidade esportiva.

## DIREÇÃO C — TEAM OPERATIONS

IDEIA CENTRAL — Assumir explicitamente o CEPRAEA como sistema operacional de equipe. A linguagem privilegia velocidade, densidade, rastreabilidade, filas, estados e leitura comparativa. É a direção mais técnica para o treinador, mas sua versão ATLETA continua simples e direta, sem transformar a atleta em usuária de um ERP.

COMPOSIÇÃO — Usa painéis operacionais, listas compactas, faixas de status, seções colapsáveis quando justificadas e tabelas mobile responsivas. Containers existem quando ajudam escaneabilidade ou delimitam ação, mas não são todos iguais e não formam grade decorativa. O topo é reservado ao contexto e à decisão, seguido de dados de suporte.

Na ATLETA, a lógica é simplificada: faixa principal de próximo compromisso/ação, listas claras para agenda/competições e detalhes objetivos. No TREINADOR, Central funciona como fila de atenção + workspace do próximo treino, com módulos compactos e hierarquia operacional.

RITMO E DENSIDADE — Compacto, com menor espaçamento entre itens relacionados e maior densidade no treinador. A atleta mantém alvos de toque confortáveis e blocos menos densos. A hierarquia nasce de alinhamento, agrupamento, rótulos de estado e ordem, não de grandes áreas decorativas.

SUPERFÍCIES E CONTRASTE — Superfícies funcionais: plano-base, faixa de navegação, área de trabalho, cabeçalho de seção e linhas de lista. O campo cromático tende a neutros claros/escuros com acentos semânticos para estado, sem tokens. Contraste favorece uso prolongado e leitura de dados, evitando excesso simultâneo de cor.

NAVEGAÇÃO VISUAL — É a direção que mais aceita expressão de sidebar/rail no treinador em larguras maiores. No mobile, CENTRAL/TREINO/AGENDA/EQUIPE/MAIS permanecem em navegação persistente compacta; MAIS abre hub secundário. Na atleta, a navegação continua reduzida e leve. Navegação parece infraestrutura do produto, não elemento promocional.

LISTAS, AGENDA E TIMELINE — Listas são protagonistas. Agenda usa linhas operacionais com horário, tipo, título, status e eventual pendência. Equipe usa busca, filtros e roster denso. Treino usa grupos por SIM/TALVEZ/NAO/SEM\_RESPOSTA com acesso nominal. Resultados usam linhas/tabelas responsivas e filtros; Qualidade usa filas por severidade e domínio.

TREINO E COMPOSIÇÃO — No treinador, Detalhe do Treino é workspace: identidade fixa, distribuição resumida, lista nominal, composição, cobertura tática condicional, conteúdo técnico e histórico. Cada região tem função operacional clara. Na atleta, a mesma tela reduz-se ao evento, própria disponibilidade e conteúdo publicável, sem vestígios de controles internos.

COMPETIÇÃO, PLACAR E DIA DO JOGO — No PRÉ, prazos e convocação funcionam como checklist/fila de preparação; no DIA DO JOGO, programação e último resultado assumem faixa operacional de execução; no PÓS, campanha e qualidade de dados sobem. Placares são compactos, legíveis e associados ao estado do jogo, sem gauges.

ESTADOS G5 — Loading usa skeleton de linhas/painéis sem valores. Vazio mostra linha/área explícita “sem itens” quando zero é operacionalmente relevante. Erro fica localizado com retry. Offline usa barra persistente de sistema + snapshot identificado. Pendência vira item de fila com prioridade clara. Sucesso confirma inline e remove/reclassifica a pendência quando aplicável. Indisponibilidade desabilita controle apenas quando a razão precisa permanecer visível; caso contrário, oculta.

ASSINATURA E RISCO — Central profissional de equipe, controle, densidade e precisão. Risco: parecer SaaS administrativo genérico. Controle: incorporar linguagem específica de beach handball em nomes, estruturas de composição, quadra, roster, competição e iconografia futura; evitar componentes de template sem função esportiva.

APLICAÇÃO POR FAMÍLIAS — Home/Central: fila + workspace. Agenda: lista operacional. Treino: painel de composição nominal. Competições: lista com prazos/estado. Detalhe: workspace contextual. Equipe: roster pesquisável. Resultados: análise tabular compacta. Qualidade: central de incidentes/coleta. Perfil/Mais: utilitários simples.

## DIREÇÃO D — MODERN COLLECTIVE SPORT

IDEIA CENTRAL — Criar identidade esportiva contemporânea e própria para esporte coletivo: tipografia futura de alto impacto, assimetria controlada, superfícies geométricas, faixas de equipe, números fortes e relações de grupo. É mais ousada que as demais sem entrar em gaming, neon ou estética de treino individual.

COMPOSIÇÃO — Usa assimetria deliberada: blocos podem ocupar larguras diferentes, criar recortes, sobrepor faixas não textuais ou romper uma grade previsível, sempre preservando ordem de leitura e área de toque. P0 pode aparecer como grande superfície/placa de equipe; P1 e P2 formam sequências modulares com proporções variadas. Cards iguais deixam de ser unidade padrão.

Na ATLETA, Home combina grande marcador temporal com faixa de ação e módulos de competição/agenda de proporções diferentes. No TREINADOR, Central usa superfície dominante de atenção e grade assimétrica de contexto operacional, enquanto listas nominais e dados densos retornam a estruturas legíveis.

RITMO E DENSIDADE — Pulsado: alterna impacto e compressão. Grandes títulos/números funcionam como âncoras; listas e detalhes usam densidade controlada. O treinador recebe mais informação por área sem perder pontos de impacto; a atleta recebe menos elementos simultâneos, porém com personalidade visual mais forte.

SUPERFÍCIES E CONTRASTE — Superfícies geométricas, faixas inclinadas ou cortes podem aparecer como identidade, mas texto crítico permanece sobre áreas estáveis. O campo cromático pode combinar off-white/charcoal com acento esportivo forte e referências discretas a areia/oceano, sem tokens. O acento não contamina todos os elementos nem funciona como neon.

NAVEGAÇÃO VISUAL — Pode usar rótulos fortes, marcador ativo geométrico e transições de posição mais expressivas, mantendo os mesmos destinos. No treinador em largura maior, pode surgir barra/rail vertical com números de seção e rótulos; na atleta, navegação inferior enxuta com identidade de equipe. Ícones futuros são apoio, não substitutos de rótulos essenciais.

LISTAS, AGENDA E TIMELINE — Agenda usa blocos temporais escalonados e datas grandes como marcadores. Listas de equipe/competição alternam linhas abertas com etiquetas de estado e números de ordem. Em dados densos, assimetria é reduzida para preservar comparação; a direção não força composição artística onde tabela/lista é mais funcional.

TREINO E COMPOSIÇÃO — Disponibilidade da atleta funciona como faixa de decisão de alto impacto conectada ao evento. No treinador, composição pode ganhar painel de equipe mais visual, com grupos e posições representados por geometria específica de quadra, enquanto lista nominal permanece legível e filtrável. A forma nunca sugere sistema tático que os dados não sustentem.

COMPETIÇÃO, PLACAR E DIA DO JOGO — É a direção mais apropriada para transformar DIA DO JOGO em momento de identidade sem criar outra Home: próximo jogo, adversário e horário ganham grande presença; último resultado vira faixa esportiva; campanha no pós usa números fortes e composição editorial-assimétrica. Convocação e prazos mantêm semântica e apenas mudam de proporção.

ESTADOS G5 — Loading preserva massas e proporções sem números ou nomes falsos. Vazio usa área negativa como parte intencional do layout. Erro interrompe a superfície do bloco afetado com mensagem clara, sem alerta teatral. Offline usa faixa persistente sem reordenar contexto. Pendência dá forma dominante ao bloco de ação. Sucesso reduz ênfase da ação ao confirmar. Indisponibilidade retira affordance ou converte em superfície informativa estável.

ASSINATURA E RISCO — Esporte coletivo contemporâneo, presença, energia de equipe e identidade autoral. Risco: exagerar geometria, animação ou escala e cair em gaming/marketing. Controle: limitar gestos expressivos aos pontos P0/P1 e usar estruturas simples em listas, detalhes longos e dados comparativos.

APLICAÇÃO POR FAMÍLIAS — Home/Central: composição de impacto + módulos assimétricos. Agenda: marcadores temporais fortes. Treino: faixa de ação + painel de equipe. Competições: módulos de etapa e estado. Detalhe: palco contextual PRÉ/JOGO/PÓS. Equipe: roster moderno com grupos. Resultados: números de campanha + listas. Qualidade: linguagem mais contida para não gamificar erro. Perfil/Mais: superfícies simples com assinatura geométrica mínima.

## Matriz de diferenciação obrigatória

TECHNICAL COURT diferencia-se por malha, eixos, linhas de quadra e zonas operacionais. BEACH EDITORIAL diferencia-se por narrativa vertical, espaço negativo, regras editoriais e pouca superfície fechada. TEAM OPERATIONS diferencia-se por densidade, filas, listas, tabelas e infraestrutura de navegação. MODERN COLLECTIVE SPORT diferencia-se por assimetria, escala, superfícies geométricas e ritmo de impacto.

Teste de autenticidade: se for possível transformar uma direção em outra apenas trocando cor, fonte e ícones, G4 visual falhou. Para passar, pelo menos composição-base, ritmo, natureza das superfícies, navegação visual e tratamento de listas/placares/timelines devem permanecer estruturalmente diferentes.

Teste de conteúdo: as quatro direções devem receber o mesmo texto e o mesmo volume de dados sem esconder informação para “ficar bonita”. A versão do treinador precisa suportar a densidade real de lista nominal, composição, prazos, resultados e qualidade; a versão da atleta precisa manter ação própria e privacidade sem herdar ruído interno.

## Pacote canônico para comparação das quatro direções

Os protótipos comparativos futuros devem usar os mesmos cenários funcionais, permitindo observar linguagem e não conteúdo. Cenário 1: ATH Início em ROTINA com disponibilidade pendente. Cenário 2: ATH Detalhe do Treino com resposta salva e plano publicável. Cenário 3: ATH Detalhe da Competição em DIA DO JOGO. Cenário 4: COACH Central em PRÉ-COMPETIÇÃO com pendência P0 e próximo treino válido. Cenário 5: COACH Detalhe do Treino com distribuição, lista nominal e composição. Cenário 6: COACH Detalhe da Competição em DIA DO JOGO. Cenário 7: COACH Resultados com parcial incompleto. Cenário 8: COACH Qualidade sem pendências.

Cada cenário deve ser repetido, quando necessário, em pelo menos um estado G5 não ideal — loading, erro, offline, pendência ou indisponibilidade — usando o mesmo dado de referência. Não se deve criar conjunto de dados diferente para favorecer uma direção.

O objetivo deste pacote não é fechar mockups agora; é garantir que, quando a prototipação começar, a comparação seja controlada e que diferenças visuais possam ser julgadas sem confusão com diferenças funcionais.

## Critérios de aceite — Seção 3 / G4 visual

1\. As quatro direções usam as mesmas 17 telas funcionais, os mesmos blocos G4, os mesmos contextos e os mesmos contratos G5.

2\. Nenhuma direção cria função, dado, métrica, rota, permissão, CTA ou estado novo.

3\. Cada direção possui gramática própria de composição, ritmo, superfície, navegação visual, lista/timeline, treino/composição, competição/placar e estados.

4\. A distinção continua perceptível sem cor; paleta isolada não é critério de diferenciação.

5\. A experiência ATLETA e TREINADOR permanece coerente dentro de cada direção, com densidades diferentes e mesma identidade de produto.

6\. Estados loading, vazio, erro, offline, pendência, sucesso e indisponibilidade possuem representação compositiva definida sem alterar sua semântica.

7\. Nenhuma direção depende de cards repetitivos, neon/glow, repertório de fitness/running, ícones genéricos ou fotografia decorativa para funcionar.

8\. Direções suportam o volume real de informação do treinador sem reduzir legibilidade e suportam a simplicidade necessária à atleta sem criar vazio artificial.

9\. Contextos ROTINA/PRÉ/JOGO/PÓS reorganizam a ênfase conforme Seção 6, sem criar segunda identidade visual ou Home paralela.

10\. Tokens atômicos continuam em aberto para G6; G4 visual encerra na gramática compositiva.

## GATE DE SAÍDA — SEÇÃO 3 / G4 VISUAL

A Seção 3 atinge G4 visual quando Technical Court, Beach Editorial, Team Operations e Modern Collective Sport conseguem representar a mesma arquitetura, conteúdo, prioridade, privacidade e estados através de quatro gramáticas compositivas realmente distintas; quando cada direção possui regras próprias para composição, ritmo, superfícies, navegação visual, listas/timelines, treino/composição, competição/placar, estados G5 e adaptação ATLETA/TREINADOR; e quando a diferença não depende apenas de paleta, fonte ou ícones. Status desta execução: QUATRO DIREÇÕES VISUAIS ESPECIFICADAS EM G4 VISUAL.

Próxima dependência: comparar as quatro direções usando o pacote canônico de cenários, selecionar a direção ou combinação aprovada e então executar Tipografia e Iconografia em G6. Somente depois devem ser consolidados tokens visuais e produzidos protótipos mobile de alta fidelidade candidatos a validação.

# IDENTIDADE VISUAL CEPRAEA — EVIDÊNCIAS E IMPLICAÇÕES PARA O PRODUTO

# 

# Objetivo e regra de evidência

# Esta seção adiciona um critério de identidade real do CEPRAEA à avaliação dos quatro Hi-Fi. Ela não substitui G3/G4/G5 nem altera conteúdo, prioridade, permissão ou comportamento. Seu papel é impedir que a interface seja visualmente coerente, porém genérica ou deslocada da equipe. Toda conclusão abaixo é classificada como EVIDÊNCIA, INFERÊNCIA DE DESIGN ou NÃO CONFIRMADO.

# 

# EVIDÊNCIA 1 — apresentação contemporânea da equipe em 2026

# Fonte pública recente: Jornal da Paraíba, 30/03/2026, registro da conquista feminina da Copa Brasil de Handebol de Praia no Paraíba World Beach Games. A fotografia mostra o CEPRAEA na areia, em contexto de conquista coletiva, com camisetas verdes, shorts pretos e elementos claros/brancos de contraste. O evento e o título também são confirmados por Repórter PB e A União.

# Implicação: verde + preto/branco constituem uma combinação contemporânea comprovadamente compatível com a apresentação da equipe. Isso NÃO autoriza declarar um HEX oficial, proporção oficial de uso ou manual de marca inexistente.

# 

# EVIDÊNCIA 2 — território físico e linguagem do esporte

# As referências públicas atuais e históricas situam o CEPRAEA repetidamente em areia, praia, quadra, treino, competição, viagem e pódio. Registros preservados de publicações sociais da fase CEPRAEA/Vasco em 2019 usam fotografia esportiva, chamadas de treino/competição, apoio da torcida e linguagem de pertencimento à equipe; um registro de 2012 aponta inclusive para álbum fotográfico do CEPRAEA no Facebook.

# Implicação: o produto deve parecer pertencente a uma equipe de beach handball. Areia, linhas de quadra, placar, uniforme, movimento, grupo e competição são repertório identitário mais legítimo que academia, corrida, wellness, halteres ou estética de fitness tracker.

# 

# EVIDÊNCIA 3 — identidade coletiva

# A comunicação pública preservada valoriza equipe, treino, classificação, defesa de título, convocação e apoio coletivo. O núcleo narrativo é “nós/time/equipe”, não a construção de um score individual de performance.

# Implicação: métricas individuais não devem dominar a primeira dobra da atleta. Composição, competição, convocação, compromisso, campanha e ação coletiva têm prioridade visual superior a metáforas de self-tracking.

# 

# EVIDÊNCIA 4 — energia e gesto técnico

# Fotografias e publicações ligadas ao CEPRAEA e ao beach handball privilegiam ação, salto, passe, giro, defesa, areia e deslocamento. A modalidade possui forte assinatura corporal e espacial.

# Implicação: assimetria, tensão espacial e diagonais podem ser usadas com parcimônia para expressar movimento; a geometria da quadra permanece uma fonte gráfica válida. Isso não autoriza linguagem de videogame, glow, neon ou excesso de efeitos.

# 

# NÃO CONFIRMADO

# Não há evidência pública suficiente, nesta pesquisa, para declarar como oficial: família tipográfica; códigos HEX institucionais; proporções/área de proteção do logotipo; regras de fotografia; sistema oficial de ícones; textura; motion; ou manual de identidade vigente. Essas decisões continuam como design de produto e devem permanecer reversíveis até existir material oficial.

# 

## Princípios de identidade para os Dashboards

# 1\. Verde passa a ser a primeira cor identitária candidata, preferencialmente em faixa média/escura e esportiva; evitar verde neon como base.

# 2\. Preto/grafite e branco/off-white formam a estrutura neutra principal; areia entra como território/material, não como obrigação de pintar toda a interface de bege.

# 3\. Fotografia real de equipe/competição deve ser suportada pelo sistema em pontos editoriais apropriados, mas nunca necessária para compreender uma ação crítica.

# 4\. Geometrias de quadra, linhas, zonas e marcações podem estruturar composição, especialmente em treino, competição e composição tática.

# 5\. Identidade deve comunicar esporte coletivo de praia: equipe + competição + movimento + pertencimento.

# 6\. Proibido usar fitness/running/wellness como linguagem visual dominante: anéis de recovery, halteres, score proprietário sem contrato, neon e estética de aplicativo de academia não representam o núcleo do CEPRAEA.

# 7\. A interface do treinador pode ser mais densa e operacional, mas deve continuar parecendo parte do mesmo clube/equipe, não um SaaS administrativo genérico.

# 8\. A interface da atleta pode ser mais humana/editorial, mas não deve virar lifestyle de praia; ação esportiva e compromisso continuam centrais.

# 

## NOVO CRITÉRIO DE REVISÃO DOS QUATRO HI-FI

# Cada candidata deve ser avaliada, além dos critérios anteriores, por oito perguntas: (1) parece CEPRAEA/equipe de beach handball? (2) verde/preto/branco entram de forma natural sem depender de neon? (3) a areia é território e não decoração? (4) a composição aceita fotografia real sem quebrar a hierarquia P0/P1? (5) o coletivo é visualmente mais forte que self-tracking? (6) placar, competição e quadra têm linguagem própria? (7) treinador e atleta compartilham identidade sem terem a mesma densidade? (8) o sistema continua legível mesmo sem fotografia.

# 

### REVISÃO A — TECHNICAL COURT

# Manter: geometria de quadra, linhas estruturais, Event Rail, Composition Line e lógica de informação aberta.

# Refinar: reduzir predominância de areia/bege como “cor da marca”; ancorar em grafite/preto + branco/off-white + verde esportivo; reservar areia para planos secundários/território. Criar zonas opcionais para fotografia coletiva em competição e pós-etapa sem converter Home em feed fotográfico. A quadra deve funcionar como gramática, não como ilustração repetitiva.

# Risco após novo critério: pode ficar técnico e impessoal se a dimensão humana do time não aparecer em momentos de competição/conquista.

# 

### REVISÃO B — BEACH EDITORIAL

# Manter: espaço negativo, narrativa, capacidade de receber fotografia, hierarquia editorial e tratamento humano das conquistas.

# Refinar: retirar qualquer leitura de resort/lifestyle; aumentar presença de preto/grafite e verde esportivo; usar areia como suporte, não como paleta dominante. Placar, agenda e disponibilidade precisam continuar nítidos e operacionais. Fotografia deve representar equipe/ação real, nunca imagem decorativa de praia.

# Risco após novo critério: tornar-se bonita/editorial, mas menos eficiente em estados de alta urgência se o ritmo visual for lento demais.

# 

### REVISÃO C — TEAM OPERATIONS

# Manter: densidade, listas, navegação técnica, roster, composição e leitura rápida do treinador.

# Refinar: substituir aparência de SaaS genérico por identidade do CEPRAEA: verde/preto/branco, sinais de quadra, linguagem de competição e hierarquia esportiva. No perfil ATLETA, reduzir sensação de painel administrativo e permitir respiro/humanidade maior.

# Risco após novo critério: ser excelente ferramenta do treinador, mas fraca identidade de equipe para a atleta se aplicada de maneira uniforme aos dois perfis.

# 

### REVISÃO D — MODERN COLLECTIVE SPORT

# Manter: energia coletiva, assimetria, tensão espacial e capacidade de expressar movimento/competição.

# Refinar: trocar acentos genéricos laranja/amarelo por verde CEPRAEA candidato e preto/branco; reduzir qualquer sinal de gaming; usar diagonais e blocos assimétricos como tradução do gesto do beach handball, não como decoração. A estrutura deve preservar leitura operacional do treinador.

# Risco após novo critério: a energia visual pode competir com o conteúdo P0 ou envelhecer rapidamente se depender de efeitos de impacto.

# 

## REGRA DE COMPARAÇÃO PÓS-IDENTIDADE

# Os quatro Hi-Fi continuam obrigados a usar os mesmos 8 cenários, conteúdo, dados, ações, estados e prioridades. A revisão de identidade pode alterar somente paleta candidata, materiais, composição, fotografia opcional, ritmo, iconografia e linguagem visual. A seleção final permanece PENDENTE até a avaliação dos quatro protótipos revisados pelo mesmo pacote canônico.

# 

## FONTES PÚBLICAS CONSULTADAS

# \- Jornal da Paraíba — “Apcef/Cascavel e Cepraea conquistam Copa Brasil de Handebol de Praia no Paraíba World Beach Games”, 30/03/2026.

# \- Repórter PB — “Paraíba World Beach Games: Copa Brasil de Handebol de Praia define campeões”, 30/03/2026.

# \- A União — edição de 31/03/2026, resultado da Copa Brasil de Handebol de Praia.

# \- SuperVasco/Instagram CEPRAEA/Vasco Beach Hand — publicações preservadas de 2019 sobre treino, Estadual, Circuito Brasileiro e seletivas.

# \- Handebol de Areia — Beach Handball — Balonmano Playa, fevereiro/2012 — referência a álbum de fotos do CEPRAEA no Facebook.

# 

## STATUS DA REVISÃO PÓS-IDENTIDADE

# As quatro candidatas A/B/C/D foram revisadas em V2 com este novo critério de identidade. A validação de comparabilidade confirma que os 8 cenários funcionais permanecem idênticos entre as quatro versões; as alterações são exclusivamente de linguagem visual/compositiva. A comparação e eventual seleção devem usar os arquivos V2 pós-identidade. Seleção final: PENDENTE.

# 

# COMPARAÇÃO DO PACOTE CANÔNICO E SELEÇÃO DA DIREÇÃO

## Método de comparação

As quatro direções foram comparadas usando exatamente o mesmo pacote canônico definido no G4 visual e os mesmos contratos G3/G4/G5. A avaliação é uma decisão de design do produto, não uma métrica estatística. Escala: 1 = fraco, 3 = adequado com ressalvas, 5 = muito forte.

## Critérios

C1 — Clareza de P0/P1 no primeiro fluxo mobile.

C2 — Simplicidade e pertencimento na experiência da atleta.

C3 — Capacidade de densidade e drill-down no treinador.

C4 — Elasticidade para ROTINA / PRÉ / DIA DO JOGO / PÓS sem perder memória espacial.

C5 — Identidade específica de handebol de praia/equipe, sem fitness/running/gaming.

C6 — Robustez para loading, vazio, erro, offline, pendência e indisponibilidade.

C7 — Baixo risco de virar template genérico de dashboard.

## Matriz de avaliação

Technical Court — C1 5 | C2 5 | C3 4 | C4 5 | C5 5 | C6 5 | C7 5 = 34/35.

Beach Editorial — C1 4 | C2 5 | C3 3 | C4 4 | C5 5 | C6 4 | C7 5 = 30/35.

Team Operations — C1 5 | C2 3 | C3 5 | C4 5 | C5 4 | C6 5 | C7 4 = 31/35.

Modern Collective Sport — C1 4 | C2 4 | C3 4 | C4 5 | C5 5 | C6 4 | C7 4 = 30/35.

## Leitura por cenário canônico

1\. Início da atleta / ROTINA: Technical Court e Beach Editorial preservam melhor a ação sem transformar a tela em painel de métricas; Technical Court oferece maior continuidade com os estados técnicos do restante do produto.

2\. Detalhe do Treino da atleta: Technical Court representa evento + ação + plano publicado como uma sequência estrutural clara e funciona bem quando o plano não existe.

3\. Detalhe da Competição / DIA DO JOGO: Technical Court e Modern Collective Sport acomodam melhor placar/próximo jogo sem perder identidade; Technical Court tem menor risco de gaming.

4\. Central do treinador / PRÉ-COMPETIÇÃO: Team Operations é o mais denso, mas Technical Court mantém atenção e prazos com densidade suficiente sem transformar a experiência inteira em admin panel.

5\. Detalhe do Treino do treinador: Technical Court é o mais alinhado à cadeia disponibilidade → lista → composição → cobertura tática, porque a própria gramática espacial pode derivar de zonas/linhas de quadra.

6\. Detalhe da Competição do treinador: Team Operations e Technical Court são fortes; Technical Court preserva mais identidade esportiva.

7\. Resultados com dado incompleto: Team Operations é muito eficiente, porém Technical Court representa resultado e qualidade sem recorrer a grade corporativa genérica.

8\. Qualidade sem pendências: Team Operations é naturalmente adequado, mas Technical Court consegue expressar integridade com linguagem técnica discreta e mantém coerência com todas as outras telas.

## STATUS DA DIREÇÃO A — TECHNICAL COURT (CANDIDATA MATERIALIZADA)

Technical Court é a primeira candidata materializada em Hi-Fi e NÃO constitui direção visual aprovada. A seleção final permanece pendente até que Beach Editorial, Team Operations e Modern Collective Sport sejam materializadas com exatamente os mesmos 8 cenários canônicos, preservando arquitetura, conteúdo, dados, prioridades, ações e estados. A comparação deve avaliar linguagem visual, composição, ritmo, superfícies, navegação e identidade; nenhuma direção pode ganhar ou perder funções ou informação para parecer melhor.

## Justificativa UX

Technical Court apresenta o melhor equilíbrio entre ação rápida para atleta, densidade operacional para treinador, identidade de esporte coletivo e capacidade de reorganização contextual. Sua maior vantagem é permitir que a informação seja agrupada por eixos, zonas, linhas, faixas e listas — reduzindo a dependência de cards — enquanto continua suportando estados G5 e listas densas.

## Riscos e mitigação

Risco: excesso de linhas/quadra virar decoração. Mitigação: cada linha deve estruturar alinhamento, sequência ou relação; textura gratuita é proibida.

Risco: aparência excessivamente técnica para atleta. Mitigação: versão atleta usa mais espaço aberto, menos divisores e linguagem humana; a gramática permanece a mesma.

Risco: uso de verde esportivo virar neon. Mitigação: acento deve ser fosco/controlado; sem glow, gradiente luminoso ou alta saturação dominante.

Risco: composição tática virar metáfora em toda tela. Mitigação: geometria de quadra é abstrata e estrutural, não uma ilustração literal permanente.

## Gate de seleção

A direção visual está selecionada quando existe uma única gramática autorizada para fechar G6 e prototipar, sem mistura silenciosa de alternativas. Status: TECHNICAL COURT SELECIONADA PARA A V1 MOBILE.

## 4\. A fonte também vira uma decisão de design

Não precisamos continuar presos a uma única combinação.

Podemos testar, por exemplo:

UI limpa

Manrope / Inter

+

informação esportiva

Barlow Condensed

versus:

UI

IBM Plex Sans

+

impacto / placares

Archivo Narrow

versus uma direção ainda mais editorial.

A escolha deve acontecer **vendo a tela completa**, porque tipografia muda densidade, ritmo e personalidade.

# EXECUÇÃO G6 — TIPOGRAFIA CEPRAEA

## Decisão tipográfica

A direção Technical Court usa dois papéis tipográficos complementares, sem multiplicar famílias por tela: IBM Plex Sans para interface/leitura e Archivo Narrow para impacto esportivo, datas/horários e placares. A família condensada nunca é usada para corpo longo. Fallbacks devem preservar legibilidade sem depender de arquivos de fonte embarcados no produto.

## Tokens tipográficos semânticos

TYPE-DISPLAY-XL — Archivo Narrow 700, 48/48 px, tracking -0,02em. Uso: placar excepcional, número/horário dominante em Dia do Jogo. Máximo 1–2 linhas; preferir uma linha.

TYPE-DISPLAY-L — Archivo Narrow 700, 40/42 px, tracking -0,015em. Uso: data/hora de próximo compromisso, resultado/campanha em destaque.

TYPE-SCORE-M — Archivo Narrow 700, 32/34 px, números tabulares/lining. Uso: placar, contagens esportivas realmente dominantes.

TYPE-NUMBER-S — Archivo Narrow 600, 22/24 px, números tabulares. Uso: contagens de disponibilidade/composição e indicadores compactos.

TYPE-H1 — IBM Plex Sans 600, 28/34 px, tracking -0,01em. Uso: título principal de tela quando necessário; evitar all-caps.

TYPE-H2 — IBM Plex Sans 600, 22/28 px. Uso: seção P0/P1 e títulos de detalhe.

TYPE-H3 — IBM Plex Sans 600, 18/24 px. Uso: subseção/bloco funcional.

TYPE-BODY-L — IBM Plex Sans 400, 17/26 px. Uso: texto explicativo curto, estados e mensagens prioritárias.

TYPE-BODY — IBM Plex Sans 400, 16/24 px. Uso: corpo padrão e conteúdo de leitura da atleta.

TYPE-BODY-COMPACT — IBM Plex Sans 400, 14/20 px. Uso: linhas densas do treinador; nunca abaixo deste tamanho para conteúdo funcional recorrente.

TYPE-LABEL — IBM Plex Sans 600, 12/16 px, tracking +0,06em. Uso: rótulos curtos, categorias, status; caixa alta opcional somente em 1–3 palavras.

TYPE-META — IBM Plex Sans 500, 13/18 px. Uso: local, fonte temporal, texto secundário e metadados.

TYPE-ACTION — IBM Plex Sans 600, 16/20 px. Uso: ações primárias e controles de disponibilidade.

TYPE-NAV — IBM Plex Sans 600, 11/14 px. Uso: rótulo da navegação inferior; nunca somente ícone em destinos primários.

## Regras de uso

1\. Números de placar, horário e contagem usam font-variant-numeric: tabular-nums quando suportado.

2\. Archivo Narrow é reservado a impacto esportivo/números e não deve transformar toda a interface em pôster esportivo.

3\. IBM Plex Sans mantém o tom técnico e humano em listas, agenda, estados e formulários.

4\. Textos longos em caixa alta são proibidos. Caixa alta fica restrita a labels/status curtos.

5\. Corpo funcional mínimo padrão: 14 px no treinador denso; 16 px na leitura normal da atleta. Não reduzir tipografia para “fazer caber”.

6\. Truncamento só é permitido quando existe acesso ao conteúdo completo; local, adversário, atleta e status críticos devem quebrar linha quando necessário.

7\. Estado/semântica não depende apenas de peso tipográfico: rótulo e estrutura acompanham cor/ícone.

8\. Escala deve suportar aumento de fonte do sistema; componentes devem crescer verticalmente em vez de cortar conteúdo essencial.

## Mapeamento por domínio

Próximo compromisso: TYPE-LABEL + TYPE-DISPLAY-L + TYPE-BODY/META.

Disponibilidade: TYPE-H3 + TYPE-ACTION + TYPE-META.

Agenda/timeline: TYPE-META para data curta, TYPE-BODY/H3 para evento, TYPE-META para local/horário.

Competição: TYPE-LABEL para estado, TYPE-H2/H3 para nome, TYPE-SCORE-M/DISPLAY para jogo somente quando contexto exigir.

Treinador/roster: TYPE-BODY-COMPACT + TYPE-LABEL; números de composição em TYPE-NUMBER-S.

Qualidade: TYPE-LABEL para severidade + TYPE-BODY-COMPACT para entidade/diagnóstico.

## Gate G6 de Tipografia

A tipografia atinge G6 quando todo texto funcional das 17 telas pode apontar para um token sem criação de estilo ad hoc; quando números esportivos possuem comportamento tabular; quando o sistema suporta nomes/locais longos e aumento de texto; e quando a família condensada não prejudica leitura. Status: TIPOGRAFIA G6 FECHADA PARA TECHNICAL COURT.

## 5\. A iconografia passa a nascer do CEPRAEA

Também não considero mais aceitável resolver funções centrais com:

🏆 ⌂ ◎ ou halteres genéricos.

Precisamos definir uma família de ícones para:

*handebol de praia*

*quadra*

*bola*

*treino*

*goleira*

*defesa*

*ataque*

*composição*

*convocação*

*competição*

*jogo*

*shoot-out*

*disponibilidade*

*agenda*

*equipe*

*alerta operacional*

Até elementos abstratos podem nascer das **linhas e geometrias da quadra de beach handball**.

Isso começa a criar identidade.

# EXECUÇÃO G6 — ICONOGRAFIA CEPRAEA

## Escopo

A iconografia G6 consolida uma família própria coerente com a direção Technical Court. Ícones universais podem usar repertório convencional, mas conceitos centrais do handebol de praia recebem metáforas próprias. Emoji, halter, troféu genérico e pictogramas de fitness não são linguagem oficial do produto.

## Gramática geométrica

Grid padrão: 24 × 24. Variante compacta: 20 × 20. Variante de destaque: 28 × 28 somente quando a hierarquia exigir.

Stroke padrão: 1,75 px; terminais e joins arredondados. Formas prioritariamente abertas, com preenchimento restrito a estados/acentos semânticos. Construção deve reutilizar retas, arcos e zonas inspiradas abstratamente nas linhas de uma quadra de beach handball.

Área óptica: manter margem interna consistente e corrigir visualmente ícones muito horizontais/verticais; centralização matemática não substitui centralização óptica.

Estado ativo: não redesenhar o pictograma. O estado ativo é indicado pela composição do item de navegação, contraste e marcador estrutural do Design System.

## Família esportiva obrigatória

COURT — retângulo/zonas essenciais da quadra, sem ilustração realista.

BALL — círculo com cortes internos próprios, simples o suficiente para 20 px.

TRAINING — recorte de quadra + trajetória/seta curta; proibido representar treino por halter.

GOLEIRA — zona de gol + elemento central de proteção/posição; não usar silhueta genérica de pessoa.

DEFESA — linha de cobertura com três pontos conectados/ocupação de zona.

ATAQUE — progressão de três pontos/rotas em direção ao gol.

COMPOSIÇÃO — distribuição de posições em zonas, não ícone de organograma corporativo.

CONVOCAÇÃO — lista nominal/jersey abstrato + confirmação, sem medalha/troféu.

COMPETIÇÃO — quadra/evento + marca de confronto; não confundir com resultado.

JOGO — dois lados + bola/centro, representando confronto.

SHOOT-OUT — trajetória 1×1 em direção ao gol, distinta de pênalti de futebol.

DISPONIBILIDADE — sistema de três estados compatível com SIM/TALVEZ/NAO, usando check/interrogação/x apenas como sinais universais subordinados ao rótulo.

AGENDA — sequência temporal/linhas de dia, evitando calendário mensal genérico como metáfora dominante.

EQUIPE — conjunto alinhado de participantes/posições, sem “grupo de usuários” corporativo padrão quando houver espaço para o ícone próprio.

QUALIDADE — vínculo/estrutura de dado com alerta, separado de aviso operacional comum.

## 

## Ícones universais permitidos

Voltar, fechar, mais opções, busca, filtro, mostrar/ocultar senha, logout, atualizar e chevron podem seguir metáforas universais, desde que usem a mesma espessura, terminais e proporção óptica. A implementação pode partir de uma biblioteca permissiva para estes utilitários; os pictogramas esportivos centrais permanecem próprios.

## Acessibilidade e semântica

Ícone nunca substitui rótulo em ações críticas. Todo ícone interativo possui nome acessível. Cor não é o único diferenciador. Ícones de SIM/TALVEZ/NAO devem permanecer distinguíveis por forma e texto. Alvos interativos mínimos: 44 × 44 pt/CSS px equivalentes no mobile.

## Estados

LOADING não usa ícone esportivo pulsante; progresso é representado por mecanismo universal discreto.

VAZIO usa linguagem de ausência do domínio, sem pictograma decorativo obrigatório.

ERRO usa sinal de erro somente junto do domínio afetado.

OFFLINE usa indicador universal de conectividade e não altera o significado do ícone esportivo.

PENDÊNCIA usa marcador semântico adjacente, não animação contínua.

SUCESSO usa confirmação breve quando há ação mutável; não mantém check decorativo permanente em todo bloco.

INDISPONIBILIDADE reduz affordance e mantém leitura quando permitido; não usar cadeado em tudo o que simplesmente não possui ação.

## Gate G6 de Iconografia

A iconografia atinge G6 quando cada conceito central possui metáfora, grid, stroke, estados, acessibilidade e regra de uso; quando nenhuma função esportiva central depende de emoji ou repertório fitness; e quando a família continua reconhecível em 20, 24 e 28 px. Status: ICONOGRAFIA G6 FECHADA PARA TECHNICAL COURT.

# DESIGN SYSTEM CANDIDATO A — TECHNICAL COURT DS 1.0

## Princípios

1\. ACTION-FIRST: P0/P1 dirigem a composição; estética nunca esconde ação ou risco operacional.

2\. LINHAS ANTES DE CARDS: usar eixos, divisores, faixas e zonas abertas; container permanente só quando agrupamento ou interação exigir fronteira clara.

3\. EVENTO COMO ÂNCORA: treino/competição/jogo preservam identidade e contexto antes de qualquer ação.

4\. ESPORTE COLETIVO: linguagem deriva de quadra, composição, confronto e equipe; evitar estética de corrida, wellness, academia e gaming.

5\. DADO CANÔNICO: estado visual nunca antecipa sucesso, conclusão ou contexto sem confirmação.

6\. PRIVACIDADE PRIMEIRO: dado não autorizado não recebe placeholder, loading ou empty state revelador.

## Paleta semântica principal

Canvas Sand 50 — #F2EFE7: fundo principal claro e quente.

Surface Warm — #FBFAF6: superfícies elevadas somente quando necessárias.

Ink 950 — #171A1C: texto principal e faixas de alto contraste.

Graphite 700 — #343A3E: texto secundário forte e elementos técnicos.

Court Line 300 — #C7C2B5: divisores, malha e linhas estruturais.

Court Green 700 — #355845: acento de identidade e ação primária controlada.

Court Green 100 — #DCE7DE: superfície de confirmação/seleção leve.

Ocean 700 — #315E68: informação/contexto secundário e links quando necessário.

SIM — #2F6B4D. TALVEZ — #9A702B. NAO/ERRO — #A24B47. SEM\_RESPOSTA/PENDÊNCIA — #767A77. INFO — #315E68.

Regra: roxo não é cor estrutural do sistema; neon não é permitido. Cor de status nunca funciona sem rótulo/forma.

## Superfícies e bordas

Open Section: fundo do canvas, sem contorno, separada por ritmo e linha.

Framed Zone: borda 1 px Court Line, raio 8–12 px; usar apenas em agrupamento funcional real.

Action Band: faixa de ação de alto contraste ou acento controlado, sem glow.

Score Strip: composição horizontal/vertical aberta, tipografia numérica dominante e divisores.

Bottom Sheet/Modal: raio 16 px e sombra restrita a elementos flutuantes.

Sombras não são usadas para separar seções comuns.

## Espaçamento e grid

Base: 4 px. Escala: 4, 8, 12, 16, 20, 24, 32, 40, 48.

Margem mobile: 16 px em 360–389 px; 20 px em 390–430 px quando não comprometer densidade.

Ritmo entre seções P0/P1: 24–32 px; grupos densos do treinador: 12–20 px conforme relação semântica.

Linhas estruturais podem atravessar mais de um bloco para criar continuidade de quadra; não devem virar textura decorativa repetitiva.

## Navegação mobile

Atleta: Bottom Navigation com 4 destinos — Início, Agenda, Competições, Perfil. Treinos permanece secundário.

Treinador: Bottom Navigation com 5 destinos — Central, Treino, Agenda, Equipe, Mais.

Altura visual mínima da área interativa: 56 px + safe-area. Ícone 24 px, rótulo curto, marcador ativo por linha/zona Technical Court. Nenhum item usa emoji.

## Componentes/padrões semânticos de design

Court Header — identidade de tela + contexto temporal/operacional.

Event Rail — evento com data/hora/local organizado por eixo temporal.

Action Band — ação P0/P1 com estado transacional explícito.

Availability Segment — SIM/TALVEZ/NAO com SEM\_RESPOSTA como estado atual, não quarta escolha.

Timeline Row — unidade de agenda por evento\_id.

Score Strip — placar/campanha sem dashboard de métricas genérico.

Roster List — lista nominal com status/função; densidade alta no treinador.

Composition Line — resumo Goleira/Defesa/Ataque sem fingir modelo tático completo.

Tactical Zone — cobertura tática condicional, somente com fonte atual suficiente.

Quality Row — severidade, entidade e caminho seguro para diagnóstico.

State Message — vazio/erro/offline/indisponibilidade adjacente ao domínio afetado.

Bottom Nav — navegação persistente por perfil.

Regra: esses nomes representam padrões de design, não nomes obrigatórios de componentes React.

## Motion e feedback

Tap/press: 120–160 ms. Mudança de seleção/estado local: 160–200 ms. Reordenação contextual confirmada: 200–240 ms com movimento mínimo e preservação espacial. Bottom sheet: 220–280 ms. Sem pulsos, brilho respirando ou animação contínua de status. Respeitar prefers-reduced-motion.

## Responsividade e ergonomia

Alvo mínimo 44 × 44. Safe areas obrigatórias. Testar largura 360, 390 e 430 px e aumento de texto. Dados densos devem quebrar para lista/linha, não reduzir corpo abaixo do token mínimo. A interface deve tolerar nomes longos, locais longos e múltiplos eventos no mesmo dia.

## Estados G5 no Design System

LOADING — skeleton/placeholder estrutural neutro apenas para conteúdo autorizado; sem números simulados.

VAZIO — mensagem contextual curta + próxima ação somente quando existe.

ERRO — estado localizado; preserva blocos independentes válidos.

OFFLINE — indicador persistente no escopo relevante; leitura cacheada identificada; escrita indisponível.

PENDÊNCIA — marcador de negócio com prioridade decorrente do G4/G3-G4, nunca spinner.

SUCESSO — confirmação server-side e feedback breve; sem celebração genérica em tarefas administrativas.

INDISPONIBILIDADE — remover affordance ou tornar somente leitura, explicando motivo no nível permitido.

## Gate de Design System

O Design System está consolidado quando Tipografia G6 + Iconografia G6 + paleta, superfícies, grid, navegação, padrões, estados, motion, acessibilidade e responsividade formam uma gramática única compatível com os contratos G3/G4/G5. Status: TECHNICAL COURT DS 1.0 CONSOLIDADO PARA PROTOTIPAÇÃO DE ALTA FIDELIDADE.

# PROTOTIPAÇÃO MOBILE HI-FI — PACOTE TECHNICAL COURT

## Artefato produzido

Foi produzido um protótipo navegável mobile baseado no Technical Court DS 1.0, sem alterar os contratos G3/G4/G5. O pacote possui oito cenários canônicos: Atleta Início/ROTINA; Atleta Detalhe do Treino; Atleta Dia do Jogo/campanha; Treinador Central/PRÉ; Treinador Detalhe do Treino; Treinador Detalhe da Competição; Treinador Resultados; Treinador Qualidade em estado controlado sem pendências.

## Regra de dados

Quando o cenário corresponde à operação atual, o protótipo utiliza dados canônicos consultados na CEPRAEA DATABASE: próximo treino TRN-2026-08-27, 27/08/2026, 20:00–21:30, Posto 4; competições e estados de participação; campanha coletiva validada de 28 jogos; e disponibilidade declarada vigente usada na visão do treinador. Conteúdo de treino ainda não publicado é tratado como ausência/publicação pendente, não exibido como texto interno para atleta.

O cenário de Qualidade “sem pendências” é identificado dentro do próprio protótipo como CENÁRIO CONTROLADO DE VALIDAÇÃO G5 e não representa a situação corrente da base.

## Cobertura visual do pacote

O protótipo implementa: superfícies abertas; linhas estruturais; Action Band; timeline; Score Strip; Roster List; Composition Line; estados de pendência/qualidade; bottom navigation própria por perfil; iconografia SVG sem emoji; tipografia e paleta definidas no DS; e resposta de disponibilidade apenas simulada localmente, sem qualquer escrita em planilha.

## Gate de prototipação

O pacote Hi-Fi pode avançar para validação comparativa com usuário quando as telas preservarem conteúdo/ordem dos contratos, nenhum dado fictício for apresentado como canônico e a direção Technical Court continuar reconhecível sem depender apenas de cor. Status: QUATRO PACOTES HI-FI PRODUZIDOS PARA COMPARAÇÃO — TECHNICAL COURT, BEACH EDITORIAL, TEAM OPERATIONS E MODERN COLLECTIVE SPORT. SELEÇÃO VISUAL FINAL PENDENTE.

## 6\. O estado da competição pode mudar o próprio Dashboard

Essa é uma oportunidade que só apareceu claramente depois da auditoria das planilhas.

O app não precisa ter uma Home estática.

Ele pode possuir estados contextuais:

### ROTINA

Próximo treino domina a Home.

### PRÉ-COMPETIÇÃO

Competição, convocação, agenda e pendências ganham prioridade.

### DIA DO JOGO

Próximo jogo, último resultado, fase e programação dominam.

### PÓS-ETAPA

Campanha, resultado final e próximo ciclo aparecem.

Isso é muito mais próximo de **um produto para equipe esportiva** do que de um dashboard fitness genérico.

O próprio Roadmap agora formaliza esse comportamento **ANTES / DURANTE / DEPOIS.**

# EXECUÇÃO G3/G4 — ESTADOS CONTEXTUAIS

## Escopo e princípio de resolução

Esta execução transforma ROTINA, PRÉ-COMPETIÇÃO, DIA DO JOGO e PÓS-ETAPA em estados operacionais objetivos aplicados às telas e blocos G4 já aprovados. O contexto altera prioridade, ordem, visibilidade e ação disponível, mas não cria novas Homes, não muda autorização, não cria dados e não substitui os contratos CNTR-\*.

Existem duas camadas de contexto.

CONTEXTO LOCAL é o estado da competição selecionada no Detalhe da Competição: ANTES, DURANTE ou DEPOIS, resolvido pela situação temporal e operacional daquela competição.

CONTEXTO GLOBAL é o estado que pode reorganizar Início da atleta e Central do treinador. O contexto global só muda quando uma competição relevante possui evidência canônica suficiente para dominar a atenção. Abrir uma competição futura não muda sozinho a Home/Central.

**Regra UX**: separar contexto local de contexto global preserva memória espacial e impede que o aplicativo pareça mudar de personalidade apenas porque existe uma competição futura no calendário.

## MATRIZ DE PRECEDÊNCIA E GATILHOS

**Precedência global: DIA DO JOGO > PRÉ-COMPETIÇÃO > PÓS-ETAPA > ROTINA.**

Uma ação P0 independente, como disponibilidade pendente para treino ou problema bloqueante de dados, não desaparece por causa do contexto; ela permanece visível e pode ocupar a primeira posição quando exigir ação imediata.

**DIA DO JOGO** — **entrada global**: existe competição relevante para o CEPRAEA em execução e há evidência canônica de jogo/programação no dia local atual ou estado operacional equivalente de DURANTE.  
\- **Saída:** não existe mais jogo/programação ativa no dia e a competição passa a encerrada/depois, ou deixa de haver evidência suficiente de execução. Não ativar apenas porque a data atual está dentro de um intervalo amplo sem evidência de operação de jogo.

**PRÉ-COMPETIÇÃO** — entrada global: existe competição futura relevante e pelo menos um sinal operacional ativo, como prazo/pendência, convocação publicada, programação publicada ou outro fato canônico que exija preparação. Para a atleta, o sinal precisa ser publicável; para o treinador, pode ser TREINADOR\_INTERNO.  
\- **Saída:** competição entra em DIA DO JOGO, é cancelada/não participada, perde todos os sinais ativos ou é superada por outro contexto de maior precedência.

**PÓS-ETAPA** — entrada global: uma competição relevante foi encerrada/realizada e existe resultado/campanha validada ou pendência de fechamento que precisa ser comunicada, sem contexto de maior precedência.  
\- **Saída:** surge DIA DO JOGO ou PRÉ-COMPETIÇÃO de maior precedência, ou a operação cotidiana volta a ter ação P0 dominante e o resultado recente deixa de precisar de promoção.

**ROTINA** — entrada global: nenhum dos contextos competitivos acima possui evidência suficiente para dominar a experiência.  
\- **Saída:** qualquer contexto de maior precedência torna-se válido.

**Fallback transversal:** quando faltarem dados para resolver um contexto, o sistema não infere. A Home/Central permanece no último estado seguro derivável, normalmente ROTINA, e a tela de detalhe mostra a informação disponível com estado de indisponibilidade/qualidade apropriado.

**Justificativa UX:** gatilhos baseados em fatos evitam mudanças inesperadas de hierarquia, falsos “dias de jogo”, promoções prematuras de competição e interfaces que parecem inconsistentes entre acessos.

## CTX-01 — ROTINA

### Definição

ROTINA é o estado-base da experiência. A pergunta dominante volta a ser “qual é o próximo compromisso e existe algo que preciso fazer agora?”, sem promoção artificial de competição ou resultado.

### ATLETA — mudanças em ROTINA

#### **CTX-ROT-ATH-01 — ATH-G4-01**

B1 Próximo compromisso/ação pendente permanece P0 quando existe disponibilidade pendente e P1 quando é apenas consulta; ordem 1.  
  
**Justificativa UX:** a única escrita operacional da atleta deve continuar acessível sem ser empurrada por informação esportiva histórica.

#### **CTX-ROT-ATH-02 — ATH-G4-01**

B2 Próxima competição/situação pessoal permanece P2 e ordem 2.

Justificativa UX: a competição continua visível para planejamento, mas não deve competir com o compromisso operacional mais próximo quando ainda não existe preparação ativa.

#### **CTX-ROT-ATH-03 — ATH-G4-01**

B3 Agenda próxima permanece P2 e B4 Resultado/campanha permanece P3. Justificativa UX: a Home funciona como orientação e não como arquivo; agenda e histórico apoiam a tarefa central sem aumentar carga cognitiva.

#### **CTX-ROT-ATH-04 — ATH-G4-05**

Competições mantém próximas relevantes antes do histórico; nenhuma competição é fixada no topo apenas por estar futura. Justificativa UX: evita sinalizar prioridade competitiva inexistente.

#### **CTX-ROT-ATH-05 — ATH-G4-02**

Agenda, ATH-G4-03 Treinos, ATH-G4-04 Detalhe do Treino e ATH-G4-07 Perfil mantêm a hierarquia G4 original.

**Justificativa UX**: contextos competitivos não devem alterar telas cuja tarefa permanece estável.

**Ações em ROTINA:** disponibilidade continua condicionada exclusivamente a aceita\_resposta; competição permanece consulta; nenhuma ação nova é criada pelo contexto.

**Fallback ROTINA:** sem próximo treino, B1 usa o próximo evento publicável pertinente se existir; sem evento publicável, mostrar ausência útil, não inventar compromisso.

### TREINADOR — mudanças em ROTINA

CTX-ROT-COACH-01 — COACH-G4-01

B1 Fila de atenção continua P0 apenas quando há pendência acionável; sem pendência, B2 Próximo Treino assume o contexto principal. Justificativa UX: a Central não precisa mostrar um alerta vazio e deve responder rapidamente qual é a próxima operação real.

CTX-ROT-COACH-02 — COACH-G4-01

B3 Disponibilidade e B4 Composição permanecem associados ao próximo treino; B5 Competição/prazo fica P2, B6 Resultado P3. Justificativa UX: mantém a Central orientada ao treino e evita transformar rotina em painel de temporada.

CTX-ROT-COACH-03 — COACH-G4-01

B7 Qualidade só sobe para P0 se o problema bloquear decisão atual; caso contrário fica PC/P3. Justificativa UX: evita que diagnóstico técnico concorra permanentemente com a operação esportiva.

#### **CTX-ROT-COACH-04 — COACH-G4-03**

Agenda mantém eventos e prazos em ordem temporal normal; COACH-G4-07 Competições mantém cronologia operacional; COACH-G4-09 Resultados permanece área analítica sob demanda. Justificativa UX: cada tela preserva seu job-to-be-done sem promoção contextual desnecessária.

#### **CTX-ROT-COACH-05 — COACH-G4-02**

Treino, COACH-G4-04 Equipe, COACH-G4-05 Detalhe da Atleta, COACH-G4-06 Mais e COACH-G4-10 Qualidade mantêm hierarquia G4 original. Justificativa UX: contexto competitivo não deve contaminar telas estáveis.

Ações em ROTINA: consulta e drill-down existentes; nenhuma escrita adicional de convocação, jogo ou resultado é criada.

Fallback ROTINA: se não houver próximo treino canônico, Central não fabrica um; promove o próximo compromisso operacional existente ou usa estado vazio apropriado.

## CTX-02 — PRÉ-COMPETIÇÃO

### Definição

PRÉ-COMPETIÇÃO representa preparação ativa para uma competição futura relevante. Não é uma janela arbitrária de N dias: depende de sinal operacional canônico.

### ATLETA — mudanças em PRÉ-COMPETIÇÃO

CTX-PRE-ATH-01 — ATH-G4-01 B2 Próxima competição/situação pessoal sobe de P2 para P1 e pode ir para ordem 1 quando não existir B1 com ação P0. Justificativa UX: a atleta precisa entender que a competição passou de referência futura para compromisso em preparação sem perder uma disponibilidade urgente de treino.

CTX-PRE-ATH-02 — Se ATH-G4-01 B1 possuir disponibilidade pendente para treino elegível, B1 permanece P0 antes de B2. Justificativa UX: contexto competitivo não pode esconder a única ação transacional da atleta nem reduzir taxa de resposta.

CTX-PRE-ATH-03 — ATH-G4-01 B3 Agenda permanece P2, mas prioriza no resumo os compromissos publicáveis ligados à preparação; B4 Resultado continua P3. Justificativa UX: preparação exige orientação temporal, enquanto campanha passada ainda é secundária.

CTX-PRE-ATH-04 — ATH-G4-05 B1 promove a competição-foco dentro do conjunto relevante e B2 torna explícito o estado de participação sem convertê-lo em confirmação. Justificativa UX: reduz dúvida sobre “esta é a competição que importa agora?” e evita falsas certezas.

CTX-PRE-ATH-05 — ATH-G4-06 B2 Minha Convocação sobe para P0/P1 quando existe decisão nominal publicada; B3 Programação sobe para P1/P2; B4 Resultados permanece P3; B1 Identidade continua primeiro como âncora. Justificativa UX: antes da etapa, a principal necessidade pessoal é saber a própria situação e a programação, não revisar resultados que ainda não existem.

CTX-PRE-ATH-06 — Se convocação própria não estiver publicada/autorizada, B2 desaparece em vez de mostrar “não convocada” por ausência de dado. Justificativa UX: ausência de registro não pode ser interpretada como decisão negativa e evita ansiedade causada por inferência falsa.

CTX-PRE-ATH-07 — ATH-G4-02 Agenda não vira tela de competição; apenas mantém eventos relacionados na ordem temporal normal. Justificativa UX: preserva previsibilidade da agenda e evita duplicação da tela de competição.

Ações em PRÉ-COMPETIÇÃO: atleta continua somente consultando competição/convocação; disponibilidade de treino mantém sua regra própria. Nenhuma confirmação de convocação é inventada.

Fallback PRÉ-COMPETIÇÃO: sem convocação ou programação publicável, mostrar somente participação e dados confirmados; se nenhum sinal publicável ativo existir, a Home da atleta retorna a ROTINA mesmo que o detalhe local da competição continue em estado ANTES.

### TREINADOR — mudanças em PRÉ-COMPETIÇÃO

CTX-PRE-COACH-01 — COACH-G4-01 B1 Fila de atenção incorpora prazos/pendências da competição como P0; B5 Competição/prazo sobe de P2 para P1/P0 conforme criticidade. Justificativa UX: o treinador precisa enxergar o que vence ou bloqueia a preparação antes de indicadores descritivos.

CTX-PRE-COACH-02 — COACH-G4-01 B2/B3/B4 Treino, disponibilidade e composição descem uma posição relativa, mas permanecem visíveis se houver treino próximo ou pendência P0. Justificativa UX: preparação competitiva muda o foco sem apagar a rotina de treino que sustenta a própria preparação.

CTX-PRE-COACH-03 — COACH-G4-03 B3 Prazos/pendências sobe para P0/P1 e pode anteceder eventos puramente informativos. Justificativa UX: deadline perdido tem custo operacional maior do que apenas saber que uma data existe.

CTX-PRE-COACH-04 — COACH-G4-07 B2 Prazos/pendências ganha precedência dentro da competição-foco; B1 mantém identidade/lista e B3 preserva estado de participação. Justificativa UX: organiza a lista pelo que precisa de ação sem abandonar a estrutura cronológica global.

CTX-PRE-COACH-05 — COACH-G4-08 B2 Prazos/Ações sobe para P0; B3 Convocação fica P1; B4 Programação sobe para P1/P2; B5 Resultado permanece P3; B6 Qualidade sobe para P0 apenas se bloquear prazo, convocação ou programação. Justificativa UX: a ordem acompanha a sequência real de preparação — resolver, saber quem vai, saber quando joga.

CTX-PRE-COACH-06 — COACH-G4-09 Resultados não é promovido por pré-competição; permanece analítico sob demanda. Justificativa UX: histórico pode apoiar decisão, mas não deve competir com tarefas administrativas e operacionais urgentes.

Ações em PRÉ-COMPETIÇÃO: abrir competição, convocação, prazo, agenda e qualidade; nenhuma edição de convocação/resultado é adicionada sem contrato/API explícitos.

Fallback PRÉ-COMPETIÇÃO: se não houver prazo, convocação, programação ou outro sinal interno ativo, Central volta a ROTINA; o detalhe da competição continua em ANTES apenas como contexto local.

## CTX-03 — DIA DO JOGO

### Definição

DIA DO JOGO é o estado de execução. Exige evidência canônica de jogo/programação do CEPRAEA no dia local atual ou estado operacional equivalente de DURANTE. Estar dentro de um intervalo multidiário, sozinho, não autoriza o app a inventar próximo jogo.

### ATLETA — mudanças em DIA DO JOGO

CTX-JOGO-ATH-01 — ATH-G4-01 B2 Competição/situação pessoal sobe para P0 e ordem 1 como contexto dominante. Justificativa UX: no dia de competição, a pergunta principal deixa de ser “quando é o próximo compromisso?” e passa a ser “o que está acontecendo agora?”.

CTX-JOGO-ATH-02 — ATH-G4-01 B1 Próximo compromisso/disponibilidade desce para P1/P2 quando se refere a treino futuro, mas não desaparece se houver ação pendente; a ação permanece acessível após o bloco de jogo. Justificativa UX: preserva obrigação futura sem tirar o foco do evento em execução.

CTX-JOGO-ATH-03 — ATH-G4-01 B4 Último resultado/campanha sobe de P3 para P1 quando existir resultado validado do dia; B3 Agenda desce para P3 e pode ser reduzida se repetir a programação já apresentada. Justificativa UX: entre jogos, último resultado tem valor imediato; uma segunda lista de agenda redundante aumenta ruído.

CTX-JOGO-ATH-04 — ATH-G4-06 B3 Programação/Próximo Jogo sobe para P0 e ordem 2 após B1; B4 Resultado sobe para P1 e vem logo depois; B2 Minha Convocação desce para P2/P3, permanecendo disponível mas fora do foco. Justificativa UX: depois de iniciada a etapa, saber o próximo jogo e o estado da campanha é mais útil do que repetir uma decisão de convocação já estabelecida.

CTX-JOGO-ATH-05 — ATH-G4-06 B5 Qualidade pública aparece somente quando a ausência/inconsistência impede exibir próximo jogo ou resultado; modifica o bloco afetado, sem diagnóstico técnico. Justificativa UX: comunica incerteza necessária sem expor linguagem administrativa nem fabricar placar.

CTX-JOGO-ATH-06 — ATH-G4-05 promove visualmente a competição em execução e rebaixa histórico. Justificativa UX: reduz o tempo de navegação até o evento ativo.

Ações em DIA DO JOGO: abrir Detalhe da Competição, consultar próximo jogo/programação e resultados; nenhuma escolha manual de jogo é criada quando o contexto já identifica a competição/jogo.

Fallback DIA DO JOGO: se o evento está em execução mas não há próximo jogo canônico, não inventar adversário/horário. Manter identidade da competição, último resultado válido se houver e mensagem pública de programação indisponível.

### TREINADOR — mudanças em DIA DO JOGO

CTX-JOGO-COACH-01 — COACH-G4-01 B5 Competição/contexto de jogo sobe para P0; B1 Fila de atenção permanece P0 apenas para pendências que afetam a execução; B6 Último resultado sobe para P1. Justificativa UX: a Central precisa virar uma porta rápida para a operação do jogo, não uma coleção de métricas gerais.

CTX-JOGO-COACH-02 — COACH-G4-01 B2/B3/B4 Treino, disponibilidade e composição descem para P2/P3, mantendo acesso sem competir com o jogo em andamento. Justificativa UX: durante a etapa, o próximo treino é importante, mas não deve ocupar o primeiro campo visual.

CTX-JOGO-COACH-03 — COACH-G4-01 B7 Qualidade sobe para P0 somente se o problema comprometer programação, adversário, placar ou decisão imediata; problemas não relacionados permanecem abaixo. Justificativa UX: severidade deve ser contextual ao risco operacional real.

CTX-JOGO-COACH-04 — COACH-G4-08 B4 Programação/Próximo Jogo sobe para P0; B5 Último resultado/campanha sobe para P1; B1 Identidade permanece âncora; B3 Convocação cai para P2/P3; B2 Prazos desaparece do fluxo principal quando resolvido/expirado e só permanece se ainda houver ação canônica válida. Justificativa UX: a hierarquia acompanha o ciclo real do dia — próximo jogo, estado atual, contexto — e remove tarefas pré-evento já encerradas.

CTX-JOGO-COACH-05 — COACH-G4-08 B6 Pendências de dados sobe para P0 se bloquear próximo jogo/resultado e aponta para COACH-G4-10. Justificativa UX: erro de dado durante competição precisa ser diagnosticável rapidamente quando afeta a operação, sem trazer toda a qualidade para a tela.

CTX-JOGO-COACH-06 — COACH-G4-03 Agenda prioriza o dia atual e os compromissos/jogos ativos, sem alterar a identidade de eventos; prazos resolvidos não são promovidos. Justificativa UX: reduz busca temporal no momento em que velocidade importa.

CTX-JOGO-COACH-07 — COACH-G4-09 Resultados, quando aberto a partir da competição ativa, prioriza a competição em contexto, mantendo filtros disponíveis. Justificativa UX: reduz retrabalho de selecionar novamente aquilo que o fluxo já sabe, preservando capacidade analítica.

Ações em DIA DO JOGO: navegar para competição, próximo jogo, resultados e diagnóstico de qualidade; escrita de resultado/convocação continua proibida até existir contrato mutável aprovado.

Fallback DIA DO JOGO: ausência de próximo jogo vira pendência de programação/dado, não adversário inventado. Resultado incompleto permanece explicitamente incompleto e não altera métricas finais.

## CTX-04 — PÓS-ETAPA

### Definição

PÓS-ETAPA é o estado de fechamento de uma competição concluída. Ele promove campanha final, resultado e pendências de fechamento sem transformar permanentemente a Home/Central em retrospectiva.

### ATLETA — mudanças em PÓS-ETAPA

CTX-POS-ATH-01 — ATH-G4-01 B4 Resultado/campanha sobe de P3 para P1 e pode ocupar ordem 1 quando não existir B1 com ação P0. Justificativa UX: imediatamente após uma etapa, o resultado coletivo é a informação esportiva mais relevante, mas não deve impedir uma tarefa operacional pendente.

CTX-POS-ATH-02 — ATH-G4-01 B1 Próximo compromisso retorna a P1/P0 conforme ação; B2 Próxima competição fica P2; B3 Agenda P2. Justificativa UX: o fechamento precisa coexistir com a continuidade do calendário sem prolongar artificialmente o modo competição.

CTX-POS-ATH-03 — ATH-G4-05 B3 Histórico promove a competição recém-encerrada dentro do histórico, enquanto futuras relevantes permanecem disponíveis. Justificativa UX: facilita encontrar a campanha recém-concluída sem inverter toda a organização cronológica do produto.

CTX-POS-ATH-04 — ATH-G4-06 B4 Resultados/campanha sobe para P0/P1 e ordem 2 após B1; B2 Convocação cai para P3; B3 Programação passa a referência/histórico P3. Justificativa UX: depois da etapa, o que importa é o desfecho; convocação e programação deixam de ser tarefas ativas.

CTX-POS-ATH-05 — Se resultado final estiver incompleto, B5 Qualidade pública aparece e B4 não assume linguagem conclusiva. Justificativa UX: evita celebrar/classificar uma campanha com dados ainda não sustentados.

Ações em PÓS-ETAPA: consultar campanha/resultados e retornar a próximos compromissos; nenhuma análise individual não reconciliada é introduzida.

Fallback PÓS-ETAPA: sem resultado final validado, mostrar competição encerrada com resultado pendente/indisponível em linguagem pública; Home pode retornar à ROTINA se não existir conteúdo pós-etapa confiável para promover.

### TREINADOR — mudanças em PÓS-ETAPA

CTX-POS-COACH-01 — COACH-G4-01 B6 Resultado/campanha sobe de P3 para P1; B2 Próximo Treino permanece P1 e pode voltar ao topo quando existir ação operacional P0 ligada ao treino. Justificativa UX: o treinador precisa fechar a etapa sem perder o próximo ciclo de trabalho.

CTX-POS-COACH-02 — COACH-G4-01 B1 Fila de atenção passa a incluir somente pendências de fechamento realmente acionáveis; B5 próxima competição retorna a P2 salvo se já entrar em PRÉ-COMPETIÇÃO. Justificativa UX: evita manter tarefas pré-evento vencidas como urgências e permite transição limpa para o próximo ciclo.

CTX-POS-COACH-03 — COACH-G4-08 B5 Último resultado/campanha sobe para P0/P1; B3 Convocação e B4 Programação descem para P2/P3; B2 Prazos desaparece se resolvido e permanece apenas se houver pendência administrativa ainda válida. Justificativa UX: a tela passa de preparação/execução para fechamento sem perder rastreabilidade.

CTX-POS-COACH-04 — COACH-G4-08 B6 Qualidade sobe para P0 quando resultado/segmentos impedem fechar a campanha; caso contrário permanece PC. Justificativa UX: dado incompleto no fechamento afeta histórico e métricas e precisa ser resolvido antes de uma leitura conclusiva.

CTX-POS-COACH-05 — COACH-G4-09 B1 Resumo da campanha e B4 Jogos/segmentos ganham relevância para a competição recém-encerrada; B5 Qualidade acompanha qualquer parcial incompleto. Justificativa UX: o pós-etapa é o momento natural de revisão do coletivo, desde que os dados estejam válidos.

CTX-POS-COACH-06 — COACH-G4-03 Agenda volta a privilegiar próximos eventos; a competição encerrada permanece no histórico sem dominar a lista. Justificativa UX: impede que o fechamento atrapalhe a continuidade operacional.

Ações em PÓS-ETAPA: abrir campanha, resultados, jogos/segmentos e qualidade; nenhuma edição destrutiva ou correção automática de parcial é criada.

Fallback PÓS-ETAPA: se a competição estiver encerrada mas a campanha não puder ser calculada com segurança, mostrar fechamento com dados pendentes no treinador e direcionar para Qualidade; não inferir placares nem métricas finais.

## MATRIZ RESUMIDA DE PROMOÇÃO / REBAIXAMENTO

ATH-G4-01 Início — ROTINA: B1 > B2 > B3 > B4. PRÉ: B1 P0 se acionável; caso contrário B2 assume topo; B3 apoio; B4 histórico. JOGO: B2 > B4 > B1 > B3, preservando eventual ação P0 de B1. PÓS: B1 P0 se acionável; caso contrário B4 > B1 > B2/B3.

ATH-G4-06 Detalhe da Competição — PRÉ: B1 > B2 > B3 > B4, com B5 condicional. JOGO: B1 > B3 > B4 > B2, com B5 junto do dado afetado. PÓS: B1 > B4 > B3/B2, com B5 se fechamento incompleto.

COACH-G4-01 Central — ROTINA: B1 acionável > B2/B3/B4 > B5 > B6, B7 contextual. PRÉ: B1 + B5 dominam; B2/B3/B4 descem; B6 histórico. JOGO: B1 bloqueante + B5 dominam; B6 sobe; B2/B3/B4 descem. PÓS: B1 de fechamento quando existir; B6 sobe; B2 retoma peso; B5 aponta próximo ciclo.

COACH-G4-08 Detalhe da Competição — PRÉ: B1 > B2 > B3 > B4 > B5. JOGO: B1 > B4 > B5 > B3; B2 só se ainda acionável. PÓS: B1 > B5 > B4/B3; B2 só se pendência administrativa válida. B6 sempre sobe para P0 quando bloquear o dado dominante.

Telas estáveis — ATH-G4-03 Treinos, ATH-G4-04 Detalhe do Treino, ATH-G4-07 Perfil, COACH-G4-02 Treino, COACH-G4-04 Equipe, COACH-G4-05 Detalhe da Atleta, COACH-G4-06 Mais e a estrutura interna de COACH-G4-10 Qualidade não mudam de ordem por contexto competitivo; apenas sua posição de acesso a partir de Home/Central pode mudar.

Justificativa UX: limitar a reordenação às telas em que o contexto realmente muda o job-to-be-done preserva memória espacial e reduz sensação de interface instável.

## REGRAS DE AÇÃO CONTEXTUAL

1\. Contexto nunca autoriza escrita sozinho. Disponibilidade continua dependente de aceita\_resposta; convocação e resultados continuam consulta na V1 até contrato mutável explícito.

2\. Contexto não altera visibilidade de dados sensíveis. ATLETA\_PUBLICO, TREINADOR\_INTERNO e SENSIVEL\_RESTRITO permanecem normativos.

3\. Ação já resolvida deve perder prioridade; ação indisponível não deve parecer habilitada.

4\. Ao navegar de um bloco contextual para detalhe, o contexto conhecido deve ser preservado para evitar que o usuário tenha de reencontrar competição/período, sem transformar contexto em critério de autorização.

5\. Se duas situações P0 coexistirem, prioridade segue risco e necessidade de ação: bloqueio do evento em execução > ação com prazo canônico > disponibilidade pendente > informação sem ação. Em empate sem regra canônica, ambas permanecem na fila de atenção em vez de o sistema escolher silenciosamente.

Justificativa UX: ações coerentes com estado real reduzem toque inútil, evitam expectativas falsas e impedem que uma mudança de contexto crie permissões que o produto não possui.

## GATE DE SAÍDA — SEÇÃO 6 / G3-G4

Os Estados Contextuais atingem G3/G4 quando os quatro contextos possuem gatilho de entrada e saída verificável, precedência, telas afetadas, promoção/rebaixamento/ocultação explícita, ações permitidas, fallback e justificativa UX individual para cada mudança; quando contexto global e local permanecem separados; e quando ausência de dado nunca ativa contexto ou conteúdo por inferência. Status desta execução: ESTADOS CONTEXTUAIS G3/G4 ESPECIFICADOS. Próxima dependência: Seção 7 — Contratos de Tela e Interação G5, que deve transformar cada bloco acionável e cada transição contextual em estados de interação, feedback, sucesso, erro, indisponibilidade e retorno.

## 

## 7\. E podemos ser ainda mais rigorosos

Antes de gerar qualquer novo mockup, eu definiria para cada tela:

### FUNÇÃO

Por que essa tela existe?

### DADO

Qual contrato/fonte a alimenta?

### AÇÃO

O que o usuário pode fazer?

### PRIORIDADE

O que precisa aparecer primeiro?

### PRIVACIDADE

Quem pode ver?

### ESTADO

Loading / vazio / erro / offline / pendente

### COMPOSIÇÃO

Que linguagem visual representa melhor essa tarefa?

Assim uma decisão de design deixa de ser:

*“coloque um card aqui porque dashboard normalmente tem card”.*

e passa a ser:

*“essa informação precisa ser agrupada porque pertence ao mesmo evento e possui uma ação”.*

É uma diferença enorme.

# EXECUÇÃO G5 — CONTRATOS DE TELA E INTERAÇÃO

## Escopo e taxonomia de estados

Esta execução transforma as 17 telas funcionais ATH-G4-\* e COACH-G4-\* em contratos G5 verificáveis. AUTH-G3-\* permanece fora desta matriz porque autenticação é fluxo compartilhado e não foi decomposta como Dashboard no G4. G5 define comportamento observável, feedback, retorno e indisponibilidade; não define cor, tipografia, ícone, radius, componente React ou animação final.

## Estados canônicos G5

LOADING — leitura ou mutação em andamento; o sistema ainda não possui evidência suficiente para afirmar o estado final. Nunca inferir conteúdo durante loading.

VAZIO — requisição concluída com sucesso e ausência válida de registros aplicáveis. Vazio não é erro.

ERRO — falha técnica, validação, conflito ou resposta inválida que impede concluir a operação. Deve existir caminho de recuperação quando seguro.

OFFLINE — conectividade indisponível. Leitura em cache só pode aparecer como dado anteriormente validado e identificado como não atualizado; escrita fica indisponível na V1, pois não existe contrato de fila offline aprovado.

PENDÊNCIA — estado de negócio incompleto ou ação ainda não resolvida, como SEM\_RESPOSTA, convocação não publicada, prazo em aberto ou dado aguardando fechamento. Pendência não é loading e não é erro.

SUCESSO — dado/ação confirmado pela fonte canônica e autorizado para a sessão. Sucesso de escrita só existe após confirmação do servidor.

INDISPONIBILIDADE — função, dado ou ação não pode ser usada por autorização, ciclo de vida, publicação, inexistência de contrato ou regra operacional; não deve parecer habilitada.

## Regras transversais G5

1\. LOADING, VAZIO, ERRO, OFFLINE, PENDÊNCIA, SUCESSO e INDISPONIBILIDADE são estados semânticos; a direção visual definirá sua aparência depois.

2\. A interface pode carregar blocos progressivamente, mas não pode mudar prioridade com base em dado ainda não resolvido.

3\. Erro localizado em um domínio não deve derrubar blocos independentes já válidos, salvo quando comprometer a identidade/autorização da tela.

4\. Dados em cache nunca autorizam escrita nem transição contextual nova. Contexto global é resolvido apenas com evidência canônica atual.

5\. Toda ação mutável possui estado inicial → envio/loading → confirmação de sucesso ou erro → retorno ao mesmo contexto. Duplo envio deve ser bloqueado enquanto a primeira mutação estiver pendente.

6\. Sucesso de navegação preserva origem, competição/evento e filtros quando isso reduz retrabalho, sem usar esse contexto como autorização.

7\. Privacidade é aplicada antes da composição: dado não autorizado não entra em loading, vazio, erro ou placeholder que revele sua existência.

8\. INDISPONIBILIDADE deve explicar a razão apenas no nível permitido ao perfil; códigos internos e diagnósticos não aparecem para atleta.

## ATLETA — CONTRATOS G5 POR TELA

### ATH-G5-01 — INÍCIO | deriva de ATH-G4-01

FUNÇÃO — Loading: responder à pergunta central fica temporariamente suspenso sem promover bloco por inferência; Vazio: orientar ausência de compromisso/ação publicável; Erro: manter navegação e indicar que o resumo não pôde ser atualizado; Offline: oferecer último resumo validado somente leitura quando existir; Pendência: tornar a própria ação pendente explícita; Sucesso: responder “o que vem agora e preciso fazer algo?”; Indisponibilidade: bloquear conteúdo se sessão/vínculo não autorizar.

DADO — Loading: eventos, disponibilidade própria, competição e resultado podem resolver separadamente; Vazio: ausência válida de próximo evento/competição/resultado não gera placeholder obrigatório; Erro: cada domínio falho é marcado sem inventar substituto; Offline: dado cacheado mantém referência temporal; Pendência: SEM\_RESPOSTA, convocação não publicada ou resultado incompleto preservam o estado real; Sucesso: somente projeções e exports canônicos; Indisponibilidade: dado interno/sensível é omitido.

AÇÃO — Loading: responder disponibilidade fica desabilitado até evento e aceita\_resposta serem confirmados; Vazio: ação principal vira navegar para Agenda quando útil; Erro: permitir tentar novamente sem perder contexto; Offline: escrita bloqueada; Pendência: SIM/TALVEZ/NAO disponível somente para treino elegível; Sucesso: confirmar resposta salva e atualizar projeção na Home; Indisponibilidade: janela encerrada/cancelamento exibe leitura sem botão ativo.

PRIORIDADE — Loading: preservar ordem contextual anterior segura; Vazio: remover blocos opcionais vazios; Erro: erro de um bloco não sobe acima de P0 real salvo se impedir a ação; Offline: não promover dado antigo a P0 por contexto; Pendência: disponibilidade própria mantém P0 conforme Seção 6; Sucesso: aplicar matriz ROTINA/PRÉ/JOGO/PÓS; Indisponibilidade: bloco sem ação cai para leitura ou desaparece.

PRIVACIDADE — Loading: não antecipar existência de convocação ou dado restrito; Vazio: ausência não significa resposta negativa; Erro: mensagem não revela outras atletas nem fonte interna; Offline: cache contém só dados autorizados da sessão; Pendência: somente pendências próprias/publicáveis; Sucesso: ATLETA\_PUBLICO + contexto próprio; Indisponibilidade: dados de terceiros, qualidade e observações internas não renderizam.

ESTADOS — Loading: shell/navegação estáveis e blocos ainda não resolvidos; Vazio: Home útil sem compromisso fabricado; Erro: parcial ou total conforme domínio; Offline: leitura degradada identificada; Pendência: ação/estado de negócio visível; Sucesso: resumo canônico atualizado; Indisponibilidade: sessão inválida redireciona para fluxo seguro.

COMPOSIÇÃO — Loading: preservar a sequência sem preencher conteúdo fictício; Vazio: deixar somente orientação/navegação necessárias; Erro: erro fica junto do bloco afetado; Offline: indicação de desatualização acompanha a informação; Pendência: bloco acionável domina sem virar modal obrigatório; Sucesso: blocos seguem hierarquia contextual; Indisponibilidade: espaço do bloco pode colapsar quando sua ausência não exige explicação.

### ATH-G5-02 — AGENDA | deriva de ATH-G4-02

FUNÇÃO — Loading: preparar orientação temporal sem afirmar eventos; Vazio: informar que não há eventos publicáveis no período; Erro: diferenciar falha de carregamento de agenda vazia; Offline: mostrar período cacheado somente leitura se disponível; Pendência: eventos podem trazer estado próprio pendente sem tornar a tela inteira pendente; Sucesso: listar compromissos publicáveis por evento\_id; Indisponibilidade: bloquear acesso se perfil não autorizado.

DADO — Loading: período e eventos resolvem sem duplicar itens; Vazio: zero eventos válidos; Erro: falha de calendário/API; Offline: lista cacheada com marca temporal; Pendência: status ou resposta própria incompletos permanecem no item; Sucesso: múltiplos eventos no mesmo dia preservados; Indisponibilidade: eventos exibir\_agenda=NAO ou não publicáveis não entram.

AÇÃO — Loading: mudança de período pode aguardar resolução atual quando houver risco de concorrência; Vazio: permitir trocar período; Erro: tentar novamente; Offline: navegar apenas entre dados cacheados disponíveis, sem resposta transacional; Pendência: abrir detalhe para resolver ação; Sucesso: selecionar evento; Indisponibilidade: ação inline de disponibilidade continua fora da V1 até contrato G5 específico posterior.

PRIORIDADE — Loading: orientação temporal permanece P1; Vazio: empty state substitui timeline; Erro: recuperação assume prioridade funcional sem ocultar período; Offline: contexto atual precede navegação ampla; Pendência: status do item não transforma toda agenda em P0; Sucesso: timeline domina; Indisponibilidade: itens ocultos não deixam lacunas.

PRIVACIDADE — Loading: não revelar quantidade de eventos ocultos; Vazio: “sem eventos” significa sem eventos publicáveis para a atleta; Erro: sem diagnóstico interno; Offline: cache filtrado pela sessão; Pendência: somente estado próprio; Sucesso: ATLETA\_PUBLICO; Indisponibilidade: competições de auditoria/não participação permanecem fora.

ESTADOS — Loading: timeline ainda não resolvida; Vazio: período sem eventos; Erro: falha técnica; Offline: histórico local identificável; Pendência: item com ação/estado incompleto; Sucesso: agenda navegável; Indisponibilidade: evento individual pode existir em backend e não estar disponível à atleta.

COMPOSIÇÃO — Loading: manter cabeçalho de período e espaço sem simular linhas reais; Vazio: mensagem + ação de mudar período; Erro: mensagem + retry; Offline: indicador persistente no escopo da lista; Pendência: marca semântica dentro do item; Sucesso: lista/timeline; Indisponibilidade: item não renderiza.

### ATH-G5-03 — TREINOS | deriva de ATH-G4-03

FUNÇÃO — Loading: resolver próximos/histórico; Vazio: distinguir “sem próximos” de “sem histórico”; Erro: permitir recuperar o conjunto afetado; Offline: consultar lista cacheada; Pendência: treino pode existir com conteúdo ainda não publicado; Sucesso: organizar sessões; Indisponibilidade: histórico não publicável não aparece.

DADO — Loading: eventos/treinos; Vazio: conjunto selecionado sem registros; Erro: leitura falhou; Offline: dados previamente validados; Pendência: conteudo\_publicado ausente não invalida o treino; Sucesso: treino e estado canônicos; Indisponibilidade: conteúdo interno excluído.

AÇÃO — Loading: controle próximos/histórico pode permanecer, mas abertura aguarda item válido; Vazio: alternar conjunto; Erro: retry; Offline: abrir detalhe cacheado se disponível, sem escrita; Pendência: abrir treino mesmo sem plano publicado; Sucesso: abrir treino; Indisponibilidade: ação inexistente para treino não publicável.

PRIORIDADE — Loading: controle temporal antes do conjunto; Vazio: empty state substitui lista; Erro: recuperação local; Offline: não promover histórico antigo; Pendência: próximo treino continua P1; Sucesso: próximos > histórico; Indisponibilidade: bloco removido.

PRIVACIDADE — Loading: sem placeholders de conteúdo técnico; Vazio: não revela registros internos; Erro: genérico; Offline: cache público; Pendência: “plano ainda não publicado” somente se útil; Sucesso: ATLETA\_PUBLICO; Indisponibilidade: observações internas nunca aparecem.

ESTADOS — Loading: lista em resolução; Vazio: subconjunto vazio; Erro: leitura indisponível; Offline: consulta degradada; Pendência: treino válido com informação parcial publicável; Sucesso: lista válida; Indisponibilidade: treino fora da política de publicação.

COMPOSIÇÃO — Loading: manter seletor e estrutura temporal; Vazio: mensagem específica ao subconjunto; Erro: retry localizado; Offline: indicação de cache; Pendência: item continua navegável; Sucesso: lista; Indisponibilidade: não reservar espaço.

### ATH-G5-04 — DETALHE DO TREINO | deriva de ATH-G4-04

FUNÇÃO — Loading: resolver identidade do evento antes da ação; Vazio: detalhe só é vazio quando evento válido não possui conteúdo opcional, nunca quando identidade falta; Erro: identidade inválida/falha crítica impede escrita; Offline: leitura cacheada, escrita bloqueada; Pendência: disponibilidade SEM\_RESPOSTA ou plano não publicado; Sucesso: permitir consultar e responder quando elegível; Indisponibilidade: evento cancelado, encerrado ou sem aceita\_resposta mantém consulta conforme regra.

DADO — Loading: evento, projeção própria e plano podem carregar progressivamente após identidade; Vazio: plano ausente é ausência válida quando não publicado; Erro: conflito de evento/projeção não pode virar resposta presumida; Offline: última projeção cacheada não é confirmação atual; Pendência: SEM\_RESPOSTA é estado próprio; Sucesso: evento + projeção canônica + conteúdo ATLETA\_PUBLICO; Indisponibilidade: conteúdo interno omitido.

AÇÃO — Loading: SIM/TALVEZ/NAO desabilitado até evento e estado atual serem conhecidos; Vazio: sem plano não afeta disponibilidade; Erro: falha ao salvar mantém estado anterior confirmado e informa que a nova escolha não foi salva; Offline: não permite salvar; Pendência: após toque, entrar em envio e bloquear duplicidade; Sucesso: resposta confirmada pelo servidor, projeção atualizada e feedback breve; Indisponibilidade: janela encerrada mostra valor atual somente leitura.

PRIORIDADE — Loading: B1 identidade precede qualquer mutação; Vazio: plano não ocupa prioridade; Erro: falha de escrita fica junto de B2; Offline: B2 informa indisponibilidade sem dominar além do necessário; Pendência: B2 P0; Sucesso: B2 cai para P2 se resolvido; Indisponibilidade: B3 pode subir após janela encerrada se publicado.

PRIVACIDADE — Loading: não buscar/mostrar outras atletas; Vazio: sem inferir equipe; Erro: não mostrar chaves internas; Offline: cache só próprio/público; Pendência: somente própria resposta; Sucesso: própria projeção + plano público; Indisponibilidade: observação técnica interna jamais aparece.

ESTADOS — Loading: evento/resposta em resolução; Vazio: conteúdo opcional ausente; Erro: leitura ou escrita distinguíveis; Offline: leitura sem mutação; Pendência: SEM\_RESPOSTA ou salvamento em andamento; Sucesso: resposta/consulta confirmadas; Indisponibilidade: ação bloqueada por ciclo de vida/regra.

COMPOSIÇÃO — Loading: identidade fixa primeiro, demais regiões progressivas; Vazio: omitir plano ou usar mensagem neutra quando necessário; Erro: mensagem adjacente à ação; Offline: estado de conexão próximo da área mutável; Pendência: controle mostra envio sem mudar para sucesso antecipadamente; Sucesso: confirmação não exige sair da tela; Indisponibilidade: substituir controles por estado somente leitura.

### ATH-G5-05 — COMPETIÇÕES | deriva de ATH-G4-05

FUNÇÃO — Loading: resolver conjunto relevante; Vazio: informar ausência de competições publicáveis relevantes; Erro: manter histórico válido se apenas próximas falharem; Offline: lista cacheada; Pendência: estado A\_CONFIRMAR/CONVIDADO permanece como tal; Sucesso: separar próximas de histórico; Indisponibilidade: competição sem participação/auditoria não entra na lista normal.

DADO — Loading: competições/participação; Vazio: zero relevantes; Erro: falha de fonte; Offline: valores anteriores identificados; Pendência: participação não confirmada nunca promovida; Sucesso: estados canônicos; Indisponibilidade: dado não publicável oculto.

AÇÃO — Loading: abrir item apenas quando identidade resolvida; Vazio: retorno/agenda; Erro: retry; Offline: abrir detalhe cacheado se existir; Pendência: consulta permitida; Sucesso: abrir competição; Indisponibilidade: sem CTA para entidade oculta.

PRIORIDADE — Loading: atuais/próximas antes do histórico; Vazio: empty state; Erro: recuperação local; Offline: sem promoções contextuais novas; Pendência: competição-foco pode subir apenas conforme Seção 6 e evidência cacheada não basta; Sucesso: aplicar contexto atual; Indisponibilidade: retirar item.

PRIVACIDADE — Loading: sem revelar convocações; Vazio: não sugere que não existem competições internas; Erro: linguagem pública; Offline: cache público; Pendência: estado da equipe publicável; Sucesso: coletivo público; Indisponibilidade: auditoria/registro interno fora.

ESTADOS — Loading: lista em resolução; Vazio: conjunto vazio; Erro: falha; Offline: cache; Pendência: participação incerta; Sucesso: lista; Indisponibilidade: item filtrado.

COMPOSIÇÃO — Loading: preservar seções sem contagens falsas; Vazio: mensagem; Erro: retry; Offline: indicação global; Pendência: estado aparece no próprio item; Sucesso: próximas + histórico; Indisponibilidade: sem espaço residual.

### ATH-G5-06 — DETALHE DA COMPETIÇÃO | deriva de ATH-G4-06

FUNÇÃO — Loading: resolver identidade/contexto local antes de reordenar; Vazio: competição válida pode não ter convocação/programação/resultados; Erro: preservar blocos independentes válidos; Offline: consulta cacheada sem ativar novo contexto global; Pendência: convocação/programação/resultado incompletos permanecem explícitos; Sucesso: aplicar PRÉ/JOGO/PÓS aos mesmos blocos; Indisponibilidade: competição não publicável bloqueia detalhe.

DADO — Loading: participação, convocação própria, jogos e resultados progressivos; Vazio: ausência de convocação publicada não significa “não convocada”; Erro: placar/programação falhos não são inferidos; Offline: último estado conhecido; Pendência: a confirmar/resultado parcial; Sucesso: somente dados coletivos e próprios autorizados; Indisponibilidade: diagnóstico interno omitido.

AÇÃO — Loading: navegação interna aguarda identidade; Vazio: consultar o que existe e retornar; Erro: retry do bloco; Offline: leitura apenas; Pendência: nenhuma confirmação administrativa criada; Sucesso: abrir programação/resultado e navegar mantendo competitionId; Indisponibilidade: ações não contratadas permanecem ausentes.

PRIORIDADE — Loading: B1 identidade fixa, demais aguardam; Vazio: bloco opcional desaparece; Erro: B5 qualidade pública acompanha o dado afetado; Offline: mantém última ordem segura sem nova transição; Pendência: prioridades seguem Seção 6 sem transformar ausência em decisão; Sucesso: PRÉ B2/B3, JOGO B3/B4, PÓS B4; Indisponibilidade: tela pode retornar à lista segura.

PRIVACIDADE — Loading: não revelar existência de lista nominal de terceiros; Vazio: convocação ausente não gera estado negativo; Erro: sem códigos de qualidade; Offline: somente cache público/próprio; Pendência: própria convocação; Sucesso: ATLETA\_PUBLICO + próprio; Indisponibilidade: outras atletas e controles internos excluídos.

ESTADOS — Loading: contexto local não resolvido; Vazio: subdomínio sem registros; Erro: falha localizada/total; Offline: consulta degradada; Pendência: informação aguardando publicação/fechamento; Sucesso: detalhe canônico; Indisponibilidade: competição/parte não autorizada.

COMPOSIÇÃO — Loading: B1 permanece âncora; Vazio: não criar containers para dados inexistentes; Erro: aviso público junto do bloco; Offline: indicador de desatualização; Pendência: linguagem não conclusiva; Sucesso: ordem contextual G3/G4; Indisponibilidade: remover ou substituir por mensagem de acesso quando necessário.

### ATH-G5-07 — PERFIL | deriva de ATH-G4-07

FUNÇÃO — Loading: resolver identidade/sessão; Vazio: campo esportivo opcional pode estar ausente sem invalidar conta; Erro: diferenciar falha de perfil de falha de autenticação; Offline: permitir consulta cacheada e logout local/sessão conforme capacidade, sem prometer operação remota; Pendência: redefinição de senha pertence ao fluxo AUTH; Sucesso: mostrar identidade/perfil e ações de sessão; Indisponibilidade: vínculo inválido encerra acesso esportivo.

DADO — Loading: conta + vínculo + perfil próprio; Vazio: posição/função opcional ausente usa estado neutro; Erro: não exibir dado parcial como definitivo; Offline: cache próprio; Pendência: atualização de credencial fora desta tela; Sucesso: dados próprios; Indisponibilidade: dados sensíveis excluídos.

AÇÃO — Loading: ações de segurança aguardam sessão; Vazio: logout continua possível; Erro: retry perfil ou sair; Offline: redefinição remota indisponível; Pendência: ao iniciar logout, bloquear duplicidade até conclusão local/servidor; Sucesso: logout retorna Login e limpa contexto protegido; Indisponibilidade: ação não contratada de editar perfil não aparece.

PRIORIDADE — Loading: identidade primeiro; Vazio: segurança continua após perfil; Erro: erro de sessão domina; Offline: sessão/segurança precede dados esportivos se houver risco; Pendência: feedback de ação próximo da ação; Sucesso: identidade → perfil → segurança; Indisponibilidade: blocos sensíveis nunca ocupam espaço.

PRIVACIDADE — Loading: nenhum dado de outras atletas; Vazio: não revelar módulos futuros; Erro: não expor tokens; Offline: cache próprio; Pendência: fluxo de senha não mostra segredo; Sucesso: somente própria conta; Indisponibilidade: Wellness/Autoavaliação/outros excluídos.

ESTADOS — Loading: sessão/perfil; Vazio: dado esportivo opcional ausente; Erro: conta/perfil; Offline: consulta degradada; Pendência: ação de sessão; Sucesso: perfil; Indisponibilidade: vínculo/feature.

COMPOSIÇÃO — Loading: manter estrutura de conta sem valores inventados; Vazio: campo opcional pode desaparecer; Erro: mensagem no domínio; Offline: indicação discreta; Pendência: ação mostra progresso; Sucesso: sport-first; Indisponibilidade: não criar atalhos inativos.

## TREINADOR — CONTRATOS G5 POR TELA

### COACH-G5-01 — CENTRAL | deriva de COACH-G4-01

FUNÇÃO — Loading: resolver atenção, treino e contexto competitivo sem fabricar urgência; Vazio: ausência de pendência é estado positivo e B1 pode desaparecer; Erro: manter blocos independentes válidos e sinalizar o que não pôde ser resolvido; Offline: mostrar último panorama validado somente leitura; Pendência: fila reúne somente itens de negócio acionáveis; Sucesso: responder “o que exige atenção agora?”; Indisponibilidade: sessão/perfil inválido bloqueia Central.

DADO — Loading: domínios podem carregar progressivamente; Vazio: zero pendências não vira alerta; Erro: conflito de fonte vira B7/qualidade quando aplicável; Offline: cache não cria P0 novo; Pendência: prazos, SEM\_RESPOSTA e fechamento incompleto permanecem fatos; Sucesso: dados canônicos agregados; Indisponibilidade: dados sensíveis fora do escopo não entram.

AÇÃO — Loading: drill-down só quando o alvo estiver resolvido; Vazio: abrir próximo treino/agenda; Erro: retry/abrir Qualidade quando seguro; Offline: navegação em cache, sem escrita; Pendência: abrir item P0; Sucesso: preservar origem ao voltar; Indisponibilidade: mutações de convocação/resultado não aparecem.

PRIORIDADE — Loading: manter última hierarquia segura; Vazio: B2 assume foco em ROTINA; Erro: erro bloqueante pode P0, erro informativo não; Offline: sem transição contextual nova; Pendência: regra de desempate da Seção 6; Sucesso: matriz ROTINA/PRÉ/JOGO/PÓS; Indisponibilidade: bloco cai/desaparece.

PRIVACIDADE — Loading: não antecipar dados restritos; Vazio: não expor ausência de módulos sensíveis; Erro: pode mostrar diagnóstico operacional permitido ao treinador, nunca segredo; Offline: cache interno protegido; Pendência: somente dados autorizados; Sucesso: TREINADOR\_INTERNO; Indisponibilidade: SENSIVEL\_RESTRITO fora da tela.

ESTADOS — Loading: panorama em resolução; Vazio: sem atenção; Erro: parcial/total; Offline: panorama desatualizado; Pendência: fila operacional; Sucesso: Central atual; Indisponibilidade: domínio/ação não disponível.

COMPOSIÇÃO — Loading: áreas mantêm ordem sem números fictícios; Vazio: B1 some e contexto dominante sobe; Erro: aviso junto do domínio; Offline: indicação global; Pendência: fila P0 no topo; Sucesso: attention-first; Indisponibilidade: não reservar containers vazios.

### COACH-G5-02 — PRÓXIMO TREINO / DETALHE DO TREINO | deriva de COACH-G4-02

FUNÇÃO — Loading: resolver evento\_id antes de composição; Vazio: treino válido pode ter zero respostas ou conteúdo vazio; Erro: falha de disponibilidade não invalida identidade do treino; Offline: leitura cacheada; Pendência: SEM\_RESPOSTA/cobertura indeterminada são estados de negócio; Sucesso: operar consulta nominal/composição; Indisponibilidade: sem próximo treino, destino primário mostra estado vazio seguro.

DADO — Loading: evento → disponibilidade → atletas → cobertura/conteúdo; Vazio: zero respostas é válido; Erro: contagens inconsistentes devem ser marcadas e não recalculadas silenciosamente; Offline: última composição identificada como desatualizada; Pendência: função INDEFINIDA/cobertura insuficiente; Sucesso: projeções atuais e cadastro canônico; Indisponibilidade: presença factual não derivada.

AÇÃO — Loading: filtros aguardam dados correspondentes; Vazio: filtrar não cria atletas; Erro: retry/Qualidade; Offline: filtros locais sobre cache permitidos, sem mutação; Pendência: selecionar SIM/TALVEZ/NAO/SEM\_RESPOSTA e abrir atleta; Sucesso: drill-down preserva filtro; Indisponibilidade: editar disponibilidade de atleta não existe na V1.

PRIORIDADE — Loading: B1 identidade primeiro; Vazio: B2/B3 continuam úteis para mostrar zero/sem respostas; Erro: B6/qualidade relacionada sobe só se bloquear decisão; Offline: cobertura tática perde força conclusiva; Pendência: lista nominal P0/P1; Sucesso: B2→B3→B4→B5→B6; Indisponibilidade: B5 oculto quando fonte não sustenta avaliação.

PRIVACIDADE — Loading: somente treinador; Vazio: sem exposição de Wellness; Erro: diagnóstico limitado ao domínio; Offline: cache interno protegido; Pendência: nomes/status autorizados; Sucesso: TREINADOR\_INTERNO; Indisponibilidade: módulos sensíveis e inferências não renderizam.

ESTADOS — Loading: composição em resolução; Vazio: grupos sem membros/conteúdo opcional vazio; Erro: domínio inconsistente; Offline: consulta degradada; Pendência: resposta/cobertura não resolvida; Sucesso: composição válida; Indisponibilidade: bloco tático ou ação não suportada.

COMPOSIÇÃO — Loading: evento fixa topo e demais blocos entram progressivamente; Vazio: grupos mostram zero quando isso informa decisão, não cards vazios; Erro: marcar bloco afetado; Offline: badge/estado de desatualização sem visual final prescrito; Pendência: agrupamento por status; Sucesso: cadeia disponibilidade→lista→composição→tática; Indisponibilidade: bloco condicional colapsa.

### COACH-G5-03 — AGENDA | deriva de COACH-G4-03

FUNÇÃO — Loading: resolver período/eventos/prazos; Vazio: ausência de compromissos no período; Erro: diferenciar falha de eventos e falha de prazos; Offline: agenda cacheada; Pendência: prazos continuam pendências de negócio; Sucesso: visão temporal operacional; Indisponibilidade: domínio específico sem fonte válida não é inventado.

DADO — Loading: eventos e prazos; Vazio: conjunto vazio; Erro: fonte falhou; Offline: cache temporal; Pendência: prazo/criticidade aberto; Sucesso: evento\_id e compromissos canônicos; Indisponibilidade: registro não aplicável pode ficar fora.

AÇÃO — Loading: filtros e troca de período devem evitar corrida de respostas; Vazio: mudar período; Erro: retry; Offline: filtros locais e abertura de cache; Pendência: abrir competição/contexto; Sucesso: selecionar evento; Indisponibilidade: nenhuma escrita de prazo é criada.

PRIORIDADE — Loading: orientação temporal P1; Vazio: empty; Erro: recuperação local; Offline: dia atual cacheado sem promover contexto novo; Pendência: prazo P0/P1 conforme criticidade; Sucesso: lista operacional; Indisponibilidade: item omitido.

PRIVACIDADE — Loading: treinador; Vazio: não expor dados sensíveis; Erro: pode indicar domínio/fonte sem segredo; Offline: cache interno; Pendência: prazos autorizados; Sucesso: TREINADOR\_INTERNO; Indisponibilidade: dados fora do escopo não entram.

ESTADOS — Loading: consulta temporal; Vazio; Erro; Offline; Pendência; Sucesso; Indisponibilidade por domínio.

COMPOSIÇÃO — Loading: período estável + região de lista; Vazio: mensagem; Erro: retry por domínio; Offline: indicador global; Pendência: prazo intercalado/associado; Sucesso: timeline operacional; Indisponibilidade: sem placeholder.

### COACH-G5-04 — EQUIPE | deriva de COACH-G4-04

FUNÇÃO — Loading: resolver elenco/vínculos; Vazio: nenhum vínculo ativo é estado válido e crítico; Erro: falha de elenco bloqueia busca; Offline: lista cacheada somente leitura; Pendência: presença factual não consolidada não vira frequência; Sucesso: localizar atleta; Indisponibilidade: indicador de frequência ausente até fonte válida.

DADO — Loading: atletas/vínculos/funções; Vazio: zero atletas ativas; Erro: inconsistência de vínculo; Offline: cadastro anterior; Pendência: INDEFINIDA é valor, não erro; Sucesso: elenco canônico; Indisponibilidade: frequência não sustentada omitida.

AÇÃO — Loading: busca/filtro pode aguardar lista; Vazio: limpar filtros quando o vazio for causado por filtro; Erro: retry; Offline: busca/filtros locais no cache; Pendência: abrir atleta continua possível; Sucesso: filtro/abrir detalhe; Indisponibilidade: não editar cadastro na V1.

PRIORIDADE — Loading: busca depois de base mínima; Vazio: distinguir “sem atletas” de “filtro sem resultado”; Erro: erro de elenco P0 funcional; Offline: sem métricas conclusivas; Pendência: função INDEFINIDA não sobe urgência automaticamente; Sucesso: lista P1; Indisponibilidade: frequência PC some.

PRIVACIDADE — Loading: treinador; Vazio: sem módulos individuais sensíveis; Erro: sem dados privados além do necessário; Offline: cache interno; Pendência: só dados esportivos autorizados; Sucesso: TREINADOR\_INTERNO; Indisponibilidade: Wellness/Autoavaliação excluídos.

ESTADOS — Loading elenco; Vazio base/filtro; Erro; Offline; Pendência de dado factual; Sucesso; Indisponibilidade de módulo.

COMPOSIÇÃO — Loading: controles e lista sem linhas fictícias; Vazio: mensagem depende de base vs filtro; Erro: recuperação; Offline: status; Pendência: valor INDEFINIDA mostrado como valor válido; Sucesso: busca→lista→estrutura; Indisponibilidade: B4 não ocupa espaço.

### COACH-G5-05 — DETALHE DA ATLETA | deriva de COACH-G4-05

FUNÇÃO — Loading: resolver athleteId/vínculo; Vazio: posição secundária ou frequência podem ser ausentes; Erro: identidade inválida impede exibir dados cruzados; Offline: consulta cacheada; Pendência: presença ainda não consolidada; Sucesso: contexto esportivo/operacional; Indisponibilidade: módulos sensíveis fora.

DADO — Loading: identidade, vínculo, função/posição, presença factual; Vazio: subdomínio opcional; Erro: conflito de atleta/vínculo; Offline: cache; Pendência: frequência aguardando fonte factual; Sucesso: dados autorizados; Indisponibilidade: Wellness/questionários não são consultados.

AÇÃO — Loading: retorno preserva origem; Vazio: nenhuma ação artificial; Erro: voltar/retry; Offline: leitura; Pendência: consultar apenas fatos disponíveis; Sucesso: retorno a Equipe/Treino; Indisponibilidade: edição não contratada.

PRIORIDADE — Loading: identidade P1; Vazio: bloco opcional colapsa; Erro: identidade domina; Offline: presença não assume conclusividade; Pendência: B3 PC; Sucesso: B1→B2→B3; Indisponibilidade: B4 normativo não renderiza.

PRIVACIDADE — Loading: autorização por perfil antes dos dados; Vazio: não revela existência de respostas sensíveis; Erro: genérico/operacional; Offline: cache interno; Pendência: apenas esportivo/factual; Sucesso: treinador autorizado; Indisponibilidade: SENSIVEL\_RESTRITO excluído.

ESTADOS — Loading; Vazio parcial; Erro; Offline; Pendência factual; Sucesso; Indisponibilidade por escopo.

COMPOSIÇÃO — Loading: identidade antes dos detalhes; Vazio: remover seções opcionais; Erro: mensagem segura; Offline: indicador; Pendência: frequência não consolidada não vira zero; Sucesso: perfil esportivo enxuto; Indisponibilidade: nenhum espaço para módulos futuros.

### COACH-G5-06 — MAIS | deriva de COACH-G4-06

FUNÇÃO — Loading: resolver autorização dos destinos; Vazio: não deve existir como menu vazio; Erro: falha de autorização exige rota segura; Offline: destinos locais permanecem navegáveis se páginas cacheadas existirem, sem prometer dados; Pendência: ação de logout/senha pode ter progresso próprio; Sucesso: hub de navegação; Indisponibilidade: destino sem feature autorizada não aparece.

DADO — Loading: mapa de rotas/perfil; Vazio: módulos futuros não contam como itens; Erro: autorização; Offline: estrutura de menu pode persistir; Pendência: sessão; Sucesso: destinos válidos; Indisponibilidade: feature flags/escopo removem destino.

AÇÃO — Loading: não abrir destino não autorizado; Vazio: conta/sessão continuam; Erro: logout seguro; Offline: navegação possível conforme cache, redefinição remota indisponível; Pendência: logout bloqueia repetição; Sucesso: navegar; Indisponibilidade: item não clicável não deve ser exibido como ativo.

PRIORIDADE — Loading: destinos operacionais antes de conta; Vazio: não preencher com atalhos inativos; Erro: segurança domina; Offline: conta continua abaixo; Pendência: ação corrente recebe feedback local; Sucesso: B1→B2; Indisponibilidade: B3 não renderiza.

PRIVACIDADE — Loading: não revelar módulos futuros; Vazio: idem; Erro: sem tokens; Offline: menu autorizado da sessão; Pendência: conta própria; Sucesso: treinador; Indisponibilidade: itens restritos ausentes.

ESTADOS — Loading autorização; Vazio apenas se nenhum destino operacional além de conta, tratado sem criar placeholders; Erro; Offline; Pendência de sessão; Sucesso; Indisponibilidade de destino.

COMPOSIÇÃO — Loading: estrutura simples; Vazio: não virar mini-dashboard; Erro: ação de sair; Offline: indicador discreto; Pendência: progresso junto da ação; Sucesso: lista de destinos; Indisponibilidade: item removido.

### COACH-G5-07 — COMPETIÇÕES | deriva de COACH-G4-07

FUNÇÃO — Loading: resolver competições/prazos; Vazio: nenhuma competição ativa/próxima; Erro: preservar histórico se possível; Offline: lista cacheada; Pendência: prazos/participação a confirmar são fatos; Sucesso: localizar competição e ação necessária; Indisponibilidade: ausência de fonte de prazo não gera prazo fictício.

DADO — Loading: competição + participação + prazo; Vazio: conjunto sem registros; Erro: domínio falhou; Offline: cache; Pendência: A\_CONFIRMAR/CONVIDADO e prazo aberto; Sucesso: estados canônicos; Indisponibilidade: dado não disponível omitido.

AÇÃO — Loading: abrir após identidade; Vazio: retorno/agenda; Erro: retry; Offline: abrir cache; Pendência: abrir detalhe; Sucesso: abrir competição; Indisponibilidade: edição de participação/prazo não criada.

PRIORIDADE — Loading: seções sem contagem falsa; Vazio: empty; Erro: recuperação; Offline: não promover competição a PRÉ/JOGO por cache; Pendência: B2 P0/P1 conforme prazo; Sucesso: B1/B2/B3 > histórico; Indisponibilidade: bloco some.

PRIVACIDADE — Loading: treinador; Vazio: não expõe dados sensíveis; Erro: diagnóstico operacional limitado; Offline: cache interno; Pendência: prazos internos autorizados; Sucesso: TREINADOR\_INTERNO; Indisponibilidade: módulos restritos fora.

ESTADOS — Loading; Vazio; Erro; Offline; Pendência operacional; Sucesso; Indisponibilidade de subdomínio.

COMPOSIÇÃO — Loading: lista estável; Vazio: mensagem; Erro: retry; Offline: aviso; Pendência: prazo associado ao item; Sucesso: atuais/próximas→histórico; Indisponibilidade: sem placeholder.

### COACH-G5-08 — DETALHE DA COMPETIÇÃO | deriva de COACH-G4-08

FUNÇÃO — Loading: resolver identidade e contexto local antes da ordem operacional; Vazio: subdomínios como prazo/convocação/programação podem estar ausentes; Erro: manter blocos independentes e elevar qualidade quando afeta decisão; Offline: consulta cacheada sem autorizar transição contextual nova; Pendência: prazo, convocação, programação ou fechamento incompletos; Sucesso: operar consulta em PRÉ/JOGO/PÓS; Indisponibilidade: mutações não contratadas ausentes.

DADO — Loading: competição, prazos, lista nominal, jogos, resultados, qualidade; Vazio: ausência válida não vira inferência; Erro: conflito/segmento incompleto permanece explícito; Offline: último snapshot; Pendência: dados em aberto; Sucesso: fontes canônicas; Indisponibilidade: dado sensível fora do contrato.

AÇÃO — Loading: ações aguardam identidade; Vazio: navegar ao que existe; Erro: retry/Qualidade; Offline: leitura; Pendência: abrir prazo/convocação/resultados sem editar; Sucesso: preservar competitionId ao navegar; Indisponibilidade: botões de editar convocação/resultado não aparecem.

PRIORIDADE — Loading: B1 fixo; Vazio: bloco opcional colapsa; Erro: B6 P0 se bloquear dominante; Offline: última ordem segura; Pendência: PRÉ B2/B3, JOGO B4, PÓS B5 conforme Seção 6; Sucesso: ordem contextual; Indisponibilidade: tarefa vencida/resolvida sai do fluxo principal.

PRIVACIDADE — Loading: treinador; Vazio: não revela módulos sensíveis; Erro: diagnóstico técnico permitido apenas no nível necessário, com link à Qualidade; Offline: cache interno; Pendência: lista nominal autorizada; Sucesso: TREINADOR\_INTERNO; Indisponibilidade: SENSIVEL\_RESTRITO fora.

ESTADOS — Loading contexto; Vazio de subdomínio; Erro localizado; Offline; Pendência operacional; Sucesso; Indisponibilidade por ciclo de vida/contrato.

COMPOSIÇÃO — Loading: identidade primeiro; Vazio: sem containers vazios; Erro: B6 junto do bloco afetado; Offline: indicador global; Pendência: linguagem de tarefa aberta; Sucesso: ordem PRÉ/JOGO/PÓS; Indisponibilidade: ação resolvida perde affordance.

### COACH-G5-09 — RESULTADOS | deriva de COACH-G4-09

FUNÇÃO — Loading: resolver resumo/filtros/jogos; Vazio: não há jogos válidos para filtro atual; Erro: métricas inválidas não são exibidas como zero; Offline: análise cacheada identificada; Pendência: jogos com segmentos incompletos permanecem separados; Sucesso: analisar campanha validada; Indisponibilidade: participação individual continua fora da V1.

DADO — Loading: agregados + adversários + segmentos; Vazio: conjunto filtrado sem jogos; Erro: inconsistência bloqueia métricas afetadas; Offline: snapshot; Pendência: parciais incompletos; Sucesso: métricas canônicas; Indisponibilidade: dado individual não reconciliado omitido.

AÇÃO — Loading: filtros podem mostrar progresso e impedir combinações concorrentes; Vazio: limpar filtro; Erro: retry/Qualidade; Offline: filtros locais sobre cache; Pendência: abrir jogo/pendência quando rota definida; Sucesso: filtrar competição/adversário; Indisponibilidade: gráfico/feature sem pergunta contratada não entra.

PRIORIDADE — Loading: resumo não mostra números provisórios; Vazio: empty substitui análise; Erro: qualidade P0 se comprometer leitura; Offline: sem conclusões novas; Pendência: B5 acompanha; Sucesso: B1→B2→B3→B4; Indisponibilidade: bloco individual não ocupa espaço.

PRIVACIDADE — Loading: treinador; Vazio: não revela dados individuais; Erro: diagnóstico autorizado; Offline: cache interno; Pendência: coletiva; Sucesso: coletiva validada; Indisponibilidade: individual sensível/inconsistente excluído.

ESTADOS — Loading; Vazio por filtro/base; Erro; Offline; Pendência de dados; Sucesso; Indisponibilidade de análise não contratada.

COMPOSIÇÃO — Loading: estrutura sem métricas falsas; Vazio: mensagem + limpar filtros; Erro: marcador no resumo afetado; Offline: indicação; Pendência: parciais sinalizados na lista; Sucesso: resumo compacto + filtros + listas; Indisponibilidade: sem gráfico decorativo obrigatório.

### COACH-G5-10 — QUALIDADE DOS DADOS | deriva de COACH-G4-10

FUNÇÃO — Loading: resolver severidade e pendências; Vazio: “sem pendências” é sucesso de integridade, não ausência de tela; Erro: falha ao consultar qualidade deve ser explicitada; Offline: não declarar integridade atual a partir de cache; Pendência: itens técnicos ou cobertura de coleta aguardam resolução; Sucesso: separar erro técnico de coleta incompleta; Indisponibilidade: diagnóstico sem destino seguro permanece somente leitura.

DADO — Loading: validações/contratos; Vazio: zero problemas atuais confirmados; Erro: mecanismo de qualidade indisponível; Offline: snapshot histórico não usado como estado atual; Pendência: conflito, sync, parcial, coleta; Sucesso: severidade/fonte/entidade rastreáveis; Indisponibilidade: segredo/token nunca exposto.

AÇÃO — Loading: abrir contexto aguarda identificação segura; Vazio: nenhuma ação corretiva; Erro: retry; Offline: consulta histórica apenas; Pendência: abrir domínio afetado; Sucesso: navegar com contexto preservado; Indisponibilidade: correção automática não é oferecida sem contrato.

PRIORIDADE — Loading: não afirmar “OK”; Vazio: B5 comunica integridade atual; Erro: falha do próprio monitoramento sobe a atenção; Offline: estado atual fica desconhecido, não verde; Pendência: B2 por severidade, B3 separado; Sucesso: B1→B2/B3→B4; Indisponibilidade: item sem ação pode permanecer informativo.

PRIVACIDADE — Loading: treinador; Vazio: sem dados sensíveis; Erro: mensagem não revela segredo; Offline: cache interno; Pendência: IDs técnicos podem aparecer quando necessários ao diagnóstico do treinador, sem credenciais; Sucesso: TREINADOR\_INTERNO; Indisponibilidade: dados secretos sempre mascarados/ausentes.

ESTADOS — Loading de validação; Vazio/OK; Erro do monitoramento; Offline/estado atual desconhecido; Pendência técnica/coleta; Sucesso diagnóstico; Indisponibilidade de ação/destino.

COMPOSIÇÃO — Loading: severidade ainda indeterminada sem contagens falsas; Vazio: estado sem pendências substitui filas; Erro: falha do monitoramento em destaque; Offline: aviso de impossibilidade de afirmar atualidade; Pendência: técnicas e coleta em grupos distintos; Sucesso: severidade→filas→rastreabilidade; Indisponibilidade: item informativo sem CTA enganoso.

## CONTRATOS G5 DOS BLOCOS ACIONÁVEIS

### G5-ACT-01 — DISPONIBILIDADE DA ATLETA

Inicial: mostrar projeção atual própria e opções somente se aceita\_resposta=true.

Ação: selecionar SIM, TALVEZ ou NAO para o evento\_id identificado.

Loading/envio: manter contexto do evento, bloquear novo envio e não declarar sucesso antecipado.

Feedback: informar que a resposta está sendo salva sem substituir a projeção confirmada por dado não confirmado.

Sucesso: servidor confirma nova versão append-only e projeção atual; Home e Detalhe refletem o mesmo valor.

Erro: preservar a última projeção confirmada, explicar que a nova escolha não foi salva e permitir tentar novamente quando seguro.

Offline: escrita indisponível; não enfileirar silenciosamente.

Indisponibilidade: aceita\_resposta=false, evento encerrado/cancelado ou sessão inválida torna o controle somente leitura/ausente conforme contexto.

Retorno: permanecer no mesmo evento; não redirecionar para outra tela após salvar.

### G5-ACT-02 — ABRIR EVENTO/COMPETIÇÃO/TREINO

Inicial: item possui identidade canônica resolvida.

Ação: abrir detalhe pelo ID estável.

Loading: manter indicação do item de origem enquanto detalhe resolve.

Sucesso: detalhe abre preservando origem e contexto relevante.

Erro: permanecer/retornar à origem com item intacto e opção de tentar novamente.

Offline: abrir apenas detalhe cacheado disponível; não fingir atualização.

Indisponibilidade: item sem autorização/publicação não deve oferecer navegação ativa.

Retorno: restaurar posição/período/filtro da origem quando tecnicamente possível.

### G5-ACT-03 — FILTROS E CONTROLES DE PERÍODO

Inicial: filtro/período atual explicitamente conhecido.

Ação: alterar seleção.

Loading: quando depender de rede, indicar atualização sem apagar prematuramente o conjunto anterior válido.

Sucesso: novo conjunto substitui o anterior e o filtro permanece visível.

Vazio: mostrar zero resultados no filtro com ação de limpar/alterar.

Erro: manter filtro escolhido e permitir retry; não retornar silenciosamente ao padrão.

Offline: filtros locais sobre cache podem funcionar; novo período sem cache fica indisponível.

Retorno: ao voltar de detalhe, restaurar filtro/período.

### G5-ACT-04 — DRILL-DOWN NOMINAL DO TREINADOR

Inicial: agregado e grupo selecionável conhecidos.

Ação: selecionar SIM/TALVEZ/NAO/SEM\_RESPOSTA ou abrir atleta.

Loading: lista nominal resolve sem alterar o agregado conhecido.

Sucesso: grupo mostra atletas canônicas; abertura de atleta preserva grupo de origem.

Vazio: grupo com zero atletas deve ser explicitamente zero quando isso é operacionalmente relevante.

Erro: não recalcular grupo por inferência; permitir retry.

Offline: usar snapshot com desatualização identificada.

Indisponibilidade: dado individual sem autorização ou domínio não consolidado não oferece drill-down.

### G5-ACT-05 — LOGOUT / SEGURANÇA

Inicial: sessão válida.

Ação: logout ou entrada no fluxo de redefinição.

Loading: bloquear repetição da ação.

Sucesso logout: limpar estado protegido, contexto de atleta/treinador e retornar a Login.

Erro logout remoto: encerrar exposição local de dados protegidos sempre que possível e informar necessidade de nova autenticação conforme capacidade técnica aprovada.

Offline: redefinição remota indisponível; logout deve priorizar remoção local de acesso protegido.

Indisponibilidade: nenhuma edição de perfil/credencial não contratada é apresentada.

## CONTRATOS G5 DAS TRANSIÇÕES CONTEXTUAIS

### G5-CTX-01 — RESOLUÇÃO DE CONTEXTO GLOBAL

Loading: enquanto evidência atual está sendo resolvida, manter o último contexto seguro e não reorganizar repetidamente a tela.

Vazio: ausência de sinal competitivo ativo resolve para ROTINA.

Erro: falha em um sinal não autoriza PRÉ/JOGO/PÓS; usar último estado seguro e indicar erro apenas se necessário à compreensão.

Offline: não criar novo contexto global a partir de cache; manter último contexto conhecido como desatualizado ou ROTINA segura.

Pendência: sinal incompleto pode manter contexto local da competição sem promover Home/Central.

Sucesso: aplicar precedência DIA DO JOGO > PRÉ-COMPETIÇÃO > PÓS-ETAPA > ROTINA.

Indisponibilidade: competição não relevante/não publicável não participa da resolução da atleta; sinais internos podem participar apenas da Central do treinador.

Retorno: mudança de contexto não muda rota atual nem remove uma ação P0 independente.

### G5-CTX-02 — TRANSIÇÃO ROTINA → PRÉ-COMPETIÇÃO

Loading: não antecipar promoção.

Sucesso: promover somente blocos definidos na Seção 6 quando existir sinal operacional canônico.

Pendência: convocação/programação ausente não vira negativa; apenas o que estiver confirmado aparece.

Erro/offline: Home/Central permanece no estado seguro anterior.

Indisponibilidade: se não existe sinal publicável para atleta, somente o detalhe local pode permanecer ANTES.

Retorno: se todos os sinais ativos desaparecerem, voltar a ROTINA sem resetar navegação/filtros.

### G5-CTX-03 — TRANSIÇÃO PRÉ → DIA DO JOGO

Loading: manter PRÉ enquanto o estado DURANTE não estiver confirmado.

Sucesso: promover próximo jogo/estado da execução e rebaixar tarefas pré-evento conforme Seção 6.

Vazio: não existe “Dia do Jogo vazio”; sem evidência de operação, não entrar no estado.

Pendência: programação parcial pode sustentar JOGO apenas se houver evidência canônica de execução, nunca por data ampla isolada.

Erro/offline: não inventar adversário/horário; preservar último estado seguro.

Indisponibilidade: prazos resolvidos deixam de ser acionáveis.

Retorno: a navegação aberta na competição permanece na mesma competitionId.

### G5-CTX-04 — TRANSIÇÃO DIA DO JOGO → PÓS-ETAPA

Loading: manter estado de execução até encerramento/resultado suficientemente resolvido.

Sucesso: promover campanha/fechamento e rebaixar programação/convocação.

Pendência: competição encerrada com parcial incompleto entra em fechamento com qualidade/resultado pendente, sem métrica conclusiva.

Erro: não transformar ausência de segmentos em placar final.

Offline: não concluir etapa apenas por horário/data local.

Indisponibilidade: ações de pré/jogo vencidas perdem affordance.

Retorno: próximo compromisso volta gradualmente à hierarquia sem criar uma nova Home.

### G5-CTX-05 — TRANSIÇÃO PÓS-ETAPA → ROTINA OU NOVO PRÉ

Loading: manter último estado seguro até resolver o próximo contexto.

Sucesso: se existe novo sinal competitivo de maior precedência, entrar em PRÉ; caso contrário ROTINA.

Pendência: fechamento não resolvido pode continuar acessível no detalhe/Resultados sem dominar indefinidamente a Home/Central.

Erro/offline: não usar ausência de atualização como prova de fechamento concluído.

Indisponibilidade: resultado sem validação não permanece promovido como campanha final.

Retorno: preservar histórico e permitir continuidade operacional do próximo treino/agenda.

## CRITÉRIOS DE ACEITE G5

1\. Cada uma das 17 telas funcionais possui contrato explícito para FUNÇÃO, DADO, AÇÃO, PRIORIDADE, PRIVACIDADE, ESTADOS e COMPOSIÇÃO nos sete estados canônicos.

2\. VAZIO, ERRO, PENDÊNCIA e INDISPONIBILIDADE nunca são tratados como sinônimos.

3\. Nenhuma escrita é confirmada visualmente antes da confirmação canônica do servidor.

4\. Offline não cria fila de escrita silenciosa na V1.

5\. Privacidade é aplicada antes de loading/empty/error; a UI não revela a existência de dado não autorizado por placeholders.

6\. Falha parcial preserva blocos independentes válidos sempre que identidade e autorização da tela permanecem confiáveis.

7\. Transição contextual não muda permissão, não inventa dados e não apaga ação P0 independente.

8\. Retorno preserva contexto útil de origem — ID, período, filtro ou grupo — sem utilizá-lo como autorização.

9\. Toda indisponibilidade de dado crítico possui comportamento seguro: ocultar, somente leitura, mensagem pública ou diagnóstico do treinador conforme classificação.

10\. Os contratos permanecem independentes de card, cor, fonte, ícone, grid, animação ou implementação React.

## GATE DE SAÍDA — SEÇÃO 7 / G5

A Seção 7 atinge G5 quando todas as telas críticas e blocos acionáveis possuem comportamento verificável para loading, vazio, erro, offline, pendência, sucesso e indisponibilidade; quando escrita, feedback e retorno estão definidos; quando as transições ROTINA/PRÉ/JOGO/PÓS preservam autorização, contexto e dados canônicos; e quando nenhuma regra depende da aparência visual final. Status desta execução: CONTRATOS DE TELA E INTERAÇÃO G5 ESPECIFICADOS PARA ATLETA E TREINADOR.

Próxima dependência de Design: executar a Seção 3 — Direções Visuais até G4 visual sobre exatamente estes contratos, sem alterar funções, prioridades, privacidade ou estados definidos. Depois, consolidar Tipografia e Iconografia em G6 e somente então produzir os protótipos mobile de alta fidelidade candidatos a validação.