```sql
-- =============================================================================
-- 07 — MATRIZ RBAC E POLÍTICAS RLS (SUPABASE) — CEPRAEA BEACH HANDBALL PRO
-- =============================================================================
-- Controle de Acesso por Linha (Row Level Security) e Princípio Default-Deny
-- =============================================================================

BEGIN;

-- 1. HABILITAR RLS EM TODAS AS TABELAS EXPOSTAS
ALTER TABLE public.athletes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.secondary_positions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.calendar_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.availability_declarations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.presence_proposals ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.factual_presences ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.competitions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.convocations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.convocation_athletes ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.matches ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.match_appearances ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.possessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.bous ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.tactical_events ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.finalizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.goalkeeper_actions ENABLE ROW LEVEL SECURITY;

-- 2. REVOGAR CONCESSÕES PADRÃO PÚBLICAS (DEFAULT-DENY)
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM anon, authenticated;

-- 3. CONCEDER PERMISSÕES EXPLICITAS POR PAPEL
-- 3.1 anon (Visitantes não autenticados - Leitura mínima restrita se aplicável)
GRANT SELECT ON public.calendar_events TO anon;
GRANT SELECT ON public.competitions TO anon;

-- 3.2 authenticated (Atletas e Comissão Técnica)
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO authenticated;

-- 4. CRIAÇÃO DE SECURITY DEFINER HELPERS NO SCHEMA PRIVATE (EVITA RECURSÃO RLS)

CREATE OR REPLACE FUNCTION private.get_current_athlete_id()
RETURNS UUID
LANGUAGE sql
SECURITY DEFINER
SET search_path = ''
STABLE
AS $$
    SELECT id FROM public.athletes 
    WHERE athlete_code = current_setting('request.jwt.claim.athlete_code', true)
    LIMIT 1;
$$;

CREATE OR REPLACE FUNCTION private.is_technical_staff()
RETURNS BOOLEAN
LANGUAGE sql
SECURITY DEFINER
SET search_path = ''
STABLE
AS $$
    SELECT COALESCE(
        current_setting('request.jwt.claim.role_staff', true)::boolean, 
        false
    );
$$;

-- 5. POLÍTICAS RLS POR TABELA

-- 5.1 `athletes`
CREATE POLICY "Atletas e Staff podem ler o cadastro de atletas"
ON public.athletes FOR SELECT TO authenticated
USING ( true );

CREATE POLICY "Somente Comissão Técnica pode alterar atletas"
ON public.athletes FOR ALL TO authenticated
USING ( private.is_technical_staff() )
WITH CHECK ( private.is_technical_staff() );

-- 5.2 `availability_declarations`
CREATE POLICY "Atletas leem e editam apenas suas proprias declaracoes"
ON public.availability_declarations FOR ALL TO authenticated
USING ( athlete_id = private.get_current_athlete_id() OR private.is_technical_staff() )
WITH CHECK ( athlete_id = private.get_current_athlete_id() OR private.is_technical_staff() );

-- 5.3 `factual_presences`
CREATE POLICY "Todos autenticados leem presencas factuais"
ON public.factual_presences FOR SELECT TO authenticated
USING ( true );

CREATE POLICY "Somente o Treinador/Steward pode gravar presencas factuais"
ON public.factual_presences FOR ALL TO authenticated
USING ( private.is_technical_staff() )
WITH CHECK ( private.is_technical_staff() );

-- 5.4 `presence_proposals`
CREATE POLICY "Atletas criam propostas proprias; Staff gerencia fila"
ON public.presence_proposals FOR ALL TO authenticated
USING ( athlete_id = private.get_current_athlete_id() OR private.is_technical_staff() )
WITH CHECK ( athlete_id = private.get_current_athlete_id() OR private.is_technical_staff() );

COMMIT;
```