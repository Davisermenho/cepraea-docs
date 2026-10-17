-- =============================================================================
-- 05 — MODELO FÍSICO POSTGRESQL / SUPABASE — CEPRAEA BEACH HANDBALL PRO
-- =============================================================================
-- Estado: APPROVED — Reconciliado com 04A (Conceitual) e 04B (Lógico).
-- Fuso Horário Padrão: 'America/Sao_Paulo'
-- Compatibilidade: PostgreSQL 15+ / Supabase
-- =============================================================================

BEGIN;

-- 1. SCHEMAS E EXTENSÕES
CREATE SCHEMA IF NOT EXISTS public;
CREATE SCHEMA IF NOT EXISTS private;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Set timezone for the current transaction
SET LOCAL timezone = 'America/Sao_Paulo';

-- 2. TIPOS ENUMERADOS CANÔNICOS

DO $$ BEGIN
    CREATE TYPE app_function_enum AS ENUM ('DEFESA', 'ATAQUE', 'INDEFINIDA');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE app_position_enum AS ENUM (
        'GOLEIRA', 'CENTRAL', 'LATERAL_ESQUERDA', 'LATERAL_DIREITA', 'PIVO',
        'DEFENSORA_SOLTA', 'DEFENSORA_BASE', 'DEFENSORA_COBERTURA',
        'CENTRAL_DIREITA', 'CENTRAL_ESQUERDA', 'DEFENSORA_AVANCADA'
    );
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE app_event_type_enum AS ENUM ('TREINO', 'COMPETICAO', 'REUNIAO', 'OUTRO');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE app_event_status_enum AS ENUM (
        'PLANEJADO', 'REALIZADO', 'CANCELADO', 'ENCERRADO_SEM_CONFIRMACAO'
    );
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE availability_response_enum AS ENUM ('SIM', 'NAO', 'TALVEZ', 'SEM_RESPOSTA');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE presence_status_enum AS ENUM ('PRESENTE', 'AUSENTE', 'FALTA_JUSTIFICADA');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE extent_type_enum AS ENUM ('FULL', 'PARTIAL', 'NONE');
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE cepraea_participation_enum AS ENUM (
        'PARTICIPOU', 'PARTICIPARA', 'NAO_PARTICIPOU', 'NAO_PARTICIPARA',
        'CONVIDADO', 'CLASSIFICADO', 'A_CONFIRMAR'
    );
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

DO $$ BEGIN
    CREATE TYPE convocation_state_enum AS ENUM (
        'AGUARDANDO_PRAZO', 'ENVIADA', 'PRAZO_VENCIDO', 'NAO_DOCUMENTADA_NA_BASE', 'CANCELLED', 'SUPERSEDED'
    );
EXCEPTION WHEN duplicate_object THEN NULL; END $$;

-- 3. TABELAS DE GOVERNANÇA E PROVENIÊNCIA

