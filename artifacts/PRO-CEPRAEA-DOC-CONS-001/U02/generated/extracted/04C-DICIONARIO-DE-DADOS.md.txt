# 04C — DICIONÁRIO DE DADOS CANÔNICO — CEPRAEA BEACH HANDBALL PRO

**Estado:** APPROVED — Reconciliado com 04A (Modelo Conceitual) e 04B (Modelo Lógico).  
**Versão:** v1.0.0 (Físico PostgreSQL 15+ / Supabase)  
**Autoridade:** Davi Sermenho (`ROLE-CEPRAEA-DATA-GOVERNANCE-STEWARD`)  
**Fuso Horário:** `America/Sao_Paulo` (ISO 8601 com Offset)

---

## 1. INTRODUÇÃO E DIRETRIZES DE GOVERNANÇA

Este Dicionário de Dados Canônico documenta a camada física e relacional do sistema **CEPRAEA Beach Handball Pro**. Cada atributo é catalogado com seu nome físico, tipo de dado PostgreSQL, restrições de integridade, definição operacional, valores permitidos, tratamento de ausência/nulos, natureza epistemológica e proveniência/autoridade.

### Classes Epistemológicas

- **FATO:** Registro observado e verificado de acontecimento real (ex.: presença confirmada pós-treino, súmula de jogo).
- **DECLARAÇÃO:** Autorrelato ou manifestação prospectiva de intenção (ex.: disponibilidade declarada, formulário Wellness).
- **PLANO:** Prescrição ou programação futura humana (ex.: plano de sessão, convocação em rascunho).
- **DECISÃO:** Ato formal de autoridade humana que homologa ou altera um estado (ex.: confirmação do treinador, reclassificação).
- **DERIVAÇÃO:** Métrica ou indicador recomputado deterministicamente por fórmula/algoritmo sem intervenção manual.
- **INFERÊNCIA:** Leitura ou interpretação analítica hipotética (nunca promovida a Fato sem evidência).

---

## 2. ESQUEMA DE TABELAS E ATRIBUTOS

### 2.1 TABELA: `public.athletes` (Cadastro Canônico de Atletas)
- **Descrição:** Cadastro mestre imutável do elenco do CEPRAEA.
- **Unidade de Análise:** 1 Linha = 1 Atleta Cadastrada.
- **Chave Primária:** `id` (UUID).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Identificador único atemporal da atleta. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sistema |
| `athlete_code` | `VARCHAR(20)` | `UNIQUE, NOT NULL` | Chave legada estável no formato `ATH-XXXX`. | `ATH-0001` a `ATH-9999` | Proibido (`NOT NULL`) | Identidade | Cadastro Oficial |
| `display_name` | `TEXT` | `NOT NULL` | Nome operacional de exibição visual. | Texto Livre Normalizado | Proibido (`NOT NULL`) | Rótulo | Relação Nominal |
| `primary_function` | `app_function_enum` | `NOT NULL` | Macrofunção tática primária cadastrada. | `'DEFESA'`, `'ATAQUE'`, `'INDEFINIDA'` | Default `'INDEFINIDA'` | Decisão Técnica | `DB_ATLETAS.funcao_principal` |
| `primary_position` | `app_position_enum` | `NOT NULL` | Posição tática principal de atuação. | `GOLEIRA`, `CENTRAL`, `LATERAL_ESQUERDA`, `LATERAL_DIREITA`, `PIVO`, `DEFENSORA_SOLTA`, `DEFENSORA_BASE`, `DEFENSORA_COBERTURA`, `CENTRAL_DIREITA`, `CENTRAL_ESQUERDA`, `DEFENSORA_AVANCADA` | Proibido (`NOT NULL`) | Decisão Técnica | `DB_ATLETAS.posicao_principal` |
| `status_active` | `BOOLEAN` | `NOT NULL, DEFAULT true` | Indica se compõe o elenco ativo do clube. | `true`, `false` | Default `true` | Estado Cadastral | Comissão Técnica |
| `jersey_number` | `INTEGER` | `CHECK (jersey_number BETWEEN 1 AND 99)` | Número do uniforme registrado na federação. | `1` a `99` ou `NULL` | Permitido (`NULL`) | Rótulo Contextual | Boletim Oficial FHERJ/CBHb |
| `jersey_source` | `TEXT` | — | Rastreabilidade do número de camisa. | Citação do documento/boletim | Permitido (`NULL`) | Proveniência | Registro de Origem |
| `provenance_id` | `UUID` | `FK -> public.provenance_records(id)` | Vínculo de rastreabilidade de origem. | UUID válido | Permitido (`NULL`) | Proveniência | Grafo de Proveniência |
| `created_at` | `TIMESTAMPTZ` | `NOT NULL, DEFAULT clock_timestamp()` | Data/hora estática de criação no banco. | ISO 8601 com fuso | Default `clock_timestamp()` | Auditoria | Sistema |
| `updated_at` | `TIMESTAMPTZ` | `NOT NULL, DEFAULT clock_timestamp()` | Data/hora estática da última alteração. | ISO 8601 com fuso | Default `clock_timestamp()` | Auditoria | Sistema |

