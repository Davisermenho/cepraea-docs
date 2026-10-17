PRODUCT REQUIREMENTS DOCUMENT | PRD

CEPRAEA BEACH PRO

Versão 0.1 • 16 de outubro de 2026 • português (Brasil)

ESTADO DOCUMENTAL: PROPOSTA PARA REVISÃO E APROVAÇÃO HUMANA — NÃO EFETIVO

ESTADO DO PRODUTO: CONCEPÇÃO, DEFINIÇÃO E PLANEJAMENTO. Nenhuma funcionalidade considerada implementada, testada, lançada ou operacional.

FINALIDADE: concentrar em uma única referência as necessidades, decisões, regras de domínio, requisitos pretendidos, critérios de aceite e limites do CEPRAEA BEACH PRO. Este PRD é uma elaboração derivada do conhecimento consolidado, não uma aprovação automática de todo o conteúdo.

CONTROLE DE SUBSTITUIÇÃO: a eventual exclusão dos documentos do Drive NÃO foi executada. O PRD só poderá substituí-los como referência de produto após aceite explícito desta versão e preservação verificável do acervo probatório e operacional; referências a fontes apagadas deixam de funcionar.

# Guia de leitura e autoridade

| **Campo** | **Estado** |
| --- | --- |
| Tipo | PRD integrado com catálogo de evidências |
| --- | --- |
| Versão | v0.1 — candidato a arquivo mestre |
| --- | --- |
| Responsável por decisões de produto | Treinador / responsável pelo CEPRAEA |
| --- | --- |
| Efeito da emissão | Documento novo para revisão; sem autorização de desenvolvimento, publicação ou exclusão |
| --- | --- |
| Base material | CEPRAEA BEACH PRO — Conhecimento Consolidado do Projeto, 16/10/2026, e suas fontes S01–S52 |
| --- | --- |
| Referência temporal | 07/09/2026 aparece como prazo HISTÓRICO vencido, não entrega comprovada |
| --- | --- |

## Como interpretar os estados de evidência

-   DECISÃO HUMANA DIRETA — mensagem original identificada e delimitada no histórico exportado; confirmada apenas no que foi dito.
-   DECLARAÇÃO DE PRODUTO DOCUMENTADA — registrada em elicitação, respostas e sínteses; seu conteúdo representa intenção, não aceite global deste PRD.
-   DECISÃO TRANSCRITA, SEM ORIGINAL LOCALIZADO — aprovação reportada por documento, cuja mensagem fonte não foi autenticada de maneira independente.
-   PROPOSTA / HIPÓTESE — forma de atendimento ainda não ratificada, risco ou futuro possível; não deve ser implementada como se fosse ordem.
-   SUPERADA — formulação anterior cuja substituição tem suporte na evolução registrada; manter a proveniência e as diferenças.
-   NÃO VERIFICADO — capacidade técnica, execução, implantação, teste ou autoridade não demonstrados por observação própria.

Os requisitos numerados neste PRD são identificadores editoriais de consolidação. A atribuição de um ID, de critério “Dado/Quando/Então” ou de prioridade “primeira entrega” não constitui nova escolha humana nem teste executado. As evidências constam em cada item e no anexo de fontes.

# 1. Contexto, problema e oportunidade

## 1.1 Contexto esportivo e origem

O CEPRAEA mantém uma equipe feminina adulta de alto rendimento de handebol de praia. O treinador relata gerir durante aproximadamente dois anos as rotinas por planilhas, documentos e WhatsApp, acumulando calendário, convocação de respostas, presença, comunicação, competições e material esportivo. Essa operação EXISTE independentemente do futuro BEACH PRO. [S01 Q001–Q004; S02; S03]

A deficiência central não é a existência de planilhas: é a impossibilidade de cruzar, sem intervenção humana contínua, a disponibilidade declarada, a função esportiva adequada, o momento do treino, as alterações, a presença efetiva e a comunicação. O treinador deixa de dedicar tempo a planejar sessões, analisar jogos e oferecer feedback esportivo para atuar como coordenador de informação. [S01 Q001; S02 Q001–Q003]

## 1.2 Incidentes determinantes documentados

-   Treino tático planejou composição de uma goleira, três defensoras e quatro atacantes; a ausência de goleira, descoberta na praia, inviabilizou o exercício previsto. A contagem de respostas SIM não validou a composição tática. [S01 Q001]
-   Treinamento noturno marcado em data de feriado revelou erro de calendário; a regra local de feriados requer análise antecipada de horário matutino. [S01 Q001]
-   Atletas podem modificar respostas em planilhas após a sessão, impedindo distinguir declaração antiga, presença física e participação real. [S01 Q001; S02 Q010]
-   Cancelamento tardio e aviso disperso no WhatsApp obrigam o treinador a perceber, conferir e agir sem diagnóstico consolidado. [S01 Q001; S02 Q013]
-   Dores, retorno de lesão, limitação física e responsabilidade por equipamentos podem ser conhecidos somente no local, impondo improvisação e riscos operacionais; isso sustenta a visão futura, não ampliação tácita do MVP. [S01 Q001]

## 1.3 Problema de produto

Como treinador/administrador de um elenco adulto de handebol de praia, preciso conhecer antecipadamente se uma sessão pode ocorrer com as atletas e capacidades certas, manter registros históricos fidedignos e reduzir cobranças e conferências repetitivas, para concentrar meu trabalho em julgamento e preparação esportivos. [S01–S04]

# 2. Visão, pessoas e limites do produto

## 2.1 Visão

Criar um ambiente privado, de uso prioritariamente móvel, confiável e orientado à ação, no qual o ciclo regular de treinos do CEPRAEA possa ser planejado e resolvido com mínima administração semanal, preservando a decisão esportiva humana e a diferença entre o que se declarou, o que se planejou e o que efetivamente aconteceu. Não é simplesmente digitalização das planilhas. [S01–S04]

## 2.2 Perfis previstos para a primeira entrega

| **Perfil** | **Papel pretendido** | **Fronteira** |
| --- | --- | --- |
| TREINADOR_ADMINISTRADOR | Revisar/publicar agenda, cadastrar capacidades, responder a exceções, apurar fatos, retificar fatos consolidados. | Autoridade operacional/esportiva; controle técnico de autenticação não escolhido. |
| --- | --- | --- |
| ATLETA | Consultar agenda/próxima ação, declarar disponibilidade própria, comunicar mudança pós-fechamento e consultar informações autorizadas. | Não edita declaração alheia nem presença/participação consolidada; não vê dados privados de outras atletas. |
| --- | --- | --- |

Dimensionamento inicial relatado: um treinador e 19 atletas adultas. Esse número descreve o elenco conhecido à época e NÃO significa que a contagem cadastral deva ser fixa, imutável ou critério de desenvolvimento para usos futuros. [S01 Q002, Q008; S02; S04]

## 2.3 Restrições e não objetivos

-   Formato PWA (Progressive Web App), com foco em smartphone e interação mobile-first, adotado como direção explícita da primeira entrega. Não implica por si suporte offline. [S01 Q007; S02]
-   Desenvolvimento solo, com apoio de VS Code, Codex e Claude Code; não pressupor APIs de inferência pagas ou equipe multidisciplinar disponível. [S01 Q006–Q008]
-   Orçamento operacional pretendido próximo de R$ 50/mês; R$ 200/mês foi declarado incompatível. São restrições de planejamento, não custo apurado. [S01 Q006; S02]
-   Não construir plataforma genérica de esportes, aplicativo de handebol indoor, sistema de arbitragem ou gestão de federações/torneios. [S01 Q005; S03]
-   Não criar rede social pública, streaming próprio, prontuário clínico, prescrição de saúde, editor profissional de vídeo, ERP contábil ou plataforma de recrutamento. [S01 Q005; S03]
-   Prazo de uma semana, ~42 horas e meta de 07/09/2026 são contexto histórico anterior a este PRD (16/10/2026); não constituem cronograma vigente nem prova de lançamento. [S01 Q006–Q008; S04]

# 3. Objetivos e definição de sucesso

| **Objetivo** | **Resultado esperado** | **Situação de aferição** |
| --- | --- | --- |
| OBJ-001 — Devolver tempo | Menos operação mecânica, mais planejamento, análise, ensino e feedback esportivo. | NÃO MEDIDO; horas históricas são estimativas, não linha de base. |
| --- | --- | --- |
| OBJ-002 — Gestão por exceção | Fluxo semanal normal sem ação administrativa obrigatória após publicar agenda. | Meta de produto documentada, sem execução verificada. |
| --- | --- | --- |
| OBJ-003 — História fidedigna | Não confundir declaração, fato e correção; auditoria de alterações. | Critérios a verificar em software futuro. |
| --- | --- | --- |
| OBJ-004 — Autonomia | Atletas consultam a próxima ação e registram diretamente suas informações. | Adoção ainda hipotética. |
| --- | --- | --- |
| OBJ-005 — Apoio à decisão | Cálculos e alertas destacam déficit sem decidir substituição tática humana. | Validar com cenários operacionais no futuro. |
| --- | --- | --- |

## 3.1 Critério principal proposto para a primeira entrega

META DOCUMENTADA: número de ações administrativas obrigatórias do treinador entre a revisão/publicação da agenda mensal e o fechamento do fluxo normal em D-5 = 0. “Zero” não elimina decisões sobre imprevistos após confirmação, mudanças voluntárias de agenda ou consolidação esportiva após a sessão. Não deve ser usado como alegação de êxito já atingido. [S02 Q009–Q012; S03 SUCCESS-001/002]

## 3.2 Indicadores e limites

-   Monitorar futuramente sessões publicadas, automaticamente confirmadas/canceladas em D-5, desvios de quórum, incidência de decisão manual pós-confirmação e necessidade de cobrança administrativa. [S03]
-   Adesão das atletas e tempo administrativo real economizado são hipóteses a validar; estimativas anteriores de 8–12 h/semana normal ou 15–20 h em semanas intensas não foram cronometradas. [S01 Q009; S04 HYP-001–003]
-   Título esportivo, resultado de competição ou número de gols NÃO são critérios diretos de validação causal do software. [S02 Q004]