CREATE TABLE IF NOT EXISTS public.provenance_records (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_document TEXT NOT NULL,
    provenance_level VARCHAR(10) NOT NULL CHECK (provenance_level IN ('P0','P1','P2','P3','A1','A2','A3','A4','D1')),
    epistemological_nature VARCHAR(20) NOT NULL CHECK (epistemological_nature IN ('FATO','DECLARACAO','PLANO','DECISAO','DERIVACAO','INFERENCIA')),
    recorded_by TEXT NOT NULL,
    recorded_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    metadata JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS public.system_config (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    notes TEXT,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.changelog (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    log_code VARCHAR(30) UNIQUE NOT NULL,
    executor TEXT NOT NULL,
    objective TEXT NOT NULL,
    tables_affected TEXT NOT NULL,
    changes_description TEXT NOT NULL,
    validations TEXT NOT NULL,
    status VARCHAR(30) NOT NULL CHECK (status IN ('executado', 'executado_validado', 'executado_com_pendencias', 'bloqueado')),
    executed_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

-- 4. DOMÍNIO DE ELENCO E POSIÇÕES

CREATE TABLE IF NOT EXISTS public.athletes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    athlete_code VARCHAR(20) UNIQUE NOT NULL,
    display_name TEXT NOT NULL,
    primary_function app_function_enum NOT NULL DEFAULT 'INDEFINIDA',
    primary_position app_position_enum NOT NULL,
    status_active BOOLEAN NOT NULL DEFAULT true,
    jersey_number INTEGER CHECK (jersey_number BETWEEN 1 AND 99),
    jersey_source TEXT,
    provenance_id UUID REFERENCES public.provenance_records(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.secondary_positions (
    athlete_id UUID PRIMARY KEY REFERENCES public.athletes(id) ON DELETE RESTRICT,
    secondary_position_1 app_position_enum,
    secondary_position_2 app_position_enum,
    secondary_position_3 app_position_enum,
    validation_status TEXT DEFAULT 'VALIDADO',
    authorized_by TEXT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

-- 5. DOMÍNIO OPERACIONAL, CALENDÁRIO E PRESENÇAS

CREATE TABLE IF NOT EXISTS public.calendar_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_code VARCHAR(30) UNIQUE NOT NULL,
    event_date DATE NOT NULL,
    event_type app_event_type_enum NOT NULL,
    start_time TIME,
    end_time TIME,
    location TEXT NOT NULL,
    event_status app_event_status_enum NOT NULL DEFAULT 'PLANEJADO',
    accepts_availability BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.availability_declarations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id UUID NOT NULL REFERENCES public.calendar_events(id) ON DELETE RESTRICT,
    athlete_id UUID NOT NULL REFERENCES public.athletes(id) ON DELETE RESTRICT,
    response availability_response_enum NOT NULL DEFAULT 'SEM_RESPOSTA',
    source_sheet TEXT NOT NULL,
    asserted_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    CONSTRAINT unique_event_athlete_availability UNIQUE (event_id, athlete_id)
);

CREATE TABLE IF NOT EXISTS public.presence_proposals (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id UUID NOT NULL REFERENCES public.calendar_events(id) ON DELETE RESTRICT,
    athlete_id UUID NOT NULL REFERENCES public.athletes(id) ON DELETE RESTRICT,
    self_reported_extent TEXT NOT NULL,
    proposed_extent extent_type_enum NOT NULL,
    derivation_state TEXT NOT NULL DEFAULT 'AGUARDANDO_CONFIRMACAO',
    coach_decision TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.factual_presences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id UUID NOT NULL REFERENCES public.calendar_events(id) ON DELETE RESTRICT,
    athlete_id UUID NOT NULL REFERENCES public.athletes(id) ON DELETE RESTRICT,
    presence_status presence_status_enum NOT NULL,
    participation_extent extent_type_enum NOT NULL,
    confirmed_by TEXT NOT NULL,
    confirmed_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    proposal_id UUID REFERENCES public.presence_proposals(id) ON DELETE SET NULL,
    CONSTRAINT unique_event_athlete_presence UNIQUE (event_id, athlete_id)
);

-- 6. DOMÍNIO COMPETITIVO E SÚMULAS

CREATE TABLE IF NOT EXISTS public.competitions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    competition_code VARCHAR(30) UNIQUE NOT NULL,
    name TEXT NOT NULL,
    organizer TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    location TEXT NOT NULL,
    event_status TEXT NOT NULL DEFAULT 'PREVISTA',
    cepraea_participation_status cepraea_participation_enum NOT NULL DEFAULT 'A_CONFIRMAR',
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.convocations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    convocation_code VARCHAR(30) UNIQUE NOT NULL,
    competition_id UUID NOT NULL REFERENCES public.competitions(id) ON DELETE RESTRICT,
    convocation_date DATE NOT NULL,
    submission_deadline DATE,
    convocation_status convocation_state_enum NOT NULL DEFAULT 'AGUARDANDO_PRAZO',
    max_stage_athletes INTEGER NOT NULL DEFAULT 12,
    max_match_athletes INTEGER NOT NULL DEFAULT 10,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.convocation_athletes (
    convocation_id UUID NOT NULL REFERENCES public.convocations(id) ON DELETE RESTRICT,
    athlete_id UUID NOT NULL REFERENCES public.athletes(id) ON DELETE RESTRICT,
    jersey_number INTEGER,
    status_participacao TEXT DEFAULT 'convocada_etapa',
    PRIMARY KEY (convocation_id, athlete_id)
);

CREATE TABLE IF NOT EXISTS public.matches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    match_code VARCHAR(30) UNIQUE NOT NULL,
    competition_id UUID NOT NULL REFERENCES public.competitions(id) ON DELETE RESTRICT,
    match_date DATE NOT NULL,
    match_stage_phase TEXT NOT NULL,
    team_a_name TEXT NOT NULL,
    team_b_name TEXT NOT NULL,
    cepraea_side TEXT NOT NULL CHECK (cepraea_side IN ('EQUIPE_A', 'EQUIPE_B')),
    set1_cepraea INTEGER CHECK (set1_cepraea >= 0),
    set1_opponent INTEGER CHECK (set1_opponent >= 0),
    set2_cepraea INTEGER CHECK (set2_cepraea >= 0),
    set2_opponent INTEGER CHECK (set2_opponent >= 0),
    shootout_cepraea INTEGER CHECK (shootout_cepraea >= 0),
    shootout_opponent INTEGER CHECK (shootout_opponent >= 0),
    sets_won_cepraea INTEGER GENERATED ALWAYS AS (
        (CASE WHEN set1_cepraea > set1_opponent THEN 1 ELSE 0 END) +
        (CASE WHEN set2_cepraea > set2_opponent THEN 1 ELSE 0 END) +
        (CASE WHEN shootout_cepraea > shootout_opponent THEN 1 ELSE 0 END)
    ) STORED,
    sets_won_opponent INTEGER GENERATED ALWAYS AS (
        (CASE WHEN set1_opponent > set1_cepraea THEN 1 ELSE 0 END) +
        (CASE WHEN set2_opponent > set2_cepraea THEN 1 ELSE 0 END) +
        (CASE WHEN shootout_opponent > shootout_cepraea THEN 1 ELSE 0 END)
    ) STORED,
    cepraea_victory BOOLEAN GENERATED ALWAYS AS (
        ((CASE WHEN set1_cepraea > set1_opponent THEN 1 ELSE 0 END) +
         (CASE WHEN set2_cepraea > set2_opponent THEN 1 ELSE 0 END) +
         (CASE WHEN shootout_cepraea > shootout_opponent THEN 1 ELSE 0 END)) >
        ((CASE WHEN set1_opponent > set1_cepraea THEN 1 ELSE 0 END) +
         (CASE WHEN set2_opponent > set2_cepraea THEN 1 ELSE 0 END) +
         (CASE WHEN shootout_opponent > shootout_cepraea THEN 1 ELSE 0 END))
    ) STORED,
    match_status TEXT NOT NULL DEFAULT 'PLANEJADO',
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.match_appearances (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    match_id UUID NOT NULL REFERENCES public.matches(id) ON DELETE RESTRICT,
    athlete_id UUID NOT NULL REFERENCES public.athletes(id) ON DELETE RESTRICT,
    convocation_id UUID NOT NULL REFERENCES public.convocations(id) ON DELETE RESTRICT,
    participation_status TEXT NOT NULL CHECK (participation_status IN ('JOGOU', 'NAO_JOGOU')),
    stepped_on_court BOOLEAN,
    role_in_match app_function_enum DEFAULT 'INDEFINIDA',
    CONSTRAINT unique_match_athlete_appearance UNIQUE (match_id, athlete_id)
);

-- 7. DOMÍNIO DE SCOUT OBSERVACIONAL

CREATE TABLE IF NOT EXISTS public.possessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    possession_code VARCHAR(30) UNIQUE NOT NULL,
    match_id UUID NOT NULL REFERENCES public.matches(id) ON DELETE CASCADE,
    possession_team TEXT NOT NULL CHECK (possession_team IN ('CEPRAEA', 'ADVERSARIO')),
    origin_type TEXT NOT NULL,
    start_timecode VARCHAR(20),
    end_timecode VARCHAR(20),
    end_reason TEXT NOT NULL DEFAULT 'FIM_IND',
    points_scored INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.bous (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bou_code VARCHAR(30) UNIQUE NOT NULL,
    possession_id UUID NOT NULL REFERENCES public.possessions(id) ON DELETE CASCADE,
    offensive_structure TEXT NOT NULL DEFAULT 'OF_IND',
    specialist_athlete_id UUID REFERENCES public.athletes(id) ON DELETE SET NULL,
    initial_defensive_structure TEXT NOT NULL DEFAULT 'DEF_IND',
    final_defensive_structure TEXT NOT NULL DEFAULT 'DEF_IND',
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.tactical_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bou_id UUID NOT NULL REFERENCES public.bous(id) ON DELETE CASCADE,
    event_order INTEGER NOT NULL CHECK (event_order >= 1),
    tactical_procedure TEXT NOT NULL DEFAULT 'PT_IND',
    executor_athlete_id UUID REFERENCES public.athletes(id) ON DELETE SET NULL,
    receiver_athlete_id UUID REFERENCES public.athletes(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.finalizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bou_id UUID REFERENCES public.bous(id) ON DELETE SET NULL,
    finalizer_athlete_id UUID REFERENCES public.athletes(id) ON DELETE SET NULL,
    origin_zone TEXT NOT NULL DEFAULT 'ZIND',
    target_zone TEXT NOT NULL DEFAULT 'ALVO_IND',
    finalization_type TEXT NOT NULL DEFAULT 'FIN_IND',
    result TEXT NOT NULL DEFAULT 'IND',
    points_awarded INTEGER NOT NULL CHECK (points_awarded IN (0, 1, 2)),
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

CREATE TABLE IF NOT EXISTS public.goalkeeper_actions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    finalization_id UUID NOT NULL REFERENCES public.finalizations(id) ON DELETE CASCADE,
    goalkeeper_athlete_id UUID REFERENCES public.athletes(id) ON DELETE SET NULL,
    defensive_action TEXT NOT NULL DEFAULT 'GK_IND',
    forward_depth BOOLEAN DEFAULT false,
    subsequent_action TEXT DEFAULT 'IND',
    created_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

-- 8. ÍNDICES DE DESEMPENHO E PERFORMANCE

CREATE INDEX IF NOT EXISTS idx_athletes_primary_pos ON public.athletes (primary_position);
CREATE INDEX IF NOT EXISTS idx_events_date ON public.calendar_events (event_date);
CREATE INDEX IF NOT EXISTS idx_avail_declarations_event_ath ON public.availability_declarations (event_id, athlete_id);
CREATE INDEX IF NOT EXISTS idx_factual_presences_event_ath ON public.factual_presences (event_id, athlete_id);
CREATE INDEX IF NOT EXISTS idx_matches_comp_date ON public.matches (competition_id, match_date);
CREATE INDEX IF NOT EXISTS idx_match_appearances_match_ath ON public.match_appearances (match_id, athlete_id);
CREATE INDEX IF NOT EXISTS idx_possessions_match ON public.possessions (match_id);
CREATE INDEX IF NOT EXISTS idx_bous_possession ON public.bous (possession_id);

COMMIT;