---

### 2.2 TABELA: `public.secondary_positions` (Versatilidade Tática)
- **Descrição:** Registra a versatilidade e as posições alternativas autorizadas pelo treinador.
- **Unidade de Análise:** 1 Linha = Atribuição de Versatilidade por Atleta.
- **Chave Primária:** `athlete_id` (1:1 com `public.athletes`).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `athlete_id` | `UUID` | `PK, FK -> public.athletes(id) ON DELETE RESTRICT` | Identificador da atleta vinculada. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.athletes.id` |
| `secondary_position_1` | `app_position_enum` | — | Primeira posição alternativa autorizada. | Enum `app_position_enum` | Permitido (`NULL`) | Decisão Técnica | `DB_POSICOES_SECUNDARIAS` |
| `secondary_position_2` | `app_position_enum` | — | Segunda posição alternativa autorizada. | Enum `app_position_enum` | Permitido (`NULL`) | Decisão Técnica | `DB_POSICOES_SECUNDARIAS` |
| `secondary_position_3` | `app_position_enum` | — | Terceira posição alternativa autorizada. | Enum `app_position_enum` | Permitido (`NULL`) | Decisão Técnica | `DB_POSICOES_SECUNDARIAS` |
| `validation_status` | `TEXT` | `DEFAULT 'VALIDADO'` | Status de homologação humana. | `'VALIDADO'`, `'PENDENTE'` | Default `'VALIDADO'` | Governança | Controle de Qualidade |
| `authorized_by` | `TEXT` | `NOT NULL` | Rastreabilidade da decisão humana. | Texto explicativo da decisão | Proibido (`NOT NULL`) | Proveniência | Homologação do Treinador |
| `updated_at` | `TIMESTAMPTZ` | `NOT NULL, DEFAULT clock_timestamp()` | Carimbo estático de alteração. | ISO 8601 com fuso | Default `clock_timestamp()` | Auditoria | Sistema |

---

### 2.3 TABELA: `public.calendar_events` (Grade Canônica de Agendas e Eventos)
- **Descrição:** Grade oficial de treinos, competições e reuniões.
- **Unidade de Análise:** 1 Linha = 1 Evento no Calendário.
- **Chave Primária:** `id` (UUID).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Chave única do evento. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sistema |
| `event_code` | `VARCHAR(30)` | `UNIQUE, NOT NULL` | Código canônico do evento. | `TRN-YYYY-MM-DD` ou `CAL-YYYY-MM-DD` | Proibido (`NOT NULL`) | Identidade | Cadastro de Agenda |
| `event_date` | `DATE` | `NOT NULL` | Data civil do evento (fuso `America/Sao_Paulo`). | Data válida `YYYY-MM-DD` | Proibido (`NOT NULL`) | Agenda | Calendário CEPRAEA |
| `event_type` | `app_event_type_enum` | `NOT NULL` | Classificação do evento. | `'TREINO'`, `'COMPETICAO'`, `'REUNIAO'`, `'OUTRO'` | Proibido (`NOT NULL`) | Taxonomia | Comissão Técnica |
| `start_time` | `TIME` | — | Horário oficial de início. | `HH:MM:SS` | Permitido (`NULL`) | Agenda | Tabela Oficial |
| `end_time` | `TIME` | — | Horário oficial de término. | `HH:MM:SS` | Permitido (`NULL`) | Agenda | Tabela Oficial |
| `location` | `TEXT` | `NOT NULL` | Ponto físico de realização. | Texto livre (ex.: "Praia de Copacabana") | Proibido (`NOT NULL`) | Logística | Comissão Técnica |
| `event_status` | `app_event_status_enum` | `NOT NULL, DEFAULT 'PLANEJADO'` | Estado corrente no ciclo de vida. | `'PLANEJADO'`, `'REALIZADO'`, `'CANCELADO'`, `'ENCERRADO_SEM_CONFIRMACAO'` | Default `'PLANEJADO'` | Ciclo de Vida | `DB_CONFIG` / Treinador |
| `accepts_availability` | `BOOLEAN` | `NOT NULL, DEFAULT true` | Flag de autorização para disponibilidade (`RN-DISP-013`). | `true`, `false` | Default `true` | Regra de Negócio | `DB_CONFIG` |

---

### 2.4 TABELA: `public.availability_declarations` (Declarações do Elenco — RN-DISP-001 a 017)
- **Descrição:** Registro de intenções e disponibilidades prospectivas declaradas pelas atletas nas abas mensais.
- **Unidade de Análise:** 1 Linha = 1 Declaração da Atleta por Evento.
- **Chave Primária:** `id` (UUID).
- **Unicidade Composta:** `UNIQUE (event_id, athlete_id)` (Regras `RN-DISP-004` e `RN-DISP-008`).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Identificador do registro. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sincronizador |
| `event_id` | `UUID` | `FK -> public.calendar_events(id) ON DELETE RESTRICT` | Evento alvo (`RN-DISP-013`). | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.calendar_events.id` |
| `athlete_id` | `UUID` | `FK -> public.athletes(id) ON DELETE RESTRICT` | Identidade canônica da atleta (`RN-DISP-003`). | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.athletes.id` |
| `response` | `availability_response_enum` | `NOT NULL` | Declaração normalizada (`RN-DISP-005`/`016`). | `'SIM'`, `'NAO'`, `'TALVEZ'`, `'SEM_RESPOSTA'` | Blank vira `'SEM_RESPOSTA'` (`RN-DISP-006`) | Autorrelato | Entrada Humana Frontend |
| `source_sheet` | `TEXT` | `NOT NULL` | Rastreabilidade da aba-fonte (`RN-DISP-002`). | Nome da aba (ex.: `'AGOSTO_2026'`) | Proibido (`NOT NULL`) | Proveniência | Sincronizador |
| `asserted_at` | `TIMESTAMPTZ` | `NOT NULL, DEFAULT clock_timestamp()` | Timestamp da declaração da atleta. | ISO 8601 com fuso | Default `clock_timestamp()` | Auditoria | Sistema |
| `updated_at` | `TIMESTAMPTZ` | `NOT NULL, DEFAULT clock_timestamp()` | Timestamp de atualização do estado corrente. | ISO 8601 com fuso | Default `clock_timestamp()` | Auditoria | Sistema |

---

### 2.5 TABELA: `public.presence_proposals` (Fila Transitória de Presença — DEC-DATA-045)
- **Descrição:** Fila transitória de propostas de presença derivadas de formulários pós-treino (Wellness Pós).
- **Unidade de Análise:** 1 Linha = 1 Proposta de Presença Autorrelatada.
- **Chave Primária:** `id` (UUID).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Chave única da proposta. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Form Wellness Pós |
| `event_id` | `UUID` | `FK -> public.calendar_events(id) ON DELETE RESTRICT` | Treino realizado. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | Resposta do Form |
| `athlete_id` | `UUID` | `FK -> public.athletes(id) ON DELETE RESTRICT` | Atleta respondente. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | Resposta do Form |
| `self_reported_extent` | `TEXT` | `NOT NULL` | Declaração da atleta sobre extensão no treino. | `'COMPLETA'`, `'PARCIAL'` | Proibido (`NOT NULL`) | Autorrelato | Resposta do Form |
| `proposed_extent` | `extent_type_enum` | `NOT NULL` | Mapeamento técnico (`COMPLETA`->`FULL`, `PARCIAL`->`PARTIAL`). | `'FULL'`, `'PARTIAL'` | Proibido (`NOT NULL`) | Mapeamento | Regra `DEC-DATA-045` |
| `derivation_state` | `TEXT` | `NOT NULL, DEFAULT 'AGUARDANDO_CONFIRMACAO'` | Estado de tramitação na fila do treinador. | `'AGUARDANDO_CONFIRMACAO'`, `'CONFIRMADA_MATERIALIZADA'`, `'REJEITADA'` | Default `'AGUARDANDO_CONFIRMACAO'` | Tramitação | Painel do Treinador |
| `coach_decision` | `TEXT` | — | Ação tomada pela autoridade técnica. | `'CONFIRMAR_PROPOSTA'`, `'AJUSTAR_FULL'`, `'AJUSTAR_PARTIAL'`, `'REJEITAR_PROPOSTA'` | Permitido (`NULL`) enquanto aguarda | Decisão Humana | Treinador CEPRAEA |

---

### 2.6 TABELA: `public.factual_presences` (SSOT Canônica de Presença Factual — DEC-DATA-045)
- **Descrição:** A ÚNICA Fonte Primária de Verdade para presenças factuais ocorridas. Nenhuma linha é criada sem homologação humana do treinador.
- **Unidade de Análise:** 1 Linha = 1 Presença Factual Confirmada por Atleta/Treino.
- **Chave Primária:** `id` (UUID).
- **Unicidade Composta:** `UNIQUE (event_id, athlete_id)`.

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Chave única da presença factual. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sistema |
| `event_id` | `UUID` | `FK -> public.calendar_events(id) ON DELETE RESTRICT` | Treino realizado. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.calendar_events.id` |
| `athlete_id` | `UUID` | `FK -> public.athletes(id) ON DELETE RESTRICT` | Atleta presente. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.athletes.id` |
| `presence_status` | `presence_status_enum` | `NOT NULL` | Fato esportivo do comparecimento. | `'PRESENTE'`, `'AUSENTE'`, `'FALTA_JUSTIFICADA'` | Proibido (`NOT NULL`) | Fato Esportivo | Homologação do Treinador |
| `participation_extent` | `extent_type_enum` | `NOT NULL` | Extensão da participação real no treino. | `'FULL'`, `'PARTIAL'`, `'NONE'` | Proibido (`NOT NULL`) | Fato Esportivo | Homologação do Treinador |
| `confirmed_by` | `TEXT` | `NOT NULL` | Identificação da autoridade que homologou. | Nome e papel (ex.: "Davi Sermenho — TREINADOR") | Proibido (`NOT NULL`) | Auditoria | Registro do Treinador |
| `confirmed_at` | `TIMESTAMPTZ` | `NOT NULL, DEFAULT clock_timestamp()` | Carimbo exato de data/hora da homologação. | ISO 8601 com fuso | Default `clock_timestamp()` | Auditoria | Sistema |
| `proposal_id` | `UUID` | `FK -> public.presence_proposals(id)` | Rastreabilidade da proposta que originou o fato. | UUID válido | Permitido (`NULL`) | Proveniência | `public.presence_proposals.id` |

---

### 2.7 TABELA: `public.competitions` (Cadastro Mestre de Campeonatos e Etapas)
- **Descrição:** Cadastro mestre dos campeonatos e etapas disputados pelo clube.
- **Unidade de Análise:** 1 Linha = 1 Competição / Etapa.
- **Chave Primária:** `id` (UUID).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Chave única da competição. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sistema |
| `competition_code` | `VARCHAR(30)` | `UNIQUE, NOT NULL` | Código canônico. | `COMP-YYYY-XXX` | Proibido (`NOT NULL`) | Identidade | Boletim Oficial |
| `name` | `TEXT` | `NOT NULL` | Nome oficial do torneio. | Texto livre normalizado | Proibido (`NOT NULL`) | Cadastro | Regulamento/Boletim |
| `organizer` | `TEXT` | `NOT NULL` | Entidade organizadora. | `'CBHb'`, `'FHERJ'`, `'IHF'`, `'OUTRO'` | Proibido (`NOT NULL`) | Organização | Regulamento do Evento |
| `start_date` | `DATE` | `NOT NULL` | Data inicial do torneio. | Data `YYYY-MM-DD` | Proibido (`NOT NULL`) | Agenda | Tabela Oficial |
| `end_date` | `DATE` | `NOT NULL` | Data final do torneio. | Data `YYYY-MM-DD` | Proibido (`NOT NULL`) | Agenda | Tabela Oficial |
| `location` | `TEXT` | `NOT NULL` | Cidade e Estado da sede. | Texto livre (ex.: "Niterói - RJ") | Proibido (`NOT NULL`) | Logística | Boletim da Sede |
| `event_status` | `TEXT` | `NOT NULL, DEFAULT 'PREVISTA'` | Estado do evento esportivo. | `'PREVISTA'`, `'REALIZADA'`, `'CANCELADA'` | Default `'PREVISTA'` | Ciclo do Evento | Boletins Oficiais |
| `cepraea_participation_status` | `cepraea_participation_enum` | `NOT NULL, DEFAULT 'A_CONFIRMAR'` | Relação do CEPRAEA com a competição. | `'PARTICIPOU'`, `'PARTICIPARA'`, `'NAO_PARTICIPOU'`, `'NAO_PARTICIPARA'`, `'CONVIDADO'`, `'CLASSIFICADO'`, `'A_CONFIRMAR'` | Default `'A_CONFIRMAR'` | Decisão do Clube | Confirmação da Comissão |

---

### 2.8 TABELA: `public.convocations` (Relações Nominais por Etapa)
- **Descrição:** Registro formal de convocação da relação nominal de 12 atletas para a etapa.
- **Unidade de Análise:** 1 Linha = 1 Convocação por Etapa.
- **Chave Primária:** `id` (UUID).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Chave única da convocação. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sistema |
| `convocation_code` | `VARCHAR(30)` | `UNIQUE, NOT NULL` | Código canônico. | `CONV-YYYY-XXX` | Proibido (`NOT NULL`) | Identidade | Protocolo |
| `competition_id` | `UUID` | `FK -> public.competitions(id) ON DELETE RESTRICT` | Competição vinculada. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.competitions.id` |
| `convocation_date` | `DATE` | `NOT NULL` | Data da convocação. | Data `YYYY-MM-DD` | Proibido (`NOT NULL`) | Agenda | Relação Nominal |
| `submission_deadline` | `DATE` | — | Data limite de envio à federação. | Data `YYYY-MM-DD` | Permitido (`NULL`) | Regulamento | Regulamento FHERJ/CBHb |
| `convocation_status` | `convocation_state_enum` | `NOT NULL, DEFAULT 'AGUARDANDO_PRAZO'` | Status do trâmite do documento. | `'AGUARDANDO_PRAZO'`, `'ENVIADA'`, `'PRAZO_VENCIDO'`, `'NAO_DOCUMENTADA_NA_BASE'` | Default `'AGUARDANDO_PRAZO'` | Governança | Protocolo de Envio |
| `max_stage_athletes` | `INTEGER` | `NOT NULL, DEFAULT 12` | Teto máximo de inscritas na etapa. | Default `12` | Proibido (`NOT NULL`) | Regulamento | Regulamento FHERJ/CBHb |
| `max_match_athletes` | `INTEGER` | `NOT NULL, DEFAULT 10` | Teto máximo em súmula por partida. | Default `10` (Regra IHF 4) | Proibido (`NOT NULL`) | Regulamento | Regra IHF 4 |

