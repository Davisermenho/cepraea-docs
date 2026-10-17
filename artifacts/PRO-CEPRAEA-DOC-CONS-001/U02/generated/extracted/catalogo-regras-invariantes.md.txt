# CATÁLOGO DE REGRAS DE NEGÓCIO E INVARIANTES — CEPRAEA BEACH HANDBALL PRO

**Estado:** APPROVED — Reconciliado com 04A (Modelo Conceitual), 04B (Modelo Lógico) e Regulamento IHF 2026.  
**Versão:** v1.0.0  
**Autoridade:** Davi Sermenho (`ROLE-CEPRAEA-DATA-GOVERNANCE-STEWARD`)

---

## 1. REGRAS DE NEGÓCIO NORMATIVAS DA SINCRONIZAÇÃO DE DISPONIBILIDADE (`RN-DISP-001` a `RN-DISP-017`)

* **`RN-DISP-001` (Declaração é Intenção, Não Presença):** Disponibilidade declarada ou compromisso expressa intenção prospectiva e JAMAIS constitui, promove ou substitui presença factual.
* **`RN-DISP-002` (Fonte Humana Exclusiva):** A declaração humana de disponibilidade nasce exclusivamente em células válidas das abas mensais do frontend.
* **`RN-DISP-003` (Identidade Canônica):** `athlete_id` (formato `ATH-XXXX` ou `UUID`) é a identidade canônica da atleta. Nomes e posições de linha são meros rótulos de exibição.
* **`RN-DISP-004` (Unicidade de Estado Corrente):** A identidade do estado corrente de disponibilidade é a chave composta `(event_id, athlete_id)`. Existe no máximo um registro corrente por essa chave.
* **`RN-DISP-005` (Domínio Estrito de Respostas):** Os estados canônicos permitidos são `'SIM'`, `'NAO'`, `'TALVEZ'` e `'SEM_RESPOSTA'`.
* **`RN-DISP-006` (Tratamento de Célula Vazia Mapeada):** Uma célula-fonte válida, mapeada e vazia representa `'SEM_RESPOSTA'` (nunca `'NAO'`).
* **`RN-DISP-007` (Evento sem Célula Mapeada):** Evento do calendário sem célula-fonte mapeada no frontend não gera registro e não pode ser convertido artificialmente em `'SEM_RESPOSTA'`.
* **`RN-DISP-008` (Operação de Upsert):** Quando a atleta altera sua declaração, o novo valor atualiza o mesmo estado corrente identificado por `(event_id, athlete_id)`, sem criar duplicatas concorrentes.
* **`RN-DISP-009` (Limpeza de Resposta):** Se uma resposta existente for apagada em célula-fonte válida, o estado corrente passa a `'SEM_RESPOSTA'` (não deleta a linha do banco).
* **`RN-DISP-010` (Fail-Closed na Resolução de Identidade):** Se atleta ou evento não puderem ser resolvidos de forma única, nenhuma escrita é permitida em `availability_declarations`. O caso deve falhar fechado (*Fail-Closed*).
* **`RN-DISP-011` (Invalidação por Mudança de Data):** Mudança material da data de um evento invalida o uso operacional da disponibilidade declarada para a data anterior; o histórico deve ser preservado e uma nova declaração recolhida.
* **`RN-DISP-012` (Filtragem de Visibilidade Operacional):** As agendas operacionais devem solicitar/exibir disponibilidade apenas de competições em que o CEPRAEA participará ou participou (`SOMENTE_PARTICIPACAO_CEPRAEA`).
* **`RN-DISP-013` (Elegibilidade do Evento):** Somente evento canônico com `accepts_availability = true` pode receber declaração pelo fluxo de disponibilidade.
* **`RN-DISP-014` (Imutabilidade do Estado do Evento pelo Sincronizador):** O sincronizador de disponibilidade não possui autoridade para alterar status/estado do evento no calendário.
* **`RN-DISP-015` (Isolamento entre Disponibilidade e Presença):** Nenhuma disponibilidade declarada ou autorrelato é promovido automaticamente a fato em `factual_presences`.
* **`RN-DISP-016` (Normalização de Entrada):** Normalização obrigatória de caixa e acentos (`TRIM`, caixa alta). Valores inválidos devem falhar sem escrita silenciosa.
* **`RN-DISP-017` (Expansão de Eventos Multidiários):** Quando uma única célula representa explicitamente uma competição multidiária, a declaração vale para todos os eventos diários canônicos pertencentes ao intervalo.