# 4. Escopo da primeira entrega versus visão futura

## 4.1 Primeira entrega pretendida (sem desenvolvimento realizado)

-   Elenco e dois perfis autorizados; funções/posições do elenco e ações próprias das atletas. [S02; S03; S04]
-   Proposta mensal da agenda, revisão humana por exceção, publicação e sessões extraordinárias. [S02; S03; S05]
-   Disponibilidade com quatro estados semânticos; histórico de declarações e prazo D-5. [S02; S05]
-   Quórum tático com oito pessoas distintas, alocação funcional e goleira na defesa; resolução automática do fluxo normal em D-5. [S02; S05; S06]
-   Ocorrências após fechamento, tratamento de quórum comprometido, decisão manter/cancelar e remarcação auditável. [S02; S05; S07]
-   Apuração factual de presença e participação, retificação auditável, histórico e visão operacional simples por perfil. [S02; S03; S05]

## 4.2 Fora da primeira entrega, mantido como intenção FUTURE

**Wellness Pré/Pós** Coleta de estado e recuperação ligada ao treinamento; dados potencialmente sensíveis, sem fazer diagnóstico ou prescrição. [S01; S02 §FUTURE; S03; S13]

**Planejamento técnico-tático** Biblioteca de exercícios, conteúdos de sessão, planejamento de microciclo e temporada. [S01; S02 §FUTURE; S03; S13]

**Scout e avaliação** Eventos de jogo, estatísticas, dashboards de desempenho, relatórios, evolução e feedback individual. [S01; S02 §FUTURE; S03; S13]

**Vídeos e materiais** Biblioteca e associação entre eventos, vídeos, PDFs, scouts e orientações; sem plataforma pública de streaming. [S01; S02 §FUTURE; S03; S13]

**Competições** Informações de torneios, jogos, adversários, resultados e classificações sob a ótica da equipe, não administração federativa. [S01; S02 §FUTURE; S03; S13]

**Logística** Viagens, equipamentos, responsabilidades e organização de materiais. [S01; S02 §FUTURE; S03; S13]

**Financeiro leve** Registros pontuais de custo interno, sem contabilidade empresarial. [S01; S02 §FUTURE; S03; S13]

**Alternativas não fechadas** Lista de espera automática, substituição automática, convidados, pontuação comportamental ou mídia pública — ideias históricas, não requisitos aprovados. [S01; S02 §FUTURE; S03; S13]

REGRA DE CONTENÇÃO: nada desta seção entra automaticamente na primeira entrega apenas porque já existiu operação similar em planilhas, foi descrito em um plano antigo ou cabe tecnicamente na arquitetura. [S02 SUPERSEDED-008/014]

# 5. Modelo de negócio e vocabulário funcional

## 5.1 Distinções indispensáveis

| **Conceito** | **Significado / fonte de autoridade** |
| --- | --- |
| Atleta | Identidade esportiva da pessoa; um cadastro não equivale a conta autenticada. [S12 DEC-DATA-002] |
| --- | --- |
| Vínculo ao elenco | Relação temporal com a equipe, diferente de existir um registro da atleta. [S12 DEC-DATA-003] |
| --- | --- |
| Agenda / proposta | Planejamento de sessões possíveis, revisável; publicação não garante realização. [S02; S05] |
| --- | --- |
| Sessão | Compromisso esportivo com identidade própria, ciclo PLANEJADO→... e atributos de data/hora/local. [S02; S05] |
| --- | --- |
| Disponibilidade | Declaração para sessão (ou ausência de resposta), prévia ao fato. [S02 Q010] |
| --- | --- |
| Quórum | Alocação suficiente de capacidades táticas diferentes em pessoas distintas. [S02 Q011; S05] |
| --- | --- |
| Ocorrência pós-D-5 | Atualização adicional, sem reescrever a disponibilidade original. [S02 Q013; S05] |
| --- | --- |
| Presença | Comparecimento físico comprovado e consolidado pelo treinador. [S02 Q010] |
| --- | --- |
| Participação | Quanto da sessão a atleta efetivamente executou; não sinônimo de presença. [S02 Q010] |
| --- | --- |
| Retificação | Correção explícita do fato consolidado, conservando a trilha do estado anterior. [S02; S05] |
| --- | --- |

## 5.2 Vocabulários observados

| **Dimensão** | **Estados/valores registrados** |
| --- | --- |
| Ciclo de sessão | PLANEJADO; PUBLICADO; CONFIRMADO; CANCELADO; REALIZADO. |
| --- | --- |
| Condição/projeção independente | DISPONIBILIDADE_ABERTA; QUÓRUM_EM_FORMAÇÃO; QUÓRUM_GARANTIDO; FALTA_DE_QUÓRUM; QUÓRUM_COMPROMETIDO. |
| --- | --- |
| Disponibilidade da atleta | DISPONÍVEL; INDISPONÍVEL; TALVEZ; NÃO RESPONDEU. |
| --- | --- |
| Evento pós-fechamento | NÃO PODEREI COMPARECER; AGORA POSSO PARTICIPAR. |
| --- | --- |
| Presença | NÃO APURADO; PRESENTE; AUSENTE. |
| --- | --- |
| Participação | NÃO APURADA; COMPLETA; PARCIAL; NÃO PARTICIPOU. |
| --- | --- |

Estados de projeção não equivalem a estados do ciclo de sessão; por exemplo, QUÓRUM_COMPROMETIDO pode coexistir com sessão CONFIRMADO, e QUÓRUM_GARANTIDO pré-D-5 não antecipa confirmação. [S02; S05]

## 5.3 Modelo de funções esportivas

| **Fase / sistema** | **Posições da fonte** |
| --- | --- |
| ATAQUE 3x1 | Central; Pivô; Lateral Esquerda; Lateral Direita. |
| --- | --- |
| ATAQUE 4x0 | Lateral Esquerda; Lateral Direita; Central Esquerda; Central Direita. |
| --- | --- |
| DEFESA 3:0 | Defensora Base; Defensora Solta; Defensora Cobertura; Goleira. |
| --- | --- |
| DEFESA 2:1 | Defensora Avançada; Defensora Solta; Defensora Cobertura; Goleira. |
| --- | --- |

A hierarquia FASE → SISTEMA → POSIÇÃO é significado esportivo, não imposição de estrutura de tabelas. Para a primeira entrega, cada atleta possui posição principal configurada pelo treinador e secundária opcional; não se presumem capacidades pessoais a partir do rótulo de equipe. [S02 Q011; S04; S05]

# 6. Fluxos de usuário, eventos e transições pretendidas

## FLUXO A — Planejamento e publicação mensal

O sistema prepara proposta de sessões recorrentes e possíveis feriados; o treinador analisa somente exceções e publica. A publicação inaugura a coleta de disponibilidade para sessões futuras.

**Invariante de fluxo** Antes da publicação, proposta pode ser alterada ou excluída; nenhuma agenda futura se apresenta como treino realizado. [S02 Q010; S05]

## FLUXO B — Declaração pré-D-5

Atleta consulta suas sessões, responde DISPONÍVEL / INDISPONÍVEL / TALVEZ e pode alterar enquanto a coleta estiver aberta. O sistema mantém a trilha e exibe a próxima ação.

**Invariante de fluxo** Não responder não é dizer NÃO. Atleta não precisa escolher posição; posições pertencem a seu perfil esportivo. [S02 Q010–Q011]

## FLUXO C — Monitoramento do quórum

O sistema analisa alocação simultânea com pessoas distintas e capacidades; pode mostrar QUÓRUM_GARANTIDO ou déficits, sem encerrar coleta antes do instante programado.

**Invariante de fluxo** Diagnóstico de viabilidade não equivale a confirmação prematura; sobreposição de funções na mesma atleta não vale como dois lugares. [S02 Q011–Q012]

## FLUXO D — Resolução em D-5

Exatamente 120 h antes de cada sessão publicada, a coleta ordinária fecha. Se composição viável, CONFIRMADO; caso contrário, CANCELADO com FALTA_DE_QUÓRUM; comunicar o resultado sem etapa manual do treinador.

**Invariante de fluxo** Cancelamento terminal; não se aplica a sessão que já estava CONFIRMADO e posteriormente perdeu quórum. [S02; S05; S06; C-B01]

## FLUXO E — Mudanças pós-fechamento

Uma atleta CONFIRMADO comunica que não poderá comparecer, ou que agora poderá; a informação altera a projeção atual e preserva a resposta histórica.

**Invariante de fluxo** Se o quórum ficar comprometido, só o treinador escolhe MANTER TREINO ou CANCELAR TREINO; a alteração nunca cancela automaticamente sessão já confirmada. [S02 Q013; S05]

## FLUXO F — Remarcação

Treinador opta por remarcar. O compromisso original é cancelado com motivo REMARCADO; surge nova sessão identificável, com novo calendário e nova coleta.

**Invariante de fluxo** Não transportar confirmações antigas nem substituir silenciosamente data/horário em sessão publicada. [S02 Q010; S05]

## FLUXO G — Realização e fatos

A experiência prepara lista provisória a partir de evidências operacionais; treinador apura comparecimento e participação, preferencialmente revendo somente exceções, e consolida.

**Invariante de fluxo** Wellness, logs e disponibilidade não constituem fatos definitivos; falha de aplicativo não apaga presença real. [S01 Q010; S02 Q010; S05]

## FLUXO H — Correção factual

Se houver erro posterior na apuração, o treinador registra retificação com situação anterior, nova, motivo, autor e momento, conservando histórico.

**Invariante de fluxo** Uma alteração de presença/participação que produza combinação inválida exige retificação dos dois eixos juntos. [S02; S05]

