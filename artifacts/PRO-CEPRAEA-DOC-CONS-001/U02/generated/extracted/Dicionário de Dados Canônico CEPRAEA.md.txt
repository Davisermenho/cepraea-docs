**Guia 1: Dicionário de Dados Canônico CEPRAEA**

---

[METADADOS_SISTEMA]

ID_FONTE: DAT-005

TITULO_CANONICO: DAT-005 Glossário de Dados Canônico CEPRAEA

FILE_ID: 1EAobzpLQFYTiYd8xUmBv_ArQeaFu3U-_ZukBGz6AinE

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Bases de Dados

SUBCATEGORIA: Dicionário de Dados

DATA_HOMOLOGACAO: 2026-10-13

AUTORIDADE: Davi Sermenho

ESCOPO: Dicionário de Dados Canônico e especificação arquitetural do CEPRAEA

[FIM_METADADOS]

---

Dicionário de Dados Canônico CEPRAEA

# Papel do Arquivo

Este documento atua como a especificação central e autoritativa do Dicionário de Dados Canônico do CEPRAEA, servindo de referência completa para a arquitetura, governança, proveniência e modelagem relacional dos dados esportivos, operacionais e táticos do clube.

# Escopo do Arquivo

O escopo deste arquivo abrange o detalhamento completo dos 5 blocos estruturais do sistema de dados:

-   **Bloco 1:** Cadastro e Atribuição Tática (Atletas, Posições e Versatilidade).
-   **Bloco 2:** Operação, Agenda, Treinos e Presenças Factuais.
-   **Bloco 3:** Competições, Convocações, Jogos e Participação Real.
-   **Bloco 4:** Scout Observacional, Eventos Táticos e Proveniência Metodológica (P0–P3 / A1–A4).
-   **Bloco 5:** Governança, Trilha Append-Only, Regras de Integridade, Testes de Regressão e Camadas de Exportação para Frontend e Dashboards.

No handebol de praia, o jogo é disputado por **4 jogadoras em quadra** (3 jogadoras de linha e 1 goleira) [1, 2]. Durante a fase ofensiva, a equipe realiza a substituição da goleira por uma jogadora de linha vestida como **Especialista**, gerando uma constante **superioridade numérica de 4 contra 3 no ataque** [2].

As posições dividem-se conforme as funções de **ataque** e **defesa** [3]:

### Posições Ofensivas (Ataque)

-   **Especialista (Coringa):** Jogadora que entra vestindo a camisa de cor diferente para criar a vantagem numérica [2]. Quaisquer gols marcados pela especialista ou pela goleira valem **2 pontos** sem a necessidade de gestos acrobáticos [2, 4]. Pode atuar tanto no centro quanto nas laterais [2, 5, 6].
-   **Central (Playmaker):** Atua no centro da quadra como a principal construtora e organizadora do ataque [7, 8]. É responsável por ler a defesa, ditar o ritmo de jogo e distribuir assistências para os arremessos em giro ou aéreas [7-9].
-   **Lateral Esquerda e Lateral Direita:** Atuam nas alas do ataque [2, 3]. Suas funções envolvem a fixação das defensoras para gerar espaços, a troca de passes de continuidade e a finalização de jogadas por meio de giros (360°) ou pontes aéreas [10-13].
-   **Pivô:** Joga infiltrada entre as defensoras adversárias próximas à linha de área [14, 15]. É responsável por regular os espaços livres, servir de apoio seguro quando a central é pressionada e finalizar jogadas de ponte aérea [14, 15].

### Posições Defensivas (Defesa)

-   **Goleira:** Responsável por defender a baliza e iniciar imediatamente a transição ofensiva ou contra-ataque após uma defesa ou sofrer um gol [16, 17].
-   **Defensora Base (Central):** Atua no centro da primeira linha defensiva [18, 19]. É a principal organizadora da comunicação da equipe, responsável por fechar a zona central e proteger o gol contra os arremessos da central e da pivô [18, 19].
-   **Defensora Solta (Pressão):** Atua na contenção direta da jogadora com a posse de bola para tirar a central e as armadoras da zona de conforto e quebrar a velocidade do ataque [20].
-   **Defensora de Cobertura (Atrás da Pivô):** Atua no combate direto à pivô adversária, buscando anular as linhas de passe para a área e realizando bloqueios duplos [18, 21].
-   **Defensora Avançada:** Utilizada em formações defensivas abertas (como o sistema 2:1), posicionando-se mais à frente para pressionar a jogadora central do adversário longe da linha de 6 metros [22, 23].

# 

No seu caderno de fontes, há um conjunto de documentos dedicados exatamente a resolver o problema do autorrelato em planilhas manuais e à garantia de que os dados permaneçam compreensíveis e íntegros ao longo de anos [1, 2].

Para estruturar esse processo, as fontes do seu notebook dividem o tema em três pilares fundamentais: **Engenharia do Conhecimento / Modelagem Semântica**, **Arquitetura de Banco de Dados / Governança de Acesso** e **Metodologia Científica / Proveniência do Dado** [2-4].

### 1. Dicionário de Dados, Significado e Identidade Canônica

Quando as próprias atletas preenchem a planilha, o erro mais comum é confundir **intenção ou autorrelato** com **fato verificado** [1, 5]. As fontes do notebook estabelecem as seguintes diretrizes para definir significados e dicionários de dados:

-   **Distinção entre Fatos, Intenções e Propostas:** Uma declaração feita pela atleta (ex.: "vou ao treino") expressa intenção prospectiva, mas não comprova comparecimento factual [1, 5, 6]. O sistema deve separar a camada de autorrelato (ex.: DB_DISPONIBILIDADE_DECLARADA ou DB_PRESENCA_PROPOSTA) da fonte canônica de fatos (ex.: DB_PRESENCA) [1].
-   **Identidade Estável (athlete_id):** Nomes e rótulos mudam com o tempo ou possuem variações de grafia [1, 7]. Para garantir que o registro continue idêntico daqui a 10 anos, a chave de ligação deve ser um identificador imutável (ex.: ATH-0001), tratando o nome escrito na planilha apenas como rótulo de exibição [1, 7].
-   **Dicionário de Variáveis e Vocabulário Controlado:** Cada campo deve possuir definições estritas de inclusão, exclusão, valores permitidos e tratamento de vazios (ex.: diferenciar uma resposta em branco de um "Não") [1, 8].

### 2. Atores, Papéis no Sistema, Relações e Cardinalidades

Para evitar que edições diretas na planilha corrompam o histórico ou gerem dados ambíguos, as fontes tratam das responsabilidades no sistema e das relações estruturais [6, 9, 10]:

-   **Atores e Papéis no Sistema:**
    -   **Atleta (Autorrelato / Consulta):** Tem permissão para declarar sua disponibilidade, responder questionários e visualizar seus próprios dados, mas não possui autoridade para promover propostas a fatos automáticos ou alterar dados de terceiros [1, 9].
    -   **Treinador / Steward (Autoridade Factual):** Papel responsável por homologar, aprovar ou confirmar presenças e convocações factuais pós-sessão [1, 11, 12].
    -   **Data Steward / Modelador:** Papel técnico encarregado de manter a integridade, o dicionário de conceitos e as regras de negócio [6, 12, 13].
-   **Governança de Acesso (RLS — *Row Level Security*):** No nível de sistema, a política de acesso garante que a atleta acesse e preencha apenas as suas próprias linhas, sem capacidade de modificar cadastros globais [9, 14].
-   **Relações e Cardinalidades (Modelagem Relacional):**
    -   **Decomposição N:N:** Uma atleta participa de vários jogos e um jogo possui várias atletas. A modelagem exige tabelas intermediárias de vínculo (ex.: DB_PARTICIPACAO_JOGO) para registrar o contexto de cada jogo sem duplicar o cadastro da atleta [6, 7].
    -   **Chaves de Unicidade:** Garantia de que exista no máximo um estado corrente para a combinação evento_id + athlete_id, permitindo atualizações (*upsert*) sem duplicar linhas [1].

### 3. Preservação Temporal e Validação Científica (Durabilidade para 10+ Anos)

Para que um dado coletado hoje mantenha o mesmo significado semântico daqui a uma década, a ciência e a engenharia de dados aplicam os seguintes princípios [4, 6, 15]:

-   **Modelagem Temporal e Imutabilidade Histórica (*Append-Only* e *Snapshots*):** Alterações de cadastro ou mudanças de regulamento futuras não podem reescrever retroativamente registros passados [6, 15]. O histórico deve ser preservado de forma acumulativa (*append-only* ou via *effective dating*), garantindo auditabilidade temporal [6, 15].
-   **Matriz de Proveniência do Dado:** O dado deve indicar a sua origem (se veio de observação humana direta, de vídeo, de formulário autorrelatado ou de cálculo derivado) [4, 16, 17]. Uma hipótese ou interpretação analítica jamais deve ser gravada no banco como se fosse um dado observado de fato [17].
-   **Metodologia Observacional e Validação de Confiabilidade:** Na ciência esportiva, o registro de eventos requer rigor metodológico ad hoc [18, 19]. Para garantir que dois observadores (ou a mesma pessoa em momentos diferentes) registrem o mesmo fenômeno de forma idêntica, aplicam-se testes estatísticos de fidedignidade, como o **Kappa de Cohen** (concordância intra/inter-observador) e o **Fleiss' Kappa** [20-24].

### Principais Fontes do seu Notebook para Consulta

1.  **Fluxo de Modelagem.gdoc (Guia 1 e Guia 2):** Documento central sobre Engenharia do Conhecimento e Modelagem Semântica [2, 11]. Detalha a separação entre cadastro, vínculo, convocação, presença e disponibilidade, regras de RLS, temporalidade e governança de dados [6, 9, 25, 26].
2.  **CEPRAEA DATABASE (Aba DB_CONFIG e Registro DEC-DATA-045):** Exemplos práticos do contrato de dados da equipe [1]. Apresenta a implementação das regras RN-DISP-001 a RN-DISP-017, normalização de entradas humanas, chaves canônicas e a separação entre declaração e presença factual [1].
3.  **Protocolo de Scout — Beach Handball (Guias 02, 05, 06 e 11):** Trata do modelo de proveniência (P0 a P3, A1 a A4), dicionários de variáveis, manuais de codificação e testes de confiabilidade [4, 8, 27, 28].
4.  **Artigos Científicos de Observação Tática e Desempenho:**
    -   *Zapardiel-Cortés et al. (2025)* (DEVELOPMENT_OF_AN_INSTRUMENT...) [22, 29].
    -   *Morillo-Baro & Hernández-Mendo (2015)* e *Vázquez-Diz et al.* (A_importância_das_posições... e Estudo das ações do guarda redes...) [19-21, 30].
    -   Tratam da criação de instrumentos *ad hoc*, validação por painel de especialistas e fidedignidade estatística (*Kappa*) [20, 22, 23].

### 1. Estrutura Canônica de Metadados (Ficha da Variável)

Cada campo ou variável registrado no dicionário deve conter uma ficha completa de atributos [2]:

1.  **Identificador Estável (VAR_ID):** Chave primária imutável e única (ex.: VAR-001, ATH-0001, TRN-2026-08-06) [1-4].
2.  **Nome Canônico:** Nome padronizado do campo no banco (ex.: posicao_principal, status_presenca, origem_posse) [2, 3, 5, 6].
3.  **Definição Operacional:** Descrição exata e inequívoca do significado semântico do campo [2].
4.  **Unidade de Análise / Aplicação:** A qual entidade a variável pertence (ex.: Atleta, Treino, Jogo, Posse, Evento) [2, 7-9].
5.  **Valores Permitidos (Domínio Fechado / Enums):** Lista estrita de entradas aceitas (ex.: SIM, NAO, TALVEZ, SEM_RESPOSTA), eliminando texto livre imprevisível [1, 2, 10].
6.  **Tipo de Dado & Natureza Epistemológica:**
    -   **Tipo Técnico:** Texto, Inteiro, Decimal, Timestamp, Boolean, Chave Estrangeira (FK) [2, 7, 11].
    -   **Natureza Epistemológica:** Classificação entre **Observável** (fato direto), **Derivado** (cálculo automático), **Inferencial** (interpretação/leitura) ou **Latente** (não observável diretamente) [2, 11-13].
7.  **Regras de Inclusão e Exclusão:** Condições em que o campo deve e **não** deve ser preenchido [2, 7-9].
8.  **Tratamento de Vazios (*Missing / Indeterminado*):** Regra para células em branco (ex.: diferenciar SEM_RESPOSTA de NAO ou NAO_APLICAVEL) [1, 2, 10, 14].
9.  **Exemplos Positivos e Negativos / Casos-Limite:** Casos práticos demonstrando o preenchimento correto e incorreto [2, 7, 8, 14].
10.  **Proveniência e Autoridade (*Source / Decision*):** Origem da regra (ex.: regulamento IHF, regra de negócio RN-DISP-005 ou confirmação do treinador) [1, 2, 5].
11.  **Status de Governança e Validação:** Estado do ciclo de vida da variável (ex.: VIGENTE, EXPERIMENTAL, PENDENTE, REJEITADO, SUBSTITUÍDO) [2, 15].

### 2. Modelo Prático de Tabela do Dicionário de Dados

Na prática (em uma planilha de governança ou tabela DB_CONFIG / DB_DICTIONARY), o dicionário é organizado com a seguinte estrutura [1, 2, 16]:

| **var_id** | **nome_campo** | **entidade** | **tipo_dado** | **valores_permitidos** | **definicao_operacional** | **regra_vazio** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-001** | athlete_id | Atleta | Texto (PK) | Chave formato ATH-XXXX | Identificador único e imutável da atleta | Proibido vazio (NOT NULL) | Cadastro de Atletas (DB_ATLETAS) [1, 3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-002** | resposta_disponibilidade | Disponibilidade | Enum | SIM, NAO, TALVEZ, SEM_RESPOSTA | Declaração de intenção de comparecimento da atleta | Converter célula em branco para SEM_RESPOSTA | Formulário do Mês / RN-DISP-005 [1, 10] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-003** | status_presenca | Presença | Enum | PRESENTE, AUSENTE, FALTA_JUSTIFICADA | Fato observado e confirmado pós-sessão pela autoridade técnica | Não preencher sem confirmação do treinador | Confirmação do Treinador (DEC-DATA-045) [1, 5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-004** | extensao_participacao | Presença | Enum | FULL, PARTIAL, NAO_APLICAVEL | Extensão da participação efetiva no treino | Preencher apenas se status_presenca = PRESENTE | Wellness Pós + Confirmação do Treinador [1, 5] |
| --- | --- | --- | --- | --- | --- | --- | --- |

### 3. Regras de Ouro para Manter o Dicionário Válido por 10+ Anos

-   **Separação entre Chaves e Rótulos:** Nomes de atletas, locais ou competições mudam ou sofrem erros de digitação. O dicionário deve forçar que todos os relacionamentos utilizem a chave estável (athlete_id, treino_id), tratando o nome escrito na planilha apenas como rótulo de exibição [1, 3, 17].
-   **Normalização Automática de Entradas Humanas:** Aplicar regras de sanitização (TRIM, caixa alta, remoção de acentos) para garantir que entradas humanas como "Sim", "sim " ou "SIM" sejam convertidas exclusivamente para o valor canônico SIM [1].
-   **Independência Semântica:** O dicionário nunca deve permitir que uma declaração de intenção (ex.: disponibilidade SIM) seja computada automaticamente como um fato de presença (PRESENTE) sem passar pela confirmação do responsável [1, 5, 18].
-   **Imutabilidade e Snapshots Temporais:** Quando uma regra de negócio ou cadastro mudar no futuro, o dicionário deve prever campos de carimbo estático (created_at, updated_at, confirmado_em) para que os dados do passado continuem refletindo a realidade da época em que foram coletados [1, 3, 5, 19].

# 1. Cadastro & Identidade do Elenco

Este bloco governa a **fonte primária de autoridade da atleta** [7]. No CEPRAEA DATABASE, o cadastro da atleta é rigorosamente separado dos seus vínculos, convocações e declarações [7, 8]. Nomes de exibição e números de camisa são tratados como rótulos mutáveis, enquanto a chave estável athlete_id garante a integridade histórica pelos próximos 10+ anos [7, 9-11].

## 1.1. Tabela Título: DB_ATLETAS (Cadastro Canônico de Atletas)

-   **Descrição Semântica:** Entidade primária de cadastro do elenco do CEPRAEA [9, 12]. Contém a identidade estável e as autoridades cadastrais de função e posição principal [7, 9].
-   **Unidade de Análise:** 1 Linha = 1 Atleta Cadastrada [9].
-   **Chave Primária (PK):** athlete_id [9].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-001** | athlete_id | Texto (PK) | Formato estrito ATH-XXXX (ex.: ATH-0001 a ATH-9999) [9] | Identificador único, imutável e atemporal da atleta no sistema [7, 9]. Jamais reutilizado [13]. | Proibido Vazio (NOT NULL) [9, 14] | Observável / Arquitetural [15] | Script de Ingestão / Cadastro [9, 16] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-002** | nome_exibicao | Texto | Texto livre normalizado sem espaços extras [9, 16] | Nome operacional de exibição da atleta nas telas e relatórios (ex.: "Aline Augusto") [9]. | Proibido Vazio (NOT NULL) [9, 14] | Observável / Rótulo [7, 9] | Relações Nominais Oficiais / Documento de Identidade [9, 17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-003** | funcao_principal | Enum | DEFESA, ATAQUE, INDEFINIDA [18] | Macrofunção tática primária atribuída à atleta na equipe [9, 18]. | Default = INDEFINIDA [18] | Observável / Decisão Técnica [9, 18] | Decisão Humana do Treinador (DB_CONFIG.athlete_primary_function_authority) [7, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-004** | posicao_principal | Enum | GOLEIRA, CENTRAL, LATERAL ESQUERDA, LATERAL DIREITA, PIVÔ, DEFENSORA SOLTA, DEFENSORA BASE, DEFENSORA COBERTURA, CENTRAL DIREITA, CENTRAL ESQUERDA, DEFENSORA AVANÇADA [18] | Posição tática principal de atuação da atleta em quadra [9, 18]. | Proibido Vazio (NOT NULL) [9, 14] | Observável / Decisão Técnica [9, 18] | Decisão Humana do Treinador (DB_CONFIG.athlete_primary_position_authority) [7, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-005** | status_ativo | Enum | SIM, NAO [9] | Indica se a atleta compõe o elenco ativo do clube para fins de visibilidade e relatórios [9, 19]. | Default = SIM [9] | Observável / Estado Cadastral [9] | Decisão da Comissão Técnica [9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-006** | numero_camisa | Texto | Número inteiro em formato texto (ex.: 19, 85) ou INDETERMINADO [9] | Número oficial da camisa da atleta registrado na federação/confederação [9, 17]. | Default = INDETERMINADO [9] | Observável / Cadastro [9] | Relações Nominais e Boletins CBHb/FHERJ [9, 17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-007** | fonte_numero_camisa | Texto | Texto livre com citação do documento/boletim [9] | Rastreabilidade documental do número de camisa cadastrado [9]. | Permitido Vazio (NULL) [9] | Observável / Proveniência [9, 20] | Registro de Origem [9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-008** | created_at | Timestamp | Formato ISO 8601 com fuso: YYYY-MM-DDTHH:MM:SS-03:00 [9] | Carimbo estático de data/hora de criação do registro no banco [7, 9]. | Gravado na inserção (NOT NULL) [9, 14] | Observável / Auditoria [7, 9] | Sistema / Banco de Dados [7, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-009** | updated_at | Timestamp | Formato ISO 8601 com fuso: YYYY-MM-DDTHH:MM:SS-03:00 [9] | Carimbo estático de data/hora da última alteração cadastral [7, 9]. | Gravado na alteração (NOT NULL) [9, 14] | Observável / Auditoria [7, 9] | Sistema / Banco de Dados [7, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-ATH-010** | fonte_autorizada | Texto | Texto livre rastreável (ex.: "Decisão humana 2026-06-22") [9] | Descrição textual da autoridade ou reunião que homologou a classificação [9]. | Proibido Vazio (NOT NULL) [9, 14] | Observável / Proveniência [9, 20] | Log de Decisão Técnica [9] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 1.2. Tabela Título: DB_POSICOES (Vocabulário Controlado de Posições)

-   **Descrição Semântica:** Tabela de domínio fechado que define o catálogo oficial de posições táticas do handebol de praia e sua vinculação às macrofunções [18].
-   **Unidade de Análise:** 1 Linha = 1 Posição Canônica [18].
-   **Chave Primária (PK):** posicao_id [18].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-POS-001** | posicao_id | Texto (PK) | Formato estrito POS-XXXX (ex.: POS-0001 a POS-0011) [18] | Identificador canônico da posição no catálogo [18]. | Proibido Vazio (NOT NULL) [18] | Observável / Arquitetural [18] | Modelagem do Banco [18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-POS-002** | posicao | Texto (UNIQUE) | Rótulos oficiais em caixa alta (ex.: GOLEIRA, CENTRAL, PIVÔ) [18] | Nome oficial da posição tática [18]. | Proibido Vazio (NOT NULL) [18] | Observável / Vocabulário [18] | Regras IHF / Decisão Técnica [7, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-POS-003** | funcao | Enum | DEFESA, ATAQUE [18] | Macrofunção à qual a posição pertence (Regra semântica: GOLEIRA pertence a DEFESA) [7, 18]. | Proibido Vazio (NOT NULL) [18] | Observável / Taxonomia [7, 18] | Decisão Humana 2026-08-10 (DB_CONFIG.goalkeeper_semantics) [7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-POS-004** | ativo | Enum | SIM, NAO [18] | Disponibilidade da posição para uso nos formulários e sistemas [18]. | Default = SIM [18] | Observável / Estado [18] | Gestão de Vocabulário [18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-POS-005** | descricao | Texto | Texto explicativo da função tática [18] | Definição resumida do papel tático da posição [18]. | Permitido Vazio (NULL) [18] | Observável / Documentação [18] | Manual Técnico [18] |
| --- | --- | --- | --- | --- | --- | --- | --- |

Dicionário de Dados Canônico CEPRAEA

# Papel do Arquivo

Este documento atua como a especificação central e autoritativa do Dicionário de Dados Canônico do CEPRAEA, servindo de referência completa para a arquitetura, governança, proveniência e modelagem relacional dos dados esportivos, operacionais e táticos do clube.

# Escopo do Arquivo

O escopo deste arquivo abrange o detalhamento completo dos 5 blocos estruturais do sistema de dados:

-   **Bloco 1:** Cadastro e Atribuição Tática (Atletas, Posições e Versatilidade).
-   **Bloco 2:** Operação, Agenda, Treinos e Presenças Factuais.
-   **Bloco 3:** Competições, Convocações, Jogos e Participação Real.
-   **Bloco 4:** Scout Observacional, Eventos Táticos e Proveniência Metodológica (P0–P3 / A1–A4).
-   **Bloco 5:** Governança, Trilha Append-Only, Regras de Integridade, Testes de Regressão e Camadas de Exportação para Frontend e Dashboards.

## 1.3. Tabela Título: DB_POSICOES_SECUNDARIAS (Atribuição de Versatilidade)

-   **Descrição Semântica:** Tabela autoritativa para atribuição e governança das posições secundárias/alternativas das atletas [7, 21].
-   **Unidade de Análise:** 1 Linha = Atribuição de Versatilidade de 1 Atleta [21].
-   **Chave Primária (PK / FK):** athlete_id (Relacionamento 1:1 com DB_ATLETAS) [21].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-SEC-001** | athlete_id | Texto (PK/FK) | Chave válida existente em DB_ATLETAS.athlete_id [21] | Chave estrangeira que vincula a versatilidade ao cadastro imutável [7, 21]. | Proibido Vazio (NOT NULL) [21] | Observável / Arquitetural [21] | DB_ATLETAS.athlete_id [7, 21] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-SEC-002** | nome_exibicao | Texto | Rótulo vindo de DB_ATLETAS [21] | Espelho do nome de exibição para facilidade de leitura manual [21]. | Proibido Vazio (NOT NULL) [21] | Derivado / Rótulo [11, 21] | DB_ATLETAS.nome_exibicao [21] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-SEC-003** | posicao_secundaria_1 | Enum / Texto | Posições válidas de DB_POSICOES ou Vazio [18, 21] | Primeira posição alternativa em que a atleta está apta a atuar [21]. | Permitido Vazio (NULL) [21] | Observável / Decisão Técnica [21] | Decisão Humana do Treinador (DB_CONFIG.positions_secondary_role) [7, 21] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-SEC-004** | posicao_secundaria_2 | Enum / Texto | Posições válidas de DB_POSICOES ou Vazio [18, 21] | Segunda posição alternativa em que a atleta está apta a atuar [21]. | Permitido Vazio (NULL) [21] | Observável / Decisão Técnica [21] | Decisão Humana do Treinador (DB_CONFIG.positions_secondary_role) [7, 21] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-SEC-005** | posicao_secundaria_3 | Enum / Texto | Posições válidas de DB_POSICOES ou Vazio [18, 21] | Terceira posição alternativa em que a atleta está apta a atuar [21]. | Permitido Vazio (NULL) [21] | Observável / Decisão Técnica [21] | Decisão Humana do Treinador (DB_CONFIG.positions_secondary_role) [7, 21] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-SEC-006** | status_validacao | Enum | VALIDADO, PENDENTE [21] | Estado de validação humana das posições secundárias [21]. | Default = PENDENTE [21] | Observável / Governança [21] | Controle de Qualidade [21] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-SEC-007** | updated_at | Timestamp | Formato ISO 8601 com fuso [21] | Carimbo estático da última atualização de versatilidade [7, 21]. | Proibido Vazio (NOT NULL) [21] | Observável / Auditoria [7, 21] | Sistema / Banco de Dados [7, 21] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 1.4. Tabela Título: DB_ATLETA_POSICOES_TATICAS (Visão Tática Materializada)

-   **Descrição Semântica:** Derivação materializada controlada que consolida o perfil tático da atleta por setor (ofensivo principal/secundário, defensivo principal/secundário e goleira) [7, 22].
-   **Regra de Ouro:** Não possui autoridade cadastral direta; é recomputada deterministicamente a partir de DB_ATLETAS + DB_POSICOES_SECUNDARIAS [7, 22].
-   **Chave Primária (PK / FK):** athlete_id [22].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-001** | athlete_id | Texto (PK/FK) | Chave válida de DB_ATLETAS [22] | Chave de ligação estável [7, 22]. | Proibido Vazio (NOT NULL) [22] | Observável / Arquitetural [22] | DB_ATLETAS.athlete_id [7, 22] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-002** | ofensiva_principal | Enum / Texto | Posições Ofensivas ou Vazio [22] | Posição de ataque principal da atleta (preenchida apenas se a posição principal for de ataque) [22]. | Permitido Vazio (NULL) [22] | Derivado / Materializado [7, 22] | Derivação Controlada (DB_CONFIG.tactical_positions_regeneration_order) [7, 22] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-003** | ofensiva_secundaria | Enum / Texto | Posições Ofensivas ou Vazio [22] | Posição de ataque secundária mapeada [22]. | Permitido Vazio (NULL) [22] | Derivado / Materializado [7, 22] | Derivação Controlada [7, 22] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-004** | defensiva_principal | Enum / Texto | Posições Defensivas (exceto Goleira) ou Vazio [22] | Posição de linha defensiva principal da atleta [22]. | Permitido Vazio (NULL) [22] | Derivado / Materializado [7, 22] | Derivação Controlada [7, 22] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-005** | defensiva_secundaria | Enum / Texto | Posições Defensivas (exceto Goleira) ou Vazio [22] | Posição de linha defensiva secundária mapeada [22]. | Permitido Vazio (NULL) [22] | Derivado / Materializado [7, 22] | Derivação Controlada [7, 22] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-006** | goleira | Enum / Texto | GOLEIRA ou Vazio [22] | Sinalização de atuação na baliza [22]. | Permitido Vazio (NULL) [22] | Derivado / Materializado [7, 22] | Derivação Controlada [7, 22] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-007** | status_validacao | Enum | VALIDADO [22] | Confirmação da regeneração tática [22]. | Proibido Vazio (NOT NULL) [22] | Derivado / Governança [22] | Script de Materialização [22] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TAC-008** | updated_at | Timestamp | Formato ISO 8601 com fuso [22] | Carimbo estático da execução do script de regeneração [7, 22]. | Proibido Vazio (NOT NULL) [22] | Derivado / Auditoria [7, 22] | DB_CONFIG.tactical_positions_last_regenerated_at [7] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 1.5. Tabela Título: DB_ATLETA_POSICOES_LONG (Projeção Relacional Longa)

-   **Descrição Semântica:** Tabela desnormalizada em formato longo (*unpivoted*) para viabilizar cruzamentos eficientes (*Joins*) de cobertura tática e sistemas de jogo sem utilizar buscas por texto ou relacionamentos complexos [7, 11, 23].
-   **Unidade de Análise:** 1 Linha = 1 Combinação Válida de athlete_id × posicao_tatica [23].
-   **Chave Primária (PK Composite):** athlete_id + posicao_tatica + origem_posicao [23].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LNG-001** | athlete_id | Texto (PK/FK) | Chave válida de DB_ATLETAS [23] | Chave primária de junção estável [7, 23]. | Proibido Vazio (NOT NULL) [23] | Derivado / Arquitetural [23] | DB_ATLETA_POSICOES_TATICAS.athlete_id [7, 23] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LNG-002** | nome_exibicao | Texto | Rótulo vindo de DB_ATLETAS [23] | Nome da atleta para inspeção direta [23]. | Proibido Vazio (NOT NULL) [23] | Derivado / Rótulo [11, 23] | DB_ATLETAS.nome_exibicao [23] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LNG-003** | tipo_sistema | Enum | ATAQUE, DEFESA [23] | Fase de jogo a que a posição tática pertence [23]. | Proibido Vazio (NOT NULL) [23] | Derivado / Taxonomia [23] | DB_POSICOES.funcao [18, 23] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LNG-004** | posicao_tatica | Enum / Texto | Posições canônicas de DB_POSICOES [18, 23] | Posição específica em que a atleta está habilitada a atuar [23]. | Proibido Vazio (NOT NULL) [23] | Derivado / Projeção [23] | DB_ATLETA_POSICOES_TATICAS [22, 23] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LNG-005** | origem_posicao | Enum | ofensiva_principal, ofensiva_secundaria, defensiva_principal, defensiva_secundaria, goleira [23] | Rastreabilidade da hierarquia de onde a habilitação tática foi projetada [23]. | Proibido Vazio (NOT NULL) [23] | Derivado / Linhagem [20, 23] | Coluna de Origem em DB_ATLETA_POSICOES_TATICAS [22, 23] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LNG-006** | status_validacao | Enum | VALIDADO [23] | Status do processo de projeção [23]. | Proibido Vazio (NOT NULL) [23] | Derivado / Governança [23] | Script de Materialização [23] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LNG-007** | updated_at | Timestamp | Formato ISO 8601 com fuso [23] | Carimbo estático de execução da projeção [7, 23]. | Proibido Vazio (NOT NULL) [23] | Derivado / Auditoria [7, 23] | Sistema / Banco de Dados [7, 23] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 2. alendário, Agendas, Treinos, Disponibilidade Declarada e Presença Factual

A regra de ouro que rege a arquitetura deste bloco — estabelecida pelas diretrizes do *Fluxo de Modelagem* e consolidada pela decisão **DEC-DATA-045** e pelas normas **RN-DISP-001 a RN-DISP-017** [1-3] — é a **separação estrita entre Intenção/Declaração e Fato Ocorrido** [1, 3].

Nenhuma declaração prospectiva em planilha mensal, nem mesmo um formulário autorrelatado de pós-treino (*Wellness Pós*), é promovido automaticamente a presença factual no banco de dados [1, 4]. Todo fato de presença exige a confirmação homologada da autoridade técnica (Treinador/Steward) [1, 4, 5].

## 2.1. Tabela Título: DB_CALENDARIO / DB_EVENTOS (Grade Canônica de Eventos)

-   **Descrição Semântica:** Fonte primária de agenda e eventos (treinos, competições, reuniões). Mapeia as datas canônicas, horários, locais e define se a data está aberta para receber declarações de disponibilidade [1, 6, 7].
-   **Unidade de Análise:** 1 Linha = 1 Evento em uma Data Específica [7].
-   **Chave Primária (PK):** evento_id (ou calendario_id) [7].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-001** | evento_id | Texto (PK) | Formato estrito TRN-YYYY-MM-DD ou CAL-YYYY-MM-DD ou COMP-YYYY-XXX [6, 7] | Identificador canônico e imutável do evento no calendário [7]. | Proibido Vazio (NOT NULL) [7] | Observável / Arquitetural [7] | Sistema / Cadastro de Calendário [7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-002** | data_evento | Data | Formato DD/MM/YYYY ou YYYY-MM-DD [6, 7] | Data civil de realização do evento no fuso America/Sao_Paulo [1, 6]. | Proibido Vazio (NOT NULL) [6] | Observável / Agenda [6] | Calendário Oficial CEPRAEA [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-003** | tipo | Enum | TREINO, COMPETICAO, REUNIAO, OUTRO [6, 7] | Classificação da natureza do evento [7]. | Proibido Vazio (NOT NULL) [7] | Observável / Taxonomia [7] | Comissão Técnica [6] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-004** | horario_inicio | Texto / Hora | Formato HH:MM (ex.: 20:00, 07:00) [6, 8] | Horário oficial de início da atividade [6, 8]. | Permitido Vazio se competição sem tabela [6] | Observável / Agenda [6] | Tabela de Treinos / Boletim Oficial [6, 8] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-005** | horario_fim | Texto / Hora | Formato HH:MM (ex.: 21:30, 09:00) [6, 8] | Horário oficial de encerramento previsto [6, 8]. | Permitido Vazio se competição sem tabela [6] | Observável / Agenda [6] | Tabela de Treinos / Boletim Oficial [6, 8] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-006** | local | Texto | Texto livre com ponto de referência (ex.: "Praia de Copacabana - Posto 4") [6, 8] | Local físico de realização do evento [6, 8]. | Proibido Vazio (NOT NULL) [8] | Observável / Logística [8] | Confirmação do Treinador / Tabela Oficial [6, 8] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-007** | status_evento | Enum | PLANEJADO, REALIZADO, PREVISTA, ENCERRADO_SEM_CONFIRMACAO, RECLASSIFICADO, CANCELADO [1, 6, 8] | Estado corrente do evento na grade [1, 8]. Treino passado sem confirmação humana passa a ENCERRADO_SEM_CONFIRMACAO [1, 8]. | Default = PLANEJADO [1, 8] | Observável / Ciclo de Vida [1, 8] | DB_CONFIG.training_lifecycle_policy / Treinador [1, 8] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CAL-008** | aceita_resposta | Enum | SIM, NAO [1, 7] | Flag de autorização para o sincronizador receber declarações de disponibilidade (Regra RN-DISP-013) [1, 7]. | Proibido Vazio (NOT NULL) [1] | Observável / Regra de Negócio [1] | DB_CONFIG.availability_event_eligibility_policy [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 2.2. Tabela Título: DB_TREINOS (Ficha Estruturada de Sessões de Treino)

-   **Descrição Semântica:** Registro canônico estruturado dos objetivos técnico-táticos, cargas e estruturas das sessões de treino (ex.: Ciclo ativo T01–T12) [8-10]. Não substitui o plano pedagógico minucioso do treinador, mas armazena os metadados necessários para governança e análise [10, 11].
-   **Unidade de Análise:** 1 Linha = 1 Sessão de Treino [8, 11].
-   **Chave Primária (PK):** treino_id [8].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-001** | treino_id | Texto (PK) | Formato estrito TRN-YYYY-MM-DD [8] | Identificador canônico do treino, vinculado a DB_CALENDARIO [8]. | Proibido Vazio (NOT NULL) [8] | Observável / Arquitetural [8] | Sistema / DB_CALENDARIO [8] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-002** | sessao_codigo | Texto | Rótulos de ciclo (ex.: T01 a T12, ORIGEM_T01) ou Vazio [8, 9, 12] | Código operacional de numeração da sessão no planejamento do ciclo ativo [8, 12]. | Permitido Vazio para treinos fora do ciclo [8] | Observável / Planejamento [8] | Planejamento Técnico Homologado [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-003** | bloco_ciclo | Enum / Texto | B1 — Corrigir e recalibrar, B2 — Construir e integrar, B3 — Resolver problemas, B4 — Consolidar [8, 9] | Bloco funcional de organização da periodização [8, 9]. | Permitido Vazio [8] | Observável / Metodologia [8] | Planejamento Técnico Homologado [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-004** | carga_planejada | Enum | L1 — BAIXA, L2 — MODERADA, L3 — ALTA [8, 9] | Nível de exigência e sustentação da sessão [8, 9]. | Default = L2 — MODERADA [8] | Observável / Prescrição [8] | Decisão do Treinador [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-005** | objetivo | Texto | Texto descritivo da meta central da sessão (ex.: "Aumentar a eficiência no shoot-out") [8, 9] | Problema principal de jogo ou objetivo N1 da sessão [8, 9, 13]. | Proibido Vazio (NOT NULL) [8] | Observável / Prescrição [8] | Decisão Técnica Homologada do Treinador [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-006** | atividade_principal | Texto | Descrição simplificada da estrutura e minutagem dos exercícios [8, 10] | Estrutura dos exercícios previstos no treino [8, 10]. | Permitido Vazio se CONTEUDO_PENDENTE [1, 8] | Observável / Prescrição [8] | Decisão do Treinador [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-007** | metas_coletivas | Texto | Indicadores e comportamentos esperados (ex.: I1: VANTAGEM_REAL-FINALIZOU) [8, 9] | Critérios e indicadores N2 observáveis de sucesso no treino [8, 9, 13]. | Permitido Vazio [8] | Observável / Indicadores [8] | Decisão do Treinador [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-TRN-008** | status_planejamento | Enum | PLANEJADO, REALIZADO, ENCERRADO_SEM_CONFIRMACAO, RECLASSIFICADO [1, 8] | Estado do planejamento do treino [8]. | Default = PLANEJADO [8] | Observável / Estado [1, 8] | Homologação Pós-Sessão do Treinador [1, 8] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 2.3. Tabela Título: DB_DISPONIBILIDADE_DECLARADA (Declarações do Elenco)

-   **Descrição Semântica:** Tabela canônica de intenções e compromissos prospectivos das atletas [1, 14]. Alimenta a análise de cobertura tática e agenda [1, 15]. Nascida do preenchimento das atletas nas abas mensais do frontend, passa por rígidas regras de sincronização (RN-DISP-001 a RN-DISP-017) [1].
-   **Unidade de Análise:** 1 Linha = 1 Declaração da Atleta para 1 Evento [1].
-   **Chave Primária e Unicidade:** Chave única composta evento_id + athlete_id (Garante estado corrente único por atleta x evento via *Upsert*, Regras RN-DISP-004 e RN-DISP-008) [1].

 ┌──────────────────────────────────────────────────────────────────────────┐

│ ÍNDICE NORMATIVO DE SINCRONIZAÇÃO (RN-DISP-001 a RN-DISP-017) │

├──────────────┬───────────────────────────────────────────────────────────┤

│ RN-DISP-001 │ Disponibilidade declarada expressa intenção; NÃO é presença factual [1]. │

│ RN-DISP-002 │ Origem exclusiva em células válidas das abas mensais do frontend [1]. │

│ RN-DISP-003 │ Identidade canônica obrigatória via athlete_id (nomes são rótulos) [1].│

│ RN-DISP-004 │ Chave evento_id|athlete_id com no máximo 1 estado corrente [1]. │

│ RN-DISP-005 │ Domínio estrito de respostas: SIM, NAO, TALVEZ, SEM_RESPOSTA [1]. │

│ RN-DISP-006 │ Célula mapeada e vazia representa SEM_RESPOSTA (nunca NAO) [1]. │

│ RN-DISP-007 │ Evento sem célula mapeada não gera registro artificial [1]. │

│ RN-DISP-008 │ Alteração de resposta atualiza o mesmo registro (Upsert, sem duplicata) [1].│

│ RN-DISP-009 │ Resposta apagada em célula válida passa a SEM_RESPOSTA (não deleta) [1].│

│ RN-DISP-010 │ Identidade ambígua de atleta ou evento falha fechado (Fail-Closed) [1].│

│ RN-DISP-011 │ Mudança material de data inativa resposta anterior e exige nova [1].│

│ RN-DISP-012 │ Exibir apenas competições de que o CEPRAEA participou/participará [1].│

│ RN-DISP-013 │ Evento requer obrigatoriamente DB_EVENTOS.aceita_resposta=SIM [1]. │

│ RN-DISP-014 │ Sincronizador consome status como snapshot (não altera o evento) [1].│

│ RN-DISP-015 │ Disponibilidade JAMAIS promove ou gera presença factual automática [1].│

│ RN-DISP-016 │ Normalização estrita (TRIM, caixa alta, remoção de acentos) [1].│

│ RN-DISP-017 │ Célula multidiária expande para todos os eventos do intervalo [1].│

└──────────────┴───────────────────────────────────────────────────────────┘



| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DSP-001** | declaracao_id | Texto (PK) | Formato DD-YYYYMMDD-ATH-XXXX ou DD-LEG-XXXX [1, 16] | Identificador único do registro de declaração [1, 16]. | Proibido Vazio (NOT NULL) [1] | Observável / Arquitetural [1] | Sincronizador de Disponibilidade [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DSP-002** | evento_id | Texto (FK) | Chave válida existente em DB_EVENTOS [1, 16] | Identificador do treino ou competição alvo (RN-DISP-013) [1]. | Proibido Vazio (NOT NULL) [1] | Observável / Arquitetural [1] | DB_EVENTOS.evento_id [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DSP-003** | athlete_id | Texto (FK) | Chave válida em DB_ATLETAS (ATH-XXXX) [1, 16] | Chave de identidade canônica da atleta (RN-DISP-003) [1]. | Proibido Vazio (NOT NULL) [1] | Observável / Arquitetural [1] | DB_ATLETAS.athlete_id [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DSP-004** | resposta | Enum | SIM, NAO, TALVEZ, SEM_RESPOSTA [1, 17] | Declaração de intenção normalizada da atleta (RN-DISP-005 e RN-DISP-016) [1]. | Célula em branco vira SEM_RESPOSTA (RN-DISP-006) [1] | Observável / Autorrelato [1] | Entrada Humana nas Abas Mensais do Frontend [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DSP-005** | origem_aba | Texto | Nome da aba de origem (ex.: AGOSTO_2026, SETEMBRO_2026) [1, 16] | Rastreabilidade da aba-fonte de preenchimento (RN-DISP-002) [1]. | Proibido Vazio (NOT NULL) [1] | Observável / Proveniência [1] | Frontend / Sincronizador [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DSP-006** | materializado_em | Timestamp | Formato ISO 8601 com fuso | Carimbo estático da gravação ou atualização do estado corrente [1]. | Proibido Vazio (NOT NULL) [1] | Observável / Auditoria [1] | Sincronizador / Banco [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 2.4. Tabela Título: DB_PRESENCA_PROPOSTA (Fila Transitória do Wellness Pós)

-   **Descrição Semântica:** Fila de propostas de presença derivadas de formulários automatizados pós-sessão (como o *Wellness Pós-Treino*) [1, 4].
-   **Regra de Isolamento:** É estritamente derivada e transitória. Não constitui fato esportivo e fica isolada do banco de produção até a decisão humana do treinador [1, 4].
-   **Unidade de Análise:** 1 Linha = 1 Proposta de Presença Autorrelatada [1, 4].
-   **Chave Primária (PK):** proposta_id [1, 4].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRP-001** | proposta_id | Texto (PK) | Formato PROP-UUID [4, 5] | Chave primária única da proposta de presença [4]. | Proibido Vazio (NOT NULL) [4] | Derivado / Arquitetural [4] | Form do Wellness Pós [1, 4] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRP-002** | treino_id | Texto (FK) | Chave válida de DB_TREINOS [4, 5] | Treino a que o autorrelato se refere [4, 5]. | Proibido Vazio (NOT NULL) [4] | Derivado / Arquitetural [4] | Resposta do Formulário [4] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRP-003** | athlete_id | Texto (FK) | Chave válida de DB_ATLETAS [4, 5] | Atleta que respondeu ao formulário [4, 5]. | Proibido Vazio (NOT NULL) [4] | Derivado / Arquitetural [4] | Resposta do Formulário [4] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRP-004** | participacao_autorrelatada | Enum | COMPLETA, PARCIAL [1, 4] | Declaração da atleta sobre sua extensão no treino [1, 4]. | Proibido Vazio (NOT NULL) [4] | Derivado / Autorrelato [1, 4] | Resposta da Atleta [4] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRP-005** | extensao_proposta | Enum | FULL, PARTIAL [1, 4] | Mapeamento técnico da extensão proposta (COMPLETA→FULL, PARCIAL→PARTIAL) [1, 4]. | Proibido Vazio (NOT NULL) [4] | Derivado / Mapeamento [4] | Regra DEC-DATA-045 [1, 4] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRP-006** | estado_derivacao | Enum | AGUARDANDO_CONFIRMACAO, CONFIRMADA_MATERIALIZADA, REJEITADA [1, 4] | Status de tramitação da proposta na fila do treinador [1, 4]. | Default = AGUARDANDO_CONFIRMACAO [1, 4] | Derivado / Tramitação [4] | Sistema / Painel do Treinador [4] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRP-007** | decisao_treinador | Enum | CONFIRMAR_PROPOSTA, AJUSTAR_FULL, AJUSTAR_PARTIAL, REJEITAR_PROPOSTA [1, 4] | Ação tomada pela autoridade técnica sobre a proposta [1, 4]. | Permitido Vazio enquanto aguarda [4] | Observável / Decisão Humana [1, 4] | Treinador CEPRAEA (DEC-DATA-045) [1, 4, 5] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 2.5. Tabela Título: DB_PRESENCA (SSOT Canônica de Presença Factual)

-   **Descrição Semântica:** A ÚNICA Fonte Primária de Verdade (*Single Source of Truth*) para presenças factuais ocorridas nos treinos [1]. Nenhuma linha é inserida nesta tabela sem o carimbo de confirmação explícita do Treinador pós-sessão [1, 4, 5].
-   **Unidade de Análise:** 1 Linha = 1 Presença Factual Confirmada de 1 Atleta em 1 Treino [5].
-   **Chave Primária (PK):** presenca_id [5].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-001** | presenca_id | Texto (PK) | Formato estrito PRES-YYYYMMDD-ATH-XXXX [5] | Chave primária única da presença factual confirmada [5]. | Proibido Vazio (NOT NULL) [5] | Observável / Arquitetural [5] | Sistema de Materialização Factual [5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-002** | treino_id | Texto (FK) | Chave válida de DB_TREINOS [5] | Identificador do treino realizado [5]. | Proibido Vazio (NOT NULL) [5] | Observável / Arquitetural [5] | DB_TREINOS.treino_id [5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-003** | athlete_id | Texto (FK) | Chave válida de DB_ATLETAS [5] | Chave de identidade imutável da atleta presente [5]. | Proibido Vazio (NOT NULL) [5] | Observável / Arquitetural [5] | DB_ATLETAS.athlete_id [5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-004** | status_presenca | Enum | PRESENTE, AUSENTE, FALTA_JUSTIFICADA [1, 5] | Fato esportivo observado do comparecimento [1, 5]. | Proibido Vazio (NOT NULL) [5] | Observável / Fato Esportivo [1, 5] | Homologação do Treinador (DEC-DATA-045) [1, 5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-005** | extensao_participacao | Enum | FULL, PARTIAL, NAO_APLICAVEL [1, 5] | Extensão da participação no treino (FULL = treino completo; PARTIAL = parte da sessão) [1, 5]. | Proibido Vazio (NOT NULL) [5] | Observável / Fato Esportivo [1, 5] | Homologação do Treinador [1, 5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-006** | confirmado_por | Texto | Identificação do responsável (ex.: "Davi Sermenho — TREINADOR CEPRAEA") [5] | Nome e papel da autoridade humana que homologou o fato [5]. | Proibido Vazio (NOT NULL) [5] | Observável / Auditoria [5] | Registro de Homologação do Treinador [5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-007** | confirmado_em | Timestamp | Formato ISO 8601 com fuso: YYYY-MM-DDTHH:MM:SS-03:00 [5] | Carimbo de data/hora exata da confirmação humana [5]. | Proibido Vazio (NOT NULL) [5] | Observável / Auditoria [5] | Sistema no evento da confirmação [5] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PRS-008** | proposta_id | Texto (FK) | Chave válida de DB_PRESENCA_PROPOSTA ou Vazio [5] | Rastreabilidade da proposta que originou a confirmação [5]. | Permitido Vazio se presença registrada sem proposta prévia [5] | Observável / Linhagem [5] | DB_PRESENCA_PROPOSTA.proposta_id [5] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 2.6. Tabela Título: DB_DISPONIBILIDADE_POSICAO (Matriz de Cobertura Tática)

-   **Descrição Semântica:** Tabela analítica derivada que calcula a cobertura tática de atletas disponíveis (SIM) para cada data de treino, cruzando os sistemas táticos (3:0, 2:1 na defesa e 3:1, 2:1 no ataque) com os 14 slots táticos da equipe [3, 15, 18].
-   **Unidade de Análise:** 1 Linha = 1 Data de Treino × 1 Slot Tático de um Sistema [15].
-   **Regra de Derivação:** Consome exclusivamente DB_DISPONIBILIDADE_DECLARADA + DB_ATLETA_POSICOES_LONG + DB_SISTEMAS_POSICOES [3, 15].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-001** | data_treino | Data | Data em formato DD/MM/YYYY [15] | Data do treino avaliado [15]. | Proibido Vazio (NOT NULL) [15] | Derivado / Arquitetural [15] | DB_CALENDARIO.data_evento [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-002** | tipo_sistema | Enum | DEFESA, ATAQUE [15, 18] | Fase de jogo do sistema tático [15, 18]. | Proibido Vazio (NOT NULL) [15] | Derivado / Taxonomia [15] | DB_SISTEMAS_POSICOES.tipo_sistema [15, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-003** | sistema | Enum | 3:0, 2:1 [15, 18] | Sistema tático de jogo [15, 18]. | Proibido Vazio (NOT NULL) [15] | Derivado / Taxonomia [15] | DB_SISTEMAS_POSICOES.sistema [15, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-004** | slot_tatico | Texto | Rótulos de slots (ex.: BASE, SOLTA, COBERTURA, CENTRAL, PIVÔ, LATERAL ESQUERDA) [15, 18] | Posição ou papel específico dentro do sistema [15, 18]. | Proibido Vazio (NOT NULL) [15] | Derivado / Taxonomia [15] | DB_SISTEMAS_POSICOES.slot_tatico [15, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-005** | quantidade_requerida | Inteiro | Número inteiro (geralmente 1) [15, 18] | Quantidade mínima de atletas necessárias para o slot [15, 18]. | Proibido Vazio (NOT NULL) [15] | Derivado / Requisito [15] | DB_SISTEMAS_POSICOES.quantidade_requerida [15, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-006** | atletas_disponiveis_qtd | Inteiro | Número inteiro >= 0 [15] | Contagem de atletas habilitadas na posição com disponibilidade SIM na data [15]. | Default = 0 [15] | Derivado / Métrica [15] | Cálculo Automático (Count) [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-007** | atletas_disponiveis_nomes | Texto | Nomes separados por vírgula (ex.: "Aline Mello, Carolina Peixinho") [15] | Lista textual de exibição dos nomes das atletas disponíveis [15]. | Permitido Vazio se quantidade = 0 [15] | Derivado / Rótulo [15] | Script de Derivação Tática [3, 15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-DXP-008** | status_cobertura | Enum | COBERTO, INSUFICIENTE [15] | Avaliação se o slot atingiu a quantidade requerida [15]. | Proibido Vazio (NOT NULL) [15] | Derivado / Diagnóstico [15] | Cálculo Automático (IF qtd >= requerida) [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3. Competições, Convocações, Jogos e Participação Real por Partida.

Este bloco conecta a regulamentação oficial das federações e confederações (CBHb, FHERJ e IHF) com o registro estatístico do clube. Para garantir rigor metodológico e histórico pelos próximos 10+ anos, aplicam-se três princípios arquiteturais fundamentais [1, 2]:

1.  **Separação de Estados e Entidades:** Competição é uma entidade distinta de Jogo; realização de evento é separada de participação da equipe (status_competicao vs. status_participacao_cepraea) [1, 2].
2.  **Hierarquia de Elegibilidade (18/20 → 12 → 10 Atletas):**
    -   **Lista Larga (*Long List*):** Até 18 atletas (ou 20 na Fase Final) inscritas no campeonato [3].
    -   **Convocação/Relação Nominal da Etapa:** Exatamente 12 atletas enviadas na relação oficial da etapa [4].
    -   **Súmula de Partida Individual:** No máximo 10 atletas uniformizadas por jogo [4]. *(Exceção: se houver atleta desqualificada com relatório no jogo anterior, a equipe joga com 9 no jogo seguinte [4]).*
3.  **Regra de Materialização de Participação (TWO_EXCLUDED_OF_TWELVE):** A convocação nominal de 12 atletas comprova apenas o chamamento para a etapa, não a entrada em quadra [1, 5, 6]. Para materializar a participação factual por jogo (DB_PARTICIPACAO_JOGO), o treinador informa explicitamente as 2 atletas que ficaram de fora da súmula daquela partida; as outras 10 são registradas deterministicamente com o status JOGOU [1].

## 3.1. Tabela Título: DB_COMPETICOES (Cadastro Canônico de Campeonatos e Etapas)

-   **Descrição Semântica:** Cadastro mestre dos campeonatos, circuitos e etapas disputados ou monitorados pelo clube.
-   **Unidade de Análise:** 1 Linha = 1 Competição / Etapa.
-   **Chave Primária (PK):** competicao_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-001** | competicao_id | Texto (PK) | Formato estrito COMP-YYYY-XXX (ex.: COMP-2026-001 a COMP-2026-012) | Identificador único e imutável da competição/etapa [1, 7]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Cadastro de Competições [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-002** | nome_competicao | Texto | Texto livre normalizado (ex.: "Circuito Estadual de Handebol de Praia 2026 - 4ª Etapa") | Nome oficial do torneio conforme boletim ou regulamento [7-9]. | Proibido Vazio (NOT NULL) | Observável / Cadastro | Regulamentos e Boletins CBHb/FHERJ [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-003** | organizador | Enum | CBHb, FHERJ, IHF, OUTRO | Entidade responsável pela realização do evento [8, 9]. | Proibido Vazio (NOT NULL) | Observável / Organização | Regulamento do Evento [8, 9] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-004** | periodo_datas | Texto / Data | Formato DD/MM/YYYY ou intervalo DD-DD/MM/YYYY | Período civil de realização do evento [7]. | Proibido Vazio (NOT NULL) | Observável / Agenda | Tabela Oficial do Torneio [7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-005** | sede_local | Texto | Cidade e Estado (ex.: "Niterói - RJ", "São Miguel do Iguaçu - PR") | Cidade/Sede da competição [7]. | Proibido Vazio (NOT NULL) | Observável / Logística | Boletim da Sede [7, 10] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-006** | status | Enum | PREVISTA, REALIZADA, CANCELADA | Estado canônico de realização do evento esportivo no calendário [1, 7]. | Default = PREVISTA | Observável / Ciclo do Evento | Boletins e Confirmação da Organização [1, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-007** | status_participacao_cepraea | Enum | PARTICIPOU, PARTICIPARA, NAO_PARTICIPOU, NAO_PARTICIPARA, CONVIDADO, CLASSIFICADO, A_CONFIRMAR | Relação operacional específica do CEPRAEA com a competição (business_rule_competicoes_visiveis) [1, 7]. | Default = A_CONFIRMAR | Observável / Decisão do Clube | Confirmação da Comissão Técnica (DB_CONFIG) [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-008** | prazo_inscricao | Data / Texto | Formato DD/MM ou Vazio | Data limite para pagamento de taxa e inscrição do clube [7, 11]. | Permitido Vazio | Observável / Regulamento | Ofício da Competição [4, 11] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CMP-009** | prazo_relacao_nominal | Data / Texto | Formato DD/MM ou Vazio | Data limite para envio da lista de 12 atletas e comissão [4, 7, 11, 12]. | Permitido Vazio | Observável / Regulamento | Regulamento Geral (72h FHERJ / 7d CBHb) [4, 12] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.2. Tabela Título: DB_CONVOCACOES (Relações Nominais por Etapa)

-   **Descrição Semântica:** Registro das convocações de etapa enviadas às federações/confederações. Define os limites regulamentares da relação nominal.
-   **Unidade de Análise:** 1 Linha = 1 Convocação de Etapa do CEPRAEA.
-   **Chave Primária (PK):** convocacao_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-001** | convocacao_id | Texto (PK) | Formato estrito CONV-YYYY-XXX (ex.: CONV-2026-001 a CONV-2026-009) | Chave primária única da convocação da etapa [13]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Convocações [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-002** | competicao_id | Texto (FK) | Chave válida de DB_COMPETICOES.competicao_id | Competição à qual a convocação está vinculada [13]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_COMPETICOES.competicao_id [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-003** | data_evento | Data | Formato YYYY-MM-DD | Data de realização da etapa [13]. | Proibido Vazio (NOT NULL) | Observável / Agenda | Tabela do Evento [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-004** | prazo_envio_convocacao | Data | Formato YYYY-MM-DD ou Vazio | Data limite operacional informada para submissão [13]. | Permitido Vazio | Observável / Regulamento | Regulamento FHERJ/CBHb [4, 12, 13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-005** | status_convocacao | Enum | AGUARDANDO_PRAZO, ENVIADA, PRAZO_VENCIDO, NAO_DOCUMENTADA_NA_BASE | Status do trâmite do documento. Antes do prazo é AGUARDANDO_PRAZO [1, 13]. | Default = AGUARDANDO_PRAZO | Observável / Governança | Decisão e Protocolo de Envio [1, 13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-006** | atletas_convocadas_max | Inteiro | Número inteiro (padrão = 12) | Teto máximo de atletas inscritas na relação nominal da etapa [4, 13]. | Default = 12 | Observável / Regulamento | Regulamento CBHb/FHERJ [4] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-007** | atletas_por_partida_max | Inteiro | Número inteiro (padrão = 10) | Teto máximo de atletas uniformizadas em súmula por jogo [4, 13]. | Default = 10 | Observável / Regulamento | Regra 4 IHF / Regulamento CBHb [4, 14] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNV-008** | relacao_nominal_drive_file_id | Texto | ID da planilha/documento no Google Drive | Link/ID do arquivo PDF/Doc oficial enviado à federação [13]. | Permitido Vazio se não documentada | Observável / Proveniência | Protocolo do Google Drive [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.3. Tabela Título: DB_CONVOCACAO_ATLETAS (Matriz Atletas × Convocação)

-   **Descrição Semântica:** Tabela relacional N:M que detalha quais atletas compõem a lista nominal de 12 convocadas para cada etapa.
-   **Unidade de Análise:** 1 Linha = 1 Atleta Convocada para 1 Etapa.
-   **Chave Primária (PK):** convocacao_atleta_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNA-001** | convocacao_atleta_id | Texto (PK) | Formato estrito CA-YYYY-XXX (ex.: CA-2026-001 a CA-2026-084) | Chave única do registro de convocação individual [15]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Convocações [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNA-002** | convocacao_id | Texto (FK) | Chave válida de DB_CONVOCACOES | Convocação de etapa correspondente [15]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_CONVOCACOES.convocacao_id [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNA-003** | athlete_id | Texto (FK) | Chave válida em DB_ATLETAS (ATH-XXXX) | Identificador estável e imutável da atleta convocada [15]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_ATLETAS.athlete_id [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNA-004** | nome_exibicao | Texto | Rótulo vindo de DB_ATLETAS | Nome da atleta para exibição visual [15]. | Proibido Vazio (NOT NULL) | Derivado / Rótulo | DB_ATLETAS.nome_exibicao [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNA-005** | status_convocacao | Enum | convocada, suplente, desconvocada | Situação da atleta na lista nominal da etapa [15]. | Default = convocada | Observável / Decisão Técnica | Comissão Técnica [15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNA-006** | status_participacao | Enum | convocada_etapa | Estado indicativo de convocação para a etapa (reforça que convocação não equivale a jogo) [6, 15]. | Default = convocada_etapa | Observável / Mapeamento | Regra de Negócio DEC-DATA-045 [1, 15] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNA-007** | camisa | Texto / Inteiro | Número da camisa na etapa (ex.: 19, 85) | Número do uniforme registrado na súmula da etapa [15]. | Permitido Vazio | Observável / Cadastro | Relação Nominal Oficial da Etapa [4, 15] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.4. Tabela Título: DB_JOGOS (Súmula, Placar e Fatos de Partidas)

-   **Descrição Semântica:** Tabela canônica de partidas disputadas pelo CEPRAEA. Registra placares por set e shoot-out, derivando deterministicamente o resultado final sem overrides manuais.
-   **Unidade de Análise:** 1 Linha = 1 Partida do CEPRAEA.
-   **Chave Primária (PK):** jogo_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-001** | jogo_id | Texto (PK) | Formato estrito JOGO-YYYY-XXX (ex.: JOGO-2026-001 a JOGO-2026-034) | Identificador canônico da partida [1, 7, 13]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Tabela de Jogos [1, 13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-002** | competicao_id | Texto (FK) | Chave válida em DB_COMPETICOES | Competição à qual a partida pertence [1, 7]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_COMPETICOES.competicao_id [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-003** | data_jogo | Data | Formato DD/MM/YYYY ou YYYY-MM-DD | Data real de realização da partida [7]. | Proibido Vazio (NOT NULL) | Observável / Agenda | Súmula / Boletim Oficial [7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-004** | fase_jogo | Enum | GRUPO, QUARTAS, SEMIFINAL, FINAL, DISPUTA_3_LUGAR, OUTRO | Fase do torneio em que a partida ocorreu [7]. | Proibido Vazio (NOT NULL) | Observável / Estrutura | Tabela da Competição [7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-005** | equipe_a | Texto | Nome oficial da Equipe A em súmula | Nome da equipe figurando no Lado A do placar [1]. | Proibido Vazio (NOT NULL) | Observável / Súmula | Súmula Oficial [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-006** | equipe_b | Texto | Nome oficial da Equipe B em súmula | Nome da equipe figurando no Lado B do placar [1]. | Proibido Vazio (NOT NULL) | Observável / Súmula | Súmula Oficial [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-007** | cepraea_lado | Enum | EQUIPE_A, EQUIPE_B | Posição nominal do CEPRAEA na súmula da partida [1]. | Proibido Vazio (NOT NULL) | Derivado / Identificação | Mapeamento Automático [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-008** | set1_cepraea | Inteiro | Número inteiro >= 0 ou Vazio | Pontos marcados pelo CEPRAEA no Set 1 (game_result_input_fields) [1]. | Permitido Vazio se não realizado | Observável / Placar | Súmula Oficial do Jogo [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-009** | set1_adversario | Inteiro | Número inteiro >= 0 ou Vazio | Pontos marcados pelo adversário no Set 1 [1]. | Permitido Vazio se não realizado | Observável / Placar | Súmula Oficial do Jogo [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-010** | set2_cepraea | Inteiro | Número inteiro >= 0 ou Vazio | Pontos marcados pelo CEPRAEA no Set 2 [1]. | Permitido Vazio se não realizado | Observável / Placar | Súmula Oficial do Jogo [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-011** | set2_adversario | Inteiro | Número inteiro >= 0 ou Vazio | Pontos marcados pelo adversário no Set 2 [1]. | Permitido Vazio se não realizado | Observável / Placar | Súmula Oficial do Jogo [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-012** | shootout_cepraea | Inteiro | Número inteiro >= 0 ou Vazio | Pontos marcados pelo CEPRAEA no Shoot-out (desempate) [1]. | Permitido Vazio se não houver SO | Observável / Placar | Súmula Oficial do Jogo [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-013** | shootout_adversario | Inteiro | Número inteiro >= 0 ou Vazio | Pontos marcados pelo adversário no Shoot-out [1]. | Permitido Vazio se não houver SO | Observável / Placar | Súmula Oficial do Jogo [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-014** | sets_cepraea | Inteiro | 0, 1 ou 2 | Total de sets vencidos pelo CEPRAEA (Derivado por fórmula) [1]. | Derivado automaticamente | Derivado / Resultado | Cálculo Automático (game_result_derived_fields) [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-015** | sets_adversario | Inteiro | 0, 1 ou 2 | Total de sets vencidos pelo adversário (Derivado por fórmula) [1]. | Derivado automaticamente | Derivado / Resultado | Cálculo Automático (game_result_derived_fields) [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-016** | vitoria_cepraea | Boolean / Enum | SIM, NAO | Flag indicativo de vitória do CEPRAEA no jogo [1, 16]. | Proibido Vazio em jogo realizado | Derivado / Resultado | Formulação Automática (IF sets_cepraea > sets_adv) [1, 16] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-017** | resultado_texto | Texto | Ex.: "CEPRAEA 2 x 0 ADM Maricá" | Descrição resumida do resultado e confronto [1]. | Derivado automaticamente | Derivado / Rótulo | Concatenação Automática [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-JOG-018** | status | Enum | PLANEJADO, REALIZADO, CANCELADO, INVALIDADO | Estado da partida. REALIZADO exige evidência factual e homologação humana [1]. | Default = PLANEJADO | Observável / Governança | Homologação Humana (game_status_policy) [1] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.5. Tabela Título: DB_PARTICIPACAO_JOGO (Atuação Factual por Partida)

-   **Descrição Semântica:** Registro da participação efetiva de cada atleta em cada partida individual. Alimenta o cálculo real de jogos disputados e scout.
-   **Unidade de Análise:** 1 Linha = Atuação Factual de 1 Atleta em 1 Jogo.
-   **Chave Primária (PK):** participacao_jogo_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-001** | participacao_jogo_id | Texto (PK) | Formato estrito PJ-XXX-001 (ex.: PJ-3ET-001 a PJ-3ET-048) | Chave primária única da participação da atleta no jogo [17]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Registro de Jogos [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-002** | jogo_id | Texto (FK) | Chave válida em DB_JOGOS | Identificador da partida correspondente [17]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_JOGOS.jogo_id [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-003** | competicao_id | Texto (FK) | Chave válida em DB_COMPETICOES | Identificador da competição vinculada [17]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_COMPETICOES.competicao_id [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-004** | convocacao_id | Texto (FK) | Chave válida em DB_CONVOCACOES | Convocação da etapa que originou a elegibilidade [17]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_CONVOCACOES.convocacao_id [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-005** | athlete_id | Texto (FK) | Chave válida em DB_ATLETAS (ATH-XXXX) | Identificador estável da atleta [17]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_ATLETAS.athlete_id [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-006** | nome_exibicao | Texto | Rótulo vindo de DB_ATLETAS | Nome da atleta para leitura analítica [17]. | Proibido Vazio (NOT NULL) | Derivado / Rótulo | DB_ATLETAS.nome_exibicao [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-007** | status_participacao | Enum | JOGOU, NAO_JOGOU | Fato de ter composto a súmula oficial de 10 atletas no jogo [1, 17]. | Proibido Vazio (NOT NULL) | Observável / Fato Esportivo | Informação do Treinador / Súmula (TWO_EXCLUDED_OF_TWELVE) [1, 17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-008** | entrou_em_quadra | Enum | SIM, NAO | Sinaliza se a atleta efetivamente pisou em quadra durante a partida [17]. | Permitido Vazio se indeterminado | Observável / Scout | Súmula / Vídeo da Partida [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-009** | funcao_no_jogo | Enum | ATAQUE, DEFESA, GOLEIRA, INDEFINIDA | Função primária exercida pela atleta naquela partida específica [17]. | Default = INDEFINIDA | Observável / Scout | Leitura Técnica do Jogo [17] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PJG-010** | regra_contagem | Texto | Ex.: jogo_real se status=JOGOU | Regra de validação de contagem para o indicador jogos_total do elenco [17, 18]. | Proibido Vazio (NOT NULL) | Derivado / Regra de Negócio | Contrato de Dados (DB_CONFIG) [1, 17] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.6. Tabela Título: DB_INDICADORES_ATLETA (Consolidado do Elenco)

-   **Descrição Semântica:** Tabela agregada que consolida a assiduidade, convocações, partidas jogadas e disponibilidades declaradas por atleta.
-   **Unidade de Análise:** 1 Linha = Sumário Consolidado de 1 Atleta.
-   **Chave Primária (PK / FK):** athlete_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-001** | athlete_id | Texto (PK/FK) | Chave válida de DB_ATLETAS | Identificador único da atleta [18]. | Proibido Vazio (NOT NULL) | Derivado / Arquitetural | DB_ATLETAS.athlete_id [18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-002** | convocacoes_total | Inteiro | Número inteiro >= 0 | Total de convocações oficiais em que a atleta constou na relação nominal de 12 [18]. | Default = 0 | Derivado / Métrica | Contagem em DB_CONVOCACAO_ATLETAS [15, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-003** | jogos_total | Inteiro | Número inteiro >= 0 | Total de partidas reais em que a atleta participou (status_participacao = JOGOU) [18]. | Default = 0 | Derivado / Métrica | Contagem em DB_PARTICIPACAO_JOGO [17, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-004** | presencas_fatuais_total | Inteiro | Número inteiro >= 0 | Total de treinos com presença factual confirmada pelo treinador em DB_PRESENCA [1, 18]. | Default = 0 | Derivado / Métrica | Contagem em DB_PRESENCA [1, 18, 19] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-005** | disponibilidades_sim_total | Inteiro | Número inteiro >= 0 | Total de respostas SIM registradas em DB_DISPONIBILIDADE_DECLARADA [18]. | Default = 0 | Derivado / Métrica | Contagem em DB_DISPONIBILIDADE_DECLARADA [1, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-006** | indisponibilidades_nao_total | Inteiro | Número inteiro >= 0 | Total de respostas NAO registradas em DB_DISPONIBILIDADE_DECLARADA [18]. | Default = 0 | Derivado / Métrica | Contagem em DB_DISPONIBILIDADE_DECLARADA [1, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-007** | declaracoes_sem_resposta_total | Inteiro | Número inteiro >= 0 | Total de eventos com célula mapeada em branco (SEM_RESPOSTA) [1, 18]. | Default = 0 | Derivado / Métrica | Contagem em DB_DISPONIBILIDADE_DECLARADA [1, 18] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-IND-008** | updated_at | Timestamp | Formato ISO 8601 com fuso | Carimbo de data/hora do último cálculo do consolidado [18]. | Proibido Vazio (NOT NULL) | Derivado / Auditoria | Sistema / Banco de Dados [18] |
| --- | --- | --- | --- | --- | --- | --- | --- |

O **BLOCO 3** está detalhado em conformidade com as fontes do caderno e os regulamentos oficiais.

📌 **Podemos avançar para o BLOCO 4 (Sistema de Scout Observacional, Eventos Táticos e Proveniência Metodológica), detalhando o modelo de posses (BOU), finalizações, ações de goleira e os níveis epistemológicos de evidência (P0–P3 / A1–A4)?**

## 4. Sistema de Scout Observacional, Eventos Táticos e Proveniência Metodológica.

Para garantir que as análises de vídeo e estatísticas do CEPRAEA mantenham rigor científico e auditabilidade ao longo de 10+ anos, o modelo de scout baseia-se nas recomendações da **Metodologia Observacional (MO)** aplicadas ao handebol de praia [1-3].

### 1. Matriz de Proveniência Metodológica (P0–P3 / A1–A4 / D1)

A rastreabilidade do dado exige a separação estrita entre o que foi **efetivamente observado no vídeo**, o que foi **calculado** e o que constitui **hipótese ou interpretação tática** [444–447]:

 ┌──────────────────────────────────────────────────────────────────────────┐

│ CADEIA DE PROVENIÊNCIA DOS DADOS DE SCOUT │

├───────┬──────────────────────────┬───────────────────────────────────────┤

│ NIVEL │ NOME DA CAMADA │ DESCRIÇÃO DA FONTE / TRANSFORMAÇÃO │

├───────┼──────────────────────────┼───────────────────────────────────────┤

│ P0 │ Fonte Primária │ Vídeo original da partida (reprodução)│

│ P1 │ Evidência Codificada │ Dados observados no vídeo com timecode│

│ P2 │ Evidência Visual Derivada│ Frames estáticos / screenshots │

│ P3 │ Evidência Descritiva │ Anotações e registros textuais humanos│

├───────┼──────────────────────────┼───────────────────────────────────────┤

│ A1 │ Resultado Analítico │ Contagens, frequências e proporções │

│ A2 │ Padrão Candidato │ Recorrência detectada em amostras │

│ A3 │ Interpretação Tática │ Significado tático atribuído ao padrão│

│ A4 │ Hipótese Explicativa │ Mecanismo causal provável inferido │

├───────┼──────────────────────────┼───────────────────────────────────────┤

│ D1 │ Recomendação Operacional │ Orientação para treino ou plano de jogo│

└───────┴──────────────────────────┴───────────────────────────────────────┘



-   **Invariante de Proveniência:** Uma hipótese (A4) ou interpretação (A3) jamais pode retroceder para alterar um dado observado (P1) [4].

### 2. Hierarquia Operacional de Observação e a BOU

Em vez de reduzir o jogo a uma planilha plana, o scout adota a estrutura hierárquica sugerida pela literatura científica de handebol de praia [471–472]:

$$text{JOGO} rightarrow text{SET} rightarrow text{POSSE} rightarrow text{FASE} rightarrow text{BOU} rightarrow text{PROCEDIMENTO TÁTICO} rightarrow text{FINALIZAÇÃO} rightarrow text{GOLEIRA} rightarrow text{DESFECHO}$$

$$text{JOGO} longrightarrow text{SET} longrightarrow text{POSSE} longrightarrow text{FASE} longrightarrow text{BOU} longrightarrow text{PROCEDIMENTO Tacute{A}TICO} longrightarrow text{FINALIZAÇtilde{A}O} longrightarrow text{GOLEIRA} longrightarrow text{DESFECHO}$$

-   **BOU (*Basic Attack Unit* / Unidade Básica de Ataque):** Definida operacionalmente como o intervalo de tempo desde o momento em que as atacantes se posicionam nos postos específicos do ataque posicionado até ocorrer uma interrupção ou mudança de posse [5-7].
-   **Posse vs. BOU:** Uma posse de bola pode conter 0 BOU (se resolvida em transição rápida) ou 1+ BOUs (se houver reorganização posicional sem perda da posse) [7, 8].

## 3.1. Tabela Título: DB_POSSES (Unidade Canônica de Posse de Bola)

-   **Descrição Semântica:** Registro do controle funcional ou legal da bola por uma equipe, desde a aquisição até o encerramento da posse [9, 10].
-   **Unidade de Análise:** 1 Linha = 1 Posse de Bola.
-   **Chave Primária (PK):** posse_id (ex.: J001_S1_P001).

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-001** | posse_id | Texto (PK) | Formato Jxxx_Sx_Pxxx | Chave primária imutável da posse. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Scout |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-002** | jogo_id | Texto (FK) | Chave válida de DB_JOGOS | Partida à qual a posse pertence. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_JOGOS.jogo_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-003** | equipe_posse | Enum | CEPRAEA, ADVERSARIO | Equipe com controle funcional ou direito de posse. | Proibido Vazio (NOT NULL) | Observável / Campo | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-004** | origem_posse | Enum | REFEREE_THROW_CONTROL, THROW_IN_RESTART, GOALKEEPER_THROW_RESTART, FREE_THROW_RESTART, SIX_M_RESTART, LIVE_BALL_CONTROL_CHANGE, OTHER_RESTART, INDETERMINADO | Mecanismo de início da posse de acordo com a regra COD-027 [695, 783–785]. | Default = INDETERMINADO | Observável / Fato | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-005** | timestamp_inicio | Texto / Timecode | Formato MM:SS.mmm | Timecode do primeiro controle ou direito à bola (VAR-004) [11]. | Permitido Vazio se cortado | Observável / Timecode | Vídeo P0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-006** | timestamp_fim | Texto / Timecode | Formato MM:SS.mmm | Timecode do evento terminal da posse (VAR-005) [12]. | Permitido Vazio se cortado | Observável / Timecode | Vídeo P0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-007** | causa_fim_posse | Enum | FIM_GOL, FIM_DEFESA_GK_POSSE_ADV, FIM_FORA, FIM_POSTE_SEM_RECUP, FIM_BLOQUEIO_POSSE_ADV, FIM_ERRO_PASSE_RECEP, FIM_INTERCEPTACAO, FIM_ERRO_REG, FIM_FALTA_OF, FIM_PASSIVO, FIM_OUTRO, FIM_IND | Evento que encerrou a posse (VAR-021 / COD-030) [13, 14]. | Default = FIM_IND | Observável / Fato | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-PSS-008** | pontos_posse | Inteiro | 0, 1, 2 ou 4 | Total de pontos produzidos na posse [10, 15]. | Default = 0 | Derivado / Súmula | Soma de DB_FINALIZACOES |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.2. Tabela Título: DB_BOU (Unidade Básica de Ataque Posicionado)

-   **Descrição Semântica:** Unidade de análise do ataque posicional estruturado, mapeando a composição, o especialista e o confronto tático [476–477, 654–655].
-   **Unidade de Análise:** 1 Linha = 1 BOU.
-   **Chave Primária (PK):** bou_id (ex.: J001_S1_P001_B01).

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-BOU-001** | bou_id | Texto (PK) | Formato Jxxx_Sx_Pxxx_Bxx | Chave primária única da BOU. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Scout |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-BOU-002** | posse_id | Texto (FK) | Chave válida de DB_POSSES | Posse à qual a BOU pertence. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_POSSES.posse_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-BOU-003** | estrutura_ofensiva | Enum | OF_31, OF_22, OF_40, OF_30, OF_21, OF_OUT, OF_IND | Estrutura tática de ataque na BOU (TAX-002) [16, 17]. | Default = OF_IND | Observável / Tática | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-BOU-004** | especialista_id | Texto (FK) | Chave de DB_ATLETAS, ESP_NENHUM ou ESP_IND | Atleta exercendo a função tática de especialista (VAR-010) [18]. | Default = ESP_IND | Observável / Identificação | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-BOU-005** | posto_especialista | Enum | POST_AI, POST_LI, POST_C, POST_LD, POST_AD, POST_PIV, POST_OUT, POST_IND, NAO_APLICAVEL | Posto funcional do especialista na quadra (VAR-011) [19]. | Default = POST_IND | Observável / Posicionamento | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-BOU-006** | estrutura_defensiva_inicial | Enum | DEF_30, DEF_21C, DEF_21E, DEF_21D, DEF_12EC, DEF_12DC, DEF_12ED, DEF_03, DEF_MTM, DEF_VP, DEF_OUT, DEF_IND | Formação defensiva adversária no início da BOU (TAX-005) [20, 21]. | Default = DEF_IND | Observável / Defesa | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-BOU-007** | estrutura_defensiva_final | Enum | Mesmos valores de estrutura_defensiva_inicial | Formação defensiva no momento da finalização (VAR-016) [22]. | Default = DEF_IND | Observável / Defesa | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.3. Tabela Título: DB_EVENTOS_TACTICOS (Procedimentos de Ataque)

-   **Descrição Semântica:** Registro cronológico dos procedimentos técnico-táticos coletivos executados dentro de uma BOU [477, 492–495, 790–794].
-   **Unidade de Análise:** 1 Linha = 1 Procedimento Tático.
-   **Chave Primária (PK):** evento_tatico_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EVT-001** | evento_tatico_id | Texto (PK) | Formato EVT-YYYY-XXX | Chave única do evento tático. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Scout |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EVT-002** | bou_id | Texto (FK) | Chave válida de DB_BOU | BOU em que o meio tático ocorreu. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_BOU.bou_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EVT-003** | ordem_evento | Inteiro | Número inteiro >= 1 | Sequência cronológica do procedimento na BOU (VAR-013) [23]. | Proibido Vazio (NOT NULL) | Observável / Cronologia | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EVT-004** | procedimento_tatico | Enum | PT_PISTON, PT_PIV_FIXO, PT_360_CONT, PT_FLY_CONT, PT_BLOQUEIO, PT_CORTE, PT_CRUZ_BOLA, PT_SCREEN, PT_PASSA_VAI, PT_CRUZ_SEM, PT_TRANSF, PT_SALTO_CONT, PT_OUTRO, PT_NENHUM, PT_IND | Meio tático coletivo observado (TAX-003 / COD-028) [492, 661, 791–794]. | Default = PT_IND | Observável / Meio Tático | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EVT-005** | atleta_executora_id | Texto (FK) | Chave de DB_ATLETAS ou ATLETA_IND | Atleta principal executora do procedimento. | Default = ATLETA_IND | Observável / Sujeito | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EVT-006** | atleta_receptora_id | Texto (FK) | Chave de DB_ATLETAS, NAO_APLICAVEL ou ATLETA_IND | Atleta beneficiada ou receptora do passe na combinação. | Permitido Vazio / NAO_APLICAVEL | Observável / Sujeito | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.4. Tabela Título: DB_FINALIZACOES (Eventos de Arremesso ao Gol)

-   **Descrição Semântica:** Registro das tentativas de arremesso. Conforme a norma **DEC-015**, a zona de origem e a zona de alvo/destino são tratadas como dimensões espaciais estritamente independentes [665–667, 737–739, 892–893].
-   **Unidade de Análise:** 1 Linha = 1 Arremesso.
-   **Chave Primária (PK):** finalizacao_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-001** | finalizacao_id | Texto (PK) | Formato FIN-YYYY-XXX | Chave primária do arremesso. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Scout |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-002** | bou_id | Texto (FK) | Chave válida em DB_BOU ou Vazio | BOU associada (Vazio se finalização em transição TO) [24]. | Permitido Vazio se em TO | Observável / Arquitetural | DB_BOU.bou_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-003** | atleta_finalizadora_id | Texto (FK) | Chave de DB_ATLETAS ou ATLETA_IND | Atleta que executou o arremesso (VAR-036) [25]. | Default = ATLETA_IND | Observável / Sujeito | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-004** | zona_origem_finalizacao | Enum | ZE (Esquerda), ZCE (Centro-Esquerda), ZCD (Centro-Direita), ZD (Direita), ZIND | Faixa lateral de origem do apoio/decolagem (TAX-006 / DEC-015) [26, 27]. | Default = ZIND | Observável / Espaço | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-005** | zona_alvo_arremesso | Enum | ALVO_AE, ALVO_AC, ALVO_AD, ALVO_BE, ALVO_BC, ALVO_BD, ALVO_FORA, ALVO_IND | Setor de destino/alvo na baliza (TAX-011 / VAR-031) [28, 29]. | Default = ALVO_IND | Observável / Espaço | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-006** | tipo_finalizacao | Enum | FIN_COMUM, FIN_360, FIN_FLY, FIN_6M, FIN_OUT, FIN_IND | Categoria técnica da finalização (TAX-007 / VAR-018) [30, 31]. | Default = FIN_IND | Observável / Técnica | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-007** | resultado_finalizacao | Enum | GOL, DEFESA_GK, POSTE_TRAVE, FORA, BLOQUEIO, OUTRO, IND | Desfecho primário do arremesso (TAX-008 / VAR-019) [30, 32]. | Default = IND | Observável / Desfecho | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-FIN-008** | pontos_atribuidos | Inteiro | 0, 1, 2 | Pontuação regulamentar validada (VAR-020 / REG-002) [15, 33]. | Proibido Vazio (NOT NULL) | Observável / Regulamento | Súmula Oficial / Regra IHF |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.5. Tabela Título: DB_GOLEIRA_ACOES (Submódulo Goleira × Finalização)

-   **Descrição Semântica:** Submódulo relacional para análise detalhada do comportamento da goleira durante a tentativa de arremesso [478, 672, 725–728].
-   **Unidade de Análise:** 1 Linha = 1 Intervenção da Goleira.
-   **Chave Primária (PK):** goleira_acao_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-GK-001** | goleira_acao_id | Texto (PK) | Formato GK-YYYY-XXX | Chave única da ação da goleira. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Scout |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-GK-002** | finalizacao_id | Texto (FK) | Chave válida de DB_FINALIZACOES | Arremesso enfrentado pela goleira. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | DB_FINALIZACOES.finalizacao_id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-GK-003** | goleira_id | Texto (FK) | Chave de DB_ATLETAS, GK_SEM ou GK_IND | Identificador da goleira em quadra (VAR-037) [34]. | Default = GK_IND | Observável / Sujeito | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-GK-004** | acao_goleiro | Enum | GK_ALTA, GK_MEDIA, GK_BAIXA, GK_ESPAGAT, GK_OUTRA, GK_IND | Postura/ação corporal defensiva da goleira (TAX-010 / DEC-013) [35-37]. | Default = GK_IND | Observável / Técnica | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-GK-005** | profundidade_acao | Enum | PROF_SIM, PROF_NAO, PROF_IND | Sinaliza avanço corporal frontal da goleira (VAR-023) [38, 39]. | Default = PROF_IND | Observável / Posicionamento | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-GK-006** | acao_posterior | Enum | LANÇAMENTO_DIRETO, CONTRA_ATAQUE, PASSE_POSICIONAL, OUTRO, IND | Primeira ação de distribuição da goleira pós-defesa/gol [40, 41]. | Permitido Vazio | Observável / Transição | Codificação do Analista |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 3.6. Tabela Título: DB_SCOUT_CONFIABILIDADE (Auditoria e Fidedignidade do Scout)

-   **Descrição Semântica:** Tabela de controle de qualidade metodológica do dado. Armazena os testes de concordância intra e inter-observador [507–510, 861–863].
-   **Unidade de Análise:** 1 Linha = 1 Sessão de Validação por Variável.
-   **Chave Primária (PK):** validacao_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNF-001** | validacao_id | Texto (PK) | Formato VAL-YYYY-XXX | Chave da sessão de auditoria. | Proibido Vazio (NOT NULL) | Derivado / Arquitetural | Sistema de Controle de Qualidade |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNF-002** | variavel_auditada | Texto | Nome de campo válido (ex.: tipo_finalizacao, estrutura_defensiva) | Campo submetido ao teste de fidedignidade [42]. | Proibido Vazio (NOT NULL) | Derivado / Metadado | Protocolo de Scout |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNF-003** | kappa_cohen_intra | Decimal | Valor entre -1.00 e 1.00 | Índice Kappa de Cohen intra-observador [43, 44]. | Permitido Vazio | Derivado / Estatística | Cálculo via R / Jamovi / Python [45] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNF-004** | kappa_cohen_inter | Decimal | Valor entre -1.00 e 1.00 | Índice Kappa de Cohen inter-observadores [43, 44]. | Permitido Vazio | Derivado / Estatística | Cálculo via R / Jamovi / Python [45] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNF-005** | fleiss_kappa | Decimal | Valor entre -1.00 e 1.00 | Índice Fleiss' Kappa para múltiplos codificadores [43, 44]. | Permitido Vazio | Derivado / Estatística | Cálculo via R / Jamovi / Python [43, 46] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNF-006** | concordancia_bruta_pct | Decimal | Percentual de 0.00% a 100.00% | Percentual de concordância direta entre codificadores [47]. | Proibido Vazio (NOT NULL) | Derivado / Estatística | Cálculo de Concordância [47] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CNF-007** | status_aprovacao | Enum | ACEITO_PRODUCAO (Kappa >= 0.80), REVISAR_DEFINICAO (0.70–0.79), REPROVADO (< 0.60) | Avaliação segundo a regra de governança CON-004 [47, 48]. | Proibido Vazio (NOT NULL) | Derivado / Governança | Painel de Controle de Qualidade |
| --- | --- | --- | --- | --- | --- | --- | --- |

O **BLOCO 4** detalha a arquitetura do scout observacional, garantindo que nenhum julgamento tático seja confundido com dado primário de vídeo.

📌 **Podemos avançar para o BLOCO 5 (Governança do Sistema, Logs *Append-Only*, Auditoria e Camada de Exportação/Frontend), fechando o Dicionário Canônico do CEPRAEA?**

## 5. Governança do Sistema, Logs *Append-Only*, Auditoria e Camada de Exportação/Frontend [1-3].

Este bloco garante que o sistema seja autoauditável, imune à sobrescrita acidental por Inteligências Artificiais ou preenchimentos humanos e perfeitamente integrado à interface visual das atletas e da comissão técnica (*Google Sheets / Apps Script / Frontend*).

### Estrutura de Governança e Regras de Segurança (RLS & *Append-Only*)

1.  **Invariante de Imutabilidade (*Append-Only*):** O histórico de alterações, execuções de scripts e homologações de presenças jamais sobrescreve linhas existentes [4, 5]. Toda atualização é gravada como um novo evento de log em DB_CHANGELOG com carimbo estático de data e hora [1-3].
2.  **Separação entre Banco Canônico (SSOT) e Camada de Exposição:** O frontend acessa o banco exclusivamente por tabelas de exportação dedicadas (DB_EXPORT_FRONTEND e DB_EXPORT_ANALISE_JOGOS) via conexões do tipo IMPORTRANGE [1, 2, 6, 7]. Nenhuma fórmula do frontend edita diretamente o núcleo do banco de dados [1, 8].
3.  **Mecanismo *Fail-Closed* e *SQL Stop Gate*:** Se houver ambiguidade na identificação de uma atleta (athlete_id), de uma competição ou de um evento, o sistema bloqueia qualquer gravação (*Fail-Closed*) para evitar contaminação do histórico [2].
4.  **Política de Preservação de Entrada Humana (PRESERVAR):** A IA ou scripts automatizados não possuem autoridade para alterar decisões, classificações ou presenças homologadas pelo treinador [1, 9].

## 5.1. Tabela Título: DB_CONFIG (Parâmetros Globais e Contrato de Negócio)

-   **Descrição Semântica:** Tabela mestre de parâmetros do sistema, chaves de contrato, diretrizes de fuso horário e registro de homologação das regras de negócio (incluindo RN-DISP-001 a RN-DISP-017 e DEC-DATA-045) [1, 2].
-   **Unidade de Análise:** 1 Linha = 1 Parâmetro Global de Configuração.
-   **Chave Primária (PK):** chave.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CFG-001** | chave | Texto (PK) | Chaves canônicas em snake_case (ex.: timezone, manual_input_policy, sql_stop_gate) [1, 2] | Nome único do parâmetro ou contrato de negócio [1, 2]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Modelagem do Sistema / DB_CONFIG [1, 2] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CFG-002** | valor | Texto | Valores de estado ou configuração (ex.: America/Sao_Paulo, PRESERVAR, FECHADO) [1, 2] | Valor operacional corrente atribuído à chave [1, 2]. | Proibido Vazio (NOT NULL) | Observável / Estado | Decisão do Steward / Modelador [1, 2] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-CFG-003** | observacao | Texto | Texto explicativo ou carimbo de homologação [1, 2] | Rastreabilidade e justificativa da regra registrada [1, 2]. | Permitido Vazio | Observável / Documentação | Histórico de Homologação [1, 2] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5.2. Tabela Título: DB_CHANGELOG / DB_LOGS (Trilha *Append-Only* de Auditoria)

-   **Descrição Semântica:** Registro histórico imutável de todas as modificações de estrutura, atualizações de carga, migrações e execuções de scripts no banco [3].
-   **Unidade de Análise:** 1 Linha = 1 Evento de Alteração/Execução no Banco.
-   **Chave Primária (PK):** id (ex.: DBLOG-0001 a DBLOG-9999) [3].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-001** | id | Texto (PK) | Formato estrito DBLOG-XXXX [3] | Identificador sequencial e único do registro de log [3]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Sistema de Log [3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-002** | timestamp | Timestamp | Formato ISO 8601 com fuso: YYYY-MM-DDTHH:MM:SS-03:00 [1, 3] | Carimbo estático e imutável do momento da execução [1, 3]. | Proibido Vazio (NOT NULL) | Observável / Auditoria | Relógio do Sistema (America/Sao_Paulo) [1, 3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-003** | executor | Texto | Nome do ator ou IA (ex.: "ChatGPT", "Davi Sermenho") [3] | Agente responsável por disparar a alteração [3]. | Proibido Vazio (NOT NULL) | Observável / Auditoria | Autenticação / Registro da Sessão [3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-004** | objetivo | Texto | Resumo curto da meta da alteração [3] | Finalidade do procedimento executado [3]. | Proibido Vazio (NOT NULL) | Observável / Documentação | Solicitante do Comando [3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-005** | abas_alteradas | Texto | Tabelas afetadas separadas por ponto e vírgula [3] | Lista das tabelas do banco modificadas pela ação [3]. | Proibido Vazio (NOT NULL) | Observável / Linhagem | Script de Execução [3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-006** | alteracoes | Texto | Descrição detalhada dos campos/linhas alterados [3] | Detalhamento das modificações físicas ou lógicas aplicadas [3]. | Proibido Vazio (NOT NULL) | Observável / Auditoria | Log da Transação [3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-007** | validacoes | Texto | Resultado do teste de regressão/validação pós-execução [3] | Verificação de integridade realizada após a gravação [3]. | Proibido Vazio (NOT NULL) | Observável / Controle de Qualidade | Script de Regressão [3] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-LOG-008** | status | Enum | executado, executado_validado, executado_com_pendencias, bloqueado [3] | Estado de conclusão do procedimento [3]. | Proibido Vazio (NOT NULL) | Observável / Governança | Módulo de Registro [3] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5.3. Tabela Título: DB_AVISOS (Central de Alertas e Comunicados Internos)

-   **Descrição Semântica:** Tabela para publicação de comunicados oficiais e avisos direcionados às atletas ou à comissão [1, 10].
-   **Unidade de Análise:** 1 Linha = 1 Comunicado Oficial.
-   **Chave Primária (PK):** aviso_id.

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-AVS-001** | aviso_id | Texto (PK) | Formato AVS-YYYY-XXX | Identificador único do comunicado [10]. | Proibido Vazio (NOT NULL) | Observável / Arquitetural | Central de Avisos [10] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-AVS-002** | data_publicacao | Data / Timestamp | Formato ISO ou DD/MM/YYYY | Data de publicação do aviso [10]. | Proibido Vazio (NOT NULL) | Observável / Agenda | Autor do Aviso [10] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-AVS-003** | titulo | Texto | Texto curto descritivo | Assunto central do comunicado [10]. | Proibido Vazio (NOT NULL) | Observável / Rótulo | Autor do Aviso [10] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-AVS-004** | mensagem | Texto | Texto livre com as instruções oficiais | Conteúdo detalhado do comunicado [10]. | Proibido Vazio (NOT NULL) | Observável / Mensagem | Comissão Técnica / Secretaria [10] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-AVS-005** | publico | Enum | TODAS_ATLETAS, GOLEIRAS, DEFESA, ATAQUE, COMISSAO | Escopo do público-alvo da mensagem [10]. | Default = TODAS_ATLETAS | Observável / Destino | Autor do Aviso [10] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-AVS-006** | status | Enum | ATIVO, EXPIRADO, CANCELADO | Estado de visibilidade do aviso nas telas [10]. | Default = ATIVO | Observável / Ciclo de Vida | Controle do Sistema [10] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5.4. Tabela Título: DB_VALIDACAO_REGRESSAO (Bateria Automatizada de Testes de Integridade)

-   **Descrição Semântica:** Tabela dinâmica que executa testes contínuos de integridade matemática, relacional e factual, impedindo a propagação de fórmulas quebradas (#REF!, #VALUE!, #N/A) para o frontend [11].
-   **Unidade de Análise:** 1 Linha = 1 Teste Automatizado de Regressão.
-   **Chave Primária (PK):** teste_id (ou Nome do Teste) [11].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-REG-001** | teste | Texto (PK) | Rótulo do teste (ex.: FRONTEND × ANALÍTICO — JOGOS, QUALIDADE DE DADOS DOS JOGOS) [11] | Descrição da asserção de integridade avaliada [11]. | Proibido Vazio (NOT NULL) | Derivado / Arquitetural | Suite de Testes de Regressão [11] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-REG-002** | esperado | Texto / Número | Valor ou condição teórica esperada (ex.: "Diferença zero", "0", "68%") [11] | Resultado matemático ou lógico esperado da validação [11]. | Proibido Vazio (NOT NULL) | Derivado / Critério | Contrato de Dados (DB_CONFIG) [11] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-REG-003** | atual | Texto / Número | Valor recomputado em tempo real pelo banco [11] | Valor efetivamente calculado na execução atual [11]. | Proibido Vazio (NOT NULL) | Derivado / Medição | Cálculo Automático do Banco [11] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-REG-004** | status | Enum | OK, ALERTA, ERRO [11] | Diagnóstico da validação. ERRO exige bloqueio e correção imediata [11]. | Proibido Vazio (NOT NULL) | Derivado / Diagnóstico | Avaliação do Teste (IF atual == esperado) [11] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-REG-005** | detalhe | Texto | Descrição descritiva do resultado ou divergência encontrada [11] | Detalhamento do impacto em caso de alerta ou erro [11]. | Permitido Vazio | Derivado / Diagnóstico | Log do Teste de Regressão [11] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5.5. Tabela Título: DB_EXPORT_FRONTEND (Visão Canônica para Conexão IMPORTRANGE)

-   **Descrição Semântica:** Tabela desnormalizada em formato chave-valor que atua como interface canônica de saída do database para a planilha/aplicativo das atletas [6, 7].
-   **Unidade de Análise:** 1 Linha = 1 Chave de Exportação.
-   **Chave Primária (PK):** export_key [6, 7].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-001** | export_key | Texto (PK) | Chaves canônicas (ex.: TEAM_TOTAL_ATLETAS, GAMES_TOTAL_VALIDOS, STAGE4_RESULT_LABEL) [6, 7] | Chave estável de leitura utilizada nas fórmulas do frontend [6, 7]. | Proibido Vazio (NOT NULL) | Derivado / Arquitetural | Interface de Exportação [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-002** | categoria | Enum | ELENCO, POSICAO, TREINO, ANALISE_JOGOS, ETAPA_23_08, FINAL_BR, SISTEMA [6, 7] | Módulo funcional do indicador exposto [6, 7]. | Proibido Vazio (NOT NULL) | Derivado / Taxonomia | Categorização de Saída [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-003** | titulo | Texto | Rótulo em linguagem natural para exibição em telas [6, 7] | Nome amigável do indicador para o usuário final [6, 7]. | Proibido Vazio (NOT NULL) | Derivado / Rótulo | Dicionário de Exibição [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-004** | valor_1 | Texto | Valor principal do indicador (ex.: "19", "68%", "🏆 CEPRAEA campeão") [6, 7] | Dado primário exportado para a interface [6, 7]. | Permitido Vazio | Derivado / Métrica | Recomposição de SSOT [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-005** | valor_2 | Texto | Valor complementar ou descrição de detalhamento [6, 7] | Atributo secundário de apoio [6, 7]. | Permitido Vazio | Derivado / Métrica | Recomposição de SSOT [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-006** | status | Enum | ATIVO, INATIVO, TECNICO_INTERNO [6, 7] | Estado de disponibilidade da chave para importação no frontend [6, 7]. | Default = ATIVO | Derivado / Governança | Controle de Exportação [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-007** | updated_at | Timestamp | Formato ISO 8601 com fuso | Carimbo de data/hora do recálculo da exportação [6, 7]. | Proibido Vazio (NOT NULL) | Derivado / Auditoria | DB_CONFIG.last_component_reconciliation [1, 6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPF-008** | origem_db | Texto | Tabela-fonte do banco (ex.: DB_ATLETAS, DB_JOGOS, DB_CALENDARIO) [6, 7] | Rastreabilidade da origem interna do dado exportado [6, 7]. | Proibido Vazio (NOT NULL) | Derivado / Proveniência | Linhagem de Dados [6, 7] |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5.6. Tabela Título: DB_EXPORT_ANALISE_JOGOS (Matriz de Desempenho por Competidor e Elenco)

-   **Descrição Semântica:** Tabela agregada que provê a visão analítica de jogos por competição, por adversário e por atleta para alimentar dashboards completos no desktop e dispositivos móveis [12, 13].
-   **Unidade de Análise:** 1 Linha = 1 Agregação por Competição, Adversário ou Atleta.
-   **Chave Primária (PK Composite):** tipo + item_id [13].

| **var_id** | **nome_campo** | **tipo_dado** | **valores_permitidos / dominio** | **definicao_operacional** | **regra_vazio** | **natureza_epistemica** | **fonte_autorizada** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-001** | tipo | Enum | COMPETICAO, ADVERSARIO, ATLETA, ALERTA [13] | Nível de agregação analítica da linha [13]. | Proibido Vazio (NOT NULL) | Derivado / Arquitetural | Sistema de Análise [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-002** | item_id | Texto | competicao_id, athlete_id ou Nome do Adversário [13] | Identificador canônico do objeto agregado [13]. | Proibido Vazio (NOT NULL) | Derivado / Arquitetural | Recomposição de IDs [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-003** | campo_01 | Texto | Nome da competição, adversário ou atleta [13] | Nome amigável de identificação do item [13]. | Proibido Vazio (NOT NULL) | Derivado / Rótulo | Recomposição do Banco [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-004** | campo_02 | Inteiro / Texto | Total de jogos disputados [13] | Contagem total de partidas no recorte [13]. | Default = 0 | Derivado / Métrica | Contagem em DB_JOGOS / DB_PARTICIPACAO_JOGO [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-005** | campo_03 | Inteiro / Texto | Vitórias do CEPRAEA [13] | Contagem de vitórias na modalidade [13]. | Default = 0 | Derivado / Métrica | Contagem de Vitórias [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-006** | campo_04 | Inteiro / Texto | Derrotas do CEPRAEA [13] | Contagem de derrotas na modalidade [13]. | Default = 0 | Derivado / Métrica | Contagem de Derrotas [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-007** | campo_05 | Texto / Percentual | Taxa de aproveitamento (ex.: "100%", "50%", "—") [13] | Percentual de vitórias sobre os jogos válidos do recorte [13]. | Default = 0% | Derivado / Métrica | Cálculo Automático (V / J) [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-008** | campo_06 | Inteiro / Texto | Sets vencidos / Último resultado em texto [13] | Total de sets pró ou descrição do último confronto [13]. | Permitido Vazio | Derivado / Métrica | Recomposição de Jogos [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-009** | campo_07 | Inteiro / Texto | Sets perdidos / Competição do último confronto [13] | Total de sets contra ou competição de referência [13]. | Permitido Vazio | Derivado / Métrica | Recomposição de Jogos [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VAR-EXPA-010** | campo_10 | Enum / Texto | OK, COM_PENDENCIAS, SEM_JOGO_REAL [13] | Diagnóstico da qualidade dos dados do recorte analítico [13]. | Proibido Vazio (NOT NULL) | Derivado / Governança | Avaliação de Qualidade [13] |
| --- | --- | --- | --- | --- | --- | --- | --- |

**Guia 2: Dicionário de Dados Canônico CEPRAEA**

---

[METADADOS_SISTEMA]

ID_FONTE: DAT-002

TITULO_CANONICO: DAT-002 Modelagem do Banco PostgreSQL Supabase

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Dados

SUBCATEGORIA: Schema Físico e RLS

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Modelagem física de tabelas, relacionamentos, chaves estrangeiras, políticas RLS e funções do banco Supabase

[FIM_METADADOS]

---

Dicionário de Dados Canônico CEPRAEA

# Papel do Documento

Este documento atua como a Fonte Única da Verdade (SSOT) e o vocabulário controlado para o modelo de dados do CEPRAEA. Ele estabelece as especificações arquiteturais, definições de tabelas, regras de integridade referencial, cardinalidades, semântica tática e governança de dados para garantir a durabilidade e a consistência do sistema de informações esportivas por longo prazo.

# Escopo do Documento

O escopo abrange o ciclo de vida completo do dado esportivo no handebol de praia, cobrindo os 5 blocos funcionais do sistema:

-   **Bloco 1 (Cadastro e Atribuição Tática):** Gestão de atletas, funções táticas e posições primárias e secundárias.
-   **Bloco 2 (Operação, Agenda e Presenças):** Calendário de treinos, declaração prospectiva de disponibilidade, homologação de presenças e matriz de cobertura tática.
-   **Bloco 3 (Competição e Desempenho):** Gestão de competições, convocações de etapas, súmulas/participação efetiva de atletas em jogos e consolidação de indicadores.
-   **Bloco 4 (Scout Observacional e Análise de Vídeo):** Estrutura hierárquica de posses, unidades básicas de ataque (BOU), eventos táticos, finalizações e ações de goleira.
-   **Bloco 5 (Governança, Auditoria e Saídas):** Trilhas de auditoria append-only, logs de alteração, parâmetros de configuração, validação das regras oficiais da IHF e exportação de dados.

## Síntese Arquitetural do Dicionário Canônico do CEPRAEA (Blocos 1 ao 5)

Com a entrega do BLOCO 5, o Dicionário de Dados Canônico do CEPRAEA está especificado, cobrindo o ciclo de vida completo do dado esportivo:

| **BLOCO DO SISTEMA** | **FLUXO DE DADOS E RELACIONAMENTOS** |
| --- | --- |
| **BLOCO 1: Cadastro e Atribuição Tática** | DB_ATLETAS ──▶ DB_POSICOES ──▶ DB_POSICOES_SECUNDARIAS   └─▶ DB_ATLETA_POSICOES_TATICAS (Visão Setorial) ──▶ DB_ATLETA_POSICOES_LONG |
| --- | --- |
| **BLOCO 2: Operação, Agenda e Presenças** | DB_CALENDARIO ──▶ DB_TREINOS ──▶ DB_DISPONIBILIDADE_DECLARADA   DB_PRESENCA_PROPOSTA (Wellness Pós-Treino) ──(Aprovação Treinador)──▶ DB_PRESENCA (SSOT) └─▶ DB_DISPONIBILIDADE_POSICAO (Matriz de Cobertura Tática) |
| --- | --- |
| **BLOCO 3: Competição e Desempenho** | DB_COMPETICOES ──▶ DB_CONVOCACOES ──▶ DB_CONVOCACAO_ATLETAS (12 Atletas)   DB_JOGOS (Placar e Sets) ──(Regra TWO_EXCLUDED_OF_TWELVE)──▶ DB_PARTICIPACAO_JOGO (10 Ativas) └─▶ DB_INDICADORES_ATLETA (Consolidado de Elenco) |
| --- | --- |
| **BLOCO 4: Scout Observacional e Análise de Vídeo** | DB_POSSES ──▶ DB_BOU (Unidades Básicas de Ataque) ──▶ DB_EVENTOS_TACTICOS   └─▶ DB_FINALIZAOES ──▶ DB_GOLEIRA_ACOES └─▶ DB_SCOUT_CONFIABILIDADE (Kappa de Cohen / Fleiss' Kappa) |
| --- | --- |
| **BLOCO 5: Governança, Auditoria e Saídas** | DB_CONFIG ──▶ DB_CHANGELOG (Append-Only) ──▶ DB_AVISOS / DB_VALIDACAO_REGRESSAO   DB_EXPORT_FRONTEND ──(IMPORTRANGE / Apps Script)──▶ Frontend Atletas DB_EXPORT_ANALISE_JOGOS ──▶ Dashboards Analíticos |
| --- | --- |

Por que este modelo garante durabilidade para os próximos 10+ anos? Atemporalidade do Dado: Ao ancorar todos os relacionamentos em chaves imutáveis (athlete_id, evento_id, jogo_id, posse_id), o banco aceita alterações de nomes, números de camisa ou patrocinadores sem perder a integridade das séries históricas [1, 2]. Separação Epistemológica: O banco distingue com precisão o que foi declarado (intenção/disponibilidade), o que é fato observado e aprovado (presença/súmula), o que é derivado por cálculo (indicadores/pontuações) e o que é interpretação tática/hipótese [1, 14-17]. Auditoria e Reversibilidade: Com a gravação append-only dos logs de alteração e a manutenção das provas de proveniência do scout (timecodes e referências de vídeo P0), qualquer cálculo ou estatística pode ser reauditado e reconstruído a qualquer tempo no futuro [3, 14-17].

zonas de quadra no handebol de praia

As principais conclusões sobre as zonas de quadra no handebol de praia — com foco no ataque posicionado e na construção de finalizações — decorrem dos estudos observacionais e de análise de redes do seu caderno (em especial a tese de Caporal sobre o adulto feminino e os protocolos de modelagem do CEPRAEA):

1.  Predomínio Absoluto e Centralidade da Zona Centro-Direita (CD) Quando a quadra é dividida em quatro zonas de passe e ataque — Lateral Esquerda (LE), Centro-Esquerda (CE), Centro-Direita (CD) e Lateral Direita (LD) —, a zona Centro-Direita (CD) emerge como o nó de maior importância e centralidade regulatória em todo o sistema ofensivo [1, 2]:

Volume de Assistências: Em análises de partidas femininas de alto nível, 66% dos passes que resultaram em arremessos em gol (416 de 629) originaram-se da zona Centro-Direita (CD) [1, 2]. Centralidade na Rede (Eigenvector Centrality = 1,0): A posição CD atua como o grande distribuidor do ataque, mantendo conexões diretas e de alto valor com todas as demais posições de finalização [1, 2]. Ranqueamento Geral de Centralidade: CD (1,0) ➔ LE (0,72) ➔ LD (0,71) ➔ CE (0,51) [1, 3].

1.  Padrão de Origem dos Passes por Tipo de Finalização A distribuição geográfica dos passes varia substancialmente dependendo de o arremesso ser de aérea ou de giro (360°):

Passes para Aérea (Ponte Aérea): 78% dos passes para gol em aérea partem da zona CD (148 de 188 ações) [1, 4]. A partir da zona CD, os passes para aérea são distribuídos de forma homogênea entre as recebedoras nas laterais e no centro (LD: 28%, CE: 27%, LE: 24%) [4]. Centralidade na Aérea: CD (1,0) ➔ LD (0,70) ➔ CE (0,67) ➔ LE (0,59) [1, 5]. Passes para Giro (360°): 70% dos passes para arremessos em giro partem da zona CD (202 de 287 ações) [1, 6]. Diferente da aérea, os passes para giro partindo da CD têm um direcionamento prioritário para as pontas/laterais: 33% para a LE e 28% para a LD [6]. Centralidade no Giro: CD (1,0) ➔ LE (0,75) ➔ LD (0,70) ➔ CE (0,38) [1, 6].

1.  Razão Tática da Assimetria entre CD e CE (A Regra da Pivô Destra) A diferença marcante de volume e centralidade entre o Centro-Direita (CD) e o Centro-Esquerda (CE) não é casual, mas decorre do comportamento tático e da dominância motora [7]:

Pivôs Destras: A maioria das pivôs em quadra é destra e atua infiltrada/fixada predominantemente no lado esquerdo do ataque (zona CE) [7]. O papel da Armadora/Especialista: Com a pivô ocupando a zona CE, a jogadora responsável por armar, distribuir e construir o jogo (Central / Especialista) posiciona-se naturalmente na zona CD [7, 8]. Inversão em caso de canhotas: Se a equipe jogar com pivô canhota, a lógica se inverte, transferindo a centralidade para a zona CE [8].

1.  Importância de Não Unificar as Zonas Centrais Estudos clássicos reuniam o meio de quadra em uma única categoria ("Centro") [7, 9]. A literatura recente do seu caderno demonstra que unificar as zonas centrais oculta informações táticas decisivas [7]:

Se as zonas fossem somadas como um "Centro" genérico, perder-se-ia a leitura do fluxo de fixação, da rotação das armadoras e do lado em que a defesa sofre maior desequilíbrio [7].

1.  Implicações Defensivas: Como Neutralizar o Ataque Entender a preferência espacial pelas zonas gera uma aplicação defensiva direta [10]:

Como 78% das jogadas de aérea nascem de passes do Centro-Direita (CD), defesas de elite devem congestioná-la e tirar o conforto da passadora/especialista nessa zona específica [10]. Pressionar a zona CD reduz a precisão dos passes altos de aérea e força o ataque a buscar giros individuais pelas extremidades (LE e LD) [10, 11].

1.  Modelo de Rastreamento no CEPRAEA (Protocolo DEC-015 e TAX-006) Na arquitetura de dados e no scout do CEPRAEA, a quadra é mapeada sob duas regras espaciais rigorosas [12, 13]:

Normalização da Quadra (TAX-006): As 4 faixas laterais de 3 metros de largura (ZE, ZCE, ZCD, ZD) são sempre contadas da perspectiva da equipe atacante olhando de frente para o gol adversário [12, 13]. Separação entre Origem e Destino/Alvo (DEC-015): A zona de origem da finalização (onde a atleta decola ou apoia para o arremesso) é uma dimensão totalmente independente da zona de alvo no gol (setor da baliza onde a bola entra ou bate) [13, 14]. Uma não pode preencher ou substituir a outra no banco de dados [13].

Zonas de Origem do Passe x Sistemas Defensivos adversários Com base nos estudos observacionais do handebol de praia feminino de alto rendimento e nas diretrizes táticas do CEPRAEA [1-4], apresento a proposta de tabela detalhada cruzando as zonas de origem do passe (Centro-Direita, Lateral Direita, Lateral Esquerda e Centro-Esquerda) com os sistemas defensivos adversários (3:0 e 2:1).

1.  Mapeamento Científico das Origens do Passe (Categoria Feminina Adulta) Os dados epidemiológicos e de análise de redes (14 partidas dos Jogos Mundiais de Praia) mostram a distribuição dos 629 passes que resultaram em arremessos em gol [1]:

Zona de Origem do Passe Total Geral (%) [5] Centralidade Geral (Eigenvector) [5] % em Jogadas de Aérea (188 passes) [6] % em Jogadas de Giro (287 passes) [7] Destinos Principais da Bola [5-7] Centro-Direita (CD) 416 (66%) 1,00 78% 70% Lateral Esquerda (33% Giro), Lateral Direita (28% Aérea / 28% Giro), Centro-Esquerda (27% Aérea) Lateral Direita (LD) 85 (14%) 0,71 11% 12% Centro-Esquerda (7% Aérea), Centro-Direita (7% Giro), Lateral Esquerda (2% Aérea) Lateral Esquerda (LE) 69 (11%) 0,73 4% 8% Centro-Esquerda (5% Giro), Centro-Direita (5% Geral), Lateral Direita (3% Aérea) Centro-Esquerda (CE) 59 (9%) 0,51 7% 10% Lateral Esquerda (6% Geral / 5% Giro), Centro-Direita (3% Giro), Lateral Direita (2% Aérea)

1.  Tabela Cruzada: Zona de Origem do Passe × Sistema Defensivo Adversário Abaixo, cada zona de origem é analisada em relação à dinâmica contra o Sistema Defensivo 3:0 (linha compacta recuada de 3 defensoras) [8, 9] e o Sistema Defensivo 2:1 (linha com 1 defensora avançada pressionando a zona central) [10-12]:

Zona de Origem do Passe Comportamento no Sistema Defensivo 3:0 (Defesa Fechada/Compacta) [8, 13] Comportamento no Sistema Defensivo 2:1 (Defesa Aberta com Avançada) [10, 12] Centro-Direita (CD)

(Especialista / Central) Zona de Conforto e Máxima Distribuição: • A defesa recuada dá tempo para a central ler a quadra e armar [13, 14]. • Permite o disparo de aéreas homogêneas para LD (28%), CE (27%) e LE (24%) [6].

• Alimenta giros diretos nas extremidades (33% para LE e 28% para LD) [7]. Zona sob Pressão Direta: • A Marcadora Avançada atua para afastar a central da zona de conforto e forçar passes mais altos/lentos [12]. • Dificulta a conexão direta em aérea de primeira intenção [12, 15].

• Resposta Tática: Exige usar a CD para atrair a avançada e acionar o passe de devolução ou buscar a pivô no espaço livre [16, 17]. Lateral Direita (LD)

(Lateral / Especialista na Direita) Fixação Lateral e Finalização: • Atrai a defensora extrema adversária, gerando espaços para infiltração no meio [18, 19].

• Serve como ponto de passe de retorno (devolução) para a CD ou assistência de giro para a LE [5, 7]. Exploração das Costas da Avançada: • Aproveita a largura da quadra para obrigar a defesa a se deslocar em diagonal [20, 21].

• Excelente origem de passe em profundidade para a pivô e inversão rápida para a LE [20]. Lateral Esquerda (LE)

(Lateral / Especialista na Esquerda) Construção de Giros e Devoluções: • Segunda maior centralidade para finalizações em giro (eigenvector = 0,75) [7, 22].

• Utilizada para fixar a defensora de base e realizar o "passe de continuidade" ou "devolução pós-giro" para a central [17, 23]. Infiltração e Ataque ao Espaço Livre: • Se a marcadora avançada subir na central, a LE ganha espaço para cortar por trás ou acionar a pivô [23, 24].

• Origem de passes precisos para a aérea da LD na extrema direita [24]. Centro-Esquerda (CE)

(Pivô Destra / Central Lado Esquerdo) Fixação Interna da Pivô: • Zona de atuação preferencial da pivô destra no ataque 3:1 [25-27].

• Ocupa a base defensiva adversária, gerando apoios curtos e tabelas de devolução com a CD/LE [16, 28]. Ponto de Escape e Distribuição Secundária: • Quando a CD é neutralizada pela marcadora avançada, a CE passa a ser a principal válvula de escape do ataque [16, 28].

• A pivô/central atua como nova distribuidora, acionando as infiltrações da LE e LD [16, 28].

1.  Principais Conclusões para o Plano de Jogo A Zona Centro-Direita (CD) é o Motor do Ataque: Independentemente da defesa adversária, CD concentra de 70% a 78% dos passes para gols de 2 pontos (Aéreas e Giros) [6, 7]. Impacto da Defesa 2:1: Quando o adversário utiliza a defesa 2:1 com marcadora avançada, a intenção é desorganizar a zona CD [12]. A resposta tática do CEPRAEA deve ser o uso imediato do jogo de devolução [17] e a ativação da pivô na zona CE como segunda construtora da jogada [16, 28]. Padrão de Finalização no Giro: Os passes vindos da zona CD para giro têm como destino prioritário a Lateral Esquerda (33%) e a Lateral Direita (28%), aproveitando a fixação das defensoras de base e o ângulo de abertura [7, 29].

Relações e Cardinalidades A modelagem de dados do CEPRAEA transforma as regras de negócio e a operação do handebol de praia em uma estrutura relacional normalizada [1-3]. Para garantir a integridade dos dados, o sistema adota identificadores estáveis imutáveis (como athlete_id, evento_id, jogo_id) [4, 5] e aplica decomposições de relacionamentos N:N através de tabelas associativas sempre que o vínculo possui atributos próprios (como datas, papéis ou status) [3, 5].

Abaixo está a explicação detalhada das relações e cardinalidades organizadas por módulos do sistema:

1.  Módulo de Cadastro, Elenco e Atribuição Tática (Bloco 1) DB_ATLETAS (1) ──(1:1)──▶ DB_POSICOES_SECUNDARIAS (1) Cardinalidade: 1:1 (Um para Um) [4, 6]. Explicação: Cada atleta cadastrada possui exatamente uma linha de registro de posições secundárias/versatilidade tática, vinculada obrigatoriamente pela chave athlete_id [4, 6]. DB_ATLETAS (1) ──(1:1)──▶ DB_ATLETA_POSICOES_TATICAS (1) Cardinalidade: 1:1 (Um para Um) [4, 7]. Explicação: Visão materializada que consolida a atribuição tática da atleta por setor (ofensiva principal/secundária, defensiva principal/secundária e goleira) [4, 7]. DB_ATLETAS (1) ──(1:N)──▶ DB_ATLETA_POSICOES_LONG (N) Cardinalidade: 1:N (Um para Muitos) [4]. Explicação: A projeção relacional longa desnormaliza as habilitações táticas da atleta [4]. Uma única atleta pode gerar de 1 a 5 linhas na tabela longa (uma linha para cada combinação válida de posição tática) [4, 7]. DB_POSICOES (1) ──(1:N)──▶ DB_ATLETAS (N) Cardinalidade: 1:N (Um para Muitos) [4, 8]. Explicação: Uma posição do vocabulário controlado (ex.: CENTRAL, PIVÔ) pode ser a posição principal de várias atletas, mas cada atleta possui apenas uma posição principal cadastrada [4, 8, 9]. Regra Semântica da Goleira: O sistema não trata GOLEIRA como um conjunto fixo de pessoas, pois uma atleta pode mudar de função no jogo [10]. A goleira é definida como uma posição que pertence à função DEFESA [4, 8].
2.  Módulo de Operação, Agendas, Treinos e Presenças (Bloco 2) DB_CALENDARIO (1) ──(1:0..1)──▶ DB_TREINOS (0..1) Cardinalidade: 1:0..1 (Um para Zero ou Um) [11, 12]. Explicação: Nem todo evento do calendário é um treino (pode ser uma competição ou reunião) [11, 12]. Quando o evento é um treino, existe uma correspondência de 1:1 entre a data/agenda e a ficha da sessão [11, 12]. DB_CALENDARIO / DB_EVENTOS (1) ──(1:N)──▶ DB_DISPONIBILIDADE_DECLARADA (N) Cardinalidade: 1:N (Um para Muitos) [4, 13]. Explicação: Um evento recebe a declaração de intenção de várias atletas [4, 13]. Unicidade e Upsert: Para a combinação específica evento_id + athlete_id, a cardinalidade é estritamente 1:1 [4]. O sistema garante no máximo um registro corrente por atleta e evento via operações de Upsert [4]. DB_TREINOS (1) ──(1:N)──▶ DB_PRESENCA_PROPOSTA (N) Cardinalidade: 1:N (Um para Muitos) [4, 14]. Explicação: Uma sessão de treino gera várias propostas de presença vindas do preenchimento do formulário Wellness Pós-Treino pelas atletas [4, 14]. DB_PRESENCA_PROPOSTA (0..1) ──(Homologação)──▶ DB_PRESENCA (1) Cardinalidade: 0..1 : 1 (Proposta opcional para fato confirmado) [4, 14]. Explicação: Uma proposta autorrelatada só gera exatamente um registro factual na tabela DB_PRESENCA após a decisão e aprovação explícita do treinador [4, 14, 15]. DB_TREINOS (1) ──(1:N)──▶ DB_PRESENCA (N) Cardinalidade: 1:N (Um para Muitos) [4, 15]. Explicação: Um treino realizado possui múltiplas presenças factuais confirmadas [4, 15]. Distinção Fundamental: O modelo separa rigorosamente Disponibilidade Declarada (intenção prospectiva) de Presença Factual (fato verificado e homologado) [4, 16, 17].
3.  Módulo de Competições, Convocações e Partidas (Bloco 3) DB_COMPETICOES (1) ──(1:N)──▶ DB_CONVOCACOES (N) Cardinalidade: 1:N (Um para Muitos) [4, 18]. Explicação: Uma competição ou circuito abrange uma ou mais convocações formais / relações nominais por etapa [4, 18]. DB_COMPETICOES (1) ──(1:N)──▶ DB_JOGOS (N) Cardinalidade: 1:N (Um para Muitos) [4, 12, 19]. Explicação: Uma competição contém diversas partidas disputadas pela equipe [4, 12, 19]. DB_ATLETAS (N) ──(N:M)──▶ DB_CONVOCACOES (M) Decomposição: Resolvida pela tabela associativa DB_CONVOCACAO_ATLETAS em duas relações 1:N [4, 20]. Cardinalidade da Associação: Uma convocação de etapa possui exatamente 12 atletas na sua relação nominal [4, 20]. Regra de Negócio: A convocação para a etapa comprova apenas a inscrição no documento oficial, não garantindo que a atleta tenha entrado em quadra em todas as partidas [4, 20-22]. DB_ATLETAS (N) ──(N:M)──▶ DB_JOGOS (M) Decomposição: Resolvida pela tabela associativa DB_PARTICIPACAO_JOGO em duas relações 1:N [4, 23]. Cardinalidade da Associação (Regra IHF 4 / TWO_EXCLUDED_OF_TWELVE): Cada jogo possui exatamente 10 atletas com status_participacao = JOGOU e 2 atletas com status_participacao = NAO_JOGOU em súmula por partida [4, 23-25].
4.  Módulo de Scout Observacional e Análise de Vídeo (Bloco 4) O scout segue uma hierarquia observacional estrita [26]:

DB_JOGOS (1) ──▶ DB_POSSES (N) ──▶ DB_BOU (N) ──▶ DB_EVENTOS_TACTICOS (N) ──▶ DB_FINALIZACOES (N) ──▶ DB_GOLEIRA_ACOES (N)

DB_JOGOS (1) ──(1:N)──▶ DB_POSSES (N) Cardinalidade: 1:N [26-28]. Uma partida é composta por dezenas de posses de bola registradas cronologicamente [27, 28]. DB_POSSES (1) ──(1:N)──▶ DB_BOU (N) Cardinalidade: 1:N [26, 29]. Uma posse de bola no ataque posicionado pode conter 1 ou mais Unidades Básicas de Ataque (BOU) [26, 29]. DB_BOU (1) ──(1:N)──▶ DB_EVENTOS_TACTICOS (N) Cardinalidade: 1:N [30]. Dentro de uma BOU, podem ser observados e codificados múltiplos procedimentos táticos sequenciais (ex.: pistão ➔ cruzamento ➔ bloqueio) [30]. DB_BOU / DB_POSSES (1) ──(1:N)──▶ DB_FINALIZACOES (N) Cardinalidade: 1:N [26]. Uma BOU ou posse de bola pode encerrar-se em tentativa de arremesso ao gol [26]. DB_FINALIZACOES (1) ──(1:1..N)──▶ DB_GOLEIRA_ACOES (1..N) Cardinalidade: 1:1 ou 1:N [26]. Cada finalização direcionada à baliza gera a análise defensiva correspondente da goleira adversária e sua ação subsequente de distribuição [26, 31].

1.  Módulo de Governança, Logs e Consolidado (Bloco 5) DB_ATLETAS (1) ──(1:1)──▶ DB_INDICADORES_ATLETA (1) Cardinalidade: 1:1 (Um para Um) [32]. Explicação: Cada atleta possui uma única linha na tabela agregada que consolida o histórico total de convocações, jogos reais, presenças confirmadas e disponibilidades [32]. DB_CONFIG (Chave-Valor) Cardinalidade: Registros individuais 1:1 para configurações e contratos universais do sistema [4]. DB_CHANGELOG (Audit Log) Cardinalidade: 1:N (Um para Muitos) [4, 33]. Cada execução de script, migração ou homologação insere um novo evento em uma trilha histórica imutável do tipo Append-Only [4, 33, 34].

DB_PARTICIPACAO_JOGO A tabela DB_PARTICIPACAO_JOGO é a tabela associativa que resolve a relação de muitos-para-muitos (N:M) entre o cadastro de atletas (DB_ATLETAS) e as partidas disputadas pela equipe (DB_JOGOS), materializando a atuação factual por jogo individual [1, 2].

Abaixo está o detalhamento completo das chaves primárias (PK), chaves estrangeiras (FK) e dos atributos de integridade e governança desta tabela:

1.  Chave Primária (Primary Key — PK) participacao_jogo_id (PK): Tipo de Dado: Texto (PK) [1]. Padrão de Formatação: Identificador único estável no formato estrito PJ-XXX-001 (ex.: PJ-NIT-001, PJ-2ET-001, PJ-3ET-001) [1]. Papel no Banco: Garante a identidade única e atemporal de cada registro individual de participação por partida [1, 3]. Constraint de Unicidade Composta: O banco impõe a restrição UNIQUE(jogo_id, athlete_id), impedindo que uma mesma atleta possua mais de uma linha de registro na mesma partida [1, 3].
2.  Chaves Estrangeiras (Foreign Keys — FK) jogo_id (FK ➔ DB_JOGOS.jogo_id):

Tipo de Dado: Texto (FK) [1]. Função: Relaciona a participação à partida específica realizada em DB_JOGOS (ex.: JOGO-2026-006 ou JOGO-2026-020) [1]. Integridade Referencial: Impede o registro de participação em partidas inexistentes ou invalidadas [3].

athlete_id (FK ➔ DB_ATLETAS.athlete_id):

Tipo de Dado: Texto (FK) [1]. Padrão de Formatação: Formato estrito ATH-XXXX (ex.: ATH-0001 a ATH-0019) [1]. Função: Vincula a participação ao cadastro imutável da atleta. Nomes de exibição e números de camisa são tratados apenas como rótulos de leitura visual, garantindo a durabilidade do dado caso a atleta mude de nome ou número no futuro [1, 2, 4].

competicao_id (FK ➔ DB_COMPETICOES.competicao_id):

Tipo de Dado: Texto (FK) [1]. Função: Relaciona o registro diretamente ao campeonato ou etapa correspondente (ex.: COMP-2026-002 ou COMP-2026-005), facilitando agregações e filtros por torneio sem necessidade de múltiplos joins [1].

convocacao_id (FK ➔ DB_CONVOCACOES.convocacao_id):

Tipo de Dado: Texto (FK) [1]. Função: Rastreia a convocação oficial da etapa que originou a elegibilidade da atleta (ex.: CONV-2026-001 ou CONV-2026-005) [1]. Regra de Separação Semântica: A relação nominal da convocação comprova a inscrição de 12 atletas na etapa, enquanto DB_PARTICIPACAO_JOGO comprova a participação real de no máximo 10 atletas uniformizadas na súmula daquela partida específica [1, 2, 4, 5].

1.  Estrutura Completa de Campos de DB_PARTICIPACAO_JOGO Campo Tipo de Dado Função & Valores Permitidos Natureza Epistêmica Fonte de Dados / Origem participacao_jogo_id Texto (PK) Identificador único da participação (ex.: PJ-NIT-001) [1]. Arquitetural Sistema [1] jogo_id Texto (FK) Chave estrangeira de DB_JOGOS [1]. Arquitetural DB_JOGOS.jogo_id [1] competicao_id Texto (FK) Chave estrangeira de DB_COMPETICOES [1]. Arquitetural DB_COMPETICOES.competicao_id [1] convocacao_id Texto (FK) Chave estrangeira de DB_CONVOCACOES [1]. Arquitetural DB_CONVOCACOES.convocacao_id [1] athlete_id Texto (FK) Chave estrangeira de DB_ATLETAS (ATH-XXXX) [1]. Arquitetural DB_ATLETAS.athlete_id [1] nome_exibicao Texto Espelho do nome da atleta para leitura direta [1]. Rótulo / Derivado DB_ATLETAS.nome_exibicao [1] status_participacao Enum JOGOU, NAO_JOGOU (Composição de súmula) [1]. Fato Esportivo Decisão do Treinador / Súmula (TWO_EXCLUDED_OF_TWELVE) [1, 4] entrou_em_quadra Enum SIM, NAO (Atuação efetiva em quadra) [1]. Scout / Observado Súmula / Análise de Vídeo [1] titular Enum / Text Status de início da partida [1]. Scout / Observado Análise de Vídeo [1] funcao_no_jogo Enum ATAQUE, DEFESA, GOLEIRA, INDEFINIDA [1]. Tática / Observado Análise Técnica da Partida [1] posicao_no_jogo Texto Posição específica desempenhada no jogo [1]. Tática / Observado Análise Técnica da Partida [1] minutos_ou_periodos Texto Minutagem ou sets atuados [1]. Scout / Observado Súmula / Vídeo [1] observacao Texto Detalhamento do confronto ou exceções [1]. Contexto Anotação Técnica [1] fonte Texto Origem da evidência (ex.: "Decisão humana do treinador") [4] Proveniência Registro de Homologação [1, 4] updated_at Timestamp Carimbo estático de alteração (America/Sao_Paulo) [1, 4]. Auditoria Sistema / Banco [1, 4] regra_contagem Texto Regra de negócio: jogo_real se status=JOGOU [1]. Regra de Negócio Contrato DB_CONFIG [1, 4]
2.  Regras de Negócio e Governança Aplicadas à Tabela Regra TWO_EXCLUDED_OF_TWELVE: Quando a relação nominal da etapa possui 12 atletas convocadas (CONV-XXXX), a participação por partida é materializada após o treinador informar explicitamente as 2 atletas que ficaram fora da súmula naquele jogo (status_participacao = NAO_JOGOU); as outras 10 atletas são registradas como JOGOU [1, 4, 5]. Impacto nos Indicadores de Elenco: O indicador jogos_total do elenco em DB_INDICADORES_ATLETA e em DB_EXPORT_ANALISE_JOGOS contabiliza estritamente as linhas onde status_participacao = JOGOU nesta tabela [1, 4, 6, 7]. Convocações sem confirmação de jogo não somam partidas jogadas [1, 2, 4].

DB_ATLETAS A tabela DB_ATLETAS é a entidade mestra de cadastro do elenco do CEPRAEA, atuando como a fonte primária de autoridade para a identidade e atribuição cadastral das jogadoras [1, 2].

Abaixo está o detalhamento completo de sua Chave Primária (PK), das Chaves Estrangeiras (FK) contidas na tabela, das tabelas externas que a referenciam e da estrutura de governança dos seus campos:

1.  Chave Primária (Primary Key — PK) athlete_id (PK): Tipo de Dado: Texto (PK) [2]. Padrão de Formatação: Identificador estável em formato estrito ATH-XXXX (ex.: ATH-0001 a ATH-0019) [2]. Função no Banco: Garante a identidade única, imutável e atemporal de cada atleta no sistema [2]. Constraint: NOT NULL / PRIMARY KEY [2]. Razão de Arquitetura: Nomes de exibição (nome_exibicao) e números de camisa sofrem variações de digitação, apelidos ou mudanças ao longo do tempo [2, 3]. Para garantir a integridade relacional por 10+ anos, todas as junções (Joins) do banco utilizam obrigatoriamente a chave estável athlete_id, tratando o nome apenas como rótulo de exibição [1].
2.  Chaves Estrangeiras (Foreign Keys — FK) dentro de DB_ATLETAS Embora DB_ATLETAS seja uma tabela mestre de cadastro, ela faz referência a duas tabelas de vocabulário controlado para garantir a integridade do domínio esportivo [1, 2, 4]:

funcao_principal (FK ➔ DB_FUNCOES.funcao):

Tipo de Dado: Enum / Texto (FK) [2, 4]. Domínio de Valores Permitidos: DEFESA, ATAQUE, INDEFINIDA [2, 4]. Função: Vincula a atleta à sua macrofunção tática primária cadastrada no clube [2, 4]. Autoridade: A autoridade cadastral desta função é restrita a DB_ATLETAS.funcao_principal [1].

posicao_principal (FK ➔ DB_POSICOES.posicao):

Tipo de Dado: Enum / Texto (FK) [2, 4]. Domínio de Valores Permitidos: GOLEIRA, CENTRAL, LATERAL ESQUERDA, LATERAL DIREITA, PIVÔ, DEFENSORA SOLTA, DEFENSORA BASE, DEFENSORA COBERTURA, CENTRAL DIREITA, CENTRAL ESQUERDA, DEFENSORA AVANÇADA [2, 4]. Função: Vincula a atleta ao catálogo oficial de posições canônicas do handebol de praia [2, 4]. Autoridade: A autoridade cadastral para a posição principal reside exclusivamente em DB_ATLETAS.posicao_principal [1].

1.  Onde DB_ATLETAS.athlete_id é Referenciado como Chave Estrangeira (FK) Para manter a consistência relacional e evitar duplicidades, o identificador athlete_id é consumido como Chave Estrangeira em quase todos os módulos do sistema [1, 2, 5-10]:

Módulo de Elenco e Posições Táticas: DB_POSICOES_SECUNDARIAS.athlete_id (PK/FK 1:1) — Atribuição de versatilidade e posições alternativas [7]. DB_ATLETA_POSICOES_TATICAS.athlete_id (PK/FK 1:1) — Visão materializada por setor [5]. DB_ATLETA_POSICOES_LONG.athlete_id (PK Composta/FK 1:N) — Projeção relacional longa [6]. Módulo Operacional e Presença: DB_DISPONIBILIDADE_DECLARADA.athlete_id (FK 1:N) — Registro de intenções/disponibilidades [9]. DB_PRESENCA_PROPOSTA.athlete_id (FK 1:N) — Fila transitória do Wellness Pós-Treino [11]. DB_PRESENCA.athlete_id (FK 1:N) — SSOT de presença factual confirmada [8]. Módulo Competitivo: DB_CONVOCACAO_ATLETAS.athlete_id (FK 1:N) — Relação nominal de 12 atletas da etapa [12]. DB_PARTICIPACAO_JOGO.athlete_id (FK 1:N) — Atuação factual por jogo individual (10 ativas por partida) [13]. Módulo Agregado / Dashboards: DB_INDICADORES_ATLETA.athlete_id (PK/FK 1:1) — Consolidado de assiduidade e jogos [10].

1.  Estrutura Completa de Atributos de DB_ATLETAS Campo Tipo de Dado Restrições & Domínio Função Operacional & Definição athlete_id Texto (PK) NOT NULL / Formato ATH-XXXX [2] Identificador canônico, único e imutável da atleta [2]. nome_exibicao Texto NOT NULL / Texto livre normalizado [2] Nome operacional de exibição nas telas e relatórios [2]. funcao_principal Enum (FK) DEFESA, ATAQUE, INDEFINIDA [2, 4] Macrofunção tática primária cadastrada [2]. posicao_principal Enum (FK) GOLEIRA, CENTRAL, PIVÔ, etc. [2, 4] Posição tática principal de atuação em quadra [2]. status_ativo Enum SIM, NAO (Default = SIM) [2] Indica se a atleta compõe o elenco ativo do clube [2]. numero_camisa Texto Inteiro em texto (ex.: 19, 85) ou INDETERMINADO [2] Número do uniforme oficial registrado na confederação/federação [2]. fonte_numero_camisa Texto Permitido Vazio (NULL) [2] Rastreabilidade documental do número de camisa (ex.: boletim/súmula) [2]. observacao Texto Permitido Vazio (NULL) [2] Anotações cadastrais de auditoria ou histórico [2]. fonte_autorizada Texto NOT NULL / Rastreável [2] Rastreabilidade da decisão humana que homologou o cadastro [2]. created_at Timestamp NOT NULL / ISO 8601 com fuso America/Sao_Paulo [2] Carimbo estático de criação do registro no banco [2]. updated_at Timestamp NOT NULL / ISO 8601 com fuso America/Sao_Paulo [2] Carimbo estático da última alteração cadastral [2].

DB_POSICOES A tabela DB_POSICOES é o vocabulário controlado e o catálogo mestre de posições táticas do handebol de praia no CEPRAEA [1]. Ela garante a padronização das posições de linha e da baliza, estabelecendo o domínio fechado de valores aceitos em todo o sistema relacional.

Abaixo está o detalhamento completo de sua Chave Primária (PK), das Chaves Estrangeiras (FK) contidas na tabela, das referências externas e da estrutura de atributos:

1.  Chave Primária (Primary Key — PK) posicao_id (PK): [1] Tipo de Dado: Texto (PK). Padrão de Formatação: Identificador estável no formato estrito POS-XXXX (ex.: POS-0001 a POS-0011) [1]. Função no Banco: Identificador único, imutável e atemporal de cada posição tática do catálogo [1]. Constraint: NOT NULL / PRIMARY KEY.
2.  Chave Estrangeira (Foreign Key — FK) dentro de DB_POSICOES funcao (FK ➔ DB_FUNCOES.funcao): [1] Tipo de Dado: Enum / Texto (FK) [1]. Domínio de Valores Permitidos: DEFESA, ATAQUE [1]. Função: Associa cada posição do catálogo à sua macrofunção tática correspondente [1]. Regra Semântica da Goleira: Por decisão de governança (DB_CONFIG.goalkeeper_semantics), a posição GOLEIRA (POS-0001) pertence obrigatoriamente à macrofunção DEFESA [1, 2]. A goleira é tratada como uma posição defensiva da baliza, e não como um grupo fixo e imutável de pessoas.
3.  Onde DB_POSICOES é Referenciada como Chave Estrangeira (FK) O vocabulário de DB_POSICOES atua como validador de integridade referencial para todos os módulos do banco de dados:

DB_ATLETAS.posicao_principal (FK): Garante que a posição principal da atleta seja uma posição válida do catálogo [1, 3]. DB_POSICOES_SECUNDARIAS.posicao_secundaria_1..3 (FK): Valida as atribuições de versatilidade e posições alternativas das jogadoras [4]. DB_SISTEMAS_POSICOES.posicao_tatica (FK): Vincula os slots táticos dos sistemas de jogo (3:0, 2:1 na defesa e 3:1, 2:1 no ataque) às posições canônicas [5]. DB_ATLETA_POSICOES_TATICAS (FKs): Valida os campos de posição ofensiva e defensiva na visão materializada por setor [6]. DB_ATLETA_POSICOES_LONG.posicao_tatica (FK): Valida as habilitações táticas na projeção longa usada para o cálculo da matriz de cobertura [7, 8].

1.  Estrutura Completa de Atributos de DB_POSICOES Campo Tipo de Dado Restrições & Domínio Definição Operacional & Exemplo [1] posicao_id Texto (PK) NOT NULL / Formato POS-XXXX Identificador único da posição no catálogo (ex.: POS-0001 a POS-0011) [1]. posicao Texto (UNIQUE) NOT NULL / Caixa alta Nome canônico da posição tática (ex.: GOLEIRA, CENTRAL, PIVÔ, DEFENSORA BASE) [1]. funcao Enum (FK) NOT NULL / DEFESA ou ATAQUE Macrofunção à qual a posição pertence em DB_FUNCOES [1]. ativo Enum NOT NULL / SIM ou NAO Indica se a posição está ativa para escolha nos formulários e sistemas [1]. descricao Texto Permitido Vazio (NULL) Texto explicativo da função tática e papéis em quadra [1].
2.  Catálogo Canônico de Posições Registrado (POS-0001 a POS-0011) O catálogo de posições cadastradas em DB_POSICOES no banco de dados do CEPRAEA compreende 11 posições oficiais [1]:

POS-0001 — GOLEIRA (Função: DEFESA): Atleta especializada de guarda-redes/baliza [1]. POS-0002 — CENTRAL (Função: ATAQUE): Armadora e construtora no centro do ataque posicionado [1]. POS-0003 — LATERAL ESQUERDA (Função: ATAQUE): Atleta de ataque pela ala esquerda [1]. POS-0004 — LATERAL DIREITA (Função: ATAQUE): Atleta de ataque pela ala direita [1]. POS-0005 — PIVÔ (Função: ATAQUE): Atleta de ataque infiltrada entre as defensoras de base [1]. POS-0006 — DEFENSORA SOLTA (Função: DEFESA): Defensora responsável pela contenção direta da bola e pressão [1]. POS-0007 — DEFENSORA BASE (Função: DEFESA): Defensora central da primeira linha [1]. POS-0008 — DEFENSORA COBERTURA (Função: DEFESA): Defensora responsável pelo combate à pivô e coberturas [1]. POS-0009 — CENTRAL DIREITA (Função: ATAQUE): Posição de armação/ataque no sistema 2:1 ofensivo [1, 5]. POS-0010 — CENTRAL ESQUERDA (Função: ATAQUE): Posição de armação/ataque no sistema 2:1 ofensivo [1, 5]. POS-0011 — DEFENSORA AVANÇADA (Função: DEFESA): Defensora que atua à frente no sistema defensivo 2:1 [1, 5].

DB_POSICOES_SECUNDARIAS A tabela DB_POSICOES_SECUNDARIAS é a fonte de autoridade do CEPRAEA para o registro, atribuição e governança da versatilidade tática e posições alternativas das atletas do elenco [1].

Abaixo está o detalhamento completo da sua Chave Primária (PK), das Chaves Estrangeiras (FK), da sua cadeia de consumo e da estrutura de atributos e regras de governança:

1.  Chave Primária (Primary Key — PK) athlete_id (PK / FK ➔ DB_ATLETAS.athlete_id): Tipo de Dado: Texto (PK/FK). Padrão de Formatação: Formato estrito ATH-XXXX (ex.: ATH-0001 a ATH-0019) [2]. Função no Banco: Por tratar-se de uma relação de cardinalidade 1:1 (Um para Um) com a tabela mestre DB_ATLETAS, a própria chave estrangeira da atleta atua como a Chave Primária da tabela. Constraint: NOT NULL / PRIMARY KEY.
2.  Chaves Estrangeiras (Foreign Keys — FK) dentro de DB_POSICOES_SECUNDARIAS A tabela conecta a atleta ao catálogo oficial de posições (DB_POSICOES) por meio de três slots flexíveis de versatilidade:

posicao_secundaria_1 (FK ➔ DB_POSICOES.posicao): Tipo de Dado: Enum / Texto (FK). Função: Primeira posição alternativa na qual a atleta está capacitada a atuar (ex.: CENTRAL DIREITA, DEFENSORA BASE, PIVÔ) [2]. posicao_secundaria_2 (FK ➔ DB_POSICOES.posicao): Tipo de Dado: Enum / Texto (FK). Função: Segunda posição alternativa mapeada (permitido vazio / NULL). posicao_secundaria_3 (FK ➔ DB_POSICOES.posicao): Tipo de Dado: Enum / Texto (FK). Função: Terceira posição alternativa mapeada (permitido vazio / NULL).

Nota de Arquitetura: Os campos nome_exibicao, funcao_principal e posicao_principal constam nesta tabela apenas como espelhos derivados de DB_ATLETAS para facilitar a leitura visual do treinador durante o preenchimento, sem criar nova autoridade cadastral [1, 2].

1.  Onde DB_POSICOES_SECUNDARIAS é Consumida na Cadeia Relacional A tabela alimenta a cadeia de materialização tática e análise de cobertura do clube conforme a ordem obrigatória de linhagem definida em DB_CONFIG [1]:

$$text{DB_ATLETAS} + text{DB_POSICOES} + mathbf{text{DB_POSICOES_SECUNDARIAS}} longrightarrow text{DB_ATLETA_POSICOES_TATICAS} longrightarrow text{DB_ATLETA_POSICOES_LONG} longrightarrow text{DB_DISPONIBILIDADE_POSICAO}$$

DB_ATLETA_POSICOES_TATICAS (Visão Materializada por Setor): Combina a posição principal cadastrada em DB_ATLETAS com as posições secundárias autorizadas para preencher os campos ofensiva_secundaria e defensiva_secundaria [2, 3]. DB_ATLETA_POSICOES_LONG (Projeção Relacional Longa): Transforma cada posição secundária em uma linha relacional individual (origem_posicao = 'ofensiva_secundaria' ou 'defensiva_secundaria') [4]. DB_DISPONIBILIDADE_POSICAO (Matriz de Cobertura Tática): Utiliza as posições secundárias projetadas para verificar se os slots táticos dos sistemas de jogo (ex.: CENTRAL DIREITA no ataque 2:1 ou DEFENSORA AVANÇADA na defesa 2:1) possuem cobertura quando atletas versáteis declaram disponibilidade SIM [5, 6].

1.  Estrutura Completa de Atributos de DB_POSICOES_SECUNDARIAS Campo Tipo de Dado Restrições & Domínio Função Operacional & Definição athlete_id Texto (PK/FK) NOT NULL / Formato ATH-XXXX Identificador único e imutável que vincula a versatilidade à atleta [2]. nome_exibicao Texto NOT NULL / Espelho de DB_ATLETAS Rótulo de exibição com o nome da atleta para inspeção humana [2]. funcao_principal Enum DEFESA, ATAQUE, INDEFINIDA Espelho da macrofunção cadastrada em DB_ATLETAS [2]. posicao_principal Enum Posições válidas de DB_POSICOES Espelho da posição principal cadastrada em DB_ATLETAS [2]. posicao_secundaria_1 Enum (FK) Posições de DB_POSICOES ou Vazio Primeira posição tática alternativa autorizada pelo treinador [2]. posicao_secundaria_2 Enum (FK) Posições de DB_POSICOES ou Vazio Segunda posição tática alternativa autorizada [2]. posicao_secundaria_3 Enum (FK) Posições de DB_POSICOES ou Vazio Terceira posição tática alternativa autorizada [2]. status_validacao Enum VALIDADO, PENDENTE Estado de homologação da atribuição de versatilidade (Default = VALIDADO) [2]. fonte_autorizada Texto NOT NULL / Texto livre Rastreabilidade da decisão humana que homologou as posições secundárias [2]. updated_at Timestamp NOT NULL / ISO 8601 estático Carimbo estático de data/hora da última atualização de versatilidade [1, 2].
2.  Regras de Negócio e Governança de Dados Autoridade Restrita (athlete_secondary_positions_authority): A tabela DB_POSICOES_SECUNDARIAS é a única autoridade do banco de dados para a atribuição de posições secundárias. Nenhuma posição alternativa pode ser criada ou alterada diretamente nas visões derivadas (DB_ATLETA_POSICOES_TATICAS ou DB_ATLETA_POSICOES_LONG) [1]. Origem por Decisão Humana Homologada: As atribuições de versatilidade foram registradas por decisão técnica explícita da comissão técnica (ex.: "Decisão humana 2026-06-23: posições secundárias informadas pelo treinador") [2]. Invariante de Goleiras Específicas: Goleiras especializadas sem atuação tática na linha (como Carolina Bezerra, Paola Wolff e Gilvania Balbino) mantêm os slots de posições secundárias estritamente em branco (NULL), evitando falsas contagens de cobertura para o ataque ou linha defensiva [2, 3].

DB_ATLETA_POSICOES_TATICA A tabela DB_ATLETA_POSICOES_TATICAS é a visão tática materializada por setor no CEPRAEA [1]. Ela consolida, em um único registro por atleta, todo o perfil tático de atuação em quadra (ofensiva principal/secundária, defensiva principal/secundária e baliza) [1].

Abaixo está o detalhamento completo de sua Chave Primária (PK), das Chaves Estrangeiras (FK), do seu papel na cadeia de regeneração e da estrutura de atributos e regras de governança:

1.  Natureza de Arquitetura e Regra de Ouro Papel de Derivação Controlada (CONTROLLED_MATERIALIZED_DERIVATION): A DB_ATLETA_POSICOES_TATICAS não possui autoridade cadastral direta [2]. Nenhuma edição manual deve ser feita diretamente nesta tabela [2]. Linhagem Determinística: Ela é recomputada e regenerada deterministicamente a partir da fusão da tabela mestre (DB_ATLETAS), do catálogo de posições (DB_POSICOES) e da atribuição de versatilidade (DB_POSICOES_SECUNDARIAS) [1, 2].
2.  Chave Primária (PK) e Chaves Estrangeiras (FK) athlete_id (PK / FK ➔ DB_ATLETAS.athlete_id): Tipo de Dado: Texto (PK/FK) [1]. Padrão de Formatação: Identificador estável ATH-XXXX (ex.: ATH-0001 a ATH-0019) [1]. Cardinalidade: Relação estrita de 1:1 (Um para Um) com a tabela mestre de atletas DB_ATLETAS [1]. Constraint: NOT NULL / PRIMARY KEY [1]. Campos de Posição Tática (FKs ➔ DB_POSICOES.posicao): ofensiva_principal: Posição de ataque primária da atleta (preenchida apenas se a posição principal vinda de DB_ATLETAS for de ataque) [1]. ofensiva_secundaria: Posição de ataque alternativa mapeada em DB_POSICOES_SECUNDARIAS [1]. defensiva_principal: Posição de linha defensiva primária (preenchida apenas se a posição principal de DB_ATLETAS for de defesa, excluindo goleira) [1]. defensiva_secundaria: Posição de linha defensiva alternativa mapeada [1]. goleira: Sinalização de atuação na baliza (GOLEIRA ou Vazio) [1]. (Nota: Por decisão de governança goalkeeper_semantics, GOLEIRA é tratada como posição defensiva sob a macrofunção DEFESA [2, 3]).
3.  Posição na Cadeia Relacional de Regeneração A regeneração da matriz tática respeita estritamente a ordem de dependência registrada em DB_CONFIG [2]:

$$text{DB_ATLETAS} + text{DB_POSICOES} + text{DB_POSICOES_SECUNDARIAS} longrightarrow mathbf{text{DB_ATLETA_POSICOES_TATICAS}} longrightarrow text{DB_ATLETA_POSICOES_LONG} longrightarrow text{DB_DISPONIBILIDADE_POSICAO}$$

1.  Estrutura Completa de Atributos de DB_ATLETA_POSICOES_TATICAS Campo Tipo de Dado Restrições & Domínio Definição Operacional & Regra de Derivação athlete_id Texto (PK/FK) NOT NULL / Formato ATH-XXXX [1] Identificador canônico e imutável da atleta [1]. nome_exibicao Texto NOT NULL / Espelho de DB_ATLETAS [1] Rótulo de nome da atleta para inspeção visual rápida [1]. funcao_principal Enum DEFESA, ATAQUE, INDEFINIDA [1] Macrofunção tática primária cadastrada em DB_ATLETAS [1]. ofensiva_principal Enum (FK) Posição de Ataque de DB_POSICOES ou Vazio [1] Posição de ataque principal da atleta [1]. ofensiva_secundaria Enum (FK) Posição de Ataque de DB_POSICOES ou Vazio [1] Posição de ataque secundária derivada de DB_POSICOES_SECUNDARIAS [1]. defensiva_principal Enum (FK) Posição Defensiva (exceto Goleira) ou Vazio [1] Posição de linha defensiva principal da atleta [1]. defensiva_secundaria Enum (FK) Posição Defensiva (exceto Goleira) ou Vazio [1] Posição de linha defensiva secundária derivada de DB_POSICOES_SECUNDARIAS [1]. goleira Enum GOLEIRA ou Vazio [1] Sinalização de atuação especializada ou secundária na baliza [1]. fonte_autorizada Texto NOT NULL / Texto de rastreabilidade [1] Rastreabilidade da combinação das tabelas de origem [1]. status_validacao Enum VALIDADO [1] Estado de validação da materialização tática [1]. updated_at Timestamp NOT NULL / ISO 8601 estático [1] Carimbo estático de execução da rotina de regeneração [1, 2].

DB_ATLETA_POSICOES_LONG A tabela DB_ATLETA_POSICOES_LONG é a projeção relacional longa (unpivoted) derivada da visão tática por setor (DB_ATLETA_POSICOES_TATICAS) [1, 2].

Ela desnormaliza os setores táticos (ofensivo principal/secundário, defensivo principal/secundário e baliza) em registros individuais por combinação de atleta × posição tática [3, 4]. O seu propósito arquitetural central é viabilizar junções relacionais eficientes (Joins) com a tabela de slots dos sistemas de jogo (DB_SISTEMAS_POSICOES) e com a declaração de disponibilidades (DB_DISPONIBILIDADE_DECLARADA), alimentando deterministicamente a matriz de cobertura tática (DB_DISPONIBILIDADE_POSICAO) [1, 5].

1.  Chave Primária Composta (PK) e Chaves Estrangeiras (FK) athlete_id (PK Composta / FK ➔ DB_ATLETAS.athlete_id): Tipo de Dado: Texto (PK/FK) [4]. Padrão de Formatação: Formato estrito ATH-XXXX (ex.: ATH-0001 a ATH-0019) [4, 6]. Função: Vincula cada linha da projeção longa ao cadastro imutável da atleta. Nomes de exibição (nome_exibicao) são apenas rótulos visuais de leitura [1, 4]. posicao_tatica (PK Composta / FK ➔ DB_POSICOES.posicao): Tipo de Dado: Enum / Texto (PK/FK) [4, 7]. Domínio de Valores Permitidos: Posições canônicas de DB_POSICOES (CENTRAL, LATERAL DIREITA, LATERAL ESQUERDA, PIVÔ, CENTRAL DIREITA, CENTRAL ESQUERDA, DEFENSORA BASE, DEFENSORA SOLTA, DEFENSORA COBERTURA, DEFENSORA AVANÇADA, GOLEIRA) [4, 7]. Função: Posição específica para a qual a atleta está habilitada e mapeada a atuar [4]. origem_posicao (PK Composta / Enum): Tipo de Dado: Enum [4]. Domínio de Valores Permitidos: ofensiva_principal, ofensiva_secundaria, defensiva_principal, defensiva_secundaria, goleira [4]. Função: Rastreia a hierarquia e o setor de origem de onde a habilitação tática foi projetada a partir da DB_ATLETA_POSICOES_TATICAS [1, 4]. Constraint de Unicidade / PK Composta: PRIMARY KEY (athlete_id, posicao_tatica, origem_posicao) [4]. Garante que uma atleta não possua registros duplicados para a mesma posição provenientes da mesma origem de setor [4].
2.  Posição na Cadeia Relacional de Regeneração (Linhagem) A projeção relacional longa é uma derivação materializada controlada (CONTROLLED_MATERIALIZED_DERIVATION) e ocupa o penúltimo elo da cadeia tática obrigatória fixada em DB_CONFIG [1]:

$$text{DB_ATLETAS} + text{DB_POSICOES} + text{DB_POSICOES_SECUNDARIAS} longrightarrow text{DB_ATLETA_POSICOES_TATICAS} longrightarrow mathbf{text{DB_ATLETA_POSICOES_LONG}} longrightarrow text{DB_DISPONIBILIDADE_POSICAO}$$ [1]

Regra de Linhagem: Nenhuma edição direta é feita em DB_ATLETA_POSICOES_LONG [1]. Ela é recomputada por scripts automatizados sempre que houver alteração cadastral em DB_ATLETAS ou na atribuição de versatilidade em DB_POSICOES_SECUNDARIAS [1, 3, 8].

1.  Estrutura Completa de Atributos de DB_ATLETA_POSICOES_LONG Campo Tipo de Dado Restrições & Domínio Função Operacional & Definição athlete_id Texto (PK/FK) NOT NULL / Formato ATH-XXXX [4] Chave primária de junção estável da atleta [1, 4]. nome_exibicao Texto NOT NULL / Espelho de DB_ATLETAS [4] Rótulo com o nome da atleta para inspeção analítica direta [4]. tipo_sistema Enum NOT NULL / ATAQUE ou DEFESA [4, 7] Fase/fase de jogo à qual a posição tática pertence (derivada da função da posição em DB_POSICOES) [4, 7]. posicao_tatica Enum (PK/FK) NOT NULL / Posições de DB_POSICOES [4, 7] Posição tática específica em que a atleta está habilitada [4]. origem_posicao Enum (PK) NOT NULL / ofensiva_principal, ofensiva_secundaria, defensiva_principal, defensiva_secundaria, goleira [4] Rastreabilidade do setor de onde a habilitação tática foi desnormalizada [4]. status_validacao Enum NOT NULL / VALIDADO [4] Estado de aprovação do processo de projeção longa [4]. fonte_autorizada Texto NOT NULL / Default = DB_ATLETA_POSICOES_TATICAS [4] Rastreabilidade do registro de origem da visão tática [4]. updated_at Timestamp NOT NULL / ISO 8601 estático (America/Sao_Paulo) [1, 4] Carimbo estático de data/hora do recálculo da projeção [1, 4].
2.  Exemplo Prático de Desnormalização (Unpivot) Quando a jogadora Aline Kecia (ATH-0002) é cadastrada com posição principal LATERAL DIREITA e posição secundária CENTRAL DIREITA, o banco transforma o registro único de linha da DB_ATLETA_POSICOES_TATICAS em duas linhas relacionais na DB_ATLETA_POSICOES_LONG [3, 4, 8]:

Seção 100

┌─────────────────────────────────┐ ┌────────────────────────────────┐ │ DB_DISPONIBILIDADE_DECLARADA │ │ DB_ATLETA_POSICOES_LONG │ │ (Atletas com resposta = 'SIM') │ │ (Posições autorizadas por ID) │ └────────────────┬────────────────┘ └───────────────┬────────────────┘ │ │ └───────────────────┬───────────────────┘ ▼ ┌───────────────────────────────┐ │ DB_DISPONIBILIDADE_POSICAO │ ◄─── ┌──────────────────────────┐ │ (Matriz de Cobertura Tática) │ │ DB_SISTEMAS_POSICOES │ └───────────────────────────────┘ │ (14 slots x Requisitos) │ └──────────────────────────┘

DB_DISPONIBILIDADE_DECLARADA: Filtra quais atletas responderam SIM para a data de treino avaliada [1]. DB_ATLETA_POSICOES_LONG: Identifica todas as posições táticas (principais e secundárias) para as quais essas atletas disponíveis estão habilitadas [1]. DB_SISTEMAS_POSICOES: Fornece o catálogo dos 14 slots táticos requeridos pelos sistemas ofensivos (3:1 e 2:1) e defensivos (3:0 e 2:1) [2, 3].

1.  Unidade de Análise e Estrutura de Chaves Unidade de Análise: 1 Linha = 1 Data de Treino × 1 Slot Tático de um Sistema de Jogo [2]. Chave Primária Composta (PK): (data_treino, tipo_sistema, sistema, slot_tatico) [2]. Chaves Estrangeiras (FK): data_treino ➔ [link suspeito removido]_evento / DB_TREINOS.treino_id posicao_tatica ➔ DB_POSICOES.posicao
2.  Estrutura Completa de Atributos de DB_DISPONIBILIDADE_POSICAO Campo Tipo de Dado Restrições / Domínio Definição Operacional & Regra de Negócio data_treino Data (PK/FK) NOT NULL / Formato DD/MM/YYYY Data da sessão de treino avaliada no calendário [2]. tipo_sistema Enum (PK) NOT NULL / DEFESA, ATAQUE Fase de jogo do sistema tático [2, 3]. sistema Enum (PK) NOT NULL / 3:0, 2:1 (Defesa) ou 3:1, 2:1 (Ataque) Sistema tático de jogo avaliado [2, 3]. slot_tatico Texto (PK) NOT NULL (ex.: BASE, SOLTA, CENTRAL, PIVÔ) Papel ou posto específico exigido dentro do sistema [2, 3]. posicao_tatica Enum (FK) NOT NULL / Posições de DB_POSICOES Posição canônica necessária para preencher o slot [2, 3]. quantidade_requerida Inteiro NOT NULL / Inteiro >= 1 (padrão = 1) Número mínimo de atletas necessárias para o slot naquele sistema [2, 3]. atletas_disponiveis_qtd Inteiro NOT NULL / Inteiro >= 0 Contagem de atletas únicas habilitadas no slot com disponibilidade SIM na data [2]. atletas_disponiveis_nomes Texto Nomes separados por vírgula ou Vazio Lista textual formatada com os nomes das atletas disponíveis para o slot [2]. status_cobertura Enum NOT NULL / COBERTO, INSUFICIENTE Diagnóstico automático de cobertura do slot [2]. origem Texto NOT NULL / Texto de rastreabilidade Registro de linhagem das tabelas consumidas [2]. updated_at Timestamp NOT NULL / ISO 8601 estático (America/Sao_Paulo) Carimbo estático de data/hora de execução do cálculo [2].
3.  Regra de Cálculo do Diagnóstico (status_cobertura) Para cada combinação de data e slot tático, a matriz recomputa o diagnóstico da seguinte forma [2]:

s_cobertura} = begin{cases} text{COBERTO}, & text{se } text{atletas_disponiveis_qtd} ge text{quantidade_requerida}  text{INSUFICIENTE}, & text{se } text{atletas_disponiveis_qtd} < text{quantidade_requerida} end{cases}$$

1.  Exemplo Prático de Matriz de Cobertura (Treino de 02/07/2026) Abaixo está uma amostra real da tabela consumidora para o treino de 02/07/2026, demonstrando como o sistema identifica posições com sobra de atletas e posições com gargalo [2]:

data_treino tipo_sistema sistema slot_tatico posicao_tatica qtd_req qtd_disp atletas_disponiveis_nomes status_cobertura 02/07/2026 DEFESA 3:0 BASE DEFENSORA BASE 1 1 Aline Mello COBERTO 02/07/2026 DEFESA 3:0 SOLTA DEFENSORA SOLTA 1 3 Gabi Peixinho, Rafaela Dillmann, Roberta Hernandez COBERTO 02/07/2026 DEFESA 2:1 AVANÇADA DEFENSORA AVANÇADA 1 1 Gabi Peixinho COBERTO 02/07/2026 ATAQUE 3:1 PIVÔ PIVÔ 1 2 Marleide Nunes, Paloma Caneca COBERTO 02/07/2026 ATAQUE 2:1 CENTRAL DIREITA CENTRAL DIREITA 1 4 Aline Augusto, Aline Kecia, Fernanda Campbell, Paloma Caneca COBERTO

Se na data 09/07/2026 nenhuma lateral esquerda com resposta SIM estivesse disponível, o slot LATERAL ESQUERDA retornaria qtd_disp = 0 e status_cobertura = INSUFICIENTE, sinalizando imediatamente o gargalo tático para a comissão técnica [2].

1.  Regras Imutáveis de Governança e Segurança Fonte Prospectiva Exclusiva (tactical_coverage_availability_source): A matriz de cobertura tática é estritamente prospectiva e consome exclusivamente a DB_DISPONIBILIDADE_DECLARADA [1]. Nenhuma presença histórica ou factual de DB_PRESENCA é utilizada para simular disponibilidades futuras [1]. Junção Segura por ID (tactical_positions_join_key): Nomes de jogadoras são tratados como rótulos mutáveis. Todos os joins internos para relacionar disponibilidades e posições utilizam obrigatoriamente a chave primária imutável athlete_id [1, 2]. Isolamento de Visibilidade: Por decisão de governança, os diagnósticos de gargalos e cobertura tática são mantidos como visualização restrita da comissão técnica no banco de dados e não são expostos no frontend público das atletas [1].

Com o detalhamento de DB_DISPONIBILIDADE_POSICAO, concluímos a análise de toda a cadeia tática e relacional do CEPRAEA!

Regras IHF As regras oficiais da IHF (Regras de Handebol de Praia 2026 e as Atualizações de 2026) exercem um impacto direto e vinculante na modelagem do banco de dados do CEPRAEA [1-3]. Elas definem os limites de integridade, os domínios de enums, as regras de derivação do placar e a validação do scout.

Abaixo estão os principais pontos onde essas fontes regulamentam e travam a estrutura das tabelas relacionais do sistema:

1.  Restrição de Elegibilidade e Limites por Partida (DB_CONVOCACOES e DB_PARTICIPACAO_JOGO) Regra IHF 4.2 e 4.3: Uma equipe é composta por até 10 jogadoras em súmula por partida, com no máximo 4 jogadoras em quadra (3 de linha e 1 goleira) [4-6]. Impacto na Modelagem: Na tabela DB_CONVOCACOES, o atributo atletas_por_partida_max é fixado estritamente no valor 10 [4, 5]. Na tabela associativa DB_PARTICIPACAO_JOGO, o banco valida a cardinalidade de no máximo 10 registros ativos com status_participacao = JOGOU por partida. Quando a relação nominal da etapa possui 12 convocadas, o sistema aplica deterministicamente a regra TWO_EXCLUDED_OF_TWELVE para marcar as 2 ausentes da súmula (NAO_JOGOU).
2.  Validação da Pontuação e Derivação do Placar (DB_FINALIZACOES e DB_JOGOS) Regra IHF 9.2, 9.3, 9.6 e 9.7–9.8: 2 Pontos: Gols criativos/espetaculares (giro 360° e ponte aérea), gols marcados pela goleira ou especialista e gols de tiro de 6 metros [7-10]. 1 Ponto: Gols simples de linha e gols contra [7, 9, 11, 12]. Estrutura de Partida: O jogo é composto por 2 períodos independentes de 10 minutos [13, 14]. Se um período terminar empatado, joga-se o Gol de Ouro [8, 10, 14, 15]; se cada equipe vencer um período (1 x 1), a partida é decidida no Shoot-out [14-17]. Impacto na Modelagem: Em DB_FINALIZACOES, o campo pontos_atribuidos é travado no domínio de inteiros (0, 1, 2). Em DB_JOGOS, a tabela implementa os atributos estruturados set1_cepraea, set1_adversario, set2_cepraea, set2_adversario, shootout_cepraea e shootout_adversario. A vitória (vitoria_cepraea) e o saldo de sets são derivados automaticamente por fórmulas relacionais, impedindo alterações manuais que violem a regra oficial da IHF.
3.  Sanção Automática para Arremesso na Cabeça da Goleira (DB_FINALIZACOES e DB_GOLEIRA_ACOES) Regra IHF 16.2j (Atualização 2026): Em situações de jogo aberto (sem defensora entre a arremessadora e a baliza), se o arremesso de uma jogadora livre atingir primeiramente a cabeça da goleira, a exclusão do arremessador é obrigatória [18-20]. Se a goleira simular o contato, a goleira deve ser punida [18-20]. Impacto na Modelagem: O módulo de scout de arremessos requer os atributos booleanos e enums: situacao_jogo_aberto (SIM/NAO), primeiro_contato_cabeca_gk (SIM/NAO) e sancao_disparada (EXCLUSAO_ATACANTE, PUNICAO_SIMULACAO_GK, NENHUMA), conectando a codificação de vídeo ao registro disciplinar do jogo.
4.  Punições Especiais nos Últimos 15 Segundos / Gol de Ouro (DB_JOGOS e DB_EVENTOS_TACTICOS) Regra IHF 8.11a e 8.11b (Atualização 2026): Qualquer interferência antidesportiva ou atraso na cobrança de um tiro nos últimos 15 segundos de qualquer período ou durante o Gol de Ouro acarreta Desqualificação Direta + Tiro de 6 Metros para a equipe adversária [20-25]. Impacto na Modelagem: Exige que os eventos de cronômetro registrem os metadados tempo_restante_periodo e is_golden_goal, permitindo ao banco auditar se uma desqualificação nos minutos finais atendeu aos critérios do artigo 8:11.
5.  Controle de Jogo Passivo e Limite de 4 Passes (DB_POSSES e DB_BOU) Regra IHF 7.10 e 7.11 (Atualização 2026): É proibido atrasar repetidamente a recolocação da bola em jogo [26-28]. Após a exibição do sinal de advertência de jogo passivo (Gesto 16), a equipe tem no máximo 4 passes para realizar um arremesso ao gol, sob pena de perda de posse por tiro livre [28-30]. Impacto na Modelagem: Na tabela de Unidades Básicas de Ataque (DB_BOU) e DB_EVENTOS_TACTICOS, a contagem de passes pós-advertência é auditada para validar a variável causa_fim_posse = FIM_PASSIVO.