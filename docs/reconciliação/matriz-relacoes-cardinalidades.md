# MATRIZ CONSOLIDADA DE RELAÇÕES E CARDINALIDADES — CEPRAEA BEACH HANDBALL PRO

**Estado:** APPROVED — Reconciliado com 04A (Modelo Conceitual) e 04B (Modelo Lógico).  
**Versão:** v1.0.0  
**Autoridade:** Davi Sermenho (`ROLE-CEPRAEA-DATA-GOVERNANCE-STEWARD`)

---

## 1. VISÃO GERAL DAS ASSOCIAÇÕES RELACIONAIS

O modelo físico do CEPRAEA Beach Handball Pro elimina ambiguidades através da especificação rigorosa de cardinalidades mínimas e máximas em **ambos os sentidos da relação**, acompanhadas das regras de integridade referencial (`ON DELETE RESTRICT` / `CASCADE`) e de isolamento de histórico.

---

## 2. MATRIZ DE CARDINALIDADES (AMBOS OS SENTIDOS)

| Entidade Origem (A) | Cardinalidade A -> B | Entidade Destino (B) | Cardinalidade B -> A | Tabela Associativa / FK Físico | Regra de Integridade Referencial (`ON DELETE`) |
| :--- | :---: | :--- | :---: | :--- | :--- |
| `public.athletes` | `1 ↔ 1` | `public.secondary_positions` | `1 ↔ 1` | `secondary_positions.athlete_id` (PK/FK) | `RESTRICT` — Impedir exclusão de atleta com versatilidade cadastrada. |
| `public.athletes` | `1 ↔ 0..N` | `public.availability_declarations` | `N ↔ 1` | `availability_declarations.athlete_id` (FK) | `RESTRICT` — Manter histórico imutável de declarações (`RN-DISP-004`). |
| `public.calendar_events` | `1 ↔ 0..N` | `public.availability_declarations` | `N ↔ 1` | `availability_declarations.event_id` (FK) | `RESTRICT` — Impedir exclusão de evento que possui declarações registradas. |
| `public.calendar_events` | `1 ↔ 0..N` | `public.presence_proposals` | `N ↔ 1` | `presence_proposals.event_id` (FK) | `RESTRICT` — Fila transitória vinculada ao evento (`DEC-DATA-045`). |
| `public.athletes` | `1 ↔ 0..N` | `public.presence_proposals` | `N ↔ 1` | `presence_proposals.athlete_id` (FK) | `RESTRICT` — Fila transitória vinculada à atleta. |
| `public.presence_proposals` | `0..1 ↔ 1` | `public.factual_presences` | `1 ↔ 0..1` | `factual_presences.proposal_id` (FK) | `SET NULL` — Presença factual confirmada sobrevive se proposta for arquivada. |
| `public.calendar_events` | `1 ↔ 0..N` | `public.factual_presences` | `N ↔ 1` | `factual_presences.event_id` (FK) | `RESTRICT` — Presença factual exige preservação absoluta de treino realizado. |
| `public.athletes` | `1 ↔ 0..N` | `public.factual_presences` | `N ↔ 1` | `factual_presences.athlete_id` (FK) | `RESTRICT` — Presença factual exige preservação absoluta de cadastro. |
| `public.competitions` | `1 ↔ 0..N` | `public.convocations` | `N ↔ 1` | `convocations.competition_id` (FK) | `RESTRICT` — Impedir exclusão de competição que possui convocação oficial. |
| `public.competitions` | `1 ↔ 0..N` | `public.matches` | `N ↔ 1` | `matches.competition_id` (FK) | `RESTRICT` — Impedir exclusão de competição que possui partidas realizadas. |
| `public.convocations` | `1 ↔ 0..12` | `public.athletes` (via `convocation_athletes`) | `N ↔ 1..N` | Tabela associativa `public.convocation_athletes` | `RESTRICT` (ambos os lados) — Relação nominal de 12 convocadas. |
| `public.matches` | `1 ↔ 0..10` | `public.athletes` (via `match_appearances`) | `N ↔ 1..N` | Tabela associativa `public.match_appearances` | `RESTRICT` (ambos os lados) — Roster ativo de 10 jogadoras por partida. |
| `public.convocations` | `1 ↔ 0..12` | `public.match_appearances` | `N ↔ 1` | `match_appearances.convocation_id` (FK) | `RESTRICT` — Convocação da etapa que originou a elegibilidade da atuação. |
| `public.matches` | `1 ↔ 0..N` | `public.possessions` | `N ↔ 1` | `possessions.match_id` (FK) | `CASCADE` — Deletar posses de scout se a partida for removida em ambiente de teste. |
| `public.possessions` | `1 ↔ 0..N` | `public.bous` | `N ↔ 1` | `bous.possession_id` (FK) | `CASCADE` — Deletar Unidades Básicas de Ataque vinculadas à posse. |
| `public.bous` | `1 ↔ 0..N` | `public.tactical_events` | `N ↔ 1` | `tactical_events.bou_id` (FK) | `CASCADE` — Deletar procedimentos táticos vinculados à BOU. |
| `public.bous` | `1 ↔ 0..N` | `public.finalizations` | `N ↔ 1` | `finalizations.bou_id` (FK) | `SET NULL` — Finalização em transição pode existir sem BOU. |
| `public.finalizations` | `1 ↔ 0..1` | `public.goalkeeper_actions` | `1 ↔ 1` | `goalkeeper_actions.finalization_id` (FK) | `CASCADE` — Ação de goleira atrelada à tentativa de arremesso. |
| `public.provenance_records` | `1 ↔ 0..N` | Todas as tabelas do sistema | `N ↔ 0..1` | Coluna `provenance_id` (FK) em cada tabela | `SET NULL` — A remoção de metadado de proveniência não apaga o dado esportivo. |

---

## 3. DECOMPOSIÇÃO DE RELACIONAMENTOS MUITOS-PARA-MUITOS (N:M)

### 3.1 `public.convocation_athletes` (Atletas Convocadas na Etapa)
- **Tabelas de Origem:** `public.convocations` × `public.athletes`.
- **Chave Composta:** `PRIMARY KEY (convocation_id, athlete_id)`.
- **Constraint de Negócio:** No máximo 12 atletas ativas por convocação de etapa.

### 3.2 `public.match_appearances` (Súmula de Partida e Participação Factual)
- **Tabelas de Origem:** `public.matches` × `public.athletes`.
- **Chave Composta:** `PRIMARY KEY (match_id, athlete_id)`.
- **Constraint de Negócio (`TWO_EXCLUDED_OF_TWELVE`):** No máximo 10 atletas com `participation_status = 'JOGOU'` por partida; exatamente 2 com `participation_status = 'NAO_JOGOU'` quando vindas de convocação nominal de 12.