# 7. Requisitos funcionais e critérios de aceite futuros

Os critérios abaixo são formulações de teste de CONFORMIDADE DOCUMENTAL e serão usados somente se a implementação for posteriormente autorizada. Não há registro de execução desses testes no CEPRAEA BEACH PRO. Origem substantiva: requisitos pretendidos consolidados de S02–S05 e B-01/B-02 quando indicado.

## 7.1 Elenco, usuários, papéis e capacidades

### RF-01 — Identidade esportiva do elenco

**Enunciado de produto** Permitir identificar a atleta e seu vínculo com a equipe sem equiparar obrigatoriamente identidade esportiva à conta de autenticação.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado registro esportivo de atleta sem login, quando for consultada sua condição de integrante, então a existência da atleta não dependerá de credencial ativa.

**Limite / exceção** Modelagem de banco, chaves e método de login não definidos.

**Evidência / classificação** S12 DEC-DATA-002/003; S02 Q008. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-02 — Dois perfis da primeira entrega

**Enunciado de produto** Diferenciar treinador/administrador e atleta para as ações de produto documentadas.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta autenticada, quando tentar atuar sobre registro de outra atleta ou consolidar presença, então a operação deve ser vedada; treinador pode executar as ações de sua autoridade.

**Limite / exceção** Não define tecnologia de autenticação nem regras físicas RLS.

**Evidência / classificação** S02 Q008; S03 ACT-001/002; S04. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-03 — Capacidade e posição da atleta

**Enunciado de produto** Treinador informa posição principal e, facultativamente, secundária para elegibilidade em exercícios/sessões; disponibilidade não exige que a atleta escolha posição.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta com duas posições válidas, quando declarar disponibilidade, então uma resposta basta, e nenhuma atribuição de posição é feita pela atleta nesse ato.

**Evidência / classificação** S02 Q011; S04; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-04 — Informações próprias

**Enunciado de produto** Atleta consulta sua próxima ação, sessões e informações pessoais pertinentes sem ter acesso aos dados privados individuais de outras.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dadas duas contas de atleta, quando uma solicitar os dados protegidos da outra, então não deverá obtê-los por interface nem por operação subjacente.

**Limite / exceção** Definições pormenorizadas de privacidade e permissões exigem especificação técnica posterior.

**Evidência / classificação** S02 Q008–Q010; S29. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

## 7.2 Agenda e ciclo da sessão

### RF-05 — Proposta de agenda mensal

**Enunciado de produto** Preparar uma proposta mensal de sessões regulares sujeita a revisão do treinador antes de publicação.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado novo ciclo mensal, quando a proposta for preparada, então o treinador consegue verificar horários e revisar exceções antes de publicar.

**Evidência / classificação** S02 Q010; S03; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-06 — Recorrências operacionais documentadas

**Enunciado de produto** Considerar como padrão histórico quintas-feiras 20h00–21h30 e domingos 07h30–09h00, em Copacabana, Posto 4, sem transformar essas condições em valores imutáveis.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado mês sem exceção e padrões vigentes, quando gerar a proposta, então representar as sessões regulares previstas com data, horário e local.

**Limite / exceção** Referência do contexto observado; rotina concreta pode mudar por decisão do treinador.

**Evidência / classificação** S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-07 — Feriados oficiais aplicáveis ao Rio

**Enunciado de produto** Incluir na proposta mensal sessões possíveis em feriados nacionais e estaduais/municipais oficiais aplicáveis ao município do Rio de Janeiro, com sugestão 07h30–09h00 e revisão humana.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado feriado oficial coincidente com treino regular, quando proposta for criada, então apresentar uma única sugestão nessa data no horário sugerido para feriado; não somar sessão duplicada.

**Limite / exceção** Ponto facultativo, apenas feriado bancário e data comemorativa sem oficialidade não geram a regra; provedor de feriados não decidido.

**Evidência / classificação** S02 DEC-017/OPEN-001; S04; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-08 — Publicação sob autoridade humana

**Enunciado de produto** Publicar somente proposta de agenda revisada pelo treinador; criação/publicação não prova realização nem quórum.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão PLANEJADO, quando o treinador publicar, então ela fica PUBLICADO e apta a obter respostas sem ser registrada como realizada.

**Evidência / classificação** S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-09 — Sessões extraordinárias

**Enunciado de produto** Permitir ao treinador criar sessão extraordinária distinta da recorrência, respeitando seu próprio ciclo e prazo.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada criação de treino adicional com D-5 futuro, quando publicado, então ele segue o mesmo fluxo ordinário de disponibilidade e resolução.

**Evidência / classificação** S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-10 — Exceção de sessão criada após o D-5

**Enunciado de produto** Exigir decisão específica do treinador quando sessão extraordinária nascer com prazo de D-5 já ultrapassado; não simular uma decisão automática pretérita.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada nova sessão com início inferior a 120 h, quando criada, então o sistema não deve retroativamente executar uma confirmação como se o checkpoint houvesse ocorrido.

**Limite / exceção** Detalhe da coleta/confirmacão desse caso exige revisão ao fechar PRD; não criar fluxo adicional não documentado.

**Evidência / classificação** S02 Q010; S03. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-11 — Estados de sessão preservados

**Enunciado de produto** Diferenciar PLANEJADO, PUBLICADO, CONFIRMADO, CANCELADO e REALIZADO de diagnósticos temporários como QUÓRUM_GARANTIDO.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado sessão publicada com quórum suficiente antes de D-5, quando exibir o status, então permanecer PUBLICADO com condição QUÓRUM_GARANTIDO, não CONFIRMADO.

**Evidência / classificação** S02; S04; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-12 — Não sobrescrever data/horário publicado

**Enunciado de produto** Mudanças que afetem o compromisso após publicação devem preservar rastreabilidade; remarcação cria nova sessão.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão PUBLICADO, quando treinador optar por trocar data/hora, então o histórico original permanece e a operação de REMARCAR é aplicada, sem edição silenciosa.

**Evidência / classificação** S02 SUPERSEDED-015; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

## 7.3 Disponibilidade e quórum

### RF-13 — Solicitar disponibilidade por sessão

**Enunciado de produto** Disponibilizar às atletas solicitação individual vinculada à sessão publicada.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão PUBLICADO antes do prazo, quando atleta acessar a próxima ação, então poderá registrar sua declaração de disponibilidade para aquela sessão.

**Evidência / classificação** S02 Q010; S03; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-14 — Quatro estados semânticos

**Enunciado de produto** Representar DISPONÍVEL, INDISPONÍVEL, TALVEZ e NÃO RESPONDEU como situações distintas, sendo a última ausência de registro e não escolha da atleta.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada solicitação sem declaração, quando o treinador consultar, então exibir NÃO RESPONDEU e não transformar automaticamente em INDISPONÍVEL.

**Evidência / classificação** S02 Q010–Q012; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-15 — Alterar resposta durante janela

**Enunciado de produto** Enquanto a coleta ordinária estiver aberta, atleta pode alterar a resposta, sem perda da anterior.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado histórico DISPONÍVEL, quando atleta mudar para TALVEZ antes de D-5, então o estado corrente será TALVEZ e a declaração anterior continuará recuperável.

**Evidência / classificação** S02 Q012; S12 DEC-DATA-006. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-16 — Justificativa de indisponibilidade

**Enunciado de produto** Preservar a possibilidade documentada de motivo curto para ausência, sem exigir diagnóstico clínico.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada seleção INDISPONÍVEL, quando for fornecida justificativa, então ela fica vinculada à declaração e não vira classificação médica automática.

**Limite / exceção** Obrigatoriedade e campos exatos de justificativa não foram homologados globalmente.

**Evidência / classificação** S01 Q001; S02 Q010. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-17 — Quórum por alocação funcional

**Enunciado de produto** Calcular viabilidade com oito atletas DISPONÍVEL distintas: quatro alocáveis no ataque, quatro na defesa, incluindo uma goleira entre as quatro na defesa.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dadas oito DISPONÍVEL com composição válida, quando cálculo avaliar, então resultado pode ser suficiente; dadas oito sem goleira alocável na defesa, resultado insuficiente.

**Evidência / classificação** S02 Q011; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-18 — Proibir dupla contagem

**Enunciado de produto** Impedir que uma atleta com múltiplas posições seja contada simultaneamente em vagas distintas.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta elegível a pivô e lateral, quando o cálculo exigir duas vagas simultâneas, então ela conta no máximo em uma delas.

**Evidência / classificação** S02 Q011; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-19 — Usar capacidades principal/secundária

**Enunciado de produto** O cálculo usa preferências registradas sem impor escolha de posição no ato da declaração.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta secundariamente elegível para posição em déficit, quando calcular possibilidades, então considerar alternativa sem declarar dois lugares ocupados por ela.

**Limite / exceção** Detalhes do algoritmo de otimização e remanejamento esportivo não escolhidos.

**Evidência / classificação** S02 Q011; S04; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-20 — Diagnosticar déficit concreto

**Enunciado de produto** A visão do treinador indica quantitativos e capacidades ausentes, não apenas um semáforo binário.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão com sete pessoas válidas ou nenhuma goleira, quando visualizar diagnóstico, então mostrar o déficit específico responsável pela insuficiência.

**Evidência / classificação** S02 Q011; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-21 — Prévia sem antecipação de compromisso

**Enunciado de produto** Antes de D-5, o sistema pode exibir QUÓRUM_GARANTIDO, mas não antecipa confirmação automática da sessão do fluxo normal.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada composição suficiente em D-7, quando a sessão for consultada, então manter coleta e ciclo PUBLICADO até D-5.

**Evidência / classificação** S02 SUPERSEDED-009; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

## 7.4 Checkpoint D-5 e ciclo terminal

### RF-22 — Checkpoint temporal exato

