## Contexto identificado

A planilha [CEPRAEA JUNHO 2026](https://docs.google.com/spreadsheets/d/14d3vIfkvhkTvjjTxkM7CxA9Oo1etHAgC2KUzGzzEn88/edit) é a **interface operacional da equipe adulta feminina de handebol de praia do CEPRAEA na temporada 2026**.

Ela começou como controle mensal de presença, mas evoluiu para um sistema híbrido que reúne:

-   agenda de treinos;
-   confirmação de presença;
-   disponibilidade para competições;
-   composição funcional do elenco;
-   convocações;
-   operação do dia do jogo;
-   resultados e participação das atletas;
-   análise de desempenho;
-   planejamento técnico;
-   agendamento de feedback individual;
-   registros de alterações e auditoria.

Portanto, o nome **“CEPRAEA JUNHO 2026” não representa mais o escopo real do arquivo**. Atualmente, ele cobre a temporada e já possui informações de julho e de competições futuras.

## Domínio de conhecimento

O domínio principal é **Gestão de Operações Esportivas orientada por dados**.

Os subdomínios presentes são:

| **Subdomínio** | **Aplicação na planilha** |
| --- | --- |
| Gestão de elenco | Cadastro, função, posição e status das atletas |
| --- | --- |
| Planejamento de treinos | Datas, horários, local, objetivo e conteúdo |
| --- | --- |
| Controle de disponibilidade | Respostas SIM, NAO e TALVEZ |
| --- | --- |
| Gestão de competições | Inscrições, relação nominal, cronogramas e cenários |
| --- | --- |
| Gestão de convocações | Atletas convocadas e composição por função |
| --- | --- |
| Análise esportiva | Jogos, vitórias, derrotas, sets e participação |
| --- | --- |
| Planejamento técnico-tático | Cobertura de sistemas defensivos e ofensivos |
| --- | --- |
| Governança de dados | Fonte, validação, auditoria e changelog |
| --- | --- |
| Comunicação operacional | Painéis para atletas e comissão técnica |
| --- | --- |

## Arquitetura real

A planilha analisada não é a fonte canônica de todos os dados. Ela funciona principalmente como **frontend operacional**, alimentado pela planilha separada [CEPRAEA DATABASE](https://docs.google.com/spreadsheets/d/10Dv1oBIKdodWEWsK8qUeLPyazzdg4hdRkVi4gjvVSno/edit).

flowchart TD

DB["CEPRAEA DATABASE — fonte canônica"] --> EX["Exports estruturados"]

EX --> IM["Abas de importação"]

IM --> FE["CEPRAEA JUNHO 2026 — interface"]

MAN["Entradas manuais de atletas"] --> FE

FE --> OP["Agenda, presença e dia do jogo"]

FE --> AN["Análises e painéis técnicos"]



A separação é esta:

| **Camada** | **Responsabilidade** |
| --- | --- |
| CEPRAEA DATABASE | Fonte primária operacional ou SSOT |
| --- | --- |
| DB_ATLETAS | Cadastro canônico de atletas, funções e posições |
| --- | --- |
| DB_TREINOS e DB_CALENDARIO | Treinos e eventos |
| --- | --- |
| DB_PRESENCA | Registros estruturados de presença |
| --- | --- |
| DB_COMPETICOES e DB_JOGOS | Competições, partidas e resultados |
| --- | --- |
| DB_CONVOCACOES | Convocações |
| --- | --- |
| DB_PARTICIPACAO_JOGO | Participação real por atleta e partida |
| --- | --- |
| DB_AUDITORIA_PARTICIPACAO_RESULTADO | Cruzamento entre participação e resultado |
| --- | --- |
| DB_EXPORT_FRONTEND | Dados preparados para a interface |
| --- | --- |
| _IMPORT_DATABASE | Importação no arquivo operacional |
| --- | --- |
| Abas visíveis | Interfaces usadas pela comissão e pelas atletas |
| --- | --- |

## Função das principais abas

-   AGENDA CEPRAEA: disponibilidade das atletas para todas as competições de 2026, prazos de inscrição e risco de composição do elenco.
-   JULHO - 2026: agenda de treinos e confirmação manual de presença.
-   AGENDA TÉCNICA V2: transforma disponibilidade em leitura de risco, foco técnico, exercício-chave e decisão da comissão.
-   🏖️ DIA DO JOGO: interface operacional com local, horários, aquecimentos, jogos, cenários e convocadas.
-   ANÁLISE JOGOS: consolida resultados por competição e participação das atletas.
-   📅 FEEDBACK INDIVIDUAL: agenda conversas individuais por Google Meet.
-   PAINEL DATABASE: demonstra os dados importados da base canônica.
-   _IMPORT_DATABASE e _IMPORT_ANALISE_JOGOS: camadas técnicas de integração.
-   📑_CHANGELOG, _FRONTEND_CHANGELOG e DB_CHANGELOG: rastreiam intervenções e pendências.

## Regras de governança já existentes

A planilha contém regras explícitas importantes:

1.  As respostas manuais das atletas devem ser preservadas.
2.  A IA não pode inferir presença ou disponibilidade.
3.  SIM, NAO, TALVEZ, células vazias e faltas justificadas não podem ser sobrescritos sem autorização.
4.  Convocação não significa que a atleta entrou em quadra.
5.  Participação real só pode ser registrada com fonte ou decisão humana validada.
6.  Resultados e placares devem ser atualizados somente após fonte validada.
7.  As ações automatizadas devem ser determinísticas.
8.  Alterações relevantes devem ser registradas nos changelogs.

## Estado atual identificado

A integração entre o banco e a interface está operacional. Em 23/07/2026 às 03:33, o banco exportava:

-   18 atletas ativas;
-   2 goleiras;
-   4 defensoras;
-   12 atletas de ataque;
-   próximo treino em 23/07/2026;
-   horário 20h00–21h30;
-   local Copacabana.

A análise consolidada registra, no momento da leitura:

-   19 jogos;
-   12 vitórias;
-   7 derrotas;
-   28 sets vencidos;
-   17 sets perdidos;
-   7 shoot-outs;
-   63% de aproveitamento.

## Inconsistências relevantes

1.  **Divergência de elenco:** a aba JULHO - 2026 contém 19 atletas, incluindo Gilvania Balbino, enquanto DB_ATLETAS possui somente 18 atletas e não contém Gilvania. Portanto, a inclusão foi feita no frontend mensal, mas ainda não foi sincronizada com a fonte canônica.
2.  **Módulo antigo quebrado:** a aba oculta PRÓXIMO TREINO ainda aponta para junho e apresenta vários erros #N/A, embora o PAINEL DATABASE possua o próximo treino correto.
3.  **Painel de jogo desatualizado:** 🏖️ DIA DO JOGO continua exibindo a 3ª Etapa Carioca de 05/07/2026, mesmo sendo uma competição passada.
4.  **Planejamento técnico incompleto:** a AGENDA TÉCNICA V2 ainda contém campos como “Preencher foco do ciclo”, “Preencher exercício-chave” e “Preencher decisão”.
5.  **Separação público/técnico pendente:** o próprio DB_CONFIG declara pendente a separação definitiva entre informações públicas para atletas e dados internos da comissão.

## Conclusão operacional

A planilha deve ser interpretada como um **sistema operacional esportivo em evolução**, e não como uma simples planilha mensal.

A fonte canônica é CEPRAEA DATABASE; CEPRAEA JUNHO 2026 é a interface híbrida de consulta e entrada manual. A arquitetura já possui integração, rastreabilidade e regras de preservação, mas ainda não pode ser considerada plenamente consistente enquanto existirem a divergência de elenco, módulos legados quebrados e painéis referentes a eventos passados.

## Qual é a realidade que justifica a existência da planilha?

## Definição canônica

A planilha existe porque o CEPRAEA é uma **operação esportiva competitiva contínua**, na qual elenco, disponibilidade, treinos, competições, convocações e resultados mudam ao longo do tempo.

A realidade que a justifica pode ser resumida assim:

A comissão técnica precisa transformar informações dispersas e mutáveis sobre atletas e competições em decisões operacionais verificáveis, tomadas no prazo correto e com composição esportiva viável.

## A realidade concreta

### 1. O elenco não é estático

Atletas entram, retornam, afastam-se ou mudam de situação. A própria planilha demonstra isso:

-   o banco registra 18 atletas ativas;
-   a aba de julho contém 19 atletas;
-   Gilvania Balbino já aparece no controle mensal, mas ainda não está no banco canônico.

Portanto, não basta possuir uma lista de nomes. É necessário controlar **quem integra oficialmente o elenco em cada momento**.

### 2. Disponibilidade não é presença

Cada atleta pode responder:

-   SIM;
-   NAO;
-   TALVEZ;
-   não responder;
-   justificar uma ausência.

Esses estados representam declarações diferentes. Além disso:

-   estar disponível não significa ser convocada;
-   ser convocada não significa jogar;
-   participar de uma competição não significa participar de todas as partidas;
-   confirmar um treino não comprova presença efetiva.

A planilha existe para impedir que essas condições sejam tratadas como equivalentes.

### 3. A equipe possui várias obrigações simultâneas

A temporada envolve:

-   treinos recorrentes;
-   etapas estaduais;
-   etapas nacionais;
-   Copa Brasil;
-   competição internacional;
-   viagens;
-   inscrições;
-   relações nominais;
-   reuniões;
-   aquecimentos;
-   jogos garantidos;
-   jogos condicionais à classificação.

Cada evento possui datas, horários, local, prazo e estado operacional próprios. Sem registro estruturado, a comissão depende de memória, mensagens de WhatsApp e documentos isolados.

### 4. Quantidade de atletas não garante uma equipe funcional

A comissão não precisa apenas saber quantas atletas estão disponíveis. Precisa identificar se a composição contém:

-   goleiras;
-   defensoras;
-   atletas de ataque;
-   posições específicas;
-   cobertura para os sistemas defensivos;
-   cobertura para os sistemas ofensivos.

Uma competição pode ter muitas atletas confirmadas e, ainda assim, apresentar risco porque falta uma função indispensável. Por isso a planilha calcula disponibilidade, composição e gargalos técnicos.

### 5. Existem limites de convocação e participação

Os registros indicam limites como:

-   até 12 atletas convocadas;
-   até 10 atletas por partida.

Isso exige escolhas. A comissão precisa decidir:

-   quem será convocada;
-   quem ficará fora;
-   quem compõe cada jogo;
-   como equilibrar funções;
-   quais critérios justificam a decisão.

A planilha fornece a memória necessária para que essas escolhas não sejam improvisadas.

### 6. As decisões dependem de fontes diferentes

As informações vêm de:

-   respostas manuais das atletas;
-   decisões da comissão técnica;
-   relações nominais;
-   tabelas oficiais;
-   boletins;
-   resultados;
-   registros de participação;
-   documentos das competições.

Essas fontes não possuem a mesma autoridade. A planilha existe para registrar **qual informação foi recebida, de onde veio e se já foi validada**.

### 7. A informação tem prazo de validade

Um painel correto em 5 de julho pode estar incorreto em 23 de julho. Mudam:

-   o próximo treino;
-   a próxima competição;
-   a disponibilidade;
-   a convocação;
-   os jogos possíveis;
-   os resultados;
-   a situação das atletas.

Por isso, a planilha precisa representar o **estado atual**, conservar o histórico e sinalizar informações desatualizadas.

### 8. Existem públicos diferentes

As atletas precisam visualizar:

-   agenda;
-   horários;
-   local;
-   convocação;
-   orientações;
-   próximos passos.

A comissão técnica também precisa acessar:

-   criticidade das posições;
-   riscos do elenco;
-   planejamento tático;
-   critérios de análise;
-   participação individual;
-   decisões internas.

A planilha, portanto, precisa separar **informação pública operacional** de **informação técnica interna**.

## Problema que existiria sem a planilha

Sem esse sistema, a operação dependeria de informações fragmentadas. As consequências prováveis seriam:

| **Falha de informação** | **Consequência operacional** |
| --- | --- |
| Disponibilidade dispersa no WhatsApp | Convocação baseada em informação incompleta |
| --- | --- |
| Elenco desatualizado | Atleta esquecida ou contabilizada incorretamente |
| --- | --- |
| Falta de controle de posições | Equipe numericamente completa, mas taticamente inviável |
| --- | --- |
| Prazos não centralizados | Perda de inscrição ou relação nominal |
| --- | --- |
| Convocação confundida com participação | Estatísticas individuais incorretas |
| --- | --- |
| Resultado sem fonte validada | Histórico esportivo falso |
| --- | --- |
| Painel antigo apresentado como atual | Comunicação errada com atletas |
| --- | --- |
| Alterações sem registro | Impossibilidade de identificar quem mudou o dado e por quê |
| --- | --- |

## As perguntas que a planilha precisa responder

Em qualquer momento, o sistema deve permitir uma resposta única para:

1.  Quem pertence atualmente ao elenco?
2.  Quem declarou disponibilidade para cada treino ou competição?
3.  Quem foi convocada?
4.  Quem efetivamente jogou?
5.  A equipe possui cobertura suficiente por função e posição?
6.  Qual é o próximo compromisso e o que precisa ser feito?
7.  Quais resultados já foram confirmados?
8.  Qual fonte sustenta cada informação?
9.  Quais pendências impedem uma decisão segura?
10.  O que mudou, quando mudou e quem realizou a alteração?

## Conclusão

A realidade que justifica a planilha não é simplesmente a necessidade de “marcar presença”.

Ela existe porque o CEPRAEA precisa **coordenar uma equipe competitiva com elenco mutável, disponibilidade variável, calendário complexo, restrições de convocação, dependências táticas e informações provenientes de múltiplas fontes**.

Sua função essencial é transformar essa realidade dinâmica em um **estado operacional compartilhado, atualizado e verificável**, a partir do qual a comissão técnica possa decidir:

-   quem treina;
-   quem viaja;
-   quem é convocada;
-   como a equipe será composta;
-   o que precisa ser treinado;
-   o que deve ser comunicado;
-   e quais resultados podem ser considerados verdadeiros.

## Qual é o problema real que a planilha resolve?

## Problema real

A planilha resolve a **falta de uma visão única, atualizada e confiável para operar a equipe**.

Antes dela, as informações necessárias para decidir estavam potencialmente distribuídas entre:

-   mensagens das atletas;
-   memória do treinador;
-   tabelas e boletins oficiais;
-   relações nominais;
-   calendários;
-   anotações de treinos;
-   resultados e registros de participação.

O problema não é apenas “desorganização”. É a impossibilidade de responder com segurança:

Para este treino ou competição, quem realmente está disponível, qual composição pode ser utilizada e qual ação a comissão precisa executar agora?

## Causas do problema

1.  **As informações mudam:** disponibilidade, convocação, horários e resultados não são permanentes.
2.  **Os estados são diferentes:** ativa, disponível, confirmada, convocada e participante não significam a mesma coisa.
3.  **Existem restrições esportivas:** quantidade máxima de atletas e necessidade de cobertura por função e posição.
4.  **Existem prazos:** inscrição, relação nominal, reunião, aquecimento e viagem.
5.  **Existem fontes com autoridades diferentes:** resposta da atleta, decisão humana, documento oficial e resultado validado.
6.  **Existem públicos diferentes:** atletas precisam de orientações; a comissão precisa de informações técnicas internas.

## Consequência sem a planilha

Sem consolidar essas informações, a comissão pode:

-   convocar uma atleta que não está disponível;
-   esquecer uma atleta que retornou ao elenco;
-   formar uma equipe sem cobertura funcional;
-   perder um prazo de inscrição;
-   comunicar horário ou local incorreto;
-   confundir convocação com participação efetiva;
-   atribuir jogos e resultados incorretamente;
-   tomar uma decisão sem conseguir justificar sua origem.

## Como a planilha resolve

Ela converte informações dispersas em um **estado operacional da equipe**:

| **Entrada** | **Transformação** | **Decisão permitida** |
| --- | --- | --- |
| Respostas das atletas | Disponibilidade normalizada | Quem pode treinar ou competir |
| --- | --- | --- |
| Cadastro do elenco | Funções e posições | Se a composição é viável |
| --- | --- | --- |
| Calendário | Prazos e próximos compromissos | O que precisa ser feito agora |
| --- | --- | --- |
| Convocações | Relação oficial | Quem foi selecionada |
| --- | --- | --- |
| Participação por jogo | Registro validado | Quem realmente jogou |
| --- | --- | --- |
| Resultados oficiais | Consolidação esportiva | Desempenho da equipe e das atletas |
| --- | --- | --- |
| Fontes e changelog | Rastreabilidade | Por que o dado pode ser aceito |
| --- | --- | --- |

## Formulação canônica

A planilha resolve o problema de transformar dados fragmentados, mutáveis e semanticamente diferentes em uma representação operacional única, que permita à comissão técnica formar, preparar, convocar e acompanhar a equipe com menor risco de erro.

## Limite atual

A planilha ainda resolve esse problema apenas parcialmente, porque existem divergências:

-   19 atletas na aba de julho, mas 18 no banco canônico;
-   Gilvania Balbino ainda ausente do banco;
-   painel de dia do jogo referente a uma competição passada;
-   módulo antigo de próximo treino com erros #N/A;
-   planejamento técnico ainda incompleto.

Portanto, o problema real é a **incerteza operacional**. A planilha é o mecanismo criado para reduzi-la, mas somente cumprirá integralmente essa função quando todas as interfaces estiverem sincronizadas com a fonte canônica e os painéis desatualizados forem corrigidos.

## Quem são as pessoas afetadas pelo problema real?

As pessoas diretamente afetadas são **Davi Sermenho, as atletas do CEPRAEA e os demais integrantes da comissão técnica e operacional**. Entretanto, cada grupo sofre uma consequência diferente.

## Mapa das pessoas afetadas

| **Prioridade** | **Pessoas afetadas** | **Como o problema as afeta** |
| --- | --- | --- |
| Primária | Davi Sermenho | Precisa decidir com informações incompletas ou contraditórias |
| --- | --- | --- |
| Primária | Atletas do CEPRAEA | Podem receber comunicação, convocação ou registro incorreto |
| --- | --- | --- |
| Primária | Atletas que entram, retornam ou mudam de situação | Correm maior risco de serem esquecidas ou não sincronizadas |
| --- | --- | --- |
| Secundária | Demais integrantes da comissão técnica | Planejam treinos e jogos sem uma visão comum do elenco |
| --- | --- | --- |
| Secundária | Responsáveis por inscrições e relações nominais | Podem enviar nomes errados ou perder prazos |
| --- | --- | --- |
| Secundária | Responsáveis pela operação do dia do jogo | Podem trabalhar com horários, locais e cenários desatualizados |
| --- | --- | --- |
| Indireta | Coordenação ou direção do CEPRAEA | Recebe registros esportivos que podem não representar a realidade |
| --- | --- | --- |
| Indireta | Organizadores das competições | Podem receber relações nominais ou informações incorretas |
| --- | --- | --- |

## 1. Davi Sermenho

Davi é a pessoa centralmente afetada porque aparece como responsável pelos treinos e precisa converter os dados em decisões.

O problema produz:

-   sobrecarga mental;
-   necessidade de conferir várias fontes;
-   risco de convocação incorreta;
-   dificuldade para identificar cobertura por posição;
-   risco de comunicar informações desatualizadas;
-   responsabilidade por decisões que talvez não possam ser justificadas posteriormente.

Davi é o **proprietário operacional do problema**: é quem precisa decidir mesmo quando os dados ainda não estão consolidados.

## Definição canônica

**Davi Costa Sermenho do Nascimento é um treinador de handebol especializado em preparação competitiva, liderança de equipes, análise de desempenho e organização técnico-operacional.** No CEPRAEA, ele é o treinador e o único responsável técnico e operacional, trabalhando diretamente com as atletas.

## Quem é Davi Sermenho?

### Fatos operacionais documentados

Davi atua atualmente em diferentes contextos do handebol:

- **CEPRAEA:** treinador da equipe adulta feminina de handebol de praia e responsável pelas decisões técnicas, treinamentos, convocações, análise de jogos, planejamento e operação das informações.

- **IDEC feminino:** treinador de equipes de formação do handebol de quadra.

- **IDEC masculino:** auxiliar técnico e responsável por atividades de scout, análise, preparação, comunicação e coordenação operacional em competições específicas.

- **HbTrack:** idealizador de soluções tecnológicas voltadas à gestão, análise e comunicação no handebol.

No CEPRAEA, não existe outra comissão técnica ou operacional. A estrutura humana é formada exclusivamente por **Davi e pelas atletas**.

### Trajetória de Davi Sermenho

Davi Sermenho é:

- Ex-atleta da Seleção Brasileira de handebol de praia;

- Campeão mundial;

- Seis vezes campeão brasileiro;

- Tricampeão pan-americano;

- Treinador campeão brasileiro com o CEPRAEA.

## Contexto no qual Davi está inserido

Davi está inserido no **esporte competitivo de rendimento**, especificamente no ecossistema do handebol de praia e do handebol de quadra.

Seu ambiente de atuação reúne quatro dimensões:

| Dimensão | Contexto |

|---|---|

| **Esportiva** | Treinamentos, jogos e competições estaduais, nacionais e internacionais de handebol |

| **Técnica** | Preparação física, técnica, tática e mental; análise de desempenho; scout e feedback |

| **Gerencial** | Controle de atletas, presença, disponibilidade, convocações, agenda, logística e resultados |

| **Tecnológica** | Desenvolvimento e utilização de planilhas, bancos de dados, documentação e ferramentas do ecossistema HbTrack |

No CEPRAEA, esse contexto possui uma característica determinante: **a centralização da operação em uma única pessoa**. Davi precisa transformar informações fornecidas pelas atletas, observações dos treinamentos, vídeos, scouts, resultados e calendário em decisões executáveis.

Consequentemente, ele não atua apenas como treinador durante o treino ou o jogo. Ele exerce simultaneamente os papéis de:

- Líder esportivo;

- Decisor técnico;

- Planejador da temporada;

- Analista de desempenho;

- Gestor operacional;

- Responsável pela comunicação com as atletas;

- Validador humano das informações esportivas;

- Idealizador de instrumentos tecnológicos de apoio.

## Domínio, subdomínio e tema principal

| Classificação | Definição |

|---|---|

| **Domínio** | Esporte de rendimento |

| **Subdomínio** | Treinamento, gestão técnico-operacional e análise de desempenho no handebol |

| **Tema principal** | Liderança e tomada de decisão para preparação e desempenho competitivo de equipes de handebol |

## Síntese final

> **Davi Sermenho é um treinador e gestor técnico de handebol cuja atuação integra liderança esportiva, preparação competitiva, análise de desempenho, organização operacional e desenvolvimento de instrumentos tecnológicos para apoiar decisões.**

No contexto específico do CEPRAEA, seu propósito central é **organizar, preparar e conduzir uma equipe adulta feminina de handebol de praia para competir e evoluir, transformando informações esportivas em decisões técnicas verificáveis**.

## 2. Atletas do CEPRAEA

As atletas são as pessoas mais expostas às consequências das decisões.

Uma informação incorreta pode fazer com que uma atleta:

-   não seja considerada para uma competição;
-   seja convocada quando não está disponível;
-   deixe de receber uma orientação;
-   tenha sua presença registrada incorretamente;
-   seja considerada convocada como se tivesse jogado;
-   tenha resultados atribuídos indevidamente;
-   seja classificada em função ou posição errada;
-   perca uma oportunidade de treino ou competição.

Também existe impacto sobre a percepção de justiça. Se os dados não forem confiáveis, a atleta pode não compreender por que foi convocada, não convocada ou utilizada em determinada função.

## 3. Atletas em transição de estado

As mais vulneráveis são aquelas que:

-   estão retornando;
-   ingressaram recentemente;
-   estão temporariamente afastadas;
-   mudaram de função;
-   ainda não responderam;
-   passaram de TALVEZ para SIM ou NAO.

Gilvania Balbino é o exemplo concreto: aparece na aba de julho, mas ainda não está no banco canônico. Isso pode fazer com que ela seja considerada em um controle e ignorada em outro.

## 4. Comissão técnica

Os demais integrantes da comissão são afetados porque precisam compartilhar a mesma compreensão sobre:

-   quem estará presente;
-   qual composição será utilizada;
-   quais posições precisam de cobertura;
-   quais conteúdos devem ser treinados;
-   quem efetivamente jogou;
-   quais análises são confiáveis.

Quando cada pessoa utiliza uma fonte diferente, a comissão deixa de tomar uma decisão coletiva e passa a operar com versões concorrentes da realidade.

## 5. Responsáveis administrativos e operacionais

As pessoas encarregadas de inscrições, relações nominais, documentação e logística precisam de dados corretos para executar ações com prazo.

Elas podem:

-   registrar uma atleta errada;
-   omitir uma atleta elegível;
-   enviar uma relação desatualizada;
-   perder um prazo;
-   preparar uma operação para quantidade incorreta de pessoas;
-   comunicar horários ou locais antigos.

A planilha não identifica nominalmente todas essas pessoas. Portanto, é possível confirmar as funções afetadas, mas não individualizar todos os responsáveis atuais.

## 6. Coordenação e direção

Quem responde institucionalmente pelo CEPRAEA também é afetado porque depende dos registros para:

-   comprovar participação;
-   reconstruir resultados;
-   acompanhar o elenco;
-   justificar decisões;
-   preservar a memória da equipe;
-   produzir relatórios futuros.

Um banco inconsistente compromete não apenas a operação presente, mas também o histórico institucional.

## Distinção principal

-   **Pessoa que mais sofre o problema decisório:** Davi Sermenho.
-   **Pessoas que mais sofrem as consequências:** as atletas.
-   **Pessoas que executam as decisões:** Davi Sermenho
-   **Pessoas que dependem dos registros posteriormente:** coordenação e direção qué formada pelas proprias atletas.

Portanto, o problema não afeta somente “quem preenche a planilha”. Ele afeta todas as pessoas cuja participação, trabalho ou decisão depende de uma representação correta do estado atual da equipe.

O CEPRAEA possui apenas dois tipos de integrantes:

1.  **Davi Sermenho — treinador**
2.  **Atletas do CEPRAEA**

Não existem outros integrantes na comissão técnica, coordenação ou equipe operacional.

Isso torna Davi simultaneamente responsável por:

-   planejamento dos treinos;
-   controle do elenco;
-   coleta das disponibilidades;
-   convocações;
-   inscrições e relações nominais;
-   comunicação com as atletas;
-   organização do dia do jogo;
-   registro de resultados;
-   análise esportiva;
-   manutenção das informações.

A planilha funciona, portanto, como a **memória operacional e o instrumento de coordenação de um treinador que concentra toda a operação da equipe**.

As atletas são afetadas porque fornecem informações e recebem as consequências das decisões: presença, convocação, utilização nos jogos, comunicação e registros individuais.

Também identifiquei que expressões existentes na planilha, como comissão técnica, decisão da comissão e coordenação, não representam a realidade atual. O modelo correto deve utilizar treinador ou Davi Sermenho.

## Qual é o ambiente operacional da planilha?

## Definição canônica

O ambiente operacional da planilha é:

Um ambiente digital, centralizado no Google Sheets, utilizado por um único treinador e pelas atletas para coordenar uma equipe adulta feminina de handebol de praia durante treinos, competições e atividades posteriores aos jogos.

É um ambiente de **operação esportiva com decisão humana**, alta variação temporal e dependência de informações manuais e documentos oficiais.

## Componentes do ambiente

| **Dimensão** | **Realidade operacional** |
| --- | --- |
| Organização | CEPRAEA — handebol de praia adulto feminino |
| --- | --- |
| Temporada | 2026 |
| --- | --- |
| Integrantes | Davi Sermenho e as atletas |
| --- | --- |
| Responsável central | Davi Sermenho |
| --- | --- |
| Plataforma | Google Sheets armazenado no Google Drive |
| --- | --- |
| Fuso horário | America/Sao_Paulo |
| --- | --- |
| Idioma e localidade | Português do Brasil — pt_BR |
| --- | --- |
| Locais de treino | Copacabana |
| --- | --- |
| Frequência regular | Quintas, 20h–21h30; domingos, 7h–9h |
| --- | --- |
| Locais de competição | Niterói e diferentes cidades brasileiras |
| --- | --- |
| Natureza dos dados | Operacional, esportiva, temporal e pessoal |
| --- | --- |
| Atualização | Manual, por fórmulas e por intervenções solicitadas à IA |
| --- | --- |
| Dependência externa | Tabelas, boletins e relações nominais oficiais |
| --- | --- |

## Pessoas e responsabilidades

### Davi Sermenho

Davi é o único operador central. Ele acumula as funções de:

-   treinador;
-   planejador dos treinos;
-   gestor do elenco;
-   responsável pelas convocações;
-   responsável por inscrições e relações nominais;
-   organizador da operação do dia do jogo;
-   comunicador das informações;
-   registrador dos resultados;
-   analista do desempenho;
-   mantenedor dos dados.

Isso significa que o ambiente possui um **ponto único de decisão e manutenção**. Se Davi não receber, registrar ou validar uma informação, não existe outra pessoa interna responsável por fazê-lo.

### Atletas

As atletas participam do ambiente principalmente como:

-   fontes das próprias disponibilidades;
-   destinatárias da agenda e das orientações;
-   pessoas sujeitas às convocações;
-   participantes dos treinos e jogos;
-   titulares dos registros individuais de presença e participação.

A autoridade da atleta está concentrada em declarar sua própria situação. Ela não define calendário, convocação, resultado ou composição da equipe.

## Ambiente tecnológico

A arquitetura possui duas planilhas principais:

| **Arquivo** | **Papel** |
| --- | --- |
| CEPRAEA DATABASE | Fonte canônica dos dados estruturados |
| --- | --- |
| CEPRAEA JUNHO 2026 | Interface operacional utilizada para consulta e preenchimento |
| --- | --- |

A integração utiliza:

-   fórmulas do Google Sheets;
-   validações de dados;
-   IMPORTRANGE;
-   abas de importação;
-   exportações estruturadas;
-   painéis derivados;
-   registros de alterações.

A IA atua como **ferramenta externa de manutenção**, somente quando Davi solicita uma ação. Ela não integra o CEPRAEA, não possui autoridade esportiva e não deve tomar decisões autonomamente.

## Fontes de informação

O ambiente recebe três classes de entrada:

### 1. Declarações das atletas

-   SIM;
-   NAO;
-   TALVEZ;
-   ausência de resposta;
-   falta justificada.

Essas entradas são manuais e devem ser preservadas.

### 2. Decisões de Davi

-   convocação;
-   função e posição;
-   conteúdo do treino;
-   composição da equipe;
-   decisão técnica;
-   validação de participação;
-   comunicação às atletas.

### 3. Fontes externas oficiais

-   tabelas das competições;
-   boletins;
-   relações nominais;
-   cronogramas;
-   documentos das federações;
-   resultados oficiais.

O ambiente precisa distinguir essas fontes porque uma resposta de disponibilidade, uma decisão do treinador e um documento oficial possuem autoridades diferentes.

## Ciclo operacional

| **Momento** | **Uso da planilha** |
| --- | --- |
| Planejamento da temporada | Calendário, competições e disponibilidade futura |
| --- | --- |
| Semana de treino | Confirmação de presença e composição esperada |
| --- | --- |
| Pré-competição | Inscrição, relação nominal, convocação e avaliação de cobertura |
| --- | --- |
| Dia do jogo | Horários, local, reunião, aquecimento e jogos condicionais |
| --- | --- |
| Pós-jogo | Resultado, participação real e análise |
| --- | --- |
| Entre competições | Feedback individual e definição do próximo ciclo técnico |
| --- | --- |

## Condições e restrições

O ambiente apresenta as seguintes condições:

1.  **Dependência de internet e Google Drive:** a informação operacional está hospedada no Google Sheets.
2.  **Dependência de entrada humana:** a planilha não descobre automaticamente disponibilidade, presença ou participação.
3.  **Atualização temporal:** um dado correto hoje pode estar errado no próximo treino ou competição.
4.  **Operação por uma única pessoa:** não há equipe administrativa ou comissão para revisar e dividir tarefas.
5.  **Necessidade de validação:** convocação, participação e resultado não podem ser inferidos.
6.  **Risco de sincronização:** o frontend e o banco podem apresentar estados diferentes.
7.  **Separação de públicos ainda incompleta:** informações para atletas e informações internas de Davi ainda convivem no mesmo arquivo.
8.  **Ausência de tempo real:** a planilha representa o último estado registrado e validado, não necessariamente o que está acontecendo naquele instante.

## Regras de autoridade

| **Informação** | **Autoridade** |
| --- | --- |
| Disponibilidade pessoal | A própria atleta |
| --- | --- |
| Planejamento e decisão técnica | Davi |
| --- | --- |
| Convocação | Davi |
| --- | --- |
| Calendário e tabela da competição | Documento oficial |
| --- | --- |
| Resultado da partida | Fonte oficial ou validação de Davi |
| --- | --- |
| Participação da atleta | Registro validado por Davi |
| --- | --- |
| Alteração estrutural da planilha | Autorização de Davi |
| --- | --- |

## O que esse ambiente não é

A planilha não opera em um ambiente com:

-   comissão técnica;
-   equipe administrativa;
-   operador de dados;
-   analista separado;
-   sistema autônomo de atualização;
-   aplicativo dedicado;
-   revisão humana por uma segunda pessoa.

Também não é apenas uma planilha de junho nem somente um controle de presença. Ela funciona como o **sistema operacional informal da equipe**.

## Conclusão

O ambiente operacional é **digital, centralizado, dependente de atualização humana e administrado exclusivamente por Davi**, com participação das atletas nos campos que dizem respeito à própria disponibilidade.

Essa configuração torna a planilha necessária como memória externa, mas também cria uma exigência crítica: ela precisa reduzir o trabalho de Davi, preservar as respostas das atletas e mostrar imediatamente o que exige decisão, porque não existe outra pessoa interna para conferir, reconciliar ou corrigir a operação.

## Quais são os objetivos da planilha?

Os dois arquivos canônicos foram confirmados: **“CEPRAEA JUNHO 2026”** é a interface operacional, e **“CEPRAEA DATABASE”** é a fonte estruturada. Agora vou verificar quais resultados cada módulo foi construído para produzir, sem confundir objetivo com recurso ou aba.

## Escopo validado

Entre os vários arquivos encontrados, a própria configuração identifica duas planilhas canônicas:

-   [CEPRAEA JUNHO 2026](https://docs.google.com/spreadsheets/d/14d3vIfkvhkTvjjTxkM7CxA9Oo1etHAgC2KUzGzzEn88/edit): interface operacional.
-   [CEPRAEA DATABASE](https://docs.google.com/spreadsheets/d/10Dv1oBIKdodWEWsK8qUeLPyazzdg4hdRkVi4gjvVSno/edit): fonte estruturada ou SSOT OPERACIONAL.

Cópias, modelagens e planilhas de teste não foram tratadas como fontes canônicas.

## Objetivo geral

Permitir que Davi planeje, execute, comunique e registre a operação esportiva do CEPRAEA utilizando informações atuais, verificáveis e preservadas sobre atletas, treinos e competições.

Em termos práticos, as planilhas devem responder:

Qual é o estado atual da equipe, qual decisão Davi precisa tomar e qual ação deve ser executada agora?

## Objetivos específicos

| **Objetivo** | **Resultado esperado** | **Evidência na estrutura** | **Estado atual** |
| --- | --- | --- | --- |
| 1. Representar o elenco atual | Saber quem integra a equipe, sua função, posição e status | DB_ATLETAS, DB_FUNCOES, DB_POSICOES | Parcial |
| --- | --- | --- | --- |
| 2. Coletar disponibilidade | Registrar SIM, NAO, TALVEZ ou ausência de resposta | AGENDA CEPRAEA, abas mensais e DB_PRESENCA | Parcial |
| --- | --- | --- | --- |
| 3. Avaliar viabilidade esportiva | Identificar se existem atletas suficientes por função e posição | DB_DISPONIBILIDADE_POSICAO e indicadores táticos | Implementado, dependente dos dados |
| --- | --- | --- | --- |
| 4. Controlar calendário e prazos | Mostrar treinos, competições, inscrições e relações nominais | DB_CALENDARIO, DB_TREINOS, AGENDA CEPRAEA | Parcial |
| --- | --- | --- | --- |
| 5. Apoiar convocações | Relacionar competição, limites e atletas selecionadas | DB_CONVOCACOES e DB_CONVOCACAO_ATLETAS | Estruturado |
| --- | --- | --- | --- |
| 6. Organizar o dia do jogo | Informar local, reunião, aquecimento, partidas e cenários | 🏖️ DIA DO JOGO | Criado, mas desatualizado |
| --- | --- | --- | --- |
| 7. Distinguir convocação de participação | Registrar quem foi convocada e quem realmente jogou | DB_PARTICIPACAO_JOGO | Estruturado |
| --- | --- | --- | --- |
| 8. Preservar resultados e histórico | Consolidar jogos, vitórias, derrotas, sets e participação | DB_JOGOS, ANÁLISE JOGOS | Operacional com pendências |
| --- | --- | --- | --- |
| 9. Apoiar o planejamento técnico | Converter disponibilidade e posições em foco de treino | AGENDA TÉCNICA V2 | Incompleto |
| --- | --- | --- | --- |
| 10. Comunicar informações às atletas | Oferecer agenda e orientações compreensíveis | Abas mensais e painéis visíveis | Parcial |
| --- | --- | --- | --- |
| 11. Organizar feedback individual | Reservar conversas individuais com apresentação de vídeos | 📅 FEEDBACK INDIVIDUAL | Não operacional |
| --- | --- | --- | --- |
| 12. Garantir rastreabilidade | Registrar fonte, alteração, executor, validação e pendência | DB_CHANGELOG, 📑_CHANGELOG, auditorias | Implementado |
| --- | --- | --- | --- |

## Objetivo 1 — reduzir a incerteza operacional de Davi

Este é o objetivo central.

Como Davi é o único treinador e também executa toda a operação, a planilha deve reduzir a necessidade de:

-   memorizar respostas;
-   conferir várias mensagens;
-   reconstruir o elenco;
-   calcular manualmente a cobertura por posição;
-   procurar datas e prazos;
-   reconciliar convocação, participação e resultado.

A planilha deve apresentar o estado já consolidado para que Davi concentre seu esforço na decisão esportiva.

## Objetivo 2 — preservar as declarações das atletas

As respostas das atletas constituem dados humanos autorizados. Por isso, a configuração determina:

-   política PRESERVAR;
-   proibição de sobrescrever respostas sem autorização;
-   execução determinística;
-   proibição de inferir presença.

O objetivo não é “adivinhar” quem comparecerá. É conservar exatamente o que cada atleta declarou.

Também é necessário distinguir:

-   disponibilidade futura;
-   confirmação esperada para um treino;
-   convocação;
-   participação efetiva.

## Objetivo 3 — verificar se a equipe pode funcionar

Contar atletas não é suficiente. A planilha deve avaliar se determinada data possui cobertura para:

-   goleiras;
-   defesa;
-   ataque;
-   posições específicas;
-   sistema defensivo 3:0;
-   sistema defensivo 2:1;
-   sistema ofensivo 3:1;
-   sistema ofensivo 2:1.

O resultado esperado é alertar Davi sobre uma lacuna antes que ela comprometa o treino ou a competição.

## Objetivo 4 — transformar calendário em ação

Datas não devem permanecer como simples informação. A planilha deve convertê-las em ações:

-   solicitar disponibilidade;
-   confirmar presença;
-   realizar inscrição;
-   enviar relação nominal;
-   convocar atletas;
-   informar reunião;
-   iniciar aquecimento;
-   acompanhar jogos condicionais;
-   registrar o resultado posteriormente.

Portanto, o objetivo é mostrar não apenas **quando algo ocorrerá**, mas **o que Davi precisa fazer antes do prazo**.

## Objetivo 5 — preservar a verdade esportiva

As planilhas procuram impedir equivalências incorretas:

-   disponível não significa convocada;
-   convocada não significa que jogou;
-   estar relacionada não significa participar de todas as partidas;
-   jogo previsto não significa jogo realizado;
-   placar informado não significa placar validado.

As abas de participação e auditoria existem para que estatísticas individuais sejam produzidas somente quando a participação real estiver vinculada a uma partida e a um resultado validado.

## Objetivo 6 — produzir memória histórica

O sistema deve permitir reconstruir:

-   quais competições foram disputadas;
-   quais jogos ocorreram;
-   quais foram os resultados;
-   quais atletas participaram;
-   qual era a composição do elenco;
-   quais fontes sustentam os registros;
-   quando e por quem o dado foi alterado.

Esse objetivo permite que o histórico não dependa exclusivamente da memória de Davi.

## Objetivo 7 — comunicar às atletas sem expor dados internos

A interface deve mostrar às atletas apenas o necessário para agir:

-   datas;
-   horários;
-   local;
-   confirmação;
-   convocação;
-   cronograma do dia;
-   orientação do treinador.

Dados como criticidade, lacunas táticas e critérios internos pertencem a Davi. A separação entre conteúdo visível às atletas e conteúdo técnico ainda aparece como pendência no DB_CONFIG.

## Objetivos que ainda não foram plenamente atingidos

A estrutura demonstra os objetivos, mas a implementação ainda possui falhas:

-   19 atletas em JULHO - 2026, contra 18 no banco;
-   Gilvania Balbino ainda não está no DB_ATLETAS;
-   o painel de dia do jogo permanece em uma competição passada;
-   o planejamento técnico contém diversos campos “Preencher”;
-   o módulo de feedback continua em configuração;
-   a correção definitiva do controle de presença permanece pendente;
-   expressões como comissão técnica e coordenação não correspondem à realidade atual.

## Conclusão

As planilhas não têm como objetivo principal apenas controlar presença ou armazenar nomes.

O objetivo canônico do conjunto é:

Ser o sistema de apoio operacional de Davi para manter uma representação confiável do CEPRAEA, transformar respostas e documentos em decisões executáveis, comunicar as atletas e preservar o histórico verificável da equipe.

Esse objetivo está corretamente representado na arquitetura, mas ainda é atendido apenas parcialmente devido às divergências de sincronização, aos módulos desatualizados e às funções ainda incompletas. Nenhum dado foi alterado durante a análise.

## Quais são os resultados esperados da planilha?

## Resultado esperado principal

O resultado esperado não é simplesmente “ter dados registrados”.

A planilha deve permitir que Davi saiba, sem reconstrução manual, qual é o estado atual do CEPRAEA, qual decisão precisa tomar e o que deve comunicar às atletas.

## Resultados verificáveis

| **ID** | **Resultado esperado** | **Critério de aceitação** |
| --- | --- | --- |
| R-01 | Elenco canônico e atualizado | Banco e interface apresentam as mesmas atletas, funções, posições e status |
| --- | --- | --- |
| R-02 | Disponibilidade preservada | Cada atleta/data possui SIM, NAO, TALVEZ ou pendência, sem inferência da IA |
| --- | --- | --- |
| R-03 | Pendências identificadas | Davi visualiza imediatamente quem ainda não respondeu |
| --- | --- | --- |
| R-04 | Viabilidade funcional calculada | A planilha informa se há goleiras, defesa e ataque suficientes |
| --- | --- | --- |
| R-05 | Próxima ação claramente apresentada | Existe apenas um próximo treino ou evento vigente, com data, horário, local e ação |
| --- | --- | --- |
| R-06 | Convocação válida | A convocação respeita limites, disponibilidade e composição funcional |
| --- | --- | --- |
| R-07 | Comunicação correta às atletas | Cada atleta visualiza somente informações atuais e necessárias para agir |
| --- | --- | --- |
| R-08 | Participação real registrada | Convocada, não convocada, jogou e não jogou permanecem estados distintos |
| --- | --- | --- |
| R-09 | Resultados esportivos verificáveis | Cada placar e participação possui jogo, competição, fonte e validação |
| --- | --- | --- |
| R-10 | Planejamento técnico executável | Próximo treino possui objetivo, atividade, metas e orientação |
| --- | --- | --- |
| R-11 | Histórico reconstruível | É possível saber o que mudou, quando, por quem e com qual fonte |
| --- | --- | --- |
| R-12 | Redução da sobrecarga de Davi | As decisões não exigem conferência manual entre mensagens e diferentes arquivos |
| --- | --- | --- |

## 1. Um único estado do elenco

O resultado esperado é que exista uma única resposta para:

-   quem integra o CEPRAEA;
-   quem está ativa;
-   qual é sua função;
-   qual é sua posição;
-   qual é seu número;
-   quando o registro foi alterado;
-   qual fonte autorizou a informação.

Não deve existir uma atleta apenas na aba mensal ou apenas no banco.

**Situação atual:** resultado não atingido, porque julho apresenta 19 atletas, enquanto o banco registra 18 e ainda não contém Gilvania Balbino.

## 2. Mapa confiável de disponibilidade

Para cada treino e competição, Davi deve visualizar:

-   confirmadas;
-   indisponíveis;
-   respostas condicionais;
-   pendentes;
-   quantidade por função e posição.

As respostas precisam continuar sendo declarações das atletas. A planilha não deve transformar uma célula vazia em ausência nem um TALVEZ em confirmação.

## 3. Alertas operacionais

A planilha deve converter dados em alertas, por exemplo:

-   atleta ainda não respondeu;
-   número insuficiente de goleiras;
-   posição tática sem cobertura;
-   prazo de inscrição próximo;
-   relação nominal pendente;
-   convocação acima do limite;
-   informação oficial ainda não validada;
-   painel referente a evento passado.

O resultado esperado não é apenas mostrar números, mas destacar o que exige ação de Davi.

## 4. Composição esportiva viável

Antes de cada treino ou competição, Davi deve conseguir determinar:

-   quantas atletas estão disponíveis;
-   quais funções estarão presentes;
-   quais sistemas podem ser treinados;
-   quais posições estão descobertas;
-   se será necessário adaptar o conteúdo;
-   se a convocação forma uma equipe funcional.

O resultado esperado é evitar uma equipe numericamente suficiente, mas taticamente incompleta.

## 5. Calendário transformado em próxima ação

A planilha deve apresentar o compromisso vigente:

-   data;
-   horário;
-   local;
-   status;
-   prazo relacionado;
-   ação necessária;
-   responsável — Davi ou a própria atleta.

Eventos passados devem ser arquivados ou claramente marcados como concluídos.

**Situação atual:** resultado parcial, pois o painel 🏖️ DIA DO JOGO ainda apresenta a etapa de 5 de julho como confirmada.

## 6. Convocação correta e justificável

O resultado esperado é uma convocação que:

-   considere as respostas das atletas;
-   respeite o limite de convocadas;
-   respeite o limite por partida;
-   possua cobertura por função;
-   identifique a competição;
-   registre a fonte;
-   preserve a decisão de Davi.

A planilha apoia a decisão, mas não deve convocar autonomamente.

## 7. Atletas corretamente orientadas

Cada atleta deve conseguir identificar:

-   quando ocorrerá o próximo treino ou jogo;
-   onde precisa estar;
-   em qual horário;
-   o que precisa responder;
-   se foi convocada;
-   quais são as orientações de Davi;
-   se alguma informação mudou.

A atleta não deve precisar interpretar áreas técnicas, fórmulas ou dados internos de Davi.

## 8. Separação entre planejamento e realidade

A planilha deve preservar as seguintes diferenças:

| **Estado planejado** | **Estado realizado** |
| --- | --- |
| Disponível | Compareceu |
| --- | --- |
| Confirmada | Participou |
| --- | --- |
| Convocada | Jogou |
| --- | --- |
| Jogo previsto | Jogo realizado |
| --- | --- |
| Escalação possível | Composição utilizada |
| --- | --- |
| Placar informado | Placar validado |
| --- | --- |

Esse resultado é indispensável para impedir estatísticas incorretas.

## 9. Histórico esportivo confiável

Após cada competição, o sistema deve produzir:

-   jogos disputados;
-   adversários;
-   placares;
-   sets;
-   shoot-outs;
-   vitórias e derrotas;
-   atletas que jogaram;
-   participação individual;
-   fonte dos registros;
-   status de auditoria.

Assim, Davi poderá analisar o desempenho sem reconstruir o campeonato posteriormente.

## 10. Planejamento técnico completo

O resultado esperado para cada ciclo é possuir:

-   competição-alvo;
-   problema técnico identificado;
-   objetivo do treino;
-   exercício principal;
-   metas coletivas;
-   critério de observação;
-   orientação às atletas.

**Situação atual:** esse resultado ainda não foi atingido, porque a AGENDA TÉCNICA V2 contém campos como “Preencher foco do ciclo”, “Preencher exercício-chave” e “Preencher decisão”.

## 11. Rastreabilidade

Toda alteração relevante deve responder:

-   o que mudou;
-   qual dado anterior foi substituído;
-   quando ocorreu;
-   quem autorizou;
-   qual fonte sustentou a mudança;
-   qual validação foi executada;
-   qual pendência permaneceu.

Esse resultado protege Davi contra a perda da memória operacional.

## 12. Redução real de trabalho

O resultado humano esperado é que Davi deixe de gastar tempo:

-   procurando respostas;
-   recontando atletas;
-   conciliando listas;
-   refazendo cálculos;
-   verificando várias versões;
-   reconstruindo resultados;
-   corrigindo comunicações.

A planilha deve concentrar esse trabalho e apresentar somente as decisões e pendências relevantes.

## Impacto esperado

A sequência esperada é:

**dados confiáveis → estado consolidado → decisão no prazo → comunicação correta → treino e competição mais bem preparados.**

A planilha pode melhorar as condições para o desempenho esportivo, mas **não pode garantir vitórias, títulos ou evolução técnica**. Esses são impactos posteriores, influenciados pelo treinamento, pelas atletas, pelos adversários e pela competição.

## Conclusão

Os resultados esperados são:

1.  informação consistente;
2.  disponibilidade conhecida;
3.  composição funcional verificável;
4.  prazos controlados;
5.  convocações corretas;
6.  atletas bem orientadas;
7.  participação e resultados validados;
8.  planejamento técnico executável;
9.  histórico auditável;
10.  menor sobrecarga operacional para Davi.

Atualmente, esses resultados são atendidos parcialmente. As divergências de elenco, os painéis desatualizados e os módulos incompletos ainda impedem que a planilha cumpra integralmente sua finalidade.

## Quais são os conceitos do domínio do CEPRAEA ?

A estrutura confirma que o domínio não é apenas “controle de presença”. Ele abrange identidade do elenco, disponibilidade, cobertura tática, treinos, competições, convocações, participação real, resultados e governança. Vou validar agora as definições e os estados usados em cada entidade.

## Domínio identificado

Após reler as planilhas [CEPRAEA JUNHO 2026](https://docs.google.com/spreadsheets/d/14d3vIfkvhkTvjjTxkM7CxA9Oo1etHAgC2KUzGzzEn88/edit) e [CEPRAEA DATABASE](https://docs.google.com/spreadsheets/d/10Dv1oBIKdodWEWsK8qUeLPyazzdg4hdRkVi4gjvVSno/edit), o domínio pode ser definido como:

**Gestão operacional, técnico-tática e histórica de uma equipe adulta feminina de handebol de praia.**

O núcleo do domínio é permitir que Davi coordene o CEPRAEA com base na situação das atletas, na cobertura tática, no calendário e em registros esportivos verificáveis.

## Subdomínios

1.  Gestão do elenco.
2.  Disponibilidade e presença.
3.  Planejamento de treinos.
4.  Composição e cobertura tática.
5.  Calendário e competições.
6.  Convocações.
7.  Operação do dia do jogo.
8.  Participação efetiva.
9.  Resultados e indicadores.
10.  Comunicação e feedback.
11.  Proveniência, validação e auditoria.

## Mapa conceitual

flowchart TD

EQ["Equipe CEPRAEA"] --> AT["Atleta"]

EQ --> TD["Treinador Davi"]

AT --> RD["Resposta de disponibilidade"]

TD --> EV["Treino ou competição"]

RD --> CT["Cobertura tática e risco"]

CT --> CV["Convocação"]

CV --> JO["Jogo"]

AT --> PA["Participação real"]

JO --> PA

PA --> RI["Resultado e indicadores"]

## 1. Pessoas e estrutura esportiva

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Equipe CEPRAEA** | Unidade esportiva formada exclusivamente pelo treinador Davi e pelas atletas. |
| --- | --- |
| **Treinador** | Davi Sermenho, única autoridade interna para planejamento, convocação, definição tática, validação e comunicação. |
| --- | --- |
| **Atleta** | Pessoa integrante ou candidata ao elenco, identificada individualmente e associada a função, posição e estado. |
| --- | --- |
| **Elenco** | Conjunto de atletas consideradas ativas em determinado momento da temporada. |
| --- | --- |
| **Temporada** | Limite temporal no qual calendário, elenco, competições e resultados são organizados. A planilha atual utiliza 2026. |
| --- | --- |
| **Status da atleta** | Indica se a atleta está integrada ao elenco. Não deve ser confundido com disponibilidade para uma data específica. |
| --- | --- |
| **Número da camisa** | Identificador esportivo utilizado nas relações nominais e jogos, sustentado por uma fonte. |
| --- | --- |

Não são conceitos válidos para a realidade atual:

-   comissão técnica;
-   coordenação;
-   equipe operacional.

Essas expressões devem ser substituídas por treinador ou Davi Sermenho.

## 2. Funções e posições

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Função principal** | Classificação esportiva ampla da atleta: GOLEIRA, DEFESA, ATAQUE, CORINGA ou INDEFINIDA. |
| --- | --- |
| **Posição principal** | Posição em que a atleta é prioritariamente utilizada. |
| --- | --- |
| **Posição secundária** | Posição alternativa autorizada por decisão de Davi. |
| --- | --- |
| **Posição ofensiva** | Papel desempenhado no ataque, como central, lateral ou pivô. |
| --- | --- |
| **Posição defensiva** | Papel desempenhado na defesa, como base, solta, cobertura ou avançada. |
| --- | --- |
| **Posição no jogo** | Posição efetivamente exercida em uma partida específica, que pode diferir da posição principal. |
| --- | --- |
| **Flexibilidade posicional** | Capacidade validada de uma atleta ocupar mais de uma posição. |
| --- | --- |

A planilha atualmente reconhece posições como:

-   goleira;
-   central;
-   central direita;
-   lateral esquerda;
-   lateral direita;
-   pivô;
-   defensora solta;
-   defensora base;
-   defensora cobertura;
-   defensora avançada.

## 3. Sistema e cobertura tática

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Sistema tático** | Organização coletiva que determina quais posições precisam estar ocupadas. |
| --- | --- |
| **Sistema defensivo** | Estrutura de defesa, atualmente representada pelos sistemas 3:0 e 2:1. |
| --- | --- |
| **Sistema ofensivo** | Estrutura de ataque, atualmente representada pelos sistemas 3:1 e 2:1. |
| --- | --- |
| **Slot tático** | Lugar funcional que precisa ser preenchido dentro de determinado sistema. |
| --- | --- |
| **Quantidade requerida** | Número mínimo de atletas necessárias para ocupar um slot. |
| --- | --- |
| **Cobertura tática** | Comparação entre posições requeridas e atletas disponíveis. |
| --- | --- |
| **Coberto** | Existem atletas disponíveis em quantidade suficiente. |
| --- | --- |
| **Insuficiente** | Não existem atletas suficientes para preencher o slot. |
| --- | --- |
| **Risco funcional** | Risco de o treino ou a competição não possuir composição adequada por função ou posição. |
| --- | --- |
| **Criticidade** | Impacto operacional da ausência de determinada função ou atleta. Não deve representar julgamento sobre o valor pessoal da atleta. |
| --- | --- |

## 4. Disponibilidade, confirmação e presença

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Resposta de disponibilidade** | Declaração da atleta sobre a possibilidade de comparecer a um treino ou competição. |
| --- | --- |
| **Resposta bruta** | Valor exatamente informado pela atleta. |
| --- | --- |
| **Resposta normalizada** | Representação padronizada da resposta para cálculo e consulta. |
| --- | --- |
| **Confirmada** | A atleta declarou SIM. |
| --- | --- |
| **Indisponível** | A atleta declarou NÃO. |
| --- | --- |
| **Talvez** | A atleta ainda não consegue confirmar nem negar. |
| --- | --- |
| **Sem resposta** | Nenhuma declaração foi registrada. |
| --- | --- |
| **Falta justificada** | Ausência acompanhada de justificativa. |
| --- | --- |
| **Comparecimento real** | Evidência de que a atleta efetivamente esteve no treino. Esse conceito ainda não está separado adequadamente no banco. |
| --- | --- |

A distinção crítica é:

SIM representa uma declaração anterior ao evento; não comprova comparecimento efetivo.

A aba DB_PRESENCA mistura semanticamente **resposta de disponibilidade** com **presença real**. O modelo deveria separar esses dois conceitos.

## 5. Treino e planejamento

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Treino** | Sessão esportiva identificada por data, horário, local e estado de planejamento. |
| --- | --- |
| **Ciclo de treino** | Conjunto de sessões orientadas para uma competição ou necessidade técnica. |
| --- | --- |
| **Competição-alvo** | Competição que orienta o conteúdo do ciclo. |
| --- | --- |
| **Objetivo do treino** | Resultado técnico ou tático que Davi pretende alcançar na sessão. |
| --- | --- |
| **Atividade principal** | Exercício central utilizado para atingir o objetivo. |
| --- | --- |
| **Metas coletivas** | Resultados observáveis esperados da equipe durante o treino. |
| --- | --- |
| **Critério de análise** | Evidência que Davi observará para avaliar o treino. |
| --- | --- |
| **Orientação às atletas** | Instrução que deve ser comunicada antes ou durante a sessão. |
| --- | --- |
| **Status de planejamento** | Estado do treino, como planejado, realizado, cancelado ou pendente. |
| --- | --- |

## 6. Calendário e obrigações

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Compromisso de calendário** | Treino, competição, reunião, feedback ou outra atividade vinculada a data e horário. |
| --- | --- |
| **Prazo de inscrição** | Data-limite para registrar a equipe na competição. |
| --- | --- |
| **Prazo da relação nominal** | Data-limite para informar oficialmente as atletas. |
| --- | --- |
| **Próximo compromisso** | Primeiro compromisso futuro ainda aplicável. |
| --- | --- |
| **Próxima ação** | Ação que Davi ou uma atleta precisa executar para manter a operação regular. |
| --- | --- |
| **Estado temporal** | Classifica um compromisso como futuro, vigente, realizado, cancelado ou vencido. |
| --- | --- |

Esse último conceito precisa ser fortalecido. O painel DIA DO JOGO continua exibindo como confirmada uma etapa de 5 de julho, embora a leitura tenha ocorrido em 23 de julho.

## 7. Competição e jogo

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Competição** | Evento esportivo organizado por entidade oficial, delimitado por temporada, tipo, cidade e datas. |
| --- | --- |
| **Etapa** | Ocorrência específica dentro de um circuito ou competição. |
| --- | --- |
| **Organização** | Entidade responsável pela competição, como CBHb ou FHERJ. |
| --- | --- |
| **Jogo** | Partida individual pertencente a uma competição. |
| --- | --- |
| **Fase** | Momento competitivo do jogo, como preliminar, semifinal ou final. |
| --- | --- |
| **Grupo** | Agrupamento de equipes na etapa classificatória. |
| --- | --- |
| **Adversário** | Equipe enfrentada pelo CEPRAEA. |
| --- | --- |
| **Lado do CEPRAEA** | Indica se o CEPRAEA aparece como equipe A ou B no registro oficial. |
| --- | --- |
| **Jogo garantido** | Partida cuja realização já está determinada. |
| --- | --- |
| **Jogo condicional** | Partida cuja realização depende da classificação ou de resultado anterior. |
| --- | --- |
| **Operação do dia do jogo** | Reunião, aquecimento, recuperação, partidas, local e próximos cenários. |
| --- | --- |

## 8. Convocação e escalação

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Convocação** | Decisão de Davi que seleciona atletas para uma competição ou etapa. |
| --- | --- |
| **Atleta convocada** | Atleta incluída formalmente na convocação. |
| --- | --- |
| **Relação nominal** | Documento oficial que relaciona as atletas inscritas ou convocadas. |
| --- | --- |
| **Limite da convocação** | Quantidade máxima de atletas permitida na etapa; atualmente registrada como 12. |
| --- | --- |
| **Escalação por partida** | Subconjunto das convocadas autorizado ou escolhido para um jogo específico. |
| --- | --- |
| **Limite por partida** | Quantidade máxima de atletas que podem participar da partida; atualmente registrada como 10. |
| --- | --- |
| **Titular** | Atleta definida para iniciar o jogo, quando esse dado estiver efetivamente registrado. |
| --- | --- |
| **Função no evento** | Função atribuída à atleta naquela competição. |
| --- | --- |

Regra indispensável:

Ser convocada para a etapa não significa ter jogado todas as partidas.

## 9. Participação real

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Participação no jogo** | Relação factual entre uma atleta e uma partida realizada. |
| --- | --- |
| **Jogou** | Existe validação de que a atleta entrou em quadra. |
| --- | --- |
| **Não jogou** | A atleta estava relacionada ou convocada, mas não participou da partida. |
| --- | --- |
| **Entrou em quadra** | Evidência operacional da participação efetiva. |
| --- | --- |
| **Função no jogo** | Função realmente desempenhada naquela partida. |
| --- | --- |
| **Posição no jogo** | Posição realmente ocupada naquela partida. |
| --- | --- |
| **Períodos ou minutos** | Medida de participação, quando disponível. |
| --- | --- |
| **Regra de contagem** | Critério que determina quando uma partida é contabilizada para a atleta. |
| --- | --- |

## 10. Resultado e desempenho

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Resultado do jogo** | Desfecho validado de uma partida realizada. |
| --- | --- |
| **Set** | Unidade parcial de resultado no handebol de praia. |
| --- | --- |
| **Shoot-out** | Desempate utilizado quando cada equipe vence um set. |
| --- | --- |
| **Vitória** | Resultado no qual o CEPRAEA vence a partida. |
| --- | --- |
| **Derrota** | Resultado no qual o CEPRAEA perde a partida. |
| --- | --- |
| **Indicador da equipe** | Métrica agregada, como jogos, vitórias, derrotas, sets e aproveitamento. |
| --- | --- |
| **Indicador da atleta** | Métrica individual derivada de convocações, jogos e registros de treino. |
| --- | --- |
| **Aproveitamento** | Proporção calculada a partir de resultados validados. |
| --- | --- |
| **Pendência analítica** | Dado necessário para completar ou validar determinada análise. |
| --- | --- |

Os indicadores não devem ser tratados como fatos primários. Eles são **dados derivados** de jogos, participações e respostas previamente validados.

## 11. Comunicação e feedback

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Aviso** | Comunicação com título, mensagem, público, validade e fonte. |
| --- | --- |
| **Público** | Destinatário da informação: Davi ou atletas. |
| --- | --- |
| **Orientação operacional** | Informação necessária para a atleta agir corretamente. |
| --- | --- |
| **Feedback individual** | Conversa individual conduzida por Davi, potencialmente apoiada por vídeos. |
| --- | --- |
| **Horário de feedback** | Intervalo reservado a uma única atleta. |
| --- | --- |
| **Status do horário** | Livre, reservado, concluído ou cancelado. |
| --- | --- |

A expressão “link informado pela coordenação” está incorreta. O conceito correto é “link informado pelo treinador Davi”.

## 12. Proveniência e governança

| **Conceito** | **Definição canônica** |
| --- | --- |
| **Fonte** | Origem do dado, como boletim, tabela, relação nominal ou decisão humana. |
| --- | --- |
| **Fonte autorizada** | Fonte aceita para sustentar determinado campo. |
| --- | --- |
| **Decisão humana** | Decisão expressa de Davi que autoriza uma classificação ou atualização. |
| --- | --- |
| **Validação** | Verificação do dado contra uma fonte autorizada. |
| --- | --- |
| **Auditoria** | Cruzamento entre entidades para detectar incoerências. |
| --- | --- |
| **Status de auditoria** | Resultado da verificação, como OK ou pendente. |
| --- | --- |
| **Rastreabilidade** | Capacidade de identificar origem, alteração e estado do dado. |
| --- | --- |
| **Changelog** | Registro das mudanças realizadas no sistema. |
| --- | --- |
| **Política de preservação** | Proibição de sobrescrever respostas humanas sem autorização. |
| --- | --- |
| **Execução determinística** | Regra que impede a IA de inventar ou inferir presença e participação. |
| --- | --- |

## Relações essenciais do domínio

1.  Uma **equipe** possui um treinador e várias atletas.
2.  Uma **atleta** possui uma função principal e uma ou mais posições autorizadas.
3.  Um **sistema tático** exige determinados slots e posições.
4.  Uma atleta fornece uma **resposta de disponibilidade** para um compromisso.
5.  A disponibilidade das atletas determina a **cobertura tática**.
6.  Davi utiliza disponibilidade e cobertura para planejar o treino ou realizar uma convocação.
7.  Uma **competição** contém jogos.
8.  Uma **convocação** pertence a uma competição ou etapa.
9.  Uma convocação contém atletas, mas a **participação real** pertence a cada jogo.
10.  Um jogo realizado produz um resultado.
11.  Resultado e participação validados produzem indicadores.
12.  Todo dado relevante deve possuir fonte, estado e histórico de alteração.

## Conceitos técnicos que não pertencem ao domínio esportivo

Os seguintes elementos pertencem à implementação:

-   Google Sheets;
-   Google Drive;
-   aba;
-   célula;
-   fórmula;
-   IMPORTRANGE;
-   DB_EXPORT_FRONTEND;
-   _IMPORT_DATABASE;
-   frontend;
-   database;
-   sheetId;
-   intervalo A1.

Eles implementam o sistema, mas não descrevem a realidade esportiva do CEPRAEA.

## Inconsistências conceituais encontradas

1.  Presença mistura declaração antecipada e comparecimento real.
2.  DB_STATUS não apresenta TALVEZ, embora esse estado seja usado e contabilizado.
3.  Comissão técnica e coordenação não existem na realidade do CEPRAEA.
4.  Decisão da comissão deve ser decisão do treinador.
5.  Criticidade precisa ser definida como risco funcional, não como avaliação pessoal.
6.  O estado temporal dos painéis não impede que um evento passado continue apresentado como vigente.
7.  Convocação e escalação por partida ainda precisam permanecer explicitamente separadas.
8.  O elenco ativo ainda diverge entre a interface e o banco.

## Conclusão

O conceito central do domínio é o **estado operacional da equipe**: a representação atual e verificável de quem integra o elenco, quem está disponível, quais sistemas podem ser executados, qual compromisso está vigente e quais fatos esportivos já foram validados.

Os demais conceitos existem para produzir ou comprovar esse estado. Nenhum dado foi alterado durante a análise.

## Qual é o problema que deve ser resolvido, para quem, em qual contexto e com qual resultado?

O problema não é “falta de uma planilha”, mas ausência de um estado operacional único e confiável.

## Declaração canônica do problema

**Davi Sermenho, único treinador e operador do CEPRAEA, precisa coordenar uma equipe adulta feminina de handebol de praia cujo elenco, disponibilidade, composição tática, calendário, convocações e resultados mudam continuamente. Atualmente, essas informações não formam um estado operacional único, atual e semanticamente consistente. O sistema deve consolidá-las e validá-las para que Davi tome decisões no prazo correto e as atletas recebam orientações confiáveis.**

## Síntese

| **Pergunta** | **Resposta** |
| --- | --- |
| **Qual problema deve ser resolvido?** | A ausência de uma representação única, atualizada e confiável do estado operacional do CEPRAEA. |
| --- | --- |
| **Para quem?** | Principalmente para Davi; secundariamente para as atletas afetadas pelas informações e decisões. |
| --- | --- |
| **Em qual contexto?** | Equipe adulta feminina de handebol de praia, administrada exclusivamente por Davi, com treinos recorrentes, competições, prazos, convocações e requisitos táticos. |
| --- | --- |
| **Com qual resultado?** | Davi deve conseguir identificar o estado atual da equipe, decidir e comunicar corretamente sem reconciliar manualmente dados divergentes. |
| --- | --- |

# 1. Qual problema deve ser resolvido?

O problema real é:

**Incerteza operacional causada por dados fragmentados, divergentes, temporalmente desatualizados e semanticamente ambíguos.**

Isso significa que Davi ainda não consegue confiar que uma única consulta representa corretamente:

-   quem integra o elenco;
-   quem está disponível;
-   quem confirmou um treino;
-   quem realmente compareceu;
-   quais posições estarão cobertas;
-   qual é o próximo compromisso;
-   quem foi convocada;
-   quem efetivamente jogou;
-   quais resultados já foram validados;
-   qual informação deve ser comunicada às atletas.

A planilha existe, mas o problema ainda permanece parcialmente porque a informação não está integralmente sincronizada.

## Evidências encontradas

### Divergência de elenco

-   JULHO - 2026 apresenta 19 atletas;
-   DB_ATLETAS apresenta 18 atletas;
-   Gilvania Balbino está na aba mensal, mas não está no banco canônico.

Consequência: Davi pode obter respostas diferentes dependendo da aba consultada.

### Informação temporalmente desatualizada

A aba 🏖️ DIA DO JOGO ainda apresenta como confirmada a 3ª Etapa Carioca de 05/07/2026, embora tenha sido atualizada em 23/07/2026.

Consequência: uma atualização técnica do painel não garante que o conteúdo esportivo exibido ainda seja vigente.

### Ambiguidade entre disponibilidade e presença

O banco utiliza DB_PRESENCA, mas os dados representam principalmente respostas antecipadas:

-   SIM;
-   NAO;
-   TALVEZ;
-   SEM_RESPOSTA.

Isso não comprova comparecimento real ao treino.

Consequência: uma declaração anterior pode ser tratada incorretamente como presença efetiva.

### Dependência de dados incompletos

O banco registra:

-   306 respostas esperadas;
-   121 SIM;
-   48 NAO;
-   9 TALVEZ;
-   128 SEM_RESPOSTA.

Consequência: cálculos de disponibilidade e cobertura precisam deixar claro quando estão baseados em respostas incompletas.

### Risco de interpretação entre convocação e participação

O próprio banco registra que:

-   convocação para a etapa não significa participação em todas as partidas;
-   somente status_participacao = JOGOU deve contar como jogo real.

Consequência: se essa distinção não for preservada, o histórico individual fica incorreto.

# 2. Para quem o problema deve ser resolvido?

## Usuário principal: Davi Sermenho

Davi é simultaneamente:

-   treinador;
-   planejador dos treinos;
-   responsável pelo elenco;
-   responsável pelas convocações;
-   responsável pelos prazos;
-   responsável pela comunicação;
-   responsável pelos registros;
-   responsável pelas análises;
-   único validador interno.

Portanto, Davi é o **proprietário do problema** e o principal usuário da solução.

O sistema precisa reduzir:

-   esforço de conferência;
-   recontagem manual;
-   busca entre abas;
-   reconciliação de versões;
-   risco de convocação errada;
-   risco de comunicação desatualizada;
-   risco de histórico incorreto.

## Usuárias afetadas: atletas

As atletas são afetadas porque:

-   fornecem a própria disponibilidade;
-   precisam saber datas, horários e locais;
-   recebem convocações;
-   recebem orientações de Davi;
-   possuem presença e participação registradas;
-   podem ser incluídas ou excluídas de decisões esportivas.

A atleta precisa receber uma informação clara e vigente, sem precisar interpretar banco de dados, fórmulas, riscos táticos ou áreas internas de Davi.

## Pessoas que não pertencem ao contexto interno

O CEPRAEA não possui:

-   comissão técnica;
-   coordenação;
-   equipe administrativa;
-   equipe operacional.

Esses termos presentes na planilha não representam a realidade e devem ser retirados do modelo conceitual.

# 3. Em qual contexto?

O problema ocorre no seguinte ambiente:

| **Dimensão** | **Contexto** |
| --- | --- |
| Equipe | CEPRAEA — adulto feminino |
| --- | --- |
| Modalidade | Handebol de praia |
| --- | --- |
| Temporada | 2026 |
| --- | --- |
| Composição humana | Davi e atletas |
| --- | --- |
| Operação | Centralizada exclusivamente em Davi |
| --- | --- |
| Treinos | Quintas, 20h–21h30; domingos, 7h–9h |
| --- | --- |
| Local recorrente | Copacabana |
| --- | --- |
| Competições | Estaduais, nacionais e internacionais |
| --- | --- |
| Obrigações | Inscrição, relação nominal, convocação, horários e resultados |
| --- | --- |
| Restrições | Até 12 convocadas e até 10 atletas por partida |
| --- | --- |
| Dependência técnica | Cobertura de funções, posições e sistemas táticos |
| --- | --- |
| Entradas | Respostas das atletas, decisões de Davi e documentos oficiais |
| --- | --- |
| Plataforma | Google Sheets e Google Drive |
| --- | --- |
| Arquitetura | Interface operacional mais banco canônico |
| --- | --- |
| Temporalidade | Informação muda antes, durante e depois de cada evento |
| --- | --- |

As planilhas analisadas são:

-   [CEPRAEA JUNHO 2026](https://docs.google.com/spreadsheets/d/14d3vIfkvhkTvjjTxkM7CxA9Oo1etHAgC2KUzGzzEn88/edit): interface operacional;
-   [CEPRAEA DATABASE](https://docs.google.com/spreadsheets/d/10Dv1oBIKdodWEWsK8qUeLPyazzdg4hdRkVi4gjvVSno/edit): fonte canônica pretendida.

# 4. Qual resultado deve ser produzido?

## Resultado principal

**Um estado operacional único, atual, verificável e pronto para decisão.**

Esse estado precisa permitir que Davi responda imediatamente:

1.  Quem integra atualmente o elenco?
2.  Quem respondeu para o próximo compromisso?
3.  Quem ainda não respondeu?
4.  Quais funções e posições estarão disponíveis?
5.  Quais sistemas podem ser treinados ou utilizados?
6.  Qual é a próxima ação?
7.  Qual é o prazo?
8.  Quem foi convocada?
9.  Quem realmente jogou?
10.  Quais resultados estão validados?
11.  O que deve ser comunicado às atletas?
12.  Qual fonte sustenta cada informação?

## Resultado para Davi

Davi deve receber:

-   visão consolidada do elenco;
-   pendências destacadas;
-   cobertura tática calculada;
-   compromisso vigente;
-   próxima ação;
-   convocação dentro dos limites;
-   separação entre planejamento e realização;
-   resultados e participações auditados;
-   histórico das alterações.

## Resultado para as atletas

As atletas devem receber somente:

-   compromisso vigente;
-   data;
-   horário;
-   local;
-   resposta registrada;
-   convocação;
-   orientação de Davi;
-   atualização relevante.

Informações internas, como criticidade e lacunas táticas, devem permanecer na área de Davi.

# 5. Critérios objetivos de sucesso

O problema estará resolvido quando:

1.  Banco e interface apresentarem exatamente o mesmo elenco.
2.  Gilvania e qualquer futura alteração existirem em todas as representações necessárias.
3.  Cada resposta manual for preservada sem inferência.
4.  Disponibilidade e comparecimento real forem conceitos separados.
5.  TALVEZ, SEM_RESPOSTA, NAO e demais estados possuírem definição única.
6.  O painel ativo exibir somente o compromisso vigente.
7.  Eventos passados forem arquivados ou marcados como concluídos.
8.  A cobertura tática utilizar dados atuais e completos.
9.  Convocação, escalação e participação real permanecerem separadas.
10.  Todo resultado possuir fonte e validação.
11.  As áreas das atletas e de Davi estiverem separadas.
12.  Não existirem referências a comissão técnica ou coordenação.
13.  Davi não precisar reconciliar manualmente duas abas para tomar uma decisão.

## Conclusão

O problema a resolver não é “melhorar a planilha”.

É:

**Eliminar a incerteza operacional de Davi, garantindo que a realidade mutável do CEPRAEA seja representada por dados atuais, consistentes, semanticamente corretos e verificáveis.**

O resultado esperado é uma fonte operacional confiável que reduza o trabalho de Davi, proteja as declarações das atletas e sustente decisões corretas sobre treino, composição, convocação, participação e comunicação.

## Definição canônica do CEPRAEA.

De acordo com as planilhas:

> **O CEPRAEA é uma equipe esportiva competitiva adulta feminina de handebol de praia, composta pelas atletas e conduzida exclusivamente pelo treinador Davi Sermenho. A equipe realiza treinos regulares, participa de competições estaduais e nacionais e mantém registros operacionais, técnico-táticos e esportivos de suas atividades.**

## Elementos que caracterizam o CEPRAEA

| Elemento | Evidência encontrada |

|---|---|

| Modalidade | Competições denominadas “Handebol de Praia” |

| Categoria | Adulto |

| Naipe | Feminino |

| Natureza | Equipe esportiva competitiva |

| Integrantes | Atletas e treinador |

| Treinador | Davi Sermenho |

| Treinos | Quintas, `20h–21h30`, e domingos, `7h–9h` |

| Local recorrente | Copacabana |

| Competições | Circuito Estadual, Circuito Brasileiro e Copa Brasil |

| Organizadores externos | FHERJ e CBHb |

| Estrutura esportiva | Goleiras, defesa e ataque |

| Temporada operacional atual | 2026 |

| Histórico disponível | Registros desde 2024 |

A planilha também registra que o CEPRAEA:

- foi campeão adulto feminino da Copa Brasil de 2026;

- obteve terceiro lugar na etapa do Circuito Brasileiro em Paranaguá;

- participa de etapas estaduais em Niterói;

- mantém calendário, disponibilidade, convocações, jogos, resultados e participação das atletas.

## Composição humana

A composição correta é:

```text

CEPRAEA

├── Treinador: Davi Sermenho

└── Atletas

```

Não existem, no contexto atual:

- comissão técnica;

- coordenação;

- equipe administrativa;

- equipe operacional interna.

Portanto, expressões presentes na planilha como `decisão da comissão` ou `informado pela coordenação` não descrevem corretamente o CEPRAEA.

## Distinção entre o CEPRAEA e as planilhas

O CEPRAEA é a **equipe esportiva real**. As planilhas são apenas sua representação digital.

| Objeto | Definição |

|---|---|

| **CEPRAEA** | Equipe formada por Davi e pelas atletas |

| **CEPRAEA DATABASE** | Banco que procura representar o estado canônico da equipe |

| **CEPRAEA JUNHO 2026** | Interface de agenda, respostas, comunicação e análise |

| **Registros históricos** | Evidências das atividades realizadas pela equipe |

Assim:

> O CEPRAEA não é a planilha, não é o banco de dados e não é o sistema. O sistema existe para registrar e apoiar a operação do CEPRAEA.

## Limites da definição

As planilhas não informam:

- a expansão formal da sigla `CEPRAEA`;

- natureza jurídica;

- CNPJ;

- estatuto;

- instituição mantenedora;

- data oficial de fundação;

- sede administrativa;

- propriedade ou representação legal.

Portanto, não é possível afirmar, apenas com essas planilhas, que o CEPRAEA seja juridicamente uma associação, clube, empresa ou projeto institucional.

A classificação comprovável é:

> **Equipe esportiva competitiva de handebol de praia adulto feminino.**

## Síntese ampliada do CEPRAEA

A busca no Google Drive encontrou 92 arquivos relacionados ao CEPRAEA. Considerando as planilhas operacionais, documentos técnicos e projetos auxiliares, a definição mais consistente é:

> **O CEPRAEA é uma equipe competitiva de handebol de praia feminino adulto, formada por atletas e dirigida pelo treinador Davi Sermenho.**

O CEPRAEA não é uma planilha nem um sistema de informação. As planilhas apenas representam e apoiam digitalmente o funcionamento da equipe. Também não encontrei evidência suficiente para defini-lo juridicamente como associação, empresa ou clube, nem para expandir com segurança o significado da sigla “CEPRAEA”.

A partir de consultas a outros arquivos, no Google Drive relacionados ao CEPRAEA, foi possível concluir que:

O CEPRAEA é uma equipe competitiva adulta feminina de handebol de praia, composta pelas atletas e conduzida exclusivamente pelo treinador Davi Sermenho. Os arquivos não comprovam a expansão da sigla, natureza jurídica, CNPJ ou existência de outros integrantes administrativos.

O Drive mostra que, além da equipe esportiva, está sendo construído um ecossistema interno de gestão e desempenho, composto por:

- controle de treinos, presenças e disponibilidade;

- calendário, inscrições e convocações;

- registro de jogos e resultados;

- classificação técnico-tática das atletas;

- análise de vídeos e scout;

- feedback individual e preparação mental;

- projetos futuros de aplicativo, banco PostgreSQL e IA/RAG.

Esses projetos representam iniciativas do CEPRAEA, mas vários ainda são modelos, pilotos ou documentos conceituais — não capacidades operacionais concluídas.

## Novos fatos encontrados

- O cadastro canônico possui 18 atletas ativas: 12 de ataque, 4 de defesa e 2 goleiras.

- A agenda de julho possui 19 atletas porque inclui Gilvania Balbino, ausente do cadastro canônico.

- Os treinos são registrados em Copacabana:

- quintas-feiras, das 20h às 21h30;

- domingos, das 7h às 9h.

- Davi Sermenho aparece como único responsável pelos treinos e proprietário das decisões.

- Nos resultados validados de 2026, até a 2ª Etapa Estadual:

- 19 jogos;

- 12 vitórias e 7 derrotas;

- 63% de aproveitamento;

- campeã da Copa Brasil adulta feminina;

- 3º lugar na 2ª Etapa do Circuito Brasileiro.

- Os documentos técnicos registram como referências táticas sistemas como ataque 3:1 e 4:0, defesa 3:0 e 2:1, transições, cobertura, giro, aérea, shoot-out e análise de posse.

- A autoavaliação contém 18 respostas coletadas em abril de 2026, sendo 13 de atletas que participaram da competição e 5 de não participantes.

- Uma resposta relata aumento da demanda de organização da equipe durante uma competição devido à ausência do treinador. É uma declaração individual, não uma constatação oficial, mas evidencia o risco de dependência operacional de uma única pessoa.

## Estrutura documental encontrada

A busca retornou 92 itens que mencionam CEPRAEA:

- 38 planilhas Google;

- 39 documentos Google;

- 5 arquivos XLSX;

- 4 PDFs;

- 4 arquivos Markdown;

- 1 DOCX e 1 pasta.

Dos 92 itens, 69 estão diretamente na raiz do Drive, 13 possuem tamanho igual ou inferior a 1 KB e 3 estão vazios. Há cópias, arquivos experimentais e títulos duplicados.

As fontes principais são:

| Arquivo | Função |

|---|---|

| [CEPRAEA DATABASE](https://docs.google.com/spreadsheets/d/10Dv1oBIKdodWEWsK8qUeLPyazzdg4hdRkVi4gjvVSno/edit) | Banco declarado como fonte oficial da verdade |

| [CEPRAEA JUNHO 2026](https://docs.google.com/spreadsheets/d/14d3vIfkvhkTvjjTxkM7CxA9Oo1etHAgC2KUzGzzEn88/edit) | Interface usada pelas atletas e por Davi |

| [CEPRAEA_CONTRACT.gdoc](https://docs.google.com/document/d/1EXWEC1ULPvUgtYCFKqrSJ4j4UBZi_bsHGgulie01T-s) | Governança, decisões, exceções e planos |

| [Arquitetura do Scout](https://drive.google.com/file/d/1bidA5X4t8KtKyPAkYFV6G2JmEeVWfdvu) | Modelo de análise de vídeo |

| [Piloto do Scout](https://docs.google.com/spreadsheets/d/1FXhp4l104X6gQ13oj1RwKA0KbtGjj-ZDdHyHVCNzeyI/edit) | Teste experimental de codificação |

| [MENTE CEPRAEA](https://docs.google.com/document/d/1gxe-gCEmCs33iG24y6KbeUStczL3lxp6S2Hy3kPTD4g) | Preparação mental e avaliações psicológicas |

| [Autoavaliação CEPRAEA](https://docs.google.com/spreadsheets/d/1N9ZdO7KiGqLkokrSGRodmbDaqNkGu8hNzxrRjNbcwpk/edit) | Respostas individuais das atletas |

| [Modelagem Attendance](https://docs.google.com/spreadsheets/d/1pRR6xrw_XUEWi65I01w27Bex7b0LFZCq8hK5AxFR83U/edit) | Projeto futuro de aplicação e banco normalizado |

## Problemas críticos identificados

1. **Permissões excessivas**

O banco oficial, o frontend, o contrato e a planilha piloto de scout estão configurados como “qualquer pessoa com o link pode editar”. No caso do `CEPRAEA DATABASE`, isso compromete diretamente a confiabilidade da fonte oficial.

2. **Divergência de elenco**

- Database: 18 atletas.

- Agenda de julho: 19 atletas.

- Gilvania aparece na agenda e nas presenças, mas não existe em `DB_ATLETAS`.

- Taís aparece na agenda, mas foi omitida da importação de presenças de julho.

Consequência concreta: em 23/07, o frontend registra 9 atletas com `SIM`, enquanto o indicador do database informa 8.

3. **Competição registrada como treino**

O database classifica 05/07 como treino em Copacabana, embora essa data corresponda à 3ª Etapa Estadual em Icaraí. Datas da etapa brasileira de junho também aparecem como treinos. Isso pode contaminar:

- totais de treinos realizados;

- indicadores de presença;

- cobertura por posição;

- avaliação individual de frequência.

4. **Conteúdo operacional vencido**

Em 23/07:

- a 3ª Etapa de 05/07 continua como `PREVISTA`;

- os resultados não foram registrados;

- “DIA DO JOGO” ainda apresenta o evento como próximo e confirmado;

- a previsão meteorológica continua sendo atualizada para uma etapa passada;

- o módulo de feedback de 07 e 10/07 permanece “EM CONFIGURAÇÃO”;

- o texto ainda diz que o link será informado pela “coordenação”, que não existe.

5. **Erros visíveis na agenda**

A consulta rápida da `AGENDA CEPRAEA` contém múltiplos erros `#REF!`, impedindo a identificação confiável de atletas confirmadas, pendentes e indisponíveis.

6. **Piloto do scout ainda não validado**

Embora indique “APROVADO COM RESTRIÇÃO”, a evidência mostra:

- apenas 12 de 29 eventos completos: 41,4%, contra meta de 90%;

- nenhuma decisão prática de treino, contra meta mínima de 3;

- indicador impossível de 999 eventos com evidência e taxa de 3.444,8%;

- eventos marcados como dúvida/revisão sem registros nas abas correspondentes;

- possível dupla contagem entre assistência e finalização.

Portanto, o piloto não deve ser tratado como sistema de scout validado.

7. **Dados sensíveis**

Existe uma planilha separada com dados cadastrais pessoais e o documento `MENTE CEPRAEA` contém interpretações psicológicas individualizadas. Ambos estão restritos ao proprietário, o que é positivo, mas devem permanecer completamente separados do frontend compartilhado e dos relatórios públicos.

## Conclusão da auditoria

A realidade documentada é a de uma equipe competitiva com bons resultados, mas operada por uma única pessoa e apoiada por um conjunto documental fragmentado. O maior problema atual não é falta de informação: é falta de uma verdade operacional única, atualizada, segura e semanticamente coerente.

A prioridade recomendada é:

1. restringir imediatamente a edição do database e do contrato;

2. decidir a situação de Gilvania e corrigir a importação de Taís;

3. separar definitivamente treino de competição;

4. atualizar a 3ª Etapa e arquivar painéis vencidos;

5. corrigir os `#REF!`;

6. recalcular presenças e treinos depois das correções;

7. substituir “coordenação”, “comissão técnica” e “staff” por “treinador” ou “Davi Sermenho”;

8. organizar cópias, pilotos e legados fora do conjunto canônico.

## Contexto do CEPRAEA

O CEPRAEA está inserido no esporte de rendimento, participando principalmente dos circuitos estadual e nacional de handebol de praia. A agenda também contempla eventos de maior abrangência.

Seu funcionamento envolve:

- Treinamentos regulares, registrados principalmente em Copacabana;

- Controle de presença e disponibilidade das atletas;

- Definição de elenco, convocações e participação em jogos;

- Participação em competições da FHERJ e da CBHb;

- Registro de resultados e desempenho individual e coletivo;

- Análise de sistemas defensivos e ofensivos;

- Scout de jogos, feedback individual e preparação mental;

- Acompanhamento da evolução da equipe durante a temporada.

Organizacionalmente, o contexto é particularmente centralizado: **Davi acumula as funções de treinador, operador das informações e principal responsável pelas decisões técnicas**. As atletas são as integrantes da equipe e também as principais fontes dos dados de presença, disponibilidade e desempenho. Não existe atualmente uma comissão técnica ou operacional adicional.

A realidade que justifica os instrumentos de gestão é, portanto, a necessidade de organizar e desenvolver uma equipe competitiva com poucos recursos humanos, mantendo informações confiáveis para que Davi possa tomar decisões sobre treinamentos, escalações, convocações, estratégia e desenvolvimento das atletas.

## Domínio, subdomínio e tema principal

| Classificação | Definição |

|---|---|

| **Domínio** | Gestão e desempenho no esporte de rendimento |

| **Subdomínio** | Gestão técnico-operacional e análise de desempenho no handebol de praia feminino adulto |

| **Tema principal** | Organização, preparação e tomada de decisão competitiva do CEPRAEA ao longo da temporada |

Essa classificação representa tanto a natureza esportiva da equipe quanto aquilo que os arquivos procuram organizar. O tema central não é simplesmente “armazenar dados”, mas **transformar informações sobre atletas, treinamentos, jogos e competições em decisões que melhorem a preparação e o desempenho competitivo do CEPRAEA**.

## Limites e inconsistências encontrados

A identidade esportiva do CEPRAEA está bem sustentada pelos arquivos, mas a auditoria encontrou pontos que exigem cautela:

- A base canônica possui 18 atletas ativas, enquanto a planilha operacional de julho apresenta 19, incluindo Gilvania Balbino. O elenco precisa ser reconciliado.

- Existem agendas e classificações de eventos que não foram atualizadas depois das respectivas datas.

- Há muitas cópias, pilotos e documentos experimentais, que não devem ser tratados como fontes oficiais.

- Projetos de software, scout automatizado e análise psicológica são iniciativas de apoio; eles não definem o que é o CEPRAEA.

- Algumas referências antigas a “comissão” ou “coordenação” não correspondem à composição atual informada: atletas e Davi.

Principais fontes auditadas:

[CEPRAEA DATABASE](https://docs.google.com/spreadsheets/d/10Dv1oBIKdodWEWsK8qUeLPyazzdg4hdRkVi4gjvVSno/edit), [CEPRAEA JUNHO 2026](https://docs.google.com/spreadsheets/d/14d3vIfkvhkTvjjTxkM7CxA9Oo1etHAgC2KUzGzzEn88/edit), [contrato operacional](https://docs.google.com/document/d/1EXWEC1ULPvUgtYCFKqrSJ4j4UBZi_bsHGgulie01T-s), [arquitetura do Scout](https://drive.google.com/file/d/1bidA5X4t8KtKyPAkYFV6G2JmEeVWfdvu) e [MENTE CEPRAEA](https://docs.google.com/document/d/1gxe-gCEmCs33iG24y6KbeUStczL3lxp6S2Hy3kPTD4g).