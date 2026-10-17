-- =============================================================================
-- 06 — MIGRATIONS VERSIONADAS E ROLLBACK — CEPRAEA BEACH HANDBALL PRO
-- =============================================================================
-- Supabase / PostgreSQL Migration Pipeline
-- Version: 20261013000001
-- =============================================================================

-- [UP MIGRATION 001: Initial Core Setup]
BEGIN;

CREATE TABLE IF NOT EXISTS public.schema_migrations (
    version VARCHAR(30) PRIMARY KEY,
    description TEXT NOT NULL,
    applied_at TIMESTAMPTZ NOT NULL DEFAULT clock_timestamp()
);

INSERT INTO public.schema_migrations (version, description)
VALUES ('20261013000001', 'Initial core tables for CEPRAEA Beach Handball Pro')
ON CONFLICT (version) DO NOTHING;

COMMIT;

-- [DOWN / ROLLBACK MIGRATION 001]
/*
BEGIN;
DROP TABLE IF EXISTS public.goalkeeper_actions CASCADE;
DROP TABLE IF EXISTS public.finalizations CASCADE;
DROP TABLE IF EXISTS public.tactical_events CASCADE;
DROP TABLE IF EXISTS public.bous CASCADE;
DROP TABLE IF EXISTS public.possessions CASCADE;
DROP TABLE IF EXISTS public.match_appearances CASCADE;
DROP TABLE IF EXISTS public.matches CASCADE;
DROP TABLE IF EXISTS public.convocation_athletes CASCADE;
DROP TABLE IF EXISTS public.convocations CASCADE;
DROP TABLE IF EXISTS public.competitions CASCADE;
DROP TABLE IF EXISTS public.factual_presences CASCADE;
DROP TABLE IF EXISTS public.presence_proposals CASCADE;
DROP TABLE IF EXISTS public.availability_declarations CASCADE;
DROP TABLE IF EXISTS public.calendar_events CASCADE;
DROP TABLE IF EXISTS public.secondary_positions CASCADE;
DROP TABLE IF EXISTS public.athletes CASCADE;
DROP TABLE IF EXISTS public.changelog CASCADE;
DROP TABLE IF EXISTS public.system_config CASCADE;
DROP TABLE IF EXISTS public.provenance_records CASCADE;
DROP TABLE IF EXISTS public.schema_migrations CASCADE;

DROP TYPE IF EXISTS convocation_state_enum;
DROP TYPE IF EXISTS cepraea_participation_enum;
DROP TYPE IF EXISTS extent_type_enum;
DROP TYPE IF EXISTS presence_status_enum;
DROP TYPE IF EXISTS availability_response_enum;
DROP TYPE IF EXISTS app_event_status_enum;
DROP TYPE IF EXISTS app_event_type_enum;
DROP TYPE IF EXISTS app_position_enum;
DROP TYPE IF EXISTS app_function_enum;

DELETE FROM public.schema_migrations WHERE version = '20261013000001';
COMMIT;
*/