**Enunciado de produto** Para sessão publicada do fluxo normal, D-5 é o instante de início menos exatamente 120 horas.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão com início definido, quando alcançadas 120 h anteriores, então encerrar a janela ordinária naquele instante lógico, independentemente do dia e horário de rotina.

**Limite / exceção** Infraestrutura de execução, fuso e consistência técnica são decisões futuras, não assumidas.

**Evidência / classificação** S02 Q012; S04; S05; C-D5. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-23 — Confirmar automaticamente se viável

**Enunciado de produto** Em D-5, após encerrar a coleta, se quórum operacional é suficiente, confirmar a sessão sem ação administrativa semanal do treinador e comunicar.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão PUBLICADO com alocação válida em D-5, quando checkpoint ocorrer, então ficará CONFIRMADO com resultado preservado e comunicado.

**Limite / exceção** Comunicação tem requisito de resultado, mas canal técnico ainda não foi decidido.

**Evidência / classificação** S02 Q012; S05; S06. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-24 — Cancelar automaticamente se insuficiente

**Enunciado de produto** Em D-5, se sessão PUBLICADO tem quórum insuficiente, cancelar automaticamente com FALTA_DE_QUÓRUM e manter resultado e histórico.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão PUBLICADO em D-5 sem composição suficiente, quando checkpoint ocorrer, então ficará CANCELADO/FALTA_DE_QUÓRUM sem esperar decisão manual.

**Evidência / classificação** S06 DEC-PWA-001; C-B01 (conversations-011.json, mensagem d7a5906b-9a48-42d4-a6c3-7a46452d3c19). DECISÃO HUMANA DIRETA B-01, escopo restrito ao fluxo normal.

### RF-25 — Cancelamento terminal

**Enunciado de produto** Não reativar sessão CANCELADO por reabertura, nova resposta, edição de prazo ou recálculo; necessidade de atividade futura cria outra sessão.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão CANCELADO, quando surgirem novas atletas disponíveis ou nova coleta, então a mesma identidade continua CANCELADO.

**Evidência / classificação** S07 DEC-PWA-002; S02; S05. DECISÃO B-02 TRANSCRITA EM DOCUMENTO — mensagem original não localizada nos 12 JSONs.

### RF-26 — Preservar resultado e informar atletas

**Enunciado de produto** Resolução de D-5 deve ser conhecida pelas atletas e consultável com motivo e histórico, sem ocultar estados intermediários relevantes.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado cancelamento em D-5, quando usuária consultar sessão, então o motivo FALTA_DE_QUÓRUM e o estado cancelado estarão distinguíveis de sessão confirmada.

**Evidência / classificação** S02; S03; S05; S06. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

## 7.5 Ocorrências após fechamento, exceções e remarcação

### RF-27 — Registrar impossibilidade pós-D-5

**Enunciado de produto** Em sessão já CONFIRMADO, atleta pode registrar NÃO PODEREI COMPARECER sem alterar declaração ordinária pregressa.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta que declarou DISPONÍVEL, quando informar que não poderá comparecer após D-5, então a disponibilidade original permanece e sua elegibilidade corrente é retirada.

**Evidência / classificação** S02 Q013; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-28 — Registrar possibilidade positiva posterior

**Enunciado de produto** Em sessão CONFIRMADO, atleta pode registrar AGORA POSSO PARTICIPAR, preservando declaração antiga.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta anteriormente INDISPONÍVEL, quando registrar mudança positiva após D-5, então ela entra como candidata atual sem apagar a negativa anterior.

**Evidência / classificação** S02 Q013; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-29 — Recalcular quórum diante de mudança

**Enunciado de produto** Ocorrência válida altera composição corrente e aciona diagnóstico sem transformar CONFIRMADO em cancelamento automático.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado CONFIRMADO cuja goleira disponível informa impossibilidade, quando recalcular, então manter CONFIRMADO e marcar QUÓRUM_COMPROMETIDO com déficit identificado.

**Evidência / classificação** S02 Q013; S05; S06. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-30 — Decisão humana sobre quórum comprometido

**Enunciado de produto** Treinador escolhe MANTER TREINO ou CANCELAR TREINO em sessão confirmada que perdeu quórum; o sistema não cancela por conta própria.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão CONFIRMADO com QUÓRUM_COMPROMETIDO, quando ocorrer baixa, então expor as duas escolhas ao treinador e aguardar seu ato explícito para eventual cancelamento.

**Limite / exceção** Não exigir inventário detalhado de adaptação tática como nova obrigação.

**Evidência / classificação** S02 Q013; S05; S06. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-31 — Recuperação de quórum após evento positivo

**Enunciado de produto** Se composição recuperar suficiência, retirar diagnóstico comprometido sem repetir compromisso ou exigir nova confirmação do treinador.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão CONFIRMADO com QUÓRUM_COMPROMETIDO, quando nova disponibilidade válida restabelecer oito atletas, então remover alerta de déficit e manter CONFIRMADO.

**Evidência / classificação** S02 Q013; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-32 — Permitir representação por treinador quando necessário

**Enunciado de produto** Quando atleta não conseguir operar o app, treinador poderá registrar ocorrência em seu nome preservando verdadeiro autor e origem.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada informação confiável recebida externamente, quando treinador lançar ocorrência de atleta, então o registro identifica treinador como autor do lançamento, sem fingir submissão pessoal da atleta.

**Limite / exceção** Critérios de confiança e tratamento de dados devem respeitar política posterior de acesso.

**Evidência / classificação** S01 Q013; S02 Q013. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-33 — Remarcar mantendo identidade histórica

**Enunciado de produto** REMARCAR cancela a sessão original com motivo REMARCADO e cria nova, com novo D-5 e sem transportar declarações.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão publicada com respostas, quando remarcada, então o registro original é preservado como CANCELADO/REMARCADO, e a nova começa sem herdar respostas.

**Evidência / classificação** S02 Q010/Q013; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

## 7.6 Presença, participação, retificação e leitura operacional

### RF-34 — Apurar presença factual por autoridade humana

**Enunciado de produto** Treinador consolida presença física (PRESENTE/AUSENTE), sem inferir presença a partir de disponibilidade, Wellness ou registros de aplicativo.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta que treinou mas ficou sem internet e não respondeu Wellness, quando treinador apurar, então poderá registrar PRESENTE sem depender da telemetria ausente.

**Evidência / classificação** S01 Q010; S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-35 — Apurar participação distinta

**Enunciado de produto** Treinador registra participação completa, parcial ou nenhuma, em conformidade com o comparecimento apurado.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta que compareceu mas não treinou, quando consolidar, então registrar PRESENTE + NÃO PARTICIPOU, não transformar em AUSENTE.

**Evidência / classificação** S01 Q010; S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-36 — Restringir combinações impossíveis

**Enunciado de produto** Impedir combinação AUSENTE com participação COMPLETA/PARCIAL e preservar o par NÃO APURADO/NÃO APURADA antes de consolidação.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado estado AUSENTE, quando tentativa atribuir COMPLETA, então rejeitar combinação; dado sem apuração, não inventar ausência.

**Evidência / classificação** S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-37 — Consolidar revendo exceções

**Enunciado de produto** Preparar lista provisória com evidências disponíveis e permitir ao treinador conferir exceções e consolidar os fatos.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado treino realizado e evidências prévias, quando treinador iniciar apuração, então poderá revisar lista proposta sem segunda chamada compulsória de todas as atletas.

**Limite / exceção** A lista provisória não é fonte oficial até chancela factual do treinador.

**Evidência / classificação** S01 Q010; S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-38 — Retificar fato sem sobrescrever

**Enunciado de produto** Treinador pode corrigir presença/participação consolidadas com registro anterior, novo valor, motivo, autor e data/hora.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada presença consolidada incorretamente, quando retificada, então estado corrente refletirá correção e histórico continuará incluindo o estado anterior e autoria.

**Evidência / classificação** S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-39 — Retificação conjunta quando necessária

**Enunciado de produto** Se alteração em somente uma dimensão gerar combinação impossível, corrigir presença e participação em uma operação coerente.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dado PRESENTE+COMPLETA e correção para AUSENTE, quando retificar, então ajustar participação para NÃO PARTICIPOU conjuntamente e preservar ambos os valores anteriores.

**Evidência / classificação** S02 Q010; S05. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-40 — Visão de próxima ação e histórico

**Enunciado de produto** Oferecer ao treinador e à atleta visão simples das sessões, próximos atos cabíveis e históricos permitidos.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada atleta com sessão pendente, quando abrir app, então identificar claramente o que falta responder; dada sessão finalizada, distinguir histórico de atos e fatos sem cobrança indevida.

**Evidência / classificação** S02 Q008–Q010; S03; S29. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

### RF-41 — Comunicação do estado real

**Enunciado de produto** Informar alteração relevante, confirmação/cancelamento e necessidade de ação sem depender estruturalmente de buscas no WhatsApp.

**Aceite futuro (cenário de conformidade, NÃO EXECUTADO)** Dada sessão cancelada, quando situação for comunicada, então destinatários não recebem orientação conflitante com o estado persistido.

**Limite / exceção** E-mail, push, WhatsApp ou in-app são opções técnicas a decidir; não exigir canal específico agora.

**Evidência / classificação** S01 Q003–Q004; S02; S03. INTENÇÃO DOCUMENTADA — homologação integral do PRD pendente.

# 8. Requisitos de qualidade, segurança e dados

As exigências abaixo registram propriedades de produto e seus limites; não inventam metas técnicas sem baseline e não escolhem infraestrutura. Os testes específicos serão definidos posteriormente, caso o desenvolvimento seja autorizado.

## RQ-01 — Integridade histórica

Respostas, ocorrências, decisões, consolidações e retificações não devem apagar eventos anteriores; reconstruir quem, o quê e quando.

**Verificação futura / fronteira** Dado registro alterado, verificar existência de valor anterior, valor atual e proveniência apropriada.

**Fonte** S02; S05; S12 DEC-DATA-001/006/011/012