---

## 2. REGRAS DE PRESENÇA FACTUAL E WELLNESS PÓS (`DEC-DATA-045`)

* **`DEC-DATA-045.1` (Single Source of Truth de Presença):** A tabela `public.factual_presences` é a ÚNICA fonte de verdade para presenças factuais.
* **`DEC-DATA-045.2` (Fila Transitória):** As respostas do formulário *Wellness Pós-Treino* alimentam exclusivamente a tabela `public.presence_proposals` com estado `'AGUARDANDO_CONFIRMACAO'`.
* **`DEC-DATA-045.3` (Gate Humano do Treinador):** A conversão de proposta em presença factual exige a ação explícita e autenticada do treinador (`'CONFIRMAR_PROPOSTA'`, `'AJUSTAR_FULL'`, `'AJUSTAR_PARTIAL'`, `'REJEITAR_PROPOSTA'`).
* **`DEC-DATA-045.4` (Auditoria Mandatória):** Todo registro factual em `public.factual_presences` grava obrigatoriamente `confirmed_by` (nome e papel do treinador) e `confirmed_at` (timestamp estático).

---

## 3. REGRAS COMPETITIVAS E REGULAMENTARES (FHERJ / CBHb / IHF 2026)

* **`REG-IHF-001` (Súmula de Partida - Regra IHF 4):** Limite máximo de **10 jogadoras uniformizadas em súmula por partida**, com no máximo 4 jogadoras em quadra (3 de linha e 1 goleira).
* **`REG-IHF-002` (Regra `TWO_EXCLUDED_OF_TWELVE`):** Quando a convocação oficial da etapa contém 12 atletas, a comissão informa as 2 ausentes da partida (`participation_status = 'NAO_JOGOU'`); as outras 10 são materializadas como `'JOGOU'`.
* **`REG-IHF-003` (Validação de Pontuação de Partida):** Partida de handebol de praia é disputada em 2 sets independentes + Shoot-out em caso de empate (1 x 1). Vitória exige vencer 2 sets ou o Shoot-out. `sets_won_cepraea` e `cepraea_victory` são derivados deterministicamente por fórmula armazenada.
* **`SGATE-0023` / `DEC-DATA-042` (Pontuação FHERJ 2026):** Mapeamento de pontuação por etapa do Circuito Carioca 2026 validado para as posições 1ª a 7ª: `{1ª:16, 2ª:13, 3ª:11, 4ª:10, 5ª:9, 6ª:8, 7ª:7}`. O Artigo 25º da cópia armazenada está classificado como `STALE_FOR_SCORING`. Posições 8+ sem tabela validada retornam `INDETERMINATE`.

---

## 4. INVARIANTES DO BANCO DE DADOS E STOP GATES

1. **Invariante de Imutabilidade (*Append-Only*):** Registros de log (`public.changelog`), snapshots históricos de rankings e auditoria jamais sofrem `UPDATE` ou `DELETE`.
2. **Invariante de Semântica de Goleira (`goalkeeper_semantics`):** `GOLEIRA` é uma posição tática pertencente à macrofunção `DEFESA`, e não uma função isolada ou um grupo imutável de pessoas.
3. **Invariante de Bloqueio Físico (`implementation_blocked`):** Os objetos `SESSION_SEGMENT` e `PLANNED_TRAINING_LOAD` permanecem expressamente não persistíveis e bloqueados até nova homologação formal.
