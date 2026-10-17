```sql
-- =============================================================================
-- 09 — SUÍTE DE TESTES ESTRUTURAIS, POSITIVOS, NEGATIVOS E RLS (pgTAP)
-- =============================================================================
-- Testes automatizados de regressão e segurança RLS para PostgreSQL/Supabase
-- =============================================================================

BEGIN;

-- Ativar pgTAP se disponível
CREATE EXTENSION IF NOT EXISTS pgtap;

SELECT plan(15);

-- 1. TESTES ESTRUTURAIS DE TABELAS E SCHEMAS
SELECT has_table('public', 'athletes', 'Tabela public.athletes deve existir');
SELECT has_table('public', 'factual_presences', 'Tabela public.factual_presences deve existir');
SELECT has_table('public', 'availability_declarations', 'Tabela public.availability_declarations deve existir');

-- 2. TESTES DE CONSTRAINTS DE UNICIDADE
SELECT col_is_pk('public', 'athletes', 'id', 'Coluna id deve ser Primary Key em athletes');
SELECT col_is_pk('public', 'factual_presences', 'id', 'Coluna id deve ser Primary Key em factual_presences');

-- 3. TESTES NEGATIVOS — DOMÍNIO E RESTRICÕES
SELECT throws_ok(
    $$ INSERT INTO public.athletes (athlete_code, display_name, primary_position, jersey_number) 
       VALUES ('ATH-TEST-ERR', 'Erro Teste', 'CENTRAL', 150) $$,
    '23514',
    NULL,
    'Número de camisa 150 deve violar constraint CHECK (between 1 and 99)'
);

SELECT throws_ok(
    $$ INSERT INTO public.availability_declarations (event_id, athlete_id, response, source_sheet) 
       VALUES ('e0000000-0000-0000-0000-000000000001', 'a0000000-0000-0000-0000-000000000001', 'SIM', 'TESTE'); $$,
    '23505',
    NULL,
    'Inserção duplicada de disponibilidade para mesmo evento x atleta deve violar restrição UNIQUE (RN-DISP-004)'
);

-- 4. TESTES POSITIVOS — DERIVAÇÕES GERADAS AUTOMATICAMENTE
INSERT INTO public.competitions (id, competition_code, name, organizer, start_date, end_date, location)
VALUES ('c0000000-0000-0000-0000-000000000001', 'COMP-2026-TEST', 'Torneio Teste pgTAP', 'FHERJ', '2026-09-01', '2026-09-01', 'Niterói - RJ')
ON CONFLICT DO NOTHING;

INSERT INTO public.matches (id, match_code, competition_id, match_date, match_stage_phase, team_a_name, team_b_name, cepraea_side, set1_cepraea, set1_opponent, set2_cepraea, set2_opponent)
VALUES ('m0000000-0000-0000-0000-000000000001', 'JOGO-TEST-001', 'c0000000-0000-0000-0000-000000000001', '2026-09-01', 'FINAL', 'CEPRAEA', 'Rival Beach', 'EQUIPE_A', 22, 18, 20, 16)
ON CONFLICT DO NOTHING;

SELECT results_eq(
    $$ SELECT sets_won_cepraea, sets_won_opponent, cepraea_victory FROM public.matches WHERE match_code = 'JOGO-TEST-001' $$,
    $$ VALUES (2, 0, true) $$,
    'Placar 2x0 de sets deve derivar sets_won_cepraea=2 e cepraea_victory=true automaticamente'
);

-- 5. TESTES DE SEGURANÇA RLS E PERMISSÕES
SELECT ok(
    not has_table_privilege('anon', 'public.factual_presences', 'insert,update,delete'),
    'Papel anon não pode ter privilégio de escrita na tabela de presenças factuais'
);

SELECT ok(
    not has_table_privilege('anon', 'public.presence_proposals', 'insert,update,delete'),
    'Papel anon não pode alterar propostas de presença'
);

-- Finalizar suíte
SELECT * FROM finish();

ROLLBACK;
```