## RQ-02 — Privacidade por perfil

Atletas não acessam dados privados de outras pessoas; concessão de acesso não pode depender somente de ocultar botão.

**Verificação futura / fronteira** Dada tentativa de acesso por usuária distinta, verificar negação no contrato executável, não só na interface.

**Fonte** S02 Q008; S28–S30

## RQ-03 — Mobile-first real

Interações curtas e legíveis em telas pequenas, sob sol forte, toques de uma mão e teclado móvel.

**Verificação futura / fronteira** Avaliar fluxo de responder e registrar ocorrência em smartphone sob condições reais.

**Fonte** S01 Q004–Q008; S29

## RQ-04 — Clareza de estados

Distinguir estado esportivo (não respondeu), interação (enviando/erro) e entrega (carregando/desatualizado); status não depende de cor apenas.

**Verificação futura / fronteira** Em estado pendente ou erro, interface não apresenta gravação definitiva nem equivale silêncio a NÃO.

**Fonte** S02; S29

## RQ-05 — Conectividade e recuperação

Falta/retorno de conexão devem ser compreensíveis e não produzir afirmação falsa de envio ou armazenamento.

**Verificação futura / fronteira** Dada falha de rede durante declaração, exibir estado recuperável e somente indicar sucesso com evidência de gravação.

**Fonte** S01; S29; S30

## RQ-06 — Baixo custo e baixa manutenção

A solução futura deve respeitar restrição do responsável a gasto operacional baixo, sem infraestrutura desproporcional ao elenco.

**Verificação futura / fronteira** Comparar custo recorrente e risco antes de ratificar arquitetura física; não alegar custo zero de serviço não verificado.

**Fonte** S01 Q006; S02

## RQ-07 — Semântica e proteção de dados sensíveis

Dado de saúde só entrará em escopo próprio posterior, com regras adequadas de acesso/finalidade; não confundir disponibilidade com diagnóstico.

**Verificação futura / fronteira** No MVP, não depender de wellness ou diagnóstico para apurar presença/quórum.

**Fonte** S01 Q005; S02; S03; S39

## RQ-08 — Consistência do ciclo

Não admitir transição contraditória, reativação de cancelada ou confirmação silenciosa fora de regras definidas.

**Verificação futura / fronteira** Dado ciclo CANCELADO, tentar transformá-lo em CONFIRMADO deve não reativar o registro original.

**Fonte** S05; S06; S07

## RQ-09 — Tempo e efeitos determinísticos

Checkpoint D-5 necessita produzir um resultado único no fluxo normal; estratégia de processamento, concorrência e reprocessamento ainda por decidir.

**Verificação futura / fronteira** Especificar futuramente ensaios de repetição de checkpoint e evitar transições duplicadas, sem alegar implementação agora.

**Fonte** S05; S06

## RQ-10 — Acessibilidade e feedback

Interface deve favorecer leitura, alvo de toque e mensagens sem ambiguidade; nível formal de conformidade WCAG não foi ratificado.

**Verificação futura / fronteira** A aceitação final requer critérios quantitativos a definir no projeto técnico, sem inventá-los neste PRD.

**Fonte** S29

# 9. Separação entre regras de produto e implementação técnica

## 9.1 Direção documentada e alternativas concorrentes

| **Linha** | **O que a fonte sustenta** | **Situação neste PRD** |
| --- | --- | --- |
| PWA mobile-first | Forma de entrega explicitamente indicada pelo responsável. [S01 Q007; S02] | Direção de produto documentada. |
| --- | --- | --- |
| Next.js + Vercel + Supabase | Faz parte de documento CEPRAEA WEB e roadmap de dashboards. [S21; S22] | Proposta/histórico; não adotada automaticamente. |
| --- | --- | --- |
| React 19 + TypeScript + Vite + Supabase | AESDS-03 descreve um snapshot de fundação de repositório. [S30] | Não verificado como implementação nem autoridade final. |
| --- | --- | --- |
| PostgreSQL, migração, RLS, tabelas | Propostas no BancoCEPRAEA, CEPRAEA-DB e DEC-DATA. [S12; S23; S24] | Planejamento de dados, não banco implantado. |
| --- | --- | --- |
| Offline, service worker, push, login | Alternativas técnicas diversas; escopo offline e autenticação seguem abertos. [S04; S21; S30] | Sem solução física eleita por este PRD. |
| --- | --- | --- |
| Git, Codex, Claude Code, agentes, testes | Organização do processo e propostas de engenharia. [S25–S38] | Não substituem requisitos nem autorizam desenvolvimento. |
| --- | --- | --- |

## 9.2 Decisões ainda necessárias somente quando aplicáveis

-   Persistência, hospedagem e execução que caibam no orçamento e sejam compatíveis com operação de 20 usuários iniciais. [S04 OPEN-TECH-002]
-   Autenticação e autorização executáveis para os dois perfis, com privacidade efetiva. [S04 OPEN-TECH-003; S28–S30]
-   Conectividade e eventual política offline, sem presumir armazenamento local de dados sensíveis ou sincronização irrestrita. [S04 OPEN-TECH-004]
-   Canal, temporalidade e tecnologia de lembretes/notificações. [S04 OPEN-TECH-005]
-   Uso de deadline_at explícito nas solicitações e regras específicas de reabertura elegível, respeitando D-5 e cancelamento terminal. [S07; S12 DEC-DATA-046]

Nenhuma dessas questões é resolvida aqui pela escolha de uma ferramenta ou arquitetura de referência. Não são bloqueios para elaborar PRD, mas podem bloquear implementações dependentes delas. [S08–S12]

# 10. Evolução, divergências e decisões documentadas

## 10.1 Decisões com suporte humano direto ou reportado

| **Registro** | **Evidência e alcance** | **Estado de autoridade** |
| --- | --- | --- |
| C-NOME | Nome CEPRAEA BEACH PRO e momento de descoberta/definição, localizado em conversations-008.json; mensagem 9fd94f21-5de8-44b2-881c-46ef9d2eb316. | Ato humano direto, escopo da denominação. |
| --- | --- | --- |
| B-01 / DEC-PWA-001 | Em 13/10/2026, aprovação de cancelamento automático por falta de quórum em D-5 para sessão PUBLICADO do fluxo normal. | Ato humano direto localizado em conversations-011.json, mensagem d7a5906b-9a48-42d4-a6c3-7a46452d3c19. |
| --- | --- | --- |
| B-02 / DEC-PWA-002 | Documento transcreve aprovação da alternativa A: CANCELADO terminal, sem reativação pela reabertura. | SUSTENTADO PARCIALMENTE: relato documental; mensagem original não localizada no corpus exportado. |
| --- | --- | --- |
| LOTE-001 completo v0.3.0 | Contrato candidato de produto/domínio traz registro P6 não aprovado, P7 não executado. | NÃO homologado integralmente. Não se converte em baseline apenas pela existência. |
| --- | --- | --- |

## 10.2 Formulações comprovadamente revistas no corpus documental

**SUPERSEDED-001** Fechamento às 20h da véspera, 24 horas antes ou em horário genérico de D-5. → D-5 é exatamente início_da_sessão − 120 horas. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-002** Wellness Pré + Pós determina presença. → Wellness é evidência; treinador consolida presença e participação. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-003** Eu crio todos os treinos. → Sistema gera proposta mensal; eu reviso por exceção. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-004** O mínimo operacional é 1G + 3D + 4A. → O mínimo é oito atletas distintas: quatro no Ataque e quatro na Defesa, com pelo menos uma Goleira dentro da alocação defensiva. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-005** Atacante, Defensora e Goleira bastam como modelo. → Taxonomia é Fase → Sistema → Posição. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-006** Resposta antecipada pode ser presença factual. → Disponibilidade, presença e participação são fatos diferentes. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-007** Número bruto de baixas ou uma classificação separada de falha crítica define a condição pós-confirmação. → Existe somente QUÓRUM_COMPROMETIDO; quantidade, margem e capacidades ausentes aparecem no diagnóstico. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-008** Produto completo e MVP possuem o mesmo escopo. → A primeira entrega segue o escopo delimitado nesta elicitação; as demais capacidades são futuras. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-009** Quórum garantido antes de D-5 permite confirmação antecipada manual. → Antes de D-5, o sistema apenas informa QUÓRUM_GARANTIDO; a confirmação automática ocorre no fechamento. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-010** Quórum insuficiente em D-5 produz AGUARDANDO_DECISÃO_DO_TREINADOR. → Em D-5, produz CANCELADO — FALTA_DE_QUÓRUM automaticamente; o treinador só decide quando uma sessão já confirmada perde quórum. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-011** Apenas a quinta-feira recorrente recebe ajuste automático quando coincide com feriado. → A proposta mensal inclui sessões possíveis nos feriados nacionais e oficiais aplicáveis à cidade do Rio de Janeiro, sugeridas entre 07h30 e 09h00. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-012** Faixas estimadas de horas administrativas são o principal critério de sucesso do MVP. → O critério principal é ações administrativas obrigatórias do treinador no fluxo semanal normal = 0; horas economizadas serão indicador futuro após baseline real. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-013** Apenas a Presença consolidada possuía mecanismo fechado para correção de erro factual. → Presença e Participação não são sobrescritas; somente o treinador/administrador pode retificá-las com valor anterior, novo valor, motivo, autoria e data/hora. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-014** Participante convidada precisava ser cadastrada com posição válida para contar no quórum. → Participantes convidadas não fazem parte do produto; diante de quórum comprometido, eu apenas mantenho ou cancelo o treino. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

**SUPERSEDED-015** Data ou horário de sessão publicada podiam ser substituídos por edição. → REMARCAR TREINO cancela a sessão original e cria uma nova, sem transportar disponibilidades. [S02 §SUPERSEDED; cotejar S01/S05/S06 quando pertinente]

## 10.3 Divergências vigentes e delimitação

### B-01 / D-5 sem quórum

