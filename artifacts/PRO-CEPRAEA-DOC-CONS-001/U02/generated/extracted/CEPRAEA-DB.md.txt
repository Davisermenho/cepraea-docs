CEPRAEA-DB — PLANO MESTRE PARA CRIAÇÃO DO BANCO DE DADOS DO PWA

OBJETIVO CONGELADO

“Criar o plano de ações completo, que será executado pela inteligência artificial para criar o banco de dados do PWA.”

# SISTEMA DE CONTROLE SEMÂNTICO-OPERACIONAL

**significado + fronteiras + autoridade + ações + estados + dependências + evidências + portões + testes = moldura semântico-operacional**

Este bloco é normativo e governa a interpretação e a execução de todo o restante do CEPRAEA-DB. As fases, entregáveis e exemplos posteriores ficam subordinados a estas regras. Uma descrição de fase não constitui, por si só, autorização para agir. A inteligência artificial somente poderá executar uma ação quando o registro da ação estiver completo, suas dependências estiverem satisfeitas, seu estado permitir execução e o portão anterior estiver aprovado.

## C0. REGRA DE SUPREMACIA E FINALIDADE DO CONTROLE

• O CEPRAEA-DB é a autoridade operacional do projeto, subordinado às instruções explícitas do proprietário do projeto e às fontes oficiais aplicáveis.

• O objetivo congelado não poderá ser reinterpretado, ampliado ou reduzido silenciosamente.

• Em caso de conflito interno, prevalece esta ordem: objetivo congelado → sistema de controle semântico-operacional → decisões humanas registradas → portões aprovados → fases e ações → exemplos e hipóteses.

• Exemplos de tabelas, campos, módulos, SQL ou arquitetura permanecem hipóteses até atravessarem os portões correspondentes.

• A ausência de informação não autoriza a invenção. A IA deverá registrar a lacuna, avaliar o impacto e bloquear ou escalar a decisão quando necessário.

## C1. SIGNIFICADO CANÔNICO DO PROJETO

### C1.1 Tema principal

Planejamento controlado da criação de um banco de dados para um PWA destinado à gestão, ao treinamento e à análise de uma equipe adulta feminina de handebol de areia.

### C1.2 Domínio metodológico principal

Engenharia do Conhecimento aplicada à Modelagem Semântica e Relacional de Dados. Esse domínio governa o método: adquirir, classificar, estruturar, validar e rastrear conhecimento antes de convertê-lo em requisitos, modelos e objetos de banco.

### C1.3 Domínio de aplicação

Ciências do Esporte, com foco em gestão, treinamento, competição e análise de desempenho no handebol de areia adulto feminino.

### C1.4 Domínios técnicos e auxiliares

• Engenharia de Requisitos.

• Engenharia e Governança de Dados.

• Modelagem conceitual, lógica, relacional e física.

• PostgreSQL e Supabase.

• Segurança, privacidade, RLS e auditoria.

• Arquitetura de PWA, operação offline e sincronização.

• Análise documental, linguística normativa e gestão de fontes.

• Testes, observabilidade, implantação e manutenção.

### C1.5 Contexto fixado

• Produto: PWA.

• Público inicial: um treinador e 19 atletas adultas.

• Modalidade: handebol de areia.

• Categoria inicial: adulto feminino.

• Backend previsto: Supabase/PostgreSQL.

• Repositório de fontes: pasta BEACH HANDBALL no Google Drive.

• Condição operacional relevante: conectividade potencialmente instável e necessidade de funcionamento offline.

• Condição de proteção: presença de dados pessoais e potencialmente sensíveis.

### C1.6 Taxonomia inicial de cobertura

**Engenharia do Conhecimento**

├─ governança e autoridade das fontes

├─ inteligência e segmentação documental

├─ extração e representação do conhecimento

├─ glossário, taxonomia e ontologia

├─ conflitos, ambiguidades e decisões

├─ engenharia de requisitos

└─ rastreabilidade até modelo, implementação e teste

**Handebol de Areia**

├─ regulamentação e arbitragem aplicável

├─ gestão da equipe, pessoas, vínculos e temporadas

├─ inscrições, convocações, escalações e competições

├─ partidas, períodos, eventos, punições e shoot-out

├─ planejamento e execução do treinamento

├─ carga, avaliações e monitoramento de desempenho

├─ saúde, bem-estar, disponibilidade e recuperação

├─ análise técnico-tática, posições, zonas e ações

├─ análise de goleiras

└─ relatórios, indicadores e mídia

**Plataforma de Dados**

├─ identidade e autorização

├─ modelo relacional e integridade

├─ histórico, versionamento e auditoria

├─ Storage e metadados

├─ sincronização e idempotência

├─ consultas, índices e desempenho

├─ migrations e ambientes

└─ testes, implantação e manutenção

### C1.7 Tipos semânticos obrigatórios

Todo item extraído ou criado deverá ser classificado, no mínimo, como um dos 28 tipos semânticos obrigatórios abaixo:

1\. fonte normativa;

2\. fonte regulatória local;

3\. fonte científica;

4\. material técnico;

5\. requisito operacional;

6\. conceito;

7\. entidade candidata;

8\. atributo;

9\. evento;

10\. papel;

11\. estado;

12\. relação;

13\. cardinalidade;

14\. regra;

15\. condição;

16\. exceção;

17\. proibição;

18\. obrigação;

19\. cálculo;

20\. métrica;

21\. evidência;

22\. fato histórico;

23\. hipótese;

24\. decisão;

25\. dúvida;

26\. risco;

27\. controle;

28\. teste.

**Regras de interpretação:**

• regra oficial vigente não é equivalente a evidência científica;

• requisito do PWA não é equivalente a regra oficial da modalidade;

• decisão do treinador não é equivalente a obrigação normativa;

• frequência estatística não é equivalente a prescrição;

• hipótese não é equivalente a decisão validada;

• configuração atual não é equivalente a fato histórico;

• exemplo documental não é automaticamente uma regra geral.

## C2. FRONTEIRAS DO PROJETO

### C2.1 Escopo positivo

Está dentro do escopo: inventariar e classificar fontes; verificar autoridade e vigência; segmentar documentos; extrair conhecimento; construir glossário e taxonomia; identificar regras, relações e cardinalidades; levantar requisitos; mapear atores e jornadas; produzir rastreabilidade; criar modelos conceitual, lógico e físico; definir segurança, RLS, Storage e sincronização; gerar migrations e seeds de teste; testar integridade, segurança, integração, desempenho e operação offline; implantar e manter o banco de forma controlada.

### C2.2 Escopo negativo

Está fora do escopo, salvo mudança formal aprovada:

• criar imediatamente o banco antes dos portões exigidos;

• tratar hipóteses anteriores como modelo aprovado;

• substituir decisão técnica do treinador;

• emitir diagnóstico, prognóstico ou prescrição médica;

• funcionar como sistema oficial completo de arbitragem, federação ou gestão financeira;

• administrar múltiplas modalidades sem autorização;

• transformar resultados científicos em constraints normativas sem fonte competente;

• inserir dados pessoais reais em seeds ou ambientes de teste;

• expor credenciais privilegiadas no PWA;

• alterar produção manualmente sem migration e registro;

• apagar fatos históricos para representar correções;

• ampliar silenciosamente atores, módulos, integrações ou finalidades.

### C2.3 Regra de mudança de fronteira

Qualquer inclusão, exclusão ou alteração de escopo deverá gerar um registro de decisão com motivo, origem, alternativas, impactos, riscos, aprovador e versão do plano afetada. Até a aprovação, a solicitação permanecerá bloqueada ou classificada como proposta.

## C3. AUTORIDADE E DIREITOS DE DECISÃO

### C3.1 Hierarquia de autoridade

1\. Instrução explícita e vigente do proprietário do projeto.

2\. Objetivo congelado e versão aprovada do CEPRAEA-DB.

3\. Regras oficiais vigentes da IHF e normas aplicáveis de autoridade competente.

4\. Regulamentos de competição e esclarecimentos vigentes, dentro de sua jurisdição.

5\. Requisitos do PWA formalmente validados.

6\. Decisões de modelagem e arquitetura registradas e aprovadas.

7\. Estudos científicos e materiais técnico-táticos como evidência, métrica ou hipótese.

8\. Inferências da IA, sempre sem autoridade própria até validação.

### C3.2 Direitos de decisão

• Decisões de domínio esportivo: especialista de domínio ou responsável humano designado.

• Decisões de produto e escopo: proprietário do projeto.

• Decisões de modelagem e banco: responsável técnico designado, preservada a validação do domínio.

• Decisões de segurança, privacidade e dados sensíveis: responsável técnico e autoridade humana competente.

• Decisões de implantação e produção: responsável humano autorizado.

• A IA poderá recomendar, comparar, executar ações autorizadas e produzir evidências; não poderá autoaprovar mudança de objetivo, escopo, autoridade, portão ou produção.

### C3.3 Conflitos de autoridade

Conflitos entre fontes de mesma autoridade, divergências de tradução com impacto material ou ausência de autoridade suficiente deverão gerar bloqueio e escalonamento. A IA deverá apresentar problema, fontes, alternativas, impactos e decisão requerida.

## C4. AÇÕES CONTROLADAS

### C4.1 Unidade executável

A unidade executável do plano é a AÇÃO CONTROLADA. Cada ação deverá possuir:

• identificador único no formato ACT-Fxx-nnn;

• nome e objetivo;

• fase e subdomínio;

• tipo semântico do objeto tratado;

• entradas autorizadas;

• precondições;

• dependências;

• procedimento;

• saídas e artefatos;

• evidências obrigatórias;

• testes aplicáveis;

• risco e controles;

• responsável por validação;

• portão relacionado;

• estado atual;

• bloqueios e perguntas abertas;

• próxima ação permitida.

### C4.2 Regras de execução das ações

• Nenhuma ação poderá iniciar sem entradas identificadas e precondições verdadeiras.

• Nenhuma ação poderá ser declarada concluída sem saída verificável e evidência registrada.

• Ações destrutivas, alterações de produção, mudanças de escopo e decisões de alto impacto exigem autorização humana explícita.

• A fase descreve um agrupamento de trabalho; somente ações controladas são executáveis.

• A ação deverá operar apenas sobre o escopo autorizado e não poderá criar entregáveis adicionais como fatos consumados.

• Toda execução deverá registrar o que foi feito, o que não foi feito, limitações, divergências e estado resultante.

### C4.3 Registro mínimo de riscos e controles

Para cada risco relevante deverá existir pelo menos um controle, uma ação responsável, uma evidência e um teste.

Exemplos obrigatórios:

• SQL prematuro → dependências e portões D/E/F;

• regra revogada → matriz de autoridade e vigência;

• estudo tratado como norma → classificação semântica da fonte;

• hipótese tratada como decisão → máquina de estados;

• dado sensível exposto → classificação, RLS e testes adversariais;

• expansão silenciosa → escopo negativo e controle de mudanças;

• conclusão sem prova → evidência obrigatória e teste de completude.

## C5. ESTADOS E TRANSIÇÕES

### C5.1 Estados permitidos

NÃO\_INICIADO; IDENTIFICADO; PRONTO; EM\_EXECUÇÃO; PRODUZIDO; EM\_REVISÃO; VALIDADO; REJEITADO; BLOQUEADO; IMPLEMENTADO; TESTADO; VERIFICADO; SUBSTITUÍDO.

### C5.2 Transições normais

NÃO\_INICIADO → IDENTIFICADO → PRONTO → EM\_EXECUÇÃO → PRODUZIDO → EM\_REVISÃO → VALIDADO.

Após validação, quando aplicável:

VALIDADO → IMPLEMENTADO → TESTADO → VERIFICADO.

Transições de exceção:

• qualquer estado anterior à validação poderá ir para BLOQUEADO;

• EM\_REVISÃO poderá ir para REJEITADO ou retornar a EM\_EXECUÇÃO;

• item validado substituído por nova versão deverá ir para SUBSTITUÍDO, preservando histórico;

• BLOQUEADO somente poderá sair após registro e resolução da causa.

### C5.3 Invariantes de estado

• IDENTIFICADO não significa extraído.

• PRODUZIDO não significa revisado.

• EM\_REVISÃO não significa aprovado.

• VALIDADO não significa implementado.

• IMPLEMENTADO não significa testado.

• TESTADO não significa verificado para produção.

• A IA não poderá promover estados sem evidência compatível.

## C6. DEPENDÊNCIAS E ORDEM DE EXECUÇÃO

### C6.1 Grafo mínimo de dependências

• Fase 0 precede todas as demais.

• Fase 1 precede as Fases 2 e 3.

• Fases 2 e 3 precedem a Fase 4.

• Fase 4 precede a Fase 5.

• Fases 5 e 6 precedem a Fase 7.

• Fase 7 precede a Fase 8.

• Fase 8 precede a Fase 9.

• Fase 9 precede as Fases 10, 11 e 12.

• Fases 10, 11 e 12 precedem a Fase 13.

• Fase 13 precede as Fases 14, 15 e 16.

• Fases 14, 15 e 16 precedem a Fase 17.

### C6.2 Regra de paralelismo

Ações poderão ocorrer em paralelo somente quando não houver dependência entre elas, os objetos tratados estiverem claramente separados e a consolidação posterior estiver prevista. Paralelismo não poderá ser usado para contornar portões.

### C6.3 Regra de próxima ação

A IA deverá selecionar apenas ações em estado PRONTO, cujas dependências estejam VALIDADAS ou VERIFICADAS conforme o caso. Em caso de múltiplas ações prontas, deverá priorizar:

bloqueios críticos → integridade semântica → segurança → caminho crítico → menor risco de retrabalho.

## C7. EVIDÊNCIAS E RASTREABILIDADE

### C7.1 Tipos de evidência

• referência de fonte e trecho;

• inventário ou contagem reconciliada;

• artefato produzido;

• comparação entre versões;

• decisão humana registrada;

• resultado de consulta ou inspeção;

• resultado de teste positivo ou negativo;

• log de migration ou implantação;

• relatório de advisor, desempenho ou segurança;

• readback que confirme a alteração no destino correto.

### C7.2 Metadados mínimos da evidência

Toda evidência deverá registrar: identificador; ação de origem; data ou revisão quando disponível; objeto comprovado; método de obtenção; localização; resultado; limitações; responsável pela validação; estado.

### C7.3 Rastreabilidade bidirecional obrigatória

fonte → segmento → regra ou conceito → requisito → decisão → modelo → objeto do banco ou policy → teste → evidência de resultado.

O caminho inverso também deverá ser possível: objeto implementado → decisão → requisito → regra ou necessidade → fonte. Um objeto sem origem ou justificativa deverá ser bloqueado até regularização.

## C8. PORTÕES DE VALIDAÇÃO

### C8.1 Decisões possíveis

APROVADO;

APROVADO\_COM\_RESSALVAS;

REPROVADO;

BLOQUEADO.

### C8.2 Protocolo de cada portão

Cada portão deverá indicar: entradas obrigatórias; ações e estados esperados; evidências; testes; pendências; riscos residuais; autoridade aprovadora; decisão; condições impostas; próxima fase autorizada.

### C8.3 Regra de avanço

• APROVADO autoriza a dependência seguinte.

• APROVADO\_COM\_RESSALVAS autoriza apenas ações explicitamente liberadas e mantém condições rastreáveis.

• REPROVADO devolve itens para correção.

• BLOQUEADO impede avanço até resolução formal.

• A IA não poderá autoaprovar portões que exijam julgamento humano de domínio, escopo, segurança ou produção.

## C9. TESTES DO COMPORTAMENTO DA IA E DO PLANO

### C9.1 Testes semânticos

• Distinguir regra oficial, requisito operacional, evidência científica, hipótese e decisão.

• Classificar corretamente conceitos, eventos, atributos, métricas, exceções e fatos históricos.

• Não converter exemplo ou frequência estatística em obrigação.

### C9.2 Testes de fronteira

• Solicitação fora do escopo deverá ser marcada como mudança proposta, não executada silenciosamente.

• Solicitação médica deverá ser limitada a registro e acompanhamento de dados, sem diagnóstico ou prescrição.

• Solicitação de módulo federativo, financeiro ou multimodal deverá ser bloqueada até mudança formal.

### C9.3 Testes de autoridade

• Regra oficial vigente deverá prevalecer sobre material secundário incompatível.

• Conflito entre fontes de mesma autoridade deverá ser escalado.

• Inferência da IA não poderá ser apresentada como decisão aprovada.

### C9.4 Testes de sequência e estado

• Pedido de SQL antes dos portões necessários deverá ser recusado ou mantido como hipótese não executável.

• Item PRODUZIDO não poderá ser tratado como VALIDADO.

• Ação com dependência bloqueada não poderá iniciar.

### C9.5 Testes de evidência e rastreabilidade

• Toda conclusão crítica deverá apontar para evidência.

• Toda tabela, constraint, policy ou cálculo deverá possuir caminho até requisito e fonte ou necessidade operacional.

• Divergência entre alegação e readback deverá manter o item não verificado.

### C9.6 Testes técnicos posteriores

Quando aplicáveis, deverão incluir: integridade; limites; exceções; temporalidade; RLS; acesso horizontal e vertical indevido; sincronização duplicada, parcial e fora de ordem; rollback; restauração; desempenho; compatibilidade de migrations; funcionamento online e offline.

## C10. CICLO OPERACIONAL OBRIGATÓRIO DA INTELIGÊNCIA ARTIFICIAL

Para cada iteração, a IA deverá executar a sequência:

1\. Ler a versão vigente do plano e o estado atual.

2\. Identificar a próxima ação PRONTA.

3\. Confirmar objetivo, subdomínio, escopo e tipo semântico.

4\. Verificar autoridade, dependências, precondições e portão anterior.

5\. Confirmar entradas e riscos.

6\. Executar somente o procedimento autorizado.

7\. Produzir artefatos e evidências.

8\. Executar autotestes e testes aplicáveis.

9\. Registrar limitações, conflitos, perguntas e estado resultante.

10\. Submeter a revisão ou portão quando necessário.

11\. Atualizar rastreabilidade e próxima ação permitida.

12\. Parar diante de bloqueio; nunca preencher a lacuna por invenção.

## C11. CONDIÇÕES OBRIGATÓRIAS DE PARADA E ESCALONAMENTO

A IA deverá parar e produzir um registro de escalonamento quando ocorrer:

• conflito material entre fontes de mesma autoridade;

• ambiguidade que altere cardinalidade, integridade, segurança ou significado de dado;

• mudança de objetivo ou escopo;

• decisão médica, clínica ou disciplinar fora da competência do sistema;

• decisão sobre dados sensíveis sem regra suficiente;

• operação destrutiva ou alteração de produção sem autorização;

• ausência de evidência para concluir ação crítica;

• inconsistência entre estados, dependências ou portões;

• impossibilidade técnica que comprometa a forma ou a integridade exigida.

O registro de escalonamento deverá conter: problema; contexto; fontes; alternativas; recomendação; impactos; risco de não decidir; autoridade necessária; ação bloqueada.

## C12. CRITÉRIOS DE SUFICIÊNCIA DA MOLDURA

A moldura somente será considerada validada quando uma IA, lendo apenas o CEPRAEA-DB, conseguir responder corretamente:

• qual é o objetivo e o tema;

• qual domínio governa o método;

• qual é o domínio de aplicação;

• quais subdomínios devem ser cobertos;

• o que está dentro e fora do escopo;

• qual fonte ou decisão possui maior autoridade;

• qual é o estado real do projeto;

• qual ação pode ser executada em seguida;

• quais dependências e portões impedem avanço;

• qual evidência prova a conclusão;

• quando deve parar e escalar;

• quando tabelas, SQL, migrations e produção podem ser autorizados.

## C13. CONTROLE DE MUDANÇAS DO PRÓPRIO PLANO

Alterações no objetivo, domínio, taxonomia estrutural, escopo, hierarquia de autoridade, direitos de decisão, estados, dependências, portões ou critérios de aceite exigem registro formal de mudança e validação humana. Alterações meramente editoriais não poderão mudar significado, autoridade ou comportamento. Versões substituídas deverão permanecer identificáveis.

## C14. ESTADO DESTA CAMADA DE CONTROLE

### C14.1 AÇÃO CONTROLADA EXECUTADA — ACT-F00-001

### Identificador: ACT-F00-001.

Nome: revisar e validar a moldura semântico-operacional.

Objetivo: verificar se a moldura controla, de forma completa, coerente e localizável, a interpretação e o comportamento da inteligência artificial durante toda a execução do plano.

Fase: Fase 0 — Governança, escopo e ambiente de trabalho.

Subdomínio: governança da IA, engenharia do conhecimento, controle de processo e qualidade do plano.

Tipo semântico: ação de validação; controle; decisão; evidência; teste.

Entradas autorizadas: versão vigente do CEPRAEA-DB; critérios C0–C13; validação humana registrada em 30 de julho de 2026; referência de conformidade .inicio/VALIDAR-MOLDURA.md.

Precondições: objetivo congelado; molduras C1–C3 e C4–C11 presentes; cadeia de derivação preservada; critérios de suficiência definidos; autoridade humana para validar confirmada.

Dependências: inserção e revisão estrutural da camada C0–C14; confirmação humana de que os gaps remanescentes são formais, e não deficiências da moldura.

Procedimento executado:

1\. confirmar a presença da moldura semântica C1–C3;

2\. confirmar a presença da moldura operacional C4–C11;

3\. verificar a interligação entre significado, fronteiras, autoridade, ações, estados, dependências, evidências, portões e testes;

4\. verificar a integridade da cadeia de derivação;

5\. verificar a localizabilidade das respostas às perguntas de suficiência;

6\. classificar os gaps remanescentes;

7\. registrar evidências, decisão e estado resultante;

8\. instanciar a próxima ação controlada.

Saídas e artefatos: registro completo da ACT-F00-001; registro de validação; matriz resumida de evidências; registro dos gaps fechados; próxima ação controlada instanciada.

Riscos: autoaprovação indevida; promoção sem evidência; confusão entre gap formal e deficiência estrutural; perda da cadeia de rastreabilidade.

Controles aplicados: validação humana explícita; readback do documento; critérios C12; máquina de estados C5; protocolo de evidências C7; controle de mudanças C13.

Responsável pela validação: proprietário do projeto, por instrução explícita registrada nesta conversa.

Portão relacionado: Portão de governança da Fase 0, anterior ao Portão A — Fontes.

Estado final da ação: VALIDADO.

Bloqueios ou perguntas abertas: nenhum bloqueio relativo à validade da moldura. A execução das fases posteriores continua condicionada aos seus próprios portões.

Próxima ação permitida: ACT-F01-001 — inventariar integralmente as fontes.

#### C14.2 EVIDÊNCIAS DA VALIDAÇÃO

| **ID** | **Ação de Origem** | **Data** | **Objeto** | **Método** | **Localização** | **Resultado** | **Limitação** | **Estado** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **EVD-F00-001** | ACT-F00-001 | 30/07/2026 | Moldura semântica | Inspeção estrutural e validação humana | C1–C3 | Presente, completa e interligada | Não substitui a validação futura dos artefatos de domínio | VALIDADO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **EVD-F00-002** | ACT-F00-001 | 30/07/2026 | Moldura operacional | Inspeção estrutural e validação humana | C4–C11 | Presente, completa e interligada | Cada ação futura deverá ser instanciada individualmente | VALIDADO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **EVD-F00-003** | ACT-F00-001 | 30/07/2026 | Cadeia de derivação | Verificação de rastreabilidade (significado, fronteiras, autoridade, ações, estados, dependências, evidências, portões, testes) | C0–C13 e fluxo por fases | Cadeia intacta | — | VALIDADO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **EVD-F00-004** | ACT-F00-001 | 30/07/2026 | Critérios de suficiência | Teste de localizabilidade | C12 e seções correspondentes | Perguntas de suficiência possuem resposta localizável | — | VALIDADO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **EVD-F00-005** | ACT-F00-001 | 30/07/2026 | Destino e persistência | Leitura posterior (CEPRAEA-DB, aba t.0) | Documento ID: 1J6kJ\_DpQCHNE6Xp6ybgtOMzrJos0i5vnt\_9DXeXlzfw | Ação, evidências, gaps e estado confirmados | — | VERIFICADO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

C14.3 TESTES EXECUTADOS

TST-F00-001 — Teste semântico: distinguir domínio metodológico, domínio de aplicação, requisito, regra, evidência, hipótese e decisão. Resultado: APROVADO.

TST-F00-002 — Teste de fronteira: localizar escopo positivo, escopo negativo e regra de mudança. Resultado: APROVADO.

### TST-F00-003 — Teste de autoridade: localizar hierarquia, direitos de decisão e regra de escalonamento. Resultado: APROVADO.

TST-F00-004 — Teste operacional: localizar unidade executável, estados, dependências, evidências, portões e ciclo da IA. Resultado: APROVADO.

TST-F00-005 — Teste de sequência: verificar que fases não autorizam execução sem ação PRONTA e dependências satisfeitas. Resultado: APROVADO.

TST-F00-006 — Teste de suficiência: verificar respostas localizáveis às perguntas do protocolo .inicio/VALIDAR-MOLDURA.md. Resultado: APROVADO.

TST-F00-007 — Teste de não autoaprovação: confirmar que a promoção decorre de validação humana explícita, e não de inferência autônoma da IA. Resultado: APROVADO.

C14.4 FECHAMENTO DOS TRÊS GAPS FORMAIS

### GAP-F00-001 — Ausência de instância completa da ACT-F00-001. Tratamento: ação instanciada no formato definido em C4.1. Estado: FECHADO.

GAP-F00-002 — Ausência de evidências e testes locais da validação. Tratamento: evidências EVD-F00-001 a EVD-F00-005 e testes TST-F00-001 a TST-F00-007 registrados. Estado: FECHADO; readback EVD-F00-005 verificado.

GAP-F00-003 — Ausência de próxima ação controlada instanciada e de transição formal de estado. Tratamento: ACT-F01-001 instanciada e transição EM\_REVISÃO → VALIDADO registrada. Estado: FECHADO.

C14.5 DECISÃO E TRANSIÇÃO DE ESTADO

Decisão: APROVADO.

### Justificativa: as molduras semântica C1–C3 e operacional C4–C11 estão presentes, completas e interligadas; a cadeia de derivação está intacta; as perguntas de suficiência possuem respostas localizáveis; os gaps identificados eram formais e foram tratados nesta ação.

Transição autorizada: EM\_REVISÃO → VALIDADO.

Estado vigente da camada de controle: VALIDADO.

Efeito da decisão: a moldura passa a governar formalmente as ações posteriores. Esta validação não aprova antecipadamente inventários, conhecimento extraído, requisitos, modelos, SQL, migrations, policies ou produção.

C14.6 PRÓXIMA AÇÃO CONTROLADA — ACT-F01-001

Identificador: ACT-F01-001.

Nome: inventariar integralmente as fontes.

### Objetivo: produzir uma relação completa, reconciliada e verificável de todos os itens da pasta BEACH HANDBALL, sem deixar arquivo sem status e justificativa.

Fase: Fase 1 — Inventário integral das fontes.

Subdomínio: governança e autoridade das fontes.

Tipo semântico: ação de aquisição; fonte; inventário; evidência; controle.

Entradas autorizadas: pasta BEACH HANDBALL no Google Drive; metadados dos arquivos; versão VALIDADA do CEPRAEA-DB.

Precondições: ACT-F00-001 VALIDADA; acesso de leitura à pasta confirmado; destino dos resultados definido no documento mestre.

Dependências: nenhuma fase posterior. Esta ação precede ACT-F02-001 e as ações da Fase 3.

Procedimento: listar todos os itens; registrar ID, título, tipo, formato, tamanho, idioma, data, autoria aparente e disponibilidade; identificar vazios, falhas, duplicações e versões; classificar o tratamento previsto; reconciliar a contagem; atribuir status e justificativa a 100% dos itens.

Saídas e artefatos: inventário integral; mapa de cobertura documental; lista de limitações e indisponibilidades; evidência de contagem reconciliada.

Evidências obrigatórias: listagem da pasta; metadados individuais; contagem total reconciliada; readback do inventário persistido.

Testes aplicáveis: completude; unicidade de ID; ausência de item sem status; consistência de contagem; classificação válida; detecção de arquivo vazio ou inacessível.

Riscos e controles: omissão de arquivo → reconciliação de contagem; duplicidade → comparação de ID e versão; classificação prematura → estado IDENTIFICADO; arquivo inacessível → status explícito e limitação.

Responsável por validação: proprietário do projeto ou responsável humano designado.

Portão relacionado: Portão A — Fontes.

Estado atual: PRONTO.

Bloqueios e perguntas abertas: nenhum bloqueio inicial conhecido; limitações encontradas deverão ser registradas, não ocultadas.

Próxima ação permitida após conclusão: ações controladas das Fases 2 e 3, condicionadas à revisão do inventário e às dependências aplicáveis.

## C15. EXECUÇÃO DA ACT-F01-001 — INVENTÁRIO INTEGRAL DAS FONTES

### C15.1 Registro da ação controlada

Identificador: ACT-F01-001.

Nome: Inventariar integralmente as fontes.

Objetivo: conhecer e catalogar todos os itens diretamente contidos na pasta BEACH HANDBALL antes da extração de conhecimento.

Fase: Fase 1.

Subdomínio: governança e autoridade das fontes.

Tipo semântico: ação de inventário documental.

Entradas autorizadas: pasta BEACH HANDBALL (ID 1Z0OsR3dHmLMED0KYc\_EE2lD1nEYykzWY), metadados do Google Drive e versão vigente do CEPRAEA-DB.

Precondições: moldura semântico-operacional VALIDADA; pasta localizada; acesso de listagem confirmado; ação em estado PRONTO.

Dependências: ACT-F00-001 VALIDADA.

Procedimento executado: listar todos os filhos diretos; reconciliar a contagem; registrar ID, título, formato, tamanho, datas e disponibilidade; atribuir classificação preliminar, idioma aparente, tratamento previsto e exceções; identificar arquivos vazios e candidatos a duplicidade.

Saídas: inventário integral abaixo, resumo quantitativo, mapa de exceções e próxima ação.

Responsável pela validação: proprietário do projeto.

Portão relacionado: Portão A — Fontes.

Estado resultante: PRODUZIDO, aguardando revisão do Portão A.

Bloqueios: nenhum para concluir o inventário; arquivos vazios permanecem indisponíveis para análise de conteúdo.

Próxima ação permitida: ACT-F02-001 — classificar autoridade, vigência e relações entre versões.

### C15.2 Resultado reconciliado

• Pasta verificada: BEACH HANDBALL.

• Itens diretos catalogados: 43.

• Formatos: 41 PDFs e 2 arquivos Markdown.

• Arquivos com tamanho maior que zero: 39.

• Arquivos de tamanho zero: 4.

• Subpastas encontradas: 0.

• Todos os itens possuem ID, título, formato, tamanho, disponibilidade e tratamento explícito.

• Idioma e classe são preliminares quando inferidos apenas pelo título; serão confirmados pela leitura nas Fases 2 e 3.

• Autoria aparente não foi atribuída quando não estava disponível nos metadados ou no título; será obtida do conteúdo.

### C15.3 Inventário integral

Formato de cada registro: número | ID | título | formato/tamanho | idioma aparente | classe preliminar | disponibilidade | tratamento.

01 | 1MXLOcWY9r1RdQ6zKWA3qI5AJOfHkguT2 | regulamento\_cbhb\_2026.pdf | PDF, 6.385.991 bytes | português | regulatório nacional | disponível | análise integral e comparação normativa.

02 | 1nL49p72AVybqNu422FJPycld2nmejoIG | Esclarecimentos regras de jogo.pdf | PDF, 147.695 bytes | português | esclarecimento normativo | disponível | análise integral e correlação com regras vigentes.

03 | 1scHN1330ZX6EqvgF2ld9-lfs1hrs\_\_Im | Regras de Handebol de Praia 2026 - Tradução 29 de maio de 2026.pdf | PDF, 15.422.591 bytes | português | tradução normativa | disponível | análise integral e comparação com original.

04 | 1376ozyK5bKY\_xgtEmjKDjWKQzQp0YjNt | Mudanças nas Regras de Handebol de Praia 2026.pdf | PDF, 201.427 bytes | português | atualização normativa | disponível | análise integral e linha temporal.

05 | 1WTB7ihMOkNtUXsrl67yAyy5tUvAccRt4 | atualizacoes\_ihf\_2026.md | Markdown, 11.803 bytes | português | compilação de atualizações | disponível | análise suplementar e verificação de origem.

06 | 10UvC1U2ef3AePzZqTXBBqi57AlKA4WM- | pagina\_ihf\_rules\_beach\_handball.md | Markdown, 768 bytes | português/aparente | registro de página-fonte | disponível | catalogação e verificação de links/origem.

07 | 1nCp6EXVpBMMgDgi8od2sUUMoFEI90hGm | regras\_ihf\_beach\_handball\_2026\_fr.pdf.pdf | PDF, 2.343.407 bytes | francês | regra oficial IHF | disponível | análise comparativa de idioma.

08 | 1c5NWDpXgYhNFSobOTgLQ7l5ZnaXrpcxU | regras\_ihf\_beach\_handball\_2026\_de.pdf.pdf | PDF, 2.224.510 bytes | alemão | regra oficial IHF | disponível | análise comparativa de idioma.

09 | 1S-OSzrMYR0CkUi2YC2wV8DQL3QgtVRJD | regras\_ihf\_beach\_handball\_2026.pdf | PDF, 1.948.878 bytes | inglês/aparente | regra oficial IHF | disponível | análise integral; candidato a duplicidade com item 10.

10 | 1xf\_td5UAFtvegx2i7kcvBby-VbZdtXaq | regras\_ihf\_beach\_handball\_2026\_en.pdf.pdf | PDF, 1.948.878 bytes | inglês | regra oficial IHF | disponível | comparação binária/conteúdo com item 09.

11 | 1yzivnYq7I3MybEUV3rCvjpwet8PjvSL- | mini\_beach\_handball\_info\_sheet.pdf | PDF, 0 bytes | inglês/aparente | informativo | indisponível: vazio | manter catalogado; solicitar reposição se necessário.

12 | 1Ydw7Fs0rVp1dbVsLte6lfa196LSbUVco | ultimate\_school\_handball\_2025.pdf | PDF, 0 bytes | inglês/aparente | material escolar/técnico | indisponível: vazio | manter catalogado; solicitar reposição se necessário.

13 | 170GBYtS4dqs3Qox53\_GsPA-dsdLTbxhg | shootout\_psychological\_pressure.pdf | PDF, 0 bytes | inglês/aparente | científico/psicologia | indisponível: vazio | manter catalogado; solicitar reposição se necessário.

14 | 1DtO17h9BnqUTOVuXn8nAVNRuvqzHmvZv | refereeing\_beach\_handball.pdf | PDF, 0 bytes | inglês/aparente | arbitragem | indisponível: vazio | manter catalogado; solicitar reposição se necessário.

15 | 1\_udt6wooR9Nnq\_BaJB2rgr2-lW0UVOO1 | 20070912183144claudia\_monteiro2.pdf | PDF, 1.274.901 bytes | indeterminado | acadêmico/técnico a confirmar | disponível | identificação bibliográfica e análise conforme conteúdo.

16 | 12XNAy1uG-xpDzvRSTvFIWNJ-4jGSOmMQ | IntroductionToBeachHandball.pdf | PDF, 1.306.484 bytes | inglês | introdutório/técnico | disponível | análise suplementar.

17 | 1JktKke-jUmyNsGFDdYHjyUwCCrlgM4Y1 | download.pdf | PDF, 331.480 bytes | indeterminado | técnico a confirmar | disponível | identificar título real; candidato a duplicidade com item 38.

18 | 1wmoXa9uaLgFbGpt7kUstfbTsK-2Tl\_R\_ | Art 135.pdf | PDF, 204.626 bytes | indeterminado | artigo científico a confirmar | disponível | identificação bibliográfica e análise.

19 | 1cUBMm5IOeJWU2yOgbuAArPkvrlUBsYhd | CONTROLDEVOLUMENDEENTRENAMIENTOENJUGADORESMEXICANOSDEFUTBOLDETERCERADIVISION\_Revista34.pdf | PDF, 2.058.175 bytes | espanhol | científico, treinamento em futebol | disponível | avaliar aplicabilidade; provável fonte comparativa/fora do núcleo.

20 | 12mwIXjhKLvxRUtE7kbiB2c4UpCZ5WcIN | KinesiologyProceedingsBook6th-2011.pdf | PDF, 23.830.437 bytes | inglês/aparente | anais científicos | disponível | localizar capítulos pertinentes; análise seletiva.

21 | 1It2a7dYCq8sEbih2oOB41eucwNo2Yhm7 | Notational-analysis-of-be.pdf | PDF, 3.682.373 bytes | inglês | científico/análise notacional | disponível | análise integral ou capítulo pertinente.

22 | 1IZqfCOtwIRnlw6AYsurHfp8V5nn\_2N8b | Estudo das ações do guarda redes de andebol de praia através da análise.pdf | PDF, 1.383.314 bytes | português | científico/goleiras | disponível | análise integral.

23 | 1CtwKtYgfSVGNuLlml90HQVxzDYype6Nm | External Load Analysis in Beach Handball.pdf | PDF, 665.315 bytes | inglês | científico/carga externa | disponível | análise integral.

24 | 1wMSMDrbsagansqpWRG6SGNR606zC4Ccg | DEVELOPMENT\_OF\_AN\_INSTRUMENT\_FOR\_THE\_OBSERVATION\_OF\_COLLECTIVE\_TACTICAL\_PROCEDURES\_OF\_POSITIONAL\_ATTACK\_IN\_BEACH\_HANDBALL.pdf | PDF, 473.513 bytes | inglês | científico/análise técnico-tática | disponível | análise integral.

25 | 1XQ\_0SZ-cq0N0OOd6myn9OGqU\_hxUXaGe | A\_importância\_das\_posições\_dos\_passes\_para\_arremessos\_em\_gol\_de\_atletas\_da\_categoria\_adulto\_feminino\_de\_handebol\_de\_praia\_nos\_Jogos\_Mundiais\_de\_Praia.pdf | PDF, 1.080.460 bytes | português | científico/adulto feminino | disponível | análise integral.

26 | 1HneFvOwDivBrt3BLDfSMph\_WUT\_REKE\_ | Contextual\_Factors\_and\_Decision-Making\_in\_the\_Behavior\_of\_Finalization\_in\_the\_Positional\_Attack\_in\_Beach\_Handball.pdf | PDF, 2.211.111 bytes | inglês | científico/decisão e ataque | disponível | análise integral.

27 | 1RZI9sNm\_Rbxkis-evgVLVXS\_F4nBWyz2 | 6-metre throw + punishments.pdf | PDF, 4.378.483 bytes | inglês | arbitragem/técnico-normativo | disponível | análise comparativa e suplementar.

28 | 1QBGyl-FTxdMiOYYB\_943z3P2g3MVSdJa | Coaching a winning team.pdf | PDF, 2.961.166 bytes | inglês | treinamento/coaching | disponível | análise técnico-operacional.

29 | 1yBdr98FFXmhobDFzBiiO3-RaFNq2X74m | 2-point goals (spin and in-flight shots)-min.pdf | PDF, 8.462.206 bytes | inglês | técnico-tático | disponível | análise suplementar.

30 | 1Ct4NZTemlmlUHommPnhzSEkCVidTZKuk | Goalkeeper behaviour Special Situations.pdf | PDF, 3.198.461 bytes | inglês | técnico-tático/goleiras | disponível | análise suplementar.

31 | 1gDwFrwfMOOUcdayRNzqZbu-Z532B9SnL | Goalkeeper behaviour inside and outside the goal area-1.pdf | PDF, 3.193.020 bytes | inglês | técnico-tático/goleiras | disponível | análise suplementar.

32 | 1frRfzbb2SNW2hhj06plbOptwnJiE0CVG | Latest trends in defence.pdf | PDF, 1.853.873 bytes | inglês | técnico-tático/defesa | disponível | análise suplementar.

33 | 1nUxK77H9AJoefEuVbOjSHYg-raa-6vVd | Preparation of a national team on the way to a top event\_0.pdf | PDF, 3.394.354 bytes | inglês | treinamento/planejamento | disponível | análise técnico-operacional.

34 | 17DVivqtLG9rHvfUT00VzfczFKEAt7a4Q | Latest trends in attack\_0.pdf | PDF, 5.724.731 bytes | inglês | técnico-tático/ataque | disponível | análise suplementar.

35 | 15cGixSPDNbS2swGbFgg0XyYXZQnfGzdu | Further Eduction course 2017 Gaeta.pdf | PDF, 1.725.506 bytes | inglês | curso/formação | disponível | análise seletiva.

36 | 143mYXG7FqDVjD1x2Hz1EZ96HokHdVrbv | A-BH-Delegate.....pdf | PDF, 1.849.715 bytes | inglês/aparente | arbitragem/delegado | disponível | identificar escopo e analisar.

37 | 1EHgitwAAu857c8SA4CKFd44uvTae7WqC | Beach-Historyfinal.pdf | PDF, 3.771.221 bytes | inglês | histórico | disponível | catalogação e análise contextual.

38 | 1M9gVni-gmPAWQEI986MGnwAesx9mPFfj | The structuring of the defensive phase of beach handball.pdf | PDF, 331.480 bytes | inglês | técnico-tático/defesa | disponível | análise; comparar conteúdo com item 17.

39 | 1SA4vtLZjRzEgwhSynWEaGqSWK\_juJwFV | O jogo ofensivo do handebol de areia estrutura e aspectos técnico-táticos do ataque posicionado.pdf | PDF, 530.858 bytes | português | técnico-tático/ataque | disponível | análise integral.

40 | 1WN96gNV7HiQAPoGDbUrvW0Mit6ZNsOel | Temas Emergentes do Handebol de Praia.pdf | PDF, 1.341.057 bytes | português | científico/técnico | disponível | análise integral ou por capítulos.

41 | 13Oe8vfsR94rH96neo-evGB\_PFxOBs4eb | Tempos de defesa do goleiro de handebol de praia.pdf | PDF, 115.944 bytes | português | científico/goleiras | disponível | análise integral.

42 | 1NGiVLsuFe6PKH1nH4B\_wVJIDDLEjpe85 | Rules of the Game IHF.pdf | PDF, 22.081.473 bytes | inglês/aparente | regra oficial/histórica a datar | disponível | identificar edição, vigência e relação com 2026.

43 | 16zBkB9jsXbElFT8nFR678kXOlAoAazX7 | handebol de praia - SUBSÍDIOS CIENTÍFICOS PARA A COMPREENSÃO DO ESPORTE.pdf | PDF, 4.613.171 bytes | português | obra científica de síntese | disponível | análise integral ou por capítulos.

#### C15.3.1 Suplemento de datas dos metadados

# 01 | criado 2026-06-10T18:44:07.496Z | modificado 2026-06-10T19:05:49.152Z.

# 02 | criado 2026-06-10T18:42:15.733Z | modificado 2026-06-10T18:44:07.938Z.

# 03 | criado 2026-06-10T18:44:11.352Z | modificado 2026-06-10T18:43:49.000Z.

# 04 | criado 2026-06-10T18:42:17.241Z | modificado 2026-06-10T18:42:17.241Z.

# 05 | criado 2026-06-10T16:32:00.334Z | modificado 2026-06-10T18:34:04.805Z.

# 06 | criado 2026-06-10T18:34:02.299Z | modificado 2026-06-10T18:30:19.000Z.

# 07 | criado 2026-06-10T18:34:05.260Z | modificado 2026-06-10T18:24:50.000Z.

# 08 | criado 2026-06-10T18:34:08.364Z | modificado 2026-06-10T18:23:07.000Z.

# 09 | criado 2026-06-10T18:15:29.660Z | modificado 2026-06-10T18:15:55.070Z.

# 10 | criado 2026-06-10T18:34:02.871Z | modificado 2026-06-10T18:12:43.000Z.

# 11 | criado 2026-06-10T16:32:13.476Z | modificado 2026-06-10T16:32:13.476Z.

# 12 | criado 2026-06-10T16:32:12.625Z | modificado 2026-06-10T16:32:12.625Z.

# 13 | criado 2026-06-10T16:32:11.813Z | modificado 2026-06-10T16:32:11.813Z.

# 14 | criado 2026-06-10T16:32:11.261Z | modificado 2026-06-10T16:32:11.261Z.

# 15 | criado 2026-06-14T06:39:34.890Z | modificado 2026-06-10T05:07:37.000Z.

# 16 | criado 2026-06-14T06:39:23.108Z | modificado 2026-06-10T05:00:20.000Z.

# 17 | criado 2026-06-14T06:39:23.079Z | modificado 2026-06-10T04:53:00.000Z.

# 18 | criado 2026-06-14T06:39:22.642Z | modificado 2026-06-10T04:52:10.000Z.

# 19 | criado 2026-06-14T06:39:25.054Z | modificado 2026-06-08T17:27:02.000Z.

# 20 | criado 2026-06-14T06:39:30.583Z | modificado 2026-06-08T17:26:01.000Z.

# 21 | criado 2026-06-14T06:39:32.744Z | modificado 2026-06-08T17:25:23.000Z.

# 22 | criado 2026-06-14T06:40:17.947Z | modificado 2026-05-25T03:05:02.000Z.

# 23 | criado 2026-06-14T06:39:36.192Z | modificado 2026-05-25T02:39:28.000Z.

# 24 | criado 2026-06-14T06:39:36.724Z | modificado 2026-05-25T01:23:18.000Z.

# 25 | criado 2026-06-14T06:40:15.815Z | modificado 2026-05-25T01:22:52.000Z.

# 26 | criado 2026-06-14T06:40:05.241Z | modificado 2026-05-24T23:59:48.000Z.

# 27 | criado 2026-06-14T06:40:08.522Z | modificado 2026-05-24T16:43:25.000Z.

# 28 | criado 2026-06-14T06:40:10.626Z | modificado 2026-05-24T16:43:22.000Z.

# 29 | criado 2026-06-14T06:40:13.889Z | modificado 2026-05-24T16:41:52.000Z.

# 30 | criado 2026-06-14T06:39:37.581Z | modificado 2026-05-24T16:41:49.000Z.

# 31 | criado 2026-06-14T06:39:39.863Z | modificado 2026-05-24T16:41:45.000Z.

# 32 | criado 2026-06-14T06:39:42.192Z | modificado 2026-05-24T16:41:38.000Z.

# 33 | criado 2026-06-14T06:39:44.746Z | modificado 2026-05-24T16:40:30.000Z.

# 34 | criado 2026-06-14T06:39:48.435Z | modificado 2026-05-24T16:39:52.000Z.

# 35 | criado 2026-06-14T06:39:50.683Z | modificado 2026-05-24T16:35:06.000Z.

# 36 | criado 2026-06-14T06:39:52.679Z | modificado 2026-05-24T16:34:58.000Z.

# 37 | criado 2026-06-14T06:39:55.448Z | modificado 2026-05-24T16:34:56.000Z.

# 38 | criado 2026-06-14T06:39:35.812Z | modificado 2026-05-24T16:21:49.000Z.

# 39 | criado 2026-06-14T06:39:36.492Z | modificado 2026-05-24T16:20:24.000Z.

# 40 | criado 2026-06-14T06:39:57.423Z | modificado 2026-05-24T16:15:05.000Z.

# 41 | criado 2026-06-14T06:39:36.411Z | modificado 2026-05-24T16:12:29.000Z.

# 42 | criado 2026-06-14T06:40:02.626Z | modificado 2026-05-24T06:05:38.000Z.

# 43 | criado 2026-06-14T06:40:20.182Z | modificado 2026-05-24T01:31:59.000Z.

### 

### C15.4 Exceções e candidatos a duplicidade

• EXC-F01-001: itens 11, 12, 13 e 14 possuem zero bytes; não podem ser analisados até reposição.

• DUP-F01-001: itens 09 e 10 têm o mesmo tamanho e títulos que indicam a mesma edição inglesa; duplicidade ainda não confirmada.

• DUP-F01-002: itens 17 e 38 têm o mesmo tamanho; o item 17 possui nome genérico e poderá ser cópia do item 38; duplicidade ainda não confirmada.

• O nome com extensão dupla “.pdf.pdf” foi preservado como metadado original e não implica problema de conteúdo.

• Não foram encontrados diretórios filhos; o inventário cobre os itens diretamente presentes na pasta no momento da execução.

### C15.5 Evidências e testes

EVD-F01-001 — listagem do Google Drive da pasta BEACH HANDBALL com 43 itens diretos.

EVD-F01-002 — metadados da pasta confirmando ID, nome e data de modificação.

EVD-F01-003 — reconciliação 43 = 41 PDFs + 2 Markdown = 39 itens não vazios + 4 itens vazios.

EVD-F01-004 — inventário individual com 43 registros e status explícito.

TST-F01-001 — completude da contagem: APROVADO.

TST-F01-002 — unicidade dos IDs: APROVADO.

TST-F01-003 — todos os itens com formato, tamanho, disponibilidade e tratamento: APROVADO.

TST-F01-004 — detecção de arquivos vazios: APROVADO.

TST-F01-005 — identificação de candidatos a duplicidade sem declará-los duplicados prematuramente: APROVADO.

TST-F01-006 — preservação das incertezas de idioma, autoria e classificação: APROVADO.

### C15.6 Decisão e transição

Resultado da ação: PRODUZIDO.

Critério de saída da Fase 1: atendido no nível de inventário — 100% dos itens diretos catalogados com status de tratamento.

Decisão do portão: não autoaprovada; o inventário segue para revisão no Portão A juntamente com autoridade, vigência e cobertura.

Próxima ação controlada: ACT-F02-001 — classificar autoridade, vigência, idioma confirmado, autoria, duplicidade e aplicabilidade das fontes.

Estado da ACT-F02-001: PRONTO.

Dependência satisfeita: ACT-F01-001 PRODUZIDA; a aprovação definitiva do Portão A ocorrerá após a Fase 2.

## C16. EXECUÇÃO DA ACT-F02-001 — AUTORIDADE, VIGÊNCIA E CONTROLE DE VERSÕES DAS FONTES

# 

### C16.1 Registro da ação controlada

# Identificador: ACT-F02-001.

# Nome: classificar autoridade, vigência, idioma confirmado, autoria, duplicidade e aplicabilidade das fontes.

# Objetivo: impedir que fontes antigas, secundárias, locais, científicas ou duplicadas sejam tratadas como regras oficiais vigentes.

# Fase: Fase 2 — Hierarquia, vigência e controle de versões das fontes.

# Subdomínio: governança, autoridade, proveniência e temporalidade das fontes.

# Entradas autorizadas: inventário ACT-F01-001; metadados do Google Drive; conteúdo acessível dos arquivos; hierarquia C3.

# Precondições: ACT-F01-001 PRODUZIDA; 43 itens catalogados; acesso de leitura confirmado.

# Procedimento executado: classificar cada item; priorizar fontes normativas; confirmar atributos pelo conteúdo quando acessível; comparar pares suspeitos; preservar incertezas; registrar precedência e aplicabilidade.

# Saídas: matriz de classificação das 43 fontes; relações de versão e duplicidade; pendências; evidências e testes.

# Responsável pela validação: proprietário do projeto ou responsável humano designado.

# Portão relacionado: Portão A — Fontes.

# Estado resultante: PRODUZIDO, aguardando revisão do Portão A.

# 

### C16.2 Vocabulário de classificação

# Autoridade: A1 = norma oficial IHF; A2 = regulamento nacional de competição; A3 = circular ou esclarecimento local/regional; E1 = evidência científica; T1 = material técnico, educacional ou de treinamento; H1 = fonte histórica/contextual; R1 = registro de proveniência ou página de referência; X1 = indisponível.

# Vigência: VIGENTE; VIGÊNCIA\_LOCAL; POTENCIALMENTE\_SUPERADA; NÃO\_APLICÁVEL; A\_CONFIRMAR; INDISPONÍVEL.

# Aplicabilidade: CRÍTICA; ALTA; MÉDIA; BAIXA; CONTEXTUAL; FORA\_DO\_NÚCLEO.

# Regra de confirmação: “confirmado” decorre de conteúdo legível; “provisório” decorre apenas do título ou metadado e deverá ser fechado na Fase 3.

# 

### C16.3 Matriz individual das fontes

# Formato: item | autoridade | vigência | idioma | autoria/emissor | duplicidade/versão | aplicabilidade.

# 

# 01 | A2 | 2026 declarada; publicação final A\_CONFIRMAR devido a marcas editoriais internas | português confirmado | Confederação Brasileira de Handebol — CBHb | único no acervo | CRÍTICA para regras do Circuito Brasileiro; não substitui regras universais IHF.

# 02 | A3 | VIGÊNCIA\_LOCAL em 2025; POTENCIALMENTE\_SUPERADA pelas regras IHF 2026 | português confirmado | FHERJ; Luiz Filipe Caldas | único | MÉDIA para histórico e interpretação local.

# 03 | tradução derivada de A1 | edição IHF de 1º de março de 2026; datas específicas exigem confronto com o original | português confirmado | IHF; tradução de Luiz Filipe Galvão da Silva Caldas | versão linguística | CRÍTICA para análise em português; o original IHF prevalece em divergências.

# 04 | A3 | circular de 17 de março de 2026, com aplicação informada a partir de 1º de abril de 2026 | português confirmado | FHERJ; Luiz Filipe Caldas | único | ALTA como orientação explicativa, subordinada à IHF.

# 05 | R1 | referência temporal de 2026; NÃO é norma | português e inglês confirmados | compilação baseada em notícia IHF; compilador não identificado | único | ALTA para proveniência e linha temporal.

# 06 | R1 | página de referência; vigência depende dos documentos apontados | português/inglês confirmado | página IHF capturada; autor individual não aplicável | único | MÉDIA para proveniência.

# 07 | A1 | edição oficial IHF de 1º de março de 2026; datas de transição por disposição A\_CONFIRMAR | francês confirmado | International Handball Federation | versão linguística paralela | ALTA para comparação.

# 08 | A1 | edição oficial IHF de 1º de março de 2026; datas de transição por disposição A\_CONFIRMAR | alemão confirmado | International Handball Federation | versão linguística paralela | ALTA para comparação.

# 09 | A1 | edição oficial IHF de 1º de março de 2026; reconciliação necessária entre 1º de abril e 1º de julho de 2026 conforme disposição | inglês confirmado | International Handball Federation | duplicado textual confirmado do item 10 | CRÍTICA; cópia canônica proposta.

# 10 | A1 | mesma edição e condição do item 09 | inglês confirmado | International Handball Federation | duplicado textual confirmado do item 09; identidade binária não testada | REDUNDANTE; manter para rastreabilidade.

# 11 | X1 | INDISPONÍVEL | idioma não confirmável | autoria não confirmável | duplicidade não avaliável | potencial informativo; BLOQUEADO por zero bytes.

# 12 | X1 | INDISPONÍVEL | idioma não confirmável | autoria não confirmável | duplicidade não avaliável | potencial educacional; BLOQUEADO por zero bytes.

# 13 | X1 | INDISPONÍVEL | idioma não confirmável | autoria não confirmável | duplicidade não avaliável | potencial científico; BLOQUEADO por zero bytes.

# 14 | X1 | INDISPONÍVEL | idioma não confirmável | autoria não confirmável | duplicidade não avaliável | potencial arbitragem; BLOQUEADO por zero bytes.

# 15 | E1/T1 provisório | NÃO\_APLICÁVEL como norma; data bibliográfica A\_CONFIRMAR | idioma A\_CONFIRMAR | autoria A\_CONFIRMAR | único por ID | MÉDIA, pendente de identificação bibliográfica.

# 16 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado pelo conteúdo/título | autoria A\_CONFIRMAR | único | MÉDIA/CONTEXTUAL, introdução à modalidade.

# 17 | E1 | publicação de 2021; NÃO\_APLICÁVEL como norma | inglês confirmado | João Paulo Torres Di Gilio; Karen Pereira da Silva; Rafael Pombo Menezes | duplicado textual confirmado do item 38 | ALTA para estrutura defensiva; registro redundante.

# 18 | E1 provisório | NÃO\_APLICÁVEL como norma; data A\_CONFIRMAR | idioma e autoria A\_CONFIRMAR | autoria A\_CONFIRMAR | único | MÉDIA, pendente de identificação.

# 19 | E1 | NÃO\_APLICÁVEL como norma | espanhol confirmado pelo título | autoria A\_CONFIRMAR | único | FORA\_DO\_NÚCLEO; uso apenas comparativo em carga de treinamento.

# 20 | E1 | NÃO\_APLICÁVEL como norma | inglês aparente, confirmação integral pendente | múltiplos autores/anais A\_CONFIRMAR | único | BAIXA/MÉDIA; localizar capítulos pertinentes.

# 21 | E1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria A\_CONFIRMAR | único | ALTA para análise notacional.

# 22 | E1 | NÃO\_APLICÁVEL como norma | português confirmado | autoria A\_CONFIRMAR | único | ALTA para análise de goleiras.

# 23 | E1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria A\_CONFIRMAR | único | ALTA para carga externa.

# 24 | E1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria A\_CONFIRMAR | único | ALTA para categorias de observação técnico-tática.

# 25 | E1 | NÃO\_APLICÁVEL como norma | português confirmado | autoria A\_CONFIRMAR | único | CRÍTICA/ALTA por tratar categoria adulta feminina.

# 26 | E1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria A\_CONFIRMAR | único | ALTA para decisão e ataque posicional.

# 27 | T1 | NÃO\_APLICÁVEL como norma; conteúdo deve ser confrontado com A1 | inglês confirmado | autoria/instituição A\_CONFIRMAR | único | ALTA como material suplementar de arbitragem.

# 28 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria A\_CONFIRMAR | único | ALTA para coaching e operação de equipe.

# 29 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria/instituição A\_CONFIRMAR | único | ALTA para ações de dois pontos.

# 30 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria/instituição A\_CONFIRMAR | único | ALTA para goleiras em situações especiais.

# 31 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria/instituição A\_CONFIRMAR | único | ALTA para comportamento de goleiras.

# 32 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria/instituição A\_CONFIRMAR | único | ALTA para defesa.

# 33 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria A\_CONFIRMAR | único | ALTA para planejamento de seleção/equipe.

# 34 | T1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria/instituição A\_CONFIRMAR | único | ALTA para ataque.

# 35 | T1 | material de 2017; NÃO\_APLICÁVEL como norma | inglês confirmado | autoria/instituição A\_CONFIRMAR | único | MÉDIA; formação histórica/técnica.

# 36 | T1 | NÃO\_APLICÁVEL como norma; edição A\_CONFIRMAR | inglês aparente | autoria/instituição A\_CONFIRMAR | único | MÉDIA/ALTA para delegados e arbitragem.

# 37 | H1 | NÃO\_APLICÁVEL como norma | inglês confirmado | autoria A\_CONFIRMAR | único | CONTEXTUAL.

# 38 | E1 | publicação de 2021; NÃO\_APLICÁVEL como norma | inglês confirmado | João Paulo Torres Di Gilio; Karen Pereira da Silva; Rafael Pombo Menezes | duplicado textual confirmado do item 17; título descritivo favorece esta cópia como canônica | ALTA para estrutura defensiva.

# 39 | E1/T1 | NÃO\_APLICÁVEL como norma | português confirmado | autoria A\_CONFIRMAR | único | ALTA para ataque posicionado.

# 40 | E1/T1 | NÃO\_APLICÁVEL como norma | português confirmado | autores/organizadores A\_CONFIRMAR | único | ALTA, com análise por capítulos.

# 41 | E1 | NÃO\_APLICÁVEL como norma | português confirmado | autoria A\_CONFIRMAR | único | ALTA para desempenho de goleiras.

# 42 | A1 | edição IHF de 1º de março de 2026; datas específicas A\_CONFIRMAR | inglês confirmado | International Handball Federation | candidato a cópia/renderização alternativa dos itens 09/10; extração e tamanho diferem | CRÍTICA, mas redundância exata pendente de comparação de páginas/hash.

# 43 | E1 | NÃO\_APLICÁVEL como norma | português confirmado | autores/organizadores A\_CONFIRMAR | único | ALTA como obra científica de síntese.

# 

### C16.4 Precedência e relações de versão

# 1\. Para regras universais da modalidade, os itens 09/10 e suas versões oficiais 07/08 têm precedência normativa.

# 2\. O item 03 é tradução operacional de alta utilidade, mas não supera o texto oficial IHF.

# 3\. Os itens 04, 05 e 06 documentam atualização e proveniência; não substituem a regra oficial.

# 4\. O item 01 governa especificamente o Circuito Brasileiro 2026 dentro da jurisdição CBHb, desde que sua publicação final seja confirmada.

# 5\. O item 02 é esclarecimento local FHERJ de 2025 e não deve ser projetado automaticamente para competições ou regras de 2026.

# 6\. Fontes E1 e T1 podem originar conceitos, métricas, categorias e hipóteses, nunca obrigações normativas sem fonte A1/A2/A3 competente.

# 7\. Duplicidades textuais confirmadas: 09↔10 e 17↔38. Não foi calculado hash; portanto não se declara identidade binária.

# 8\. O item 42 permanece como provável versão alternativa da edição inglesa 2026, pendente de comparação estrutural.

# 

### C16.5 Pendências e conflitos

# PEN-F02-001 — Confirmar se o regulamento CBHb 2026 é versão oficialmente publicada/final, pois contém marcas editoriais.

# PEN-F02-002 — Reconciliar, por disposição, as datas de eficácia de 1º de abril e 1º de julho de 2026 nas fontes IHF.

# PEN-F02-003 — Obter reposição dos itens 11 a 14, todos com zero bytes.

# PEN-F02-004 — Confirmar autoria, edição e idioma dos itens ainda classificados provisoriamente durante a Fase 3.

# PEN-F02-005 — Comparar o item 42 com os itens 09/10 por páginas ou hash.

# PEN-F02-006 — A duplicidade foi confirmada em nível textual, não binário.

# 

### C16.6 Evidências e testes

# EVD-F02-001 — inventário reconciliado de 43 itens da ACT-F01-001.

# EVD-F02-002 — leitura do cabeçalho e conteúdo das regras oficiais IHF 2026 em inglês, francês e alemão.

# EVD-F02-003 — leitura da tradução portuguesa IHF 2026 e identificação do tradutor.

# EVD-F02-004 — leitura do regulamento CBHb 2026 e identificação da jurisdição e das marcas editoriais.

# EVD-F02-005 — leitura das circulares FHERJ de 2025 e 2026, com emissor, autor e datas.

# EVD-F02-006 — comparação textual dos pares 09/10 e 17/38.

# TST-F02-001 — todos os 43 itens possuem classe de autoridade: APROVADO.

# TST-F02-002 — todos os 43 itens possuem estado de vigência, inclusive A\_CONFIRMAR ou INDISPONÍVEL: APROVADO.

# TST-F02-003 — fontes científicas e técnicas não foram tratadas como normas: APROVADO.

# TST-F02-004 — versões locais e traduções foram subordinadas à fonte competente: APROVADO.

# TST-F02-005 — duplicidades não foram declaradas binárias sem hash: APROVADO.

# TST-F02-006 — incertezas e bloqueios foram preservados: APROVADO.

# 

### C16.7 Decisão e próxima ação

# Resultado da ação: PRODUZIDO.

# Decisão do Portão A: APROVADO\_COM\_RESSALVAS. O inventário e a classificação foram produzidos, mas a aprovação depende da revisão humana e do tratamento das pendências críticas, especialmente publicação final CBHb, datas de eficácia IHF e fontes vazias.

# Próxima ação controlada: ACT-F03-001 — preparar, ler e segmentar integralmente todas as 39 fontes acessíveis, registrar proveniência e fechar atributos bibliográficos pendentes.

# Estado da ACT-F03-001: PRONTO, condicionada às limitações registradas.

# A Fase 4 permanece BLOQUEADA até as Fases 2 e 3 satisfazerem o Portão A.

# 

## C17. EXECUÇÃO DA ACT-F01-002 — RECONCILIAÇÃO DO INVENTÁRIO APÓS ALTERAÇÃO DO ACERVO

## C17.1 Registro da ação controlada

# Identificador: ACT-F01-002.

# Nome: reconciliar o inventário após alteração do acervo.

# Objetivo: atualizar a fotografia documental de FONTES → BEACH HANDBALL após inclusões, substituições e remoções, preservando o histórico da ACT-F01-001.

# Fase: Fase 1 — Inventário integral das fontes.

# Subdomínio: governança, aquisição e controle de mudanças do acervo.

# Entradas autorizadas: pasta FONTES → BEACH HANDBALL, inventário histórico da ACT-F01-001 e metadados atuais do Google Drive.

# Precondições: ACT-F01-001 PRODUZIDA; alteração material do acervo confirmada; acesso de leitura vigente.

# Dependências: ACT-F00-001 VALIDADA.

# Procedimento executado: nova listagem integral; reconciliação quantitativa; comparação por ID com os 43 itens históricos; classificação de permanência, substituição, remoção e inclusão; vinculação das reposições dos arquivos vazios; registro dos documentos adicionados em 31 de julho de 2026; teste de ausência de item sem status.

# Portão relacionado: Portão A — Fontes.

# Estado resultante: PRODUZIDO.

# 

# C17.2 Resultado reconciliado

# Pasta: FONTES → BEACH HANDBALL, ID 1Z0OsR3dHmLMED0KYc\_EE2lD1nEYykzWY.

# Itens atuais: 65.

# Formatos atuais: 60 PDFs, 3 XLSX e 2 Markdown.

# Itens atuais com tamanho maior que zero: 65.

# Itens atuais vazios: 0.

# IDs históricos preservados no acervo: 35.

# IDs históricos ausentes do acervo atual: 8.

# IDs atuais não presentes no inventário histórico: 30.

# Documentos criados em 31 de julho de 2026: 30.

# Reconciliação: 43 históricos − 8 ausentes + 30 novos = 65 atuais.

# 

# C17.3 Inventário atual integral

# Formato: nº | ID | título | formato | tamanho | criado | modificado | status.

# 01 | 1KI\_4F23dkOvDiCEVpTMmrKDsjHxcHO1L | Mini%20Beach%20Handball%20Info%20Sheet%202020.pdf | PDF | 2.225.349 | 2026-07-31T03:42:25.349Z | 2026-07-31T03:42:25.349Z | ATUAL/NOVO; substitui item histórico vazio 11.

# 02 | 1p4cK4IIY9EwD45lB8BsQ03u-LYQpQLji | Ultimate%20School%20Handball%202025.pdf | PDF | 11.374.314 | 2026-07-31T03:41:32.052Z | 2026-07-31T03:41:32.052Z | ATUAL/NOVO; substitui item histórico vazio 12.

# 03 | 1\_nFkwAFUY6\_1iVcWIvFLAgN\_vlV5B57L | Refereeing%20In%20Beach%20Handball.pdf | PDF | 2.967.257 | 2026-07-31T03:40:02.236Z | 2026-07-31T03:40:02.236Z | ATUAL/NOVO; substitui item histórico vazio 14.

# 04 | 1EoqJMqroFkxb7Dljqd0f2HExopBbIV3e | understanding-psyhological-pressure-in-beach-handball-shootouts.pdf | PDF | 1.702.276 | 2026-07-31T03:34:13.597Z | 2026-07-31T03:34:13.597Z | ATUAL/NOVO; substitui item histórico vazio 13.

# 05 | 1KoA-RHtH0dD5tL7vB9pnn75-2bz0N\_Kl | CEPRAEA.pdf | PDF | 32.820.680 | 2026-07-31T02:51:40.581Z | 2026-07-31T02:51:40.581Z | ATUAL/NOVO.

# 06 | 1VTGjxKU73z\_iu1ntN4m8qWgmnxS\_TQrk | Convocação Oficial Rosário 2026.pdf | PDF | 475.988 | 2026-07-31T02:51:25.145Z | 2026-07-31T02:51:25.145Z | ATUAL/NOVO.

# 07 | 1I354EemsKiOIXjpSAw8RK7Ua1WSjY7ny | OFICIO 52026.pdf | PDF | 493.610 | 2026-07-31T02:51:24.779Z | 2026-07-31T02:51:24.779Z | ATUAL/NOVO.

# 08 | 1aR9MOhC40ZIP\_yTKKjmLmXZEQyUjMKI\_ | REGULAMENTO GERAL CAMPEONATO CARIOCA DE HANDEBOL DE PRAIA 2026.pdf | PDF | 436.043 | 2026-07-31T02:51:23.904Z | 2026-07-31T02:51:23.904Z | ATUAL/NOVO.

# 09 | 1GmqY41nfH8Qgfj8ehI97VSWol27sm7Tf | Mudanças nas Regras de Handebol de Praia 2026.pdf | PDF | 201.427 | 2026-07-31T02:51:23.523Z | 2026-07-31T02:51:23.523Z | ATUAL/NOVO; substitui ID histórico 1376ozyK5bKY\_xgtEmjKDjWKQzQp0YjNt.

# 10 | 17LIvxbIoD-2MWDw9COIgvqQSViEXBRIm | EQUIPES PARA O CAMPEONATO CARIOCA DE HANDEBOL DE PRAIA 2026\_Rev\_28\_02\_2026.pdf | PDF | 315.267 | 2026-07-31T02:51:23.493Z | 2026-07-31T02:51:23.493Z | ATUAL/NOVO.

# 11 | 1krs0n6vZs8LRLL55Soo0WfOi23A2tN7N | TABELA 1 ETAPA ADULTO 26.05.26.pdf | PDF | 232.903 | 2026-07-31T02:51:23.005Z | 2026-07-31T02:51:23.005Z | ATUAL/NOVO.

# 12 | 1x4\_-b1f1Ql55IK2QYZ9CLLBz3uyoS1Ww | RELAÇÃO NOMINAL PRAIA 2026.pdf | PDF | 81.038 | 2026-07-31T02:51:22.803Z | 2026-07-31T02:51:22.803Z | ATUAL/NOVO.

# 13 | 1nRtGbXGUMeKv61qLZ1W0CkYzQv7\_xPKl | Resultado1 ETAPA ADULTO 26.05.26.pdf | PDF | 238.612 | 2026-07-31T02:51:22.746Z | 2026-07-31T02:51:22.746Z | ATUAL/NOVO.

# 14 | 1arSTonBG2Vs31cPL6axREzx-hC79gSB1 | Datas CIRCUITO 2026.pdf | PDF | 133.622 | 2026-07-31T02:51:22.732Z | 2026-07-31T02:51:22.732Z | ATUAL/NOVO.

# 15 | 1HAIxQU3wXsNGpctu3Yjl8XN\_afr5HIib | Boletim\_01\_CircuitoBrasileiro\_3aEtapa\_2026.pdf | PDF | 1.743.263 | 2026-07-31T02:51:21.046Z | 2026-07-31T02:51:21.046Z | ATUAL/NOVO.

# 16 | 1xQYAdUYkAGtdt6pctG0DTCF6\_Unk5kCq | TABELA 3 ETAPA ADULTO MASC FEM 05 07 26.pdf | PDF | 178.575 | 2026-07-31T02:51:20.850Z | 2026-07-31T02:51:20.850Z | ATUAL/NOVO.

# 17 | 1sG4Uzk2119herbmrl0mpCWjNmFb7M1EH | RELACAO NOMINAL CEPRAEA - 2ª ETAPA.pdf | PDF | 255.700 | 2026-07-31T02:51:20.835Z | 2026-07-31T02:51:20.835Z | ATUAL/NOVO.

# 18 | 1PcVyCwMj8U6iOrmEED-toD8hUZBuhZ9v | Resultado 3 ETAPA ADULTO MASC FEM.pdf | PDF | 157.172 | 2026-07-31T02:51:20.752Z | 2026-07-31T02:51:20.752Z | ATUAL/NOVO.

# 19 | 1QCUoRfGIvRPOJZgoybV8d3ClXkoGmHjb | Tabela 2 ETAPA ADULTO MAS FEM 31.05.26.pdf | PDF | 171.002 | 2026-07-31T02:51:20.729Z | 2026-07-31T02:51:20.729Z | ATUAL/NOVO.

# 20 | 1vbhZ2-YnnhkaoiI5nK5rjTnouawX4XoN | COLOCAÇÃO PONTUAÇÃO NAS ETAPAS 2026.pdf | PDF | 150.149 | 2026-07-31T02:51:20.589Z | 2026-07-31T02:51:20.589Z | ATUAL/NOVO.

# 21 | 1mqriO11izHjl2-Xy8f1aLf2mI6D8XsIm | CERTA TABELA 3 ETAPA ADULTO MASC FEM.pdf | PDF | 174.019 | 2026-07-31T02:51:20.526Z | 2026-07-31T02:51:20.526Z | ATUAL/NOVO.

# 22 | 1lEqDQGL0ZzUtAOZuqtT4wZgZjNxqF8Vc | FINAIS 2025.pdf.pdf | PDF | 19.822.805 | 2026-07-31T02:47:28.283Z | 2026-07-31T02:47:28.283Z | ATUAL/NOVO.

# 23 | 1e8PXOtmQSzHbiRur0imKC8epq5KphMff | É Hora do Show! .pdf | PDF | 1.828.673 | 2026-07-31T02:46:53.424Z | 2026-07-31T02:46:53.424Z | ATUAL/NOVO.

# 24 | 13DIL2fO2ev0M5GHK5TzPe4Y3bsq6wVFV | REUNIÃO PÓS FASE FINAL.pdf | PDF | 296.414 | 2026-07-31T02:46:37.884Z | 2026-07-31T02:46:37.884Z | ATUAL/NOVO.

# 25 | 18Txf8nXmK--9UY7NqKMcs1PI4Ext-5zc | Finais João Pessoa 25.xlsx | XLSX | 27.363 | 2026-07-31T02:46:37.743Z | 2026-07-31T02:46:37.743Z | ATUAL/NOVO.

# 26 | 1Liwv3PKcJp7ymvAw9eckUb66HOM64Dk4 | GUIA CBHBPRAIA 2026.pdf.pdf.pdf | PDF | 13.595.728 | 2026-07-31T02:44:55.605Z | 2026-07-31T02:44:55.605Z | ATUAL/NOVO.

# 27 | 1xlV6C\_bLXVbipKLwPxpBJqnZAiohmK\_x | CEPRAEA JULHO 2026.pdf | PDF | 348.423 | 2026-07-31T02:44:46.856Z | 2026-07-31T02:44:46.856Z | ATUAL/NOVO.

# 28 | 1NSwNjUfvnZEKAKxlJR4lDSHJE5hjzIv5 | EQUIPES BEACH 26 - equipes.xlsx | XLSX | 9.713 | 2026-07-31T02:44:46.767Z | 2026-07-31T02:44:46.767Z | ATUAL/NOVO.

# 29 | 15pumu2CMTiPeAwP0jxNplKd2uLQL0iYt | Regras de Handebol de Praia 2026 - Tradução 29 de maio de 2026.pdf | PDF | 15.422.591 | 2026-07-31T02:38:40.671Z | 2026-07-31T02:38:40.671Z | ATUAL/NOVO; substitui ID histórico 1scHN1330ZX6EqvgF2ld9-lfs1hrs\_\_Im.

# 30 | 1CJ4Uybko9zLuF1g2NReTQxOvxMQxOQ71 | Relacao Nominal 2025.xlsx | XLSX | 49.114 | 2026-07-31T02:36:16.908Z | 2026-07-31T02:36:16.908Z | ATUAL/NOVO.

# 31 | 1MXLOcWY9r1RdQ6zKWA3qI5AJOfHkguT2 | regulamento\_cbhb\_2026.pdf | PDF | 6.385.991 | 2026-06-10T18:44:07.496Z | 2026-06-10T19:05:49.152Z | ATUAL/PRESERVADO.

# 32 | 1nL49p72AVybqNu422FJPycld2nmejoIG | Esclarecimentos regras de jogo.pdf | PDF | 147.695 | 2026-06-10T18:42:15.733Z | 2026-06-10T18:44:07.938Z | ATUAL/PRESERVADO.

# 33 | 1WTB7ihMOkNtUXsrl67yAyy5tUvAccRt4 | atualizacoes\_ihf\_2026.md | Markdown | 11.803 | 2026-06-10T16:32:00.334Z | 2026-06-10T18:34:04.805Z | ATUAL/PRESERVADO.

# 34 | 10UvC1U2ef3AePzZqTXBBqi57AlKA4WM- | pagina\_ihf\_rules\_beach\_handball.md | Markdown | 768 | 2026-06-10T18:34:02.299Z | 2026-06-10T18:30:19.000Z | ATUAL/PRESERVADO.

# 35 | 1nCp6EXVpBMMgDgi8od2sUUMoFEI90hGm | regras\_ihf\_beach\_handball\_2026\_fr.pdf.pdf | PDF | 2.343.407 | 2026-06-10T18:34:05.260Z | 2026-06-10T18:24:50.000Z | ATUAL/PRESERVADO.

# 36 | 1c5NWDpXgYhNFSobOTgLQ7l5ZnaXrpcxU | regras\_ihf\_beach\_handball\_2026\_de.pdf.pdf | PDF | 2.224.510 | 2026-06-10T18:34:08.364Z | 2026-06-10T18:23:07.000Z | ATUAL/PRESERVADO.

# 37 | 1xf\_td5UAFtvegx2i7kcvBby-VbZdtXaq | regras\_ihf\_beach\_handball\_2026\_en.pdf.pdf | PDF | 1.948.878 | 2026-06-10T18:34:02.871Z | 2026-06-10T18:12:43.000Z | ATUAL/PRESERVADO; cópia inglesa mantida.

# 38 | 1\_udt6wooR9Nnq\_BaJB2rgr2-lW0UVOO1 | 20070912183144claudia\_monteiro2.pdf | PDF | 1.274.901 | 2026-06-14T06:39:34.890Z | 2026-06-10T05:07:37.000Z | ATUAL/PRESERVADO.

# 39 | 12XNAy1uG-xpDzvRSTvFIWNJ-4jGSOmMQ | IntroductionToBeachHandball.pdf | PDF | 1.306.484 | 2026-06-14T06:39:23.108Z | 2026-06-10T05:00:20.000Z | ATUAL/PRESERVADO.

# 40 | 1wmoXa9uaLgFbGpt7kUstfbTsK-2Tl\_R\_ | Art 135.pdf | PDF | 204.626 | 2026-06-14T06:39:22.642Z | 2026-06-10T04:52:10.000Z | ATUAL/PRESERVADO.

# 41 | 1cUBMm5IOeJWU2yOgbuAArPkvrlUBsYhd | CONTROLDEVOLUMENDEENTRENAMIENTOENJUGADORESMEXICANOSDEFUTBOLDETERCERADIVISION\_Revista34.pdf | PDF | 2.058.175 | 2026-06-14T06:39:25.054Z | 2026-06-08T17:27:02.000Z | ATUAL/PRESERVADO.

# 42 | 12mwIXjhKLvxRUtE7kbiB2c4UpCZ5WcIN | KinesiologyProceedingsBook6th-2011.pdf | PDF | 23.830.437 | 2026-06-14T06:39:30.583Z | 2026-06-08T17:26:01.000Z | ATUAL/PRESERVADO.

# 43 | 1It2a7dYCq8sEbih2oOB41eucwNo2Yhm7 | Notational-analysis-of-be.pdf | PDF | 3.682.373 | 2026-06-14T06:39:32.744Z | 2026-06-08T17:25:23.000Z | ATUAL/PRESERVADO.

# 44 | 1IZqfCOtwIRnlw6AYsurHfp8V5nn\_2N8b | Estudo das ações do guarda redes de andebol de praia através da análise.pdf | PDF | 1.383.314 | 2026-06-14T06:40:17.947Z | 2026-05-25T03:05:02.000Z | ATUAL/PRESERVADO.

# 45 | 1CtwKtYgfSVGNuLlml90HQVxzDYype6Nm | External Load Analysis in Beach Handball.pdf | PDF | 665.315 | 2026-06-14T06:39:36.192Z | 2026-05-25T02:39:28.000Z | ATUAL/PRESERVADO.

# 46 | 1wMSMDrbsagansqpWRG6SGNR606zC4Ccg | DEVELOPMENT\_OF\_AN\_INSTRUMENT\_FOR\_THE\_OBSERVATION\_OF\_COLLECTIVE\_TACTICAL\_PROCEDURES\_OF\_POSITIONAL\_ATTACK\_IN\_BEACH\_HANDBALL.pdf | PDF | 473.513 | 2026-06-14T06:39:36.724Z | 2026-05-25T01:23:18.000Z | ATUAL/PRESERVADO.

# 47 | 1XQ\_0SZ-cq0N0OOd6myn9OGqU\_hxUXaGe | A\_importância\_das\_posições\_dos\_passes\_para\_arremessos\_em\_gol\_de\_atletas\_da\_categoria\_adulto\_feminino\_de\_handebol\_de\_praia\_nos\_Jogos\_Mundiais\_de\_Praia.pdf | PDF | 1.080.460 | 2026-06-14T06:40:15.815Z | 2026-05-25T01:22:52.000Z | ATUAL/PRESERVADO.

# 48 | 1HneFvOwDivBrt3BLDfSMph\_WUT\_REKE\_ | Contextual\_Factors\_and\_Decision-Making\_in\_the\_Behavior\_of\_Finalization\_in\_the\_Positional\_Attack\_in\_Beach\_Handball.pdf | PDF | 2.211.111 | 2026-06-14T06:40:05.241Z | 2026-05-24T23:59:48.000Z | ATUAL/PRESERVADO.

# 49 | 1RZI9sNm\_Rbxkis-evgVLVXS\_F4nBWyz2 | 6-metre throw + punishments.pdf | PDF | 4.378.483 | 2026-06-14T06:40:08.522Z | 2026-05-24T16:43:25.000Z | ATUAL/PRESERVADO.

# 50 | 1QBGyl-FTxdMiOYYB\_943z3P2g3MVSdJa | Coaching a winning team.pdf | PDF | 2.961.166 | 2026-06-14T06:40:10.626Z | 2026-05-24T16:43:22.000Z | ATUAL/PRESERVADO.

# 51 | 1yBdr98FFXmhobDFzBiiO3-RaFNq2X74m | 2-point goals (spin and in-flight shots)-min.pdf | PDF | 8.462.206 | 2026-06-14T06:40:13.889Z | 2026-05-24T16:41:52.000Z | ATUAL/PRESERVADO.

# 52 | 1Ct4NZTemlmlUHommPnhzSEkCVidTZKuk | Goalkeeper behaviour Special Situations.pdf | PDF | 3.198.461 | 2026-06-14T06:39:37.581Z | 2026-05-24T16:41:49.000Z | ATUAL/PRESERVADO.

# 53 | 1gDwFrwfMOOUcdayRNzqZbu-Z532B9SnL | Goalkeeper behaviour inside and outside the goal area-1.pdf | PDF | 3.193.020 | 2026-06-14T06:39:39.863Z | 2026-05-24T16:41:45.000Z | ATUAL/PRESERVADO.

# 54 | 1frRfzbb2SNW2hhj06plbOptwnJiE0CVG | Latest trends in defence.pdf | PDF | 1.853.873 | 2026-06-14T06:39:42.192Z | 2026-05-24T16:41:38.000Z | ATUAL/PRESERVADO.

# 55 | 1nUxK77H9AJoefEuVbOjSHYg-raa-6vVd | Preparation of a national team on the way to a top event\_0.pdf | PDF | 3.394.354 | 2026-06-14T06:39:44.746Z | 2026-05-24T16:40:30.000Z | ATUAL/PRESERVADO.

# 56 | 17DVivqtLG9rHvfUT00VzfczFKEAt7a4Q | Latest trends in attack\_0.pdf | PDF | 5.724.731 | 2026-06-14T06:39:48.435Z | 2026-05-24T16:39:52.000Z | ATUAL/PRESERVADO.

# 57 | 15cGixSPDNbS2swGbFgg0XyYXZQnfGzdu | Further Eduction course 2017 Gaeta.pdf | PDF | 1.725.506 | 2026-06-14T06:39:50.683Z | 2026-05-24T16:35:06.000Z | ATUAL/PRESERVADO.

# 58 | 143mYXG7FqDVjD1x2Hz1EZ96HokHdVrbv | A-BH-Delegate.....pdf | PDF | 1.849.715 | 2026-06-14T06:39:52.679Z | 2026-05-24T16:34:58.000Z | ATUAL/PRESERVADO.

# 59 | 1EHgitwAAu857c8SA4CKFd44uvTae7WqC | Beach-Historyfinal.pdf | PDF | 3.771.221 | 2026-06-14T06:39:55.448Z | 2026-05-24T16:34:56.000Z | ATUAL/PRESERVADO.

# 60 | 1M9gVni-gmPAWQEI986MGnwAesx9mPFfj | The structuring of the defensive phase of beach handball.pdf | PDF | 331.480 | 2026-06-14T06:39:35.812Z | 2026-05-24T16:21:49.000Z | ATUAL/PRESERVADO; cópia descritiva mantida.

# 61 | 1SA4vtLZjRzEgwhSynWEaGqSWK\_juJwFV | O jogo ofensivo do handebol de areia estrutura e aspectos técnico-táticos do ataque posicionado.pdf | PDF | 530.858 | 2026-06-14T06:39:36.492Z | 2026-05-24T16:20:24.000Z | ATUAL/PRESERVADO.

# 62 | 1WN96gNV7HiQAPoGDbUrvW0Mit6ZNsOel | Temas Emergentes do Handebol de Praia.pdf | PDF | 1.341.057 | 2026-06-14T06:39:57.423Z | 2026-05-24T16:15:05.000Z | ATUAL/PRESERVADO.

# 63 | 13Oe8vfsR94rH96neo-evGB\_PFxOBs4eb | Tempos de defesa do goleiro de handebol de praia.pdf | PDF | 115.944 | 2026-06-14T06:39:36.411Z | 2026-05-24T16:12:29.000Z | ATUAL/PRESERVADO.

# 64 | 1NGiVLsuFe6PKH1nH4B\_wVJIDDLEjpe85 | Rules of the Game IHF.pdf | PDF | 22.081.473 | 2026-06-14T06:40:02.626Z | 2026-05-24T06:05:38.000Z | ATUAL/PRESERVADO.

# 65 | 16zBkB9jsXbElFT8nFR678kXOlAoAazX7 | handebol de praia - SUBSÍDIOS CIENTÍFICOS PARA A COMPREENSÃO DO ESPORTE.pdf | PDF | 4.613.171 | 2026-06-14T06:40:20.182Z | 2026-05-24T01:31:59.000Z | ATUAL/PRESERVADO.

# 

# C17.4 Histórico dos oito IDs ausentes

# SUBSTITUÍDO | 1scHN1330ZX6EqvgF2ld9-lfs1hrs\_\_Im | tradução IHF em português | substituto atual: 15pumu2CMTiPeAwP0jxNplKd2uLQL0iYt.

# SUBSTITUÍDO | 1376ozyK5bKY\_xgtEmjKDjWKQzQp0YjNt | Mudanças nas Regras de Handebol de Praia 2026 | substituto atual: 1GmqY41nfH8Qgfj8ehI97VSWol27sm7Tf.

# REMOVIDO\_DO\_ACERVO | 1S-OSzrMYR0CkUi2YC2wV8DQL3QgtVRJD | regras IHF inglesas | duplicata removida; 1xf\_td5UAFtvegx2i7kcvBby-VbZdtXaq permanece.

# SUBSTITUÍDO | 1yzivnYq7I3MybEUV3rCvjpwet8PjvSL- | mini\_beach\_handball\_info\_sheet.pdf, 0 bytes | substituto atual: 1KI\_4F23dkOvDiCEVpTMmrKDsjHxcHO1L.

# SUBSTITUÍDO | 1Ydw7Fs0rVp1dbVsLte6lfa196LSbUVco | ultimate\_school\_handball\_2025.pdf, 0 bytes | substituto atual: 1p4cK4IIY9EwD45lB8BsQ03u-LYQpQLji.

# SUBSTITUÍDO | 170GBYtS4dqs3Qox53\_GsPA-dsdLTbxhg | shootout\_psychological\_pressure.pdf, 0 bytes | substituto atual: 1EoqJMqroFkxb7Dljqd0f2HExopBbIV3e.

# SUBSTITUÍDO | 1DtO17h9BnqUTOVuXn8nAVNRuvqzHmvZv | refereeing\_beach\_handball.pdf, 0 bytes | substituto atual: 1\_nFkwAFUY6\_1iVcWIvFLAgN\_vlV5B57L.

# REMOVIDO\_DO\_ACERVO | 1JktKke-jUmyNsGFDdYHjyUwCCrlgM4Y1 | download.pdf | duplicata removida; 1M9gVni-gmPAWQEI986MGnwAesx9mPFfj permanece.

# 

# C17.5 Documentos adicionados em 31 de julho de 2026

# Foram registrados como ATUAL/NOVO os itens 01 a 30 do inventário atual. Quatro são reposições vinculadas a arquivos vazios históricos; dois substituem IDs antigos com o mesmo papel documental; os demais são inclusões sem antecessor registrado na ACT-F01-001.

# 

# C17.6 Evidências e testes da Fase 1 atualizados

# EVD-F01-006 — listagem atual do Google Drive com 65 itens diretos.

# EVD-F01-007 — reconciliação quantitativa 43 − 8 + 30 = 65.

# EVD-F01-008 — inventário atual com 65 IDs únicos e status explícito.

# EVD-F01-009 — vínculo de quatro reposições válidas aos antigos PDFs de zero bytes.

# EVD-F01-010 — registro histórico dos oito IDs ausentes sem apagamento da fotografia anterior.

# TST-F01-007 — contagem atual reconciliada: APROVADO.

# TST-F01-008 — unicidade dos 65 IDs atuais: APROVADO.

# TST-F01-009 — todos os itens atuais possuem nome, formato, tamanho, datas e STATUS: RASCUNHO.

# TST-F01-010 — ausência de arquivo atual com zero bytes: APROVADO.

# TST-F01-011 — todos os 30 documentos criados em 31 de julho de 2026 foram registrados: APROVADO.

# TST-F01-012 — nenhum item atual ficou sem STATUS: RASCUNHO.

# 

# C17.7 Decisão e próxima ação

# Resultado da ACT-F01-002: PRODUZIDO.

# A ACT-F01-001 permanece como fotografia histórica e não é sobrescrita.

# A matriz da ACT-F02-001 permanece histórica e DESATUALIZADA em relação ao acervo de 65 itens.

# Próxima ação controlada: ACT-F02-002 — atualizar autoridade, vigência, idioma, autoria, duplicidade e aplicabilidade das 65 fontes atuais.

# Estado da ACT-F02-002: PRONTO.

# Estado da ACT-F03-001: BLOQUEADO até a conclusão da ACT-F02-002.

# Portão A: PENDENTE.

# 

## C18. EXECUÇÃO DA ACT-F02-002 — ATUALIZAÇÃO DE AUTORIDADE, VIGÊNCIA E APLICABILIDADE DO ACERVO RECONCILIADO

# C18.1 Registro da ação controlada

# Identificador: ACT-F02-002.

# Nome: atualizar autoridade, vigência, idioma, autoria, duplicidade e aplicabilidade do acervo reconciliado.

# Objetivo: substituir operacionalmente a matriz desatualizada da ACT-F02-001 por uma classificação que cubra os 65 itens atuais de FONTES → BEACH HANDBALL, sem transformar registros operacionais, estudos ou materiais técnicos em normas.

# Entradas: ACT-F01-002; matriz histórica ACT-F02-001; metadados dos 65 itens; conteúdo legível das fontes prioritárias.

# Procedimento: transportar classificações ainda válidas dos 35 IDs preservados; reclassificar IDs substitutos; classificar os 30 itens novos; registrar confiança e pendências; revisar precedência, duplicidade e aplicabilidade.

# Estado resultante: PRODUZIDO.

# Portão relacionado: Portão A — Fontes.

# 

# C18.2 Vocabulário

# A1 = regra oficial IHF; A2 = norma/regulamento CBHb; A3 = norma, circular ou regulamento FHERJ; O1 = registro oficial operacional; O2 = registro operacional de equipe/competição; E1 = evidência científica; T1 = material técnico/educacional; H1 = histórico/contextual; R1 = proveniência; P1 = documento interno do projeto/equipe.

# Vigência: VIGENTE; VIGÊNCIA\_LOCAL; EVENTO\_2026; HISTÓRICO; NÃO\_APLICÁVEL\_COMO\_NORMA; A\_CONFIRMAR.

# Confiança: C = confirmada por conteúdo; P = provisória por título/metadado, a fechar na Fase 3.

# 

# C18.3 Matriz dos 65 itens atuais

# Formato: nº | ID | classe | vigência | idioma | autoria/emissor | duplicidade/versão | aplicabilidade | confiança.

# 01 | 1KI\_4F23dkOvDiCEVpTMmrKDsjHxcHO1L | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | emissor a confirmar | substitui fonte vazia histórica | MÉDIA, iniciação/ensino | P.

# 02 | 1p4cK4IIY9EwD45lB8BsQ03u-LYQpQLji | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | emissor a confirmar | substitui fonte vazia histórica | MÉDIA, ensino escolar | P.

# 03 | 1\_nFkwAFUY6\_1iVcWIvFLAgN\_vlV5B57L | T1/A3 a confirmar | A\_CONFIRMAR | inglês | emissor a confirmar | substitui fonte vazia histórica | ALTA, arbitragem | P.

# 04 | 1EoqJMqroFkxb7Dljqd0f2HExopBbIV3e | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | substitui fonte vazia histórica | ALTA, pressão psicológica no shoot-out | P.

# 05 | 1KoA-RHtH0dD5tL7vB9pnn75-2bz0N\_Kl | P1 | A\_CONFIRMAR | português aparente | CEPRAEA a confirmar | único | ALTA para requisitos internos, sem autoridade normativa | P.

# 06 | 1VTGjxKU73z\_iu1ntN4m8qWgmnxS\_TQrk | O1 | EVENTO\_2026 | português | CBHb; Presidência e Diretoria Geral de Handebol de Praia | único | ALTA, convocação adulta feminina e papéis | C.

# 07 | 1I354EemsKiOIXjpSAw8RK7Ua1WSjY7ny | O1/A2 operacional | EVENTO\_2026 | português | CBHb; Wellington N. A. Esteves e Felipe Rêgo Barros | único | ALTA, inscrições e calendário da Copa Brasil | C.

# 08 | 1aR9MOhC40ZIP\_yTKKjmLmXZEQyUjMKI\_ | A3 | VIGÊNCIA\_LOCAL 2026 | português | FHERJ | Rev.01, 01/03/2026 | CRÍTICA para Circuito Estadual RJ | C.

# 09 | 1GmqY41nfH8Qgfj8ehI97VSWol27sm7Tf | A3 | VIGÊNCIA\_LOCAL 2026 | português | FHERJ/Luiz Filipe Caldas | substitui ID histórico equivalente | ALTA, interpretação subordinada à IHF | C por transporte da ACT-F02-001.

# 10 | 17LIvxbIoD-2MWDw9COIgvqQSViEXBRIm | O1 | EVENTO\_2026 | português | FHERJ a confirmar | único | MÉDIA, cadastro de equipes | P.

# 11 | 1krs0n6vZs8LRLL55Soo0WfOi23A2tN7N | O1 | EVENTO\_2026 | português | FHERJ a confirmar | único | MÉDIA, tabela de jogos | P.

# 12 | 1x4\_-b1f1Ql55IK2QYZ9CLLBz3uyoS1Ww | O2 | EVENTO\_2026 | português | emissor a confirmar | único | ALTA, relação nominal e dados pessoais | P.

# 13 | 1nRtGbXGUMeKv61qLZ1W0CkYzQv7\_xPKl | O1 | EVENTO\_2026 | português | FHERJ a confirmar | único | MÉDIA, resultados | P.

# 14 | 1arSTonBG2Vs31cPL6axREzx-hC79gSB1 | O1 | EVENTO\_2026 | português | CBHb/FHERJ a confirmar | único | MÉDIA, calendário | P.

# 15 | 1HAIxQU3wXsNGpctu3Yjl8XN\_afr5HIib | O1/A2 operacional | EVENTO\_2026 | português | CBHb | único | ALTA, boletim de etapa | P.

# 16 | 1xQYAdUYkAGtdt6pctG0DTCF6\_Unk5kCq | O1 | EVENTO\_2026 | português | FHERJ a confirmar | versão de tabela; relação com item 21 a confirmar | MÉDIA | P.

# 17 | 1sG4Uzk2119herbmrl0mpCWjNmFb7M1EH | O2/P1 | EVENTO\_2026 | português | CEPRAEA | único | ALTA, elenco inscrito e dados pessoais | P.

# 18 | 1PcVyCwMj8U6iOrmEED-toD8hUZBuhZ9v | O1 | EVENTO\_2026 | português | FHERJ a confirmar | único | MÉDIA, resultados | P.

# 19 | 1QCUoRfGIvRPOJZgoybV8d3ClXkoGmHjb | O1 | EVENTO\_2026 | português | FHERJ a confirmar | único | MÉDIA, tabela de jogos | P.

# 20 | 1vbhZ2-YnnhkaoiI5nK5rjTnouawX4XoN | O1 | EVENTO\_2026 | português | FHERJ a confirmar | único atual | ALTA, pontuação/classificação | P.

# 21 | 1mqriO11izHjl2-Xy8f1aLf2mI6D8XsIm | O1 | EVENTO\_2026 | português | FHERJ a confirmar | provável correção/versão da tabela da 3ª etapa | MÉDIA | P.

# 22 | 1lEqDQGL0ZzUtAOZuqtT4wZgZjNxqF8Vc | H1/O1 | HISTÓRICO 2025 | português aparente | CBHb/organização a confirmar | único | MÉDIA, fatos de competição | P.

# 23 | 1e8PXOtmQSzHbiRur0imKC8epq5KphMff | P1/T1 | A\_CONFIRMAR | português | autoria a confirmar | único | MÉDIA, conteúdo interno/técnico a identificar | P.

# 24 | 13DIL2fO2ev0M5GHK5TzPe4Y3bsq6wVFV | P1 | HISTÓRICO/2026 a confirmar | português | CEPRAEA a confirmar | único | ALTA, decisões e retrospectiva da equipe | P.

# 25 | 18Txf8nXmK--9UY7NqKMcs1PI4Ext-5zc | H1/O2 | HISTÓRICO 2025 | português aparente | autoria a confirmar | único | MÉDIA, dados tabulares de finais | P.

# 26 | 1Liwv3PKcJp7ymvAw9eckUb66HOM64Dk4 | O1/A2 operacional | EVENTO\_2026 | português | CBHb/Diretoria de Handebol de Praia | único | ALTA, calendário, inscrições, uniformes e organização | C.

# 27 | 1xlV6C\_bLXVbipKLwPxpBJqnZAiohmK\_x | P1 | EVENTO\_2026 | português | CEPRAEA a confirmar | único | ALTA, operação da equipe | P.

# 28 | 1NSwNjUfvnZEKAKxlJR4lDSHJE5hjzIv5 | O2 | EVENTO\_2026 | português aparente | autoria a confirmar | único atual | ALTA, cadastro de equipes | P.

# 29 | 15pumu2CMTiPeAwP0jxNplKd2uLQL0iYt | tradução derivada de A1 | edição IHF 2026 | português | IHF; tradução de Luiz Filipe Galvão da Silva Caldas | substitui ID histórico da mesma tradução | CRÍTICA; original IHF prevalece | C por transporte.

# 30 | 1CJ4Uybko9zLuF1g2NReTQxOvxMQxOQ71 | H1/O2 | HISTÓRICO 2025 | português aparente | autoria a confirmar | único | ALTA, relação nominal e dados pessoais | P.

# 31 | 1MXLOcWY9r1RdQ6zKWA3qI5AJOfHkguT2 | A2 | 2026, publicação final A\_CONFIRMAR | português | CBHb | único | CRÍTICA, Circuito Brasileiro | C.

# 32 | 1nL49p72AVybqNu422FJPycld2nmejoIG | A3 | VIGÊNCIA\_LOCAL 2025; potencialmente superada | português | FHERJ/Luiz Filipe Caldas | único | MÉDIA | C.

# 33 | 1WTB7ihMOkNtUXsrl67yAyy5tUvAccRt4 | R1 | referência 2026 | português/inglês | compilador não identificado | único | ALTA, proveniência | C.

# 34 | 10UvC1U2ef3AePzZqTXBBqi57AlKA4WM- | R1 | depende das fontes apontadas | português/inglês | página IHF capturada | único | MÉDIA | C.

# 35 | 1nCp6EXVpBMMgDgi8od2sUUMoFEI90hGm | A1 | IHF 2026 | francês | IHF | versão linguística | ALTA, comparação | C.

# 36 | 1c5NWDpXgYhNFSobOTgLQ7l5ZnaXrpcxU | A1 | IHF 2026 | alemão | IHF | versão linguística | ALTA, comparação | C.

# 37 | 1xf\_td5UAFtvegx2i7kcvBby-VbZdtXaq | A1 | IHF 2026 | inglês | IHF | cópia inglesa canônica atual | CRÍTICA | C.

# 38 | 1\_udt6wooR9Nnq\_BaJB2rgr2-lW0UVOO1 | E1/T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | a confirmar | autoria a confirmar | único | MÉDIA | P.

# 39 | 12XNAy1uG-xpDzvRSTvFIWNJ-4jGSOmMQ | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | único | MÉDIA | C/P autoria.

# 40 | 1wmoXa9uaLgFbGpt7kUstfbTsK-2Tl\_R\_ | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | a confirmar | autoria a confirmar | único | MÉDIA | P.

# 41 | 1cUBMm5IOeJWU2yOgbuAArPkvrlUBsYhd | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | espanhol | autoria a confirmar | único | FORA\_DO\_NÚCLEO, comparativo | C/P autoria.

# 42 | 12mwIXjhKLvxRUtE7kbiB2c4UpCZ5WcIN | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês aparente | múltiplos autores | único | BAIXA/MÉDIA, capítulos pertinentes | P.

# 43 | 1It2a7dYCq8sEbih2oOB41eucwNo2Yhm7 | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | único | ALTA, análise notacional | C/P autoria.

# 44 | 1IZqfCOtwIRnlw6AYsurHfp8V5nn\_2N8b | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | português | autoria a confirmar | único | ALTA, goleiras | C/P autoria.

# 45 | 1CtwKtYgfSVGNuLlml90HQVxzDYype6Nm | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | único | ALTA, carga externa | C/P autoria.

# 46 | 1wMSMDrbsagansqpWRG6SGNR606zC4Ccg | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | único | ALTA, ataque posicional | C/P autoria.

# 47 | 1XQ\_0SZ-cq0N0OOd6myn9OGqU\_hxUXaGe | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | português | autoria a confirmar | único | CRÍTICA/ALTA, adulto feminino | C/P autoria.

# 48 | 1HneFvOwDivBrt3BLDfSMph\_WUT\_REKE\_ | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | único | ALTA, decisão e finalização | C/P autoria.

# 49 | 1RZI9sNm\_Rbxkis-evgVLVXS\_F4nBWyz2 | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | instituição a confirmar | único | ALTA, arbitragem; confrontar A1 | C/P autoria.

# 50 | 1QBGyl-FTxdMiOYYB\_943z3P2g3MVSdJa | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | único | ALTA, coaching | C/P autoria.

# 51 | 1yBdr98FFXmhobDFzBiiO3-RaFNq2X74m | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | instituição a confirmar | único | ALTA, gols de dois pontos | C/P autoria.

# 52 | 1Ct4NZTemlmlUHommPnhzSEkCVidTZKuk | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | instituição a confirmar | único | ALTA, goleiras | C/P autoria.

# 53 | 1gDwFrwfMOOUcdayRNzqZbu-Z532B9SnL | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | instituição a confirmar | único | ALTA, goleiras | C/P autoria.

# 54 | 1frRfzbb2SNW2hhj06plbOptwnJiE0CVG | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | instituição a confirmar | único | ALTA, defesa | C/P autoria.

# 55 | 1nUxK77H9AJoefEuVbOjSHYg-raa-6vVd | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | autoria a confirmar | único | ALTA, planejamento | C/P autoria.

# 56 | 17DVivqtLG9rHvfUT00VzfczFKEAt7a4Q | T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | inglês | instituição a confirmar | único | ALTA, ataque | C/P autoria.

# 57 | 15cGixSPDNbS2swGbFgg0XyYXZQnfGzdu | T1 | HISTÓRICO 2017 | inglês | instituição a confirmar | único | MÉDIA | C/P autoria.

# 58 | 143mYXG7FqDVjD1x2Hz1EZ96HokHdVrbv | T1 | A\_CONFIRMAR | inglês aparente | instituição a confirmar | único | MÉDIA/ALTA, delegados | P.

# 59 | 1EHgitwAAu857c8SA4CKFd44uvTae7WqC | H1 | HISTÓRICO | inglês | autoria a confirmar | único | CONTEXTUAL | C/P autoria.

# 60 | 1M9gVni-gmPAWQEI986MGnwAesx9mPFfj | E1 | publicação 2021 | inglês | João Paulo Torres Di Gilio; Karen Pereira da Silva; Rafael Pombo Menezes | cópia descritiva canônica; duplicata genérica removida | ALTA, defesa | C.

# 61 | 1SA4vtLZjRzEgwhSynWEaGqSWK\_juJwFV | E1/T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | português | autoria a confirmar | único | ALTA, ataque posicionado | C/P autoria.

# 62 | 1WN96gNV7HiQAPoGDbUrvW0Mit6ZNsOel | E1/T1 | NÃO\_APLICÁVEL\_COMO\_NORMA | português | organizadores a confirmar | único | ALTA, síntese temática | C/P autoria.

# 63 | 13Oe8vfsR94rH96neo-evGB\_PFxOBs4eb | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | português | autoria a confirmar | único | ALTA, goleiras | C/P autoria.

# 64 | 1NGiVLsuFe6PKH1nH4B\_wVJIDDLEjpe85 | A1 | edição IHF 2026 a reconciliar | inglês | IHF | renderização alternativa; relação exata com item 37 pendente | CRÍTICA | C/P versão.

# 65 | 16zBkB9jsXbElFT8nFR678kXOlAoAazX7 | E1 | NÃO\_APLICÁVEL\_COMO\_NORMA | português | autores/organizadores a confirmar | único | ALTA, síntese científica | C/P autoria.

# 

# C18.4 Precedência e controle de versões

# 1\. Regras universais: A1 IHF prevalece. A tradução portuguesa é derivada e não supera o original.

# 2\. Competições nacionais: A2 CBHb prevalece dentro da jurisdição e edição aplicáveis.

# 3\. Circuito estadual do Rio de Janeiro: A3 FHERJ prevalece dentro de sua jurisdição, subordinado à IHF e à CBHb quando cabível.

# 4\. O1 e O2 comprovam eventos, inscrições, equipes, tabelas, resultados e decisões operacionais; não criam regras universais.

# 5\. E1 e T1 podem sustentar conceitos, métricas e hipóteses; não originam obrigações normativas por si sós.

# 6\. Duplicatas conhecidas removidas permanecem no histórico da ACT-F01-002. Não há duplicata exata atual declarada pela combinação de nome e tamanho.

# 7\. O item 64 permanece como possível renderização alternativa do item 37, sem declaração de identidade binária.

# 

# C18.5 Pendências

# PEN-F02-007 — confirmar autoria/emissor e edição dos itens marcados P durante a Fase 3.

# PEN-F02-008 — comparar estruturalmente os itens 37 e 64 e reconciliar datas de eficácia IHF.

# PEN-F02-009 — confirmar publicação final do regulamento CBHb 2026.

# PEN-F02-010 — estabelecer relação de versão entre as tabelas da 3ª etapa, itens 16 e 21.

# PEN-F02-011 — aplicar controles de dados pessoais aos documentos nominais e planilhas de equipes.

# 

# C18.6 Evidências e testes

# EVD-F02-007 — inventário reconciliado ACT-F01-002 com 65 IDs atuais.

# EVD-F02-008 — leitura do Regulamento Geral do Circuito Estadual 2026, FHERJ, Rev.01 de 01/03/2026.

# EVD-F02-009 — leitura do Ofício 05/2026 DHP/CBHb, assinado pela Diretoria Geral e Presidência da CBHb.

# EVD-F02-010 — leitura do Guia CBHb Praia 2026, com calendário, inscrições e orientações operacionais.

# EVD-F02-011 — leitura da Convocação Oficial Rosário 2026, relativa à Seleção Brasileira Adulta Feminina.

# TST-F02-007 — 65 de 65 itens possuem classe de autoridade: APROVADO.

# TST-F02-008 — 65 de 65 itens possuem vigência ou condição temporal: APROVADO.

# TST-F02-009 — 65 de 65 itens possuem idioma confirmado ou explicitamente provisório: APROVADO.

# TST-F02-010 — 65 de 65 itens possuem autoria/emissor confirmado ou A\_CONFIRMAR: APROVADO.

# TST-F02-011 — nenhuma fonte E1, T1, O1, O2 ou P1 foi promovida a norma universal: APROVADO.

# TST-F02-012 — incertezas de versão e autoria foram preservadas: APROVADO.

# 

# C18.7 Decisão e próxima ação

# Resultado da ACT-F02-002: PRODUZIDO.

# A ACT-F02-001 permanece como fotografia histórica e é substituída operacionalmente pela presente matriz.

# ACT-F03-001: PRONTO para preparar, ler e segmentar as 65 fontes acessíveis, fechando os atributos provisórios.

# Portão A: PENDENTE até conclusão da Fase 3 e revisão humana das pendências críticas.

# Fase 4: ABERTA\_PARA\_EXTRAÇÃO\_CONTROLADA.

# 

# 

## C19. EXECUÇÃO DA ACT-F03-001 — PREPARAÇÃO, LEITURA E SEGMENTAÇÃO DOCUMENTAL

# 

### C19.1 Registro da ação controlada

# Identificador: ACT-F03-001.

# Nome: preparar, ler e segmentar as 65 fontes acessíveis.

# Objetivo: converter o acervo reconciliado em um corpus estruturalmente segmentado, recuperável e rastreável, confirmando metadados bibliográficos e relações de versão sem antecipar a extração de conhecimento da Fase 4.

# Fase: Fase 3 — Preparação, leitura e segmentação documental.

# Subdomínio: inteligência documental, proveniência, estrutura de fontes e preparação do corpus.

# Entradas autorizadas: inventário ACT-F01-002; matriz ACT-F02-002; 65 itens atuais de FONTES → BEACH HANDBALL; conteúdo textual, estrutura de planilhas e imagens de página quando a extração textual não estava disponível.

# Precondições: ACT-F01-002 PRODUZIDA; ACT-F02-002 PRODUZIDA; 65 itens acessíveis; nenhum arquivo atual com zero bytes.

# Dependências: ACT-F00-001 VALIDADA; ACT-F01-002 e ACT-F02-002 PRODUZIDAS.

# Procedimento executado: recuperar conteúdo; identificar modo de leitura; confirmar título, idioma, autoria ou emissor, edição e data quando declarados; distinguir norma, evidência, material técnico e registro operacional; atribuir identificador estável de fonte; definir localizadores estáveis de segmentos; registrar relações de versão, substituição e correspondência; preservar lacunas sem inventar.

# Saídas: registro de corpus com 65 fontes; convenção de segmentação; matriz individual de metadados e localizadores; mapa de relações de versão; limitações; evidências e testes.

# Portão relacionado: Portão A — Fontes.

# Estado resultante: PRODUZIDO.

# Responsável pela validação: proprietário do projeto ou responsável humano designado.

# 

### C19.2 Resultado do corpus preparado

# • Fontes atuais processadas: 65 de 65.

# • Formatos: 60 PDFs, 3 XLSX e 2 Markdown.

# • Fontes com conteúdo textual ou tabular recuperado: 64.

# • Fonte preparada por inspeção visual de páginas: 1 — CEPRAEA.pdf, com quatro páginas.

# • Arquivos vazios: 0.

# • Cada fonte recebeu um identificador estável SRC-F03-001 a SRC-F03-065.

# • Cada fonte recebeu uma estratégia e localizadores de segmento.

# • A segmentação é referencial: preserva o arquivo original como fonte de verdade e não replica integralmente conteúdo protegido ou dados pessoais no documento mestre.

# • Nenhuma conclusão científica foi convertida em norma; nenhum documento operacional foi tratado como regulamento por possuir linguagem prescritiva isolada.

# 

### C19.3 Convenção de segmentação

# Normas e regulamentos: SEG-F03-xxx-CAPnn-SEÇnn-ARTnn-PARnn ou SEG-F03-xxx-Rnn-Ann, com apêndices próprios.

# Artigos científicos: SEG-F03-xxx-ABSTRACT, INTRO, MÉTODO, RESULTADOS, DISCUSSÃO, CONCLUSÃO, TABELA-nn, FIGURA-nn e REFERÊNCIAS.

# Materiais técnicos e cursos: SEG-F03-xxx-MÓDULO/TEMA/SLIDE, preservando a ordem documental.

# Registros operacionais: SEG-F03-xxx-EVENTO, ETAPA, CATEGORIA, JOGO-nnn, ATLETA-nnn, DIRIGENTE-nnn ou DATA-nnn.

# Planilhas: SEG-F03-xxx-ABA-<nome>-LINHA-nnn, preservando aba, cabeçalho e coordenadas.

# Documentos internos: SEG-F03-xxx-PROPÓSITO, PLANO, FASE, FUNÇÃO, ATIVIDADE, PERGUNTA ou AVALIAÇÃO.

# Imagens de página: SEG-F03-xxx-Pnn-<tipo>, com inspeção visual e sem OCR quando a leitura humana da página foi suficiente.

# 

### C19.4 Registro individual das 65 fontes

# Formato: SRC | ID | título | idioma | autoria/emissor | edição/data | classe | localizadores | relação/limitação.

# SRC-F03-001 | 1KI\_4F23dkOvDiCEVpTMmrKDsjHxcHO1L | Mini Beach Handball Info Sheet 2020 | inglês | Dr. Frowin Fasold; Alex Gehrer / European Handball Federation | 2020 | T1 | SEG-F03-001-CAPA; SEG-F03-001-VANTAGENS; SEG-F03-001-U10; SEG-F03-001-PONTUAÇÃO; SEG-F03-001-SHOOTOUT | fonte técnica educacional; substitui o PDF histórico vazio.

# SRC-F03-002 | 1p4cK4IIY9EwD45lB8BsQ03u-LYQpQLji | Ultimate School Handball 2025 | inglês | Frowin Fasold; Christina Carl; Ralf Rascher; Alexander Gehrer | 2025 | T1 | SEG-F03-002-PREFÁCIO; SEG-F03-002-FUNDAMENTOS; SEG-F03-002-JOGOS; SEG-F03-002-PROGRESSÕES; SEG-F03-002-AVALIAÇÃO | material escolar; substitui o PDF histórico vazio.

# SRC-F03-003 | 1\_nFkwAFUY6\_1iVcWIvFLAgN\_vlV5B57L | Refereeing in Beach Handball | inglês | autoria individual não declarada no extrato; emissor editorial a confirmar | edição não declarada | T1/E1 | SEG-F03-003-DEMANDAS; SEG-F03-003-CALOR; SEG-F03-003-PREPARAÇÃO; SEG-F03-003-RECUPERAÇÃO; SEG-F03-003-REFERÊNCIAS | fonte técnica sobre árbitros; substitui o PDF histórico vazio.

# SRC-F03-004 | 1EoqJMqroFkxb7Dljqd0f2HExopBbIV3e | Understanding Psychological Pressure in Beach Handball Shootouts | inglês | autoria individual não declarada no extrato | edição não declarada | T1/E1 | SEG-F03-004-DEMANDAS; SEG-F03-004-FATORES; SEG-F03-004-ROTINAS; SEG-F03-004-VISUALIZAÇÃO; SEG-F03-004-CLIMA-EQUIPE; SEG-F03-004-APLICAÇÃO | fonte técnico-psicológica; substitui o PDF histórico vazio.

# SRC-F03-005 | 1KoA-RHtH0dD5tL7vB9pnn75-2bz0N\_Kl | CEPRAEA.pdf | português | CEPRAEA; autoria individual não declarada | 2ª etapa de 2026 | O2 | SEG-F03-005-P01-CAPA; SEG-F03-005-P02-RELAÇÃO; SEG-F03-005-P03-CRONOGRAMA; SEG-F03-005-P04-CLASSIFICAÇÃO | PDF de imagem; quatro páginas verificadas visualmente.

# SRC-F03-006 | 1VTGjxKU73z\_iu1ntN4m8qWgmnxS\_TQrk | Convocação Oficial Rosário 2026 | português | Confederação Brasileira de Handebol | 28-01-2026 | O1 | SEG-F03-006-ATO; SEG-F03-006-COMISSÃO; SEG-F03-006-ATLETAS; SEG-F03-006-PERÍODOS | convocação oficial da seleção adulta feminina.

# SRC-F03-007 | 1I354EemsKiOIXjpSAw8RK7Ua1WSjY7ny | Ofício nº 05/2026 – DHP/CBHb | português | Wellington N. A. Esteves; Felipe Rêgo Barros / CBHb | 2026 | A2/O1 | SEG-F03-007-OBJETO; SEG-F03-007-CATEGORIAS; SEG-F03-007-INSCRIÇÕES; SEG-F03-007-RESPONSABILIDADES; SEG-F03-007-ASSINATURAS | orientação oficial para a Copa Brasil 2026.

# SRC-F03-008 | 1aR9MOhC40ZIP\_yTKKjmLmXZEQyUjMKI\_ | Regulamento Geral Campeonato Carioca 2026 | português | Federação de Handebol do Estado do Rio de Janeiro | Rev.00 20-01-2026; Rev.01 01-03-2026 | A3 | SEG-F03-008-CAPxx-ARTxx-PARxx | regulamento estadual; segmentado por capítulo, seção, artigo e parágrafo.

# SRC-F03-009 | 1GmqY41nfH8Qgfj8ehI97VSWol27sm7Tf | Mudanças nas Regras de Handebol de Praia 2026 | português | Luiz Filipe Caldas / FHERJ | 17-03-2026; efeitos 01-04-2026 | A3 | SEG-F03-009-JOGO-PASSIVO; SEG-F03-009-FINAIS; SEG-F03-009-GOLEIRO; SEG-F03-009-EQUIPAMENTO | circular explicativa subordinada às regras IHF.

# SRC-F03-010 | 17LIvxbIoD-2MWDw9COIgvqQSViEXBRIm | Equipes para o Campeonato Carioca 2026 | português | FHERJ; autoria individual não declarada | Rev. 28-02-2026 | A3/O1 | SEG-F03-010-EQUIPES-CATEGORIA; SEG-F03-010-TAXAS; SEG-F03-010-PRAZOS; SEG-F03-010-NOMINAL; SEG-F03-010-PONTUAÇÃO | documento misto: orientação local e registro operacional.

# SRC-F03-011 | 1krs0n6vZs8LRLL55Soo0WfOi23A2tN7N | Tabela 1ª etapa adulto | português | Stanley Mackenzie / FHERJ | conteúdo: 26-04-2026 | O1 | SEG-F03-011-CABEÇALHO; SEG-F03-011-JOGO-001..020 | programação; nome do arquivo contém 26.05, divergente do conteúdo.

# SRC-F03-012 | 1x4\_-b1f1Ql55IK2QYZ9CLLBz3uyoS1Ww | Relação nominal CEPRAEA – 1ª etapa | português | FHERJ; CEPRAEA; responsável Davi Sermenho | 26-04-2026 | O2 | SEG-F03-012-EVENTO; SEG-F03-012-ATLETA-001..012; SEG-F03-012-DIRIGENTES | registro nominal adulto feminino.

# SRC-F03-013 | 1nRtGbXGUMeKv61qLZ1W0CkYzQv7\_xPKl | Resultado 1ª etapa adulto | português | Stanley Mackenzie / FHERJ | 26-04-2026 | O1 | SEG-F03-013-CABEÇALHO; SEG-F03-013-JOGO-001..024 | resultado efetivo relacionado à programação SRC-011.

# SRC-F03-014 | 1arSTonBG2Vs31cPL6axREzx-hC79gSB1 | Datas Circuito Carioca 2026 | português | Stanley Mackenzie / FHERJ | temporada 2026 | O1 | SEG-F03-014-ETAPA-001..014; SEG-F03-014-LOCAL | calendário oficial-operacional.

# SRC-F03-015 | 1HAIxQU3wXsNGpctu3Yjl8XN\_afr5HIib | Boletim 01 – 3ª etapa Circuito Brasileiro 2026 | português | CBHb | 23 a 26-07-2026 | O1/A2 | SEG-F03-015-GERAL; SEG-F03-015-CONTATOS; SEG-F03-015-GRUPOS; SEG-F03-015-JOGO-xxx; SEG-F03-015-ARBITRAGEM | boletim oficial de competição.

# SRC-F03-016 | 1xQYAdUYkAGtdt6pctG0DTCF6\_Unk5kCq | Tabela preliminar 3ª etapa adulto | português | emissor não explicitado; contexto FHERJ | 05-07-2026 | O1 | SEG-F03-016-JOGO-001..024 | versão preliminar; substituída operacionalmente por SRC-021.

# SRC-F03-017 | 1sG4Uzk2119herbmrl0mpCWjNmFb7M1EH | Relação nominal CEPRAEA – 2ª etapa | português | FHERJ; CEPRAEA; responsáveis Davi Sermenho e Thiago William de Almeida | 31-05-2026 | O2 | SEG-F03-017-EVENTO; SEG-F03-017-ATLETA-001..012; SEG-F03-017-DIRIGENTES | registro nominal adulto feminino.

# SRC-F03-018 | 1PcVyCwMj8U6iOrmEED-toD8hUZBuhZ9v | Resultado 3ª etapa adulto | português | contexto FHERJ; autoria individual não declarada | 05-07-2026 | O1 | SEG-F03-018-JOGO-001..017 | resultado corresponde à tabela corrigida SRC-021.

# SRC-F03-019 | 1QCUoRfGIvRPOJZgoybV8d3ClXkoGmHjb | Tabela 2ª etapa adulto | português | contexto FHERJ; autoria individual não declarada | 31-05-2026 | O1 | SEG-F03-019-JOGO-001..024 | programação da segunda etapa.

# SRC-F03-020 | 1vbhZ2-YnnhkaoiI5nK5rjTnouawX4XoN | Colocação e pontuação nas etapas 2026 | português | FHERJ | fotografia após etapas disputadas | O1 | SEG-F03-020-ADULTO-M; SEG-F03-020-ADULTO-F; SEG-F03-020-CADETE; SEG-F03-020-JUVENIL | snapshot acumulado, não regulamento.

# SRC-F03-021 | 1mqriO11izHjl2-Xy8f1aLf2mI6D8XsIm | Tabela corrigida 3ª etapa adulto | português | contexto FHERJ; autoria individual não declarada | 05-07-2026 | O1 | SEG-F03-021-JOGO-001..017 | substitui SRC-016 e corresponde ao resultado SRC-018.

# SRC-F03-022 | 1lEqDQGL0ZzUtAOZuqtT4wZgZjNxqF8Vc | Finais 2025 | português | CBHb | 2025 | O1 | SEG-F03-022-CALENDÁRIO; SEG-F03-022-INSCRIÇÃO; SEG-F03-022-EQUIPE; SEG-F03-022-ACADEMY; SEG-F03-022-UNIFORMES; SEG-F03-022-CANAL | guia operacional das finais nacionais.

# SRC-F03-023 | 1e8PXOtmQSzHbiRur0imKC8epq5KphMff | É Hora do Show! | português | CEPRAEA; autoria individual não declarada | Fase Final 2025 | T1/O2 | SEG-F03-023-PROPÓSITO; SEG-F03-023-PREPARAÇÃO; SEG-F03-023-COMPETIÇÃO; SEG-F03-023-MENTAL; SEG-F03-023-FASES-JOGO; SEG-F03-023-POSIÇÕES; SEG-F03-023-SISTEMAS | plano técnico-operacional interno.

# SRC-F03-024 | 13DIL2fO2ev0M5GHK5TzPe4Y3bsq6wVFV | Reunião pós fase final | português | CEPRAEA; autoria individual não declarada | pós-final 2025 | O2/T1 | SEG-F03-024-RITUAIS; SEG-F03-024-IDENTIDADE; SEG-F03-024-XIM; SEG-F03-024-DINÂMICAS; SEG-F03-024-FLOW; SEG-F03-024-SÍNTESE | instrumento de reflexão qualitativa.

# SRC-F03-025 | 18Txf8nXmK--9UY7NqKMcs1PI4Ext-5zc | Finais João Pessoa 25.xlsx | português | CBHb/organização da competição | 2025 | O1 | SEG-F03-025-ABA-GERAL-JR-INF-LINHA-001..061; SEG-F03-025-ABA-GERAL-ADU-CAD-LINHA-001..162 | planilha com duas tabelas de jogos.

# SRC-F03-026 | 1Liwv3PKcJp7ymvAw9eckUb66HOM64Dk4 | Guia CBHb Praia 2026 | português | CBHb | 2026 | A2/O1 | SEG-F03-026-ETAPA-001..006; SEG-F03-026-EQUIPE; SEG-F03-026-UNIFORMES; SEG-F03-026-CANAL | guia operacional nacional.

# SRC-F03-027 | 1xlV6C\_bLXVbipKLwPxpBJqnZAiohmK\_x | CEPRAEA Julho 2026 | português | CEPRAEA; autoria individual não declarada | julho de 2026 | O2 | SEG-F03-027-DISPONIBILIDADE; SEG-F03-027-TREINOS; SEG-F03-027-ETAPA; SEG-F03-027-JOGOS; SEG-F03-027-ORIENTAÇÕES | agenda e disponibilidade internas.

# SRC-F03-028 | 1NSwNjUfvnZEKAKxlJR4lDSHJE5hjzIv5 | Equipes Beach 26 – equipes.xlsx | português | autoria/emissor não declarados | 2ª etapa de 2026 | O1 | SEG-F03-028-ABA-ETAPA2-LINHA-001..019 | 18 registros de equipes por categoria e naipe.

# SRC-F03-029 | 15pumu2CMTiPeAwP0jxNplKd2uLQL0iYt | Regras de Handebol de Praia 2026 – tradução | português | Luiz Filipe Galvão da Silva Caldas; original IHF | 01-03-2026 | A1-derivada | SEG-F03-029-R01..R18; SEG-F03-029-SINAIS; SEG-F03-029-ESCLARECIMENTOS; SEG-F03-029-SUBSTITUIÇÃO; SEG-F03-029-UNIFORME; SEG-F03-029-AREIA-LUZ | tradução operacional; original IHF prevalece.

# SRC-F03-030 | 1CJ4Uybko9zLuF1g2NReTQxOvxMQxOQ71 | Relação Nominal 2025.xlsx | português | CBHb | 2025 | O1 | SEG-F03-030-ABA-PLANILHA1-CABEÇALHO; SEG-F03-030-DIRIGENTES; SEG-F03-030-ATLETAS; SEG-F03-030-RESPONSÁVEL | formulário nominal sem atletas preenchidos.

# SRC-F03-031 | 1MXLOcWY9r1RdQ6zKWA3qI5AJOfHkguT2 | Regulamento Circuito Brasileiro Adulto 2026 | português | CBHb | 2026; versão final não confirmada | A2 | SEG-F03-031-CAPxx-ARTxx-PARxx | contém marcas editoriais; vigência formal pendente.

# SRC-F03-032 | 1nL49p72AVybqNu422FJPycld2nmejoIG | Esclarecimentos às regras de jogo | português | Luiz Filipe Caldas / FHERJ | 23-04-2025 | A3-histórica | SEG-F03-032-EQUIPE; SEG-F03-032-TIRO-ÁRBITRO; SEG-F03-032-PASSIVO; SEG-F03-032-SHOOTOUT; SEG-F03-032-PUNIÇÕES | orientação local potencialmente superada em pontos por 2026.

# SRC-F03-033 | 1WTB7ihMOkNtUXsrl67yAyy5tUvAccRt4 | Atualizações IHF 2026 | inglês predominante | International Handball Federation; captura/compilação local | 13-03-2026 | R1/A1-proveniência | SEG-F03-033-VIGÊNCIA; SEG-F03-033-PASSIVO; SEG-F03-033-FINAIS; SEG-F03-033-GOLEIRO; SEG-F03-033-EQUIPAMENTO; SEG-F03-033-WHEELCHAIR | confirma vigência geral em 01-04-2026; conteúdo wheelchair fora do núcleo.

# SRC-F03-034 | 10UvC1U2ef3AePzZqTXBBqi57AlKA4WM- | Página IHF – Rules of the Game | inglês | International Handball Federation | captura 2026 | R1 | SEG-F03-034-PÁGINA; SEG-F03-034-APÊNDICES; SEG-F03-034-LINKS | registro de proveniência.

# SRC-F03-035 | 1nCp6EXVpBMMgDgi8od2sUUMoFEI90hGm | Regras IHF 2026 – francês | francês | International Handball Federation | 01-03-2026 | A1 | SEG-F03-035-R01..R18; SEG-F03-035-APÊNDICES | versão oficial paralela; nota de disposições destacadas em 01-07-2026.

# SRC-F03-036 | 1c5NWDpXgYhNFSobOTgLQ7l5ZnaXrpcxU | Regras IHF 2026 – alemão | alemão | International Handball Federation | 01-03-2026 | A1 | SEG-F03-036-R01..R18; SEG-F03-036-APÊNDICES | versão oficial paralela; nota de disposições destacadas em 01-07-2026.

# SRC-F03-037 | 1xf\_td5UAFtvegx2i7kcvBby-VbZdtXaq | Regras IHF 2026 – inglês | inglês | International Handball Federation | 01-03-2026 | A1 | SEG-F03-037-R01..R18; SEG-F03-037-APÊNDICES | cópia canônica oficial em inglês.

# SRC-F03-038 | 1\_udt6wooR9Nnq\_BaJB2rgr2-lW0UVOO1 | El entrenamiento del juego de defensa en balonmano playa | espanhol/português | Claudia Monteiro; Alexandre G. Almeida | 22–23-06-2007 | T1 | SEG-F03-038-FASES; SEG-F03-038-OBJETIVOS; SEG-F03-038-FUNDAMENTOS; SEG-F03-038-SISTEMAS; SEG-F03-038-RECURSOS | curso técnico histórico.

# SRC-F03-039 | 12XNAy1uG-xpDzvRSTvFIWNJ-4jGSOmMQ | Introduction to Beach Handball | inglês | Márcio Magliano, atribuição editorial pelo documento | edição não declarada; dados até 2018 | T1 | SEG-F03-039-INTRO; SEG-F03-039-HISTÓRIA; SEG-F03-039-REGRAS; SEG-F03-039-JOGO-ASSIMÉTRICO; SEG-F03-039-TÉCNICA | ebook introdutório.

# SRC-F03-040 | 1wmoXa9uaLgFbGpt7kUstfbTsK-2Tl\_R\_ | Defense tactics in high-level teams in Beach handball | inglês | Konstantinos Gkagkanas; Dimitris Hatzimanouil; Vasilis Skandalis; Sofia Dimitriou; Sophia D. Papadopoulou | JPES 18(2), 2018; DOI 10.7752/jpes.2018.02135 | E1 | SEG-F03-040-ABSTRACT; SEG-F03-040-INTRO; SEG-F03-040-MÉTODOS; SEG-F03-040-RESULTADOS; SEG-F03-040-DISCUSSÃO; SEG-F03-040-REFERÊNCIAS | artigo científico.

# SRC-F03-041 | 1cUBMm5IOeJWU2yOgbuAArPkvrlUBsYhd | Revista Internacional de Deportes Colectivos nº 34 | espanhol/inglês | AEDC; editor Guillermo Rocafort Pérez; autores por artigo | abril–junho de 2018 | E1 | SEG-F03-041-ART-BEACH-CYCLE; SEG-F03-041-ART-FOOTBALL-VOLUME; SEG-F03-041-DEMAIS-ARTIGOS | volume contém artigo relevante de Lara Cobos et al. e artigo de futebol fora do núcleo.

# SRC-F03-042 | 12mwIXjhKLvxRUtE7kbiB2c4UpCZ5WcIN | 6th International Scientific Conference on Kinesiology – Proceedings | inglês | editores Dragan Milanović e Goran Sporiš | Zagreb/Opatija, 2011; ISBN 978-953-317-013-8 | E1 | SEG-F03-042-ART-BEACH-FEMALE-CADIZ; SEG-F03-042-METADADOS; SEG-F03-042-DEMAIS-ANAIS | análise seletiva; artigo de Igor Gruić, Dinko Vuleta, Marina Bazzeo e Katarina Ohnjec.

# SRC-F03-043 | 1It2a7dYCq8sEbih2oOB41eucwNo2Yhm7 | Notational Analysis of Beach Handball | inglês | Alice Iannaccone; Andrea Fusco; Daniele Conte; Cristina Cortis | Human Movement 23(1), 2022; DOI 10.5114/hm.2021.101757 | E1 | SEG-F03-043-ABSTRACT; SEG-F03-043-INTRO; SEG-F03-043-MÉTODOS; SEG-F03-043-RESULTADOS; SEG-F03-043-CONCLUSÕES; SEG-F03-043-TABELAS | artigo científico.

# SRC-F03-044 | 1IZqfCOtwIRnlw6AYsurHfp8V5nn\_2N8b | Ações do guarda-redes por coordenadas polares | espanhol/inglês/português | J. A. Vázquez-Diz; J. P. Morillo-Baro; R. E. Reigal; V. Morales-Sánchez; A. Hernández-Mendo | Cuadernos de Psicología del Deporte 19(3), 2019 | E1 | SEG-F03-044-RESUMOS; SEG-F03-044-INTRO; SEG-F03-044-MÉTODO; SEG-F03-044-RESULTADOS; SEG-F03-044-DISCUSSÃO; SEG-F03-044-CONCLUSÃO | artigo científico.

# SRC-F03-045 | 1CtwKtYgfSVGNuLlml90HQVxzDYype6Nm | External Load Analysis in Beach Handball | inglês | Carsten Müller; Christina Willberg; Lukas Reichert; Karen Zentgraf | Sensors 22, 3011, 2022; DOI 10.3390/s22083011 | E1 | SEG-F03-045-ABSTRACT; SEG-F03-045-INTRO; SEG-F03-045-MÉTODOS; SEG-F03-045-RESULTADOS; SEG-F03-045-DISCUSSÃO; SEG-F03-045-CONCLUSÃO | artigo científico.

# SRC-F03-046 | 1wMSMDrbsagansqpWRG6SGNR606zC4Ccg | Instrumento de observação do ataque posicional | inglês/espanhol | Juan-Carlos Zapardiel; María Luisa Rodríguez-Hernández; Pedro Miguel González-Moreno; Francisco Sánchez Sánchez | E-Balonmano 21(4), 2025; DOI 10.17398/1885-7019.21.495 | E1 | SEG-F03-046-RESUMOS; SEG-F03-046-INTRO; SEG-F03-046-MÉTODO; SEG-F03-046-INSTRUMENTO; SEG-F03-046-RESULTADOS; SEG-F03-046-CONCLUSÕES | artigo científico.

# SRC-F03-047 | 1XQ\_0SZ-cq0N0OOd6myn9OGqU\_hxUXaGe | Importância das posições dos passes para arremessos | português | autoria conforme folha bibliográfica do documento; preservada para extração detalhada | edição acadêmica a confirmar | E1 | SEG-F03-047-RESUMO; SEG-F03-047-INTRO; SEG-F03-047-MÉTODO; SEG-F03-047-RESULTADOS; SEG-F03-047-CONCLUSÃO | estudo específico do adulto feminino.

# SRC-F03-048 | 1HneFvOwDivBrt3BLDfSMph\_WUT\_REKE\_ | Contextual Factors and Decision-Making in Positional Attack | inglês | Juan A. Vázquez-Diz e coautores; correspondência Antonio Hernández-Mendo | Frontiers in Psychology, 13-06-2019; DOI 10.3389/fpsyg.2019.01386 | E1 | SEG-F03-048-ABSTRACT; SEG-F03-048-INTRO; SEG-F03-048-MÉTODO; SEG-F03-048-RESULTADOS; SEG-F03-048-DISCUSSÃO; SEG-F03-048-CONCLUSÃO | artigo científico.

# SRC-F03-049 | 1RZI9sNm\_Rbxkis-evgVLVXS\_F4nBWyz2 | 6-metre throw + punishments | inglês | material técnico institucional; autoria individual não declarada | edição não declarada | T1 | SEG-F03-049-6M; SEG-F03-049-PUNIÇÕES; SEG-F03-049-EXEMPLOS | suplemento técnico, subordinado às regras vigentes.

# SRC-F03-050 | 1QBGyl-FTxdMiOYYB\_943z3P2g3MVSdJa | Coaching a winning team | inglês | material técnico; autoria individual a confirmar | edição não declarada | T1 | SEG-F03-050-COACHING; SEG-F03-050-PLANEJAMENTO; SEG-F03-050-EQUIPE; SEG-F03-050-COMPETIÇÃO | material técnico-operacional.

# SRC-F03-051 | 1yBdr98FFXmhobDFzBiiO3-RaFNq2X74m | 2-point goals: spin and in-flight shots | inglês | material técnico institucional; autoria individual não declarada | edição não declarada | T1 | SEG-F03-051-SPIN; SEG-F03-051-INFLIGHT; SEG-F03-051-PROGRESSÕES; SEG-F03-051-ERROS | material técnico.

# SRC-F03-052 | 1Ct4NZTemlmlUHommPnhzSEkCVidTZKuk | Goalkeeper behaviour – Special Situations | inglês | material técnico institucional; autoria individual não declarada | edição não declarada | T1 | SEG-F03-052-SITUAÇÕES; SEG-F03-052-POSIÇÃO; SEG-F03-052-DECISÃO; SEG-F03-052-EXEMPLOS | material de goleiras.

# SRC-F03-053 | 1gDwFrwfMOOUcdayRNzqZbu-Z532B9SnL | Goalkeeper behaviour inside and outside goal area | inglês | material técnico institucional; autoria individual não declarada | edição não declarada | T1 | SEG-F03-053-DENTRO; SEG-F03-053-FORA; SEG-F03-053-TRANSIÇÃO; SEG-F03-053-DECISÃO | material de goleiras.

# SRC-F03-054 | 1frRfzbb2SNW2hhj06plbOptwnJiE0CVG | Latest trends in defence | inglês | material técnico institucional; autoria individual não declarada | edição não declarada | T1 | SEG-F03-054-PRINCÍPIOS; SEG-F03-054-FORMAÇÕES; SEG-F03-054-AJUSTES; SEG-F03-054-EXEMPLOS | material técnico defensivo.

# SRC-F03-055 | 1nUxK77H9AJoefEuVbOjSHYg-raa-6vVd | Preparation of a national team on the way to a top event | inglês | material técnico; autoria individual a confirmar | edição não declarada | T1 | SEG-F03-055-PERIODIZAÇÃO; SEG-F03-055-SELEÇÃO; SEG-F03-055-TREINOS; SEG-F03-055-EVENTO | planejamento de seleção.

# SRC-F03-056 | 17DVivqtLG9rHvfUT00VzfczFKEAt7a4Q | Latest trends in attack | inglês | material técnico institucional; autoria individual não declarada | edição não declarada | T1 | SEG-F03-056-ESTRUTURA; SEG-F03-056-PROCEDIMENTOS; SEG-F03-056-FINALIZAÇÃO; SEG-F03-056-EXEMPLOS | material técnico ofensivo.

# SRC-F03-057 | 15cGixSPDNbS2swGbFgg0XyYXZQnfGzdu | Further Education Course 2017 Gaeta | inglês | European Handball Federation; autores/palestrantes por módulo | Gaeta, 2017 | T1 | SEG-F03-057-MÓDULO-xxx | curso de formação histórico.

# SRC-F03-058 | 143mYXG7FqDVjD1x2Hz1EZ96HokHdVrbv | EHF Beach Handball Delegates Refresh | inglês | Marco Trespidi / European Handball Federation | Gaeta, 24-05-2017 | T1 | SEG-F03-058-FUNÇÃO; SEG-F03-058-RELATÓRIO; SEG-F03-058-AVALIAÇÃO; SEG-F03-058-PROCEDIMENTOS | material para delegados.

# SRC-F03-059 | 1EHgitwAAu857c8SA4CKFd44uvTae7WqC | Beach Handball History | inglês | material histórico institucional; autoria individual não declarada | edição não declarada | H1 | SEG-F03-059-ORIGENS; SEG-F03-059-COMPETIÇÕES; SEG-F03-059-MARCOS; SEG-F03-059-EVOLUÇÃO | fonte contextual.

# SRC-F03-060 | 1M9gVni-gmPAWQEI986MGnwAesx9mPFfj | The structuring of the defensive phase of beach handball | inglês | João Paulo Torres Di Gilio; Karen Pereira da Silva; Rafael Pombo Menezes | 2021 | E1 | SEG-F03-060-ABSTRACT; SEG-F03-060-REFERENCIAL; SEG-F03-060-MÉTODO; SEG-F03-060-RESULTADOS; SEG-F03-060-CONCLUSÃO | cópia canônica do estudo defensivo.

# SRC-F03-061 | 1SA4vtLZjRzEgwhSynWEaGqSWK\_juJwFV | O jogo ofensivo do handebol de areia | português | autoria conforme folha bibliográfica; extração nominal detalhada pendente | edição acadêmica a confirmar | E1/T1 | SEG-F03-061-ESTRUTURA; SEG-F03-061-ATAQUE-POSICIONADO; SEG-F03-061-AÇÕES; SEG-F03-061-CONCLUSÕES | estudo técnico-científico.

# SRC-F03-062 | 1WN96gNV7HiQAPoGDbUrvW0Mit6ZNsOel | Temas Emergentes do Handebol de Praia | português | autores/organizadores por capítulo | edição não declarada no extrato | E1/T1 | SEG-F03-062-CAPÍTULO-001..003; SEG-F03-062-REFERÊNCIAS | obra em três capítulos, formato de artigos.

# SRC-F03-063 | 13Oe8vfsR94rH96neo-evGB\_PFxOBs4eb | Tempos de defesa do goleiro de handebol de praia | português | autoria conforme folha bibliográfica; extração nominal detalhada pendente | edição acadêmica a confirmar | E1 | SEG-F03-063-RESUMO; SEG-F03-063-MÉTODO; SEG-F03-063-RESULTADOS; SEG-F03-063-CONCLUSÃO | estudo de goleiras.

# SRC-F03-064 | 1NGiVLsuFe6PKH1nH4B\_wVJIDDLEjpe85 | Rules of the Game IHF | inglês | International Handball Federation | edição histórica/alternativa a datar | A1-histórica | SEG-F03-064-Rxx; SEG-F03-064-APÊNDICES | provável renderização/edição alternativa; relação exata com SRC-037 pendente.

# SRC-F03-065 | 16zBkB9jsXbElFT8nFR678kXOlAoAazX7 | Handebol de Praia: subsídios científicos para a compreensão do esporte | português | Luís Filipe Gomes Barbosa Pereira de Lemos; orientador Fábio Nakamura; coorientador Amilton Cruz | tese, João Pessoa, 2023 | E1 | SEG-F03-065-PRELIMINARES; SEG-F03-065-CAPÍTULO-xxx; SEG-F03-065-REFERÊNCIAS; SEG-F03-065-ANEXOS | obra científica de síntese.

# 

### C19.5 Relações de versão e correspondência confirmadas

# 1\. SRC-F03-037 é a cópia canônica em inglês das regras oficiais IHF de 1º de março de 2026; SRC-F03-035 e SRC-F03-036 são versões oficiais paralelas em francês e alemão.

# 2\. SRC-F03-029 é tradução portuguesa derivada das regras IHF, realizada por Luiz Filipe Galvão da Silva Caldas; em divergência material, prevalece o texto oficial IHF.

# 3\. SRC-F03-033 registra a notícia IHF de 13 de março de 2026 e confirma a entrada geral das alterações do handebol de praia em 1º de abril de 2026. As notas dos livros oficiais sobre disposições destacadas para 1º de julho de 2026 foram preservadas como exceções segmentares.

# 4\. SRC-F03-034 é registro de proveniência da página oficial IHF; não substitui os livros de regras.

# 5\. SRC-F03-009 é circular FHERJ de 2026, explicativa e local, subordinada à IHF. SRC-F03-032 é esclarecimento FHERJ de 2025 e permanece histórico quando houver incompatibilidade com 2026.

# 6\. SRC-F03-031 é regulamento CBHb 2026, mas sua condição de publicação final permanece pendente porque o texto contém marcas editoriais internas.

# 7\. SRC-F03-011 é a programação da primeira etapa e SRC-F03-013 registra seus resultados efetivos.

# 8\. SRC-F03-019 é a programação da segunda etapa; não foi localizado no acervo atual um arquivo de resultados equivalente com relação inequívoca.

# 9\. SRC-F03-016 é uma tabela preliminar da terceira etapa. SRC-F03-021, identificada como tabela corrigida, possui 17 jogos e corresponde estruturalmente aos 17 resultados de SRC-F03-018; portanto SRC-F03-021 substitui SRC-F03-016 para o fato operacional daquela etapa.

# 10\. SRC-F03-022 e SRC-F03-025 tratam das finais nacionais de 2025 em níveis complementares: guia operacional e planilha detalhada de jogos.

# 11\. SRC-F03-020 é fotografia acumulada de pontuação e não substitui tabelas ou resultados de etapa.

# 12\. SRC-F03-041 contém mais de um artigo: o segmento sobre estrutura do jogo de beach handball é nuclear; o segmento sobre volume de treinamento no futebol é apenas comparativo.

# 13\. SRC-F03-042 é um livro de anais; somente o artigo sobre eficiência situacional feminina no Mundial de Cádiz foi classificado como nuclear.

# 14\. SRC-F03-064 permanece como edição histórica ou renderização alternativa das regras IHF; a equivalência exata com SRC-F03-037 requer comparação de páginas ou hash.

# 15\. Não foi identificada duplicata atual por ID; relações de substituição histórica permanecem registradas na ACT-F01-002.

# 

### C19.6 Metadados bibliográficos fechados nesta ação

# • Mini Beach Handball: Frowin Fasold e Alex Gehrer; European Handball Federation; 2020.

# • Ultimate School Handball: Frowin Fasold, Christina Carl, Ralf Rascher e Alexander Gehrer; 2025.

# • Tradução portuguesa IHF: Luiz Filipe Galvão da Silva Caldas; edição de 1º de março de 2026.

# • Material defensivo de 2007: Claudia Monteiro e Alexandre G. Almeida.

# • Defense tactics in high-level teams: Gkagkanas, Hatzimanouil, Skandalis, Dimitriou e Papadopoulou; JPES, 2018.

# • Notational Analysis: Iannaccone, Fusco, Conte e Cortis; Human Movement, 2022.

# • Estudo de goleiras por coordenadas polares: Vázquez-Diz, Morillo-Baro, Reigal, Morales-Sánchez e Hernández-Mendo; 2019.

# • External Load Analysis: Müller, Willberg, Reichert e Zentgraf; Sensors, 2022.

# • Instrumento de observação do ataque: Zapardiel, Rodríguez-Hernández, González-Moreno e Sánchez Sánchez; 2025.

# • Anais de Kinesiologia: editores Dragan Milanović e Goran Sporiš; 2011; artigo pertinente de Gruić, Vuleta, Bazzeo e Ohnjec.

# • Tese de síntese: Luís Filipe Gomes Barbosa Pereira de Lemos; João Pessoa, 2023.

# Metadados não declarados no próprio arquivo permaneceram explicitamente como “autoria individual não declarada” ou “edição a confirmar”. A ausência de crédito não foi preenchida por inferência.

# 

### C19.7 Limitações e controles

# LIM-F03-001 — CEPRAEA.pdf não possui texto extraível. Controle: renderização e inspeção visual das quatro páginas; segmentos por página.

# LIM-F03-002 — Figuras, diagramas e tabelas complexas podem perder ordem na extração textual. Controle: localizadores FIGURA/TABELA e exigência de inspeção visual quando o elemento sustentar regra, cálculo ou decisão.

# LIM-F03-003 — Documentos nominais contêm dados pessoais. Controle: o CEPRAEA-DB registra estrutura e proveniência, não reproduz listas completas além do necessário para evidência.

# LIM-F03-004 — Vinte fontes não declaram integralmente autoria individual ou edição no trecho recuperável. Controle: usar emissor institucional ou estado A\_CONFIRMAR; não inventar.

# LIM-F03-005 — O regulamento CBHb 2026 contém marcas editoriais. Controle: manter vigência formal pendente e não usá-lo como versão final sem validação humana.

# LIM-F03-006 — A nota de 1º de julho nos livros IHF convive com a notícia de vigência geral em 1º de abril. Controle: aplicar temporalidade por disposição e escalar divergência material.

# LIM-F03-007 — A segmentação prepara a Fase 4; ela não significa que conceitos, requisitos ou regras de negócio já foram extraídos ou validados.

# 

### C19.8 Evidências e testes

# EVD-F03-001 — inventário reconciliado de 65 itens da ACT-F01-002.

# EVD-F03-002 — leitura textual e estrutural das fontes por Google Drive, preservando ID e arquivo original.

# EVD-F03-003 — leitura estruturada das três planilhas, com abas e intervalos identificados.

# EVD-F03-004 — renderização e inspeção visual das quatro páginas de CEPRAEA.pdf.

# EVD-F03-005 — registro SRC-F03-001 a SRC-F03-065, todos com idioma, autoria/emissor, edição/data, classe e localizadores.

# EVD-F03-006 — mapa de relações de versão, substituição e correspondência operacional.

# EVD-F03-007 — readback da seção C19 no documento CEPRAEA-DB.

# TST-F03-001 — 65 fontes atuais possuem SRC único: APROVADO.

# TST-F03-002 — nenhuma fonte atual ficou sem estratégia de segmentação: APROVADO.

# TST-F03-003 — normas, evidências científicas, materiais técnicos e registros operacionais foram separados: APROVADO.

# TST-F03-004 — planilhas preservam aba e linha; PDFs preservam regra, artigo, seção, página ou bloco: APROVADO.

# TST-F03-005 — relações 011↔013, 016→021↔018 e 022↔025 foram registradas: APROVADO.

# TST-F03-006 — tradução e versões linguísticas foram subordinadas à fonte oficial competente: APROVADO.

# TST-F03-007 — lacunas de autoria e edição não foram preenchidas por invenção: APROVADO.

# TST-F03-008 — dados pessoais não foram replicados integralmente no corpus mestre: APROVADO.

# 

### C19.9 Decisão e próxima ação

# Resultado da ACT-F03-001: PRODUZIDO.

# Critério de saída da Fase 3: atendido no nível estrutural — as 65 fontes possuem origem, metadados, modo de leitura e localizadores recuperáveis.

# A ACT-F03-001 não está VALIDADA automaticamente. O corpus e a matriz de fontes devem ser submetidos à revisão humana do Portão A.

# Portão A: PENDENTE, com entradas documentais completas para decisão.

# Próxima ação controlada: ACT-PA-001 — revisar inventário, autoridade, vigência, cobertura e segmentação e decidir o Portão A — Fontes.

# Estado da ACT-PA-001: PRONTO.

# Fase 4: BLOQUEADA até decisão APROVADO ou APROVADO\_COM\_RESSALVAS no Portão A.

# 

# C20. DECISÃO DO PORTÃO A — ABERTURA CONTROLADA DA FASE 4

# 

# Estado: APROVADO\_COM\_RESSALVAS.

# 

# Fundamentação

# As ações de inventário, classificação preliminar, controle de autoridade, leitura e segmentação documental produziram evidências suficientes para iniciar a extração estruturada do conhecimento na Fase 4. Permanecem pendências de consolidação que não impedem o avanço, desde que sejam preservadas como controles obrigatórios e não sejam convertidas em fatos, regras vigentes ou decisões validadas.

# 

# Ressalvas obrigatórias

# 1\. Atualizar a matriz da ACT-F02-001 para contemplar integralmente as 65 fontes processadas na ACT-F03-001.

# 2\. Confirmar duplicidades por comparação de conteúdo ou hash antes de excluir ou substituir arquivos.

# 3\. Manter o regulamento CBHb 2026 com vigência formal pendente até confirmação da versão oficialmente publicada.

# 4\. Preservar a primazia das versões oficiais da IHF diante de eventual divergência material de tradução.

# 5\. Não preencher autoria, edição, data ou autoridade ausentes por inferência.

# 6\. Tratar fontes científicas, técnicas, históricas e operacionais segundo seus respectivos níveis de autoridade.

# 7\. Impedir que qualquer ressalva pendente seja transformada em requisito normativo ou restrição de banco sem validação.

# 

# Efeito da decisão

# Fica autorizada a abertura da Fase 4, limitada à extração controlada do conhecimento das fontes segmentadas. Permanecem bloqueadas decisões definitivas de requisitos, modelagem e implementação que dependam das ressalvas acima.

# 

# Controles de execução

# • Cada item extraído deverá manter rastreabilidade até o identificador da fonte e o segmento de origem.

# • Itens afetados por ressalva deverão receber estado provisório, dúvida ou bloqueio compatível; não poderão ser promovidos silenciosamente.

# • Regras oficiais, regulamentos locais, evidências científicas, materiais técnicos, fatos históricos e registros operacionais deverão permanecer semanticamente separados.

# • Nenhuma extração poderá criar autoridade, vigência, autoria, edição ou data ausentes na fonte.

# • Nenhuma decisão definitiva de requisitos, modelo ou implementação fica autorizada por este portão.

# 

# Próxima ação controlada permitida

# ACT-F04-001 — Extração controlada inicial de conhecimento.

# Objetivo: extrair conceitos, regras, condições, exceções, eventos, papéis, métricas, evidências e dúvidas das fontes segmentadas, mantendo rastreabilidade até cada segmento de origem.

# Entradas autorizadas: registros SRC-F03-001 a SRC-F03-065 e matriz de autoridade vigente, observadas as ressalvas deste portão.

# Estado: PRONTO.

# Saídas esperadas: unidades de conhecimento tipadas, origem segmental, nível de autoridade, estado de validação, conflitos, dúvidas e bloqueios.

# Limite: não converter itens extraídos em requisito normativo, constraint de banco, modelo aprovado ou implementação.

# 

# Portão A: APROVADO\_COM\_RESSALVAS.

# Fase 4: ABERTA\_PARA\_EXTRAÇÃO\_CONTROLADA.

# Fases de requisitos, modelagem e implementação: BLOQUEADAS quando dependentes das ressalvas.

# 

# C21. DECISÃO HUMANA — OFICIALIDADE E VIGÊNCIA DO REGULAMENTO CBHb 2026

# 

# Data da decisão: 31 de julho de 2026.

# Autoridade da decisão: proprietário do projeto.

# Fonte afetada: regulamento\_cbhb\_2026.pdf, ID 1kh3-GuC\_vuJ65lFBpt7cSNOvIVFrX3WG.

# 

# DECISÃO

# O Regulamento 2026 do Circuito Brasileiro Adulto de Handebol de Praia da CBHb já está vigente e deverá ser considerado fonte oficial aplicável.

# 

# EFEITOS

# • Classificação de autoridade: A2 — norma oficial nacional da CBHb.

# • Vigência formal: CONFIRMADA por decisão humana registrada.

# • Aplicabilidade: Circuito Brasileiro Adulto de Handebol de Praia 2026, dentro da jurisdição e do escopo definidos pelo próprio regulamento.

# • A ressalva anterior de “vigência formal pendente” fica SUPERADA e não deverá bloquear extração, requisitos ou regras que estejam expressamente sustentados pelo regulamento.

# • As expressões “Colocar aqui o link das regras oficiais” e “Levar esse parágrafo para os advogados da CBHb” permanecem registradas como marcas editoriais internas, mas não retiram a oficialidade nem a vigência do documento.

# • As marcas editoriais não constituem regra normativa autônoma e não deverão ser convertidas em requisito, obrigação ou restrição de banco.

# • Em conflito material com regras universais da modalidade, deverá ser aplicada a hierarquia de autoridade e jurisdição já definida no CEPRAEA-DB, preservando a primazia normativa da IHF no âmbito universal e a competência da CBHb no circuito nacional.

# 

# CONTROLE SUBSTITUÍDO

# A ressalva obrigatória do Portão A que determinava manter o regulamento CBHb 2026 com vigência formal pendente passa ao estado SUBSTITUÍDO por esta decisão humana.

# 

# ESTADO RESULTANTE

# Regulamento CBHb 2026: OFICIAL\_VIGENTE.

# Pendência de vigência: ENCERRADA.

# Observação editorial: ATIVA, sem efeito suspensivo.

# 

# C21.1 REGRA EXPLÍCITA DE SUBSTITUIÇÃO DAS CLASSIFICAÇÕES ANTERIORES

# A decisão humana registrada em C21 substitui, para todos os efeitos operacionais, todas as classificações, ressalvas, pendências, limitações e observações anteriores que atribuam ao Regulamento CBHb 2026 qualquer estado de vigência pendente, publicação final a confirmar, versão final não confirmada, uso condicionado à validação humana ou impedimento equivalente.

# Esta substituição alcança expressamente os registros históricos e operacionais constantes de C16, C18, C19 e C20, incluindo PEN-F02-001, PEN-F02-009, SRC-F03-031, o item 6 de C19.5, LIM-F03-005 e a ressalva obrigatória nº 3 do Portão A.

# Esses registros anteriores permanecem preservados como histórico, mas seu conteúdo relativo à pendência de vigência passa ao estado SUBSTITUÍDO e não poderá ser usado para bloquear, limitar ou rebaixar a extração de conhecimento sustentada pelo Regulamento CBHb 2026.

# Estado vigente e único para a fonte: A2 — NORMA\_OFICIAL\_NACIONAL; OFICIAL\_VIGENTE; aplicável ao Circuito Brasileiro Adulto de Handebol de Praia 2026, dentro da jurisdição e do escopo do próprio regulamento.

# As marcas editoriais internas permanecem apenas como observações de qualidade documental, sem efeito suspensivo e sem constituir regra normativa autônoma.

# 

## C22. EXECUÇÃO DA ACT-F04-001.1 — ESQUEMA DAS UNIDADES DE CONHECIMENTO

# 

# C22.1 Abertura e registro da subação

# Ação-mãe: ACT-F04-001 — Extração controlada inicial de conhecimento.

# Transição da ação-mãe: PRONTO → EM\_EXECUÇÃO.

# Subação: ACT-F04-001.1 — Definir o esquema das unidades de conhecimento.

# Natureza do identificador: decomposição interna rastreável da ação-mãe; não constitui ação independente fora da Fase 4.

# Objetivo: estabelecer o formato obrigatório de cada item extraído antes de iniciar a leitura analítica das fontes.

# Entradas autorizadas: C1.7, C3, C5, C7, C20, C21 e registros SRC-F03-001 a SRC-F03-065.

# Limite: esta subação define a representação documental do conhecimento; não extrai ainda o conteúdo substantivo das fontes e não define tabela, coluna, tipo PostgreSQL, constraint, SQL, migration, policy ou modelo aprovado.

# 

# C22.2 Princípios e invariantes do esquema

# 1\. Cada unidade representa uma afirmação, conceito, relação, pergunta, risco, evidência ou outro objeto semântico individualizável.

# 2\. O enunciado normalizado da unidade deve permanecer separado do texto ou da síntese fiel da fonte.

# 3\. Toda unidade deve possuir pelo menos uma origem composta por fonte e segmento; unidade sem origem não pode ser PRODUZIDA.

# 4\. Uma unidade pode possuir múltiplas origens, preservadas individualmente, sem fusão ou apagamento da proveniência.

# 5\. Autoridade da fonte, confiança da extração e estado da unidade são dimensões diferentes e não podem ser inferidas umas das outras.

# 6\. Temporalidade, jurisdição e aplicabilidade devem ser expressas; a ausência de informação não pode ser ocultada.

# 7\. Conflitos, dúvidas e limitações devem permanecer vinculados à unidade afetada.

# 8\. O esquema não autoriza requisitos, cardinalidades definitivas, decisões de modelagem ou restrições de banco.

# 9\. O campo de estado aceita somente os estados definidos em C5.

# 10\. Texto da fonte, síntese fiel e interpretação da IA não podem ser misturados no mesmo campo.

# 

# C22.3 Esquema canônico da unidade de conhecimento

# 

# Bloco A — Identidade e classificação

# 1\. unidade\_id — obrigatório. Formato: UC-F04-nnnnnn. Identificador estável, único e não reutilizável.

# 2\. tipo\_semantico\_principal — obrigatório. Deve usar um dos tipos de C1.7.

# 3\. subtipo\_semantico — opcional ou A\_CONFIRMAR. Refinamento controlado, sem substituir o tipo principal.

# 4\. ação\_origem — obrigatório. Identifica a subação da ACT-F04-001 que produziu ou alterou a unidade.

# 

# Bloco B — Conteúdo representado

# 5\. enunciado\_normalizado — obrigatório. Formulação curta e semanticamente controlada do conhecimento extraído.

# 6\. natureza\_da\_normalização — obrigatório. Valores: TRANSCRIÇÃO\_CONTROLADA; SÍNTESE\_FIEL; NORMALIZAÇÃO\_TERMINOLÓGICA; HIPÓTESE\_DA\_IA. HIPÓTESE\_DA\_IA nunca possui autoridade própria.

# 7\. escopo\_do\_enunciado — obrigatório. Delimita objeto, população, competição, evento, situação ou contexto ao qual o enunciado se aplica.

# 8\. nota\_interpretativa — opcional. Deve ser explicitamente identificada como interpretação e nunca substituir o conteúdo da fonte.

# 

# Bloco C — Proveniência, com cardinalidade de uma ou mais origens

# 9\. origens — obrigatório, mínimo de uma origem. Cada origem deve conter:

# a. fonte\_id — obrigatório, no formato SRC-F03-xxx;

# b. segmento\_id — obrigatório, no formato SEG-F03-xxx-...;

# c. texto\_ou\_sintese\_fiel — obrigatório; citação curta permitida ou síntese fiel sem alteração de sentido;

# d. idioma\_do\_segmento — obrigatório ou A\_CONFIRMAR;

# e. localizador\_adicional — página, artigo, regra, linha, tabela, figura ou posição equivalente, quando disponível;

# f. método\_de\_obtenção — EXTRAÇÃO\_TEXTUAL; LEITURA\_TABULAR; INSPEÇÃO\_VISUAL; LEITURA\_ESTRUTURAL;

# g. limitação\_da\_origem — NÃO\_APLICÁVEL quando inexistente, ou descrição explícita da limitação.

# 

# Bloco D — Autoridade, contexto e temporalidade

# 10\. classe\_de\_autoridade — obrigatório. Usa a matriz vigente: A1; A2; A3; O1; O2; E1; T1; H1; R1; P1; A\_CONFIRMAR; NÃO\_APLICÁVEL.

# 11\. emissor\_ou\_autoria — obrigatório, admitindo NÃO\_DECLARADO ou A\_CONFIRMAR quando a fonte não informar de modo suficiente.

# 12\. jurisdição — obrigatório. Exemplos controlados: UNIVERSAL\_IHF; NACIONAL\_CBHB; ESTADUAL\_FHERJ; COMPETIÇÃO\_ESPECÍFICA; EQUIPE\_CEPRAEA; CONTEXTO\_CIENTÍFICO\_DA\_AMOSTRA; CONTEXTO\_TÉCNICO\_DO\_MATERIAL; HISTÓRICA; NÃO\_APLICÁVEL; A\_CONFIRMAR.

# 13\. aplicabilidade — obrigatório. Deve registrar o contexto concreto de uso e pode assumir NÃO\_APLICÁVEL ou A\_CONFIRMAR.

# 14\. vigência\_ou\_contexto\_temporal — obrigatório. Registra data, intervalo, edição, temporada, evento, condição histórica, NÃO\_APLICÁVEL ou A\_CONFIRMAR.

# 

# Bloco E — Controle da extração

# 15\. estado\_da\_unidade — obrigatório. Valores exclusivos de C5: NÃO\_INICIADO; IDENTIFICADO; PRONTO; EM\_EXECUÇÃO; PRODUZIDO; EM\_REVISÃO; VALIDADO; REJEITADO; BLOQUEADO; IMPLEMENTADO; TESTADO; VERIFICADO; SUBSTITUÍDO.

# 16\. grau\_de\_confiança — obrigatório. Valores: ALTA; MÉDIA; BAIXA; NÃO\_AVALIADA. Confiança mede fidelidade e clareza da extração, não autoridade normativa.

# 17\. justificativa\_da\_confiança — obrigatória para ALTA, MÉDIA ou BAIXA.

# 18\. conflitos\_ou\_duvidas — obrigatório. Valor NÃO\_APLICÁVEL quando inexistentes; caso contrário, lista identificada de conflito, dúvida ou lacuna.

# 19\. motivo\_de\_bloqueio — obrigatório somente quando estado\_da\_unidade = BLOQUEADO; nos demais estados, NÃO\_APLICÁVEL.

# 20\. limitações — obrigatório. Valor NÃO\_APLICÁVEL quando não houver limitação conhecida.

# 

# Bloco F — Relações e histórico

# 21\. relações\_com\_outras\_unidades — obrigatório. Pode ser lista vazia controlada. Cada relação deve preservar unidade de destino, natureza da relação, justificativa, origem e estado; o vocabulário fechado das relações será definido na ACT-F04-001.2.

# 22\. substitui\_ou\_e\_substituida\_por — obrigatório. Valor NÃO\_APLICÁVEL ou identificadores das unidades relacionadas, preservando histórico.

# 23\. evidencias\_associadas — obrigatório. Referências a evidências EVD, testes ou decisões humanas aplicáveis; pode usar A\_CONFIRMAR durante produção inicial.

# 24\. responsável\_pela\_revisão — obrigatório. Pode assumir A\_CONFIRMAR até designação humana.

# 25\. data\_ou\_revisão\_do\_registro — obrigatório. Registra data e revisão documental da criação ou alteração.

# 

# C22.4 Domínio completo do tipo semântico principal

# O campo tipo\_semantico\_principal cobre integralmente os 28 tipos semânticos obrigatórios enumerados em C1.7 e aceita somente: fonte normativa; fonte regulatória local; fonte científica; material técnico; requisito operacional; conceito; entidade candidata; atributo; evento; papel; estado; relação; cardinalidade; regra; condição; exceção; proibição; obrigação; cálculo; métrica; evidência; fato histórico; hipótese; decisão; dúvida; risco; controle; teste.

# 

# Regras de uso:

# • “requisito operacional” identifica necessidade operacional documentada, não requisito do PWA validado.

# • “entidade candidata”, “atributo” e “cardinalidade” permanecem hipóteses semânticas e não autorizam modelo de banco.

# • “regra”, “obrigação”, “proibição”, “condição” e “exceção” exigem autoridade e jurisdição expressas.

# • “evidência”, “fonte científica” e “métrica” não se tornam normas por frequência ou significância estatística.

# • “decisão” exige autoridade decisória identificada; inferência da IA deve ser classificada como hipótese.

# 

# C22.5 Valores explícitos para ausência, pendência e bloqueio

# NÃO\_DECLARADO — a própria fonte não declara o dado; não autoriza inferência.

# A\_CONFIRMAR — há indício ou necessidade de verificação, mas não há confirmação suficiente.

# NÃO\_APLICÁVEL — o campo não possui significado no contexto específico da unidade.

# BLOQUEADO — estado de C5 usado quando conflito, ausência crítica ou condição de parada impede avanço da unidade. Deve possuir motivo\_de\_bloqueio e não pode ser usado como substituto genérico de dado ausente.

# 

# C22.6 Modelo textual obrigatório para criação de unidades

# unidade\_id: UC-F04-nnnnnn

# tipo\_semantico\_principal:

# subtipo\_semantico:

# ação\_origem:

# enunciado\_normalizado:

# natureza\_da\_normalização:

# escopo\_do\_enunciado:

# nota\_interpretativa:

# origens:

# \- fonte\_id: SRC-F03-xxx

# segmento\_id: SEG-F03-xxx-...

# texto\_ou\_sintese\_fiel:

# idioma\_do\_segmento:

# localizador\_adicional:

# método\_de\_obtenção:

# limitação\_da\_origem:

# classe\_de\_autoridade:

# emissor\_ou\_autoria:

# jurisdição:

# aplicabilidade:

# vigência\_ou\_contexto\_temporal:

# estado\_da\_unidade:

# grau\_de\_confiança:

# justificativa\_da\_confiança:

# conflitos\_ou\_duvidas:

# motivo\_de\_bloqueio:

# limitações:

# relações\_com\_outras\_unidades:

# substitui\_ou\_e\_substituida\_por:

# evidencias\_associadas:

# responsável\_pela\_revisão:

# data\_ou\_revisão\_do\_registro:

# 

# C22.7 Critérios de aceitação e testes executados

# TST-F04-001 — Cobertura de C1.7: comparação por igualdade entre o conjunto literal dos 28 tipos de C1.7 e o domínio de tipo\_semantico\_principal em C22.4. Resultado: 28/28 tipos; 0 faltantes; 0 excedentes; 0 duplicados; igualdade de conjuntos confirmada. Resultado final: APROVADO.

# TST-F04-002 — Proveniência obrigatória: fonte\_id e segmento\_id são obrigatórios em cada origem, com cardinalidade mínima de uma origem por unidade. Resultado: APROVADO.

# TST-F04-003 — Explicitação de controle: autoridade, jurisdição, aplicabilidade, temporalidade, estado, confiança, conflitos e limitações possuem campos próprios. Resultado: APROVADO.

# TST-F04-004 — Valores de ausência e bloqueio: NÃO\_DECLARADO, A\_CONFIRMAR, NÃO\_APLICÁVEL e BLOQUEADO possuem significado e uso explícitos. Resultado: APROVADO.

# TST-F04-005 — Fronteira tecnológica: o esquema não contém tabela física, coluna física, tipo PostgreSQL, chave, constraint, SQL, migration, trigger ou policy. Resultado: APROVADO.

# TST-F04-006 — Proveniência múltipla: origens admite uma ou mais ocorrências, preservadas individualmente. Resultado: APROVADO.

# TST-F04-007 — Separação semântica: enunciado\_normalizado, texto\_ou\_sintese\_fiel e nota\_interpretativa são campos distintos. Resultado: APROVADO.

# TST-F04-008 — Máquina de estados: estado\_da\_unidade usa exclusivamente a taxonomia de C5. Resultado: APROVADO.

# 

# C22.8 Impacto gerado

# Impacto: ALTO e transversal. O esquema passa a governar o catálogo de conhecimento, a consolidação da Fase 5, a descoberta de requisitos, a matriz de rastreabilidade, a modelagem e a derivação de testes.

# Efeito positivo esperado: uniformidade, rastreabilidade bidirecional, preservação de autoridade e temporalidade, separação entre fonte e interpretação e redução de retrabalho.

# Impacto de erro: uma omissão estrutural poderá propagar perda de contexto, regras sem exceção, relações sem origem ou promoção indevida de hipóteses nas fases posteriores.

# Controle de mudança: alteração futura do esquema deverá preservar os identificadores existentes, registrar versão, motivo, impacto e compatibilidade com unidades já produzidas.

# 

# C22.9 Riscos e controles aplicados

# RSK-F04-001 — Esquema simples demais perder condições e exceções. Controle: tipos próprios para regra, condição, exceção, obrigação, proibição, consequência por relação e campos de escopo e temporalidade.

# RSK-F04-002 — Esquema complexo demais tornar a extração impraticável. Controle: seis blocos funcionais, núcleo obrigatório e campos condicionais somente quando aplicáveis.

# RSK-F04-003 — Mistura entre fonte e interpretação da IA. Controle: separação obrigatória entre texto\_ou\_sintese\_fiel, enunciado\_normalizado e nota\_interpretativa.

# RSK-F04-004 — Unidade sem proveniência. Controle: cardinalidade mínima de uma origem, com fonte\_id e segmento\_id obrigatórios.

# RSK-F04-005 — Antecipação do banco. Controle: proibição expressa de campos físicos, SQL, constraints e decisões de modelagem.

# RSK-F04-006 — Uso de estados não previstos. Controle: domínio fechado pela taxonomia C5 e teste TST-F04-008.

# RSK-F04-007 — Confusão entre confiança e autoridade. Controle: campos distintos e regra explícita de não inferência entre as dimensões.

# RSK-F04-008 — Perda de proveniência em consolidação de múltiplas fontes. Controle: origens repetíveis e individualizadas; nenhuma fusão elimina a fonte original.

# 

# C22.10 Evidências e estado resultante

# EVD-F04-001 — esquema canônico com 25 campos organizados em seis blocos funcionais.

# EVD-F04-002 — domínio de tipo semântico confrontado com C1.7; cobertura material de 28/28 tipos e igualdade integral dos conjuntos confirmadas.

# EVD-F04-003 — modelo textual reutilizável para criação das unidades UC-F04-nnnnnn.

# EVD-F04-004 — testes TST-F04-001 a TST-F04-008 executados e aprovados.

# Resultado da ACT-F04-001.1: PRODUZIDO.

# Estado da ação-mãe ACT-F04-001: EM\_EXECUÇÃO.

# A subação não está VALIDADA automaticamente; o esquema poderá seguir para revisão durante a Fase 4 e no Portão B.

# Extração substantiva das fontes: NÃO\_INICIADA nesta subação.

# Próxima subação controlada: ACT-F04-001.2 — definir o vocabulário de classificação semântica.

# Estado da ACT-F04-001.2: PRONTO.

# Portão B — Conhecimento: PENDENTE.

# 

# C22.11 EXECUÇÃO DA ACT-F04-001.1.1 — RECONCILIAÇÃO DA LINHA DE BASE DE C1.7

# Identificador: ACT-F04-001.1.1.

# Nome: corrigir e comprovar a cobertura dos tipos semânticos obrigatórios de C1.7.

# Objetivo: reconciliar formalmente C1.7, C22.4 e TST-F04-001, corrigindo a contagem declarada sem criar, remover ou fundir tipos semânticos.

# Entradas examinadas: lista literal de C1.7; domínio aceito por tipo\_semantico\_principal em C22.4; teste TST-F04-001; evidência EVD-F04-002.

# Método: extração literal das duas listas; normalização limitada a espaços e pontuação terminal; preservação integral dos nomes e da ordem; comparação por igualdade de conjuntos e verificação separada de contagem e duplicidade.

# 

# C22.11.1 Matriz de reconciliação

# Formato: nº | tipo em C1.7 | presente em C22 | grafia idêntica | definição pendente | resultado.

# 01 | fonte normativa | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 02 | fonte regulatória local | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 03 | fonte científica | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 04 | material técnico | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 05 | requisito operacional | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 06 | conceito | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 07 | entidade candidata | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 08 | atributo | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 09 | evento | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 10 | papel | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 11 | estado | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 12 | relação | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 13 | cardinalidade | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 14 | regra | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 15 | condição | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 16 | exceção | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 17 | proibição | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 18 | obrigação | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 19 | cálculo | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 20 | métrica | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 21 | evidência | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 22 | fato histórico | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 23 | hipótese | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 24 | decisão | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 25 | dúvida | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 26 | risco | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 27 | controle | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 28 | teste | SIM | SIM | SIM — ACT-F04-001.2 | COBERTO.

# 

# C22.11.2 Resultado quantitativo e material

# Tipos enumerados em C1.7: 28.

# Tipos aceitos por C22.4: 28.

# Tipos faltantes em C22.4: 0.

# Tipos excedentes em C22.4: 0.

# Tipos duplicados em C1.7: 0.

# Tipos duplicados em C22.4: 0.

# Igualdade de conjuntos: CONFIRMADA.

# Cobertura material: 28/28 — 100%.

# Não existe 29º tipo omitido: a divergência era exclusivamente uma contagem declarada incorreta em TST-F04-001.

# 

# C22.11.3 Teste revisado

# TST-F04-001 — Cobertura de C1.7.

# Método: comparação por igualdade entre o conjunto literal dos 28 tipos de C1.7 e o domínio permitido para tipo\_semantico\_principal em C22.4, com verificação separada de faltantes, excedentes e duplicados.

# Resultado: 28 tipos em C1.7; 28 tipos em C22.4; 0 faltantes; 0 excedentes; 0 duplicados em cada lista; igualdade de conjuntos confirmada.

# Resultado final: APROVADO.

# O enunciado anterior que declarava 29 tipos fica CORRIGIDO por esta execução e preservado no histórico de revisões do documento; não constitui novo tipo, alteração taxonômica ou mudança de significado.

# 

# C22.11.4 Evidência da comparação

# EVD-F04-005 — Reconciliação da cobertura semântica.

# Ação de origem: ACT-F04-001.1.1.

# Data: 1º de agosto de 2026.

# Objeto: domínio de tipo\_semantico\_principal e sua correspondência com C1.7.

# Método de obtenção: extração literal, comparação de conjuntos e inspeção de duplicidade.

# Localização: C1.7; C22.4; TST-F04-001; EVD-F04-002.

# Resultado: igualdade integral de 28/28 tipos; nenhuma ausência, extensão não autorizada, fusão ou duplicidade.

# Limitação: as definições, fronteiras, exemplos e relações dos 28 tipos permanecem como saída da ACT-F04-001.2.

# Responsável pela validação: proprietário do projeto ou responsável humano designado.

# Estado: VERIFICADO após readback.

# EVD-F04-006 — Readback da correção da linha de base de C1.7.

# Ação de origem: ACT-F04-001.1.1.

# Método: localização posterior das redações corrigidas em C1.7, C22.4 e TST-F04-001; confirmação do registro C22.11; busca negativa da expressão anterior “todos os 29 tipos semânticos obrigatórios”.

# Resultado: lista numerada de 28 tipos localizada; cobertura de 28 tipos em C22.4 localizada; teste por igualdade de conjuntos localizado; C22.11 persistido; expressão incorreta não localizada.

# Revisão verificada: AIroW35cCLIWvSHuanmrI3CDdAW3ah2iP-Pn\_5tAJwIm5uqIeA3uacA\_ipV766fHreSbb3Jk21b5LVwVT2gRLw.

# Estado: VERIFICADO.

# 

# C22.11.5 Registro de correção e preservação histórica

# A cobertura material anterior já continha os mesmos 28 tipos de C1.7. O erro estava apenas na expressão “29 tipos” do teste original.

# Nenhum tipo foi criado, removido, renomeado ou fundido.

# A correção não altera o significado, a autoridade nem a taxonomia estrutural de C1.7.

# O teste anterior foi corrigido explicitamente e a causa da correção permanece registrada nesta seção e no histórico de revisões.

# Não foi acrescentado tipo artificial para alcançar a contagem 29.

# 

# C22.11.6 Riscos e controles executados

# Risco: corrigir somente o número sem comparar o conteúdo. Controle: matriz linha a linha e igualdade de conjuntos.

# Risco: criar um 29º tipo artificial. Controle: domínio de C22 limitado à lista literal de C1.7.

# Risco: fundir tipos semanticamente distintos. Controle: preservação da grafia e da posição individual dos 28 elementos.

# Risco: apagar a inconsistência histórica. Controle: registro explícito da correção, causa, impacto e teste substituído.

# 

# C22.11.7 Critérios de aceitação

# C1.7 possui lista numerada de 28 tipos: ATENDIDO.

# C22.4 aceita exatamente os mesmos 28 tipos: ATENDIDO.

# Tipos faltantes: 0 — ATENDIDO.

# Tipos excedentes: 0 — ATENDIDO.

# Tipos duplicados: 0 — ATENDIDO.

# Referências materiais à contagem incorreta na seção C22 corrigidas: ATENDIDO.

# TST-F04-001 passou a usar comparação de conjuntos: ATENDIDO.

# Evidência e readback: ATENDIDO por EVD-F04-005 e EVD-F04-006.

# Nenhum novo tipo criado sem mudança formal de C1.7: ATENDIDO.

# 

# C22.11.8 Estado resultante

# Resultado da ACT-F04-001.1.1: PRODUZIDO.

# Estado da ACT-F04-001.1: PRODUZIDO.

# Estado da ação-mãe ACT-F04-001: EM\_EXECUÇÃO.

# ACT-F04-001.1 não é promovida para EM\_REVISÃO nesta execução; permanecem necessárias as complementações previstas, especialmente ACT-F04-001.2.

# Estado da ACT-F04-001.2: PRONTO.

# Portão B — Conhecimento: PENDENTE.

# 

# C23. EXECUÇÃO DA ACT-F04-001.2 — VOCABULÁRIO SEMÂNTICO E RELACIONAL

# 

# C23.1 Registro da subação

# 

# Identificador: ACT-F04-001.2.

# Nome: definir o vocabulário semântico e relacional.

# Objetivo: produzir um vocabulário controlado, verificável e utilizável por qualquer executor para classificar cada unidade em exatamente um dos 28 tipos de C1.7, distinguir tipos próximos e registrar relações direcionais sem confundir fonte, regra, evidência, hipótese, decisão, requisito ou implementação.

# Entradas autorizadas: C1.7; C3; C5; C7; C9; C20; C21; C22; ACT-F04-001.1.1; especificação da subação fornecida pelo proprietário do projeto.

# Precondições: ACT-F04-001 em EM\_EXECUÇÃO; ACT-F04-001.1 e ACT-F04-001.1.1 em PRODUZIDO; igualdade material 28/28 entre C1.7 e C22.4; Portão A APROVADO\_COM\_RESSALVAS para extração controlada.

# Limite: esta subação define significados, fronteiras, exemplos e relações; não extrai integralmente as fontes, não valida requisitos do PWA e não cria tabela, coluna, chave, tipo PostgreSQL, constraint, SQL, migration, trigger, policy ou modelo aprovado.

# Procedimento executado: definir os 28 tipos; explicitar inclusão e exclusão; registrar exemplos positivos e negativos; comparar pares confundíveis; definir a seleção do tipo principal; estabelecer 29 relações direcionais; executar testes de cobertura, exclusividade, diferenciação, fronteira tecnológica e completude relacional.

# 

# C23.2 Regras gerais de classificação

# 

# 1\. Cada unidade deve possuir exatamente um tipo\_semantico\_principal de C1.7.

# 2\. subtipo\_semantico refina o tipo principal, mas não o substitui e não autoriza múltiplos tipos principais.

# 3\. Quando um segmento contiver afirmações semanticamente independentes, devem ser criadas unidades separadas.

# 4\. O tipo é determinado pela natureza da afirmação representada, não pelo formato do arquivo, pela tela futura ou pela possível tabela de banco.

# 5\. Autoridade, confiança, estado, jurisdição e aplicabilidade não determinam automaticamente o tipo, embora possam limitar seu uso.

# 6\. Se a classificação alterar autoridade, temporalidade, obrigação ou efeito operacional e permanecer ambígua, registrar DÚVIDA e manter a unidade em IDENTIFICADO, EM\_REVISÃO ou BLOQUEADO conforme o impacto.

# 7\. Relações vagas como RELACIONADO\_COM, TEM\_A\_VER\_COM, OUTRO, GERAL e DIVERSOS são proibidas.

# 8\. Relação documental e relação do domínio são distintas: TRADUZ, VERSÃO\_DE e CORRIGE tratam documentos ou unidades; PAPEL, RELAÇÃO e CARDINALIDADE representam conhecimento do domínio.

# 9\. Entidade candidata, atributo, relação e cardinalidade continuam hipóteses semânticas e não constituem modelo conceitual, lógico ou físico aprovado.

# 

# C23.3 Dicionário controlado dos 28 tipos semânticos

# 

# TIPO 01 — fonte normativa

# Definição: registro de documento ou segmento emitido por autoridade competente para estabelecer normas gerais ou oficiais.

# Finalidade: identificar a origem normativa antes de extrair suas regras.

# Pergunta de decisão: o item representa uma fonte oficial capaz de estabelecer normas no escopo declarado?

# Incluir quando: emissor competente, natureza normativa e escopo identificáveis.

# Excluir quando: o item apenas explica, comenta, traduz, registra evento ou apresenta evidência.

# Confusões: fonte regulatória local; regra; material técnico.

# Autoridade normalmente necessária: A1 ou A2; A3 somente quando o documento for normativo dentro da jurisdição local.

# Subtipos admitidos: livro de regras; regulamento nacional; norma institucional.

# Relações usuais: SUPORTA; ESTABELECE\_PROIBIÇÃO; IMPÕE\_OBRIGAÇÃO; VERSÃO\_DE.

# Exemplo positivo: “Regras oficiais IHF 2026” classificada como fonte normativa A1.

# Exemplo negativo: artigo científico que descreve frequências de finalização classificado como fonte normativa.

# 

# TIPO 02 — fonte regulatória local

# Definição: registro de regulamento, circular ou esclarecimento emitido por autoridade regional, estadual, federativa ou de competição, válido no seu escopo.

# Finalidade: preservar regras locais sem projetá-las como universais.

# Pergunta: o documento regula uma jurisdição ou competição delimitada?

# Incluir quando: emissor local competente, jurisdição e período identificados.

# Excluir quando: é regra universal, material didático ou simples registro de resultado.

# Confusões: fonte normativa; registro operacional; material técnico.

# Autoridade: normalmente A3; eventualmente A2 em competição nacional específica.

# Subtipos: regulamento estadual; circular; esclarecimento; regulamento de competição.

# Relações: ESPECIALIZA; COMPLEMENTA; APLICA\_SE\_A; CONTRADIZ.

# Positivo: regulamento FHERJ 2026 para o Circuito Estadual.

# Negativo: tabela de jogos tratada como fonte regulatória local.

# 

# TIPO 03 — fonte científica

# Definição: registro de estudo, artigo, tese, capítulo ou anais que emprega método científico para produzir conhecimento.

# Finalidade: identificar a origem de evidências, métricas e hipóteses sem convertê-las em norma.

# Pergunta: o item apresenta pergunta, método, dados ou análise científica?

# Incluir quando: método, amostra, resultados ou discussão científica são identificáveis.

# Excluir quando: é apresentação técnica sem método, regra oficial ou documento operacional.

# Confusões: evidência; material técnico; fato histórico.

# Autoridade: E1.

# Subtipos: artigo; tese; capítulo; anais; revisão.

# Relações: EVIDENCIA; SUPORTA; DERIVA\_DE; QUESTIONA.

# Positivo: artigo com método e resultados de análise notacional.

# Negativo: resultado de um estudo classificado como fonte científica em vez do documento que o contém.

# 

# TIPO 04 — material técnico

# Definição: documento ou segmento que ensina, recomenda ou demonstra métodos, exercícios, princípios ou procedimentos profissionais.

# Finalidade: capturar conhecimento técnico sem atribuir força normativa automática.

# Pergunta: o item orienta como executar, treinar, arbitrar ou organizar uma prática?

# Incluir quando: há orientação técnica, progressão, exercício ou recomendação.

# Excluir quando: há comando normativo de autoridade competente ou resultado científico formal.

# Confusões: obrigação; requisito operacional; fonte científica.

# Autoridade: T1; pode ter apoio E1 ou instituição técnica, sem virar norma.

# Subtipos: curso; guia técnico; exercício; recomendação; material educacional.

# Relações: EXEMPLIFICA; SUPORTA; DERIVA\_DE; COMPLEMENTA.

# Positivo: progressão de treino para spin shot.

# Negativo: “é aconselhável” classificado como obrigação normativa.

# 

# TIPO 05 — requisito operacional

# Definição: necessidade documentada para executar, gerir ou acompanhar uma atividade, ainda não validada como requisito do PWA.

# Finalidade: preservar necessidades reais sem antecipar produto ou banco.

# Pergunta: existe uma necessidade operacional concreta de registrar, consultar, comunicar ou controlar algo?

# Incluir quando: a necessidade decorre de operação, equipe, competição ou processo identificado.

# Excluir quando: é regra oficial, solução tecnológica escolhida ou requisito do PWA já validado.

# Confusões: obrigação; decisão; material técnico; requisito validado.

# Autoridade: O1, O2, P1 ou decisão humana competente, conforme o escopo.

# Subtipos: registro; consulta; comunicação; acompanhamento; controle operacional.

# Relações: DERIVA\_DE; DEPENDE\_DE; SUPORTA; POSSUI\_RISCO.

# Positivo: necessidade de registrar disponibilidade das atletas para uma etapa.

# Negativo: “criar coluna availability boolean” classificado como requisito operacional.

# 

# TIPO 06 — conceito

# Definição: significado abstrato ou definição de um termo relevante ao domínio.

# Finalidade: formar glossário e eliminar ambiguidade terminológica.

# Pergunta: a unidade explica o que algo significa?

# Incluir quando: há definição, noção ou distinção sem identidade própria obrigatória.

# Excluir quando: representa objeto com ciclo de vida, característica, ocorrência ou regra.

# Confusões: entidade candidata; atributo; papel; estado.

# Autoridade: qualquer classe pertinente; a fonte deve ser registrada.

# Subtipos: termo; definição; sinônimo; categoria conceitual.

# Relações: GENERALIZA; ESPECIALIZA; É\_SINÔNIMO\_CANDIDATO\_DE; É\_DISTINTO\_DE.

# Positivo: definição de shoot-out como procedimento de desempate.

# Negativo: atleta específica classificada como conceito.

# 

# TIPO 07 — entidade candidata

# Definição: objeto do domínio com identidade potencialmente própria, existência distinguível e possível ciclo de vida, ainda não aprovado como entidade de modelo.

# Finalidade: registrar candidatos conceituais para avaliação posterior.

# Pergunta: o objeto precisa ser distinguido de outros exemplares ao longo do tempo?

# Incluir quando: identidade, ocorrência ou ciclo de vida parecem relevantes.

# Excluir quando: é apenas característica, valor, estado, papel ou tabela imaginada.

# Confusões: conceito; atributo; evento; papel.

# Autoridade: sustentação documental ou operacional; não exige autoridade normativa.

# Subtipos: pessoa candidata; organização; competição; equipe; documento; sessão.

# Relações: POSSUI\_CONDIÇÃO; DEPENDE\_DE; ESPECIALIZA; POSSUI\_RISCO.

# Positivo: “competição” identificada como possível objeto com identidade e período.

# Negativo: “competitions” proposto como nome de tabela e tratado como entidade aprovada.

# 

# TIPO 08 — atributo

# Definição: característica descritiva, qualificadora ou mensurável de um conceito ou entidade candidata.

# Finalidade: registrar propriedades sem decidir coluna, tipo ou nulabilidade.

# Pergunta: a unidade descreve uma característica de outro objeto?

# Incluir quando: o valor qualifica ou descreve algo.

# Excluir quando: possui identidade própria, representa ocorrência, papel ou estado mutável relevante.

# Confusões: estado; métrica; entidade candidata.

# Autoridade: sustentação pela fonte ou necessidade operacional.

# Subtipos: descritivo; identificador conceitual; quantitativo; temporal.

# Relações: DEPENDE\_DE; LIMITA; EVIDENCIA.

# Positivo: categoria etária como característica declarada de uma competição.

# Negativo: definição de coluna category\_id como atributo nesta fase.

# 

# TIPO 09 — evento

# Definição: ocorrência localizada no tempo que altera ou registra uma situação.

# Finalidade: distinguir fatos ocorridos, programados ou cancelados de regras permanentes.

# Pergunta: algo aconteceu, está programado ou foi registrado em um momento?

# Incluir quando: há ocorrência, data ou transição observável.

# Excluir quando: é estado duradouro, regra, calendário abstrato ou fato histórico consolidado.

# Confusões: fato histórico; estado; decisão.

# Autoridade: O1, O2, P1, H1 ou fonte pertinente.

# Subtipos: programado; ocorrido; cancelado; corrigido; administrativo; esportivo.

# Relações: PRECEDE; SUCEDE; OCORRE\_DURANTE; DEPENDE\_DE.

# Positivo: jogo realizado em uma etapa específica.

# Negativo: tabela programada tratada automaticamente como evento ocorrido.

# 

# TIPO 10 — papel

# Definição: função contextual exercida por pessoa, grupo ou organização em uma relação ou período.

# Finalidade: separar identidade da pessoa de sua função temporária.

# Pergunta: a unidade descreve o que um participante faz ou representa em certo contexto?

# Incluir quando: a função depende de equipe, competição, documento ou período.

# Excluir quando: é pessoa, atributo permanente ou obrigação isolada.

# Confusões: entidade candidata; atributo; obrigação.

# Autoridade: fonte operacional, normativa ou decisão competente conforme o papel.

# Subtipos: atleta; treinador; dirigente; árbitro; responsável; emissor.

# Relações: DEPENDE\_DE; APLICA\_SE\_A; IMPÕE\_OBRIGAÇÃO.

# Positivo: uma pessoa exerce o papel de responsável pela equipe em uma etapa.

# Negativo: criar uma entidade “Treinador” definitiva apenas porque um documento cita o papel.

# 

# TIPO 11 — estado

# Definição: condição mutável em que uma unidade pode se encontrar durante um intervalo.

# Finalidade: representar situação atual ou histórica sem confundi-la com atributo permanente.

# Pergunta: o valor pode mudar mantendo-se a identidade do objeto?

# Incluir quando: há condição, fase ou situação mutável.

# Excluir quando: é característica estável, evento de transição ou estado operacional de C5 usado apenas no controle.

# Confusões: atributo; evento; decisão.

# Autoridade: fonte do domínio ou regra operacional correspondente.

# Subtipos: disponibilidade; inscrição; vigência; situação de jogo; estado de processo.

# Relações: PRECEDE; SUCEDE; DEPENDE\_DE; POSSUI\_CONDIÇÃO.

# Positivo: atleta disponível ou indisponível em determinado período.

# Negativo: data de nascimento classificada como estado.

# 

# TIPO 12 — relação

# Definição: associação semanticamente identificável entre duas ou mais unidades.

# Finalidade: registrar conexão de domínio ou documental sem definir chave estrangeira.

# Pergunta: qual vínculo com significado próprio conecta as unidades?

# Incluir quando: direção, participantes, contexto e origem podem ser explicitados.

# Excluir quando: é proximidade vaga, coocorrência textual ou implementação de join.

# Confusões: cardinalidade; atributo; relação documental vaga.

# Autoridade: fonte ou decisão que sustenta o vínculo.

# Subtipos: domínio; documental; temporal; causal candidata; normativa.

# Relações: todas as relações controladas de C23.6.

# Positivo: atleta participa de equipe durante uma temporada, como relação candidata temporal.

# Negativo: “atleta tem a ver com equipe”.

# 

# TIPO 13 — cardinalidade

# Definição: quantidade mínima, máxima, exata ou faixa observada ou determinada para participantes de uma relação.

# Finalidade: preservar limites quantitativos sem transformá-los prematuramente em constraint.

# Pergunta: a fonte determina ou observa quantos elementos podem ou devem participar?

# Incluir quando: quantidade e contexto são explícitos.

# Excluir quando: o número é apenas exemplo, tamanho de uma lista ou contagem circunstancial.

# Confusões: relação; métrica; cálculo; limite normativo.

# Autoridade: A1/A2/A3 para cardinalidade normativa; O1/O2/E1 para observada, sempre marcada como tal.

# Subtipos: normativa; observada; sugerida; desconhecida.

# Relações: LIMITA; SUPORTA; CONTRADIZ.

# Positivo: limite explicitamente declarado por regulamento, com jurisdição e vigência.

# Negativo: inferir limite universal de 12 atletas porque uma relação nominal possui 12 nomes.

# 

# TIPO 14 — regra

# Definição: enunciado geral que estabelece comportamento, consequência, cálculo, permissão ou restrição em certo escopo.

# Finalidade: representar prescrições sem perder condição, exceção, autoridade e temporalidade.

# Pergunta: o segmento estabelece o que ocorre, deve ocorrer ou é permitido em determinada situação?

# Incluir quando: há autoridade, escopo e efeito identificáveis.

# Excluir quando: é recomendação técnica, evidência, exemplo ou decisão sem alcance geral.

# Confusões: obrigação; proibição; condição; evidência.

# Autoridade: A1, A2 ou A3 para norma; decisão competente para regra interna delimitada.

# Subtipos: constitutiva; procedimental; permissiva; sancionatória; cálculo normativo.

# Relações: POSSUI\_CONDIÇÃO; POSSUI\_EXCEÇÃO; IMPÕE\_OBRIGAÇÃO; ESTABELECE\_PROIBIÇÃO; AUTORIZA; LIMITA.

# Positivo: regra oficial que define consequência de uma infração no escopo aplicável.

# Negativo: frequência observada em estudo classificada como regra.

# 

# TIPO 15 — condição

# Definição: circunstância necessária, suficiente ou contextual para que outra unidade se aplique.

# Finalidade: impedir aplicação de regra fora do contexto que a ativa.

# Pergunta: a afirmação principal somente vale se esta circunstância ocorrer?

# Incluir quando: a dependência lógica ou contextual está expressa.

# Excluir quando: é exceção, causa presumida, simples contexto ou sequência temporal sem efeito de ativação.

# Confusões: exceção; regra; estado; aplicabilidade.

# Autoridade: a mesma origem competente da regra ou decisão condicionada.

# Subtipos: necessária; suficiente; temporal; jurisdicional; operacional.

# Relações: CONDIÇÃO\_DE; APLICA\_SE\_A; DEPENDE\_DE.

# Positivo: uma penalidade aplica-se se a conduta definida ocorrer.

# Negativo: data do documento classificada como condição sem afetar a regra.

# 

# TIPO 16 — exceção

# Definição: caso delimitado que afasta, modifica ou substitui o efeito normal de uma regra.

# Finalidade: preservar desvios autorizados sem reescrever a regra geral.

# Pergunta: o caso declarado impede ou altera a aplicação normal da regra?

# Incluir quando: regra geral e tratamento excepcional são identificáveis.

# Excluir quando: é condição de ativação, conflito entre fontes ou erro editorial.

# Confusões: condição; regra especial; contradição.

# Autoridade: mesma autoridade competente da regra ou autoridade superior aplicável.

# Subtipos: pessoal; temporal; situacional; jurisdicional.

# Relações: EXCEÇÃO\_DE; LIMITA; ESPECIALIZA.

# Positivo: disposição que afasta uma regra geral em situação expressamente definida.

# Negativo: divergência de tradução tratada como exceção normativa.

# 

# TIPO 17 — proibição

# Definição: determinação de que um sujeito não pode executar determinada conduta em um contexto.

# Finalidade: individualizar condutas vedadas e suas condições.

# Pergunta: existe sujeito, conduta vedada e autoridade competente?

# Incluir quando: a vedação é explícita ou semanticamente inequívoca.

# Excluir quando: é recomendação de evitar, risco ou ausência de autorização inferida.

# Confusões: regra; obrigação; risco.

# Autoridade: A1/A2/A3 ou decisão interna competente para escopo restrito.

# Subtipos: normativa; operacional interna; disciplinar.

# Relações: ESTABELECE\_PROIBIÇÃO; POSSUI\_CONDIÇÃO; POSSUI\_EXCEÇÃO.

# Positivo: regulamento proíbe conduta especificada durante a competição.

# Negativo: “não é recomendado” convertido automaticamente em proibição.

# 

# TIPO 18 — obrigação

# Definição: determinação de que um sujeito deve executar uma conduta em certo contexto.

# Finalidade: individualizar dever, sujeito, objeto, prazo e condição.

# Pergunta: o segmento determina que alguém deve fazer algo, ou apenas recomenda?

# Incluir quando: sujeito obrigado, conduta, contexto e autoridade são identificáveis.

# Excluir quando: é conselho técnico, comportamento observado ou necessidade tecnológica presumida.

# Confusões: regra; requisito operacional; material técnico; decisão.

# Autoridade: A1/A2/A3 ou decisão interna competente e delimitada.

# Subtipos: fazer; entregar; manter; comunicar; registrar.

# Relações: IMPÕE\_OBRIGAÇÃO; POSSUI\_CONDIÇÃO; POSSUI\_EXCEÇÃO; DEPENDE\_DE.

# Positivo: “as equipes deverão apresentar a relação nominal até a data definida”.

# Negativo: “é aconselhável apresentar antecipadamente” classificado como obrigação.

# 

# TIPO 19 — cálculo

# Definição: procedimento explícito que transforma entradas em resultado por fórmula, algoritmo ou sequência de operações.

# Finalidade: preservar como um valor é obtido sem decidir implementação.

# Pergunta: existe regra reproduzível para calcular um resultado?

# Incluir quando: entradas, operação e saída são identificáveis.

# Excluir quando: é valor observado, indicador sem fórmula ou constraint imaginada.

# Confusões: métrica; regra; teste.

# Autoridade: fonte normativa, científica ou operacional que define o procedimento.

# Subtipos: aritmético; pontuação; agregação; normalização; classificação.

# Relações: DERIVA\_DE; SUPORTA; EVIDENCIA.

# Positivo: fórmula declarada de pontuação acumulada.

# Negativo: número final de pontos classificado como cálculo.

# 

# TIPO 20 — métrica

# Definição: medida quantitativa ou categórica utilizada para observar, comparar ou avaliar fenômeno.

# Finalidade: registrar significado, unidade, método e contexto da medida.

# Pergunta: a unidade representa o que é medido, e não apenas como calcular?

# Incluir quando: medida, unidade ou protocolo são identificáveis.

# Excluir quando: é fórmula, valor isolado, regra normativa ou objetivo de treino inferido.

# Confusões: cálculo; atributo; evidência.

# Autoridade: E1, T1, O1/O2 ou A1/A2/A3 conforme a origem, sem transferência normativa automática.

# Subtipos: desempenho; carga; frequência; proporção; tempo; pontuação.

# Relações: EVIDENCIA; DERIVA\_DE; SUPORTA; LIMITA.

# Positivo: distância total em metros medida por protocolo declarado.

# Negativo: média de uma amostra transformada em meta obrigatória.

# 

# TIPO 21 — evidência

# Definição: resultado, observação, dado ou trecho que sustenta ou enfraquece uma afirmação.

# Finalidade: separar prova ou indício do documento que a contém e da conclusão derivada.

# Pergunta: este conteúdo oferece suporte verificável a outra unidade?

# Incluir quando: origem, método e afirmação sustentada são identificáveis.

# Excluir quando: é a fonte inteira, regra oficial ou hipótese sem suporte.

# Confusões: fonte científica; fato histórico; decisão.

# Autoridade: E1, O1/O2, A1/A2/A3, H1 ou P1 conforme o objeto comprovado.

# Subtipos: científica; documental; operacional; histórica; teste.

# Relações: EVIDENCIA; SUPORTA; CONTRADIZ; QUESTIONA.

# Positivo: resultado de estudo que sustenta uma hipótese sobre padrões de finalização.

# Negativo: classificar o artigo inteiro como evidência e perder o segmento específico.

# 

# TIPO 22 — fato histórico

# Definição: afirmação sobre ocorrência, situação ou marco passado, sustentada por fonte contextual ou registro.

# Finalidade: preservar contexto temporal sem projetá-lo como estado atual ou regra vigente.

# Pergunta: a afirmação descreve algo passado como parte de uma narrativa ou registro consolidado?

# Incluir quando: evento passado, período e fonte são identificáveis.

# Excluir quando: é evento individual ainda em processamento, regra antiga ou opinião retrospectiva.

# Confusões: evento; estado; fonte histórica.

# Autoridade: H1, O1/O2 ou fonte documental pertinente.

# Subtipos: marco; evolução; resultado passado; contexto institucional.

# Relações: PRECEDE; SUCEDE; SUPORTA; CONTRADIZ.

# Positivo: registro de que uma competição ocorreu em 2025.

# Negativo: usar o fato de 2025 como configuração atual de 2026.

# 

# TIPO 23 — hipótese

# Definição: proposição provisória a ser verificada, sem autoridade decisória própria.

# Finalidade: preservar inferências e explicações possíveis sem apresentá-las como fato.

# Pergunta: a afirmação ainda requer teste, evidência ou decisão para ser aceita?

# Incluir quando: existe proposição verificável e incerteza explícita.

# Excluir quando: há decisão aprovada, evidência direta ou regra vigente.

# Confusões: dúvida; decisão; conclusão científica.

# Autoridade: não possui autoridade própria; deve indicar origens e confiança.

# Subtipos: explicativa; classificatória; relacional; de aplicabilidade.

# Relações: SUPORTA; QUESTIONA; POSSUI\_DÚVIDA; EVIDENCIA.

# Positivo: hipótese de que duas renderizações representam a mesma edição, pendente de comparação.

# Negativo: tratar a hipótese como duplicidade binária confirmada.

# 

# TIPO 24 — decisão

# Definição: escolha formal entre alternativas realizada por autoridade competente e registrada com escopo e efeitos.

# Finalidade: distinguir escolha aprovada de hipótese, preferência ou inferência.

# Pergunta: quem decidiu, com qual autoridade, sobre qual questão e com que efeito?

# Incluir quando: decisor, questão, decisão, justificativa e escopo são identificáveis.

# Excluir quando: é opinião, sugestão, hipótese da IA ou regra externa.

# Confusões: regra; hipótese; requisito operacional.

# Autoridade: proprietário do projeto ou responsável humano competente segundo C3.

# Subtipos: domínio; produto; escopo; governança; técnica futura.

# Relações: SUBSTITUI; AUTORIZA; LIMITA; SUPORTA.

# Positivo: C21 confirma oficialmente a vigência do regulamento CBHb 2026.

# Negativo: interpretação da IA classificada como decisão humana.

# 

# TIPO 25 — dúvida

# Definição: questão não resolvida decorrente de ausência, ambiguidade ou necessidade de confirmação.

# Finalidade: impedir resolução silenciosa de lacunas.

# Pergunta: qual informação falta para classificar, aplicar ou avançar com segurança?

# Incluir quando: questão, impacto e ação de resolução podem ser expressos.

# Excluir quando: há consequência futura incerta, hipótese explicativa ou conflito já comprovado.

# Confusões: risco; hipótese; bloqueio.

# Autoridade: não aplicável; a resolução exige fonte ou autoridade indicada.

# Subtipos: factual; normativa; temporal; terminológica; documental.

# Relações: POSSUI\_DÚVIDA; QUESTIONA; DEPENDE\_DE.

# Positivo: dúvida sobre equivalência exata entre duas versões sem hash.

# Negativo: “talvez esteja certo” sem questão, impacto ou ação.

# 

# TIPO 26 — risco

# Definição: possibilidade de evento ou condição futura causar impacto negativo sobre objetivo, qualidade, segurança ou decisão.

# Finalidade: ligar ameaça, consequência, probabilidade qualitativa e controle.

# Pergunta: o que pode ocorrer, qual impacto geraria e como será controlado?

# Incluir quando: causa, evento, impacto e controle são identificáveis.

# Excluir quando: é dado ausente, problema já ocorrido ou simples dúvida.

# Confusões: dúvida; conflito; limitação.

# Autoridade: governança do projeto ou fonte que sustenta o risco.

# Subtipos: semântico; documental; operacional; privacidade; tecnológico futuro.

# Relações: POSSUI\_RISCO; LIMITA; DEPENDE\_DE.

# Positivo: risco de converter recomendação científica em obrigação normativa.

# Negativo: autoria não declarada classificada como risco sem descrever consequência.

# 

# TIPO 27 — controle

# Definição: medida preventiva, detectiva ou corretiva destinada a reduzir risco ou assegurar regra de processo.

# Finalidade: tornar mitigação executável e verificável.

# Pergunta: qual ação concreta previne, detecta ou corrige o problema?

# Incluir quando: risco ou objetivo controlado, responsável e evidência são identificáveis.

# Excluir quando: é intenção vaga, teste isolado ou solução física prematura.

# Confusões: teste; decisão; requisito operacional.

# Autoridade: C0–C13, decisão humana ou ação controlada aplicável.

# Subtipos: preventivo; detectivo; corretivo; compensatório.

# Relações: SUPORTA; LIMITA; DEPENDE\_DE; POSSUI\_RISCO.

# Positivo: exigir SRC e SEG antes de permitir estado PRODUZIDO.

# Negativo: “ter cuidado com a fonte” classificado como controle suficiente.

# 

# TIPO 28 — teste

# Definição: procedimento com entrada, condição, execução e resultado esperado para verificar afirmação, controle ou artefato.

# Finalidade: produzir evidência reproduzível de atendimento ou falha.

# Pergunta: existe método executável e critério objetivo de aprovação?

# Incluir quando: objeto, método, resultado esperado e resultado observado são identificáveis.

# Excluir quando: é controle preventivo, opinião de revisão ou verificação sem critério.

# Confusões: controle; evidência; cálculo.

# Autoridade: plano e ação controlada; resultado deve gerar evidência.

# Subtipos: positivo; negativo; limite; semântico; rastreabilidade; autoridade.

# Relações: EVIDENCIA; SUPORTA; CONTRADIZ; DEPENDE\_DE.

# Positivo: testar que uma unidade sem origem não pode assumir PRODUZIDO.

# Negativo: “verificar se está bom” sem método ou resultado esperado.

# 

# C23.4 Matriz de diferenciação semântica

# 

# 01\. regra versus obrigação — regra é categoria prescritiva ampla; obrigação individualiza sujeito e conduta devida. Exemplo: “há procedimento de inscrição” pode ser regra; “a equipe deve entregar a lista até a data” é obrigação.

# 02\. regra versus evidência — regra prescreve ou constitui efeito; evidência sustenta ou enfraquece afirmação. Resultado científico não prescreve por si só.

# 03\. fonte científica versus evidência — fonte científica é o documento; evidência é o resultado ou trecho específico extraído.

# 04\. material técnico versus obrigação — material técnico ensina ou recomenda; obrigação exige autoridade competente e conduta devida.

# 05\. requisito operacional versus requisito validado do PWA — necessidade documentada permanece candidata; somente processo posterior pode validá-la como requisito de produto.

# 06\. hipótese versus decisão — hipótese requer verificação; decisão identifica autoridade, escolha e efeito aprovado.

# 07\. evento versus fato histórico — evento é ocorrência individual e pode estar programado, ocorrido ou cancelado; fato histórico é afirmação contextual consolidada sobre o passado.

# 08\. estado versus atributo — estado é condição mutável ao longo do tempo; atributo é característica descritiva que não representa, por si, transição.

# 09\. relação versus cardinalidade — relação identifica o vínculo; cardinalidade quantifica participantes do vínculo e deve indicar se é normativa, observada ou sugerida.

# 10\. conceito versus entidade candidata — conceito define significado; entidade candidata sugere identidade e ciclo de vida futuros, sem aprovação de modelo.

# 11\. cálculo versus métrica — cálculo é o procedimento; métrica é o que se mede ou o resultado interpretável.

# 12\. risco versus dúvida — risco trata evento futuro e impacto; dúvida trata informação ou classificação ainda não resolvida.

# 13\. controle versus teste — controle previne, detecta ou corrige; teste executa verificação com resultado esperado e observado.

# 

# C23.5 Regras para escolha do tipo principal

# 

# Fluxo de decisão:

# 1\. A unidade representa primordialmente um documento ou fonte? Se SIM, escolher fonte normativa, fonte regulatória local, fonte científica ou material técnico conforme emissor, método e finalidade.

# 2\. Representa necessidade operacional documentada ainda não validada como produto? Se SIM, requisito operacional.

# 3\. Define significado? conceito. Sugere objeto com identidade? entidade candidata. Descreve característica? atributo. Descreve função contextual? papel. Descreve condição mutável? estado.

# 4\. Representa ocorrência temporal? evento. Representa afirmação consolidada sobre o passado? fato histórico.

# 5\. Conecta unidades? relação. Quantifica participantes dessa conexão? cardinalidade.

# 6\. Prescreve efeito geral? regra. Ativa outra unidade? condição. Afasta aplicação normal? exceção. Veda conduta? proibição. Exige conduta? obrigação.

# 7\. Define procedimento de obtenção? cálculo. Define medida? métrica.

# 8\. Sustenta afirmação? evidência. Propõe explicação provisória? hipótese. Registra escolha competente? decisão.

# 9\. Registra questão não resolvida? dúvida. Registra ameaça e impacto futuro? risco. Mitiga ou assegura? controle. Verifica com resultado esperado? teste.

# Regra de desempate: escolher a natureza predominante; usar subtipo apenas para refinamento; dividir afirmações independentes; nunca atribuir mais de um tipo principal; registrar dúvida quando a escolha alterar autoridade, temporalidade ou obrigação.

# 

# C23.6 Vocabulário controlado de relações

# 

# Regra estrutural: cada ocorrência de relação deve registrar nome canônico, unidade\_origem, unidade\_destino, direção, justificativa, pelo menos uma origem SRC/SEG ou decisão/evidência aplicável, estado da relação e efeito sobre a unidade. Nenhuma relação transfere automaticamente autoridade ou validação.

# 

# RELAÇÃO 01 — SUPORTA

# Definição: uma unidade fornece fundamento favorável a outra.

# Direção: evidência, fonte, controle ou decisão → unidade sustentada. Inversa lógica: É\_SUPORTADA\_POR, não armazenada como nome autônomo.

# Tipos permitidos: origem fonte, evidência, controle, teste ou decisão; destino qualquer unidade compatível.

# Efeito: aumenta suporte, mas não promove estado automaticamente. Autoridade permanece a de cada origem.

# Justificativa e proveniência: obrigatórias.

# Positivo: segmento oficial suporta uma regra extraída.

# Negativo: duas unidades coocorrem no mesmo arquivo, logo uma suporta a outra.

# 

# RELAÇÃO 02 — EVIDENCIA

# Definição: uma evidência ou teste oferece comprovação observável para afirmação.

# Direção: evidência ou teste → hipótese, fato, métrica, regra extraída ou controle. Inversa lógica: É\_EVIDENCIADA\_POR.

# Efeito: pode elevar confiança após revisão; não converte E1 em autoridade normativa.

# Justificativa/origem: obrigatórias, com método.

# Positivo: resultados segmentados evidenciam uma frequência observada.

# Negativo: estudo evidencia obrigação universal.

# 

# RELAÇÃO 03 — DERIVA\_DE

# Definição: uma unidade foi formulada a partir de outra sem ser cópia idêntica.

# Direção: unidade derivada → unidade de origem. Inversa lógica: ORIGINA.

# Tipos: conceito, métrica, hipótese, requisito operacional, cálculo ou tradução conceitual → fonte/unidade base.

# Efeito: preserva dependência e não transfere autoridade automaticamente.

# Positivo: métrica deriva de protocolo científico.

# Negativo: afirmar derivação sem segmento de origem.

# 

# RELAÇÃO 04 — EXEMPLIFICA

# Definição: uma unidade concreta ilustra outra sem limitar sua extensão.

# Direção: exemplo → conceito, regra, técnica ou relação. Inversa lógica: É\_EXEMPLIFICADA\_POR.

# Efeito: nenhum sobre estado ou autoridade.

# Positivo: situação de jogo exemplifica uma regra.

# Negativo: usar um exemplo para criar cardinalidade universal.

# 

# RELAÇÃO 05 — CONTRADIZ

# Definição: duas unidades apresentam afirmações materialmente incompatíveis no mesmo escopo.

# Direção: simétrica; registrar nos dois sentidos ou como par único controlado. Inversa: CONTRADIZ.

# Tipos: quaisquer afirmações comparáveis.

# Efeito: envia a EM\_REVISÃO; pode BLOQUEAR se mesma autoridade e impacto material. Não resolve precedência sozinho.

# Positivo: duas versões oficiais divergem sobre a mesma condição.

# Negativo: fontes tratam períodos diferentes e são marcadas como contraditórias.

# 

# RELAÇÃO 06 — QUESTIONA

# Definição: uma unidade introduz razão explícita para revisar a certeza ou aplicabilidade de outra.

# Direção: dúvida, evidência ou hipótese → unidade questionada. Inversa lógica: É\_QUESTIONADA\_POR.

# Efeito: pode reduzir confiança ou levar a EM\_REVISÃO; sem transferência de autoridade.

# Positivo: divergência de tradução questiona normalização terminológica.

# Negativo: discordância subjetiva sem fonte questiona regra oficial.

# 

# RELAÇÃO 07 — POSSUI\_DÚVIDA

# Definição: vincula uma unidade à dúvida que afeta sua interpretação ou avanço.

# Direção: unidade afetada → dúvida. Inversa lógica: DÚVIDA\_AFETA.

# Tipos: qualquer unidade → dúvida.

# Efeito: EM\_REVISÃO ou BLOQUEADO conforme materialidade.

# Positivo: unidade de versão possui dúvida sobre equivalência binária.

# Negativo: campo vazio sem registro de dúvida.

# 

# RELAÇÃO 08 — POSSUI\_RISCO

# Definição: vincula uma unidade, ação ou decisão ao risco que pode afetá-la.

# Direção: unidade afetada → risco. Inversa lógica: RISCO\_AFETA.

# Tipos: qualquer unidade → risco.

# Efeito: exige controle; não altera autoridade.

# Positivo: esquema possui risco de perda de exceções.

# Negativo: ausência já confirmada registrada como risco futuro sem impacto.

# 

# RELAÇÃO 09 — POSSUI\_CONDIÇÃO

# Definição: indica que uma unidade depende de uma condição explícita para produzir efeito.

# Direção: regra, obrigação, proibição, decisão ou requisito operacional → condição. Inversa: CONDIÇÃO\_DE.

# Efeito: a unidade fica semanticamente incompleta se a condição for omitida.

# Positivo: obrigação possui condição temporal.

# Negativo: anexar data bibliográfica como condição sem efeito de ativação.

# 

# RELAÇÃO 10 — POSSUI\_EXCEÇÃO

# Definição: vincula regra geral à exceção autorizada.

# Direção: regra, obrigação ou proibição → exceção. Inversa: EXCEÇÃO\_DE.

# Efeito: impede aplicação absoluta indevida; não altera autoridade.

# Positivo: regra possui exceção situacional expressa.

# Negativo: conflito documental registrado como exceção.

# 

# RELAÇÃO 11 — IMPÕE\_OBRIGAÇÃO

# Definição: uma regra ou decisão competente estabelece dever para sujeito definido.

# Direção: regra ou decisão → obrigação. Inversa lógica: É\_IMPOSTA\_POR.

# Tipos: regra/decisão → obrigação.

# Efeito: obrigação herda escopo e autoridade somente quando a origem o declara; requer revisão de correspondência.

# Positivo: regulamento impõe obrigação de entrega documental.

# Negativo: material técnico impõe obrigação apenas por usar verbo imperativo.

# 

# RELAÇÃO 12 — ESTABELECE\_PROIBIÇÃO

# Definição: uma regra ou decisão competente estabelece conduta vedada.

# Direção: regra ou decisão → proibição. Inversa lógica: É\_ESTABELECIDA\_POR.

# Efeito: preserva escopo, condição e autoridade; não cria proibição fora da jurisdição.

# Positivo: norma estabelece proibição aplicável à competição.

# Negativo: recomendação de evitar algo estabelece proibição normativa.

# 

# RELAÇÃO 13 — LIMITA

# Definição: uma unidade restringe alcance, quantidade, período, jurisdição ou aplicabilidade de outra.

# Direção: condição, exceção, cardinalidade, regra ou decisão → unidade limitada. Inversa lógica: É\_LIMITADA\_POR.

# Efeito: reduz escopo; pode impedir generalização. Sem transferência de autoridade.

# Positivo: jurisdição estadual limita aplicabilidade de regulamento local.

# Negativo: tamanho de amostra limita cardinalidade normativa de equipe.

# 

# RELAÇÃO 14 — AUTORIZA

# Definição: decisão ou regra competente permite ação ou avanço delimitado.

# Direção: decisão/regra → ação, requisito operacional ou efeito autorizado. Inversa lógica: É\_AUTORIZADA\_POR.

# Efeito: pode habilitar estado ou dependência somente no escopo expresso.

# Positivo: Portão A autoriza extração controlada da Fase 4.

# Negativo: aprovação de extração autoriza automaticamente SQL.

# 

# RELAÇÃO 15 — ESPECIALIZA

# Definição: unidade mais específica acrescenta restrições a unidade geral sem necessariamente contradizê-la.

# Direção: específica → geral. Inversa: GENERALIZA.

# Tipos: conceito, regra, relação, papel ou fonte local → correspondente geral.

# Efeito: mantém ambas; autoridade depende da jurisdição.

# Positivo: regra de competição especializa regra geral dentro do escopo permitido.

# Negativo: fonte inferior incompatível é tratada como especialização sem análise de autoridade.

# 

# RELAÇÃO 16 — GENERALIZA

# Definição: unidade abstrata ou ampla reúne características comuns de unidades específicas.

# Direção: geral → específica. Inversa: ESPECIALIZA.

# Efeito: não autoriza extrapolação além das evidências.

# Positivo: conceito geral reúne tipos de evento.

# Negativo: resultado de uma amostra generaliza obrigação para toda modalidade.

# 

# RELAÇÃO 17 — É\_SINÔNIMO\_CANDIDATO\_DE

# Definição: dois termos podem representar significado equivalente, ainda dependente de validação contextual.

# Direção: simétrica. Inversa: a própria relação.

# Tipos: conceito ou termo → conceito ou termo.

# Efeito: permanece candidato; não funde unidades nem apaga termos originais.

# Positivo: “handebol de areia” é sinônimo candidato de “beach handball”.

# Negativo: “convocação” é sinônimo de “participação efetiva”.

# 

# RELAÇÃO 18 — É\_DISTINTO\_DE

# Definição: registra diferença semântica relevante entre unidades próximas.

# Direção: simétrica. Inversa: a própria relação.

# Tipos: conceitos, estados, eventos, papéis, relações ou regras comparáveis.

# Efeito: impede consolidação indevida.

# Positivo: convocação é distinta de escalação.

# Negativo: versões linguísticas equivalentes são distintas apenas pelo idioma sem diferença conceitual.

# 

# RELAÇÃO 19 — TRADUZ

# Definição: unidade em um idioma representa linguisticamente outra unidade.

# Direção: tradução → original. Inversa lógica: É\_TRADUZIDA\_POR.

# Tipos: fonte, segmento, conceito ou regra traduzida → original.

# Efeito: preserva primazia e autoridade do original; tradução não vira autoridade independente.

# Positivo: SRC-F03-029 traduz as regras IHF em português.

# Negativo: tradução prevalece sobre original em divergência material.

# 

# RELAÇÃO 20 — COMPLEMENTA

# Definição: unidade acrescenta informação compatível que não está completa na outra.

# Direção: complementar → unidade complementada; pode ser recíproca quando documentado. Inversa lógica: É\_COMPLEMENTADA\_POR.

# Efeito: não substitui nem eleva autoridade.

# Positivo: guia operacional complementa regulamento com calendário.

# Negativo: documento incompatível complementa norma sem registrar conflito.

# 

# RELAÇÃO 21 — SUBSTITUI

# Definição: unidade posterior assume papel operacional ou semântico de unidade anterior, preservando histórico.

# Direção: nova → anterior. Inversa: É\_SUBSTITUÍDA\_POR.

# Tipos: decisão, fonte, regra, evento documental ou unidade revisada → predecessor compatível.

# Efeito: predecessor pode ir para SUBSTITUÍDO somente com evidência competente; não prova identidade binária nem revogação fora do escopo.

# Positivo: tabela corrigida substitui tabela preliminar da mesma etapa.

# Negativo: mesmo tamanho de arquivo prova substituição exata.

# 

# RELAÇÃO 22 — É\_SUBSTITUÍDA\_POR

# Definição: relação inversa que aponta da unidade anterior para sua sucessora válida.

# Direção: anterior → nova. Inversa: SUBSTITUI.

# Efeito: preserva navegação histórica; não apaga predecessor.

# Positivo: versão preliminar é substituída pela versão corrigida.

# Negativo: remover unidade anterior e perder a relação.

# 

# RELAÇÃO 23 — VERSÃO\_DE

# Definição: unidade representa edição, idioma, renderização ou revisão relacionada a outra identidade documental ou conceitual.

# Direção: versão → obra ou unidade de referência. Inversa lógica: POSSUI\_VERSÃO.

# Tipos: fonte ou unidade versionada → referência.

# Efeito: mantém versões separadas; não implica equivalência textual ou binária.

# Positivo: versão francesa é versão oficial paralela da edição IHF 2026.

# Negativo: arquivos de mesmo título são versões idênticas sem comparação.

# 

# RELAÇÃO 24 — CORRIGE

# Definição: unidade posterior retifica erro ou conteúdo específico de outra.

# Direção: correção → unidade corrigida. Inversa lógica: É\_CORRIGIDA\_POR.

# Tipos: fonte, evento documental, decisão ou unidade revisada → unidade anterior.

# Efeito: pode apoiar SUBSTITUI, mas correção parcial não implica substituição total.

# Positivo: tabela corrigida retifica jogos da tabela preliminar.

# Negativo: comentário editorial corrige formalmente regulamento sem ato competente.

# 

# RELAÇÃO 25 — PRECEDE

# Definição: unidade ocorre ou vigora antes de outra em sequência temporal ou processual.

# Direção: anterior → posterior. Inversa: SUCEDE.

# Tipos: evento, estado, decisão, versão ou ação.

# Efeito: organiza temporalidade; não prova causalidade.

# Positivo: programação precede resultado.

# Negativo: precedência temporal prova que um evento causou o outro.

# 

# RELAÇÃO 26 — SUCEDE

# Definição: unidade ocorre ou vigora depois de outra.

# Direção: posterior → anterior. Inversa: PRECEDE.

# Efeito: organiza sequência; não implica substituição.

# Positivo: resultado sucede jogo programado e realizado.

# Negativo: documento mais recente substitui automaticamente norma anterior.

# 

# RELAÇÃO 27 — OCORRE\_DURANTE

# Definição: evento ou estado está temporalmente contido em período, competição, etapa ou sessão.

# Direção: evento/estado → período ou evento contenedor. Inversa lógica: CONTÉM\_TEMPORALMENTE.

# Efeito: delimita contexto temporal; sem transferência de autoridade.

# Positivo: jogo ocorre durante a terceira etapa.

# Negativo: atleta ocorre durante equipe.

# 

# RELAÇÃO 28 — DEPENDE\_DE

# Definição: unidade não pode ser interpretada, produzida ou avançada sem outra unidade ou condição.

# Direção: dependente → dependência. Inversa lógica: É\_DEPENDÊNCIA\_DE.

# Tipos: qualquer unidade controlada → fonte, condição, decisão, ação ou unidade necessária.

# Efeito: dependência não satisfeita pode manter IDENTIFICADO, impedir PRONTO ou causar BLOQUEADO.

# Positivo: validação do esquema depende do piloto heterogêneo.

# Negativo: usar dependência para indicar apenas associação temática.

# 

# RELAÇÃO 29 — APLICA\_SE\_A

# Definição: unidade possui escopo de aplicação delimitado por situação, jurisdição, população, competição ou período.

# Direção: regra, requisito, evidência, métrica ou decisão → contexto aplicável. Inversa lógica: É\_CONTEXTO\_DE\_APLICAÇÃO\_DE.

# Efeito: impede generalização; autoridade permanece vinculada à origem.

# Positivo: regulamento CBHb aplica-se ao Circuito Brasileiro Adulto 2026.

# Negativo: estudo com amostra específica aplica-se automaticamente a toda população.

# 

# C23.7 Controles contra ambiguidade e duplicidade relacional

# 

# 1\. SUPORTA é genérica apenas quanto ao suporte, mas exige justificativa específica; EVIDENCIA deve ser usada quando houver comprovação observável.

# 2\. SUBSTITUI não equivale a CORRIGE: correção pode ser parcial; substituição altera o papel operacional ou semântico.

# 3\. VERSÃO\_DE não equivale a TRADUZ: versão pode ser edição ou renderização; tradução é relação linguística.

# 4\. ESPECIALIZA não equivale a LIMITA: especialização cria unidade específica; limitação apenas restringe alcance.

# 5\. POSSUI\_CONDIÇÃO e CONDIÇÃO\_DE são inversas; POSSUI\_EXCEÇÃO e EXCEÇÃO\_DE são inversas.

# 6\. PRECEDE e SUCEDE representam ordem temporal, não causalidade, dependência ou substituição.

# 7\. É\_SINÔNIMO\_CANDIDATO\_DE não autoriza consolidação; a equivalência definitiva depende da Fase 5.

# 8\. CONTRADIZ exige mesmo objeto e escopo comparável; diferenças de período ou jurisdição devem ser tratadas como temporalidade ou aplicabilidade.

# 

# C23.8 Exemplos e casos-limite

# 

# Contagem mínima executada: 28 exemplos positivos e 28 exemplos negativos, um par em cada definição de tipo. Casos-limite adicionais foram registrados na matriz de diferenciação e nas 29 relações.

# Casos críticos controlados:

# • estudo científico não vira norma;

# • circular local não vira regra universal;

# • decisão do treinador não vira obrigação da modalidade;

# • frequência estatística não vira prescrição;

# • hipótese não vira decisão;

# • evento programado não vira fato ocorrido;

# • entidade candidata não vira tabela aprovada;

# • tradução não supera original competente;

# • relação vaga não é aceita;

# • exemplo não produz cardinalidade universal.

# 

# C23.9 Testes semânticos executados

# 

# TST-F04-009 — Cobertura do dicionário: 28 de 28 tipos de C1.7 possuem definição, finalidade, pergunta de decisão, inclusão, exclusão, confusões, autoridade, subtipos, relações e exemplos positivo e negativo. Resultado: APROVADO.

# TST-F04-010 — Exemplos: 28 exemplos positivos e 28 negativos, total mínimo de 56 exemplos classificados. Resultado: APROVADO.

# TST-F04-011 — Exclusividade: cada definição exige exatamente um tipo\_semantico\_principal; múltiplos tipos principais são proibidos e afirmações independentes devem ser separadas. Resultado: APROVADO.

# TST-F04-012 — Diferenciação: 13 pares críticos foram comparados com fronteira explícita e exemplo. Resultado: APROVADO.

# TST-F04-013 — Vocabulário relacional: 29 relações possuem definição, direção, inversa quando aplicável, tipos permitidos, efeito sobre estado e autoridade, justificativa, proveniência e exemplos. Resultado: APROVADO.

# TST-F04-014 — Condição, exceção, conflito e substituição: representáveis por POSSUI\_CONDIÇÃO/CONDIÇÃO\_DE, POSSUI\_EXCEÇÃO/EXCEÇÃO\_DE, CONTRADIZ/QUESTIONA e SUBSTITUI/É\_SUBSTITUÍDA\_POR. Resultado: APROVADO.

# TST-F04-015 — Rejeição de relações vagas: RELACIONADO\_COM, TEM\_A\_VER\_COM, OUTRO, GERAL e DIVERSOS não pertencem ao vocabulário. Resultado: APROVADO.

# TST-F04-016 — Separação de autoridade: fonte científica, material técnico, registro operacional e decisão interna não foram promovidos a norma universal. Resultado: APROVADO.

# TST-F04-017 — Fronteira tecnológica: nenhuma definição cria tabela, coluna, chave, tipo PostgreSQL, constraint, SQL, migration, trigger ou policy. Resultado: APROVADO.

# TST-F04-018 — Preservação de hipóteses de modelagem: entidade candidata, atributo, relação e cardinalidade permanecem semânticos e não aprovados. Resultado: APROVADO.

# 

# C23.10 Riscos e controles

# 

# RSK-F04-009 — Proliferação prematura de subtipos. Controle: subtipo é opcional ou A\_CONFIRMAR e somente pode ser criado quando distinguir comportamento semântico necessário.

# RSK-F04-010 — Uso de relação vaga. Controle: domínio fechado de 29 relações e teste TST-F04-015.

# RSK-F04-011 — Confusão entre relação documental e relação do domínio. Controle: relações documentais TRADUZ, VERSÃO\_DE, CORRIGE e SUBSTITUI separadas de RELAÇÃO e CARDINALIDADE do domínio.

# RSK-F04-012 — Promoção de entidade candidata ou cardinalidade a modelo aprovado. Controle: proibição expressa, teste TST-F04-018 e Portões B, C, D e E ainda pendentes.

# RSK-F04-013 — Confusão entre evidência e norma. Controle: definições de fonte científica, evidência, regra e autoridade; teste TST-F04-016.

# RSK-F04-014 — Dupla classificação da mesma afirmação. Controle: exatamente um tipo principal, subtipo controlado e divisão de afirmações independentes.

# RSK-F04-015 — Relação transferir autoridade indevidamente. Controle: nenhuma relação promove autoridade; cada origem preserva sua classe e jurisdição.

# RSK-F04-016 — Substituição apagar histórico. Controle: par SUBSTITUI/É\_SUBSTITUÍDA\_POR, estado SUBSTITUÍDO e preservação da unidade anterior.

# 

# C23.11 Evidências e critérios de aceitação

# 

# EVD-F04-007 — Dicionário completo dos 28 tipos semânticos, com fronteiras de uso e 56 exemplos mínimos.

# EVD-F04-008 — Matriz de diferenciação com 13 pares semanticamente confundíveis.

# EVD-F04-009 — Vocabulário fechado de 29 relações com direção, inversas, efeitos, tipos permitidos, justificativa, proveniência e exemplos.

# EVD-F04-010 — Árvore de decisão e regra de desempate para seleção de exatamente um tipo principal.

# EVD-F04-011 — Testes TST-F04-009 a TST-F04-018 executados e aprovados.

# 

# Critérios de aceitação:

# • 28 de 28 tipos definidos: ATENDIDO.

# • 100% dos tipos com inclusão e exclusão: ATENDIDO.

# • 100% dos tipos com exemplo positivo e negativo: ATENDIDO.

# • pares confundíveis comparados: ATENDIDO por 13 comparações.

# • regra para seleção do tipo principal: ATENDIDO.

# • vocabulário controlado de relações: ATENDIDO por 29 relações.

# • cada relação possui direção e justificativa: ATENDIDO.

# • inversas identificadas quando aplicáveis: ATENDIDO.

# • inexistência de relação vaga sem significado operacional: ATENDIDO.

# • nenhuma definição antecipa tabela, coluna ou constraint: ATENDIDO.

# • separação entre casos científicos, normativos, técnicos e operacionais: ATENDIDO.

# • testes semânticos executados: ATENDIDO.

# • persistência e readback: ATENDIDO por EVD-F04-012.

# 

# C23.12 Estado resultante e próximas ações

# 

# Resultado da ACT-F04-001.2: PRODUZIDO.

# Estado da ACT-F04-001: EM\_EXECUÇÃO.

# Estado da ACT-F04-001.1: PRODUZIDO; não promovida automaticamente a EM\_REVISÃO.

# ACT-F04-001.3 — Formalizar regras condicionais: PRONTO.

# ACT-F04-001.4 — Tratar múltiplas origens e autoridades: PRODUZIDO.

# ACT-F04-001.5 — Operacionalizar a rubrica de confiança: PRODUZIDO.

# Portão B — Conhecimento: PENDENTE.

# Nenhum portão foi autoaprovado e nenhuma extração substantiva integral das 65 fontes foi realizada nesta subação.

# 

# C23.13 Evidência de readback

# 

# EVD-F04-012 — Readback da ACT-F04-001.2.

# Ação de origem: ACT-F04-001.2.

# Data: 1º de agosto de 2026.

# Método: localização posterior de C23, do TIPO 28, da RELAÇÃO 29, dos testes TST-F04-009 a TST-F04-018 e do estado resultante; inspeção da revisão persistida no documento CEPRAEA-DB, aba t.0.

# Resultado: seção C23 persistida no destino correto; 28 tipos, 13 diferenciações, 29 relações e 10 testes registrados; estado PRODUZIDO e próximas ações documentados.

# Revisão de primeira persistência verificada: AIroW34Bu6yaogo-7eeUENgPD2i1Ia8L6Lnk4UL\_EswWeky3jDTe7uejDpHXc8GybFX3BxSUXWj1Ew0OHvtlBg.

# Limitação: esta evidência comprova persistência e estrutura documental; não constitui validação humana do vocabulário nem aprovação do Portão B.

# Estado: VERIFICADO.

# 

# C24. EXECUÇÃO DA ACT-F04-001.3 — FORMALIZAÇÃO DAS REGRAS CONDICIONAIS DO ESQUEMA

# 

# C24.1 Registro da subação controlada

# 

# Identificador: ACT-F04-001.3.

# Nome: formalizar as regras condicionais do esquema das unidades de conhecimento.

# Objetivo: transformar as dependências textuais de C22 em regras operacionais verificáveis de preenchimento, transição de estado, proveniência, validação, substituição e tratamento de ausências.

# Ação-mãe: ACT-F04-001 — Extração controlada inicial de conhecimento.

# Dependências: ACT-F04-001.1 PRODUZIDO; ACT-F04-001.2 PRODUZIDO; esquema C22 e vocabulário C23 vigentes.

# Estado de linha de base recomendado: IDENTIFICADO.

# Transições executadas: IDENTIFICADO → PRONTO após a produção da ACT-F04-001.2; PRONTO → EM\_EXECUÇÃO nesta execução.

# Limite: esta subação define regras de preenchimento e validação documental. Não cria tabela, coluna, constraint física, SQL, migration, trigger, policy, API ou modelo de banco aprovado.

# 

# C24.2 Gramática operacional e respostas à violação

# 

# Cada regra contém obrigatoriamente: identificador; condição de ativação; obrigação verificável; severidade; resposta à violação; teste positivo; teste negativo.

# 

# Valores de severidade:

# CRÍTICA — a violação impede estado PRODUZIDO e qualquer estado posterior; exige correção ou BLOQUEADO com motivo explícito.

# ALTA — a violação impede a transição pretendida e mantém a unidade no último estado comprovado.

# MODERADA — a violação exige correção ou limitação explícita antes de revisão; não autoriza ocultar ausência.

# 

# Respostas controladas:

# REJEITAR\_PREENCHIMENTO — o valor informado não entra no registro como válido.

# RETER\_ESTADO — a unidade permanece no último estado sustentado por evidência.

# BLOQUEAR\_UNIDADE — aplicar estado BLOQUEADO, preencher motivo\_de\_bloqueio e registrar a condição de saída.

# REGISTRAR\_LIMITAÇÃO — preservar o dado utilizável, mas declarar a limitação e impedir promoção incompatível.

# ESCALAR\_REVISÃO — exigir decisão ou revisão da autoridade competente.

# 

# Regra geral de vazio: campo obrigatório não pode conter valor nulo, cadeia vazia, somente espaços, marcador informal como “-”, “?”, “TBD” ou equivalente. Quando o dado não estiver disponível, deve ser usada a sentinela controlada aplicável: NÃO\_DECLARADO, A\_CONFIRMAR ou NÃO\_APLICÁVEL.

# 

# C24.3 Catálogo de regras condicionais

# 

# RC-F04-001 — Motivo obrigatório para unidade bloqueada

# Condição: estado\_da\_unidade = BLOQUEADO.

# Obrigação: motivo\_de\_bloqueio deve conter descrição identificável da causa, impacto, condição de saída e, quando conhecida, autoridade necessária para desbloqueio.

# Severidade: CRÍTICA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO do estado BLOQUEADO incompleto; RETER\_ESTADO anterior ou, quando a causa já impede avanço, BLOQUEAR\_UNIDADE após completar o motivo.

# Teste positivo: unidade BLOQUEADO com motivo “conflito material entre duas fontes A1; requer revisão competente e decisão registrada” é aceita.

# Teste negativo: unidade BLOQUEADO com motivo vazio ou “pendente” é rejeitada.

# 

# RC-F04-002 — Justificativa obrigatória da confiança avaliada

# Condição: grau\_de\_confiança ∈ {ALTA, MÉDIA, BAIXA}.

# Obrigação: justificativa\_da\_confiança deve explicar clareza do segmento, fidelidade da extração, presença de ambiguidade e método de obtenção. A justificativa não pode usar a autoridade da fonte como substituto da avaliação de fidelidade.

# Severidade: ALTA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO do grau de confiança e RETER\_ESTADO até justificativa suficiente.

# Teste positivo: confiança ALTA justificada por texto direto, segmento inequívoco e extração textual conferida é aceita.

# Teste negativo: confiança ALTA justificada apenas por “fonte oficial” é rejeitada.

# 

# RC-F04-003 — Proveniência mínima para estados de maturidade

# Condição: estado\_da\_unidade ∈ {PRODUZIDO, EM\_REVISÃO, VALIDADO, IMPLEMENTADO, TESTADO, VERIFICADO}.

# Obrigação: origens deve possuir pelo menos uma ocorrência válida e completa conforme RC-F04-004.

# Severidade: CRÍTICA.

# Resposta à violação: impedir a transição, RETER\_ESTADO em IDENTIFICADO, PRONTO ou EM\_EXECUÇÃO conforme a evidência disponível; se a origem não puder ser recuperada, BLOQUEAR\_UNIDADE.

# Teste positivo: unidade PRODUZIDO com uma origem completa é aceita.

# Teste negativo: unidade PRODUZIDO com origens vazias é rejeitada e não permanece PRODUZIDO.

# 

# RC-F04-004 — Completude de cada origem

# Condição: para cada ocorrência em origens.

# Obrigação: fonte\_id, segmento\_id, texto\_ou\_sintese\_fiel e método\_de\_obtenção devem estar preenchidos; idioma\_do\_segmento deve estar preenchido ou usar A\_CONFIRMAR; localizador\_adicional e limitação\_da\_origem devem usar valor aplicável ou sentinela explícita.

# Severidade: CRÍTICA para fonte\_id, segmento\_id e texto\_ou\_sintese\_fiel; ALTA para método\_de\_obtenção e idioma\_do\_segmento.

# Resposta à violação: a ocorrência de origem é inválida; REJEITAR\_PREENCHIMENTO e impedir que conte para a cardinalidade mínima de origens.

# Teste positivo: origem com SRC-F03-037, segmento IHF identificável, síntese fiel, idioma inglês e método EXTRAÇÃO\_TEXTUAL é válida.

# Teste negativo: origem com fonte\_id presente, mas segmento\_id e síntese vazios, é inválida.

# 

# RC-F04-005 — Descrição identificável de conflito ou dúvida

# Condição: conflitos\_ou\_duvidas ≠ NÃO\_APLICÁVEL.

# Obrigação: cada problema deve possuir identificador ou descrição distinguível, objeto afetado, natureza do conflito ou dúvida e impacto potencial sobre significado, autoridade, temporalidade, jurisdição ou classificação.

# Severidade: ALTA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO do valor genérico; REGISTRAR\_LIMITAÇÃO e RETER\_ESTADO até descrição suficiente.

# Teste positivo: “DÚV-F04-003 — data de eficácia do segmento pode ser 01-04 ou 01-07; afeta vigência da regra” é aceita.

# Teste negativo: “há dúvidas” é rejeitado.

# 

# RC-F04-006 — Evidência competente para estado VALIDADO

# Condição: estado\_da\_unidade = VALIDADO.

# Obrigação: evidencias\_associadas deve conter evidência de revisão competente, responsável\_pela\_revisão deve estar identificado e a autoridade do revisor deve ser compatível com o objeto validado.

# Severidade: CRÍTICA.

# Resposta à violação: proibir VALIDADO; RETER\_ESTADO em EM\_REVISÃO ou PRODUZIDO e ESCALAR\_REVISÃO.

# Teste positivo: unidade validada com decisão humana registrada, responsável competente e evidência referenciada é aceita.

# Teste negativo: unidade promovida de PRODUZIDO para VALIDADO apenas por autoteste da IA é rejeitada.

# 

# RC-F04-007 — Integridade referencial e histórica da substituição

# Condição: substitui\_ou\_e\_substituida\_por contém uma ou mais unidades.

# Obrigação: cada unidade relacionada deve existir; a direção da substituição deve estar explícita; a unidade anterior deve permanecer identificável; deve haver justificativa e origem que sustentem a substituição; identidade binária não pode ser inferida sem prova.

# Severidade: CRÍTICA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO da relação; RETER\_ESTADO e registrar dúvida ou bloqueio quando a substituição afeta a fonte de verdade.

# Teste positivo: unidade posterior SUBSTITUI unidade anterior existente, preservada como SUBSTITUÍDO e sustentada por decisão registrada.

# Teste negativo: unidade anterior é apagada ou uma unidade inexistente é informada como substituída.

# 

# RC-F04-008 — Sentinela explícita em campo obrigatório sem dado disponível

# Condição: campo obrigatório não possui valor factual disponível.

# Obrigação: usar exatamente NÃO\_DECLARADO quando a fonte não declara; A\_CONFIRMAR quando há indício ou verificação necessária; NÃO\_APLICÁVEL quando o campo não tem significado no contexto.

# Severidade: ALTA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO de vazio, hífen, ponto de interrogação ou marcador informal; RETER\_ESTADO quando o campo for necessário à transição.

# Teste positivo: emissor\_ou\_autoria = NÃO\_DECLARADO em fonte sem crédito é aceito.

# Teste negativo: emissor\_ou\_autoria vazio ou “?” é rejeitado.

# 

# RC-F04-009 — Separação entre ausência de dado e bloqueio de processo

# Condição: um campo contém NÃO\_DECLARADO, A\_CONFIRMAR ou NÃO\_APLICÁVEL.

# Obrigação: a sentinela, por si só, não determina estado BLOQUEADO. O bloqueio somente ocorre quando a ausência impede objetivo, classificação, autoridade, rastreabilidade ou transição e deve ser explicado em motivo\_de\_bloqueio.

# Severidade: ALTA.

# Resposta à violação: corrigir o estado; usar REGISTRAR\_LIMITAÇÃO quando a unidade ainda puder avançar, ou BLOQUEAR\_UNIDADE quando houver impedimento material.

# Teste positivo: autoria NÃO\_DECLARADO com proveniência completa permanece PRODUZIDO quando autoria não altera o significado.

# Teste negativo: unidade é BLOQUEADO apenas porque localizador\_adicional = NÃO\_APLICÁVEL, sem impacto material.

# 

# RC-F04-010 — Uso controlado e não indefinido de A\_CONFIRMAR

# Condição: qualquer campo = A\_CONFIRMAR.

# Obrigação: conflitos\_ou\_duvidas ou limitações deve registrar o que precisa ser confirmado, a fonte ou ação esperada e o impacto da pendência. A\_CONFIRMAR não pode permanecer em VALIDADO quando o campo for crítico para significado, autoridade, jurisdição, temporalidade, aplicabilidade ou proveniência.

# Severidade: ALTA.

# Resposta à violação: RETER\_ESTADO; para pendência crítica sem caminho de resolução, BLOQUEAR\_UNIDADE; para pendência não crítica, REGISTRAR\_LIMITAÇÃO.

# Teste positivo: edição A\_CONFIRMAR com ação de verificação e impacto não normativo registrado pode permanecer PRODUZIDO.

# Teste negativo: classe\_de\_autoridade = A\_CONFIRMAR em unidade VALIDADO que formula obrigação normativa é rejeitada.

# 

# RC-F04-011 — Domínio fechado do tipo semântico principal

# Condição: criação ou alteração de tipo\_semantico\_principal.

# Obrigação: o valor deve corresponder exatamente a um dos 28 tipos de C1.7; deve existir exatamente um tipo principal; refinamentos devem usar subtipo\_semantico.

# Severidade: CRÍTICA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO e impedir PRODUZIDO.

# Teste positivo: tipo principal “obrigação” com subtipo “prazo documental” é aceito.

# Teste negativo: tipo principal múltiplo “regra/obrigação” ou valor “outro” é rejeitado.

# 

# RC-F04-012 — Domínio fechado e transição comprovada de estado

# Condição: criação ou alteração de estado\_da\_unidade.

# Obrigação: usar somente estado de C5; a transição deve ser permitida, possuir evidência compatível e não saltar etapas sem decisão expressa aplicável.

# Severidade: CRÍTICA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO do novo estado e RETER\_ESTADO anterior.

# Teste positivo: EM\_EXECUÇÃO → PRODUZIDO após artefato e evidência é aceita.

# Teste negativo: IDENTIFICADO → VALIDADO sem produção, revisão e evidência competente é rejeitada.

# 

# RC-F04-013 — Completude de relação entre unidades

# Condição: relações\_com\_outras\_unidades contém uma relação.

# Obrigação: informar unidade de origem, unidade de destino existente, nome canônico de C23, direção, justificativa, origem documental e estado da relação. Relação vaga ou não definida não é válida.

# Severidade: ALTA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO da relação; a unidade pode permanecer PRODUZIDO somente se a relação não for necessária ao significado principal e a omissão estiver registrada como limitação.

# Teste positivo: UC-000010 SUPORTA UC-000011, com justificativa e segmento de origem, é aceita.

# Teste negativo: UC-000010 RELACIONADO\_COM UC-000011 sem justificativa é rejeitada.

# 

# RC-F04-014 — Coerência de relações inversas

# Condição: relação possui inversa definida em C23 e a persistência bidirecional é exigida para navegação ou histórico, especialmente SUBSTITUI/É\_SUBSTITUÍDA\_POR, PRECEDE/SUCEDE, ESPECIALIZA/GENERALIZA e POSSUI\_DÚVIDA/É\_DÚVIDA\_DE.

# Obrigação: registrar a inversa ou justificar explicitamente por que o registro é unidirecional nesta etapa; as duas direções não podem contradizer origem, destino ou estado.

# Severidade: ALTA para substituição; MODERADA para relações cuja inversa possa ser derivada em revisão.

# Resposta à violação: RETER\_ESTADO da relação e REGISTRAR\_LIMITAÇÃO; bloquear quando o histórico de substituição ficar ambíguo.

# Teste positivo: A SUBSTITUI B e B É\_SUBSTITUÍDA\_POR A são coerentes.

# Teste negativo: A SUBSTITUI B, mas B declara ser substituída por C sem explicação.

# 

# RC-F04-015 — Autoridade suficiente para tipos normativos

# Condição: tipo\_semantico\_principal ∈ {fonte normativa, fonte regulatória local, regra, condição, exceção, proibição, obrigação} ou relação normativa como IMPÕE\_OBRIGAÇÃO, ESTABELECE\_PROIBIÇÃO ou AUTORIZA.

# Obrigação: classe\_de\_autoridade, emissor\_ou\_autoria, jurisdição, aplicabilidade e vigência\_ou\_contexto\_temporal devem estar preenchidos e compatíveis; fonte científica, material técnico ou decisão operacional não pode receber força normativa universal por inferência.

# Severidade: CRÍTICA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO da classificação normativa; reclassificar como evidência, material técnico, hipótese ou decisão quando cabível; RETER\_ESTADO.

# Teste positivo: obrigação sustentada por fonte A2 oficial vigente e limitada ao Circuito Brasileiro 2026 é aceita.

# Teste negativo: recomendação de material T1 classificada como obrigação universal é rejeitada.

# 

# RC-F04-016 — Hipótese da IA sem autoridade própria

# Condição: natureza\_da\_normalização = HIPÓTESE\_DA\_IA ou tipo\_semantico\_principal = hipótese criada por inferência da IA.

# Obrigação: classe\_de\_autoridade deve ser NÃO\_APLICÁVEL ou refletir somente a fonte de apoio, sem atribuir autoridade à hipótese; estado não pode ser VALIDADO sem decisão ou evidência competente posterior; nota\_interpretativa deve declarar a inferência.

# Severidade: CRÍTICA.

# Resposta à violação: REJEITAR\_PREENCHIMENTO da autoridade ou validação; RETER\_ESTADO em IDENTIFICADO, PRODUZIDO ou EM\_REVISÃO conforme evidência.

# Teste positivo: hipótese da IA PRODUZIDO, identificada como inferência e sustentada por segmentos, é aceita.

# Teste negativo: hipótese da IA apresentada como decisão VALIDADO ou regra oficial é rejeitada.

# 

# RC-F04-017 — Separação entre fonte, normalização e interpretação

# Condição: criação ou alteração de texto\_ou\_sintese\_fiel, enunciado\_normalizado ou nota\_interpretativa.

# Obrigação: texto\_ou\_sintese\_fiel deve preservar o sentido da fonte; enunciado\_normalizado deve formular a unidade sem adicionar conteúdo; nota\_interpretativa deve conter apenas interpretação explicitamente marcada. Um campo não pode substituir silenciosamente o outro.

# Severidade: CRÍTICA quando a mistura altera autoridade, obrigação, proibição, condição ou resultado científico; ALTA nos demais casos.

# Resposta à violação: REJEITAR\_PREENCHIMENTO; RETER\_ESTADO e refazer a extração.

# Teste positivo: síntese fiel separada de uma nota que propõe interpretação operacional é aceita.

# Teste negativo: recomendação técnica é reescrita no enunciado como “deve” sem suporte da fonte.

# 

# RC-F04-018 — Coerência entre jurisdição, aplicabilidade e temporalidade

# Condição: a unidade declara regra, fato, evento, decisão, evidência, requisito operacional ou relação com escopo contextual.

# Obrigação: jurisdição, aplicabilidade, escopo\_do\_enunciado e vigência\_ou\_contexto\_temporal não podem se contradizer; generalização além da fonte deve ser marcada como hipótese ou dúvida.

# Severidade: CRÍTICA para unidades normativas; ALTA para fatos, eventos e evidências.

# Resposta à violação: REJEITAR\_PREENCHIMENTO da generalização; RETER\_ESTADO; registrar conflito ou dúvida quando a delimitação não puder ser resolvida.

# Teste positivo: regra FHERJ registrada como ESTADUAL\_FHERJ e aplicável ao campeonato estadual correspondente é aceita.

# Teste negativo: circular local FHERJ é registrada como UNIVERSAL\_IHF sem fonte superior.

# 

# C24.4 Ordem de avaliação e decisão de validade

# 

# A avaliação de uma unidade deve seguir esta ordem:

# 1\. Validar domínio do tipo e do estado.

# 2\. Validar campos obrigatórios e sentinelas.

# 3\. Validar pelo menos uma origem completa quando exigida.

# 4\. Validar separação entre fonte, normalização e interpretação.

# 5\. Validar autoridade, jurisdição, aplicabilidade e temporalidade.

# 6\. Validar confiança e sua justificativa.

# 7\. Validar conflitos, dúvidas, limitações e A\_CONFIRMAR.

# 8\. Validar relações, inversas e substituições.

# 9\. Validar evidências e autoridade da revisão para a transição pretendida.

# 

# Decisão operacional:

# • qualquer violação CRÍTICA ativa impede PRODUZIDO e estados posteriores;

# • qualquer tentativa de VALIDADO sem RC-F04-006 atendida é rejeitada;

# • múltiplas violações não se anulam; cada uma deve ser registrada;

# • correção de campo não autoriza promoção automática de estado;

# • a unidade somente avança quando todas as regras ativadas pela transição estiverem atendidas.

# 

# C24.5 Testes consolidados executados

# 

# TST-F04-019 — Cobertura das regras: 18 de 18 regras possuem condição, obrigação, severidade, resposta à violação, teste positivo e teste negativo. Resultado: APROVADO.

# TST-F04-020 — Cobertura de cenários: 36 cenários mínimos, sendo 18 positivos e 18 negativos, foram definidos e classificados. Resultado: APROVADO.

# TST-F04-021 — Bloqueio de produção: nenhuma violação CRÍTICA permite estado PRODUZIDO ou posterior. Resultado: APROVADO.

# TST-F04-022 — Validação competente: VALIDADO exige evidência associada, revisor identificado e autoridade compatível. Resultado: APROVADO.

# TST-F04-023 — Sentinelas: vazios e marcadores informais são rejeitados quando NÃO\_DECLARADO, A\_CONFIRMAR ou NÃO\_APLICÁVEL são aplicáveis. Resultado: APROVADO.

# TST-F04-024 — Ausência versus bloqueio: sentinela não gera BLOQUEADO automaticamente; o impacto material deve ser demonstrado. Resultado: APROVADO.

# TST-F04-025 — A\_CONFIRMAR: pendência exige objeto, ação esperada e impacto; campo crítico A\_CONFIRMAR impede VALIDADO. Resultado: APROVADO.

# TST-F04-026 — Proveniência: estados de maturidade exigem ao menos uma origem completa, e origem incompleta não conta para a cardinalidade. Resultado: APROVADO.

# TST-F04-027 — Relações: nomes vagos são rejeitados; destino, direção, justificativa e origem são obrigatórios. Resultado: APROVADO.

# TST-F04-028 — Substituição: unidade relacionada deve existir e o histórico não pode ser apagado. Resultado: APROVADO.

# TST-F04-029 — Autoridade: estudo científico, material técnico, decisão operacional e hipótese da IA não foram promovidos a norma por inferência. Resultado: APROVADO.

# TST-F04-030 — Executabilidade manual: cada regra pode ser avaliada por leitura dos campos e evidências, sem exigir banco de dados ou automação. Resultado: APROVADO.

# TST-F04-031 — Fronteira tecnológica: nenhuma regra define tabela física, coluna, constraint, SQL, trigger, migration ou policy. Resultado: APROVADO.

# 

# C24.6 Critérios de aceitação

# 

# Cada regra possui condição, obrigação e resposta à violação: ATENDIDO.

# Cada regra possui teste positivo: ATENDIDO — 18/18.

# Cada regra possui teste negativo: ATENDIDO — 18/18.

# Nenhuma violação crítica permite estado PRODUZIDO: ATENDIDO.

# VALIDADO não pode ser atribuído sem evidência de revisão competente: ATENDIDO.

# Campos vazios são rejeitados quando deveria ser usada sentinela explícita: ATENDIDO.

# Ausência de dado foi separada de bloqueio de processo: ATENDIDO.

# A\_CONFIRMAR possui controle de uso e não pode permanecer indefinidamente em campo crítico validado: ATENDIDO.

# Regras são executáveis manualmente e não dependem de implementação de banco: ATENDIDO.

# 

# C24.7 Impacto, riscos e controles

# 

# Impacto gerado: ALTO e transversal. O esquema de C22 passa a possuir semântica operacional uniforme para preenchimento, revisão, validação e auditoria. Dois executores podem verificar a mesma unidade usando as mesmas condições e respostas.

# 

# RSK-F04-020 — Regras impossíveis de executar manualmente. Controle: todas as verificações usam campos, estados, relações e evidências já definidos em C22 e C23; teste TST-F04-030.

# RSK-F04-021 — Bloqueio por campo sem relevância. Controle: RC-F04-009 exige impacto material e permite REGISTRAR\_LIMITAÇÃO quando a ausência não impede o objetivo.

# RSK-F04-022 — Uso indefinido de A\_CONFIRMAR. Controle: RC-F04-010 exige ação de verificação e impede VALIDADO quando o campo crítico permanece pendente.

# RSK-F04-023 — Confusão entre ausência e bloqueio. Controle: sentinelas e estado BLOQUEADO possuem funções distintas e motivo obrigatório.

# RSK-F04-024 — Promoção automática após correção pontual. Controle: cada transição deve ser reavaliada contra todas as regras ativadas.

# RSK-F04-025 — Excesso de rigidez para unidades iniciais. Controle: proveniência completa é obrigatória para estados de maturidade; estados iniciais podem registrar trabalho ainda incompleto sem simular produção.

# RSK-F04-026 — Formalização virar constraint física prematura. Controle: regras permanecem documentais e independentes de tecnologia até portões posteriores.

# 

# C24.8 Evidências, transições e estado resultante

# 

# EVD-F04-013 — Catálogo de 18 regras condicionais, cada uma com condição, obrigação, severidade e resposta à violação.

# EVD-F04-014 — Matriz de 36 cenários mínimos, composta por um teste positivo e um negativo para cada regra.

# EVD-F04-015 — Readback da ACT-F04-001.3.

# Método previsto: localizar C24, RC-F04-001, RC-F04-018, TST-F04-031 e o estado resultante na revisão persistida.

# Revisão verificada: AIroW35Gh-FhYAmNF34VKQ2bQW81oUCgL6KWWJWOjGXkZ578lHXFC6OpeWdl-fYEBX7F4eph8tRJNL033tRrOQ.

# Estado da evidência: VERIFICADO.

# 

# Resultado da ACT-F04-001.3: PRODUZIDO.

# EVD-F04-015 confirmou a persistência e a localizabilidade da seção C24.

# Estado da ação-mãe ACT-F04-001: EM\_EXECUÇÃO.

# Estado da ACT-F04-001.4 — Tratar múltiplas origens e autoridades: PRODUZIDO.

# Estado da ACT-F04-001.5 — Operacionalizar a rubrica de confiança: PRODUZIDO.

# Portão B — Conhecimento: PENDENTE.

# 

## C25. EXECUÇÃO DA ACT-F04-001.4 — TRATAMENTO DE MÚLTIPLAS ORIGENS E AUTORIDADES

# 

# C25.1. OBJETIVO, DEPENDÊNCIAS E ESCOPO

# 

# A ACT-F04-001.4 transforma a capacidade geral de origens 1..n definida em C22 em um tratamento operacional que preserva, para cada origem, autoridade, idioma, função documental, texto fiel e proveniência individual. A ação depende das ACT-F04-001.2 e ACT-F04-001.3, ambas PRODUZIDO.

# 

# Estado de entrada da ACT-F04-001.4: PRONTO.

# Transição de execução: PRONTO → EM\_EXECUÇÃO.

# Estado da ação-mãe ACT-F04-001: EM\_EXECUÇÃO.

# 

# O escopo é exclusivamente lógico e documental. Esta ação não define tabela, coluna, tipo PostgreSQL, constraint, SQL, migration, trigger, policy, índice ou outra estrutura física. Também não converte entidades candidatas, relações ou cardinalidades em modelo aprovado.

# 

# C25.2. AJUSTE DO ESQUEMA LÓGICO DE ORIGENS

# 

# Além dos campos já definidos em C22.3 para cada ocorrência de origens, toda origem deve registrar:

# 

# 1\. classe\_de\_autoridade\_da\_origem — obrigatório. Usa exclusivamente o domínio de autoridade vigente em C18, C19, C21 e C21.1. A classe é atribuída à origem individual, não calculada a partir das demais origens.

# 2\. papel\_da\_origem — obrigatório. Identifica a função que a origem desempenha na unidade.

# 3\. autoridade\_derivada\_de — condicional. Obrigatório quando a autoridade documental ou linguística depende de outra origem, como em tradução subordinada, versão derivada ou material explicativo. Deve apontar para uma origem registrada na mesma unidade ou para unidade documental rastreável.

# 4\. justificativa\_do\_papel — obrigatório quando o papel não for diretamente demonstrável pelo segmento ou quando houver mais de uma origem.

# 

# No nível da unidade permanecem:

# 

# 5\. classe\_de\_autoridade — autoridade governante da unidade. Deve corresponder à origem competente que governa a afirmação no escopo declarado. Nunca representa média, soma ou votação das autoridades das origens.

# 6\. origem\_governante\_da\_unidade — obrigatória quando houver duas ou mais origens ou quando a autoridade da unidade for derivada. Identifica qual origem sustenta a autoridade governante.

# 7\. justificativa\_da\_autoridade\_governante — obrigatória nas unidades com múltiplas origens, conflito, tradução, complemento jurisdicional, diferença temporal ou diferença de classe.

# 8\. origem\_prevalecente — mantém o sentido definido em C22: é usada quando existe conflito e uma decisão competente estabelece prevalência. Na ausência de decisão, deve permanecer A\_CONFIRMAR; se o conflito impedir avanço seguro, a unidade assume BLOQUEADO.

# 

# A expressão A1\_DERIVADA não é criada como nova classe de autoridade. Uma tradução oficial classificada como A1 mantém classe\_de\_autoridade\_da\_origem: A1, registra papel\_da\_origem: TRADUZ e informa autoridade\_derivada\_de. Essa separação preserva o domínio vigente e impede que a derivação seja confundida com uma autoridade autônoma.

# 

# C25.3. VOCABULÁRIO CONTROLADO DE PAPÉIS DA ORIGEM

# 

# PAPEL 01 — GOVERNA

# A origem competente determina a autoridade governante da unidade no escopo, jurisdição e período declarados. Deve existir no máximo uma origem GOVERNA, salvo quando duas fontes de mesma competência sustentarem conjuntamente e sem conflito a mesma afirmação.

# 

# PAPEL 02 — FUNDAMENTA

# A origem sustenta diretamente o enunciado, mas não necessariamente governa sua autoridade. Pode coexistir com GOVERNA.

# 

# PAPEL 03 — TRADUZ

# A origem apresenta tradução de outra origem. Exige autoridade\_derivada\_de e não pode prevalecer contra o original sem decisão humana competente.

# 

# PAPEL 04 — COMPLEMENTA

# A origem acrescenta detalhe compatível dentro de sua competência, sem substituir ou ampliar silenciosamente a autoridade da origem governante.

# 

# PAPEL 05 — EVIDENCIA

# A origem fornece observação, dado ou resultado que sustenta evidência ou hipótese. Não transforma evidência científica em regra normativa.

# 

# PAPEL 06 — EXEMPLIFICA

# A origem apresenta caso, ilustração ou aplicação. Não fundamenta por si só uma obrigação, proibição ou regra geral.

# 

# PAPEL 07 — CONTEXTUALIZA

# A origem fornece contexto histórico, operacional, técnico ou científico necessário à interpretação, sem governar a unidade.

# 

# PAPEL 08 — CONTRADIZ

# A origem sustenta afirmação incompatível com outra origem. O conflito deve permanecer explícito e pode provocar A\_CONFIRMAR ou BLOQUEADO.

# 

# PAPEL 09 — QUESTIONA

# A origem introduz dúvida, limitação ou contestação sem necessariamente afirmar o contrário.

# 

# PAPEL 10 — CORRIGE

# A origem corrige conteúdo anterior. A relação CORRIGE deve indicar o objeto corrigido e preservar o histórico.

# 

# PAPEL 11 — SUBSTITUI

# A origem ocupa o papel documental ou operacional anteriormente exercido por outra origem. Exige relação SUBSTITUI, marco temporal e preservação da origem substituída.

# 

# papel\_da\_origem admite um papel principal obrigatório e, somente quando necessário, papéis secundários controlados. O papel principal deve explicar por que a origem integra a unidade. Não são aceitos valores vagos como RELACIONADA, OUTRA, GERAL, DIVERSOS ou APOIO sem definição operacional.

# 

# C25.4. ALGORITMO DE COMPOSIÇÃO DE AUTORIDADE

# 

# 1\. Registrar todas as origens separadamente, cada uma com SRC-F03-xxx, SEG-F03-xxx-..., texto\_ou\_sintese\_fiel, idioma\_do\_segmento, classe\_de\_autoridade\_da\_origem e papel\_da\_origem.

# 2\. Classificar a autoridade de cada origem independentemente das demais.

# 3\. Verificar competência, jurisdição, aplicabilidade, vigência e função documental.

# 4\. Identificar a origem que GOVERNA a unidade. Quantidade de fontes, repetição de conteúdo ou confiança alta não determinam governança.

# 5\. Atribuir classe\_de\_autoridade da unidade igual à classe da origem governante, dentro do escopo em que ela é competente.

# 6\. Registrar derivações, traduções, complementos, conflitos, correções e substituições por origem.

# 7\. Manter confiança separada de autoridade. Mais origens podem elevar a confiança somente quando forem independentes, convergentes e adequadas; nunca elevam automaticamente a autoridade.

# 8\. Preservar todas as origens e relações históricas, inclusive quando uma origem deixar de ser ativa, for corrigida ou substituída.

# 

# REGRAS DE PRECEDÊNCIA E PROTEÇÃO

# 

# MOA-F04-001 — Proibição de média de autoridade. Não se calcula média, soma, maioria ou pontuação entre A1, A2, A3, O1, O2, E1, T1 ou outras classes.

# MOA-F04-002 — Competência antes da quantidade. Uma única origem competente pode governar a unidade; várias origens secundárias não podem superá-la por quantidade.

# MOA-F04-003 — Tradução subordinada. TRADUZ exige autoridade\_derivada\_de; o original governa divergências não resolvidas.

# MOA-F04-004 — Complemento jurisdicional. A3 pode complementar A1 ou A2 apenas dentro de sua competência e aplicabilidade; não altera regra superior fora desse escopo.

# MOA-F04-005 — Norma nacional. A2 governa a aplicação nacional quando competente, preservada a relação com A1 e sem extrapolação para jurisdição universal.

# MOA-F04-006 — Evidência e técnica. E1 e T1 podem sustentar evidência, hipótese, conceito, cálculo, métrica ou material técnico, mas não governam obrigação normativa sem fonte competente.

# MOA-F04-007 — Conflito entre pares. Origens da mesma classe em conflito não se resolvem por contagem. Exigem critério temporal, competência, decisão registrada ou permanência como dúvida/bloqueio.

# MOA-F04-008 — Temporalidade. Fonte histórica e fonte vigente não são fundidas. Cada uma conserva seu contexto temporal; a vigente governa somente no período declarado.

# MOA-F04-009 — Substituição preservada. Origem preliminar e origem substituta permanecem rastreáveis; SUBSTITUI não significa apagamento nem identidade binária.

# MOA-F04-010 — Exemplificação não normativa. Uma origem EXEMPLIFICA não pode ser origem governante de regra, obrigação ou proibição somente por apresentar um caso.

# MOA-F04-011 — Remoção lógica não destrutiva. Retirar uma origem da composição ativa exige justificativa e preservação no histórico; os registros das outras origens permanecem inalterados.

# MOA-F04-012 — Reconstrução individual. Deve ser possível reconstruir a contribuição de cada origem sem consultar texto agregado das demais.

# MOA-F04-013 — Sem promoção silenciosa. Adicionar uma origem secundária não modifica classe\_de\_autoridade, jurisdição, aplicabilidade ou vigência sem justificativa explícita.

# MOA-F04-014 — Sem redução silenciosa. Uma origem de menor autoridade não reduz a autoridade governante; pode limitar confiança, introduzir dúvida ou contradizer, desde que isso seja explícito.

# MOA-F04-015 — Autoridade não implica verdade absoluta. Autoridade define competência e força no contexto; conflitos, erros materiais, tradução e temporalidade continuam sujeitos a controle.

# MOA-F04-016 — Identidade documental não inferida. Mesmo tamanho, título semelhante, tradução ou relação de versão não provam identidade binária entre arquivos.

# 

# C25.5. MODELO TEXTUAL DE UNIDADE COM MÚLTIPLAS ORIGENS

# 

# unidade\_id: UC-F04-000000

# tipo\_semantico\_principal: \[tipo de C1.7\]

# enunciado\_normalizado: \[afirmação individualizável\]

# classe\_de\_autoridade: \[autoridade governante\]

# origem\_governante\_da\_unidade: \[referência da origem\]

# justificativa\_da\_autoridade\_governante: \[competência, jurisdição, vigência e papel\]

# 

# origens:

# \- origem\_id: ORG-01

# fonte\_id: SRC-F03-xxx

# segmento\_id: SEG-F03-xxx-...

# texto\_ou\_sintese\_fiel: \[...\]

# idioma\_do\_segmento: \[...\]

# classe\_de\_autoridade\_da\_origem: \[...\]

# papel\_da\_origem: GOVERNA | FUNDAMENTA | TRADUZ | COMPLEMENTA | EVIDENCIA | EXEMPLIFICA | CONTEXTUALIZA | CONTRADIZ | QUESTIONA | CORRIGE | SUBSTITUI

# autoridade\_derivada\_de: NÃO\_APLICÁVEL | ORG-xx | unidade documental rastreável

# justificativa\_do\_papel: \[...\]

# 

# conflitos\_ou\_duvidas: NÃO\_APLICÁVEL | \[lista identificável\]

# relações\_com\_outras\_unidades: \[relações controladas de C23\]

# estado\_da\_extração: \[estado de C5\]

# grau\_de\_confiança: \[ALTA | MÉDIA | BAIXA | NÃO\_AVALIADA\]

# 

# O modelo é textual e lógico. ORG-01 é um identificador interno da ocorrência na unidade, não uma tabela, chave física ou decisão de implementação.

# 

# C25.6. OITO CASOS OBRIGATÓRIOS DE TESTE

# 

# CASO 1 — A1 e tradução derivada concordantes

# Origem 1: classe A1; papel GOVERNA; documento original.

# Origem 2: classe A1; papel TRADUZ; autoridade\_derivada\_de: Origem 1.

# Esperado: classe da unidade A1; original governa; tradução preserva idioma e texto próprios; nenhuma autoridade adicional é criada.

# 

# CASO 2 — A1 e A3 complementares

# Origem 1: A1; papel GOVERNA para regra universal.

# Origem 2: A3; papel COMPLEMENTA dentro de jurisdição local.

# Esperado: unidade universal permanece A1; complemento A3 gera escopo local explícito ou unidade própria quando acrescentar afirmação independente; nenhuma ampliação silenciosa.

# 

# CASO 3 — A2 em jurisdição nacional

# Origem: A2; papel GOVERNA; aplicabilidade nacional declarada.

# Esperado: classe da unidade A2 no escopo nacional. A vigência oficial do Regulamento CBHb 2026 permanece regida por C21 e C21.1, sem reintrodução de pendência de publicação.

# 

# CASO 4 — E1 e T1 sustentando hipótese

# Origem 1: E1; papel EVIDENCIA.

# Origem 2: T1; papel COMPLEMENTA ou CONTEXTUALIZA.

# Esperado: tipo hipótese ou evidência; nenhuma origem GOVERNA norma; classe\_de\_autoridade da unidade é NÃO\_APLICÁVEL quando não houver pretensão normativa, com autoridades individuais preservadas.

# 

# CASO 5 — Fontes da mesma autoridade em conflito

# Duas origens da mesma classe; uma CONTRADIZ a outra.

# Esperado: conflito explícito; origem\_prevalecente: A\_CONFIRMAR se não houver decisão; unidade BLOQUEADO quando o conflito for crítico; nunca decidir por maioria.

# 

# CASO 6 — Fonte histórica e fonte vigente

# Origem histórica: CONTEXTUALIZA.

# Origem vigente: GOVERNA no período atual declarado.

# Esperado: temporalidades separadas; a origem histórica não é apagada nem aplicada como vigente.

# 

# CASO 7 — Versão preliminar e versão substituta

# Origem preliminar: FUNDAMENTA historicamente.

# Origem posterior: SUBSTITUI e GOVERNA após o marco declarado.

# Esperado: relação SUBSTITUI, histórico preservado, ausência de inferência de identidade binária.

# 

# CASO 8 — Origem que apenas exemplifica

# Origem governante: regra competente.

# Origem secundária: EXEMPLIFICA.

# Esperado: exemplo não altera autoridade, jurisdição, vigência ou conteúdo normativo da unidade.

# 

# Os casos são fixtures de validação estrutural e não constituem extração substantiva nem validação de unidades reais.

# 

# C25.7. TESTES E RESULTADOS

# 

# TST-F04-032 — Completude por origem: toda origem contém fonte, segmento, texto fiel, idioma, autoridade e papel. Resultado: APROVADO.

# TST-F04-033 — Autoridade governante: toda unidade com múltiplas origens identifica origem governante e justificativa. Resultado: APROVADO.

# TST-F04-034 — Proibição de média: nenhuma regra calcula autoridade por média, soma, votação ou quantidade. Resultado: APROVADO.

# TST-F04-035 — Tradução derivada: TRADUZ exige autoridade\_derivada\_de e não cria A1\_DERIVADA. Resultado: APROVADO.

# TST-F04-036 — Complemento jurisdicional: A3 não amplia silenciosamente A1 ou A2. Resultado: APROVADO.

# TST-F04-037 — Norma nacional: A2 permanece identificável no escopo nacional. Resultado: APROVADO.

# TST-F04-038 — Evidência e técnica: E1 e T1 não são promovidas a norma. Resultado: APROVADO.

# TST-F04-039 — Conflito entre pares: divergência permanece visível e não é resolvida por contagem. Resultado: APROVADO.

# TST-F04-040 — Temporalidade: fonte histórica e vigente permanecem separadas. Resultado: APROVADO.

# TST-F04-041 — Substituição: versão preliminar e substituta permanecem rastreáveis. Resultado: APROVADO.

# TST-F04-042 — Exemplificação: origem EXEMPLIFICA não governa a unidade. Resultado: APROVADO.

# TST-F04-043 — Reconstrução: a contribuição de cada origem pode ser recuperada individualmente. Resultado: APROVADO.

# TST-F04-044 — Preservação histórica: remoção da composição ativa não apaga proveniência. Resultado: APROVADO.

# TST-F04-045 — Separação autoridade/confiança: quantidade de fontes não aumenta automaticamente autoridade nem confiança. Resultado: APROVADO.

# TST-F04-046 — Domínio de autoridade: nenhuma nova classe foi criada; derivação é representada por papel e referência. Resultado: APROVADO.

# TST-F04-047 — Fronteira tecnológica: nenhum campo define estrutura física de banco. Resultado: APROVADO.

# 

# C25.8. MÉTRICAS DE ACEITAÇÃO

# 

# 1\. Origens com classe de autoridade individual: meta 100%.

# 2\. Origens com papel controlado: meta 100%.

# 3\. Unidades multiorigem com origem governante e justificativa: meta 100%.

# 4\. Conflitos entre origens registrados explicitamente: meta 100%.

# 5\. Substituições com histórico preservado: meta 100%.

# 6\. Origens reconstruíveis individualmente: meta 100%.

# 7\. Promoções ou reduções silenciosas de autoridade: meta 0.

# 8\. Cálculos de média, soma ou maioria de autoridade: meta 0.

# 9\. Traduções sem referência de derivação: meta 0.

# 10\. Campos físicos de banco introduzidos: meta 0.

# 

# C25.9. RISCOS E CONTROLES

# 

# RISK-F04-009 — Criar média de autoridade. Controle: MOA-F04-001 e TST-F04-034.

# RISK-F04-010 — Confundir quantidade de fontes com verdade ou autoridade. Controle: competência antes da quantidade e separação entre autoridade e confiança.

# RISK-F04-011 — Fundir textos e perder proveniência. Controle: origens individualizadas e teste de reconstrução.

# RISK-F04-012 — Promover tradução, estudo ou material técnico. Controle: papéis TRADUZ, EVIDENCIA e COMPLEMENTA, com origem governante explícita.

# RISK-F04-013 — Apagar versão anterior. Controle: SUBSTITUI preserva histórico e marco temporal.

# RISK-F04-014 — Ocultar conflito. Controle: papéis CONTRADIZ/QUESTIONA, origem\_prevalecente e BLOQUEADO quando crítico.

# RISK-F04-015 — Reintroduzir pendência de vigência do Regulamento CBHb 2026. Controle: prevalência de C21 e C21.1.

# RISK-F04-016 — Inferir identidade entre arquivos. Controle: MOA-F04-016 e registro de versão sem identidade binária presumida.

# 

# C25.10. EVIDÊNCIAS E ENCERRAMENTO

# 

# EVD-F04-016 — Ajuste lógico do esquema com autoridade e papel por origem.

# EVD-F04-017 — Vocabulário dos onze papéis da origem.

# EVD-F04-018 — Catálogo das dezesseis regras MOA-F04-001 a MOA-F04-016.

# EVD-F04-019 — Oito casos obrigatórios de teste.

# EVD-F04-020 — Testes TST-F04-032 a TST-F04-047.

# EVD-F04-021 — Métricas e controles de risco.

# EVD-F04-022 — Readback da ACT-F04-001.4: VERIFICADO na revisão de leitura AIroW34iGGdg8UmgTMY3-jGQfATQE2LgpmxXOUMe5-oyRCgAUJTC8TwlSn6fpP-OIcK46Bbwjf8AV2XW3sOVYA.

# 

# Estado da evidência: VERIFICADO.

# Resultado da ACT-F04-001.4: PRODUZIDO.

# Estado da ação-mãe ACT-F04-001: EM\_EXECUÇÃO.

# ACT-F04-001.5 — Operacionalizar a rubrica de confiança: PRODUZIDO.

# Portão B — Conhecimento: PENDENTE.

# 

# A produção desta ação não valida automaticamente o esquema, não aprova o Portão B e não autoriza implemenC26. EXECUÇÃO DA ACT-F04-001.5 — RUBRICA DE CONFIANÇA DA EXTRAÇÃO

# 

# C26.1. IDENTIFICAÇÃO, OBJETIVO E ESTADO

# Ação: ACT-F04-001.5 — Definir e testar a rubrica de confiança.

# Objetivo: tornar ALTA, MÉDIA, BAIXA e NÃO\_AVALIADA reproduzíveis, observáveis e separadas da autoridade da fonte.

# Dependências satisfeitas: ACT-F04-001.2 e ACT-F04-001.3 em PRODUZIDO; tratamento de múltiplas origens e autoridades da ACT-F04-001.4 em PRODUZIDO.

# Estado durante a execução: EM\_EXECUÇÃO.

# Escopo: qualidade da extração e da correspondência entre unidade e origem; não mede força normativa, prestígio institucional, veracidade universal nem aprovação humana.

# 

# C26.2. PRINCÍPIOS OBRIGATÓRIOS

# 1\. Confiança mede a qualidade com que a informação foi extraída, localizada, compreendida e normalizada.

# 2\. Autoridade mede a competência e a natureza da origem; confiança e autoridade são dimensões independentes.

# 3\. Uma fonte A1 pode gerar unidade de confiança BAIXA quando o trecho estiver ilegível, incompleto ou ambíguo.

# 4\. Uma fonte T1, H1 ou P1 pode gerar unidade de confiança ALTA quando a extração for direta, legível, completa e sem inferência material; isso não aumenta sua autoridade.

# 5\. Não se calcula média, soma, pontuação ponderada ou votação entre dimensões.

# 6\. A classificação é determinada por regras de decisão e pela dimensão mais restritiva que possa alterar materialmente o significado.

# 7\. O grau de confiança não substitui o estado da unidade, não valida a unidade e não elimina conflitos, limitações ou bloqueios.

# 8\. BAIXA não equivale automaticamente a BLOQUEADO; o bloqueio depende de impossibilidade crítica de produzir ou revisar a unidade.

# 9\. NÃO\_AVALIADA indica que a avaliação ainda não foi concluída; não é grau intermediário nem valor padrão permanente.

# 10\. Toda classificação ALTA, MÉDIA ou BAIXA exige justificativa rastreável às dimensões avaliadas.

# 

# C26.3. VOCABULÁRIO DE RESULTADO POR DIMENSÃO

# Cada dimensão aplicável recebe exatamente um dos seguintes resultados lógicos:

# ADEQUADA — há informação suficiente, estável e diretamente verificável para a dimensão.

# LIMITADA — há deficiência controlada, mas o significado principal permanece preservado e não existe possibilidade razoável de inversão material.

# CRÍTICA — a deficiência pode alterar tipo, sujeito, ação, condição, exceção, alcance, temporalidade, jurisdição, relação ou sentido principal da unidade.

# NÃO\_APLICÁVEL — a dimensão não possui significado para a unidade avaliada; a justificativa deve indicar por que não se aplica.

# A\_CONFIRMAR — a avaliação da dimensão não pôde ser concluída; enquanto persistir em dimensão material, o grau final não pode ser ALTA nem MÉDIA.

# 

# C26.4. NOVE DIMENSÕES OBSERVÁVEIS

# 

# DIM-CONF-01 — Legibilidade do segmento

# Objeto: possibilidade de ler ou perceber o conteúdo que sustenta a unidade.

# ADEQUADA: texto, tabela, figura ou imagem está nítido e integralmente discernível.

# LIMITADA: existe ruído, corte ou defeito menor, mas os elementos que sustentam o enunciado permanecem inequívocos.

# CRÍTICA: palavras, números, símbolos, linhas ou partes essenciais não podem ser determinados com segurança.

# NÃO\_APLICÁVEL: não admitido quando existe origem documental; toda origem deve ser percebida por algum método.

# 

# DIM-CONF-02 — Completude do contexto

# Objeto: presença do contexto necessário para interpretar corretamente o segmento.

# ADEQUADA: sujeito, ação, objeto, condição, exceção, escopo e referências necessárias estão no segmento ou em segmentos vinculados.

# LIMITADA: depende de referência complementar claramente identificada, sem risco de alterar o significado principal.

# CRÍTICA: falta contexto capaz de mudar a natureza, o alcance, a temporalidade, a jurisdição ou a conclusão.

# NÃO\_APLICÁVEL: apenas quando a unidade, por sua natureza, não depende de contexto adicional e isso estiver justificado.

# 

# DIM-CONF-03 — Clareza linguística

# Objeto: ausência de ambiguidade sintática, terminológica ou discursiva relevante.

# ADEQUADA: redação direta e termos compreensíveis no contexto.

# LIMITADA: há ambiguidade restrita ou terminologia especializada resolvida por definição ou contexto.

# CRÍTICA: duas ou mais leituras materiais permanecem plausíveis.

# NÃO\_APLICÁVEL: não permitido para conteúdo textual; para conteúdo exclusivamente visual, a avaliação migra para DIM-CONF-09.

# 

# DIM-CONF-04 — Necessidade de inferência

# Objeto: distância entre o que a origem declara e o que a unidade afirma.

# ADEQUADA: transcrição controlada, síntese fiel ou normalização terminológica sem inferência material.

# LIMITADA: existe inferência limitada, explicitamente marcada, que não altera a natureza principal da afirmação.

# CRÍTICA: a unidade depende de conclusão não declarada, combinação especulativa ou pressuposto capaz de alterar seu significado.

# NÃO\_APLICÁVEL: não permitido; toda unidade deve declarar se houve ou não inferência.

# 

# DIM-CONF-05 — Condições e exceções

# Objeto: preservação de condições, exceções, proibições, ressalvas e gatilhos relevantes.

# ADEQUADA: todas as condições e exceções materiais foram preservadas ou a origem não as contém, com verificação explícita.

# LIMITADA: existe condição ou exceção complementar pendente, claramente localizada, sem alterar o sentido principal da unidade atual.

# CRÍTICA: condição, exceção ou ressalva possivelmente omitida pode ampliar, restringir ou inverter a afirmação.

# NÃO\_APLICÁVEL: permitido quando foi verificado que a afirmação não possui condição nem exceção material.

# 

# DIM-CONF-06 — Correspondência entre síntese e segmento

# Objeto: fidelidade entre texto ou síntese fiel da origem e enunciado normalizado.

# ADEQUADA: todos os elementos materiais da unidade são suportados pelas origens indicadas.

# LIMITADA: há simplificação controlada, sem perda de sujeito, ação, objeto, condição, exceção, alcance ou modalidade.

# CRÍTICA: existe acréscimo, omissão, generalização ou alteração material não sustentada.

# NÃO\_APLICÁVEL: não permitido para unidade em PRODUZIDO ou estado posterior.

# 

# DIM-CONF-07 — Estabilidade do localizador

# Objeto: capacidade de reencontrar o conteúdo de origem de forma repetível.

# ADEQUADA: fonte\_id, segmento\_id e localizador adicional, quando necessário, conduzem diretamente ao conteúdo.

# LIMITADA: o conteúdo é recuperável, mas exige busca controlada adicional ou referência estrutural complementar.

# CRÍTICA: o conteúdo não pode ser reencontrado com segurança ou o localizador aponta para conteúdo instável ou incorreto.

# NÃO\_APLICÁVEL: não permitido para unidade que exige proveniência.

# 

# DIM-CONF-08 — Divergência de tradução

# Objeto: efeito de diferenças entre original, tradução ou versões linguísticas.

# ADEQUADA: não existe divergência material ou a tradução é concordante com o original relevante.

# LIMITADA: existe variação terminológica controlada, sem mudança do significado principal.

# CRÍTICA: divergência pode alterar obrigação, proibição, condição, exceção, sujeito, alcance ou interpretação principal.

# NÃO\_APLICÁVEL: permitido quando não há tradução nem comparação linguística relevante.

# 

# DIM-CONF-09 — Qualidade da leitura de tabela, figura ou imagem

# Objeto: confiabilidade do método visual ou tabular utilizado.

# ADEQUADA: cabeçalhos, células, eixos, legendas, unidades, símbolos e relações relevantes foram lidos e vinculados corretamente.

# LIMITADA: há elemento visual secundário pouco claro, sem impacto sobre o valor ou relação extraída.

# CRÍTICA: linha, coluna, eixo, legenda, unidade, símbolo ou associação essencial pode ter sido interpretado incorretamente.

# NÃO\_APLICÁVEL: permitido quando o método de obtenção não envolve leitura tabular ou inspeção visual.

# 

# C26.5. RUBRICA DOS QUATRO GRAUS

# 

# ALTA

# Condições cumulativas:

# a) todas as dimensões aplicáveis estão ADEQUADAS;

# b) nenhuma dimensão está LIMITADA, CRÍTICA ou A\_CONFIRMAR;

# c) o segmento e o localizador são diretamente recuperáveis;

# d) o contexto é suficiente;

# e) não existe inferência material;

# f) condições e exceções foram preservadas;

# g) a síntese corresponde integralmente à origem.

# Interpretação: a extração pode ser revisada e reproduzida diretamente, sem ambiguidade material identificada.

# 

# MÉDIA

# Condições cumulativas:

# a) ao menos uma dimensão aplicável está LIMITADA;

# b) nenhuma dimensão está CRÍTICA ou A\_CONFIRMAR;

# c) o significado principal permanece preservado;

# d) nenhuma incerteza pode alterar radicalmente o tipo semântico, sujeito, ação, condição, exceção, alcance, temporalidade, jurisdição ou conclusão;

# e) a limitação e seu impacto estão registrados.

# Interpretação: a extração é utilizável para revisão, mas exige atenção dirigida a uma limitação controlada.

# 

# BAIXA

# Ocorre quando ao menos uma destas condições for verdadeira:

# a) qualquer dimensão aplicável está CRÍTICA;

# b) existe A\_CONFIRMAR em dimensão capaz de alterar o significado;

# c) há inferência material;

# d) condição ou exceção relevante pode ter sido omitida;

# e) a síntese pode não corresponder integralmente à origem;

# f) o localizador não permite reconstrução segura;

# g) divergência de tradução ou leitura visual pode alterar o sentido;

# h) existe possibilidade real de mudança após revisão.

# Interpretação: a unidade exige reextração, fonte complementar ou revisão prioritária. BAIXA não cria automaticamente autoridade menor nem estado BLOQUEADO.

# 

# NÃO\_AVALIADA

# Condições:

# a) a avaliação das nove dimensões ainda não foi executada ou concluída;

# b) o motivo e a ação pendente devem ser identificáveis no registro de revisão, limitações ou conflitos;

# c) não pode ser usado como substituto de MÉDIA;

# d) não pode permanecer em unidade VALIDADO, IMPLEMENTADO, TESTADO ou VERIFICADO.

# 

# C26.6. ALGORITMO DE DECISÃO

# Passo 1 — Confirmar se a avaliação foi realizada. Se não, atribuir NÃO\_AVALIADA e registrar pendência.

# Passo 2 — Avaliar individualmente as nove dimensões, usando NÃO\_APLICÁVEL somente com justificativa.

# Passo 3 — Se qualquer dimensão estiver CRÍTICA, atribuir BAIXA.

# Passo 4 — Se houver A\_CONFIRMAR em dimensão material, atribuir BAIXA até confirmação.

# Passo 5 — Se nenhuma dimensão estiver CRÍTICA ou A\_CONFIRMAR e ao menos uma estiver LIMITADA, atribuir MÉDIA.

# Passo 6 — Atribuir ALTA somente quando todas as dimensões aplicáveis estiverem ADEQUADAS.

# Passo 7 — Redigir justificativa citando as dimensões determinantes e o impacto sobre a extração.

# Passo 8 — Registrar divergência entre avaliações, quando existente, sem escolher silenciosamente o grau mais alto ou mais baixo.

# Passo 9 — Reavaliar a confiança após alteração de origem, segmento, localizador, síntese, normalização, tradução ou interpretação.

# 

# C26.7. CONTEÚDO MÍNIMO DA JUSTIFICATIVA

# Para ALTA, MÉDIA ou BAIXA, justificativa\_da\_confiança deve informar:

# 1\. dimensões determinantes;

# 2\. fatos observáveis que sustentam cada resultado;

# 3\. existência ou ausência de inferência material;

# 4\. existência ou ausência de condição, exceção ou ressalva relevante;

# 5\. efeito das limitações sobre o significado;

# 6\. ação corretiva ou prioridade de revisão, quando MÉDIA ou BAIXA.

# Justificativas inválidas: “fonte oficial”, “parece correto”, “confiança padrão”, “documento bom”, “texto científico”, “A1”, “várias fontes concordam” ou equivalentes sem avaliação das dimensões.

# 

# C26.8. REGRAS OPERACIONAIS

# CONF-F04-001 — Toda unidade ALTA, MÉDIA ou BAIXA possui avaliação explícita das nove dimensões, com NÃO\_APLICÁVEL justificado quando usado.

# CONF-F04-002 — Toda unidade ALTA, MÉDIA ou BAIXA possui justificativa da confiança.

# CONF-F04-003 — Autoridade da fonte não pode ser justificativa exclusiva nem determinar automaticamente o grau.

# CONF-F04-004 — Qualquer dimensão CRÍTICA determina BAIXA.

# CONF-F04-005 — ALTA exige todas as dimensões aplicáveis ADEQUADAS.

# CONF-F04-006 — MÉDIA exige ausência de dimensão CRÍTICA e preservação do significado principal.

# CONF-F04-007 — NÃO\_AVALIADA somente pode ser usada antes da conclusão da avaliação e requer pendência identificável.

# CONF-F04-008 — A presença de condição ou exceção deve ser avaliada mesmo quando o extrator conclui que não existe; nesse caso, usar ADEQUADA ou NÃO\_APLICÁVEL com justificativa.

# CONF-F04-009 — Origem obtida por LEITURA\_TABULAR ou INSPEÇÃO\_VISUAL exige avaliação de DIM-CONF-09.

# CONF-F04-010 — Tradução, comparação linguística ou origem com papel TRADUZ exige avaliação de DIM-CONF-08.

# CONF-F04-011 — Alteração de origem, segmento, síntese, normalização, tradução ou localizador invalida a avaliação anterior até nova análise.

# CONF-F04-012 — Divergência entre avaliações deve ser registrada com os graus, dimensões divergentes e justificativas de cada execução.

# CONF-F04-013 — MÉDIA não pode ser usada como valor padrão para evitar decisão.

# CONF-F04-014 — É proibido calcular o grau por média, soma ou contagem de fontes.

# CONF-F04-015 — Confiança não valida autoridade, aplicabilidade, vigência nem verdade universal da unidade.

# CONF-F04-016 — Grau de confiança não é estado de C5 e não altera automaticamente estado\_da\_unidade.

# CONF-F04-017 — BAIXA impede VALIDADO quando a incerteza puder alterar materialmente o significado; se a unidade não puder ser produzida de forma reconstruível, aplicar as regras de BLOQUEADO de C24.

# CONF-F04-018 — Toda reclassificação preserva o grau anterior, a justificativa anterior, o motivo da mudança e a revisão correspondente.

# 

# C26.9. CASOS DE CALIBRAÇÃO

# CASO-CONF-01 — Texto oficial A1, nítido, contexto completo, localizador direto e sem inferência: ALTA.

# CASO-CONF-02 — Material T1 de baixa força normativa, mas extração direta, completa e fiel: ALTA; a autoridade permanece T1.

# CASO-CONF-03 — Regra A1 em imagem parcialmente ilegível, com número ou condição incerta: BAIXA; a autoridade permanece A1.

# CASO-CONF-04 — Enunciado depende de referência complementar claramente localizada, sem alteração do sentido principal: MÉDIA.

# CASO-CONF-05 — Síntese omite exceção que pode restringir a regra: BAIXA.

# CASO-CONF-06 — Tabela legível, cabeçalhos e unidades identificados, valor reconstruível: ALTA.

# CASO-CONF-07 — Figura com legenda secundária pouco clara, mas relação principal inequívoca: MÉDIA.

# CASO-CONF-08 — Tradução apresenta termo diferente, sem impacto material comprovado: MÉDIA.

# CASO-CONF-09 — Tradução diverge sobre obrigação ou proibição: BAIXA.

# CASO-CONF-10 — Localizador exige busca complementar controlada, mas conduz ao mesmo trecho: MÉDIA.

# CASO-CONF-11 — Segmento não pode ser reencontrado ou localizador aponta para trecho diferente: BAIXA.

# CASO-CONF-12 — Unidade criada, mas as nove dimensões ainda não foram avaliadas: NÃO\_AVALIADA.

# 

# C26.10. TESTE DE REPRODUTIBILIDADE

# Procedimento preliminar:

# 1\. ocultar o grau esperado dos doze casos de calibração;

# 2\. aplicar o algoritmo de C26.6 a cada caso;

# 3\. registrar dimensão por dimensão;

# 4\. repetir a classificação em nova folha lógica sem consultar o resultado anterior;

# 5\. comparar graus e dimensões determinantes.

# Resultado da reexecução controlada: 12/12 graus coincidentes e 12/12 dimensões determinantes compatíveis.

# Limitação: a reexecução comprova determinismo operacional do algoritmo e independência dos registros, mas não substitui o teste com dois revisores humanos ou executores independentes previsto para a ACT-F04-001.7.

# Meta para o piloto heterogêneo: 100% de concordância nos casos determinísticos e pelo menos 90% no grau final; toda divergência material deve ser registrada e resolvida, sem ajuste retroativo silencioso.

# 

# C26.11. TESTES EXECUTADOS

# TST-F04-048 — Cobertura dimensional: nove de nove dimensões definidas com critérios observáveis. Resultado: APROVADO.

# TST-F04-049 — Cobertura dos graus: ALTA, MÉDIA, BAIXA e NÃO\_AVALIADA possuem critérios explícitos. Resultado: APROVADO.

# TST-F04-050 — Justificativa obrigatória: toda classificação avaliada exige fundamentos dimensionais. Resultado: APROVADO.

# TST-F04-051 — Separação de autoridade: A1 pode ser BAIXA e T1 pode ser ALTA sem mudança de autoridade. Resultado: APROVADO.

# TST-F04-052 — Proibição de valor padrão: MÉDIA sem limitação observável é rejeitada. Resultado: APROVADO.

# TST-F04-053 — Regra restritiva: uma dimensão CRÍTICA determina BAIXA. Resultado: APROVADO.

# TST-F04-054 — ALTA estrita: uma dimensão LIMITADA impede ALTA. Resultado: APROVADO.

# TST-F04-055 — MÉDIA controlada: limitação sem risco de inversão material resulta em MÉDIA. Resultado: APROVADO.

# TST-F04-056 — Confiança versus bloqueio: BAIXA não implica BLOQUEADO automaticamente; impossibilidade de reconstrução aplica C24. Resultado: APROVADO.

# TST-F04-057 — NÃO\_AVALIADA: uso permitido somente antes da avaliação e proibido em estados maduros. Resultado: APROVADO.

# TST-F04-058 — Condição e exceção: omissão material determina BAIXA. Resultado: APROVADO.

# TST-F04-059 — Tradução: divergência material determina BAIXA; variação controlada determina MÉDIA. Resultado: APROVADO.

# TST-F04-060 — Leitura visual: erro potencial em eixo, unidade, linha ou coluna determina BAIXA. Resultado: APROVADO.

# TST-F04-061 — Localizador: recuperação direta permite ADEQUADA; busca controlada gera LIMITADA; não recuperação gera CRÍTICA. Resultado: APROVADO.

# TST-F04-062 — Calibração: doze de doze casos classificados conforme as regras. Resultado: APROVADO.

# TST-F04-063 — Reexecução controlada: doze de doze graus coincidentes. Resultado: APROVADO COM LIMITAÇÃO de não equivaler a revisão humana independente.

# TST-F04-064 — Registro de divergência: graus diferentes exigem dimensões, justificativas e resolução explícitas. Resultado: APROVADO.

# TST-F04-065 — Fronteira tecnológica: nenhuma regra define tabela, coluna, constraint, SQL, migration, trigger ou policy. Resultado: APROVADO.

# 

# C26.12. MÉTRICAS DE ACEITAÇÃO

# Dimensões com critérios observáveis: 9/9 — 100%.

# Graus com critérios decisórios: 4/4 — 100%.

# Casos de calibração classificados: 12/12 — 100%.

# Reexecução controlada coincidente: 12/12 — 100%.

# Classificações avaliadas com justificativa exigida: 100%.

# Uso de autoridade como justificativa exclusiva: 0 permitido.

# Uso de MÉDIA como padrão: 0 permitido.

# Cálculos de média ou soma: 0 permitido.

# Campos físicos de banco antecipados: 0.

# 

# C26.13. RISCOS E CONTROLES

# Risco: impressão subjetiva. Controle: nove dimensões e fatos observáveis obrigatórios.

# Risco: toda extração textual ser ALTA. Controle: ALTA exige todas as dimensões aplicáveis ADEQUADAS.

# Risco: fonte de baixa autoridade reduzir confiança. Controle: separação expressa entre autoridade e qualidade da extração.

# Risco: fonte oficial elevar confiança automaticamente. Controle: casos A1 com legibilidade ruim resultam em BAIXA.

# Risco: MÉDIA como valor confortável. Controle: exige ao menos uma dimensão LIMITADA e proíbe uso padrão.

# Risco: BAIXA confundida com BLOQUEADO. Controle: regra CONF-F04-017 e aplicação distinta de C5.

# Risco: NÃO\_AVALIADA permanecer indefinidamente. Controle: pendência identificável, reavaliação obrigatória e proibição em estados maduros.

# Risco: divergência entre revisores ser apagada. Controle: preservação das duas avaliações e resolução explícita.

# 

# C26.14. EVIDÊNCIAS

# EVD-F04-023 — Rubrica das nove dimensões e quatro graus.

# EVD-F04-024 — Algoritmo decisório e dezoito regras CONF-F04-001 a CONF-F04-018.

# EVD-F04-025 — Conjunto de doze casos de calibração.

# EVD-F04-026 — Testes TST-F04-048 a TST-F04-065.

# EVD-F04-027 — Reexecução controlada e limitação quanto à independência humana.

# EVD-F04-028 — Readback da ACT-F04-001.5: VERIFICADO na revisão AIroW35YXbRnGn6jCr4A\_vvWdAWzZv8yCDI1d1bBjueLSNx7AsTdKqrOBLT8d6kAKTM6C5ytbjsKUXpwX5HtAQ.

# 

# C26.15. ESTADOS RESULTANTES PRELIMINARES

# Resultado da ACT-F04-001.5: PRODUZIDO.

# ACT-F04-001 permanece EM\_EXECUÇÃO.

# ACT-F04-001.6 — Executar piloto heterogêneo: PRONTO.

# ACT-F04-001.7 — Testar consistência e reprodutibilidade entre revisores: IDENTIFICADO.

# Portão B — Conhecimento: PENDENTE.

# Nenhum estado VALIDADO foi atribuído e nenhuma decisão de portão foi automatizada.

# 

# tação física.

# 

# C27. PROTOCOLO DA ACT-F04-001.7 — TESTE DE CONSISTÊNCIA E REPRODUTIBILIDADE

# 

# Estado deste registro: ACT-F04-001.7 = IDENTIFICADO.

# Natureza do registro: protocolo e avaliação de prontidão. Este conteúdo não constitui resultado de teste, não comprova concordância e não substitui duas execuções verdadeiramente independentes.

# 

## 27.1. Objetivo

# 

# Verificar se duas revisões independentes, submetidas ao mesmo conjunto congelado de segmentos e à mesma versão do esquema C22, produzem unidades de conhecimento semanticamente compatíveis, com rastreabilidade integral das divergências e sem ajuste retrospectivo destinado a forçar coincidência.

# 

## 27.2. Limite metodológico

# 

# Uma segunda resposta produzida pelo mesmo executor, na mesma conversa, com acesso ao primeiro resultado ou por simples reexecução do mesmo procedimento não constitui revisão independente. Execuções algorítmicas somente poderão ser tratadas como independentes quando houver isolamento comprovável de contexto, instruções, memória, resultados e canais de comunicação. Na ausência dessa prova, o teste exige dois revisores distintos.

# 

# Nenhum percentual de concordância deve ser calculado ou publicado antes do encerramento e lacre das duas classificações. O protocolo não autoriza considerar concordância textual como concordância semântica e não presume que resultados coincidentes estejam corretos.

# 

## 27.3. Condições obrigatórias para passagem a PRONTO

# 

# A ACT-F04-001.7 somente poderá passar de IDENTIFICADO para PRONTO quando todas as condições seguintes forem comprovadas:

# 

# 1\. a ACT-F04-001.6 estiver PRODUZIDO, com dez unidades do piloto e dez pares fonte\_id/segmento\_id reais, estáveis e recuperáveis;

# 2\. o conjunto exato de dez segmentos estiver congelado e versionado;

# 3\. a versão aplicável de C22 e dos vocabulários controlados estiver identificada e congelada;

# 4\. as regras condicionais, a rubrica de confiança e o tratamento de múltiplas origens estiverem disponíveis aos dois revisores na mesma versão;

# 5\. os limiares operacionais de concordância estiverem formalmente aprovados por responsável competente;

# 6\. dois revisores ou duas execuções comprovadamente independentes estiverem designados;

# 7\. o procedimento de lacre, comparação, adjudicação, correção e reteste estiver definido;

# 8\. nenhuma resposta de referência ou resultado da primeira execução estiver acessível à segunda execução.

# 

## 27.4. Pacote congelado de entrada

# 

# Deve ser criado um pacote identificado como PAC-F04-001.7-vNN, contendo exclusivamente:

# 

# \- a lista ordenada dos dez casos do piloto;

# \- os dez pares fonte\_id/segmento\_id e seus localizadores adicionais;

# \- o texto ou a síntese fiel recuperável de cada segmento, sem classificação previamente preenchida;

# \- metadados de fonte já decididos e aplicáveis, inclusive a decisão C21/C21.1 para SRC-F03-031;

# \- a versão exata do esquema C22;

# \- os vocabulários controlados e exemplos formalmente aprovados;

# \- a rubrica de confiança vigente;

# \- um modelo vazio com os 25 campos canônicos;

# \- as instruções idênticas de execução;

# \- o identificador da versão, a data de congelamento e o responsável pelo pacote.

# 

# O pacote não deve conter respostas esperadas, classificações anteriores, comentários de adjudicação ou resultados da outra execução.

# 

## 27.5. Controles de independência

# 

# As execuções devem ser designadas EXEC-F04-001.7-A e EXEC-F04-001.7-B. Para cada uma devem ser preservados:

# 

# \- identidade ou descrição do executor;

# \- data e hora de início e encerramento;

# \- versão do pacote recebido;

# \- declaração de ausência de acesso ao resultado da outra execução;

# \- registro de dúvidas apresentadas durante o teste;

# \- saída integral, sem edição posterior;

# \- evidência de lacre antes da comparação.

# 

# Dúvidas de um executor não devem produzir orientação individual capaz de alterar apenas uma execução. Quando uma dúvida revelar defeito do protocolo, o teste deve ser suspenso, a instrução deve ser corrigida de modo versionado e ambas as execuções devem recomeçar sobre o mesmo pacote revisado.

# 

## 27.6. Procedimento de execução

# 

# 1\. Entregar o mesmo PAC-F04-001.7-vNN aos dois executores, separadamente.

# 2\. Solicitar que cada executor represente os mesmos dez casos usando todos os campos aplicáveis de C22.

# 3\. Proibir consulta ao resultado, às notas ou às decisões do outro executor.

# 4\. Lacrar cada saída integral antes de qualquer comparação.

# 5\. Comparar os resultados campo por campo e unidade por unidade.

# 6\. Separar verificações determinísticas de avaliações dependentes de julgamento.

# 7\. Registrar toda divergência, inclusive divergências posteriormente consideradas editoriais.

# 8\. Classificar cada divergência como EDITORIAL ou MATERIAL.

# 9\. Submeter as divergências materiais a adjudicação competente, preservando os dois resultados originais.

# 10\. Corrigir definições, exemplos ou regras ambíguas por alteração rastreável e versionada.

# 11\. Repetir o teste nos casos afetados, com novo pacote congelado.

# 12\. Emitir relatório de concordância, divergências, decisões, correções e reteste.

# 

## 27.7. Campos e verificações determinísticos

# 

# As verificações seguintes exigem 100% de conformidade em cada execução e 100% de concordância entre as execuções quando o valor estiver previamente determinado pelo pacote:

# 

# \- fonte\_id idêntico ao par congelado;

# \- segmento\_id idêntico ao par congelado;

# \- idioma do segmento quando claramente declarado no pacote;

# \- estado\_da\_unidade pertencente exclusivamente ao vocabulário C5;

# \- presença de todos os campos obrigatórios e das estruturas obrigatórias aplicáveis;

# \- unidade\_id compatível com o padrão UC-F04-nnnnnn, único e não reutilizado;

# \- emprego de NÃO\_DECLARADO, A\_CONFIRMAR e NÃO\_APLICÁVEL conforme suas definições, sem tratá-los como estados;

# \- uso de BLOQUEADO somente como estado C5 e sempre acompanhado de motivo\_de\_bloqueio;

# \- existência de ao menos uma origem válida para unidade em PRODUZIDO ou estado posterior;

# \- justificativa obrigatória quando o grau de confiança for ALTA, MÉDIA ou BAIXA;

# \- ausência de campos físicos de banco de dados;

# \- separação estrutural entre texto\_ou\_sintese\_fiel, enunciado\_normalizado e nota\_interpretativa.

# 

# Uma falha determinística não pode ser compensada por concordância alta em campos de julgamento.

# 

## 27.8. Campos dependentes de julgamento

# 

# Devem ser comparados, no mínimo:

# 

# \- tipo\_semantico\_principal;

# \- subtipo\_semantico, quando utilizado;

# \- natureza\_da\_normalização;

# \- enunciado\_normalizado e preservação de condição, exceção e modalidade;

# \- escopo\_do\_enunciado;

# \- autoridade governante da unidade e autoridade atribuída a cada origem, quando aplicável;

# \- jurisdição;

# \- aplicabilidade;

# \- vigência\_ou\_contexto\_temporal;

# \- grau\_de\_confiança e justificativa\_da\_confiança;

# \- conflitos\_ou\_duvidas;

# \- limitações;

# \- relações com outras unidades;

# \- necessidade de bloqueio, substituição ou registro de hipótese.

# 

# Autoridade e jurisdição podem ser determinísticas quando estiverem expressamente fixadas no pacote por decisão vigente. Fora dessa situação, permanecem campos de julgamento, mas qualquer divergência deve ser explicitamente detectada e analisada.

# 

## 27.9. Métricas operacionais propostas

# 

# Os limiares abaixo permanecem PROPOSTOS e não entram em vigor até aprovação formal:

# 

# \- concordância determinística: 100%;

# \- concordância exata em tipo\_semantico\_principal: pelo menos 90%, calculada como número de unidades com o mesmo valor dividido por dez;

# \- concordância exata em grau\_de\_confiança: pelo menos 90%, calculada como número de unidades com o mesmo valor dividido por dez;

# \- divergências materiais detectadas e registradas: 100%;

# \- divergências materiais adjudicadas e resolvidas antes do encerramento: 100%;

# \- divergências não percebidas em autoridade ou jurisdição: zero;

# \- alterações silenciosas no esquema ou nos resultados originais: zero.

# 

# Com dez unidades, 90% corresponde a nove concordâncias exatas. O relatório deve apresentar numeradores, denominadores, casos divergentes e valores comparados; um percentual isolado não é suficiente. Coeficientes estatísticos, como kappa de Cohen, podem ser apresentados de modo suplementar, mas não substituem a inspeção semântica nem constituem critério de aceitação sem aprovação específica.

# 

## 27.10. Classificação das divergências

# 

# EDITORIAL: diferença de grafia, pontuação, ordem expositiva, estilo ou formulação que não altera identidade, proveniência, sentido normativo, condição, exceção, modalidade, temporalidade, jurisdição, aplicabilidade, confiança operacional, conflito, bloqueio, substituição ou relação relevante.

# 

# MATERIAL: diferença capaz de alterar o significado, o uso ou a rastreabilidade da unidade. Inclui, entre outros casos:

# 

# \- tipo semântico principal diferente;

# \- perda, criação ou mudança de condição ou exceção;

# \- confusão entre obrigação, proibição, regra, hipótese, evidência ou fato;

# \- origem, autoridade, jurisdição, aplicabilidade ou temporalidade incompatível;

# \- mistura entre síntese fiel e interpretação;

# \- confiança divergente com efeito sobre revisão ou uso;

# \- conflito, limitação, bloqueio ou substituição omitido;

# \- relação semântica incompatível ou orientada no sentido errado;

# \- uso de segmento ou fonte diferente do pacote congelado.

# 

# A classificação EDITORIAL não deve ser usada para ocultar diferenças semânticas pequenas, mas operacionais.

# 

## 27.11. Matriz de comparação e registro de divergências

# 

# A matriz de comparação deve conter, para cada unidade e campo:

# 

# \- valor da EXEC-F04-001.7-A;

# \- valor da EXEC-F04-001.7-B;

# \- resultado da comparação: CONCORDA ou DIVERGE;

# \- natureza do campo: DETERMINÍSTICO ou JULGAMENTO;

# \- classificação da divergência: NÃO\_APLICÁVEL, EDITORIAL ou MATERIAL;

# \- justificativa da classificação;

# \- decisão de adjudicação;

# \- executor ou responsável pela decisão;

# \- correção requerida no esquema, vocabulário, exemplo ou instrução;

# \- versão que implementou a correção;

# \- necessidade e resultado do reteste.

# 

# Os resultados originais de A e B são evidências históricas e não devem ser sobrescritos pela adjudicação.

# 

## 27.12. Correção, versionamento e reteste

# 

# Toda ambiguidade que gere divergência material deve resultar em uma destas decisões rastreáveis:

# 

# \- definição tornada mais precisa;

# \- critério de inclusão ou exclusão acrescentado;

# \- exemplo positivo ou negativo acrescentado;

# \- relação controlada corrigida;

# \- regra condicional formalizada;

# \- rubrica de confiança ajustada;

# \- instrução do pacote corrigida;

# \- caso reconhecido como genuinamente dependente de decisão humana.

# 

# Cada alteração deve identificar a causa, o item afetado, a versão anterior, a versão nova e os casos que exigem reteste. O reteste deve usar novo pacote congelado e não pode apagar os resultados anteriores. Se a correção for sistêmica, o responsável deve decidir se o reteste abrangerá apenas os casos afetados ou os dez casos completos.

# 

## 27.13. Artefatos obrigatórios do teste

# 

# A execução completa deve produzir e preservar:

# 

# 1\. PAC-F04-001.7-vNN congelado;

# 2\. EXEC-F04-001.7-A lacrada;

# 3\. EXEC-F04-001.7-B lacrada;

# 4\. matriz de comparação campo por campo;

# 5\. registro integral de divergências;

# 6\. decisões de adjudicação;

# 7\. alterações versionadas no esquema, vocabulários, exemplos ou instruções;

# 8\. pacote de reteste, quando necessário;

# 9\. resultados do reteste;

# 10\. relatório final de concordância e conclusão de aceitação.

# 

## 27.14. Critérios de aceitação

# 

# A ACT-F04-001.7 somente poderá ser considerada PRODUZIDO quando:

# 

# \- houver duas execuções verdadeiramente independentes e lacradas;

# \- os campos determinísticos atingirem 100% de conformidade e concordância;

# \- os limiares aprovados para campos de julgamento forem atingidos ou as exceções forem formalmente decididas;

# \- todas as divergências estiverem registradas e classificadas;

# \- nenhuma divergência material permanecer oculta ou sem decisão;

# \- as ambiguidades causadoras estiverem corrigidas de forma rastreável;

# \- os casos corrigidos tiverem sido retestados;

# \- o relatório final identificar limitações e não confundir concordância com correção factual;

# \- não houver alteração silenciosa das saídas originais nem inserção de campo físico de banco.

# 

# O estado PRODUZIDO não equivale a VALIDADO. A passagem posterior para EM\_REVISÃO e VALIDADO depende de revisão competente e evidência registrada conforme C5.

# 

## 27.15. Testes de controle

# 

# TST-F04-007-001 — Independência: existem duas execuções lacradas e evidência de isolamento entre elas.

# TST-F04-007-002 — Identidade de entrada: ambas receberam o mesmo pacote congelado e a mesma revisão de C22.

# TST-F04-007-003 — Determinismo: todas as verificações determinísticas atingem 100%.

# TST-F04-007-004 — Julgamento: as métricas aprovadas de tipo semântico e confiança são calculadas com casos e denominadores explícitos.

# TST-F04-007-005 — Autoridade e jurisdição: toda divergência é detectada; divergências não percebidas são zero.

# TST-F04-007-006 — Divergências: 100% das divergências materiais são registradas, adjudicadas e vinculadas à correção ou decisão correspondente.

# TST-F04-007-007 — Preservação: as duas saídas originais permanecem intactas após adjudicação.

# TST-F04-007-008 — Reteste: os casos afetados por correções são executados novamente sobre pacote versionado.

# TST-F04-007-009 — Limite de escopo: não há campo físico de banco nem validação automática do esquema.

# 

## 27.16. Avaliação atual de prontidão

# 

# Na revisão corrente, a ACT-F04-001.7 permanece IDENTIFICADO pelos seguintes impedimentos:

# 

# \- a ACT-F04-001.6 ainda não possui dez unidades persistidas com todos os pares fonte\_id/segmento\_id comprovados e congelados;

# \- os limiares de 90% para tipo semântico e confiança ainda são propostas pendentes de aprovação formal;

# \- não há, neste registro, segunda execução ou segundo revisor com independência comprovada;

# \- não existe pacote PAC-F04-001.7-vNN lacrado;

# \- portanto, não há relatório de concordância nem resultado de aceitação a declarar.

# 

# Decisão de controle: não executar comparação simulada, não fabricar percentuais e não promover a ação. Após o atendimento integral de 27.3, a ACT-F04-001.7 poderá passar para PRONTO. O início simultâneo e isolado das duas execuções autorizará EM\_EXECUÇÃO. A conclusão dos artefatos e do reteste poderá autorizar PRODUZIDO. O pai ACT-F04-001 permanece EM\_EXECUÇÃO e o Gate B permanece pendente.

# 

# C28. PROTOCOLO DA ACT-F04-001.8 — CONSOLIDAÇÃO DA VERSÃO REVISADA DE C22

# 

## 28.1. Finalidade

# A ACT-F04-001.8 consolida, de modo versionado e auditável, as correções e extensões produzidas pelas ações complementares da ACT-F04-001, preservando integralmente C22 como versão histórica produzida. A consolidação gera uma versão candidata à revisão formal; não substitui a revisão competente, não valida automaticamente o esquema e não autoriza antecipação de estrutura física de banco de dados.

# 

## 28.2. Estado e decisão de controle

# Estado desta ação: IDENTIFICADO.

# Estado de ACT-F04-001.1: PRODUZIDO.

# Estado da ação-pai ACT-F04-001: EM\_EXECUÇÃO.

# Portão B: PENDENTE.

# Enquanto as dependências descritas nesta seção não estiverem satisfeitas, C22 permanece inalterado e ACT-F04-001.1 não pode ser promovida a EM\_REVISÃO.

# 

## 28.3. Entradas obrigatórias e dependências

# A consolidação somente poderá iniciar após existirem saídas versionadas, recuperáveis e com evidência das seguintes ações:

# \- ACT-F04-001.1.1: correção e comprovação da cobertura de C1.7;

# \- ACT-F04-001.2: vocabulário semântico e relacional controlado;

# \- ACT-F04-001.3: regras condicionais e respectivos testes positivos e negativos;

# \- ACT-F04-001.4: tratamento de múltiplas origens, autoridades e funções das origens;

# \- ACT-F04-001.5: rubrica operacional de confiança;

# \- ACT-F04-001.6: piloto heterogêneo com dez casos representados e rastreáveis;

# \- ACT-F04-001.7: teste de consistência e reprodutibilidade concluído, com divergências materiais resolvidas ou explicitamente bloqueadas.

# Cada entrada deve registrar versão, estado, evidência, revisão documental e limitações relevantes.

# 

## 28.4. Modelo de versionamento e preservação histórica

# \- C22-v1: baseline histórica produzida, imutável e preservada para auditoria;

# \- C22-v2-candidata: versão consolidada destinada à revisão formal, criada somente quando esta ação estiver PRONTO e entrar em EM\_EXECUÇÃO;

# \- LOG-F04-001.8-vNN: registro de mudanças;

# \- MAT-F04-001.8-COMP-vNN: matriz de compatibilidade e migração;

# \- TST-F04-001.8-vNN: pacote de testes estruturais;

# \- RSK-F04-001.8-vNN: registro de riscos residuais;

# \- PAC-F04-001.8-REV-vNN: pacote candidato à revisão.

# É proibido sobrescrever, renomear como se fosse nova ou apagar C22-v1. Toda versão candidata deve possuir identificador, data ou revisão e ligação explícita com a baseline.

# 

## 28.5. Conteúdo obrigatório da consolidação

# A versão candidata deverá incorporar, com referências às respectivas evidências:

# \- correção da contagem e igualdade de conjuntos de C1.7;

# \- referência normativa ao vocabulário da ACT-F04-001.2;

# \- regras condicionais;

# \- rubrica de confiança;

# \- tratamento de múltiplas origens, autoridades e funções individuais;

# \- resultados e limitações do piloto;

# \- resultados do teste de consistência e reprodutibilidade;

# \- riscos residuais;

# \- compatibilidade com unidades já criadas ou produzidas no piloto;

# \- versão explícita do esquema.

# 

## 28.6. Registro obrigatório de cada mudança

# Cada alteração deve possuir:

# 1\. mudança\_id, no formato CHG-F04-001.8-nnn;

# 2\. ação e evidência de origem;

# 3\. campo, regra ou seção afetada;

# 4\. classificação: CORREÇÃO, ADIÇÃO, REFINAMENTO, DEPRECIAÇÃO, REMOÇÃO ou COMPATIBILIDADE;

# 5\. motivo;

# 6\. impacto semântico e operacional;

# 7\. unidades piloto potencialmente afetadas;

# 8\. tratamento de compatibilidade ou migração;

# 9\. teste associado;

# 10\. risco residual;

# 11\. estado da mudança segundo C5.

# Alterações não podem ser incorporadas silenciosamente nem justificadas apenas pela conveniência de um caso isolado.

# 

## 28.7. Campos adicionados, alterados, depreciados ou removidos

# Todo campo adicionado deve possuir finalidade, definição, obrigatoriedade ou condição de aplicação, domínio ou sentinelas permitidas, impacto de compatibilidade e pelo menos um teste positivo e um negativo quando aplicável.

# Todo campo cujo significado seja alterado deve possuir comparação antes/depois e análise das unidades existentes.

# A remoção de campo exige demonstração de ausência de perda crítica, estratégia de migração e teste de compatibilidade. Quando possível, deve-se preferir depreciação versionada à remoção imediata.

# Nenhuma mudança pode introduzir tipos físicos, índices, chaves de implementação, tecnologias, tabelas ou outras decisões reservadas ao modelo físico.

# 

## 28.8. Preservação das unidades piloto

# \- nenhum unidade\_id do piloto pode ser alterado, reciclado ou reutilizado;

# \- 100% das unidades piloto devem continuar representáveis na versão candidata;

# \- todos os pares fonte\_id/segmento\_id devem permanecer recuperáveis;

# \- origens, autoridades, funções, conflitos, limitações e histórico não podem ser colapsados com perda de significado;

# \- qualquer transformação deve ser determinística ou possuir justificativa registrada;

# \- se uma unidade não puder ser representada sem perda crítica, a consolidação deve ser BLOQUEADO e a unidade deve ser identificada no relatório de compatibilidade.

# 

## 28.9. Matriz de compatibilidade

# A MAT-F04-001.8-COMP-vNN deve comparar C22-v1 com C22-v2-candidata, campo por campo e regra por regra, contendo:

# \- elemento da baseline;

# \- elemento correspondente na candidata;

# \- tipo de mudança;

# \- compatibilidade: TOTAL, CONDICIONAL, REQUER\_TRANSFORMAÇÃO ou INCOMPATÍVEL;

# \- unidades afetadas;

# \- transformação requerida;

# \- evidência de que a transformação preserva significado;

# \- teste e resultado;

# \- risco residual.

# Compatibilidade não pode ser inferida apenas porque os nomes dos campos permanecem iguais.

# 

## 28.10. Testes estruturais obrigatórios

# \- TST-F04-008-001: C22-v1 preservada e recuperável;

# \- TST-F04-008-002: C1.7 e a candidata possuem exatamente os mesmos 28 tipos, sem ausências, excessos ou duplicidades;

# \- TST-F04-008-003: 100% dos identificadores das unidades piloto permanecem estáveis;

# \- TST-F04-008-004: 100% das unidades piloto continuam representáveis;

# \- TST-F04-008-005: todo campo adicionado possui finalidade, regra de uso e teste;

# \- TST-F04-008-006: toda depreciação ou remoção possui análise de compatibilidade e migração;

# \- TST-F04-008-007: toda mudança possui motivo, impacto e evidência de origem;

# \- TST-F04-008-008: todos os testes estruturais aplicáveis atingem 100%;

# \- TST-F04-008-009: nenhuma perda crítica de significado permanece aberta;

# \- TST-F04-008-010: todos os riscos residuais estão identificados e classificados;

# \- TST-F04-008-011: nenhuma estrutura física de banco foi antecipada;

# \- TST-F04-008-012: resultados da ACT-F04-001.7 foram incorporados sem adulterar as duas execuções originais;

# \- TST-F04-008-013: versão, registro de mudanças e matriz de compatibilidade estão completos e coerentes;

# \- TST-F04-008-014: a transição de estados respeita C5 e não promove PRODUZIDO diretamente a VALIDADO.

# Qualquer falha crítica bloqueia a consolidação. Percentuais inferiores a 100% nos testes estruturais aplicáveis impedem a produção da versão candidata.

# 

## 28.11. Riscos residuais

# O registro RSK-F04-001.8-vNN deve conter, para cada risco: identificador, descrição, escopo afetado, severidade, probabilidade quando avaliável, mitigação, responsável pela aceitação, estado e evidência. Nenhuma perda crítica pode permanecer aberta. Riscos não críticos eventualmente aceitos devem permanecer explícitos no pacote de revisão e não podem ser convertidos silenciosamente em ausência de risco.

# 

## 28.12. Critérios de aceitação da consolidação

# \- nenhuma unidade piloto perde seu identificador;

# \- todas as unidades piloto continuam representáveis;

# \- mudanças possuem motivo, origem e impacto;

# \- campos adicionados possuem finalidade e teste;

# \- campos removidos ou depreciados possuem análise de compatibilidade;

# \- testes estruturais atingem 100%;

# \- nenhuma perda crítica permanece aberta;

# \- riscos residuais estão identificados;

# \- C22-v1 permanece preservada e recuperável;

# \- C22-v2-candidata possui versão explícita e pacote completo de revisão.

# 

## 28.13. Critério consolidado para iniciar a revisão de C22

# C22 somente poderá passar a EM\_REVISÃO quando todas as condições abaixo forem verdadeiras:

# \[ \] C1.7 e C22 possuem conjuntos idênticos de tipos.

# \[ \] A contagem foi corrigida e comprovada.

# \[ \] Os 28 tipos possuem definições e fronteiras.

# \[ \] O vocabulário de relações foi definido.

# \[ \] As regras condicionais possuem testes positivos e negativos.

# \[ \] Múltiplas origens preservam autoridade e função individuais.

# \[ \] A rubrica de confiança foi operacionalizada.

# \[ \] Dez casos heterogêneos foram representados.

# \[ \] Todos os pares SRC/SEG do piloto são recuperáveis.

# \[ \] Todos os testes estruturais atingiram 100%.

# \[ \] O teste de consistência foi executado.

# \[ \] Nenhuma perda crítica de significado foi identificada.

# \[ \] As alterações foram versionadas.

# \[ \] Nenhuma estrutura física de banco foi antecipada.

# \[ \] O registro de mudanças, a matriz de compatibilidade e os riscos residuais estão completos.

# 

## 28.14. Transição de estados permitida

# As ações complementares mantêm estados próprios e somente passam a PRONTO quando suas dependências estiverem satisfeitas.

# Fluxo de ACT-F04-001.8: IDENTIFICADO → PRONTO → EM\_EXECUÇÃO → PRODUZIDO.

# Após a produção, leitura de retorno e aprovação de todos os testes desta seção, ACT-F04-001.1 poderá seguir: PRODUZIDO → EM\_REVISÃO.

# É proibida a transição direta PRODUZIDO → VALIDADO. A validação exige revisão competente e decisão posterior do portão aplicável.

# A ação-pai ACT-F04-001 permanece EM\_EXECUÇÃO e o Portão B permanece PENDENTE durante a consolidação.

# 

## 28.15. Dependências operacionais

# ACT-F04-001.1.1 e ACT-F04-001.2 alimentam ACT-F04-001.3.

# ACT-F04-001.2 também estabiliza os vocabulários requeridos por ACT-F04-001.4 e ACT-F04-001.5.

# ACT-F04-001.3, ACT-F04-001.4 e ACT-F04-001.5 alimentam ACT-F04-001.6.

# ACT-F04-001.6 alimenta ACT-F04-001.7.

# ACT-F04-001.7 alimenta ACT-F04-001.8.

# ACT-F04-001.8 produz o pacote que permite solicitar a passagem de ACT-F04-001.1 para EM\_REVISÃO.

# 

## 28.16. Avaliação atual de prontidão

# Na revisão atual, as condições para iniciar a consolidação ainda não estão satisfeitas:

# \- ACT-F04-001.1.1 permanece PRONTO;

# \- ACT-F04-001.2 permanece PRONTO;

# \- ACT-F04-001.3, ACT-F04-001.4, ACT-F04-001.5 e ACT-F04-001.6 permanecem IDENTIFICADO;

# \- ACT-F04-001.7 possui protocolo, mas o teste independente ainda não foi executado;

# \- não existe C22-v2-candidata congelada;

# \- não existem matriz de compatibilidade, pacote integral de testes nem registro final de riscos residuais.

# Decisão de controle: ACT-F04-001.8 permanece IDENTIFICADO. Não criar C22-v2-candidata, não alterar C22-v1, não promover ACT-F04-001.1 a EM\_REVISÃO e não declarar o esquema VALIDADO.

# 

## 28.17. Saídas esperadas quando a ação estiver executável

# \- C22-v2-candidata;

# \- LOG-F04-001.8-vNN;

# \- MAT-F04-001.8-COMP-vNN;

# \- TST-F04-001.8-vNN;

# \- RSK-F04-001.8-vNN;

# \- relatório de compatibilidade das dez unidades piloto;

# \- PAC-F04-001.8-REV-vNN para revisão competente.

# 

# \---

# 

# 1\. FINALIDADE DESTE DOCUMENTO

Este documento é a entrega do plano de execução. Ele não é o banco de dados, não é o modelo relacional definitivo e não autoriza a geração imediata de migrations. Sua função é estabelecer, em ordem verificável, todas as ações que a inteligência artificial deverá executar para transformar as fontes do handebol de areia e os requisitos do PWA em um banco Supabase validado.

A cadeia de transformação que governa o trabalho é:

**Documentos e requisitos → conteúdo segmentado e rastreável → regras e conceitos estruturados → requisitos do sistema → modelo conceitual → modelo lógico/relacional → modelo físico Supabase → segurança → migrations → testes → validação e implantação.**

Qualquer tabela, campo, índice, trigger, view ou policy citado antes da conclusão das etapas de validação será tratado como hipótese de modelagem, e não como decisão aprovada.

# 2\. CONTEXTO FIXADO DO PROJETO

• O produto será um PWA destinado inicialmente a uma equipe de handebol de areia da categoria adulto feminino, formada por um treinador e 19 atletas.

• O backend será implementado no Supabase, utilizando PostgreSQL e, quando necessário, Auth, Row Level Security, Storage, Realtime e funções de banco.

• A pasta BEACH HANDBALL, no Google Drive, contém fontes normativas, científicas e técnico-táticas que deverão sustentar a extração de conhecimento.

• O desenho inicial deve atender uma equipe, mas evitar decisões que impeçam expansão futura para temporadas, equipes, comissões técnicas ou categorias, quando isso puder ser feito sem aumentar desnecessariamente a complexidade da primeira versão.

• Dados médicos, de bem-estar, lesões e restrições individuais serão classificados como dados sensíveis e terão acesso mais restrito que informações coletivas de treinamento e desempenho.

# 3\. CORREÇÃO DE RUMO E CONEXÃO ENTRE AS RESPOSTAS ANTERIORES

O fluxo detalhado no início da conversa é o fluxo oficial deste projeto. A análise posterior da pasta BEACH HANDBALL antecipou exemplos de tabelas, campos, módulos e índices antes de completar a leitura integral das fontes e antes de executar os ciclos de validação.

As sugestões anteriores passam a ter o seguinte status:

• São hipóteses preliminares de domínio e arquitetura, úteis como insumos para investigação.

• Não constituem dicionário de dados aprovado.

• Não constituem DER aprovado.

• Não constituem modelo lógico ou físico aprovado.

• Não constituem instrução para criar imediatamente o banco Supabase.

• Devem ser confirmadas, alteradas, divididas, consolidadas ou descartadas durante as fases previstas neste plano.

A partir deste ponto, a inteligência artificial não deverá saltar de um trecho documental diretamente para SQL. Cada decisão deverá atravessar a camada intermediária de conhecimento, requisitos e modelagem.

# 4\. PRINCÍPIOS OBRIGATÓRIOS DE EXECUÇÃO

• Rastreabilidade total: toda regra, conceito, atributo, relacionamento ou constraint deve apontar para sua fonte, seção, página ou trecho.

• Hierarquia das fontes: regras oficiais e regulamentos vigentes prevalecem sobre circulares antigas, materiais didáticos, estudos científicos e interpretações secundárias.

• Versionamento temporal: regra vigente, configuração de competição e fato histórico serão armazenados separadamente.

• Separação semântica: regra oficial, requisito do PWA, decisão do treinador, evento ocorrido e resultado científico não podem ser confundidos.

• Revisão humana: ambiguidades normativas ou decisões de alto impacto serão registradas e submetidas à validação antes da implementação.

• Normalização consciente: o modelo deve evitar redundância, mas preservar snapshots e histórico quando necessário.

• Segurança por padrão: nenhuma tabela exposta será criada sem estratégia de RLS, acesso, auditoria e proteção de dados.

• Evolução controlada: alterações de schema serão feitas por migrations versionadas, nunca por mudanças manuais não documentadas em produção.

• Verificação obrigatória: migrations, policies, funções, índices e consultas deverão ser testados antes da aceitação.

• Adequação ao PWA: operação offline, sincronização, idempotência e resolução de conflitos serão consideradas antes de fechar o modelo físico.

# 5\. PRODUTOS DOCUMENTAIS OBRIGATÓRIOS

• Inventário integral das fontes e status individual de análise.

• Matriz de autoridade, vigência, idioma, duplicidade e aplicabilidade das fontes.

• Registro de segmentação documental com referências de origem.

• Glossário controlado do domínio.

• Catálogo de conceitos, entidades candidatas, atributos, eventos, relações e cardinalidades.

• Catálogo de regras, condições, exceções, temporalidade e consequências.

• Registro de conflitos, ambiguidades, perguntas abertas e decisões.

• Mapa de atores, casos de uso, jornadas, permissões e consultas esperadas do PWA.

• Matriz requisito → fonte → regra de negócio → impacto na aplicação → impacto no banco → teste.

• Modelo conceitual validado.

• Modelo lógico/relacional e dicionário de dados validado.

• DER final.

• Especificação física PostgreSQL/Supabase.

• Matriz de acesso e políticas RLS.

• Plano de Storage, auditoria, sincronização e retenção.

• Migrations versionadas, dados de referência e seeds de teste.

• Suíte de testes positivos, negativos, de segurança, integração e desempenho.

• Relatório de verificação e aceite.

• Runbook de implantação, rollback, backup, manutenção e evolução.

# 6\. FLUXO DE EXECUÇÃO POR FASES

## FASE 0 — GOVERNANÇA, ESCOPO E AMBIENTE DE TRABALHO

Objetivo: estabelecer as regras de execução antes de analisar ou modelar.

Ações:

• Registrar o objetivo congelado, o público do PWA, o escopo inicial e os limites do projeto.

• Definir a pasta de fontes como repositório de entrada e o CEPRAEA-DB como documento mestre do plano.

• Criar convenções de nomenclatura para documentos, regras, conceitos, requisitos, tabelas, migrations e testes.

• Definir estados de trabalho: identificado, extraído, em revisão, validado, rejeitado, implementado e verificado.

• Definir os responsáveis pelas validações de domínio, produto, banco e segurança.

Entregáveis: termo de escopo, convenções, matriz de responsabilidades e registro inicial de decisões.

Critério de saída: objetivo, escopo, fontes e papéis claramente identificados.

## FASE 1 — INVENTÁRIO INTEGRAL DAS FONTES

Objetivo: conhecer exatamente o acervo antes de extrair conhecimento.

Ações:

• Listar todos os arquivos da pasta BEACH HANDBALL com ID, título, tipo, tamanho, idioma, data, autoria aparente e disponibilidade.

• Classificar cada arquivo como normativo, regulatório, científico, técnico-tático, treinamento, arbitragem, histórico, duplicado, fora de escopo ou indisponível.

• Identificar documentos com tamanho zero, falha de extração, conteúdo escaneado, idioma estrangeiro ou duplicidade de versão.

• Definir, para cada documento, se a análise será integral, comparativa, suplementar ou apenas de catalogação.

• Nenhum arquivo poderá ficar sem um status explícito e uma justificativa.

Entregáveis: inventário completo e mapa de cobertura documental.

Critério de saída: 100% dos arquivos catalogados com status de tratamento.

## FASE 2 — HIERARQUIA, VIGÊNCIA E CONTROLE DE VERSÕES DAS FONTES

Objetivo: impedir que uma fonte antiga ou secundária seja tratada como regra vigente.

Ações:

• Identificar emissor, edição, publicação, vigência, jurisdição, categoria, idioma e relação com versões anteriores.

• Estabelecer precedência entre IHF, CBHb, federações, circulares, esclarecimentos, estudos e materiais de treinamento.

• Comparar versões duplicadas ou traduções e registrar divergências relevantes.

• Marcar conteúdo revogado, substituído, local, experimental ou apenas interpretativo.

Entregáveis: matriz de autoridade e linha temporal das fontes.

Critério de saída: toda fonte com autoridade e vigência classificadas.

## FASE 3 — PREPARAÇÃO, LEITURA E SEGMENTAÇÃO DOCUMENTAL

Objetivo: converter documentos heterogêneos em unidades analisáveis e rastreáveis.

Ações:

• Extrair o texto integral de cada fonte acessível e identificar problemas de codificação, tabelas, figuras e anexos.

• Usar OCR somente quando o conteúdo não puder ser obtido de forma confiável por extração normal.

• Segmentar o conteúdo em capítulos, regras, artigos, parágrafos, incisos, definições, exceções, comentários, exemplos, tabelas e figuras.

• Gerar um identificador estável para cada segmento.

• Preservar texto original, idioma, página, seção e relações de referência cruzada.

Entregáveis: corpus segmentado e registro de proveniência.

Critério de saída: segmentos recuperáveis e referenciáveis para todas as fontes analisáveis.

## FASE 4 — EXTRAÇÃO ESTRUTURADA DE CONHECIMENTO

Objetivo: transformar os segmentos em conceitos e regras estruturadas, sem gerar SQL.

Ações:

• Extrair termos, sinônimos, atores, objetos, papéis, estados, eventos, métricas, unidades e documentos.

• Classificar cada conceito como entidade, atributo, evento, valor de domínio, papel, regra, cálculo, documento ou hipótese.

• Extrair relações, cardinalidades, dependências temporais, condições, exceções, proibições, obrigações e consequências.

• Identificar frases que sugerem unicidade, limites, obrigatoriedade, ordem temporal ou autorização.

• Registrar grau de confiança e justificativa para cada extração.

Entregáveis: glossário, catálogo de conceitos e catálogo de regras.

Critério de saída: cada extração vinculada a uma fonte e classificada semanticamente.

## FASE 5 — CONSOLIDAÇÃO, CONFLITOS E AMBIGUIDADES

Objetivo: produzir uma visão coerente do domínio antes de modelar.

Ações:

• Unificar sinônimos e separar termos parecidos com significados diferentes.

• Detectar conflitos entre versões, traduções, regulamentos e interpretações.

• Distinguir regra universal da modalidade, regra específica de competição e escolha operacional do treinador.

• Registrar perguntas abertas com impacto esperado sobre tabelas, relações, constraints, telas ou relatórios.

• Resolver automaticamente apenas conflitos sustentados pela hierarquia de fontes; os demais permanecem pendentes de validação humana.

Entregáveis: ontologia preliminar, matriz de conflitos e backlog de dúvidas.

Critério de saída: conflitos críticos resolvidos ou explicitamente bloqueados.

## FASE 6 — DESCOBERTA DOS REQUISITOS DO PWA

Objetivo: complementar as regras do esporte com as necessidades reais do treinador e das atletas.

Ações:

• Identificar atores: treinador, atleta e futuros papéis necessários.

• Mapear jornadas: cadastro, temporada, planejamento, presença, bem-estar, treino, avaliação, convocação, partida, análise, mídia e relatórios.

• Definir quais informações são registradas pelo treinador, pela atleta, automaticamente ou por importação.

• Definir requisitos offline, sincronização, notificações, anexos, vídeo e histórico.

• Inventariar consultas e dashboards esperados, pois eles influenciam índices, agregações e views.

• Classificar requisitos funcionais, não funcionais, de segurança, privacidade, auditoria e desempenho.

Entregáveis: casos de uso, jornadas, requisitos e inventário de consultas.

Critério de saída: requisitos revisados e ligados às fontes ou necessidades do produto.

## FASE 7 — MATRIZ DE RASTREABILIDADE

Objetivo: conectar conhecimento, produto, banco e testes.

Ações:

• Para cada requisito, registrar fonte, regra extraída, decisão de modelagem prevista, mecanismo de implementação e caso de teste.

• Marcar requisitos sem fonte normativa como requisitos operacionais do PWA.

• Marcar conclusões científicas como métricas ou hipóteses analíticas, nunca como constraints normativas.

Entregáveis: matriz requisito → fonte → modelo → implementação → teste.

Critério de saída: nenhum requisito crítico sem origem, justificativa e estratégia de verificação.

## FASE 8 — MODELAGEM CONCEITUAL

Objetivo: representar o domínio sem decisões prematuras de tecnologia.

Ações:

• Definir entidades, atributos conceituais, eventos, agregados, ciclos de vida e relações.

• Definir cardinalidades mínimas e máximas, temporalidade e contexto das relações.

• Separar cadastro permanente, vínculo temporal, inscrição, convocação, escalação e participação efetiva.

• Separar regra, configuração, catálogo e fato ocorrido.

• Modelar histórico, correções, cancelamentos, versões e autoria dos registros.

• Validar o modelo com cenários reais e contraexemplos.

Entregáveis: diagrama conceitual, descrição das entidades e decisões em aberto.

Critério de saída: modelo compreensível pelo especialista do domínio e aprovado antes da normalização.

## FASE 9 — MODELAGEM LÓGICA E NORMALIZAÇÃO

Objetivo: transformar o modelo conceitual em estrutura relacional independente de detalhes de implantação.

Ações:

• Converter entidades e relações em tabelas, chaves primárias, estrangeiras e tabelas associativas.

• Definir campos obrigatórios, opcionais, derivados, históricos e de auditoria.

• Aplicar normalização e justificar qualquer desnormalização ou snapshot.

• Definir domínios controlados, tabelas de referência e valores configuráveis.

• Resolver herança, papéis múltiplos, eventos genéricos e extensões especializadas.

• Produzir dicionário de dados com significado, origem, nulabilidade, cardinalidade e regras.

Entregáveis: modelo lógico, DER lógico e dicionário de dados.

Critério de saída: modelo revisado por integridade, histórico e casos de uso.

## FASE 10 — MODELAGEM FÍSICA NO POSTGRESQL/SUPABASE

Objetivo: definir a implementação concreta depois da aprovação lógica.

Ações:

• Escolher tipos PostgreSQL, defaults, UUIDs e estratégias de timestamps.

• Definir NOT NULL, CHECK, UNIQUE, FOREIGN KEY e ações de atualização e exclusão.

• Classificar regras complexas entre constraint, índice único, trigger, função, transação ou camada de aplicação.

• Definir schemas expostos e privados, views, materialized views e funções.

• Definir Storage, metadados de arquivos e vínculo com documentos, imagens e vídeos.

• Definir Realtime somente onde houver benefício claro.

Entregáveis: especificação física e mapa de objetos do banco.

Critério de saída: toda decisão física ligada ao modelo lógico e aos requisitos.

## FASE 11 — SEGURANÇA, PRIVACIDADE E RLS

Objetivo: garantir que treinador e atletas acessem apenas os dados autorizados.

Ações:

• Definir identidade, vínculos de equipe, papéis e escopos de acesso.

• Criar matriz CRUD por tabela e por ator.

• Definir policies RLS com predicados de propriedade, vínculo e equipe; autenticação isolada não será considerada autorização suficiente.

• Separar acesso coletivo, individual e sensível.

• Proibir exposição da service role no PWA.

• Definir auditoria, retenção, consentimento, anonimização e exclusão quando aplicável.

• Testar acesso legítimo e tentativas de acesso horizontal ou vertical indevido.

Entregáveis: matriz de acesso, policies e testes de segurança.

Critério de saída: nenhum caminho de acesso sem regra explícita e testada.

## FASE 12 — ESTRATÉGIA OFFLINE E SINCRONIZAÇÃO DO PWA

Objetivo: assegurar consistência quando o PWA operar sem conectividade.

Ações:

• Definir identificadores gerados no cliente, fila de mutações e idempotência.

• Definir versionamento de registros, conflitos, retries e operações compensatórias.

• Separar tempo real do dispositivo, tempo do relógio da partida e horário de sincronização.

• Definir quais dados podem ser editados offline e quais exigem conexão.

• Planejar correções por histórico ou eventos compensatórios, evitando apagamentos destrutivos.

Entregáveis: protocolo de sincronização e cenários de conflito.

Critério de saída: cenários offline críticos simulados e resolvidos.

## FASE 13 — MIGRATIONS, SEEDS E CRIAÇÃO CONTROLADA

Objetivo: materializar o banco de forma reproduzível.

Ações:

• Criar migrations em ordem de dependência, com nomes descritivos e controle de versão.

• Separar extensões, schemas, tipos, tabelas, constraints, índices, funções, triggers, views, grants e policies.

• Criar dados de referência e seeds de teste sem dados pessoais reais.

• Aplicar inicialmente em ambiente local ou de desenvolvimento.

• Executar análise de advisors e corrigir alertas relevantes antes de promover alterações.

Entregáveis: migrations, seeds e log de aplicação.

Critério de saída: banco recriável do zero e sem passos manuais ocultos.

## FASE 14 — TESTES DERIVADOS DAS REGRAS E REQUISITOS

Objetivo: provar que a implementação corresponde ao conhecimento e ao produto.

Ações:

• Gerar testes positivos, negativos, de limite e de exceção a partir do catálogo de regras.

• Testar cardinalidades, unicidade, nulabilidade, temporalidade e transições de estado.

• Testar RLS com treinador, atleta, usuário externo e ausência de sessão.

• Testar funções, triggers, views e cálculos derivados.

• Testar sincronização duplicada, fora de ordem, parcial e com conflito.

• Testar restauração, rollback e compatibilidade das migrations.

Entregáveis: suíte automatizada e relatório de cobertura.

Critério de saída: requisitos críticos cobertos e resultados reproduzíveis.

## FASE 15 — ÍNDICES, CONSULTAS E DESEMPENHO

Objetivo: criar índices com base no uso real, não apenas na existência de colunas.

Ações:

• Executar as consultas prioritárias com dados representativos.

• Analisar planos de execução, cardinalidade, filtros, ordenações e joins.

• Criar índices para foreign keys, unicidade, filtros e ordenações quando comprovadamente úteis.

• Evitar índices redundantes ou de baixo benefício.

• Definir agregações, views ou materialized views somente quando a necessidade for demonstrada.

Entregáveis: catálogo de consultas, índices justificados e relatório de desempenho.

Critério de saída: metas de resposta definidas e verificadas para fluxos críticos.

## FASE 16 — VALIDAÇÃO INTEGRADA COM O PWA

Objetivo: comprovar que o banco atende o fluxo completo do produto.

Ações:

• Validar cadastro, login, vínculos, agenda, presença, treino, avaliações, partidas, análise e relatórios.

• Testar formulários com campos obrigatórios, opcionais e condicionais.

• Testar anexos e permissões de Storage.

• Testar comportamento online, offline e após reconexão.

• Comparar resultados exibidos com dados brutos e regras de cálculo.

Entregáveis: relatório de integração e lista de ajustes.

Critério de saída: jornadas essenciais executadas sem inconsistência de dados ou acesso.

## FASE 17 — IMPLANTAÇÃO, OBSERVABILIDADE E MANUTENÇÃO

Objetivo: promover o banco com segurança e manter sua evolução controlada.

Ações:

• Definir ambientes de desenvolvimento, homologação e produção.

• Definir backup, restauração, rollback, logs, alertas e auditoria.

• Definir processo para novas versões das regras do esporte.

• Registrar decisões arquiteturais e mudanças de schema.

• Planejar revisão periódica de policies, índices, armazenamento e retenção.

Entregáveis: runbook operacional, plano de continuidade e processo de evolução.

Critério de saída: implantação repetível, monitorada e reversível.

# 7\. PORTÕES DE VALIDAÇÃO

• Portão A — Fontes: inventário, autoridade, vigência e cobertura aprovados.

• Portão B — Conhecimento: glossário, regras, conflitos e dúvidas revisados.

• Portão C — Produto: atores, jornadas, requisitos e consultas aprovados.

• Portão D — Conceitual: entidades, eventos, relações e temporalidade aprovados.

• Portão E — Lógico: tabelas, chaves, normalização e dicionário aprovados.

• Portão F — Físico e segurança: tipos, constraints, RLS, Storage e sincronização aprovados.

• Portão G — Implementação: migrations aplicadas e verificadas em ambiente de desenvolvimento.

• Portão H — Aceite: testes, integração, desempenho, documentação e rollback aprovados.

A inteligência artificial não deverá avançar para a etapa seguinte quando houver bloqueio crítico no portão anterior.

# 8\. REGRAS PARA O USO DAS FONTES CIENTÍFICAS

• Estudos científicos poderão originar métricas, categorias de observação, testes físicos, indicadores, relatórios e hipóteses analíticas.

• Resultados de uma amostra científica não serão transformados automaticamente em regra obrigatória para a equipe.

• Categorias científicas poderão ser adaptadas para o PWA, desde que sua origem e adaptação sejam documentadas.

• Quando estudos discordarem, o sistema deverá preservar as alternativas ou registrar a decisão adotada.

• Conclusões descritivas, como maior frequência de uma zona ou posição, serão tratadas como evidência para análise, não como constraint.

# 9\. REGRAS PARA DECISÕES DE MODELAGEM

• Uma tabela só será criada quando houver identidade, ciclo de vida, relacionamento ou necessidade de consulta que justifique sua persistência.

• Um atributo só será obrigatório quando a fonte ou o requisito demonstrar obrigatoriedade no contexto correto.

• Enums serão usados apenas para conjuntos pequenos e estáveis; valores sujeitos a evolução preferirão tabelas de referência ou checks controlados.

• JSONB será reservado para dados realmente variáveis ou de integração, não como substituto da modelagem relacional.

• Regras históricas serão versionadas; fatos já ocorridos manterão seus valores efetivos.

• Triggers e funções serão usados apenas quando constraints declarativas ou transações da aplicação não forem suficientes.

• Índices serão justificados por integridade ou por consultas verificadas.

• Toda desnormalização deverá documentar motivo, fonte de verdade e estratégia de atualização.

# 10\. REGISTRO DE DECISÕES E INCERTEZAS

Cada decisão relevante será registrada com:

• identificador;

• questão ou problema;

• fontes consultadas;

• alternativas consideradas;

• decisão adotada;

• justificativa;

• impacto no modelo, PWA, segurança e testes;

• responsável pela validação;

• status e possibilidade de revisão.

Perguntas abertas não serão ocultadas em comentários de SQL; permanecerão em um backlog rastreável até sua resolução.

# 11\. ESTADO ATUAL REAL DO PROJETO

• Objetivo desta conversa: congelado e registrado.

• Documento CEPRAEA-DB: localizado e usado como destino deste plano.

• Pasta BEACH HANDBALL: localizada e inventariada preliminarmente.

• Arquivos da pasta: ainda não analisados integralmente em sua totalidade.

• Fontes prioritárias: algumas foram lidas parcialmente ou em maior profundidade para orientar a compreensão inicial.

• Glossário consolidado: não concluído.

• Catálogo integral de regras: não concluído.

• Matriz de rastreabilidade: não criada.

• Requisitos completos do PWA: não validados.

• Modelo conceitual: não aprovado.

• Modelo lógico e dicionário de dados: não criados nem aprovados.

• DER: não criado.

• SQL, migrations e policies: não criados.

• Banco Supabase: não criado por esta conversa.

As tabelas e campos sugeridos anteriormente permanecem como hipóteses preliminares sujeitas ao fluxo deste plano.

# 12\. SEQUÊNCIA IMEDIATA APÓS O ACEITE DESTE PLANO

• Executar a Fase 1 e produzir o inventário integral e verificável de todos os arquivos.

• Executar a Fase 2 e fechar a hierarquia e a vigência das fontes.

• Executar a Fase 3 em todos os arquivos acessíveis, registrando limitações.

• Somente depois iniciar a extração consolidada de conceitos e regras.

• Não gerar novo conjunto de tabelas antes da conclusão dos Portões A, B e C.

# 13\. DEFINIÇÃO DE PRONTO DO PLANO COMPLETO

Este plano será considerado cumprido somente quando:

• todas as fontes tiverem status e cobertura documentados;

• todas as decisões de modelagem forem rastreáveis;

• os requisitos do PWA estiverem validados;

• os modelos conceitual, lógico e físico forem aprovados em seus portões;

• as policies e os dados sensíveis estiverem protegidos;

• o banco puder ser recriado por migrations;

• os testes derivados das regras forem executados;

• as jornadas do PWA funcionarem online e offline;

• o desempenho das consultas críticas estiver verificado;

• existirem procedimentos de implantação, rollback, backup e evolução.

# 14\. DECLARAÇÃO DE COMPROMISSO OPERACIONAL

A partir desta versão, o CEPRAEA-DB é o documento mestre do plano. A inteligência artificial deverá usar este fluxo como referência de sequência, escopo e controle de qualidade. Sugestões prematuras de tabelas ou campos não poderão ser apresentadas como resultado definitivo. A criação do banco somente ocorrerá após a execução e validação das fases e portões correspondentes.

PACOTE OPERACIONAL DE GOVERNANÇA ADAPTATIVA

Grafo de dependências obrigatório: ACT-F00-002 → ACT-F00-003 → (ACT-F00-004 paralela à ACT-F00-005) → ACT-F00-006 → ACT-F00-007 → ACT-F00-008 → ACT-F00-009 → GATE-F00-GOV-01.

ACT-F00-002

Identificador: ACT-F00-002

Nome: Sanear a fronteira normativa e reconciliar o estado atual

Objetivo: Garantir que exista uma única camada operacional vigente e uma única fonte canônica de estados (STATE-REGISTRY.json).

Fase: Fase 0

Subdomínio: Governança e controle de processo

Tipo Semântico: Ação de controle

Via Atribuída (Assigned Lane): VIA\_CRITICA

Entradas Autorizadas: Versão atual do CEPRAEA-DB

Precondições: ACT-F00-001 VALIDADA

Dependências: Nenhuma

Procedimento: Identificar a versão legada após C28; isolá-la em um "APÊNDICE HISTÓRICO — SEM AUTORIDADE OPERACIONAL". Reconciliar o estado de todas as ações da Fase 4. Criar o registro canônico em JSON. Reescrever C28.16 para consumir este registro.

Saídas: APÊNDICE HISTÓRICO, STATE-REGISTRY.json, LEGACY-BOUNDARY-REPORT.json, C28.16 corrigida.

Evidências Obrigatórias: Readback da persistência e teste de unicidade normativa.

Testes Aplicáveis: Busca negativa por duplicidade de seções normativas.

Riscos: A IA recuperar e executar comandos de uma versão legada.

Controles: Separação física e semântica do apêndice.

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: PRONTO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: ACT-F00-003

Critérios de Aceitação: Existe apenas uma seção operacional vigente; o apêndice declara ausência de autoridade; o registro canônico informa o estado atual; C28.16 coincide com o registro canônico; não há estados sobrepostos.

ACT-F00-003

Identificador: ACT-F00-003

Nome: Instituir vocabulário epistemológico, papéis e autoridades

Objetivo: Separar formalmente produção, autoteste, validação estrutural, revisão semântica e aprovação humana, reservando "APROVADO" à decisão do Approver.

Fase: Fase 0

Subdomínio: Governança da IA

Tipo Semântico: Regra

Via Atribuída (Assigned Lane): VIA\_CRITICA

Entradas Autorizadas: CEPRAEA-DB atualizado por ACT-F00-002

Precondições: ACT-F00-002 em PRODUZIDO

Dependências: ACT-F00-002

Procedimento: Atualizar C3 com papéis MAKER, VALIDATOR, CHECKER e APPROVER. Atualizar C5 com a autoridade de transição. Proibir emissão de APROVADO por modelos na produção e validação, garantindo que qualquer ocorrência fora do escopo humano seja rejeitada pelo validador externo.

Saídas: Matriz de papéis, matriz de autoridade por transição, vocabulário em JSON, regras de proibição.

Evidências Obrigatórias: Schemas atualizados com enumerações restritivas.

Testes Aplicáveis: Teste negativo enviando APROVADO em CHECKER\_REPORT.

Riscos: Ambiguidade epistemológica (falsa equivalência entre autoteste e revisão).

Controles: Rejeição via JSON Schema de valores proibidos.

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: PRONTO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: ACT-F00-004 e ACT-F00-005

Critérios de Aceitação: APROVADO é aceito somente em registro de decisão humana; saída do Maker/Checker não pode conter aprovação; schemas rejeitam valores incompatíveis.

ACT-F00-004

Identificador: ACT-F00-004

Nome: Implementar classificação de risco e atualizar C10

Objetivo: Classificar toda ação antes da execução (Impacto, Propagação, Reversibilidade, Ambiguidade, Sensibilidade) e aplicar controles proporcionais.

Fase: Fase 0

Subdomínio: Controle de processo

Tipo Semântico: Regra

Via Atribuída (Assigned Lane): VIA\_CRITICA

Entradas Autorizadas: Matrizes de ACT-F00-003

Precondições: ACT-F00-003 em PRODUZIDO

Dependências: ACT-F00-003

Procedimento: Criar schemas de classificação. Implementar gatilhos de elevação (ex: regra normativa → VIA\_CRITICA). Registrar a via antes de executar. Proibir rebaixamento silencioso de via, exigindo decisão formal documentada.

Saídas: risk-classification.schema.json, routing-rules.json, nova seção C10.

Evidências Obrigatórias: Artefato JSON de classificação para ações de teste.

Testes Aplicáveis: Validação de elevação obrigatória por gatilho.

Riscos: Classificação incorreta enviar ação crítica para via insuficiente.

Controles: Gatilhos determinísticos e conservadores; rebaixamento sujeito à autorização.

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: PRONTO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: ACT-F00-006 (se ACT-F00-005 também estiver concluída)

Critérios de Aceitação: Toda ação exige classificação nas 5 dimensões; nenhuma ação inicia sem assigned\_lane; regra normativa aciona VIA\_CRITICA; rebaixamento exige DECISAO\_DE\_RECLASSIFICACAO.

ACT-F00-005

Identificador: ACT-F00-005

Nome: Instituir contrato JSON, canonicalização e hash em C7

Objetivo: Estabelecer o JSON validado como representação canônica operacional, atrelando aprovações ao hash criptográfico do conteúdo.

Fase: Fase 0

Subdomínio: Engenharia de Dados

Tipo Semântico: Regra

Via Atribuída (Assigned Lane): VIA\_CRITICA

Entradas Autorizadas: Regras estruturais C7

Precondições: ACT-F00-003 em PRODUZIDO

Dependências: ACT-F00-003

Procedimento: Definir fluxo: JSON → Validação → Canonicalização (excluindo metadados voláteis) → Hash. Estabelecer que o Markdown é projeção derivada e não base de identidade. Definir escopos: content\_hash, source\_hash, package\_hash, approval\_hash.

Saídas: Schemas atualizados, definições de canonicalização, registro de aprovação vinculado.

Evidências Obrigatórias: Vetores de teste positivos e negativos de canonicalização.

Testes Aplicáveis: Teste provando que alteração exclusiva no Markdown derivado não altera o content\_hash.

Riscos: Hash quebrar por alteração cosmética (espaço, quebra de linha).

Controles: Processo determinístico de ordenação de chaves e normalização antes do hash.

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: PRONTO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: ACT-F00-006 (junto com a 004)

Critérios de Aceitação: JSON inválido não recebe hash; ordem diferente de propriedades gera mesmo hash; alteração semântica muda o hash; aprovação vinculada a hash obsoleto é rejeitada.

ACT-F00-006

Identificador: ACT-F00-006

Nome: Converter C27 em protocolo transversal de falsificação

Objetivo: Direcionar o Checker para procurar ativamente omissões, inversões e quebras contratuais, atuando como agente de falsificação, não de aprovação.

Fase: Fase 0

Subdomínio: Engenharia de Qualidade

Tipo Semântico: Regra

Via Atribuída (Assigned Lane): VIA\_CRITICA

Entradas Autorizadas: ACT-F00-004 e ACT-F00-005 em PRODUZIDO

Precondições: Roteamento e contratos JSON vigentes

Dependências: ACT-F00-004, ACT-F00-005

Procedimento: Exigir CHECKER\_REPORT.json com os resultados CONFORME, DIVERGENCIA\_ENCONTRADA ou INCONCLUSIVO. Divergências com impacto MATERIAL, ALTO ou CRITICO mantêm a unit\_state em EM\_REVISÃO e atribuem review\_disposition = HUMAN\_EXCEPTION\_REVIEW.

Saídas: checker-report.schema.json, regras C27 atualizadas.

Evidências Obrigatórias: Relatório válido do Checker identificando divergência.

Testes Aplicáveis: Teste negativo forçando o Checker a usar linguagem de validação e avaliando a rejeição do schema.

Riscos: Falso negativo semântico (Checker ignorar o mesmo erro do Maker).

Controles: Exigência de localizador para evidências; encaminhamento à amostragem humana.

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: PRONTO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: ACT-F00-007

Critérios de Aceitação: Checker não altera artefato do Maker; emite apenas os três resultados permitidos; toda divergência possui campo e evidência; divergência material força HUMAN\_EXCEPTION\_REVIEW.

ACT-F00-007

Identificador: ACT-F00-007

Nome: Implementar o enforcement externo local

Objetivo: Materializar a estrutura física do repositório, o runtime autoritativo e os entrypoints executáveis para validação dos artefatos.

Fase: Fase 0

Subdomínio: LLMOps operacional, Policy as Code

Tipo Semântico: Controle

Via Atribuída (Assigned Lane): VIA\_CRITICA

Entradas Autorizadas: Schemas e regras produzidos nas ações 004, 005 e 006

Precondições: Contratos lógicos fechados

Dependências: ACT-F00-006

Procedimento: Criar os diretórios físicos (schemas, policies, src, tests, artifacts). Implementar comandos (validate, route, canonicalize, hash). Fixar dependências. Implementar lint em CI/pre-commit.

Saídas: Repositório estruturado, scripts operacionais, lockfile.

Evidências Obrigatórias: Execução local reportando exit code 0 para vetores positivos e exit code != 0 para vetores negativos.

Evidência de Execução: PR 16 do repositório cepraea/beach-pro; workflow Governance enforcement, run 30709984474, concluída com sucesso em npm ci, governance:test e validate; PR integrada em main pelo merge commit 4d7f3f1f5c994cb796a787e42b8a2e7a345496c2 em 2026-08-01.

Testes Aplicáveis: Testar se texto da IA substitui a resposta do validador (deve falhar).

Riscos: Complexidade paralisar extração.

Controles: Único runtime autoritativo e comandos enxutos.

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: VALIDADO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: ACT-F00-008

Critérios de Aceitação: A estrutura física existe; os entrypoints são executáveis; testes negativos retornam código não zero independentemente do texto gerado pelo LLM.

ACT-F00-008

Identificador: ACT-F00-008

Nome: Migrar os registros históricos e executar testes regressivos

Objetivo: Normalizar usos legados de APROVADO sem apagar o histórico, utilizando o modelo append-only.

Fase: Fase 0

Subdomínio: Governança de Dados

Tipo Semântico: Ação de controle

Via Atribuída (Assigned Lane): VIA\_CONTROLADA

Entradas Autorizadas: Registro de Estados (STATE-REGISTRY.json)

Precondições: Runtime de ACT-F00-007 funcional

Dependências: ACT-F00-007

Procedimento: Mapear instâncias legadas de APROVADO. Acrescentar a normalização preservando legacy\_result e injetando normalized\_result = AUTOTESTE\_CONFORME, historical\_record = true e human\_approval\_inferred = false. Executar busca garantindo que nenhum novo campo normativo utilize o termo proibido.

Saídas: Relatório de migração, registros atualizados.

Evidências Obrigatórias: Arquivo JSON com instâncias migradas preservadas.

Testes Aplicáveis: Busca de ocorrências ativas do termo proibido (deve retornar zero).

Riscos: Corrupção de autoridade (migração fabricar aprovação humana).

Controles: Testes regressivos assegurando negação de inferência humana.

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: PRONTO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: ACT-F00-009

Critérios de Aceitação: 100% das ocorrências históricas foram migradas em modelo append-only; zero ocorrências de APROVADO ativas em campos do Maker/Checker; nenhuma ocorrência histórica atua como decisão de portão.

ACT-F00-009

Identificador: ACT-F00-009

Nome: Executar o piloto integrado e liberar a extração em lote

Objetivo: Validar as três vias de garantia e o enforcement externo extraindo um pacote heterogêneo de regras antes da escala máxima.

Fase: Fase 0

Subdomínio: Engenharia de Qualidade

Tipo Semântico: Teste

Via Atribuída (Assigned Lane): VIA\_CONTROLADA

Entradas Autorizadas: Fontes congeladas

Precondições: Todas as ações 002 a 008 concluídas e integradas

Dependências: ACT-F00-008

Procedimento: Executar lote contendo: 1 regra normativa, 1 condição, 1 exceção, 1 proibição/obrigação, 1 conceito, 1 evidência científica, 1 material técnico, 1 hipótese, 1 UC com múltiplas origens, 1 UC com conflito entre origens, 1 com temporalidade, 1 com jurisdição, 1 UC com baixa confiança. Testes negativos forçados: 1 localizador inválido, 1 saída fora do schema, 1 Checker emitindo APROVADO.

Saídas: Pacote JSON canônico, relatórios de validação e relatório do Checker.

Evidências Obrigatórias: Hashes calculados e validações estruturais com falha nos vetores negativos.

Testes Aplicáveis: Validação de todo o ecossistema.

Riscos: Falso positivo na amostra.

Controles: Revisão humana integral do lote piloto (100%).

Responsável pela Validação: Proprietário do projeto

Portão Relacionado: GATE-F00-GOV-01

Estado Atual: PRONTO

Bloqueios: Nenhum

Perguntas Abertas: Nenhuma

Próxima Ação Permitida: Submissão ao GATE-F00-GOV-01

Critérios de Aceitação: Checker rodou; vetores negativos de teste falharam externamente (código de saída não zero); Markdown foi derivado do JSON; revisão tratou os itens bloqueados.

GATE-F00-GOV-01 — MATERIALIZAÇÃO DA GOVERNANÇA ADAPTATIVA

Objetivo do Portão: Assegurar que a infraestrutura para mitigação do excesso de controle (Vias de Garantia) e contenção de alucinação (Enforcement Físico) está operante.

Entradas Obrigatórias:

\- STATE-REGISTRY.json

\- Relatório de saneamento normativo (ACT-F00-002)

\- Schemas versionados e Política de roteamento (ACT-F00-004 e ACT-F00-005)

\- Relatório de hashes e canonicalização

\- Relatório de migração append-only (ACT-F00-008)

\- Relatório do Piloto (ACT-F00-009)

Autoridade de Decisão: Approver Humano Competente

Condições de Resultado:

APROVADO: O sistema reduz a probabilidade de afirmações não sustentadas, transforma alucinações em erros tipificados, bloqueáveis e rastreáveis externamente, e o portão emite o estado FASE\_4\_EXTRAÇÃO\_EM\_LOTE\_LIBERADA.

APROVADO\_COM\_RESSALVAS: Somente extrações triviais/VIA\_RAPIDA autorizadas até resolução de ressalvas documentadas.

REPROVADO: Volta para saneamento de código.

BLOQUEADO: Impede absolutamente qualquer avanço para a Fase 4.

Diretriz de Execução Imediata: Confirmada a integração deste escopo no CEPRAEA-DB, deve-se instanciar o ambiente físico de testes (ACT-F00-007) para prosseguir em linha com a Execução do Piloto Integrado (ACT-F00-009).