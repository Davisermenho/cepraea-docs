-- =============================================================================
-- 08 — SEEDS EXCLUSIVAMENTE SIMULADOS — CEPRAEA BEACH HANDBALL PRO
-- =============================================================================
-- Dados anonimizados/simulados para validação de testes e integridade
-- =============================================================================

BEGIN;

-- 1. PROVENIÊNCIA E CONFIGURAÇÃO
INSERT INTO public.provenance_records (id, source_document, provenance_level, epistemological_nature, recorded_by)
VALUES 
    ('11111111-1111-1111-1111-111111111111', 'DB_CONFIG_INITIAL_SEED', 'P1', 'DECISAO', 'Davi Sermenho'),
    ('22222222-2222-2222-2222-222222222222', 'SCOUT_PILOT_TEST_MATCH', 'P1', 'FATO', 'O01 — Davi Sermenho')
ON CONFLICT DO NOTHING;

-- 2. ATLETAS SIMULADAS
INSERT INTO public.athletes (id, athlete_code, display_name, primary_function, primary_position, status_active, jersey_number)
VALUES 
    ('a0000000-0000-0000-0000-000000000001', 'ATH-0001', 'Atleta Alpha', 'ATAQUE', 'CENTRAL', true, 10),
    ('a0000000-0000-0000-0000-000000000002', 'ATH-0002', 'Atleta Beta', 'ATAQUE', 'LATERAL_DIREITA', true, 8),
    ('a0000000-0000-0000-0000-000000000003', 'ATH-0003', 'Atleta Gamma', 'DEFESA', 'DEFENSORA_BASE', true, 3),
    ('a0000000-0000-0000-0000-000000000004', 'ATH-0004', 'Atleta Delta', 'DEFESA', 'GOLEIRA', true, 85)
ON CONFLICT (athlete_code) DO NOTHING;

-- 3. CALENDÁRIO SIMULADO
INSERT INTO public.calendar_events (id, event_code, event_date, event_type, start_time, end_time, location, event_status, accepts_availability)
VALUES 
    ('e0000000-0000-0000-0000-000000000001', 'TRN-2026-08-06', '2026-08-06', 'TREINO', '20:00', '21:30', 'Praia de Copacabana - Posto 4', 'REALIZADO', true),
    ('e0000000-0000-0000-0000-000000000002', 'TRN-2026-08-13', '2026-08-13', 'TREINO', '20:00', '21:30', 'Praia de Copacabana - Posto 4', 'PLANEJADO', true)
ON CONFLICT (event_code) DO NOTHING;

-- 4. DISPONIBILIDADES DECLARADAS (RN-DISP-001..017)
INSERT INTO public.availability_declarations (event_id, athlete_id, response, source_sheet)
VALUES 
    ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000001', 'SIM', 'AGOSTO_2026'),
    ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000002', 'SIM', 'AGOSTO_2026'),
    ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000003', 'SIM', 'AGOSTO_2026'),
    ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000004', 'NAO', 'AGOSTO_2026')
ON CONFLICT DO NOTHING;

-- 5. PRESENÇA FACTUAL HOMOLOGADA (DEC-DATA-045)
INSERT INTO public.factual_presences (event_id, athlete_id, presence_status, participation_extent, confirmed_by)
VALUES 
    ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000001', 'PRESENTE', 'FULL', 'Davi Sermenho — TREINADOR'),
    ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000002', 'PRESENTE', 'FULL', 'Davi Sermenho — TREINADOR'),
    ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000003', 'PRESENTE', 'PARTIAL', 'Davi Sermenho — TREINADOR')
ON CONFLICT DO NOTHING;

COMMIT;