Formulações/evidência: S01 preserva regra de aguardar treinador; S02 posterior prevê cancelamento automático; C-B01 registra fala explícita aprovatória em 13/10.

Juízo: CONTRADITO PELA EVIDÊNCIA o uso da regra antiga como vigente no escopo de B-01; cancelamento automático SUSTENTADO INTEGRALMENTE para fluxo normal, não para já CONFIRMADO.

### B-02 / reabertura

Formulações/evidência: S12 DEC-DATA-046 permite reabrir solicitação elegível; S07 documenta que não reativa CANCELADO.

Juízo: SUSTENTADO PARCIALMENTE para aprovação B-02 (sem turno original no JSON). Distinção solicitação ≠ sessão preservada; casos específicos de reabertura NÃO DOCUMENTADOS.

### B-03 / identidade/versões

Formulações/evidência: S11 declara “B-03 normalizada no derivado”; revisão de identificadores e linhagem ainda observada nos candidatos.

Juízo: NÃO VERIFICADO como ato independente de ratificação integral; não promover normalização documental a decisão de produto.

### B-04 / autoridade documental

Formulações/evidência: S08/S11 indicam questão pendente; fontes se declaram canônicas ou homologadas mutuamente.

Juízo: NÃO DOCUMENTADO um ato humano que homologue o contrato reconciliado completo; B-04 pendente.

### S01 vs S02 / escopo

Formulações/evidência: S01 contém ideias mais extensas, prazos/métricas antigos; S02 retira Wellness/scout da primeira entrega.

Juízo: Usar S01 para história/problemas; tratar S02 como formulação posterior documentada, sem inferir aceite global independente.

### Stack Next vs Vite

Formulações/evidência: S21/S22 descrevem Next.js+Vercel; S30 cita React/Vite+Supabase e outros artefatos postergam tech.

Juízo: SEM SUSTENTAÇÃO SUFICIENTE para declarar stack completa definitivamente aprovada ou código funcionando.

### Planilhas vs “banco do produto”

Formulações/evidência: S13/S39–S43 têm operações e dados já existentes; S23/S24 especificam futuro banco.

Juízo: Confundir sistemas seria CONTRADITO PELA EVIDÊNCIA e pela premissa do usuário: operação atual ≠ BEACH PRO.

### Rótulos de teste PASS

Formulações/evidência: S11 aponta verificações textuais direcionadas; S10 testes futuros especificados; S30 fala em stack de testes.

Juízo: NÃO VERIFICADO funcionamento do produto; PASS textual não prova funcionalidade.

# 11. Questões abertas, hipóteses e critérios de decisão

## 11.1 Pendências materiais já presentes nas fontes

### D01 — B-02: mensagem primária não localizada nos 12 arquivos

S07 transcreve aceite; nenhum turno exportado correspondente foi identificado pelo texto exato.

**Classificação** NÃO_BLOQUEANTE para conhecimento da proposta; DECISÃO_HUMANA/PROVENIÊNCIA para alegação de aprovação independente.

### D02 — B-03/B-04 e homologação integral do LOTE-001

S08 e S11 registram candidatos e pendência de autoridade; P6 não passou, P7 não executado.

**Classificação** BLOQUEANTE somente para uso do LOTE como baseline integral; NÃO_BLOQUEANTE para esta síntese.

### D03 — Reabertura de coleta fora do fluxo D-5

S12 DEC-DATA-046 prevê reabertura auditável por autorização; S07 só decide que CANCELADO não reativa.

**Classificação** DECISÃO_HUMANA futura quando caso concreto exigir; sem inventar estados.

### D04 — Arquitetura física, hospedagem, autenticação, offline, notificações

S04 OPEN-TECH-002..005 e propostas S21/S30 divergem.

**Classificação** NÃO_BLOQUEANTE para concepção e documento; decisão técnica futura.

### D05 — Modelo de permissões e privacidade executável

Atleta acessa só dados próprios; detalhes RLS/autenticação permanecem propostas.

**Classificação** NÃO DOCUMENTADO contrato executável aprovado e testado.

### D06 — Data real de início de produto e cumprimento da meta temporal

07/09/2026 consta como prazo histórico da elicitação, sem produto entregue.

**Classificação** HIPÓTESE/PRAZO SUPERADO COMO FATO ATUAL; não reportar “lançado”.

### D07 — Viabilidade do piloto em 42 horas e adesão de atletas

S04 HYP-001–003; nenhum teste funcional BEACH PRO.

**Classificação** HIPÓTESE ainda não validada.

### D08 — Fonte de horário local e feriados em runtime

Regra esportiva foi definida para Rio; provedor técnico de feriados não.

**Classificação** NÃO_BLOQUEANTE documental; solução técnica não definida.

### D09 — Cobertura integral de fontes acessíveis, revisões e multimídia

Este levantamento leu corpus JSON e conteúdo de muitos documentos, mas não inspecionou célula a célula cada planilha, PDFs/imagens, ZIPs, comentários e todas revisões do Drive.

**Classificação** LIMITAÇÃO MATERIAL DE COBERTURA; não declarar exaustividade absoluta.

## 11.2 Hipóteses operacionais não testadas

-   HYP-001: as atletas adotarão o produto diretamente; não existe teste empírico do CEPRAEA BEACH PRO. [S04]
-   HYP-002: escopo completo da primeira entrega poderia caber em aproximadamente 42 horas; data e estimativa são históricas e sem comprovação de viabilidade. [S04]
-   HYP-003: reduzir administração e liberar tempo produzirá melhora real de rotina; não há baseline quantitativa medida. [S01 Q009; S04]
-   Dados da operação real exigem regras explícitas antes de qualquer migração; formato, limpeza e qualidade do legado não provam schema futuro aprovado. [S12; S13; S23/S24]

# 12. Critérios de aceite do PRD e condição de arquivo mestre

Este documento é uma proposta de especificação da intenção do produto, produzida para apreciação pelo responsável. Ela não autoriza implementação ou migração apenas pela entrega. Diferenciar aceite documental, autorização de desenvolvimento e aceitação de software futuramente executado.

## 12.1 Para reconhecer o PRD como documento mestre de PRODUTO

-   O responsável aprova expressamente a versão completa deste PRD ou aponta as alterações necessárias; título, data e nomes de fases em arquivos antecedentes não substituem esse ato.
-   O escopo da primeira entrega e da visão FUTURE é validado como aqui separado, sem trazer automaticamente planos e recursos históricos mais amplos.
-   As divergências com efeito de produto estão resolvidas ou permanecem explicitamente abertas, sem delegar escolhas de produto a artefatos de arquitetura.
-   Cada requisito mantém vínculo às evidências e classificação; redação derivada por IA não vira decisão humana sem confirmação.
-   A integridade do acervo de origem é preservada por cópias verificáveis e indexadas antes de qualquer remoção no Drive; apagar arquivos destrói links e provas que este PRD cita.
-   O PRD aprovado é então indicado como a referência central de INTENÇÃO E REQUISITOS do software, não como substituto material de históricos operacionais, fontes legais, arquivos originais de decisão, dados brutos, schemas executáveis ou relatórios de teste futuros.

## 12.2 Não constitui DONE

Não comprova qualquer implementação, teste, deploy, operação por atletas, migração, segurança efetiva ou redução de horas. Também não autoriza apagar em lote documentos e planilhas atuais — sobretudo os que contêm dados reais da operação esportiva. A exclusão é ação distinta, irreversível ou de recuperação incerta, que exige seleção e confirmação específicas. [S03; S08–S12; documentos da operação]

# Anexo A. Rastreabilidade e fontes históricas

Os códigos S01–S52 preservam as referências presentes no documento de consolidação, sem afirmar que as URLs continuarão funcionais após exclusão. IDs de Drive ajudam a identificar arquivos apenas enquanto ainda existirem no provedor; backup/export com nome, conteúdo, hash e localização torna-se indispensável se a decisão futura for eliminar versões do Drive.

**S01 —** Beach Handball PWA — Product & Domain Specification (S1, 01/09/2026): https://docs.google.com/document/d/1X683QQ9cCEQJwebYW3U394OZEvLXFfBWjZQlNZQ-58c/edit — elicitação histórica, respostas em 1ª pessoa e formulações concorrentes

**S02 —** CEPRAEA BEACH PRO — Elicitação de Produto e Regras do Domínio v2.10 (S2, 02/09/2026): https://docs.google.com/document/d/19-WeGMs7Q25qhAN6OnWMnae1Ll_1EjiTnWsWvGQjORA/edit — síntese textual de produto; o rótulo DECIDED não substitui aprovação independente

**S03 —** 02-PROJECT-CHARTER.md: https://drive.google.com/file/d/1UdoUt12z4LLKsQD-2DWJHJOJW8yob0dl/view — visão, resultados observáveis, escopo da primeira entrega e FUTURE

**S04 —** 03-SHARED-UNDERSTANDING.md: https://drive.google.com/file/d/1yr04V9gpdPcfRpqSiKbuxXmxI93YIUcx/view — conceitos, atores, fluxos e hipóteses; derivado da elicitação

**S05 —** TRAINING_FLOW_CONTRACT.md v1.6: https://drive.google.com/file/d/1E6kh2MbDHi_84wDE55hHKmYdEfNq9M7e/view — contrato lógico de transições derivado; não arquitetura física

**S06 —** DEC-PWA-001 — B-01, cancelamento automático em D-5 (13/10/2026): https://docs.google.com/document/d/1308tVRRuKydsSMN-9M5ZIifxo3nye0yNg1SF4tQ7dTo/edit — registro da decisão com transcrição confirmada no histórico exportado

**S07 —** DEC-PWA-002 — B-02, cancelamento terminal (13/10/2026): https://docs.google.com/document/d/1kqWcLdNbaK_MbiBiIup_9xzeqMInFvIH9y3mMkzj4yM/edit — registro do Drive que transcreve aprovação; mensagem original não localizada nos 12 JSONs