---

### 2.9 TABELA: `public.matches` (Súmulas e Resultados de Partidas)
- **Descrição:** Registro canônico de partidas disputadas pelo CEPRAEA com placar por set e shoot-out.
- **Unidade de Análise:** 1 Linha = 1 Partida do CEPRAEA.
- **Chave Primária:** `id` (UUID).

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Chave única da partida. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sistema |
| `match_code` | `VARCHAR(30)` | `UNIQUE, NOT NULL` | Código canônico. | `JOGO-YYYY-XXX` | Proibido (`NOT NULL`) | Identidade | Tabela de Jogos |
| `competition_id` | `UUID` | `FK -> public.competitions(id) ON DELETE RESTRICT` | Competição vinculada. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.competitions.id` |
| `match_date` | `DATE` | `NOT NULL` | Data real da partida. | Data `YYYY-MM-DD` | Proibido (`NOT NULL`) | Agenda | Súmula Oficial |
| `match_stage_phase` | `TEXT` | `NOT NULL` | Fase do torneio. | `'GRUPO'`, `'QUARTAS'`, `'SEMIFINAL'`, `'FINAL'`, `'DISPUTA_3_LUGAR'` | Proibido (`NOT NULL`) | Estrutura | Tabela Oficial |
| `team_a_name` | `TEXT` | `NOT NULL` | Nome da Equipe A em súmula. | Texto livre | Proibido (`NOT NULL`) | Súmula | Súmula Oficial |
| `team_b_name` | `TEXT` | `NOT NULL` | Nome da Equipe B em súmula. | Texto livre | Proibido (`NOT NULL`) | Súmula | Súmula Oficial |
| `cepraea_side` | `TEXT` | `NOT NULL, CHECK (cepraea_side IN ('EQUIPE_A', 'EQUIPE_B'))` | Posição nominal do CEPRAEA. | `'EQUIPE_A'`, `'EQUIPE_B'` | Proibido (`NOT NULL`) | Derivado | Mapeamento |
| `set1_cepraea` | `INTEGER` | `CHECK (set1_cepraea >= 0)` | Pontos CEPRAEA no Set 1. | Inteiro >= 0 | Permitido (`NULL`) | Placar | Súmula Oficial |
| `set1_opponent` | `INTEGER` | `CHECK (set1_opponent >= 0)` | Pontos adversário no Set 1. | Inteiro >= 0 | Permitido (`NULL`) | Placar | Súmula Oficial |
| `set2_cepraea` | `INTEGER` | `CHECK (set2_cepraea >= 0)` | Pontos CEPRAEA no Set 2. | Inteiro >= 0 | Permitido (`NULL`) | Placar | Súmula Oficial |
| `set2_opponent` | `INTEGER` | `CHECK (set2_opponent >= 0)` | Pontos adversário no Set 2. | Inteiro >= 0 | Permitido (`NULL`) | Placar | Súmula Oficial |
| `shootout_cepraea` | `INTEGER` | `CHECK (shootout_cepraea >= 0)` | Pontos CEPRAEA no Shoot-out. | Inteiro >= 0 | Permitido (`NULL`) | Placar | Súmula Oficial |
| `shootout_opponent` | `INTEGER` | `CHECK (shootout_opponent >= 0)` | Pontos adversário no Shoot-out. | Inteiro >= 0 | Permitido (`NULL`) | Placar | Súmula Oficial |
| `sets_won_cepraea` | `INTEGER` | `GENERATED ALWAYS AS (...) STORED` | Total de sets vencidos pelo CEPRAEA. | `0`, `1`, `2` | Gerado por Fórmula | Derivado | Cálculo Automático |
| `sets_won_opponent` | `INTEGER` | `GENERATED ALWAYS AS (...) STORED` | Total de sets vencidos pelo adversário. | `0`, `1`, `2` | Gerado por Fórmula | Derivado | Cálculo Automático |
| `cepraea_victory` | `BOOLEAN` | `GENERATED ALWAYS AS (...) STORED` | Flag de vitória do CEPRAEA. | `true`, `false` | Gerado por Fórmula | Derivado | Cálculo Automático |
| `match_status` | `TEXT` | `NOT NULL, DEFAULT 'PLANEJADO'` | Status de realização. | `'PLANEJADO'`, `'REALIZADA'`, `'CANCELADO'`, `'INVALIDADO'` | Default `'PLANEJADO'` | Governança | Homologação Humana |

---

### 2.10 TABELA: `public.match_appearances` (Atuação Factual por Jogo)
- **Descrição:** Materialização da atuação factual de cada atleta por partida individual.
- **Unidade de Análise:** 1 Linha = Atuação de 1 Atleta em 1 Jogo.
- **Chave Primária:** `id` (UUID).
- **Unicidade Composta:** `UNIQUE (match_id, athlete_id)`.

| Nome Coluna Físico | Tipo PostgreSQL | Restrições | Definição Operacional | Domínio / Valores Permitidos | Tratamento Vazio | Natureza Epistêmica | Fonte / Autoridade |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `id` | `UUID` | `PK, DEFAULT gen_random_uuid()` | Chave única da atuação. | UUID v4 | Proibido (`NOT NULL`) | Arquitetural | Sistema |
| `match_id` | `UUID` | `FK -> public.matches(id) ON DELETE RESTRICT` | Partida correspondente. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.matches.id` |
| `athlete_id` | `UUID` | `FK -> public.athletes(id) ON DELETE RESTRICT` | Atleta participante. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.athletes.id` |
| `convocation_id` | `UUID` | `FK -> public.convocations(id) ON DELETE RESTRICT` | Convocação que originou elegibilidade. | UUID válido | Proibido (`NOT NULL`) | Arquitetural | `public.convocations.id` |
| `participation_status` | `TEXT` | `NOT NULL, CHECK (participation_status IN ('JOGOU', 'NAO_JOGOU'))` | Fato de ter composto a súmula oficial de 10 atletas. | `'JOGOU'`, `'NAO_JOGOU'` | Proibido (`NOT NULL`) | Fato Esportivo | Regra `TWO_EXCLUDED_OF_TWELVE` / Súmula |
| `stepped_on_court` | `BOOLEAN` | — | Sinaliza se efetivamente pisou em quadra. | `true`, `false` | Permitido (`NULL`) | Scout | Súmula / Vídeo |
| `role_in_match` | `app_function_enum` | `DEFAULT 'INDEFINIDA'` | Função primária exercida no jogo. | Enum `app_function_enum` | Default `'INDEFINIDA'` | Tática | Leitura Técnica |
