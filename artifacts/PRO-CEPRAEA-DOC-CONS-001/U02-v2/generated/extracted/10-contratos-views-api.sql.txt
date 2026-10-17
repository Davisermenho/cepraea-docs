-- =============================================================================
-- 10 — CONTRATOS DE VIEWS E API EXPOSTA — CEPRAEA BEACH HANDBALL PRO
-- =============================================================================
-- Views de leitura segura expostas via Supabase Data API (security_invoker)
-- =============================================================================

BEGIN;

-- 1. VIEW: Resumo de Atletas e Versatilidade Tática
CREATE OR REPLACE VIEW public.v_athlete_tactical_summary
WITH (security_invoker = true)
AS
SELECT 
    a.id AS athlete_id,
    a.athlete_code,
    a.display_name,
    a.primary_function,
    a.primary_position,
    a.jersey_number,
    sp.secondary_position_1,
    sp.secondary_position_2,
    sp.secondary_position_3,
    a.status_active
FROM public.athletes a
LEFT JOIN public.secondary_positions sp ON a.id = sp.athlete_id
WHERE a.status_active = true;

-- 2. VIEW: Centro de Comando do Próximo Treino
CREATE OR REPLACE VIEW public.v_next_session_command_center
WITH (security_invoker = true)
AS
SELECT 
    e.id AS event_id,
    e.event_code,
    e.event_date,
    e.start_time,
    e.location,
    e.event_status,
    COUNT(CASE WHEN ad.response = 'SIM' THEN 1 END) AS confirmed_athletes_count,
    COUNT(CASE WHEN ad.response = 'SEM_RESPOSTA' THEN 1 END) AS pending_athletes_count
FROM public.calendar_events e
LEFT JOIN public.availability_declarations ad ON e.id = ad.event_id
WHERE e.event_type = 'TREINO' AND e.event_date >= CURRENT_DATE
GROUP BY e.id, e.event_code, e.event_date, e.start_time, e.location, e.event_status
ORDER BY e.event_date ASC
LIMIT 1;

-- 3. VIEW: Resumo Factual de Jogos e Aproveitamento do Clube
CREATE OR REPLACE VIEW public.v_match_performance_summary
WITH (security_invoker = true)
AS
SELECT 
    c.name AS competition_name,
    COUNT(m.id) AS total_matches,
    COUNT(CASE WHEN m.cepraea_victory = true THEN 1 END) AS wins,
    COUNT(CASE WHEN m.cepraea_victory = false THEN 1 END) AS losses,
    ROUND(
        (COUNT(CASE WHEN m.cepraea_victory = true THEN 1 END)::DECIMAL / 
        NULLIF(COUNT(m.id), 0)) * 100, 2
    ) AS win_rate_percentage
FROM public.competitions c
JOIN public.matches m ON c.id = m.competition_id
WHERE m.match_status = 'REALIZADO'
GROUP BY c.id, c.name;

COMMIT;
```