**S08 —** Contrato reconciliado de produto/domínio — LOTE-001 candidato v0.3.0: https://docs.google.com/document/d/1fhtyJfrFvcwh4Kf7rFj3_K1-NUPByiOfwc1KJHIt86A/edit — candidato não efetivo, homologação integral pendente

**S09 —** Matriz de afirmações e evidências — LOTE-001 revisão 0.2: https://docs.google.com/document/d/1dfBT40pl8ocMW7to3EcsEo7AIbghO0M1Ob28KoMy84Y/edit — 25 claims textuais, cobertura declarada parcial

**S10 —** Requisitos e testes candidatos — LOTE-001 revisão 0.2: https://docs.google.com/document/d/1kaK-w5b2SQztL-mk6XO_d0vc4m5Bncjpr6UebvF6a_U/edit — 18 requisitos/cenários candidatos, sem testes de produto executados

**S11 —** CEPRAEA LOTE-001 — Relatório de validação e manifestos (13/10/2026): https://docs.google.com/document/d/1Gw5pA3zO0FOQ1he1DwiOQs59B6jimUs7EXATnSgRVE0/edit — P6 não passou, P7 não executado; versão integral não homologada

**S12 —** 08-REGISTRO-DE-DECISÕES-ARQUITETURAIS — DADOS: https://docs.google.com/document/d/1N6KpxNqGPxkT0F1ZBk9gCCWbICYFwjUwyCLfri0tr0k/edit — DEC-DATA-001.. e DEC-DATA-046: propostas/políticas declaradas; autoridade de adoção específica a verificar

**S13 —** Regras de Negócio — CEPRAEA BEACH PRO: https://docs.google.com/document/d/1e85S7bSrpfMQPh_xk2qrcaFAo1wytQK3ea9F7nc-n1A/edit — regras derivadas do legado CEPRAEA DATABASE, não promoção automática ao futuro software

**S14 —** Proposta de Requirements: https://drive.google.com/file/d/1AcxBm6F4pCu-X_g9W1nkP126FAqkkUcz/view — texto propositivo de requisitos; aprovação individual não verificada

**S15 —** 07-TRACEABILITY.md: https://drive.google.com/file/d/1pcsMI8qDp2VoD8cBWgAT17N4PFoeho-5/view — rastreabilidade documental, Gate C não executado na revisão lida

**S16 —** 04-REQUIREMENTS.md — modelo: https://drive.google.com/file/d/18z6ow4K8uWTziw_hxTc4JMuHpaU3oc_W/view — template não preenchido; não é especificação aprovada

**S17 —** 11-ARCHITECTURE-OPTIONS.md — modelo: https://drive.google.com/file/d/1PRP2o2-n4Oxb5Xx8zjwNIGx9uc_nj8j7/view — template de comparação técnica em branco

**S18 —** 12-ARCHITECTURE.md — modelo: https://drive.google.com/file/d/1ircD2reoB3znZYOz3-hAruIq7E9qYCfH/view — template de arquitetura em branco

**S19 —** BASE CEPRAEA BEACH PRO — v0.1: https://drive.google.com/file/d/1q2638UlqF3cC392PlN2L9w_P3jz1qKVD/view — base documental derivada marcada PROPOSED

**S20 —** BASE CEPRAEA BEACH PRO — v0.2 — Fundação e Acesso Multiagente: https://drive.google.com/file/d/1FAyi8WvGuc4cUwlnYRsEQmj64NSXqW3m/view — proposta de fundação e acesso, conteúdo heterogêneo

**S21 —** CEPRAEA WEB — Conectando dados da areia à vitória: https://docs.google.com/document/d/1e43cM_cprntNbWyMmm9Cpqx1TXPjM4Z_upc3bABPcV4/edit — visão histórica divergente: Next.js/Supabase e afirmação de software existente

**S22 —** Roadmap de Implementação dos Dashboards: https://drive.google.com/file/d/1QYo4q89sYNWpXhR0DvJXlj4rRPGFiQIm/view — plano Vercel+Supabase+planilhas; alternativa histórica, sem confirmação do futuro produto

**S23 —** BancoCEPRAEA.docx: https://drive.google.com/file/d/1xwhwfJdXZ_cjKO28uc6hy--ocEldbNfd/view — modelagem SQL/Supabase proposta, não banco instalado

**S24 —** CEPRAEA-DB.docx: https://drive.google.com/file/d/1FKOk0-lhgdnlTOAsjdCBuzf97_2gRp3v/view — plano mestre de dados para execução futura

**S25 —** Manual Operacional — CEPRAEA Beach Pro: https://drive.google.com/file/d/14mNOwF7_IHXq8iqcSjNEzKy6p6UOLuso/view — roteiro de uso de IA, NotebookLM e IDE, não prova operacional

**S26 —** FLUXO COMPLETO DE DESENVOLVIMENTO — CEPRAEA BEACH PRO: https://drive.google.com/file/d/1F_ckYZtNrya-4qnq4EBjOZuestQkfPlZ/view — processo proposto; rótulos de homologação carecem verificação independente

**S27 —** AESDS 00 — Índice mestre: https://drive.google.com/file/d/1UUAenfd7_iFb7OmGU5xpPG-2lzUQtqQz/view — catálogo de documentos para execução com agentes

**S28 —** AESDS 01 — Contrato de produto e domínio: https://drive.google.com/file/d/1Hs2BoOFWBTodY5uVXgnpzYhew-uwEO4m/view — orientação de semântica e fronteira produto/UI

**S29 —** AESDS 02 — Experiência e interação: https://drive.google.com/file/d/1cLr8XR8tLouarqCrxeB9g2OBm0zYt3sv/view — UX mobile-first, estados e recuperação propostos

**S30 —** AESDS 03 — Arquitetura técnica frontend: https://drive.google.com/file/d/1RHyLJV8iA1RD9PrKqDUtvqB8GuLIFuJh/view — snapshot declarado React/Vite/Supabase; não verificado em runtime

**S31 —** AESDS 04 — Roadmap e grafo de tarefas: https://drive.google.com/file/d/1xsuNGvuRn6U6TjH_UrN7Psy5MAqH6Dwl/view — sequência F0–F12 proposta, sem execução evidenciada

**S32 —** AESDS 05 — Tarefas atômicas e critérios: https://drive.google.com/file/d/1Mv7HjMWZalL0fS_BayjvWXfykJvhRRu1/view — planejamento de trabalho com agentes

**S33 —** AESDS 06 — Testes e verificação: https://drive.google.com/file/d/15xvEXOZZ5C-vnq1w3E1kyfmw92hqAJTV/view — proposta de testes, não resultados

**S34 —** AESDS 07 — Execução e review dos agentes: https://drive.google.com/file/d/1VUfsmjzvU2SWIo6vNX9-p64ZmcYnAPzF/view — procedimentos para execução futura

**S35 —** AESDS 08 — Catálogo de referências: https://drive.google.com/file/d/1hf7hD161qmqwHQioYTrAIfcVw0tqtdfX/view — referências e protocolo documental

**S36 —** AESDS 09 — Runbooks e estado operacional: https://drive.google.com/file/d/1QrA82AnyJdInWFuRCYAnTlTOoAz-fAfD/view — inventário de procedimentos não confundível com software funcionando

**S37 —** AESDS 10 — Artefatos, papéis e enforcement: https://drive.google.com/file/d/1Ao95Uu4SmoJtVgeAg46H9vzT6crJIETK/view — documento extenso com sinais de drift e revalidação

**S38 —** AESDS 11 — Auditoria/assurance agêntico: https://drive.google.com/file/d/1x1_uKzarnVqD9COQX8J5_EOU5vG0InTK/view — proposta de mecanismos de qualidade

**S39 —** CEPRAEA — Wellness — Configuração e Respostas.xlsx: https://drive.google.com/file/d/17e5YOWjXDjpBQV6Tx6UeHnI6fobpRhG4/view — dados operacionais pré/pós do CEPRAEA, NÃO recurso implementado no Beach Pro

**S40 —** CEPRAEA AGOSTO 2026.xlsx: https://drive.google.com/file/d/13TlMsjqUHXeRJk378tBSagea3wCjxLGS/view — agenda/gestão atual, evidência de problemas e terminologia

**S41 —** CEPRAEA DATABASE.xlsx: https://drive.google.com/file/d/1RIbDM9R8PcDunxN2vXUy2Jdnj8fwBBM2/view — planilha operacional, não banco do produto novo

**S42 —** Plano — Pesquisa de Disponibilidade e Grupo Treinável — Brasileiro 2026: https://docs.google.com/document/d/1L5rIMdz0-Bs13fQ1GjCT7Akmdki0Wm8iWI75sZ76v8s/edit — decisão esportiva operacional, pontuação de horários distinta da regra MVP

**S43 —** Dicionário de Dados Canônico CEPRAEA: https://docs.google.com/document/d/1EAobzpLQFYTiYd8xUmBv_ArQeaFu3U-_ZukBGz6AinE/edit — semântica do legado; verificar antes de converter em requisito

**S44 —** [ATIVO] Mapeamento Mestre de Fontes e Metadados: https://docs.google.com/document/d/1OsZpqYak84xuvdNUo4FaIi_9n8tVjBlLxCSQeHbo4Fg/edit — índice de fontes; rótulo ATIVO não demonstra aprovação das regras do produto

**S45 —** Inventário de Fontes CEPRAEA - Google Drive: https://docs.google.com/document/d/1bZ7noN_MShpmbR58kKnCZFYOh8C-nsU82u4ykPKmbtA/edit — catálogo de fontes temáticas, sem substituir originais

**S46 —** Constituição do Projeto de Reorganização do Google Drive: https://docs.google.com/document/d/1ytvfgxUr6w05ChXTc6u-3X_r8UduoqAUKglJqoSeo3o/edit — governança de repositório, não aprovação de requisitos do software

**S47 —** [ATIVO] 20-CURRENT-STATE-INDEX: https://docs.google.com/document/d/1i9XtjdPMGJhYSbV6Al5QdzV1iWRMNJ9c58zZXUK-z8g/edit — índice documental com metadados autoatribuídos

**S48 —** CEPRAEA BEACH PRO.docx (guia técnica de scripts): https://drive.google.com/file/d/1-AZ5zsS4fZ5PGmc96iWocFg1u6AzZZ30/view — material técnico diverso; código citado não prova implementação

**S49 —** CEPRAEA BEACH PRO (Google Doc extenso): https://docs.google.com/document/d/126eCVhvAbZpSvdbOvyVxo_VGXZkuWpPe--TouQ_FImM/edit — documentação histórica técnica multiaba

**S50 —** SFA-20260906-001 — Auditoria de Fidelidade de Escopo: https://drive.google.com/file/d/18JOrD9Kjk7Uvgt8iPlb8xRI9mGIOM69q/view — auditoria documental, não execução do software

**S51 —** README — Kit de Engenharia Assistida por IA: https://drive.google.com/file/d/1SOLe32wDdvNBEQ5Vj2vEcrKkPMo3CKke/view — kit de engenharia rastreável e templates

**S52 —** CEPRAEA — Benchmark Visual UX/UI dos Dashboards: https://drive.google.com/file/d/17eL1JqkbliCqezp7CvZC1JZh4s-naU79/view — referência visual futura, não interface pronta

# Anexo B. Mensagens originais e localização no export

C-NOME: Decisão do nome e estágio descoberta/definição de contexto. conversations-008.json | conversa UUID 6a621d8d-f9cc-83e9-b970-3ae425e9e756 | mensagem UUID 9fd94f21-5de8-44b2-881c-46ef9d2eb316 | data inicial 2026-07-23.

Abrir conversa C-NOME: https://chatgpt.com/c/6a621d8d-f9cc-83e9-b970-3ae425e9e756 — link de conveniência; ID de exportação permanece a prova estável

C-ELICITACAO: Aprimoramento de Q-001 a Q-013 e texto da elicitação. conversations-009.json | conversa UUID 6a96c893-8ed8-83e9-a6c4-f3fbadab1960 | mensagem UUID a3a3993e-4784-48e2-bbae-b32fe99661b8 | data inicial 2026-09-01.

Abrir conversa C-ELICITACAO: https://chatgpt.com/c/6a96c893-8ed8-83e9-a6c4-f3fbadab1960 — link de conveniência; ID de exportação permanece a prova estável

C-D5: Declaração do responsável: responder cinco dias antes. conversations-009.json | conversa UUID 6a96c893-8ed8-83e9-a6c4-f3fbadab1960 | mensagem UUID 84a1c34f-48a8-460d-aeae-1bcfc7671103 | data inicial 2026-09-01.

Abrir conversa C-D5: https://chatgpt.com/c/6a96c893-8ed8-83e9-a6c4-f3fbadab1960 — link de conveniência; ID de exportação permanece a prova estável

C-B01: Aprovação humana explícita B-01 cancelamento automático D-5. conversations-011.json | conversa UUID 6accffd6-0740-83e9-a756-b2f16bda5b17 | mensagem UUID d7a5906b-9a48-42d4-a6c3-7a46452d3c19 | data inicial 2026-10-12.

Abrir conversa C-B01: https://chatgpt.com/c/6accffd6-0740-83e9-a756-b2f16bda5b17 — link de conveniência; ID de exportação permanece a prova estável

C-WELLNESS: Operação atual: Wellness Pré apenas em dias de treino. conversations-009.json | conversa UUID 6a7e3d6a-2058-83e9-8105-094fb1e16920 | mensagem UUID 0dbc81cf-7a49-4f0c-8d6e-c76ba7170a92 | data inicial 2026-08-13.

Abrir conversa C-WELLNESS: https://chatgpt.com/c/6a7e3d6a-2058-83e9-8105-094fb1e16920 — link de conveniência; ID de exportação permanece a prova estável

C-SCOUT: História de análise/scout em handebol de praia, fora do primeiro produto. conversations-007.json | conversa UUID 69f8b0f9-9618-83e9-af5d-0cb25641d468 | data inicial 2026-05-04.

Abrir conversa C-SCOUT: https://chatgpt.com/c/69f8b0f9-9618-83e9-af5d-0cb25641d468 — link de conveniência; ID de exportação permanece a prova estável

C-DADOS: Modelagem e pesquisa de dados, não execução do banco novo. conversations-011.json | conversa UUID 6ac87280-41c8-83e9-b758-082b553c7bc8 | data inicial 2026-10-09.

Abrir conversa C-DADOS: https://chatgpt.com/c/6ac87280-41c8-83e9-b758-082b553c7bc8 — link de conveniência; ID de exportação permanece a prova estável

C-CONTEXTO: Discussão proporcionalidade de arquitetura e contexto Beach Pro. conversations-008.json | conversa UUID 6a725d1b-5628-83e9-9f4d-f268b8893744 | data inicial 2026-08-04.

Abrir conversa C-CONTEXTO: https://chatgpt.com/c/6a725d1b-5628-83e9-9f4d-f268b8893744 — link de conveniência; ID de exportação permanece a prova estável

C-QUORUM: Conceitos de fluxo, disponibilidade e viabilidade. conversations-008.json | conversa UUID 6a750dbd-2a4c-83e9-9ba5-5276b280207a | data inicial 2026-08-06.

Abrir conversa C-QUORUM: https://chatgpt.com/c/6a750dbd-2a4c-83e9-9ba5-5276b280207a — link de conveniência; ID de exportação permanece a prova estável

C-PLANILHAS: Consulta operacional a planilhas CEPRAEA. conversations-008.json | conversa UUID 6a61b56f-1b54-83e9-a938-5dea43f004af | data inicial 2026-07-23.

Abrir conversa C-PLANILHAS: https://chatgpt.com/c/6a61b56f-1b54-83e9-a938-5dea43f004af — link de conveniência; ID de exportação permanece a prova estável

Nota B-02: a citação literal de aprovação aparece em S07; a pesquisa de texto no corpus dos 12 arquivos não encontrou a frase exata “aprovo a alternativa A”, tampouco “Para B-02, aprovo...”. Por isso, não se atribui a ela um UUID de mensagem fictício.

# Anexo C. Vocabulário e fronteiras finais

**PWA** Progressive Web App: aplicação web pensada para acesso móvel e, quando autorizado, comportamento instalável; não implica offline automaticamente.

**MVP/primeira entrega** Primeira capacidade do produto pretendida, ainda não desenvolvida; neste documento não equivale a aprovação integral nem release realizado.

**D-5** Checkpoint 120 horas antes do início de cada sessão publicada, no fluxo normal documentado.

**Quórum operacional** Composição funcional e alocável de pessoas/posições; não simples total de respostas SIM.

**Disponibilidade** Declaração individual anterior ao treino ou ausência de declaração; não comparecimento factual.

**Presença** Fato de comparecimento registrado/consolidado pelo treinador após a sessão.

**Participação** Fato de realização completa, parcial ou nula da sessão pela atleta, diferente de presença física.

**Retificação** Correção de fato consolidado preservando original e trilha de autoria/momento/motivo.

**FUTURE** Capacidade desejada para uma versão posterior; não entra implicitamente no primeiro escopo.

**Baseline** Versão de referência formalmente aprovada; título de pasta/arquivo ou PASS textual não é prova de baseline efetiva.

**RLS** Row Level Security: controle de acesso por linha de banco; citado como proposta de implementação, não verificado.

**UX/UI** Experiência e interface; princípios documentados não significam telas prontas.

**Proveniência** Ligação entre afirmação/dado, fonte, autor, data, transformações e decisões; evita confundir derivados com fatos.

**Append-only** Princípio de preservar versões ou eventos anteriores em vez de sobrescrevê-los silenciosamente.

**Gate/PASS documental** Verificação declarada de uma etapa ou arquivo; não comprova software implementado ou aceito fora daquele escopo.

# Anexo D. Evidências preservadas dentro deste PRD

Atos documentais de maior impacto de produto mantidos em texto para que o significado sobreviva ao eventual desaparecimento de um link:

**B-01 — citação do responsável** “Para B-01, aprovo o cancelamento automático por falta de quórum em D-5. Registre a decisão com rastreabilidade e examine as consequências para os documentos.” Fonte original: conversations-011.json, conversa 6accffd6-0740-83e9-a756-b2f16bda5b17; mensagem d7a5906b-9a48-42d4-a6c3-7a46452d3c19. [C-B01; S06]

**B-02 — citação apenas transcrita no documento do Drive** “Para B-02, aprovo a alternativa A: o cancelamento em D-5 é terminal, sem reativação pela reabertura de disponibilidade. Registre e valide as consequências.” [S07] NÃO VERIFICADO independentemente no arquivo exportado; reproduzida como transcrição documental, não como mensagem direta autenticada.

**Formulação antiga concorrente** A fonte S01 mantinha “D-5 com quórum insuficiente nunca cancela automaticamente; exige decisão do treinador”; a fonte S02 e a confirmação B-01 fixam o cancelamento automático apenas para PUBLICADO no fluxo normal. [S01; S02; S06]

**Limite de aplicação da B-01** Queda de quórum depois de CONFIRMADO não cancela automaticamente: treinador precisa decidir MANTER TREINO ou CANCELAR TREINO. B-01 tampouco ratifica arquitetura, SQL, login, testes ou deploy. [S06]

**Reserva de proveniência** Este anexo contém citações limitadas, não cópias íntegras de documentos. O PRD só se torna arquivo mestre seguro caso a origem seja preservada em arquivo histórico acessível e verificável. [S08–S11]

FIM DO DOCUMENTO — CEPRAEA BEACH PRO / PRD v0.1 / CANDIDATO A ARQUIVO MESTRE