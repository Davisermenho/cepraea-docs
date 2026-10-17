**BANCO CEPRAEA**

**Modelagem completa corrigida do banco de dados  
MVP CEPRAEA BEACH PRO**

PostgreSQL / Supabase • ambiente sintético • perfil LEAN

*Documento técnico para implementação e revisão de domínio*

# 1. Finalidade e resultado

Este documento especifica o banco de dados do MVP do CEPRAEA BEACH PRO após reconciliação das planilhas operacionais, das decisões documentais do projeto, do repositório React/TypeScript/Supabase e das regras oficiais atuais do handebol de praia. A modelagem separa identidade, vínculo, disponibilidade, lista prevista, presença factual, comunicação, privacidade e auditoria.

| **Dimensão** | **Decisão de modelagem** |
| --- | --- |
| Escopo ativo | 23 tabelas físicas nos schemas public, private e audit. |
| --- | --- |
| Indicadores | Views derivadas; não duplicar fatos em tabelas de indicadores/exportação. |
| --- | --- |
| Disponibilidade | Solicitação + destinatário + resposta versionada; NÃO RESPONDEU é derivado. |
| --- | --- |
| Presença | Fato registrado depois do treino; nunca inferido da disponibilidade ou lista. |
| --- | --- |
| Função ampla | GOLEIRA, DEFESA, ATAQUE e INDEFINIDA. |
| --- | --- |
| Especialista/coringa | Mesmo papel tático contextual; fora do cadastro e fora do MVP atual. |
| --- | --- |
| Segurança | RLS por equipe, MFA/AAL2 para treinador, schemas privados e RPCs. |
| --- | --- |
| Ambiente | Somente dados sintéticos até nova decisão formal. |
| --- | --- |
| Futuro | Extensões previstas por contrato, sem antecipar tabelas de competição/scout no MVP. |
| --- | --- |

# 2. Evidências e correções aplicadas

-   DB_ATLETAS possui IDs estáveis, mas mistura identidade, função, posição e estado ativo; o novo modelo separa athlete de athlete_roster_membership.
-   DB_PRESENCA armazena SIM/NÃO/TALVEZ/SEM_RESPOSTA antes do treino; isso é disponibilidade declarada, não presença factual.
-   DB_CALENDARIO e DB_TREINOS duplicam datas e horários; commitments torna-se a agenda única, e training_sessions apenas especializa treino.
-   DB_CONVOCACOES, DB_CONVOCACAO_ATLETAS e DB_PARTICIPACAO_JOGO comprovam que convocada para etapa não equivale a escalada ou jogou uma partida.
-   DB_FUNCOES contém CORINGA como função legada. A correção aplicada remove CORINGA/ESPECIALISTA do cadastro e preserva-os apenas como um futuro papel tático contextual.
-   DB_JOGOS demonstra necessidade futura de resultado por sets e shoot-out, porém competição e partida continuam fora do MVP autorizado.
-   O repositório atual contém o esqueleto funcional e dependência Supabase, mas não possui migrations de domínio implementadas; este documento define a base inicial.

# 3. Regras normativas consideradas

A modelagem não codifica regras esportivas mutáveis como constantes globais. Cada temporada registra ruleset_code; competições futuras deverão armazenar snapshots de limites e regras locais. Pontos usados agora:

-   As regras IHF de Beach Handball possuem versão vigente e anexos próprios; mudanças entram em vigor por data.
-   As alterações IHF válidas desde 1º de abril de 2026 permitem números de uniforme de 1 a 99; por isso shirt_number é temporal e validado nesse intervalo.
-   Resultados de praia possuem períodos/sets e, quando necessário, shoot-out; o futuro módulo de partidas não deve guardar apenas um placar textual.
-   O limite de atletas inscritas/por partida pode depender da competição e não deve ser um CHECK fixo no cadastro da equipe.

Fontes oficiais: [IHF — Rules of the Game (Beach Handball)](https://www.ihf.info/node/4653) • [IHF — alterações vigentes desde 1º de abril de 2026](https://www.ihf.info/index.php/media-center/news/new-rules-beach-handball-and-wheelchair-handball-be-observed-1-april-and-1-july)

# 4. Princípios obrigatórios do domínio

| **ID** | **Invariante** |
| --- | --- |
| DOM-001 | Disponibilidade ≠ presença real. |
| --- | --- |
| DOM-002 | Lista prevista ≠ presença real. |
| --- | --- |
| DOM-003 | Convocação de etapa ≠ escalação/roster de partida ≠ participação real. |
| --- | --- |
| DOM-004 | Nome não é chave; joins usam UUID ou código legado controlado. |
| --- | --- |
| DOM-005 | Respostas, correções, presença e eventos de vínculo preservam histórico. |
| --- | --- |
| DOM-006 | Justificativas são privadas e nunca integram listas compartilhadas. |
| --- | --- |
| DOM-007 | ESPECIALISTA = CORINGA; ambos são papel tático contextual, não função ampla nem posição permanente. |
| --- | --- |
| DOM-008 | Indicadores são projeções de fatos validados. |
| --- | --- |
| DOM-009 | Mudança de regra esportiva não reescreve fatos históricos. |
| --- | --- |
| DOM-010 | Nenhum dado real é autorizado no estágio sintético atual. |
| --- | --- |

# 5. Arquitetura lógica e schemas

| **Schema** | **Responsabilidade** | **Exposição** |
| --- | --- | --- |
| public | Domínio operacional, views e RPCs. | Exposto pela API Supabase, sempre com RLS. |
| --- | --- | --- |
| private | Justificativas e funções auxiliares. | Não exposto; sem grants diretos ao cliente. |
| --- | --- | --- |
| audit | Log técnico append-only. | Somente treinador AAL2 em leitura; escrita por trigger/RPC. |
| --- | --- | --- |
| auth | Identidade gerenciada pelo Supabase Auth. | Gerenciado pelo Supabase; não duplicar credenciais. |
| --- | --- | --- |

# 6. Catálogo de tipos PostgreSQL

-- 0001_foundation.sql  
create schema if not exists private;  
create schema if not exists audit;  
create schema if not exists extensions;  
  
create extension if not exists pgcrypto with schema extensions;  
  
create type public.app_role as enum ('COACH', 'ATHLETE');  
create type public.access_membership_status as enum ('ACTIVE', 'SUSPENDED', 'ENDED');  
create type public.season_status as enum ('PLANEJADA', 'ATIVA', 'ENCERRADA');  
create type public.athlete_relationship_status as enum  
('ATIVA', 'INATIVA_TEMPORARIA', 'VINCULO_ENCERRADO');  
create type public.broad_player_function as enum  
('GOLEIRA', 'DEFESA', 'ATAQUE', 'INDEFINIDA');  
create type public.commitment_type as enum  
('TREINO', 'COMPETICAO', 'REUNIAO', 'FEEDBACK', 'OUTRO');  
create type public.commitment_status as enum  
('RASCUNHO', 'PLANEJADO', 'PUBLICADO', 'REALIZADO', 'CANCELADO');  
create type public.response_semantic_group as enum  
('AFFIRMATIVE', 'NEGATIVE', 'UNCERTAIN');  
create type public.request_status as enum  
('RASCUNHO', 'ABERTA', 'ENCERRADA', 'CANCELADA');  
create type public.correction_action as enum ('REPLACE', 'VOID');  
create type public.operational_list_type as enum ('TRAINING_EXPECTED');  
create type public.list_publication_status as enum  
('RASCUNHO', 'PUBLICADA', 'SUBSTITUIDA', 'ENCERRADA', 'NAO_PUBLICADA');  
create type public.attendance_status as enum  
('PRESENTE', 'AUSENTE', 'ATRASADA', 'SAIDA_ANTECIPADA', 'DISPENSADA');  
create type public.communication_audience_type as enum  
('ALL_ACTIVE_ATHLETES', 'SELECTED', 'COACH_ONLY');  
create type public.communication_status as enum  
('RASCUNHO', 'PUBLICADA', 'ARQUIVADA');  
create type public.delivery_status as enum ('PENDING', 'DELIVERED', 'FAILED');  
  
comment on type public.broad_player_function is  
'Funções amplas cadastrais. ESPECIALISTA/CORINGA é papel tático contextual e não pertence a este enum.';  
  
create or replace function private.set_updated_at()  
returns trigger  
language plpgsql  
security invoker  
set search_path = ''  
as $$  
begin  
new.updated_at := now();  
return new;  
end;  
$$;  
  
create or replace function private.prevent_update_delete()  
returns trigger  
language plpgsql  
security invoker  
set search_path = ''  
as $$  
begin  
raise exception 'Tabela append-only: operação % não permitida em %.%',  
tg_op, tg_table_schema, tg_table_name;  
end;  
$$;  

# 7. Catálogo de tabelas

| **#** | **Nome da tabela** | **Descrição** |
| --- | --- | --- |
| 1 | public.teams | Unidade esportiva isoladora de acesso. No MVP representa o CEPRAEA e permite expansão futura para outras equipes sem misturar dados. |
| --- | --- | --- |
| 2 | public.seasons | Recorte temporal esportivo da equipe. Centraliza vigência do elenco, compromissos e versão de regras aplicável. |
| --- | --- | --- |
| 3 | public.profiles | Extensão mínima de auth.users. Contém apenas dados de apresentação e estado da conta; papéis de equipe ficam em team_access_memberships. |
| --- | --- | --- |
| 4 | public.team_access_memberships | Vínculo temporal entre perfil autenticado e equipe, com papel COACH ou ATHLETE. É a base das políticas RLS. |
| --- | --- | --- |
| 5 | public.athletes | Identidade esportiva estável da atleta. Não guarda função, posição ou status temporal do elenco; esses atributos pertencem ao vínculo de temporada. |
| --- | --- | --- |
| 6 | public.athlete_roster_memberships | Vínculo temporal da atleta com uma temporada. Guarda estado do elenco, função ampla corrigida e número de camisa. |
| --- | --- | --- |
| 7 | public.athlete_roster_events | Histórico append-only de mudanças no vínculo esportivo. Preserva estado anterior, novo estado, efetividade e autoridade. |
| --- | --- | --- |
| 8 | public.commitments | Agenda operacional unificada. Representa treino e, futuramente, competição, reunião, feedback ou outro compromisso sem duplicar calendário. |
| --- | --- | --- |
| 9 | public.training_sessions | Especialização 1:1 de commitments para treinos. Guarda planejamento esportivo e orientação sem misturar confirmação antecipada ou presença real. |
| --- | --- | --- |
| 10 | public.request_definitions | Catálogo de tipos de solicitação operacional. Permite disponibilidade para treino hoje e novos fluxos futuros sem alterar o esquema. |
| --- | --- | --- |
| 11 | public.request_definition_options | Opções válidas de cada tipo de solicitação. Representa SIM, NÃO e TALVEZ; ausência de resposta é derivada e nunca cadastrada como opção. |
| --- | --- | --- |
| 12 | public.operational_requests | Instância versionada de uma pergunta operacional enviada a atletas, normalmente vinculada a um compromisso. |
| --- | --- | --- |
| 13 | public.request_recipients | Materializa quem deve responder a cada solicitação. É a origem do estado NÃO RESPONDEU quando não existe resposta válida. |
| --- | --- | --- |
| 14 | public.operational_responses | Declarações imutáveis das atletas. Cada nova resposta referencia a anterior; a resposta efetiva é calculada por view/RPC. |
| --- | --- | --- |
| 15 | public.justification_categories | Vocabulário mínimo e controlado de justificativas. Reduz texto livre e permite privacidade por desenho. |
| --- | --- | --- |
| 16 | private.response_justifications | Conteúdo privado opcional associado a uma resposta. Fica fora do schema exposto e só é acessado por RPCs autorizadas. |
| --- | --- | --- |
| 17 | public.response_corrections | Correção administrativa append-only aplicada sobre uma resposta, sem modificar a declaração original da atleta. |
| --- | --- | --- |
| 18 | public.operational_lists | Cabeçalho versionado de projeções operacionais, como lista prevista de treino. Suporta publicação, substituição, encerramento e decisão explícita de não publicar. |
| --- | --- | --- |
| 19 | public.operational_list_members | Membros de uma versão de lista. Mantém snapshots mínimos de nome e função para preservar exatamente o que foi publicado. |
| --- | --- | --- |
| 20 | public.attendance_records | Registro factual append-only de presença em treino. Ausência de linha significa “não registrado”, nunca ausência automática. |
| --- | --- | --- |
| 21 | public.communications | Mensagem operacional criada no produto. Separa conteúdo da entrega individual, leitura e ciência. |
| --- | --- | --- |
| 22 | public.communication_recipients | Estado individual de distribuição de uma comunicação: entrega, visualização e ciência são fatos distintos. |
| --- | --- | --- |
| 23 | audit.audit_events | Log técnico append-only para alterações e eventos de segurança. Complementa, mas não substitui, históricos de domínio. |
| --- | --- | --- |

# 8. Relações entre as tabelas

| **Origem** | **Destino** | **Cardinalidade** | **Finalidade** | **Exclusão** |
| --- | --- | --- | --- | --- |
| teams | seasons | 1:N | Uma equipe possui várias temporadas. | RESTRICT |
| --- | --- | --- | --- | --- |
| auth.users | profiles | 1:1 | Perfil é extensão da identidade Supabase Auth. | CASCADE somente no perfil |
| --- | --- | --- | --- | --- |
| teams / profiles | team_access_memberships | 1:N / 1:N | Resolve acesso temporal e papel por equipe. | RESTRICT |
| --- | --- | --- | --- | --- |
| teams / profiles | athletes | 1:N / 0..1:1 | Atleta pode existir antes de possuir conta. | RESTRICT / SET NULL |
| --- | --- | --- | --- | --- |
| athletes / seasons | athlete_roster_memberships | 1:N / 1:N | Vínculo temporal com função ampla e camisa. | RESTRICT |
| --- | --- | --- | --- | --- |
| athlete_roster_memberships | athlete_roster_events | 1:N | Histórico append-only de mudanças. | RESTRICT |
| --- | --- | --- | --- | --- |
| teams / seasons | commitments | 1:N / 1:N | Agenda única da operação. | RESTRICT |
| --- | --- | --- | --- | --- |
| commitments | training_sessions | 1:0..1 | Especialização somente para TREINO. | RESTRICT |
| --- | --- | --- | --- | --- |
| request_definitions | request_definition_options | 1:N | Opções válidas de cada solicitação. | RESTRICT |
| --- | --- | --- | --- | --- |
| request_definitions / commitments | operational_requests | 1:N / 0..N | Pergunta versionada sobre um compromisso. | RESTRICT |
| --- | --- | --- | --- | --- |
| operational_requests / athletes | request_recipients | 1:N / 1:N | Materializa obrigação individual de responder. | RESTRICT |
| --- | --- | --- | --- | --- |
| request_recipients | operational_responses | 1:N | Cada nova declaração preserva a anterior. | RESTRICT |
| --- | --- | --- | --- | --- |
| operational_responses | private.response_justifications | 1:0..1 | Conteúdo privado separado fisicamente. | RESTRICT |
| --- | --- | --- | --- | --- |
| request_recipients | response_corrections | 1:N | Correções administrativas sem sobrescrever autoria. | RESTRICT |
| --- | --- | --- | --- | --- |
| commitments | operational_lists | 1:N | Listas versionadas e publicáveis. | RESTRICT |
| --- | --- | --- | --- | --- |
| operational_lists / athletes | operational_list_members | 1:N / 1:N | Snapshot mínimo do que foi publicado. | RESTRICT |
| --- | --- | --- | --- | --- |
| training_sessions / athletes | attendance_records | 1:N / 1:N | Fatos de presença versionados. | RESTRICT |
| --- | --- | --- | --- | --- |
| communications | communication_recipients | 1:N | Estado individual de entrega, leitura e ciência. | RESTRICT |
| --- | --- | --- | --- | --- |
| tabelas operacionais | audit.audit_events | N:1 lógico | Auditoria técnica transversal sem acoplamento destrutivo. | Sem cascade |
| --- | --- | --- | --- | --- |

A regra geral de exclusão é RESTRICT: fatos históricos não devem desaparecer em cascata. SET NULL é usado apenas para relações opcionais de conta/autor que podem ser desativadas sem apagar o domínio.

# 9. Dicionário completo e SQL por tabela

Cada subseção apresenta a tabela estrutural, o significado de cada coluna, as regras da tabela, o CREATE TABLE e os índices em bloco separado.

## 9.1 public.teams

Unidade esportiva isoladora de acesso. No MVP representa o CEPRAEA e permite expansão futura para outras equipes sem misturar dados.

### Regras da tabela

-   Uma linha por equipe.
-   No perfil LEAN atual, synthetic_only deve permanecer true.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.teams | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.teams | code | text | UK | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.teams | name | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.teams | timezone | text | - | Não | 'America/Sao_Paulo' |
| --- | --- | --- | --- | --- | --- |
| public.teams | locale | text | - | Não | 'pt-BR' |
| --- | --- | --- | --- | --- | --- |
| public.teams | synthetic_only | boolean | - | Não | true |
| --- | --- | --- | --- | --- | --- |
| public.teams | active | boolean | - | Não | true |
| --- | --- | --- | --- | --- | --- |
| public.teams | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.teams | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador interno imutável da equipe. | Sistema | Sim | Identidade técnica | Relacionar todos os dados operacionais à equipe. | Nunca reutilizar ou expor como código humano. |
| --- | --- | --- | --- | --- | --- | --- |
| code | Código curto e estável da equipe. | Administrador | Sim | Identificador humano | Permitir referências legíveis e integrações. | Maiúsculo, sem espaços; imutável após uso. |
| --- | --- | --- | --- | --- | --- | --- |
| name | Nome oficial ou operacional da equipe. | Administrador | Sim | Apresentação | Exibir a equipe na PWA. | Não confundir produto, organização e equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| timezone | Fuso usado em calendário, prazos e logs. | Configuração | Sim | Temporal | Evitar conversões ambíguas. | Valor IANA válido. |
| --- | --- | --- | --- | --- | --- | --- |
| locale | Localidade padrão para textos e formatos. | Configuração | Sim | Internacionalização | Padronizar data, idioma e números. | Código BCP 47. |
| --- | --- | --- | --- | --- | --- | --- |
| synthetic_only | Indica que o ambiente está autorizado apenas para dados sintéticos. | Migração | Sim | Governança | Bloquear uso de dados reais no estágio vigente. | Só pode virar false após decisão formal e nova migration. |
| --- | --- | --- | --- | --- | --- | --- |
| active | Indica se a equipe está operacional. | Administrador | Sim | Ciclo de vida | Desativar sem apagar histórico. | Desativação não elimina registros. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Data/hora de criação. | Sistema | Sim | Auditoria | Rastrear origem temporal. | UTC no banco; apresentação no fuso da equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última atualização técnica. | Trigger | Sim | Auditoria | Controlar concorrência e sincronização. | Atualizado automaticamente. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.teams (  
id uuid primary key default gen_random_uuid(),  
code text not null,  
name text not null,  
timezone text default 'America/Sao_Paulo' not null,  
locale text default 'pt-BR' not null,  
synthetic_only boolean default true not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint teams_code_ck check (code ~ '^[A-Z0-9][A-Z0-9_-]{1,31}$')  
);

### Índices

create unique index teams_code_uq on public.teams (code);  
create index teams_active_idx on public.teams (active) where active;

## 9.2 public.seasons

Recorte temporal esportivo da equipe. Centraliza vigência do elenco, compromissos e versão de regras aplicável.

### Regras da tabela

-   ruleset_code registra referência normativa, mas limites de competição não devem ser codificados como constantes globais.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.seasons | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.seasons | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.seasons | label | text | UK parcial | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.seasons | starts_on | date | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.seasons | ends_on | date | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.seasons | status | public.season_status | - | Não | 'PLANEJADA' |
| --- | --- | --- | --- | --- | --- |
| public.seasons | ruleset_code | text | - | Não | 'IHF_BEACH_2026-04-01' |
| --- | --- | --- | --- | --- | --- |
| public.seasons | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.seasons | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da temporada. | Sistema | Sim | Identidade técnica | Referenciar o período esportivo. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe proprietária da temporada. | Sistema | Sim | Particionamento | Impedir mistura entre equipes. | Deve apontar para equipe ativa ou histórica válida. |
| --- | --- | --- | --- | --- | --- | --- |
| label | Nome legível, por exemplo “Temporada 2026”. | Treinador | Sim | Apresentação | Identificar o ciclo esportivo. | Único por equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| starts_on | Primeiro dia de vigência. | Treinador | Sim | Temporal | Delimitar elenco e calendário. | Deve ser anterior ou igual a ends_on. |
| --- | --- | --- | --- | --- | --- | --- |
| ends_on | Último dia de vigência. | Treinador | Sim | Temporal | Encerrar o ciclo sem apagar fatos. | Deve ser posterior ou igual a starts_on. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Estado da temporada. | Treinador/RPC | Sim | Fluxo | Controlar planejamento, operação e encerramento. | Somente uma temporada ATIVA por equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| ruleset_code | Versão normativa esportiva de referência. | Administrador | Sim | Governança esportiva | Evitar regras implícitas ou hardcoded. | Mudança exige validação e não altera fatos históricos. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Data/hora de criação. | Sistema | Sim | Auditoria | Rastrear criação. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração. | Trigger | Sim | Auditoria | Rastrear manutenção. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.seasons (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
label text not null,  
starts_on date not null,  
ends_on date not null,  
status public.season_status default 'PLANEJADA' not null,  
ruleset_code text default 'IHF_BEACH_2026-04-01' not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint seasons_dates_ck check (ends_on >= starts_on),  
constraint seasons_team_label_uq unique (team_id, label)  
);

### Índices

create unique index seasons_one_active_per_team_uq on public.seasons (team_id) where status = 'ATIVA';  
create index seasons_team_dates_idx on public.seasons (team_id, starts_on, ends_on);

## 9.3 public.profiles

Extensão mínima de auth.users. Contém apenas dados de apresentação e estado da conta; papéis de equipe ficam em team_access_memberships.

### Regras da tabela

-   Não armazenar senha, token ou segredo.
-   A conta não define sozinha acesso à equipe.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.profiles | id | uuid | PK/FK → auth.users.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.profiles | display_name | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.profiles | preferred_name | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.profiles | active | boolean | - | Não | true |
| --- | --- | --- | --- | --- | --- |
| public.profiles | mfa_required | boolean | - | Não | false |
| --- | --- | --- | --- | --- | --- |
| public.profiles | last_seen_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.profiles | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.profiles | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Mesmo UUID da conta Supabase Auth. | Trigger de cadastro/Administrador | Sim | Identidade de acesso | Vincular autenticação ao domínio. | Não criar sem usuário Auth correspondente. |
| --- | --- | --- | --- | --- | --- | --- |
| display_name | Nome mostrado na interface administrativa. | Usuário/Administrador | Sim | Apresentação | Identificar a conta. | Não usar como chave ou join. |
| --- | --- | --- | --- | --- | --- | --- |
| preferred_name | Nome curto opcional escolhido pelo usuário. | Usuário via RPC | Não | Preferência | Personalizar a interface. | Sem dados sensíveis desnecessários. |
| --- | --- | --- | --- | --- | --- | --- |
| active | Estado operacional da conta no produto. | Administrador | Sim | Segurança | Suspender acesso sem apagar histórico. | Conta inativa não satisfaz políticas RLS. |
| --- | --- | --- | --- | --- | --- | --- |
| mfa_required | Indica exigência operacional de MFA. | Administrador | Sim | Segurança | Reforçar ações privilegiadas. | Obrigatório para treinador no MVP. |
| --- | --- | --- | --- | --- | --- | --- |
| last_seen_at | Última atividade observada. | Sistema | Não | Operação | Apoiar suporte e revogação. | Não é prova de leitura de comunicação. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação do perfil. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração. | Trigger | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.profiles (  
id uuid primary key references auth.users(id) on delete cascade,  
display_name text not null,  
preferred_name text default null,  
active boolean default true not null,  
mfa_required boolean default false not null,  
last_seen_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null  
);

### Índices

create index profiles_active_idx on public.profiles (active) where active;  
create index profiles_display_name_idx on public.profiles (lower(display_name));

## 9.4 public.team_access_memberships

Vínculo temporal entre perfil autenticado e equipe, com papel COACH ou ATHLETE. É a base das políticas RLS.

### Regras da tabela

-   Treinador exige MFA nível AAL2 para escrita privilegiada.
-   Vínculo encerrado permanece para auditoria.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | profile_id | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | role | public.app_role | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | status | public.access_membership_status | - | Não | 'ACTIVE' |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | valid_from | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | valid_until | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | created_by | uuid | FK → profiles.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.team_access_memberships | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador do vínculo de acesso. | Sistema | Sim | Identidade técnica | Versionar concessões de acesso. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe acessível. | Administrador | Sim | Escopo RLS | Restringir dados por equipe. | Obrigatório em toda autorização. |
| --- | --- | --- | --- | --- | --- | --- |
| profile_id | Perfil que recebe o acesso. | Administrador | Sim | Sujeito de acesso | Associar usuário ao escopo. | Perfil deve estar ativo para operar. |
| --- | --- | --- | --- | --- | --- | --- |
| role | Papel exercido na equipe. | Administrador | Sim | Autorização | Distinguir treinador e atleta. | MVP aceita somente COACH e ATHLETE. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Estado do acesso. | Administrador/RPC | Sim | Segurança | Suspender ou encerrar sem apagar. | Somente ACTIVE concede acesso. |
| --- | --- | --- | --- | --- | --- | --- |
| valid_from | Início da validade. | Administrador | Sim | Temporal | Preservar histórico de concessão. | Não pode sobrepor vínculo ativo equivalente. |
| --- | --- | --- | --- | --- | --- | --- |
| valid_until | Fim da validade. | Administrador | Não | Temporal | Encerrar concessão. | Nulo representa vigência aberta. |
| --- | --- | --- | --- | --- | --- | --- |
| created_by | Perfil que concedeu o acesso. | Sistema/RPC | Não | Auditoria | Identificar autoridade. | Primeiro treinador pode ser provisionado por service role. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Registro da concessão. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.team_access_memberships (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
profile_id uuid references public.profiles(id) on delete restrict not null,  
role public.app_role not null,  
status public.access_membership_status default 'ACTIVE' not null,  
valid_from timestamptz default now() not null,  
valid_until timestamptz default null,  
created_by uuid references public.profiles(id) on delete set null,  
created_at timestamptz default now() not null,  
constraint team_access_period_ck check (valid_until is null or valid_until > valid_from)  
);

### Índices

create index team_access_profile_idx on public.team_access_memberships (profile_id, status, valid_until);  
create index team_access_team_role_idx on public.team_access_memberships (team_id, role, status);  
create unique index team_access_open_uq on public.team_access_memberships (team_id, profile_id, role) where valid_until is null and status = 'ACTIVE';

## 9.5 public.athletes

Identidade esportiva estável da atleta. Não guarda função, posição ou status temporal do elenco; esses atributos pertencem ao vínculo de temporada.

### Regras da tabela

-   Retorno reutiliza a mesma linha.
-   Não armazenar CORINGA/ESPECIALISTA em athletes.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.athletes | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.athletes | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.athletes | profile_id | uuid | FK → profiles.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athletes | legacy_athlete_id | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athletes | display_name | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.athletes | created_by | uuid | FK → profiles.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athletes | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.athletes | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador interno estável da atleta. | Sistema | Sim | Identidade de domínio | Referenciar a pessoa em todo histórico. | Nunca recriar a identidade em retorno ao elenco. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe que mantém o cadastro. | Treinador | Sim | Particionamento | Isolar identidades por equipe. | Não usar para inferir vínculo ativo. |
| --- | --- | --- | --- | --- | --- | --- |
| profile_id | Conta da própria atleta, quando ativada. | Treinador/Convite | Não | Acesso | Permitir autoatendimento. | Pode ser nulo antes do convite; único quando preenchido. |
| --- | --- | --- | --- | --- | --- | --- |
| legacy_athlete_id | Código estável da planilha, como ATH-0001. | Migração controlada | Não | Proveniência | Conciliar legado sem depender do nome. | Somente importação validada; único por equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| display_name | Nome operacional mostrado a treinador e em projeções autorizadas. | Treinador | Sim | Apresentação | Identificar a atleta. | Não usar como chave; alterações não quebram histórico. |
| --- | --- | --- | --- | --- | --- | --- |
| created_by | Perfil responsável pelo cadastro. | Sistema/RPC | Não | Auditoria | Registrar autoridade. | Pode ser nulo em seed/migração controlada. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação da identidade. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última atualização cadastral. | Trigger | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.athletes (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
profile_id uuid references public.profiles(id) on delete set null,  
legacy_athlete_id text default null,  
display_name text not null,  
created_by uuid references public.profiles(id) on delete set null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint athletes_team_legacy_uq unique (team_id, legacy_athlete_id),  
constraint athletes_team_profile_uq unique (team_id, profile_id)  
);

### Índices

create index athletes_team_name_idx on public.athletes (team_id, lower(display_name));  
create index athletes_profile_idx on public.athletes (profile_id) where profile_id is not null;

## 9.6 public.athlete_roster_memberships

Vínculo temporal da atleta com uma temporada. Guarda estado do elenco, função ampla corrigida e número de camisa.

### Regras da tabela

-   Função é ampla, não posição específica.
-   Ausência em treino não altera status do vínculo.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | athlete_id | uuid | FK → athletes.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | season_id | uuid | FK → seasons.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | status | public.athlete_relationship_status | - | Não | 'ATIVA' |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | broad_function | public.broad_player_function | - | Não | 'INDEFINIDA' |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | shirt_number | smallint | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | starts_on | date | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | ends_on | date | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | source_note | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | created_by | uuid | FK → profiles.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_memberships | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador do vínculo esportivo. | Sistema | Sim | Identidade técnica | Referenciar o estado da atleta no período. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| athlete_id | Atleta vinculada. | Treinador | Sim | Relacionamento | Associar identidade ao elenco. | Não duplicar identidade em retorno. |
| --- | --- | --- | --- | --- | --- | --- |
| season_id | Temporada do vínculo. | Treinador | Sim | Temporal | Separar ciclos esportivos. | Atleta e temporada devem pertencer à mesma equipe, validado por trigger/RPC. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Estado do vínculo: ATIVA, INATIVA_TEMPORARIA ou VINCULO_ENCERRADO. | Treinador/RPC | Sim | Ciclo de vida | Representar afastamento e encerramento sem apagar. | Não confundir com disponibilidade para compromisso. |
| --- | --- | --- | --- | --- | --- | --- |
| broad_function | Função esportiva ampla. | Treinador | Sim | Classificação ampla | Apoiar cobertura descritiva do elenco. | Somente GOLEIRA, DEFESA, ATAQUE, INDEFINIDA; especialista/coringa é papel tático contextual. |
| --- | --- | --- | --- | --- | --- | --- |
| shirt_number | Número de camisa válido na temporada. | Treinador | Não | Identificação esportiva | Apoiar listas e futuras competições. | Entre 1 e 99 conforme regra IHF vigente desde 01/04/2026; pode variar por temporada. |
| --- | --- | --- | --- | --- | --- | --- |
| starts_on | Início do vínculo. | Treinador | Sim | Temporal | Determinar elenco em uma data. | Dentro ou compatível com a temporada. |
| --- | --- | --- | --- | --- | --- | --- |
| ends_on | Fim do vínculo. | Treinador/RPC | Não | Temporal | Preservar encerramento. | Nulo = aberto; não anterior a starts_on. |
| --- | --- | --- | --- | --- | --- | --- |
| source_note | Referência curta da decisão ou origem. | Treinador/Migração | Não | Proveniência | Explicar origem sem guardar documento inteiro. | Não incluir dado sensível desnecessário. |
| --- | --- | --- | --- | --- | --- | --- |
| created_by | Autor do vínculo. | Sistema/RPC | Não | Auditoria | Registrar autoridade. | - |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação do vínculo. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração materializada. | Trigger | Sim | Auditoria | Rastreabilidade. | Mudanças relevantes também geram athlete_roster_events. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.athlete_roster_memberships (  
id uuid primary key default gen_random_uuid(),  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
season_id uuid references public.seasons(id) on delete restrict not null,  
status public.athlete_relationship_status default 'ATIVA' not null,  
broad_function public.broad_player_function default 'INDEFINIDA' not null,  
shirt_number smallint default null,  
starts_on date not null,  
ends_on date default null,  
source_note text default null,  
created_by uuid references public.profiles(id) on delete set null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint roster_period_ck check (ends_on is null or ends_on >= starts_on),  
constraint roster_shirt_number_ck check (shirt_number is null or shirt_number between 1 and 99)  
);

### Índices

create index roster_season_status_idx on public.athlete_roster_memberships (season_id, status, broad_function);  
create index roster_athlete_period_idx on public.athlete_roster_memberships (athlete_id, starts_on, ends_on);  
create unique index roster_open_per_season_uq on public.athlete_roster_memberships (athlete_id, season_id) where ends_on is null;

## 9.7 public.athlete_roster_events

Histórico append-only de mudanças no vínculo esportivo. Preserva estado anterior, novo estado, efetividade e autoridade.

### Regras da tabela

-   Proibir UPDATE e DELETE por trigger.
-   Correção cria novo evento; não reescreve eventos passados.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | membership_id | uuid | FK → athlete_roster_memberships.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | event_type | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | effective_on | date | - | Não | current_date |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | from_state | jsonb | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | to_state | jsonb | - | Não | '{}'::jsonb |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | reason | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | actor_profile_id | uuid | FK → profiles.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.athlete_roster_events | occurred_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador do evento. | Sistema | Sim | Identidade técnica | Rastrear cada mudança. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| membership_id | Vínculo afetado. | RPC | Sim | Relacionamento | Conectar evento ao histórico. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| event_type | Tipo controlado da mudança. | RPC | Sim | Semântica | Explicar o que ocorreu. | Valores recomendados: CREATED, STATUS_CHANGED, FUNCTION_CHANGED, SHIRT_NUMBER_CHANGED, RETURNED, ENDED. |
| --- | --- | --- | --- | --- | --- | --- |
| effective_on | Data esportiva em que a mudança produz efeito. | Treinador/RPC | Sim | Temporal | Reconstruir elenco histórico. | Pode diferir de occurred_at. |
| --- | --- | --- | --- | --- | --- | --- |
| from_state | Snapshot anterior dos campos relevantes. | RPC | Não | Auditoria de domínio | Comparar antes/depois. | Não incluir dados secretos ou justificativas privadas. |
| --- | --- | --- | --- | --- | --- | --- |
| to_state | Snapshot resultante. | RPC | Sim | Auditoria de domínio | Reconstruir decisão. | Chaves compatíveis com o vínculo. |
| --- | --- | --- | --- | --- | --- | --- |
| reason | Motivo administrativo curto. | Treinador | Não | Contexto | Explicar alteração. | Evitar dados de saúde ou sensíveis. |
| --- | --- | --- | --- | --- | --- | --- |
| actor_profile_id | Perfil que executou a alteração. | Sistema | Não | Autoridade | Identificar responsável. | Nulo apenas para migração/service role identificada em metadata. |
| --- | --- | --- | --- | --- | --- | --- |
| occurred_at | Momento do registro. | Sistema | Sim | Auditoria | Ordenar eventos. | UTC. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.athlete_roster_events (  
id uuid primary key default gen_random_uuid(),  
membership_id uuid references public.athlete_roster_memberships(id) on delete restrict not null,  
event_type text not null,  
effective_on date default current_date not null,  
from_state jsonb default null,  
to_state jsonb default '{}'::jsonb not null,  
reason text default null,  
actor_profile_id uuid references public.profiles(id) on delete set null,  
occurred_at timestamptz default now() not null  
);

### Índices

create index roster_events_membership_time_idx on public.athlete_roster_events (membership_id, occurred_at desc);  
create index roster_events_type_idx on public.athlete_roster_events (event_type, occurred_at desc);

## 9.8 public.commitments

Agenda operacional unificada. Representa treino e, futuramente, competição, reunião, feedback ou outro compromisso sem duplicar calendário.

### Regras da tabela

-   DB_CALENDARIO vira view de commitments.
-   Não inferir realização apenas pela passagem do horário.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.commitments | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.commitments | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.commitments | season_id | uuid | FK → seasons.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.commitments | commitment_type | public.commitment_type | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.commitments | title | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.commitments | description | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.commitments | starts_at | timestamptz | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.commitments | ends_at | timestamptz | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.commitments | timezone | text | - | Não | 'America/Sao_Paulo' |
| --- | --- | --- | --- | --- | --- |
| public.commitments | location_name | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.commitments | status | public.commitment_status | - | Não | 'RASCUNHO' |
| --- | --- | --- | --- | --- | --- |
| public.commitments | published_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.commitments | cancelled_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.commitments | created_by | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.commitments | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.commitments | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador do compromisso. | Sistema | Sim | Identidade técnica | Unificar agenda e fluxos associados. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe proprietária. | Treinador | Sim | Particionamento | Aplicar RLS e calendário. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| season_id | Temporada do compromisso. | Treinador | Sim | Temporal | Relacionar agenda ao ciclo. | Mesma equipe do compromisso. |
| --- | --- | --- | --- | --- | --- | --- |
| commitment_type | Natureza do compromisso. | Treinador | Sim | Classificação | Permitir extensão sem criar calendários paralelos. | TREINO ativa training_sessions; demais tipos podem ganhar módulos próprios. |
| --- | --- | --- | --- | --- | --- | --- |
| title | Título legível. | Treinador | Sim | Apresentação | Exibir agenda e solicitações. | Claro e não sensível. |
| --- | --- | --- | --- | --- | --- | --- |
| description | Descrição pública operacional. | Treinador | Não | Comunicação | Dar contexto. | Visível apenas conforme status/políticas. |
| --- | --- | --- | --- | --- | --- | --- |
| starts_at | Início do compromisso. | Treinador | Sim | Temporal | Ordenar agenda e abrir fluxos. | Armazenar com offset/fuso correto. |
| --- | --- | --- | --- | --- | --- | --- |
| ends_at | Fim previsto ou real. | Treinador | Sim | Temporal | Definir duração. | Posterior a starts_at. |
| --- | --- | --- | --- | --- | --- | --- |
| timezone | Fuso de apresentação do compromisso. | Treinador | Sim | Temporal | Preservar intenção local. | IANA válido. |
| --- | --- | --- | --- | --- | --- | --- |
| location_name | Local legível. | Treinador | Não | Logística | Orientar participantes. | Não substitui futura entidade venue. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Estado do compromisso. | Treinador/RPC | Sim | Fluxo | Controlar visibilidade e execução. | Atletas não veem RASCUNHO. |
| --- | --- | --- | --- | --- | --- | --- |
| published_at | Momento da publicação. | RPC | Não | Auditoria de publicação | Comprovar quando ficou visível. | Obrigatório quando PUBLICADO/REALIZADO. |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled_at | Momento do cancelamento. | RPC | Não | Auditoria | Distinguir cancelado de apagado. | Obrigatório quando CANCELADO. |
| --- | --- | --- | --- | --- | --- | --- |
| created_by | Treinador criador. | Sistema/RPC | Sim | Autoridade | Rastrear origem. | Deve ser COACH da equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração. | Trigger | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.commitments (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
season_id uuid references public.seasons(id) on delete restrict not null,  
commitment_type public.commitment_type not null,  
title text not null,  
description text default null,  
starts_at timestamptz not null,  
ends_at timestamptz not null,  
timezone text default 'America/Sao_Paulo' not null,  
location_name text default null,  
status public.commitment_status default 'RASCUNHO' not null,  
published_at timestamptz default null,  
cancelled_at timestamptz default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint commitments_period_ck check (ends_at > starts_at),  
constraint commitments_publish_ck check (status not in ('PUBLICADO','REALIZADO') or published_at is not null),  
constraint commitments_cancel_ck check (status <> 'CANCELADO' or cancelled_at is not null)  
);

### Índices

create index commitments_team_start_idx on public.commitments (team_id, starts_at);  
create index commitments_season_type_status_idx on public.commitments (season_id, commitment_type, status);  
create index commitments_upcoming_idx on public.commitments (team_id, starts_at) where status in ('PLANEJADO','PUBLICADO');

## 9.9 public.training_sessions

Especialização 1:1 de commitments para treinos. Guarda planejamento esportivo e orientação sem misturar confirmação antecipada ou presença real.

### Regras da tabela

-   Disponibilidade deve ser coletada por operational_requests.
-   Presença real deve ser registrada em attendance_records.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | commitment_id | uuid | FK/UK → commitments.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | objective | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | main_activity | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | collective_goals | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | athlete_guidance | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | attendance_opened_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | attendance_closed_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.training_sessions | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da sessão. | Sistema | Sim | Identidade técnica | Referenciar presença e indicadores. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| commitment_id | Compromisso do tipo TREINO. | Treinador/RPC | Sim | Especialização | Evitar duplicação de data, horário e local. | Único; trigger valida commitment_type = TREINO. |
| --- | --- | --- | --- | --- | --- | --- |
| objective | Objetivo técnico ou tático do treino. | Treinador | Não | Planejamento | Explicar resultado esperado. | Não usar como avaliação individual automática. |
| --- | --- | --- | --- | --- | --- | --- |
| main_activity | Atividade principal planejada. | Treinador | Não | Planejamento | Organizar conteúdo. | Pode ser revisada até realização. |
| --- | --- | --- | --- | --- | --- | --- |
| collective_goals | Metas coletivas observáveis. | Treinador | Não | Planejamento | Direcionar execução. | Evitar julgamento pessoal. |
| --- | --- | --- | --- | --- | --- | --- |
| athlete_guidance | Orientação comunicável às atletas. | Treinador | Não | Comunicação | Preparar participantes. | Sem informações privadas de outras atletas. |
| --- | --- | --- | --- | --- | --- | --- |
| attendance_opened_at | Momento em que o treinador iniciou o registro factual. | Treinador/RPC | Não | Controle operacional | Distinguir planejamento de apuração. | Não cria presença automaticamente. |
| --- | --- | --- | --- | --- | --- | --- |
| attendance_closed_at | Momento de encerramento da apuração. | Treinador/RPC | Não | Controle operacional | Indicar consolidação. | Posterior a attendance_opened_at. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação da especialização. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração. | Trigger | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.training_sessions (  
id uuid primary key default gen_random_uuid(),  
commitment_id uuid references public.commitments(id) on delete restrict not null,  
objective text default null,  
main_activity text default null,  
collective_goals text default null,  
athlete_guidance text default null,  
attendance_opened_at timestamptz default null,  
attendance_closed_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint training_commitment_uq unique (commitment_id),  
constraint training_attendance_window_ck check (attendance_closed_at is null or attendance_opened_at is not null and attendance_closed_at >= attendance_opened_at)  
);

### Índices

create index training_commitment_idx on public.training_sessions (commitment_id);  
create index training_attendance_open_idx on public.training_sessions (attendance_opened_at) where attendance_opened_at is not null and attendance_closed_at is null;

## 9.10 public.request_definitions

Catálogo de tipos de solicitação operacional. Permite disponibilidade para treino hoje e novos fluxos futuros sem alterar o esquema.

### Regras da tabela

-   Definições e opções já usadas não devem ser apagadas.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | code | text | UK | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | name | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | subject_type | text | - | Não | 'COMMITMENT' |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | description | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | allow_justification | boolean | - | Não | true |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | active | boolean | - | Não | true |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.request_definitions | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da definição. | Sistema | Sim | Identidade técnica | Referenciar solicitações. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe proprietária do catálogo. | Treinador | Sim | Particionamento | Permitir vocabulário por equipe. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| code | Código estável, por exemplo TRAINING_AVAILABILITY. | Migração/Administrador | Sim | Contrato | Servir de chave funcional em RPCs. | Maiúsculo snake_case; não renomear após uso. |
| --- | --- | --- | --- | --- | --- | --- |
| name | Nome legível da solicitação. | Treinador | Sim | Apresentação | Exibir ao usuário. | Pode ser traduzido sem mudar code. |
| --- | --- | --- | --- | --- | --- | --- |
| subject_type | Tipo da entidade sobre a qual se pergunta. | Administrador | Sim | Extensibilidade | Permitir novos assuntos. | MVP usa COMMITMENT. |
| --- | --- | --- | --- | --- | --- | --- |
| description | Explicação operacional. | Treinador | Não | Orientação | Reduzir ambiguidade. | Não conter regra que pertença às opções. |
| --- | --- | --- | --- | --- | --- | --- |
| allow_justification | Autoriza justificativa opcional. | Administrador | Sim | Privacidade/UX | Controlar coleta mínima. | Justificativa continua privada e opcional. |
| --- | --- | --- | --- | --- | --- | --- |
| active | Disponibilidade para novas solicitações. | Administrador | Sim | Ciclo de vida | Descontinuar sem apagar histórico. | Inativo não pode gerar nova solicitação. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última atualização. | Trigger | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.request_definitions (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
code text not null,  
name text not null,  
subject_type text default 'COMMITMENT' not null,  
description text default null,  
allow_justification boolean default true not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint request_def_team_code_uq unique (team_id, code),  
constraint request_def_code_ck check (code ~ '^[A-Z][A-Z0-9_]{2,63}$')  
);

### Índices

create index request_def_active_idx on public.request_definitions (team_id, active);

## 9.11 public.request_definition_options

Opções válidas de cada tipo de solicitação. Representa SIM, NÃO e TALVEZ; ausência de resposta é derivada e nunca cadastrada como opção.

### Regras da tabela

-   SEM_RESPOSTA resulta da existência de destinatário sem resposta vigente.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | request_definition_id | uuid | FK → request_definitions.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | code | text | UK parcial | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | label | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | semantic_group | public.response_semantic_group | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | sort_order | smallint | - | Não | 0 |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | requires_justification | boolean | - | Não | false |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | active | boolean | - | Não | true |
| --- | --- | --- | --- | --- | --- |
| public.request_definition_options | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da opção. | Sistema | Sim | Identidade técnica | Referenciar resposta sem texto livre. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| request_definition_id | Definição à qual pertence. | Administrador | Sim | Relacionamento | Restringir opções ao contexto correto. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| code | Código estável, por exemplo YES, NO, UNCERTAIN. | Administrador | Sim | Contrato | Padronizar integrações e indicadores. | Nunca usar NOT_RESPONDED/SEM_RESPOSTA. |
| --- | --- | --- | --- | --- | --- | --- |
| label | Rótulo em português, por exemplo Sim, Não, Talvez. | Administrador | Sim | Apresentação | Exibir escolha. | Pode mudar sem alterar code. |
| --- | --- | --- | --- | --- | --- | --- |
| semantic_group | Grupo semântico AFFIRMATIVE, NEGATIVE ou UNCERTAIN. | Administrador | Sim | Análise | Permitir indicadores independentes do rótulo. | Não contém ausência de resposta. |
| --- | --- | --- | --- | --- | --- | --- |
| sort_order | Ordem de apresentação. | Administrador | Sim | UX | Organizar botões. | Não define prioridade esportiva. |
| --- | --- | --- | --- | --- | --- | --- |
| requires_justification | Indica se a interface deve solicitar justificativa. | Administrador | Sim | UX | Apoiar contexto quando autorizado. | Mesmo true, texto sensível não deve ser obrigatório; categoria pode satisfazer. |
| --- | --- | --- | --- | --- | --- | --- |
| active | Disponível para novas respostas. | Administrador | Sim | Ciclo de vida | Descontinuar sem invalidar histórico. | Opção inativa permanece referenciável. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.request_definition_options (  
id uuid primary key default gen_random_uuid(),  
request_definition_id uuid references public.request_definitions(id) on delete restrict not null,  
code text not null,  
label text not null,  
semantic_group public.response_semantic_group not null,  
sort_order smallint default 0 not null,  
requires_justification boolean default false not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
constraint request_option_code_uq unique (request_definition_id, code),  
constraint request_option_code_ck check (code ~ '^[A-Z][A-Z0-9_]{1,31}$')  
);

### Índices

create index request_options_definition_order_idx on public.request_definition_options (request_definition_id, active, sort_order);

## 9.12 public.operational_requests

Instância versionada de uma pergunta operacional enviada a atletas, normalmente vinculada a um compromisso.

### Regras da tabela

-   Não editar silenciosamente uma solicitação já publicada.
-   A resposta não se transforma em presença.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | definition_id | uuid | FK → request_definitions.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | commitment_id | uuid | FK → commitments.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | title | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | instructions | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | status | public.request_status | - | Não | 'RASCUNHO' |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | opens_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | deadline_at | timestamptz | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | closed_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | version | integer | - | Não | 1 |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | supersedes_request_id | uuid | FK → operational_requests.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | created_by | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | published_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.operational_requests | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da solicitação. | Sistema | Sim | Identidade técnica | Vincular destinatários e respostas. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe proprietária. | Sistema/RPC | Sim | Particionamento | Aplicar RLS. | Deve coincidir com definição e compromisso. |
| --- | --- | --- | --- | --- | --- | --- |
| definition_id | Tipo da solicitação. | Treinador | Sim | Semântica | Determinar opções e regras. | Definição ativa ao criar. |
| --- | --- | --- | --- | --- | --- | --- |
| commitment_id | Compromisso relacionado. | Treinador | Não | Contexto | Relacionar disponibilidade a treino ou evento. | Obrigatório quando subject_type = COMMITMENT. |
| --- | --- | --- | --- | --- | --- | --- |
| title | Título apresentado às atletas. | Treinador | Sim | Comunicação | Explicar ação esperada. | Curto e objetivo. |
| --- | --- | --- | --- | --- | --- | --- |
| instructions | Orientação complementar. | Treinador | Não | Comunicação | Reduzir dúvida. | Não deve expor respostas de outras atletas. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Estado da solicitação. | Treinador/RPC | Sim | Fluxo | Controlar abertura e encerramento. | Resposta só em ABERTA e dentro do prazo. |
| --- | --- | --- | --- | --- | --- | --- |
| opens_at | Início da janela. | Treinador | Sim | Temporal | Controlar quando responder. | Anterior ao deadline_at. |
| --- | --- | --- | --- | --- | --- | --- |
| deadline_at | Prazo de resposta. | Treinador | Sim | Temporal | Gerar pendências e impedir resposta tardia sem regra explícita. | Posterior a opens_at. |
| --- | --- | --- | --- | --- | --- | --- |
| closed_at | Momento efetivo de encerramento. | RPC | Não | Auditoria | Distinguir prazo de ação humana. | Preenchido ao encerrar/cancelar. |
| --- | --- | --- | --- | --- | --- | --- |
| version | Versão da solicitação. | Sistema/RPC | Sim | Versionamento | Preservar mudanças de prazo/texto. | Inteiro positivo; nova versão cria nova linha. |
| --- | --- | --- | --- | --- | --- | --- |
| supersedes_request_id | Versão anterior substituída. | RPC | Não | Versionamento | Manter cadeia histórica. | Mesma equipe/definição/assunto. |
| --- | --- | --- | --- | --- | --- | --- |
| created_by | Treinador criador. | Sistema/RPC | Sim | Autoridade | Rastrear decisão. | COACH da equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| published_at | Momento de abertura/publicação. | RPC | Não | Auditoria | Comprovar disponibilidade da pergunta. | Obrigatório quando ABERTA/ENCERRADA. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração permitida. | Trigger | Sim | Auditoria | Rastreabilidade. | Após publicação, mudanças materiais criam nova versão. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.operational_requests (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
definition_id uuid references public.request_definitions(id) on delete restrict not null,  
commitment_id uuid references public.commitments(id) on delete restrict default null,  
title text not null,  
instructions text default null,  
status public.request_status default 'RASCUNHO' not null,  
opens_at timestamptz default now() not null,  
deadline_at timestamptz not null,  
closed_at timestamptz default null,  
version integer default 1 not null,  
supersedes_request_id uuid references public.operational_requests(id) on delete restrict default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
published_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint operational_request_window_ck check (deadline_at > opens_at),  
constraint operational_request_version_ck check (version > 0),  
constraint operational_request_publish_ck check (status = 'RASCUNHO' or published_at is not null)  
);

### Índices

create index requests_team_status_deadline_idx on public.operational_requests (team_id, status, deadline_at);  
create index requests_commitment_idx on public.operational_requests (commitment_id, status);  
create unique index requests_subject_version_uq on public.operational_requests (definition_id, commitment_id, version) where commitment_id is not null;

## 9.13 public.request_recipients

Materializa quem deve responder a cada solicitação. É a origem do estado NÃO RESPONDEU quando não existe resposta válida.

### Regras da tabela

-   Não respondido = destinatário ativo sem resposta efetiva.
-   Lista de destinatários não é lista confirmada.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.request_recipients | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.request_recipients | request_id | uuid | FK → operational_requests.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_recipients | athlete_id | uuid | FK → athletes.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.request_recipients | sent_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.request_recipients | cancelled_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.request_recipients | delivery_channel | text | - | Não | 'APP' |
| --- | --- | --- | --- | --- | --- |
| public.request_recipients | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador do destinatário. | Sistema | Sim | Identidade técnica | Referenciar respostas e pendências. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| request_id | Solicitação enviada. | RPC | Sim | Relacionamento | Agrupar destinatários. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| athlete_id | Atleta destinatária. | RPC | Sim | Sujeito | Definir a pessoa que pode responder. | Deve ter vínculo aplicável ao compromisso. |
| --- | --- | --- | --- | --- | --- | --- |
| sent_at | Momento em que foi incluída. | Sistema | Sim | Entrega lógica | Comprovar criação da pendência. | Não equivale a entrega técnica nem leitura. |
| --- | --- | --- | --- | --- | --- | --- |
| cancelled_at | Momento em que deixou de ser destinatária. | Treinador/RPC | Não | Ciclo de vida | Remover obrigação sem apagar histórico. | Não apagar respostas existentes. |
| --- | --- | --- | --- | --- | --- | --- |
| delivery_channel | Canal pretendido de solicitação. | Sistema | Sim | Integração futura | Distinguir PWA de canais externos futuros. | MVP usa APP; não implica sincronização externa. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.request_recipients (  
id uuid primary key default gen_random_uuid(),  
request_id uuid references public.operational_requests(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
sent_at timestamptz default now() not null,  
cancelled_at timestamptz default null,  
delivery_channel text default 'APP' not null,  
created_at timestamptz default now() not null,  
constraint request_recipient_uq unique (request_id, athlete_id)  
);

### Índices

create index request_recipients_athlete_idx on public.request_recipients (athlete_id, cancelled_at, sent_at desc);  
create index request_recipients_request_idx on public.request_recipients (request_id, cancelled_at);

## 9.14 public.operational_responses

Declarações imutáveis das atletas. Cada nova resposta referencia a anterior; a resposta efetiva é calculada por view/RPC.

### Regras da tabela

-   Proibir UPDATE/DELETE.
-   Correção administrativa nunca altera esta linha.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | request_recipient_id | uuid | FK → request_recipients.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | option_id | uuid | FK → request_definition_options.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | responded_by_profile_id | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | responded_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | client_submission_id | uuid | UK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | supersedes_response_id | uuid | FK → operational_responses.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_responses | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da declaração. | Sistema | Sim | Identidade técnica | Preservar cada versão. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| request_recipient_id | Destinatário respondido. | RPC | Sim | Relacionamento | Assegurar autoria e escopo. | A conta deve pertencer à atleta destinatária. |
| --- | --- | --- | --- | --- | --- | --- |
| option_id | Opção escolhida. | Atleta via RPC | Sim | Conteúdo da resposta | Representar SIM/NÃO/TALVEZ sem texto livre. | Opção deve pertencer à definição da solicitação. |
| --- | --- | --- | --- | --- | --- | --- |
| responded_by_profile_id | Perfil autenticado que respondeu. | Sistema/RPC | Sim | Autoria | Comprovar declaração própria. | No fluxo normal deve ser o profile_id da atleta. |
| --- | --- | --- | --- | --- | --- | --- |
| responded_at | Momento da declaração. | Sistema | Sim | Temporal | Ordenar versões. | Timestamp do servidor. |
| --- | --- | --- | --- | --- | --- | --- |
| client_submission_id | Chave idempotente enviada pelo cliente. | Cliente/RPC | Sim | Resiliência | Evitar duplicidade por retry ou conexão instável. | Única globalmente. |
| --- | --- | --- | --- | --- | --- | --- |
| supersedes_response_id | Resposta anterior substituída pela atleta. | RPC | Não | Versionamento | Preservar histórico sem overwrite. | Mesma request_recipient_id. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Registro técnico. | Sistema | Sim | Auditoria | Rastreabilidade. | Geralmente igual ou posterior a responded_at. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.operational_responses (  
id uuid primary key default gen_random_uuid(),  
request_recipient_id uuid references public.request_recipients(id) on delete restrict not null,  
option_id uuid references public.request_definition_options(id) on delete restrict not null,  
responded_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
responded_at timestamptz default now() not null,  
client_submission_id uuid default gen_random_uuid() not null,  
supersedes_response_id uuid references public.operational_responses(id) on delete restrict default null,  
created_at timestamptz default now() not null,  
constraint operational_response_client_uq unique (client_submission_id)  
);

### Índices

create index responses_recipient_time_idx on public.operational_responses (request_recipient_id, responded_at desc, created_at desc);  
create index responses_supersedes_idx on public.operational_responses (supersedes_response_id) where supersedes_response_id is not null;

## 9.15 public.justification_categories

Vocabulário mínimo e controlado de justificativas. Reduz texto livre e permite privacidade por desenho.

### Regras da tabela

-   Categoria e texto nunca aparecem em listas compartilhadas.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | code | text | UK | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | label | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | description | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | sensitive | boolean | - | Não | false |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | sort_order | smallint | - | Não | 0 |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | active | boolean | - | Não | true |
| --- | --- | --- | --- | --- | --- |
| public.justification_categories | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da categoria. | Sistema | Sim | Identidade técnica | Referenciar justificativas. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe proprietária. | Administrador | Sim | Particionamento | Permitir catálogo controlado. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| code | Código estável, por exemplo LOGISTICA ou SAUDE_PRIVADA. | Administrador | Sim | Contrato | Padronizar seleção. | Não deve revelar detalhe sensível por si só. |
| --- | --- | --- | --- | --- | --- | --- |
| label | Rótulo apresentado à atleta. | Administrador | Sim | UX | Facilitar resposta mínima. | Linguagem neutra e não julgadora. |
| --- | --- | --- | --- | --- | --- | --- |
| description | Explicação opcional. | Administrador | Não | Orientação | Esclarecer uso. | Não induzir exposição indevida. |
| --- | --- | --- | --- | --- | --- | --- |
| sensitive | Sinaliza categoria potencialmente sensível. | Administrador | Sim | Privacidade | Apoiar mascaramento e retenção. | Não torna o dado público em nenhum cenário. |
| --- | --- | --- | --- | --- | --- | --- |
| sort_order | Ordem na interface. | Administrador | Sim | UX | Organizar opções. | Sem efeito esportivo. |
| --- | --- | --- | --- | --- | --- | --- |
| active | Disponível para novos registros. | Administrador | Sim | Ciclo de vida | Descontinuar sem apagar. | Histórico continua válido. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.justification_categories (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
code text not null,  
label text not null,  
description text default null,  
sensitive boolean default false not null,  
sort_order smallint default 0 not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
constraint justification_category_uq unique (team_id, code)  
);

### Índices

create index justification_categories_active_idx on public.justification_categories (team_id, active, sort_order);

## 9.16 private.response_justifications

Conteúdo privado opcional associado a uma resposta. Fica fora do schema exposto e só é acessado por RPCs autorizadas.

### Regras da tabela

-   Sem grants diretos para authenticated/anon.
-   Leitura restrita à própria atleta e treinador autorizado por função SECURITY DEFINER.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| private.response_justifications | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| private.response_justifications | response_id | uuid | FK/UK → operational_responses.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| private.response_justifications | category_id | uuid | FK → justification_categories.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| private.response_justifications | free_text | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| private.response_justifications | submitted_by_profile_id | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| private.response_justifications | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| private.response_justifications | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da justificativa. | Sistema | Sim | Identidade técnica | Referenciar registro privado. | Imutável em autoria; alteração controlada. |
| --- | --- | --- | --- | --- | --- | --- |
| response_id | Resposta justificada. | RPC | Sim | Relacionamento | Manter conteúdo separado da resposta pública. | Uma justificativa por versão de resposta. |
| --- | --- | --- | --- | --- | --- | --- |
| category_id | Categoria controlada escolhida. | Atleta via RPC | Não | Minimização | Evitar texto livre quando suficiente. | Deve pertencer à mesma equipe da solicitação. |
| --- | --- | --- | --- | --- | --- | --- |
| free_text | Observação curta opcional. | Atleta via RPC | Não | Contexto privado | Permitir detalhe estritamente necessário. | Limite recomendado de 500 caracteres; nunca expor em views compartilhadas. |
| --- | --- | --- | --- | --- | --- | --- |
| submitted_by_profile_id | Perfil que forneceu o conteúdo. | Sistema/RPC | Sim | Autoria | Comprovar origem. | Deve ser autora da resposta. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração autorizada. | Trigger/RPC | Sim | Auditoria | Rastreabilidade. | Não usar como histórico; revisão futura pode adotar versionamento. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table private.response_justifications (  
id uuid primary key default gen_random_uuid(),  
response_id uuid references public.operational_responses(id) on delete restrict not null,  
category_id uuid references public.justification_categories(id) on delete restrict default null,  
free_text text default null,  
submitted_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint response_justification_response_uq unique (response_id),  
constraint response_justification_content_ck check (category_id is not null or nullif(btrim(free_text), '') is not null),  
constraint response_justification_length_ck check (free_text is null or char_length(free_text) <= 500)  
);

### Índices

create index response_justifications_category_idx on private.response_justifications (category_id) where category_id is not null;

## 9.17 public.response_corrections

Correção administrativa append-only aplicada sobre uma resposta, sem modificar a declaração original da atleta.

### Regras da tabela

-   Proibir UPDATE/DELETE.
-   A view efetiva mostra a correção, mas conserva autoria separada.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | request_recipient_id | uuid | FK → request_recipients.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | response_id | uuid | FK → operational_responses.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | action | public.correction_action | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | replacement_option_id | uuid | FK → request_definition_options.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | reason | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | corrected_by_profile_id | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | corrected_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.response_corrections | supersedes_correction_id | uuid | FK → response_corrections.id | Sim | null |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da correção. | Sistema | Sim | Identidade técnica | Rastrear intervenção humana. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| request_recipient_id | Destinatário cujo estado efetivo é corrigido. | Treinador/RPC | Sim | Relacionamento | Aplicar correção ao fluxo correto. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| response_id | Resposta original relacionada, quando existe. | Treinador/RPC | Não | Referência | Explicar qual declaração motivou a correção. | Pode ser nulo para registrar resposta administrativa ausente, se autorizado. |
| --- | --- | --- | --- | --- | --- | --- |
| action | Ação REPLACE ou VOID. | Treinador/RPC | Sim | Semântica | Determinar efeito. | REPLACE exige replacement_option_id; VOID não. |
| --- | --- | --- | --- | --- | --- | --- |
| replacement_option_id | Opção efetiva definida administrativamente. | Treinador/RPC | Não | Correção | Corrigir estado sem falsificar autoria. | Somente em REPLACE e pertencente à mesma definição. |
| --- | --- | --- | --- | --- | --- | --- |
| reason | Motivo administrativo explícito. | Treinador | Sim | Auditoria | Justificar intervenção. | Não copiar justificativa privada da atleta. |
| --- | --- | --- | --- | --- | --- | --- |
| corrected_by_profile_id | Treinador responsável. | Sistema/RPC | Sim | Autoridade | Rastrear decisão. | COACH AAL2 da equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| corrected_at | Momento da correção. | Sistema | Sim | Temporal | Determinar correção vigente. | Timestamp do servidor. |
| --- | --- | --- | --- | --- | --- | --- |
| supersedes_correction_id | Correção anterior substituída. | RPC | Não | Versionamento | Preservar cadeia administrativa. | Mesmo request_recipient_id. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.response_corrections (  
id uuid primary key default gen_random_uuid(),  
request_recipient_id uuid references public.request_recipients(id) on delete restrict not null,  
response_id uuid references public.operational_responses(id) on delete restrict default null,  
action public.correction_action not null,  
replacement_option_id uuid references public.request_definition_options(id) on delete restrict default null,  
reason text not null,  
corrected_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
corrected_at timestamptz default now() not null,  
supersedes_correction_id uuid references public.response_corrections(id) on delete restrict default null,  
constraint response_correction_action_ck check ((action = 'REPLACE' and replacement_option_id is not null) or (action = 'VOID' and replacement_option_id is null))  
);

### Índices

create index response_corrections_recipient_time_idx on public.response_corrections (request_recipient_id, corrected_at desc);  
create index response_corrections_response_idx on public.response_corrections (response_id) where response_id is not null;

## 9.18 public.operational_lists

Cabeçalho versionado de projeções operacionais, como lista prevista de treino. Suporta publicação, substituição, encerramento e decisão explícita de não publicar.

### Regras da tabela

-   Publicação é projeção, não fato.
-   Versão publicada não deve ser editada; nova lista a substitui.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | commitment_id | uuid | FK → commitments.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | list_type | public.operational_list_type | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | version | integer | - | Não | 1 |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | status | public.list_publication_status | - | Não | 'RASCUNHO' |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | title | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | published_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | not_published_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | supersedes_list_id | uuid | FK → operational_lists.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | created_by | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_lists | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da versão da lista. | Sistema | Sim | Identidade técnica | Referenciar membros e publicação. | Imutável após publicação. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe proprietária. | Sistema/RPC | Sim | Particionamento | Aplicar RLS. | Mesma equipe do compromisso. |
| --- | --- | --- | --- | --- | --- | --- |
| commitment_id | Compromisso ao qual a lista se refere. | Treinador | Sim | Contexto | Distinguir previsão por evento. | Lista não comprova presença ou participação. |
| --- | --- | --- | --- | --- | --- | --- |
| list_type | Tipo da projeção. | Treinador | Sim | Semântica | Permitir listas de treino e extensões futuras. | MVP utiliza TRAINING_EXPECTED; tipos futuros exigem decisão. |
| --- | --- | --- | --- | --- | --- | --- |
| version | Número sequencial da versão. | Sistema/RPC | Sim | Versionamento | Preservar listas substituídas. | Inteiro positivo e único no compromisso/tipo. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Estado de publicação. | Treinador/RPC | Sim | Fluxo | Controlar visibilidade e decisão de não publicar. | Atletas veem somente PUBLICADA. |
| --- | --- | --- | --- | --- | --- | --- |
| title | Título público da lista. | Treinador | Sim | Apresentação | Contextualizar projeção. | Sem justificativas privadas. |
| --- | --- | --- | --- | --- | --- | --- |
| published_at | Momento da publicação. | RPC | Não | Auditoria | Comprovar vigência. | Obrigatório em PUBLICADA/SUBSTITUIDA/ENCERRADA. |
| --- | --- | --- | --- | --- | --- | --- |
| not_published_at | Momento da decisão de não publicar. | RPC | Não | Auditoria | Representar ausência intencional de lista. | Obrigatório em NAO_PUBLICADA. |
| --- | --- | --- | --- | --- | --- | --- |
| supersedes_list_id | Versão anterior substituída. | RPC | Não | Versionamento | Preservar cadeia. | Mesmo compromisso e tipo. |
| --- | --- | --- | --- | --- | --- | --- |
| created_by | Treinador criador. | Sistema/RPC | Sim | Autoridade | Rastrear decisão. | COACH da equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.operational_lists (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
commitment_id uuid references public.commitments(id) on delete restrict not null,  
list_type public.operational_list_type not null,  
version integer default 1 not null,  
status public.list_publication_status default 'RASCUNHO' not null,  
title text not null,  
published_at timestamptz default null,  
not_published_at timestamptz default null,  
supersedes_list_id uuid references public.operational_lists(id) on delete restrict default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
constraint operational_list_version_ck check (version > 0),  
constraint operational_list_version_uq unique (commitment_id, list_type, version),  
constraint operational_list_dates_ck check ((status = 'NAO_PUBLICADA' and not_published_at is not null) or status <> 'NAO_PUBLICADA')  
);

### Índices

create index operational_lists_current_idx on public.operational_lists (commitment_id, list_type, version desc);  
create unique index operational_lists_one_published_uq on public.operational_lists (commitment_id, list_type) where status = 'PUBLICADA';

## 9.19 public.operational_list_members

Membros de uma versão de lista. Mantém snapshots mínimos de nome e função para preservar exatamente o que foi publicado.

### Regras da tabela

-   Não inclui resposta, justificativa ou presença.
-   Snapshots são deliberadamente denormalizados.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | list_id | uuid | FK → operational_lists.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | athlete_id | uuid | FK → athletes.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | roster_membership_id | uuid | FK → athlete_roster_memberships.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | display_name_snapshot | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | broad_function_snapshot | public.broad_player_function | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | sort_order | integer | - | Não | 0 |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | public_note | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.operational_list_members | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador do membro. | Sistema | Sim | Identidade técnica | Referenciar item da lista. | Imutável com a versão. |
| --- | --- | --- | --- | --- | --- | --- |
| list_id | Versão da lista. | RPC | Sim | Relacionamento | Agrupar projeção. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| athlete_id | Atleta incluída. | Treinador/RPC | Sim | Identidade | Relacionar ao cadastro. | Uma vez por versão. |
| --- | --- | --- | --- | --- | --- | --- |
| roster_membership_id | Vínculo de elenco utilizado na composição. | RPC | Não | Proveniência | Explicar função e elegibilidade usadas. | Pode ser nulo em importação excepcional validada. |
| --- | --- | --- | --- | --- | --- | --- |
| display_name_snapshot | Nome exibido no momento da publicação. | RPC | Sim | Snapshot | Preservar conteúdo histórico. | Não atualizar quando cadastro mudar. |
| --- | --- | --- | --- | --- | --- | --- |
| broad_function_snapshot | Função ampla usada na lista. | RPC | Sim | Snapshot | Permitir cobertura histórica. | Nunca ESPECIALISTA/CORINGA. |
| --- | --- | --- | --- | --- | --- | --- |
| sort_order | Ordem de exibição. | Treinador/RPC | Sim | Apresentação | Produzir lista determinística. | Não representa titularidade ou prioridade esportiva. |
| --- | --- | --- | --- | --- | --- | --- |
| public_note | Observação explicitamente publicável. | Treinador | Não | Comunicação | Acrescentar instrução mínima. | Nunca copiar justificativa ou dado sensível. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação do item. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.operational_list_members (  
id uuid primary key default gen_random_uuid(),  
list_id uuid references public.operational_lists(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
roster_membership_id uuid references public.athlete_roster_memberships(id) on delete restrict default null,  
display_name_snapshot text not null,  
broad_function_snapshot public.broad_player_function not null,  
sort_order integer default 0 not null,  
public_note text default null,  
created_at timestamptz default now() not null,  
constraint operational_list_member_uq unique (list_id, athlete_id)  
);

### Índices

create index operational_list_members_order_idx on public.operational_list_members (list_id, sort_order, display_name_snapshot);  
create index operational_list_members_athlete_idx on public.operational_list_members (athlete_id, list_id);

## 9.20 public.attendance_records

Registro factual append-only de presença em treino. Ausência de linha significa “não registrado”, nunca ausência automática.

### Regras da tabela

-   Proibir UPDATE/DELETE.
-   Indicadores usam somente a última cadeia válida por treino/atleta.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | training_session_id | uuid | FK → training_sessions.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | athlete_id | uuid | FK → athletes.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | status | public.attendance_status | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | arrived_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | departed_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | recorded_by_profile_id | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | recorded_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | client_record_id | uuid | UK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | supersedes_record_id | uuid | FK → attendance_records.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | source_note | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.attendance_records | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da versão do registro. | Sistema | Sim | Identidade técnica | Preservar apurações e correções. | Imutável. |
| --- | --- | --- | --- | --- | --- | --- |
| training_session_id | Treino observado. | Treinador/RPC | Sim | Contexto | Vincular fato à sessão. | Compromisso deve estar realizado ou em apuração autorizada. |
| --- | --- | --- | --- | --- | --- | --- |
| athlete_id | Atleta observada. | Treinador/RPC | Sim | Sujeito | Registrar presença individual. | Não inferir a partir de lista ou resposta. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Fato observado: PRESENTE, AUSENTE, ATRASADA, SAIDA_ANTECIPADA ou DISPENSADA. | Treinador/RPC | Sim | Fato operacional | Consolidar comparecimento. | AUSENTE só após verificação humana. |
| --- | --- | --- | --- | --- | --- | --- |
| arrived_at | Horário de chegada quando relevante. | Treinador | Não | Detalhe factual | Apoiar atraso. | Compatível com o período do treino. |
| --- | --- | --- | --- | --- | --- | --- |
| departed_at | Horário de saída quando relevante. | Treinador | Não | Detalhe factual | Apoiar saída antecipada. | Posterior a arrived_at quando ambos preenchidos. |
| --- | --- | --- | --- | --- | --- | --- |
| recorded_by_profile_id | Treinador que registrou. | Sistema/RPC | Sim | Autoria | Comprovar autoridade. | COACH AAL2. |
| --- | --- | --- | --- | --- | --- | --- |
| recorded_at | Momento do registro. | Sistema | Sim | Temporal | Determinar versão efetiva. | Timestamp do servidor. |
| --- | --- | --- | --- | --- | --- | --- |
| client_record_id | Chave idempotente do comando. | Cliente/RPC | Sim | Resiliência | Evitar duplicatas. | Única. |
| --- | --- | --- | --- | --- | --- | --- |
| supersedes_record_id | Registro anterior corrigido. | RPC | Não | Versionamento | Preservar histórico. | Mesmo treino e atleta. |
| --- | --- | --- | --- | --- | --- | --- |
| source_note | Nota curta da apuração. | Treinador | Não | Proveniência | Explicar correção excepcional. | Sem justificativa privada da atleta. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação técnica. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.attendance_records (  
id uuid primary key default gen_random_uuid(),  
training_session_id uuid references public.training_sessions(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
status public.attendance_status not null,  
arrived_at timestamptz default null,  
departed_at timestamptz default null,  
recorded_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
recorded_at timestamptz default now() not null,  
client_record_id uuid default gen_random_uuid() not null,  
supersedes_record_id uuid references public.attendance_records(id) on delete restrict default null,  
source_note text default null,  
created_at timestamptz default now() not null,  
constraint attendance_client_record_uq unique (client_record_id),  
constraint attendance_time_ck check (departed_at is null or arrived_at is null or departed_at >= arrived_at)  
);

### Índices

create index attendance_training_athlete_time_idx on public.attendance_records (training_session_id, athlete_id, recorded_at desc);  
create index attendance_athlete_time_idx on public.attendance_records (athlete_id, recorded_at desc);  
create index attendance_supersedes_idx on public.attendance_records (supersedes_record_id) where supersedes_record_id is not null;

## 9.21 public.communications

Mensagem operacional criada no produto. Separa conteúdo da entrega individual, leitura e ciência.

### Regras da tabela

-   Mensagem publicada é independente de entrega e leitura.
-   Integrações externas não fazem parte do MVP.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.communications | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.communications | team_id | uuid | FK → teams.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.communications | commitment_id | uuid | FK → commitments.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.communications | title | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.communications | body | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.communications | audience_type | public.communication_audience_type | - | Não | 'SELECTED' |
| --- | --- | --- | --- | --- | --- |
| public.communications | status | public.communication_status | - | Não | 'RASCUNHO' |
| --- | --- | --- | --- | --- | --- |
| public.communications | valid_from | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.communications | valid_until | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.communications | published_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.communications | created_by | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.communications | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.communications | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador da comunicação. | Sistema | Sim | Identidade técnica | Referenciar destinatários. | Imutável após publicação salvo arquivamento. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe proprietária. | Treinador | Sim | Particionamento | Aplicar RLS. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| commitment_id | Compromisso relacionado. | Treinador | Não | Contexto | Vincular aviso a treino/evento. | Pode ser nulo para aviso geral. |
| --- | --- | --- | --- | --- | --- | --- |
| title | Título da mensagem. | Treinador | Sim | Comunicação | Facilitar leitura. | Claro e objetivo. |
| --- | --- | --- | --- | --- | --- | --- |
| body | Conteúdo da mensagem. | Treinador | Sim | Comunicação | Transmitir orientação. | Não incluir justificativas ou dados privados de atletas. |
| --- | --- | --- | --- | --- | --- | --- |
| audience_type | Forma de seleção de destinatários. | Treinador | Sim | Distribuição | Distinguir todas as atletas ativas de seleção explícita. | Destinatários devem ser materializados em communication_recipients. |
| --- | --- | --- | --- | --- | --- | --- |
| status | Estado da comunicação. | Treinador/RPC | Sim | Fluxo | Controlar publicação. | Destinatários só veem PUBLICADA. |
| --- | --- | --- | --- | --- | --- | --- |
| valid_from | Início de validade. | Treinador | Sim | Temporal | Controlar inbox. | Pode ser futura. |
| --- | --- | --- | --- | --- | --- | --- |
| valid_until | Fim de validade. | Treinador | Não | Temporal | Retirar de destaque sem apagar. | Posterior a valid_from. |
| --- | --- | --- | --- | --- | --- | --- |
| published_at | Momento de publicação. | RPC | Não | Auditoria | Comprovar disponibilização. | Obrigatório quando PUBLICADA/ARQUIVADA. |
| --- | --- | --- | --- | --- | --- | --- |
| created_by | Treinador autor. | Sistema/RPC | Sim | Autoria | Rastrear decisão. | COACH da equipe. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração permitida. | Trigger | Sim | Auditoria | Rastreabilidade. | Após publicação, mudança material deve gerar nova comunicação. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.communications (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
commitment_id uuid references public.commitments(id) on delete restrict default null,  
title text not null,  
body text not null,  
audience_type public.communication_audience_type default 'SELECTED' not null,  
status public.communication_status default 'RASCUNHO' not null,  
valid_from timestamptz default now() not null,  
valid_until timestamptz default null,  
published_at timestamptz default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint communication_validity_ck check (valid_until is null or valid_until > valid_from),  
constraint communication_publish_ck check (status = 'RASCUNHO' or published_at is not null)  
);

### Índices

create index communications_team_validity_idx on public.communications (team_id, status, valid_from, valid_until);  
create index communications_commitment_idx on public.communications (commitment_id) where commitment_id is not null;

## 9.22 public.communication_recipients

Estado individual de distribuição de uma comunicação: entrega, visualização e ciência são fatos distintos.

### Regras da tabela

-   Somente o próprio destinatário marca viewed/acknowledged.
-   Treinador lê estado, não altera ciência em nome da atleta.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | id | uuid | PK | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | communication_id | uuid | FK → communications.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | profile_id | uuid | FK → profiles.id | Não | - |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | athlete_id | uuid | FK → athletes.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | delivery_status | public.delivery_status | - | Não | 'PENDING' |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | delivered_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | viewed_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | acknowledged_at | timestamptz | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | created_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| public.communication_recipients | updated_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador do destinatário. | Sistema | Sim | Identidade técnica | Referenciar estado individual. | Imutável no vínculo; timestamps avançam via RPC. |
| --- | --- | --- | --- | --- | --- | --- |
| communication_id | Comunicação distribuída. | RPC | Sim | Relacionamento | Agrupar destinatários. | Obrigatório. |
| --- | --- | --- | --- | --- | --- | --- |
| profile_id | Conta destinatária. | RPC | Sim | Sujeito | Permitir inbox e leitura própria. | Perfil ativo no momento da distribuição. |
| --- | --- | --- | --- | --- | --- | --- |
| athlete_id | Atleta associada ao perfil, quando aplicável. | RPC | Não | Domínio | Facilitar relatórios por atleta. | Deve corresponder ao profile_id. |
| --- | --- | --- | --- | --- | --- | --- |
| delivery_status | Resultado da entrega lógica/técnica. | Sistema/RPC | Sim | Entrega | Distinguir pendente, entregue e falha. | ENTREGUE não significa visualizada. |
| --- | --- | --- | --- | --- | --- | --- |
| delivered_at | Momento da entrega. | Sistema | Não | Evidência técnica | Medir distribuição. | Preenchido quando DELIVERED. |
| --- | --- | --- | --- | --- | --- | --- |
| viewed_at | Primeira abertura pela pessoa. | Própria pessoa via RPC | Não | Leitura | Comprovar visualização mínima. | Não atualizar em reaberturas; não implica concordância. |
| --- | --- | --- | --- | --- | --- | --- |
| acknowledged_at | Momento de ciência explícita. | Própria pessoa via RPC | Não | Ciência | Registrar confirmação consciente. | Posterior ou igual a viewed_at quando ambos existem. |
| --- | --- | --- | --- | --- | --- | --- |
| created_at | Criação do destinatário. | Sistema | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |
| updated_at | Última alteração de estado. | Trigger | Sim | Auditoria | Rastreabilidade. | Automático. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table public.communication_recipients (  
id uuid primary key default gen_random_uuid(),  
communication_id uuid references public.communications(id) on delete restrict not null,  
profile_id uuid references public.profiles(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict default null,  
delivery_status public.delivery_status default 'PENDING' not null,  
delivered_at timestamptz default null,  
viewed_at timestamptz default null,  
acknowledged_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint communication_recipient_uq unique (communication_id, profile_id),  
constraint communication_ack_ck check (acknowledged_at is null or viewed_at is null or acknowledged_at >= viewed_at)  
);

### Índices

create index communication_recipients_profile_idx on public.communication_recipients (profile_id, viewed_at, acknowledged_at);  
create index communication_recipients_comm_status_idx on public.communication_recipients (communication_id, delivery_status);

## 9.23 audit.audit_events

Log técnico append-only para alterações e eventos de segurança. Complementa, mas não substitui, históricos de domínio.

### Regras da tabela

-   Sem UPDATE/DELETE.
-   Sem INSERT direto do cliente.
-   Retenção e exportação devem ser formalizadas antes de dados reais.

### Estrutura física

| **Nome da Tabela** | **Nome da Coluna** | **Tipo (PostgreSQL)** | **Chave (PK/FK)** | **Nulável** | **Default** |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | id | bigint | PK | Não | generated always as identity |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | team_id | uuid | FK lógico → teams.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | actor_profile_id | uuid | FK lógico → profiles.id | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | actor_auth_uid | uuid | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | event_type | text | - | Não | - |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | entity_schema | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | entity_table | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | entity_id | text | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | occurred_at | timestamptz | - | Não | now() |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | correlation_id | uuid | - | Não | gen_random_uuid() |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | before_data | jsonb | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | after_data | jsonb | - | Sim | null |
| --- | --- | --- | --- | --- | --- |
| audit.audit_events | metadata | jsonb | - | Não | '{}'::jsonb |
| --- | --- | --- | --- | --- | --- |

### Semântica e preenchimento

| **Coluna** | **Descrição individual** | **Regras e tipo de preenchimento** | **Obrigatório** | **Papel e função** | **Objetivo do campo** | **Regras de negócio** |
| --- | --- | --- | --- | --- | --- | --- |
| id | Identificador sequencial do evento. | Sistema/Trigger | Sim | Identidade técnica | Ordenar e referenciar auditoria. | Não expor como chave de negócio. |
| --- | --- | --- | --- | --- | --- | --- |
| team_id | Equipe relacionada, quando aplicável. | Trigger/RPC | Não | Particionamento | Permitir consulta de auditoria por equipe. | Pode ser nulo para evento global de autenticação. |
| --- | --- | --- | --- | --- | --- | --- |
| actor_profile_id | Perfil de domínio que atuou. | Sistema | Não | Autoria | Identificar responsável. | Pode ser nulo para service role; registrar em metadata. |
| --- | --- | --- | --- | --- | --- | --- |
| actor_auth_uid | UUID recebido do contexto Auth. | Sistema | Não | Segurança | Preservar identidade técnica mesmo se perfil mudar. | Não é segredo. |
| --- | --- | --- | --- | --- | --- | --- |
| event_type | Código do evento. | Trigger/RPC | Sim | Semântica | Classificar ação. | Código estável snake_case ou UPPER_SNAKE_CASE. |
| --- | --- | --- | --- | --- | --- | --- |
| entity_schema | Schema da entidade afetada. | Trigger | Não | Referência | Localizar origem. | Não necessário em evento sem entidade. |
| --- | --- | --- | --- | --- | --- | --- |
| entity_table | Tabela da entidade afetada. | Trigger | Não | Referência | Localizar origem. | - |
| --- | --- | --- | --- | --- | --- | --- |
| entity_id | ID serializado da entidade. | Trigger | Não | Referência | Permitir investigação. | Texto para aceitar UUID/bigint. |
| --- | --- | --- | --- | --- | --- | --- |
| occurred_at | Momento do evento. | Sistema | Sim | Temporal | Ordenar auditoria. | UTC. |
| --- | --- | --- | --- | --- | --- | --- |
| correlation_id | Identificador de uma operação distribuída. | RPC/Trigger | Sim | Observabilidade | Agrupar eventos do mesmo comando. | Pode vir do cliente confiável ou ser gerado no servidor. |
| --- | --- | --- | --- | --- | --- | --- |
| before_data | Snapshot anterior filtrado. | Trigger | Não | Auditoria | Investigar alteração. | Excluir segredos, tokens e texto de justificativa privada. |
| --- | --- | --- | --- | --- | --- | --- |
| after_data | Snapshot posterior filtrado. | Trigger | Não | Auditoria | Investigar alteração. | Mesma regra de minimização. |
| --- | --- | --- | --- | --- | --- | --- |
| metadata | Contexto adicional não sensível. | Sistema | Sim | Observabilidade | Registrar origem, versão do app ou service role. | Não armazenar payload bruto sensível. |
| --- | --- | --- | --- | --- | --- | --- |

### SQL da tabela

create table audit.audit_events (  
id bigint generated always as identity primary key,  
team_id uuid default null,  
actor_profile_id uuid default null,  
actor_auth_uid uuid default null,  
event_type text not null,  
entity_schema text default null,  
entity_table text default null,  
entity_id text default null,  
occurred_at timestamptz default now() not null,  
correlation_id uuid default gen_random_uuid() not null,  
before_data jsonb default null,  
after_data jsonb default null,  
metadata jsonb default '{}'::jsonb not null  
);

### Índices

create index audit_events_team_time_idx on audit.audit_events (team_id, occurred_at desc);  
create index audit_events_entity_idx on audit.audit_events (entity_schema, entity_table, entity_id, occurred_at desc);  
create index audit_events_actor_time_idx on audit.audit_events (actor_profile_id, occurred_at desc);  
create index audit_events_correlation_idx on audit.audit_events (correlation_id);

# 10. Views e indicadores derivados

As views abaixo substituem abas de indicadores, calendário e exportação. São recalculadas a partir dos fatos e devem usar security_invoker=true para respeitar RLS.

| **View** | **Finalidade** |
| --- | --- |
| v_current_roster | Estado atual do elenco por temporada. |
| --- | --- |
| v_request_recipient_state | Resposta efetiva, correção e pendência sem expor justificativa. |
| --- | --- |
| v_calendar | Agenda consolidada de commitments e detalhes de treino. |
| --- | --- |
| v_current_published_lists | Projeção mínima da lista vigente. |
| --- | --- |
| v_training_expected_composition | Contagem esperada por função ampla. |
| --- | --- |
| v_function_coverage | SIM/NÃO/TALVEZ/NÃO RESPONDEU por função. |
| --- | --- |
| v_availability_attendance_divergence | Diferença descritiva entre declaração e fato posterior. |
| --- | --- |
| v_athlete_inbox | Solicitações e comunicações da própria atleta. |
| --- | --- |
| v_coach_pending_actions | Pendências operacionais do treinador. |
| --- | --- |
| v_operational_state | Resumo do estado operacional por equipe. |
| --- | --- |

-- 0004_views.sql  
create or replace view public.v_current_roster  
with (security_invoker = true)  
as  
select  
arm.id as roster_membership_id,  
a.team_id,  
arm.season_id,  
a.id as athlete_id,  
a.profile_id,  
a.legacy_athlete_id,  
a.display_name,  
arm.status,  
arm.broad_function,  
arm.shirt_number,  
arm.starts_on,  
arm.ends_on  
from public.athlete_roster_memberships arm  
join public.athletes a on a.id = arm.athlete_id  
where arm.starts_on <= current_date  
and (arm.ends_on is null or arm.ends_on >= current_date)  
and arm.status in ('ATIVA', 'INATIVA_TEMPORARIA');  
  
create or replace view public.v_request_recipient_state  
with (security_invoker = true)  
as  
with latest_response as (  
select distinct on (request_recipient_id)  
request_recipient_id, id as response_id, option_id,  
responded_by_profile_id, responded_at  
from public.operational_responses  
order by request_recipient_id, responded_at desc, created_at desc  
), latest_correction as (  
select distinct on (request_recipient_id)  
request_recipient_id, id as correction_id, action,  
replacement_option_id, corrected_at  
from public.response_corrections  
order by request_recipient_id, corrected_at desc  
)  
select  
rr.id as request_recipient_id,  
r.team_id,  
r.id as request_id,  
r.commitment_id,  
rr.athlete_id,  
lr.response_id,  
lc.correction_id,  
case  
when rr.cancelled_at is not null then 'CANCELLED'  
when lc.action = 'VOID' then 'NOT_RESPONDED'  
when lc.action = 'REPLACE' then co.code  
when lr.response_id is null then 'NOT_RESPONDED'  
else ro.code  
end as effective_option_code,  
case  
when lc.action = 'REPLACE' then co.semantic_group  
when lc.action = 'VOID' or lr.response_id is null then null  
else ro.semantic_group  
end as effective_semantic_group,  
lr.responded_at,  
lc.corrected_at,  
r.deadline_at,  
(lr.response_id is null and lc.correction_id is null and rr.cancelled_at is null) as pending  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
left join latest_response lr on lr.request_recipient_id = rr.id  
left join latest_correction lc on lc.request_recipient_id = rr.id  
left join public.request_definition_options ro on ro.id = lr.option_id  
left join public.request_definition_options co on co.id = lc.replacement_option_id;  
  
create or replace view public.v_calendar  
with (security_invoker = true)  
as  
select  
c.id as commitment_id,  
c.team_id,  
c.season_id,  
c.commitment_type,  
c.title,  
c.starts_at,  
c.ends_at,  
c.timezone,  
c.location_name,  
c.status,  
c.published_at,  
c.cancelled_at,  
ts.id as training_session_id,  
ts.objective,  
ts.main_activity,  
ts.collective_goals,  
ts.athlete_guidance  
from public.commitments c  
left join public.training_sessions ts on ts.commitment_id = c.id;  
  
create or replace view public.v_current_published_lists  
with (security_invoker = true)  
as  
select  
l.id as list_id,  
l.team_id,  
l.commitment_id,  
l.list_type,  
l.version,  
l.title,  
l.published_at,  
m.athlete_id,  
m.display_name_snapshot,  
m.broad_function_snapshot,  
m.sort_order,  
m.public_note  
from public.operational_lists l  
join public.operational_list_members m on m.list_id = l.id  
where l.status = 'PUBLICADA';  
  
create or replace view public.v_training_expected_composition  
with (security_invoker = true)  
as  
select  
l.team_id,  
l.commitment_id,  
m.broad_function_snapshot as broad_function,  
count(*)::integer as expected_athletes  
from public.operational_lists l  
join public.operational_list_members m on m.list_id = l.id  
where l.status = 'PUBLICADA'  
and l.list_type = 'TRAINING_EXPECTED'  
group by l.team_id, l.commitment_id, m.broad_function_snapshot;  
  
create or replace view public.v_function_coverage  
with (security_invoker = true)  
as  
select  
s.team_id,  
s.request_id,  
s.commitment_id,  
r.broad_function,  
count(*) filter (where s.effective_semantic_group = 'AFFIRMATIVE')::integer as affirmative,  
count(*) filter (where s.effective_semantic_group = 'UNCERTAIN')::integer as uncertain,  
count(*) filter (where s.effective_semantic_group = 'NEGATIVE')::integer as negative,  
count(*) filter (where s.effective_option_code = 'NOT_RESPONDED')::integer as not_responded  
from public.v_request_recipient_state s  
join public.v_current_roster r on r.athlete_id = s.athlete_id  
group by s.team_id, s.request_id, s.commitment_id, r.broad_function;  
  
create or replace view public.v_availability_attendance_divergence  
with (security_invoker = true)  
as  
with latest_attendance as (  
select distinct on (training_session_id, athlete_id)  
training_session_id, athlete_id, status as attendance_status, recorded_at  
from public.attendance_records  
order by training_session_id, athlete_id, recorded_at desc, created_at desc  
)  
select  
rs.team_id,  
rs.request_id,  
rs.commitment_id,  
ts.id as training_session_id,  
rs.athlete_id,  
rs.effective_option_code as availability_code,  
la.attendance_status,  
la.recorded_at,  
case  
when la.attendance_status is null then 'ATTENDANCE_NOT_RECORDED'  
when rs.effective_semantic_group = 'AFFIRMATIVE'  
and la.attendance_status = 'AUSENTE' then 'CONFIRMED_BUT_ABSENT'  
when rs.effective_semantic_group = 'NEGATIVE'  
and la.attendance_status in ('PRESENTE','ATRASADA','SAIDA_ANTECIPADA') then 'UNAVAILABLE_BUT_ATTENDED'  
else 'NO_DIVERGENCE'  
end as divergence_code  
from public.v_request_recipient_state rs  
join public.training_sessions ts on ts.commitment_id = rs.commitment_id  
left join latest_attendance la  
on la.training_session_id = ts.id and la.athlete_id = rs.athlete_id;  
  
create or replace view public.v_athlete_inbox  
with (security_invoker = true)  
as  
select  
'REQUEST'::text as item_type,  
rr.athlete_id,  
r.team_id,  
r.id as item_id,  
r.title,  
r.opens_at as available_at,  
r.deadline_at as due_at,  
case when s.pending then 'PENDING' else 'ANSWERED' end as item_status  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.v_request_recipient_state s on s.request_recipient_id = rr.id  
where rr.cancelled_at is null  
union all  
select  
'COMMUNICATION'::text,  
cr.athlete_id,  
c.team_id,  
c.id,  
c.title,  
c.valid_from,  
c.valid_until,  
case  
when cr.acknowledged_at is not null then 'ACKNOWLEDGED'  
when cr.viewed_at is not null then 'VIEWED'  
else 'UNREAD'  
end  
from public.communication_recipients cr  
join public.communications c on c.id = cr.communication_id  
where c.status = 'PUBLICADA';  
  
create or replace view public.v_coach_pending_actions  
with (security_invoker = true)  
as  
select  
r.team_id,  
'REQUEST_RESPONSES'::text as action_type,  
r.id as entity_id,  
r.title,  
r.deadline_at as due_at,  
count(*) filter (where s.pending)::integer as pending_count  
from public.operational_requests r  
join public.v_request_recipient_state s on s.request_id = r.id  
where r.status = 'ABERTA'  
group by r.team_id, r.id, r.title, r.deadline_at  
having count(*) filter (where s.pending) > 0  
union all  
select  
c.team_id,  
'COMMUNICATION_ACK'::text,  
c.id,  
c.title,  
c.valid_until,  
count(*) filter (where cr.acknowledged_at is null)::integer  
from public.communications c  
join public.communication_recipients cr on cr.communication_id = c.id  
where c.status = 'PUBLICADA'  
group by c.team_id, c.id, c.title, c.valid_until  
having count(*) filter (where cr.acknowledged_at is null) > 0;  
  
create or replace view public.v_operational_state  
with (security_invoker = true)  
as  
select  
t.id as team_id,  
t.name as team_name,  
(select count(*) from public.v_current_roster r  
where r.team_id = t.id and r.status = 'ATIVA')::integer as active_roster_count,  
(select count(*) from public.commitments c  
where c.team_id = t.id and c.starts_at >= now()  
and c.status in ('PLANEJADO','PUBLICADO'))::integer as upcoming_commitments,  
(select count(*) from public.v_request_recipient_state s  
where s.team_id = t.id and s.pending)::integer as pending_responses,  
(select count(*) from public.communication_recipients cr  
join public.communications c on c.id = cr.communication_id  
where c.team_id = t.id and c.status = 'PUBLICADA'  
and cr.acknowledged_at is null)::integer as pending_acknowledgements  
from public.teams t;  
  
grant select on public.v_current_roster,  
public.v_request_recipient_state,  
public.v_calendar,  
public.v_current_published_lists,  
public.v_training_expected_composition,  
public.v_function_coverage,  
public.v_availability_attendance_divergence,  
public.v_athlete_inbox,  
public.v_coach_pending_actions,  
public.v_operational_state  
to authenticated;  

# 11. Segurança, RLS e privacidade

-   Anon não recebe acesso às tabelas.
-   O treinador opera apenas equipes em que possui vínculo COACH ativo e MFA AAL2.
-   A atleta lê e altera apenas seus próprios fluxos; listas publicadas expõem somente snapshots mínimos.
-   Justificativas ficam em private.response_justifications e não recebem grants diretos.
-   Service role nunca deve ser incluída no frontend.
-   Políticas e colunas usadas em RLS possuem índices para evitar degradação de desempenho.

Referências de implementação: [Supabase — Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security) • [Supabase — Multi-Factor Authentication](https://supabase.com/docs/guides/auth/auth-mfa)

-- 0005_rls.sql  
revoke all on schema private from anon, authenticated;  
revoke all on schema audit from anon, authenticated;  
grant usage on schema public to anon, authenticated;  
  
create or replace function private.is_team_member(p_team_id uuid)  
returns boolean  
language sql  
stable  
security definer  
set search_path = ''  
as $$  
select exists (  
select 1  
from public.team_access_memberships m  
join public.profiles p on p.id = m.profile_id  
where m.team_id = p_team_id  
and m.profile_id = auth.uid()  
and m.status = 'ACTIVE'  
and p.active  
and m.valid_from <= now()  
and (m.valid_until is null or m.valid_until > now())  
);  
$$;  
  
create or replace function private.is_team_coach(p_team_id uuid)  
returns boolean  
language sql  
stable  
security definer  
set search_path = ''  
as $$  
select exists (  
select 1  
from public.team_access_memberships m  
join public.profiles p on p.id = m.profile_id  
where m.team_id = p_team_id  
and m.profile_id = auth.uid()  
and m.role = 'COACH'  
and m.status = 'ACTIVE'  
and p.active  
and m.valid_from <= now()  
and (m.valid_until is null or m.valid_until > now())  
and coalesce(auth.jwt() ->> 'aal', 'aal1') = 'aal2'  
);  
$$;  
  
create or replace function private.is_own_athlete(p_athlete_id uuid)  
returns boolean  
language sql  
stable  
security definer  
set search_path = ''  
as $$  
select exists (  
select 1 from public.athletes a  
where a.id = p_athlete_id and a.profile_id = auth.uid()  
);  
$$;  
  
revoke all on function private.is_team_member(uuid) from public;  
revoke all on function private.is_team_coach(uuid) from public;  
revoke all on function private.is_own_athlete(uuid) from public;  
grant execute on function private.is_team_member(uuid) to authenticated;  
grant execute on function private.is_team_coach(uuid) to authenticated;  
grant execute on function private.is_own_athlete(uuid) to authenticated;  
  
alter table public.teams enable row level security;  
alter table public.seasons enable row level security;  
alter table public.profiles enable row level security;  
alter table public.team_access_memberships enable row level security;  
alter table public.athletes enable row level security;  
alter table public.athlete_roster_memberships enable row level security;  
alter table public.athlete_roster_events enable row level security;  
alter table public.commitments enable row level security;  
alter table public.training_sessions enable row level security;  
alter table public.request_definitions enable row level security;  
alter table public.request_definition_options enable row level security;  
alter table public.operational_requests enable row level security;  
alter table public.request_recipients enable row level security;  
alter table public.operational_responses enable row level security;  
alter table public.justification_categories enable row level security;  
alter table private.response_justifications enable row level security;  
alter table public.response_corrections enable row level security;  
alter table public.operational_lists enable row level security;  
alter table public.operational_list_members enable row level security;  
alter table public.attendance_records enable row level security;  
alter table public.communications enable row level security;  
alter table public.communication_recipients enable row level security;  
alter table audit.audit_events enable row level security;  
  
-- Equipe e temporada  
create policy teams_select_member on public.teams  
for select to authenticated using (private.is_team_member(id));  
create policy seasons_select_member on public.seasons  
for select to authenticated using (private.is_team_member(team_id));  
create policy seasons_write_coach on public.seasons  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
  
-- Perfil e acesso  
create policy profiles_select_self_or_coach on public.profiles  
for select to authenticated using (  
id = auth.uid() or exists (  
select 1 from public.team_access_memberships self_m  
join public.team_access_memberships target_m on target_m.team_id = self_m.team_id  
where self_m.profile_id = auth.uid()  
and self_m.role = 'COACH' and self_m.status = 'ACTIVE'  
and target_m.profile_id = profiles.id  
and private.is_team_coach(self_m.team_id)  
)  
);  
create policy team_access_select_self_or_coach on public.team_access_memberships  
for select to authenticated using (  
profile_id = auth.uid() or private.is_team_coach(team_id)  
);  
create policy team_access_write_coach on public.team_access_memberships  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
  
-- Atletas e elenco  
create policy athletes_select_own_or_coach on public.athletes  
for select to authenticated using (  
profile_id = auth.uid() or private.is_team_coach(team_id)  
);  
create policy athletes_write_coach on public.athletes  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy roster_select_own_or_coach on public.athlete_roster_memberships  
for select to authenticated using (  
private.is_own_athlete(athlete_id) or exists (  
select 1 from public.athletes a  
where a.id = athlete_id and private.is_team_coach(a.team_id)  
)  
);  
create policy roster_write_coach on public.athlete_roster_memberships  
for all to authenticated using (  
exists (select 1 from public.athletes a where a.id = athlete_id and private.is_team_coach(a.team_id))  
) with check (  
exists (select 1 from public.athletes a where a.id = athlete_id and private.is_team_coach(a.team_id))  
);  
create policy roster_events_select_own_or_coach on public.athlete_roster_events  
for select to authenticated using (  
exists (  
select 1 from public.athlete_roster_memberships m  
join public.athletes a on a.id = m.athlete_id  
where m.id = membership_id  
and (a.profile_id = auth.uid() or private.is_team_coach(a.team_id))  
)  
);  
  
-- Compromissos e treinos  
create policy commitments_select_authorized on public.commitments  
for select to authenticated using (  
private.is_team_coach(team_id)  
or (private.is_team_member(team_id) and status <> 'RASCUNHO')  
);  
create policy commitments_write_coach on public.commitments  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy training_select_authorized on public.training_sessions  
for select to authenticated using (  
exists (  
select 1 from public.commitments c  
where c.id = commitment_id  
and (private.is_team_coach(c.team_id)  
or (private.is_team_member(c.team_id) and c.status <> 'RASCUNHO'))  
)  
);  
create policy training_write_coach on public.training_sessions  
for all to authenticated using (  
exists (select 1 from public.commitments c where c.id = commitment_id and private.is_team_coach(c.team_id))  
) with check (  
exists (select 1 from public.commitments c where c.id = commitment_id and private.is_team_coach(c.team_id))  
);  
  
-- Definições e opções  
create policy request_def_select_member on public.request_definitions  
for select to authenticated using (private.is_team_member(team_id));  
create policy request_def_write_coach on public.request_definitions  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy request_options_select_member on public.request_definition_options  
for select to authenticated using (  
exists (select 1 from public.request_definitions d  
where d.id = request_definition_id and private.is_team_member(d.team_id))  
);  
create policy request_options_write_coach on public.request_definition_options  
for all to authenticated using (  
exists (select 1 from public.request_definitions d  
where d.id = request_definition_id and private.is_team_coach(d.team_id))  
) with check (  
exists (select 1 from public.request_definitions d  
where d.id = request_definition_id and private.is_team_coach(d.team_id))  
);  
  
-- Solicitações e respostas  
create policy requests_select_coach_or_recipient on public.operational_requests  
for select to authenticated using (  
private.is_team_coach(team_id)  
or exists (  
select 1 from public.request_recipients rr  
join public.athletes a on a.id = rr.athlete_id  
where rr.request_id = operational_requests.id  
and rr.cancelled_at is null and a.profile_id = auth.uid()  
)  
);  
create policy requests_write_coach on public.operational_requests  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy recipients_select_coach_or_self on public.request_recipients  
for select to authenticated using (  
exists (  
select 1 from public.operational_requests r  
join public.athletes a on a.id = athlete_id  
where r.id = request_id  
and (private.is_team_coach(r.team_id) or a.profile_id = auth.uid())  
)  
);  
create policy recipients_write_coach on public.request_recipients  
for all to authenticated using (  
exists (select 1 from public.operational_requests r where r.id = request_id and private.is_team_coach(r.team_id))  
) with check (  
exists (select 1 from public.operational_requests r where r.id = request_id and private.is_team_coach(r.team_id))  
);  
create policy responses_select_coach_or_self on public.operational_responses  
for select to authenticated using (  
exists (  
select 1 from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.athletes a on a.id = rr.athlete_id  
where rr.id = request_recipient_id  
and (private.is_team_coach(r.team_id) or a.profile_id = auth.uid())  
)  
);  
create policy categories_select_member on public.justification_categories  
for select to authenticated using (private.is_team_member(team_id));  
create policy categories_write_coach on public.justification_categories  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy corrections_select_coach_or_self on public.response_corrections  
for select to authenticated using (  
exists (  
select 1 from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.athletes a on a.id = rr.athlete_id  
where rr.id = request_recipient_id  
and (private.is_team_coach(r.team_id) or a.profile_id = auth.uid())  
)  
);  
  
-- Listas  
create policy lists_select_authorized on public.operational_lists  
for select to authenticated using (  
private.is_team_coach(team_id)  
or (status = 'PUBLICADA' and private.is_team_member(team_id))  
);  
create policy lists_write_coach on public.operational_lists  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy list_members_select_authorized on public.operational_list_members  
for select to authenticated using (  
exists (  
select 1 from public.operational_lists l  
where l.id = list_id  
and (private.is_team_coach(l.team_id)  
or (l.status = 'PUBLICADA' and private.is_team_member(l.team_id)))  
)  
);  
create policy list_members_write_coach on public.operational_list_members  
for all to authenticated using (  
exists (select 1 from public.operational_lists l where l.id = list_id and private.is_team_coach(l.team_id))  
) with check (  
exists (select 1 from public.operational_lists l where l.id = list_id and private.is_team_coach(l.team_id))  
);  
  
-- Presença  
create policy attendance_select_own_or_coach on public.attendance_records  
for select to authenticated using (  
private.is_own_athlete(athlete_id)  
or exists (  
select 1 from public.training_sessions ts  
join public.commitments c on c.id = ts.commitment_id  
where ts.id = training_session_id and private.is_team_coach(c.team_id)  
)  
);  
  
-- Comunicação  
create policy communications_select_coach_or_recipient on public.communications  
for select to authenticated using (  
private.is_team_coach(team_id)  
or exists (  
select 1 from public.communication_recipients cr  
where cr.communication_id = communications.id and cr.profile_id = auth.uid()  
)  
);  
create policy communications_write_coach on public.communications  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy communication_recipients_select_self_or_coach on public.communication_recipients  
for select to authenticated using (  
profile_id = auth.uid()  
or exists (  
select 1 from public.communications c  
where c.id = communication_id and private.is_team_coach(c.team_id)  
)  
);  
  
-- Auditoria: apenas treinador AAL2 lê; nenhum cliente escreve.  
create policy audit_select_coach on audit.audit_events  
for select to authenticated using (team_id is not null and private.is_team_coach(team_id));  
  
-- Grants mínimos. Escritas sensíveis ocorrem exclusivamente por RPC.  
grant select on all tables in schema public to authenticated;  
grant insert, update, delete on public.seasons,  
public.team_access_memberships,  
public.athletes,  
public.athlete_roster_memberships,  
public.commitments,  
public.training_sessions,  
public.request_definitions,  
public.request_definition_options,  
public.operational_requests,  
public.request_recipients,  
public.justification_categories,  
public.operational_lists,  
public.operational_list_members,  
public.communications  
to authenticated;  
  
grant select on audit.audit_events to authenticated;  
revoke all on private.response_justifications from anon, authenticated;  
revoke insert, update, delete on public.operational_responses,  
public.athlete_roster_events,  
public.response_corrections,  
public.attendance_records,  
public.communication_recipients  
from authenticated;  
  
  
revoke select on public.response_corrections from authenticated;  
grant select (  
id, request_recipient_id, response_id, action,  
replacement_option_id, corrected_at, supersedes_correction_id  
) on public.response_corrections to authenticated;  

# 12. RPCs transacionais

| **RPC** | **Quem executa** | **Garantia** |
| --- | --- | --- |
| submit_operational_response | Atleta | Autoria própria, janela válida, opção correta, idempotência e justificativa privada. |
| --- | --- | --- |
| correct_operational_response | Treinador AAL2 | Correção separada da declaração original. |
| --- | --- | --- |
| record_training_attendance | Treinador AAL2 | Fato append-only e correção por supersedes. |
| --- | --- | --- |
| change_roster_membership | Treinador AAL2 | Atualização material + evento de domínio. |
| --- | --- | --- |
| mark_communication_viewed | Destinatário | Marca apenas a própria primeira visualização. |
| --- | --- | --- |
| acknowledge_communication | Destinatário | Marca ciência explícita própria. |
| --- | --- | --- |
| close_operational_request | Treinador AAL2 | Encerramento auditável da solicitação. |
| --- | --- | --- |

-- 0006_rpcs.sql  
create or replace function public.submit_operational_response(  
p_request_recipient_id uuid,  
p_option_code text,  
p_category_code text default null,  
p_justification text default null,  
p_client_submission_id uuid default gen_random_uuid()  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_request public.operational_requests%rowtype;  
v_athlete public.athletes%rowtype;  
v_option_id uuid;  
v_previous_id uuid;  
v_response_id uuid;  
v_category_id uuid;  
v_allow_justification boolean;  
begin  
select r, a into v_request, v_athlete  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.athletes a on a.id = rr.athlete_id  
where rr.id = p_request_recipient_id  
and rr.cancelled_at is null;  
  
if not found or v_athlete.profile_id is distinct from auth.uid() then  
raise exception 'Destinatário não autorizado';  
end if;  
if v_request.status <> 'ABERTA'  
or now() < v_request.opens_at  
or now() > v_request.deadline_at then  
raise exception 'Solicitação fora da janela de resposta';  
end if;  
  
select o.id, d.allow_justification  
into v_option_id, v_allow_justification  
from public.request_definition_options o  
join public.request_definitions d on d.id = o.request_definition_id  
where o.request_definition_id = v_request.definition_id  
and o.code = upper(p_option_code)  
and o.active;  
if v_option_id is null then  
raise exception 'Opção inválida';  
end if;  
  
select id into v_previous_id  
from public.operational_responses  
where request_recipient_id = p_request_recipient_id  
order by responded_at desc, created_at desc  
limit 1;  
  
insert into public.operational_responses (  
request_recipient_id, option_id, responded_by_profile_id,  
client_submission_id, supersedes_response_id  
) values (  
p_request_recipient_id, v_option_id, auth.uid(),  
p_client_submission_id, v_previous_id  
)  
on conflict (client_submission_id) do update  
set client_submission_id = excluded.client_submission_id  
returning id into v_response_id;  
  
if p_category_code is not null or nullif(btrim(p_justification), '') is not null then  
if not v_allow_justification then  
raise exception 'Esta solicitação não admite justificativa';  
end if;  
if p_category_code is not null then  
select id into v_category_id  
from public.justification_categories  
where team_id = v_request.team_id  
and code = upper(p_category_code)  
and active;  
if v_category_id is null then  
raise exception 'Categoria de justificativa inválida';  
end if;  
end if;  
insert into private.response_justifications (  
response_id, category_id, free_text, submitted_by_profile_id  
) values (  
v_response_id, v_category_id,  
nullif(btrim(p_justification), ''), auth.uid()  
) on conflict (response_id) do nothing;  
end if;  
  
insert into audit.audit_events (  
team_id, actor_profile_id, actor_auth_uid, event_type,  
entity_schema, entity_table, entity_id, after_data  
) values (  
v_request.team_id, auth.uid(), auth.uid(), 'RESPONSE_SUBMITTED',  
'public', 'operational_responses', v_response_id::text,  
jsonb_build_object('request_recipient_id', p_request_recipient_id,  
'option_id', v_option_id)  
);  
return v_response_id;  
end;  
$$;  
  
create or replace function public.correct_operational_response(  
p_request_recipient_id uuid,  
p_action public.correction_action,  
p_replacement_option_code text,  
p_reason text  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_team_id uuid;  
v_definition_id uuid;  
v_response_id uuid;  
v_option_id uuid;  
v_previous_correction uuid;  
v_id uuid;  
begin  
select r.team_id, r.definition_id into v_team_id, v_definition_id  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
where rr.id = p_request_recipient_id;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
if nullif(btrim(p_reason), '') is null then  
raise exception 'Motivo obrigatório';  
end if;  
  
select id into v_response_id  
from public.operational_responses  
where request_recipient_id = p_request_recipient_id  
order by responded_at desc, created_at desc limit 1;  
  
if p_action = 'REPLACE' then  
select id into v_option_id  
from public.request_definition_options  
where request_definition_id = v_definition_id  
and code = upper(p_replacement_option_code) and active;  
if v_option_id is null then raise exception 'Opção substituta inválida'; end if;  
elsif p_replacement_option_code is not null then  
raise exception 'VOID não aceita opção substituta';  
end if;  
  
select id into v_previous_correction  
from public.response_corrections  
where request_recipient_id = p_request_recipient_id  
order by corrected_at desc limit 1;  
  
insert into public.response_corrections (  
request_recipient_id, response_id, action, replacement_option_id,  
reason, corrected_by_profile_id, supersedes_correction_id  
) values (  
p_request_recipient_id, v_response_id, p_action, v_option_id,  
btrim(p_reason), auth.uid(), v_previous_correction  
) returning id into v_id;  
  
insert into audit.audit_events (  
team_id, actor_profile_id, actor_auth_uid, event_type,  
entity_schema, entity_table, entity_id, after_data  
) values (  
v_team_id, auth.uid(), auth.uid(), 'RESPONSE_CORRECTED',  
'public', 'response_corrections', v_id::text,  
jsonb_build_object('request_recipient_id', p_request_recipient_id,  
'action', p_action, 'replacement_option_id', v_option_id)  
);  
return v_id;  
end;  
$$;  
  
create or replace function public.record_training_attendance(  
p_training_session_id uuid,  
p_athlete_id uuid,  
p_status public.attendance_status,  
p_arrived_at timestamptz default null,  
p_departed_at timestamptz default null,  
p_source_note text default null,  
p_client_record_id uuid default gen_random_uuid()  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_team_id uuid;  
v_previous_id uuid;  
v_id uuid;  
begin  
select c.team_id into v_team_id  
from public.training_sessions ts  
join public.commitments c on c.id = ts.commitment_id  
where ts.id = p_training_session_id;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
if not exists (select 1 from public.athletes a where a.id = p_athlete_id and a.team_id = v_team_id) then  
raise exception 'Atleta fora da equipe';  
end if;  
  
select id into v_previous_id  
from public.attendance_records  
where training_session_id = p_training_session_id  
and athlete_id = p_athlete_id  
order by recorded_at desc, created_at desc limit 1;  
  
insert into public.attendance_records (  
training_session_id, athlete_id, status, arrived_at, departed_at,  
recorded_by_profile_id, client_record_id, supersedes_record_id, source_note  
) values (  
p_training_session_id, p_athlete_id, p_status, p_arrived_at, p_departed_at,  
auth.uid(), p_client_record_id, v_previous_id, nullif(btrim(p_source_note),'')  
)  
on conflict (client_record_id) do update  
set client_record_id = excluded.client_record_id  
returning id into v_id;  
  
insert into audit.audit_events (  
team_id, actor_profile_id, actor_auth_uid, event_type,  
entity_schema, entity_table, entity_id, after_data  
) values (  
v_team_id, auth.uid(), auth.uid(), 'ATTENDANCE_RECORDED',  
'public', 'attendance_records', v_id::text,  
jsonb_build_object('training_session_id', p_training_session_id,  
'athlete_id', p_athlete_id, 'status', p_status)  
);  
return v_id;  
end;  
$$;  
  
create or replace function public.change_roster_membership(  
p_membership_id uuid,  
p_status public.athlete_relationship_status,  
p_broad_function public.broad_player_function,  
p_shirt_number smallint,  
p_effective_on date,  
p_reason text default null  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_old public.athlete_roster_memberships%rowtype;  
v_team_id uuid;  
v_event_id uuid;  
begin  
select m.*, a.team_id into v_old, v_team_id  
from public.athlete_roster_memberships m  
join public.athletes a on a.id = m.athlete_id  
where m.id = p_membership_id for update;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
if p_shirt_number is not null and (p_shirt_number < 1 or p_shirt_number > 99) then  
raise exception 'Número de camisa deve estar entre 1 e 99';  
end if;  
  
update public.athlete_roster_memberships  
set status = p_status,  
broad_function = p_broad_function,  
shirt_number = p_shirt_number,  
ends_on = case when p_status = 'VINCULO_ENCERRADO' then p_effective_on else ends_on end  
where id = p_membership_id;  
  
insert into public.athlete_roster_events (  
membership_id, event_type, effective_on, from_state, to_state,  
reason, actor_profile_id  
) values (  
p_membership_id, 'MEMBERSHIP_CHANGED', p_effective_on,  
jsonb_build_object('status', v_old.status, 'broad_function', v_old.broad_function,  
'shirt_number', v_old.shirt_number, 'ends_on', v_old.ends_on),  
jsonb_build_object('status', p_status, 'broad_function', p_broad_function,  
'shirt_number', p_shirt_number),  
nullif(btrim(p_reason),''), auth.uid()  
) returning id into v_event_id;  
return v_event_id;  
end;  
$$;  
  
create or replace function public.mark_communication_viewed(p_recipient_id uuid)  
returns timestamptz  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare v_time timestamptz;  
begin  
update public.communication_recipients  
set viewed_at = coalesce(viewed_at, now())  
where id = p_recipient_id and profile_id = auth.uid()  
returning viewed_at into v_time;  
if v_time is null then raise exception 'Destinatário não autorizado'; end if;  
return v_time;  
end;  
$$;  
  
create or replace function public.acknowledge_communication(p_recipient_id uuid)  
returns timestamptz  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare v_time timestamptz;  
begin  
update public.communication_recipients  
set viewed_at = coalesce(viewed_at, now()),  
acknowledged_at = coalesce(acknowledged_at, now())  
where id = p_recipient_id and profile_id = auth.uid()  
returning acknowledged_at into v_time;  
if v_time is null then raise exception 'Destinatário não autorizado'; end if;  
return v_time;  
end;  
$$;  
  
create or replace function public.close_operational_request(p_request_id uuid)  
returns void  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare v_team_id uuid;  
begin  
select team_id into v_team_id from public.operational_requests where id = p_request_id;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
update public.operational_requests  
set status = 'ENCERRADA', closed_at = now()  
where id = p_request_id and status = 'ABERTA';  
end;  
$$;  
  
revoke all on function public.submit_operational_response(uuid,text,text,text,uuid) from public;  
revoke all on function public.correct_operational_response(uuid,public.correction_action,text,text) from public;  
revoke all on function public.record_training_attendance(uuid,uuid,public.attendance_status,timestamptz,timestamptz,text,uuid) from public;  
revoke all on function public.change_roster_membership(uuid,public.athlete_relationship_status,public.broad_player_function,smallint,date,text) from public;  
revoke all on function public.mark_communication_viewed(uuid) from public;  
revoke all on function public.acknowledge_communication(uuid) from public;  
revoke all on function public.close_operational_request(uuid) from public;  
  
grant execute on function public.submit_operational_response(uuid,text,text,text,uuid) to authenticated;  
grant execute on function public.correct_operational_response(uuid,public.correction_action,text,text) to authenticated;  
grant execute on function public.record_training_attendance(uuid,uuid,public.attendance_status,timestamptz,timestamptz,text,uuid) to authenticated;  
grant execute on function public.change_roster_membership(uuid,public.athlete_relationship_status,public.broad_player_function,smallint,date,text) to authenticated;  
grant execute on function public.mark_communication_viewed(uuid) to authenticated;  
grant execute on function public.acknowledge_communication(uuid) to authenticated;  
grant execute on function public.close_operational_request(uuid) to authenticated;  

# 13. Migrations do banco

| **Ordem** | **Arquivo** | **Conteúdo** | **Bloco neste documento** |
| --- | --- | --- | --- |
| 1 | 0001_foundation.sql | Schemas, extensões, enums e funções-base. | FOUNDATION_SQL |
| --- | --- | --- | --- |
| 2 | 0002_tables.sql | Criação das 23 tabelas na ordem apresentada; cada bloco deste documento é executável. | Tabela SQL |
| --- | --- | --- | --- |
| 3 | 0003_indexes_integrity.sql | Índices de todas as tabelas, validações cruzadas, updated_at e proteção append-only. | Índices + RELATIONSHIP_SQL |
| --- | --- | --- | --- |
| 4 | 0004_views.sql | Projeções operacionais e indicadores derivados. | VIEWS_SQL |
| --- | --- | --- | --- |
| 5 | 0005_rls.sql | Funções de autorização, RLS, políticas e grants. | RLS_SQL |
| --- | --- | --- | --- |
| 6 | 0006_rpcs.sql | Comandos transacionais para resposta, correção, presença, elenco e comunicação. | RPC_SQL |
| --- | --- | --- | --- |
| 7 | 0007_audit.sql | Captura de alterações mutáveis e log técnico. | AUDIT_SQL |
| --- | --- | --- | --- |
| 8 | 0008_seed_synthetic.sql | Dados exclusivamente fictícios do ambiente sintético. | SEED_SQL |
| --- | --- | --- | --- |

## 13.1 0001_foundation.sql

-- 0001_foundation.sql  
create schema if not exists private;  
create schema if not exists audit;  
create schema if not exists extensions;  
  
create extension if not exists pgcrypto with schema extensions;  
  
create type public.app_role as enum ('COACH', 'ATHLETE');  
create type public.access_membership_status as enum ('ACTIVE', 'SUSPENDED', 'ENDED');  
create type public.season_status as enum ('PLANEJADA', 'ATIVA', 'ENCERRADA');  
create type public.athlete_relationship_status as enum  
('ATIVA', 'INATIVA_TEMPORARIA', 'VINCULO_ENCERRADO');  
create type public.broad_player_function as enum  
('GOLEIRA', 'DEFESA', 'ATAQUE', 'INDEFINIDA');  
create type public.commitment_type as enum  
('TREINO', 'COMPETICAO', 'REUNIAO', 'FEEDBACK', 'OUTRO');  
create type public.commitment_status as enum  
('RASCUNHO', 'PLANEJADO', 'PUBLICADO', 'REALIZADO', 'CANCELADO');  
create type public.response_semantic_group as enum  
('AFFIRMATIVE', 'NEGATIVE', 'UNCERTAIN');  
create type public.request_status as enum  
('RASCUNHO', 'ABERTA', 'ENCERRADA', 'CANCELADA');  
create type public.correction_action as enum ('REPLACE', 'VOID');  
create type public.operational_list_type as enum ('TRAINING_EXPECTED');  
create type public.list_publication_status as enum  
('RASCUNHO', 'PUBLICADA', 'SUBSTITUIDA', 'ENCERRADA', 'NAO_PUBLICADA');  
create type public.attendance_status as enum  
('PRESENTE', 'AUSENTE', 'ATRASADA', 'SAIDA_ANTECIPADA', 'DISPENSADA');  
create type public.communication_audience_type as enum  
('ALL_ACTIVE_ATHLETES', 'SELECTED', 'COACH_ONLY');  
create type public.communication_status as enum  
('RASCUNHO', 'PUBLICADA', 'ARQUIVADA');  
create type public.delivery_status as enum ('PENDING', 'DELIVERED', 'FAILED');  
  
comment on type public.broad_player_function is  
'Funções amplas cadastrais. ESPECIALISTA/CORINGA é papel tático contextual e não pertence a este enum.';  
  
create or replace function private.set_updated_at()  
returns trigger  
language plpgsql  
security invoker  
set search_path = ''  
as $$  
begin  
new.updated_at := now();  
return new;  
end;  
$$;  
  
create or replace function private.prevent_update_delete()  
returns trigger  
language plpgsql  
security invoker  
set search_path = ''  
as $$  
begin  
raise exception 'Tabela append-only: operação % não permitida em %.%',  
tg_op, tg_table_schema, tg_table_name;  
end;  
$$;  

## 13.2 0002_tables.sql

create table public.teams (  
id uuid primary key default gen_random_uuid(),  
code text not null,  
name text not null,  
timezone text default 'America/Sao_Paulo' not null,  
locale text default 'pt-BR' not null,  
synthetic_only boolean default true not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint teams_code_ck check (code ~ '^[A-Z0-9][A-Z0-9_-]{1,31}$')  
);  
  
create table public.seasons (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
label text not null,  
starts_on date not null,  
ends_on date not null,  
status public.season_status default 'PLANEJADA' not null,  
ruleset_code text default 'IHF_BEACH_2026-04-01' not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint seasons_dates_ck check (ends_on >= starts_on),  
constraint seasons_team_label_uq unique (team_id, label)  
);  
  
create table public.profiles (  
id uuid primary key references auth.users(id) on delete cascade,  
display_name text not null,  
preferred_name text default null,  
active boolean default true not null,  
mfa_required boolean default false not null,  
last_seen_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null  
);  
  
create table public.team_access_memberships (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
profile_id uuid references public.profiles(id) on delete restrict not null,  
role public.app_role not null,  
status public.access_membership_status default 'ACTIVE' not null,  
valid_from timestamptz default now() not null,  
valid_until timestamptz default null,  
created_by uuid references public.profiles(id) on delete set null,  
created_at timestamptz default now() not null,  
constraint team_access_period_ck check (valid_until is null or valid_until > valid_from)  
);  
  
create table public.athletes (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
profile_id uuid references public.profiles(id) on delete set null,  
legacy_athlete_id text default null,  
display_name text not null,  
created_by uuid references public.profiles(id) on delete set null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint athletes_team_legacy_uq unique (team_id, legacy_athlete_id),  
constraint athletes_team_profile_uq unique (team_id, profile_id)  
);  
  
create table public.athlete_roster_memberships (  
id uuid primary key default gen_random_uuid(),  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
season_id uuid references public.seasons(id) on delete restrict not null,  
status public.athlete_relationship_status default 'ATIVA' not null,  
broad_function public.broad_player_function default 'INDEFINIDA' not null,  
shirt_number smallint default null,  
starts_on date not null,  
ends_on date default null,  
source_note text default null,  
created_by uuid references public.profiles(id) on delete set null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint roster_period_ck check (ends_on is null or ends_on >= starts_on),  
constraint roster_shirt_number_ck check (shirt_number is null or shirt_number between 1 and 99)  
);  
  
create table public.athlete_roster_events (  
id uuid primary key default gen_random_uuid(),  
membership_id uuid references public.athlete_roster_memberships(id) on delete restrict not null,  
event_type text not null,  
effective_on date default current_date not null,  
from_state jsonb default null,  
to_state jsonb default '{}'::jsonb not null,  
reason text default null,  
actor_profile_id uuid references public.profiles(id) on delete set null,  
occurred_at timestamptz default now() not null  
);  
  
create table public.commitments (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
season_id uuid references public.seasons(id) on delete restrict not null,  
commitment_type public.commitment_type not null,  
title text not null,  
description text default null,  
starts_at timestamptz not null,  
ends_at timestamptz not null,  
timezone text default 'America/Sao_Paulo' not null,  
location_name text default null,  
status public.commitment_status default 'RASCUNHO' not null,  
published_at timestamptz default null,  
cancelled_at timestamptz default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint commitments_period_ck check (ends_at > starts_at),  
constraint commitments_publish_ck check (status not in ('PUBLICADO','REALIZADO') or published_at is not null),  
constraint commitments_cancel_ck check (status <> 'CANCELADO' or cancelled_at is not null)  
);  
  
create table public.training_sessions (  
id uuid primary key default gen_random_uuid(),  
commitment_id uuid references public.commitments(id) on delete restrict not null,  
objective text default null,  
main_activity text default null,  
collective_goals text default null,  
athlete_guidance text default null,  
attendance_opened_at timestamptz default null,  
attendance_closed_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint training_commitment_uq unique (commitment_id),  
constraint training_attendance_window_ck check (attendance_closed_at is null or attendance_opened_at is not null and attendance_closed_at >= attendance_opened_at)  
);  
  
create table public.request_definitions (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
code text not null,  
name text not null,  
subject_type text default 'COMMITMENT' not null,  
description text default null,  
allow_justification boolean default true not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint request_def_team_code_uq unique (team_id, code),  
constraint request_def_code_ck check (code ~ '^[A-Z][A-Z0-9_]{2,63}$')  
);  
  
create table public.request_definition_options (  
id uuid primary key default gen_random_uuid(),  
request_definition_id uuid references public.request_definitions(id) on delete restrict not null,  
code text not null,  
label text not null,  
semantic_group public.response_semantic_group not null,  
sort_order smallint default 0 not null,  
requires_justification boolean default false not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
constraint request_option_code_uq unique (request_definition_id, code),  
constraint request_option_code_ck check (code ~ '^[A-Z][A-Z0-9_]{1,31}$')  
);  
  
create table public.operational_requests (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
definition_id uuid references public.request_definitions(id) on delete restrict not null,  
commitment_id uuid references public.commitments(id) on delete restrict default null,  
title text not null,  
instructions text default null,  
status public.request_status default 'RASCUNHO' not null,  
opens_at timestamptz default now() not null,  
deadline_at timestamptz not null,  
closed_at timestamptz default null,  
version integer default 1 not null,  
supersedes_request_id uuid references public.operational_requests(id) on delete restrict default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
published_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint operational_request_window_ck check (deadline_at > opens_at),  
constraint operational_request_version_ck check (version > 0),  
constraint operational_request_publish_ck check (status = 'RASCUNHO' or published_at is not null)  
);  
  
create table public.request_recipients (  
id uuid primary key default gen_random_uuid(),  
request_id uuid references public.operational_requests(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
sent_at timestamptz default now() not null,  
cancelled_at timestamptz default null,  
delivery_channel text default 'APP' not null,  
created_at timestamptz default now() not null,  
constraint request_recipient_uq unique (request_id, athlete_id)  
);  
  
create table public.operational_responses (  
id uuid primary key default gen_random_uuid(),  
request_recipient_id uuid references public.request_recipients(id) on delete restrict not null,  
option_id uuid references public.request_definition_options(id) on delete restrict not null,  
responded_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
responded_at timestamptz default now() not null,  
client_submission_id uuid default gen_random_uuid() not null,  
supersedes_response_id uuid references public.operational_responses(id) on delete restrict default null,  
created_at timestamptz default now() not null,  
constraint operational_response_client_uq unique (client_submission_id)  
);  
  
create table public.justification_categories (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
code text not null,  
label text not null,  
description text default null,  
sensitive boolean default false not null,  
sort_order smallint default 0 not null,  
active boolean default true not null,  
created_at timestamptz default now() not null,  
constraint justification_category_uq unique (team_id, code)  
);  
  
create table private.response_justifications (  
id uuid primary key default gen_random_uuid(),  
response_id uuid references public.operational_responses(id) on delete restrict not null,  
category_id uuid references public.justification_categories(id) on delete restrict default null,  
free_text text default null,  
submitted_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint response_justification_response_uq unique (response_id),  
constraint response_justification_content_ck check (category_id is not null or nullif(btrim(free_text), '') is not null),  
constraint response_justification_length_ck check (free_text is null or char_length(free_text) <= 500)  
);  
  
create table public.response_corrections (  
id uuid primary key default gen_random_uuid(),  
request_recipient_id uuid references public.request_recipients(id) on delete restrict not null,  
response_id uuid references public.operational_responses(id) on delete restrict default null,  
action public.correction_action not null,  
replacement_option_id uuid references public.request_definition_options(id) on delete restrict default null,  
reason text not null,  
corrected_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
corrected_at timestamptz default now() not null,  
supersedes_correction_id uuid references public.response_corrections(id) on delete restrict default null,  
constraint response_correction_action_ck check ((action = 'REPLACE' and replacement_option_id is not null) or (action = 'VOID' and replacement_option_id is null))  
);  
  
create table public.operational_lists (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
commitment_id uuid references public.commitments(id) on delete restrict not null,  
list_type public.operational_list_type not null,  
version integer default 1 not null,  
status public.list_publication_status default 'RASCUNHO' not null,  
title text not null,  
published_at timestamptz default null,  
not_published_at timestamptz default null,  
supersedes_list_id uuid references public.operational_lists(id) on delete restrict default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
constraint operational_list_version_ck check (version > 0),  
constraint operational_list_version_uq unique (commitment_id, list_type, version),  
constraint operational_list_dates_ck check ((status = 'NAO_PUBLICADA' and not_published_at is not null) or status <> 'NAO_PUBLICADA')  
);  
  
create table public.operational_list_members (  
id uuid primary key default gen_random_uuid(),  
list_id uuid references public.operational_lists(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
roster_membership_id uuid references public.athlete_roster_memberships(id) on delete restrict default null,  
display_name_snapshot text not null,  
broad_function_snapshot public.broad_player_function not null,  
sort_order integer default 0 not null,  
public_note text default null,  
created_at timestamptz default now() not null,  
constraint operational_list_member_uq unique (list_id, athlete_id)  
);  
  
create table public.attendance_records (  
id uuid primary key default gen_random_uuid(),  
training_session_id uuid references public.training_sessions(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict not null,  
status public.attendance_status not null,  
arrived_at timestamptz default null,  
departed_at timestamptz default null,  
recorded_by_profile_id uuid references public.profiles(id) on delete restrict not null,  
recorded_at timestamptz default now() not null,  
client_record_id uuid default gen_random_uuid() not null,  
supersedes_record_id uuid references public.attendance_records(id) on delete restrict default null,  
source_note text default null,  
created_at timestamptz default now() not null,  
constraint attendance_client_record_uq unique (client_record_id),  
constraint attendance_time_ck check (departed_at is null or arrived_at is null or departed_at >= arrived_at)  
);  
  
create table public.communications (  
id uuid primary key default gen_random_uuid(),  
team_id uuid references public.teams(id) on delete restrict not null,  
commitment_id uuid references public.commitments(id) on delete restrict default null,  
title text not null,  
body text not null,  
audience_type public.communication_audience_type default 'SELECTED' not null,  
status public.communication_status default 'RASCUNHO' not null,  
valid_from timestamptz default now() not null,  
valid_until timestamptz default null,  
published_at timestamptz default null,  
created_by uuid references public.profiles(id) on delete restrict not null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint communication_validity_ck check (valid_until is null or valid_until > valid_from),  
constraint communication_publish_ck check (status = 'RASCUNHO' or published_at is not null)  
);  
  
create table public.communication_recipients (  
id uuid primary key default gen_random_uuid(),  
communication_id uuid references public.communications(id) on delete restrict not null,  
profile_id uuid references public.profiles(id) on delete restrict not null,  
athlete_id uuid references public.athletes(id) on delete restrict default null,  
delivery_status public.delivery_status default 'PENDING' not null,  
delivered_at timestamptz default null,  
viewed_at timestamptz default null,  
acknowledged_at timestamptz default null,  
created_at timestamptz default now() not null,  
updated_at timestamptz default now() not null,  
constraint communication_recipient_uq unique (communication_id, profile_id),  
constraint communication_ack_ck check (acknowledged_at is null or viewed_at is null or acknowledged_at >= viewed_at)  
);  
  
create table audit.audit_events (  
id bigint generated always as identity primary key,  
team_id uuid default null,  
actor_profile_id uuid default null,  
actor_auth_uid uuid default null,  
event_type text not null,  
entity_schema text default null,  
entity_table text default null,  
entity_id text default null,  
occurred_at timestamptz default now() not null,  
correlation_id uuid default gen_random_uuid() not null,  
before_data jsonb default null,  
after_data jsonb default null,  
metadata jsonb default '{}'::jsonb not null  
);

## 13.3 Índices de 0003_indexes_integrity.sql

create unique index teams_code_uq on public.teams (code);  
create index teams_active_idx on public.teams (active) where active;  
create unique index seasons_one_active_per_team_uq on public.seasons (team_id) where status = 'ATIVA';  
create index seasons_team_dates_idx on public.seasons (team_id, starts_on, ends_on);  
create index profiles_active_idx on public.profiles (active) where active;  
create index profiles_display_name_idx on public.profiles (lower(display_name));  
create index team_access_profile_idx on public.team_access_memberships (profile_id, status, valid_until);  
create index team_access_team_role_idx on public.team_access_memberships (team_id, role, status);  
create unique index team_access_open_uq on public.team_access_memberships (team_id, profile_id, role) where valid_until is null and status = 'ACTIVE';  
create index athletes_team_name_idx on public.athletes (team_id, lower(display_name));  
create index athletes_profile_idx on public.athletes (profile_id) where profile_id is not null;  
create index roster_season_status_idx on public.athlete_roster_memberships (season_id, status, broad_function);  
create index roster_athlete_period_idx on public.athlete_roster_memberships (athlete_id, starts_on, ends_on);  
create unique index roster_open_per_season_uq on public.athlete_roster_memberships (athlete_id, season_id) where ends_on is null;  
create index roster_events_membership_time_idx on public.athlete_roster_events (membership_id, occurred_at desc);  
create index roster_events_type_idx on public.athlete_roster_events (event_type, occurred_at desc);  
create index commitments_team_start_idx on public.commitments (team_id, starts_at);  
create index commitments_season_type_status_idx on public.commitments (season_id, commitment_type, status);  
create index commitments_upcoming_idx on public.commitments (team_id, starts_at) where status in ('PLANEJADO','PUBLICADO');  
create index training_commitment_idx on public.training_sessions (commitment_id);  
create index training_attendance_open_idx on public.training_sessions (attendance_opened_at) where attendance_opened_at is not null and attendance_closed_at is null;  
create index request_def_active_idx on public.request_definitions (team_id, active);  
create index request_options_definition_order_idx on public.request_definition_options (request_definition_id, active, sort_order);  
create index requests_team_status_deadline_idx on public.operational_requests (team_id, status, deadline_at);  
create index requests_commitment_idx on public.operational_requests (commitment_id, status);  
create unique index requests_subject_version_uq on public.operational_requests (definition_id, commitment_id, version) where commitment_id is not null;  
create index request_recipients_athlete_idx on public.request_recipients (athlete_id, cancelled_at, sent_at desc);  
create index request_recipients_request_idx on public.request_recipients (request_id, cancelled_at);  
create index responses_recipient_time_idx on public.operational_responses (request_recipient_id, responded_at desc, created_at desc);  
create index responses_supersedes_idx on public.operational_responses (supersedes_response_id) where supersedes_response_id is not null;  
create index justification_categories_active_idx on public.justification_categories (team_id, active, sort_order);  
create index response_justifications_category_idx on private.response_justifications (category_id) where category_id is not null;  
create index response_corrections_recipient_time_idx on public.response_corrections (request_recipient_id, corrected_at desc);  
create index response_corrections_response_idx on public.response_corrections (response_id) where response_id is not null;  
create index operational_lists_current_idx on public.operational_lists (commitment_id, list_type, version desc);  
create unique index operational_lists_one_published_uq on public.operational_lists (commitment_id, list_type) where status = 'PUBLICADA';  
create index operational_list_members_order_idx on public.operational_list_members (list_id, sort_order, display_name_snapshot);  
create index operational_list_members_athlete_idx on public.operational_list_members (athlete_id, list_id);  
create index attendance_training_athlete_time_idx on public.attendance_records (training_session_id, athlete_id, recorded_at desc);  
create index attendance_athlete_time_idx on public.attendance_records (athlete_id, recorded_at desc);  
create index attendance_supersedes_idx on public.attendance_records (supersedes_record_id) where supersedes_record_id is not null;  
create index communications_team_validity_idx on public.communications (team_id, status, valid_from, valid_until);  
create index communications_commitment_idx on public.communications (commitment_id) where commitment_id is not null;  
create index communication_recipients_profile_idx on public.communication_recipients (profile_id, viewed_at, acknowledged_at);  
create index communication_recipients_comm_status_idx on public.communication_recipients (communication_id, delivery_status);  
create index audit_events_team_time_idx on audit.audit_events (team_id, occurred_at desc);  
create index audit_events_entity_idx on audit.audit_events (entity_schema, entity_table, entity_id, occurred_at desc);  
create index audit_events_actor_time_idx on audit.audit_events (actor_profile_id, occurred_at desc);  
create index audit_events_correlation_idx on audit.audit_events (correlation_id);

## 13.4 Integridade e triggers

-- 0003_integrity_triggers.sql  
create or replace function private.validate_training_commitment()  
returns trigger  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_type public.commitment_type;  
begin  
select commitment_type into v_type  
from public.commitments  
where id = new.commitment_id;  
  
if v_type is distinct from 'TREINO'::public.commitment_type then  
raise exception 'training_sessions exige commitment_type=TREINO';  
end if;  
return new;  
end;  
$$;  
  
create trigger training_sessions_validate_commitment  
before insert or update of commitment_id on public.training_sessions  
for each row execute function private.validate_training_commitment();  
  
create or replace function private.validate_roster_scope()  
returns trigger  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_athlete_team uuid;  
v_season_team uuid;  
begin  
select team_id into v_athlete_team from public.athletes where id = new.athlete_id;  
select team_id into v_season_team from public.seasons where id = new.season_id;  
if v_athlete_team is distinct from v_season_team then  
raise exception 'Atleta e temporada pertencem a equipes diferentes';  
end if;  
return new;  
end;  
$$;  
  
create trigger roster_validate_scope  
before insert or update of athlete_id, season_id  
on public.athlete_roster_memberships  
for each row execute function private.validate_roster_scope();  
  
create or replace function private.validate_response_option()  
returns trigger  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_expected uuid;  
v_actual uuid;  
begin  
select r.definition_id into v_expected  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
where rr.id = new.request_recipient_id;  
  
select request_definition_id into v_actual  
from public.request_definition_options  
where id = new.option_id;  
  
if v_expected is distinct from v_actual then  
raise exception 'Opção não pertence à definição da solicitação';  
end if;  
return new;  
end;  
$$;  
  
create trigger responses_validate_option  
before insert on public.operational_responses  
for each row execute function private.validate_response_option();  
  
-- updated_at  
create trigger teams_set_updated_at before update on public.teams  
for each row execute function private.set_updated_at();  
create trigger seasons_set_updated_at before update on public.seasons  
for each row execute function private.set_updated_at();  
create trigger profiles_set_updated_at before update on public.profiles  
for each row execute function private.set_updated_at();  
create trigger athletes_set_updated_at before update on public.athletes  
for each row execute function private.set_updated_at();  
create trigger roster_set_updated_at before update on public.athlete_roster_memberships  
for each row execute function private.set_updated_at();  
create trigger commitments_set_updated_at before update on public.commitments  
for each row execute function private.set_updated_at();  
create trigger training_set_updated_at before update on public.training_sessions  
for each row execute function private.set_updated_at();  
create trigger request_def_set_updated_at before update on public.request_definitions  
for each row execute function private.set_updated_at();  
create trigger requests_set_updated_at before update on public.operational_requests  
for each row execute function private.set_updated_at();  
create trigger justifications_set_updated_at before update on private.response_justifications  
for each row execute function private.set_updated_at();  
create trigger communications_set_updated_at before update on public.communications  
for each row execute function private.set_updated_at();  
create trigger communication_recipients_set_updated_at  
before update on public.communication_recipients  
for each row execute function private.set_updated_at();  
  
-- append-only  
create trigger roster_events_no_mutation before update or delete  
on public.athlete_roster_events for each row  
execute function private.prevent_update_delete();  
create trigger responses_no_mutation before update or delete  
on public.operational_responses for each row  
execute function private.prevent_update_delete();  
create trigger corrections_no_mutation before update or delete  
on public.response_corrections for each row  
execute function private.prevent_update_delete();  
create trigger attendance_no_mutation before update or delete  
on public.attendance_records for each row  
execute function private.prevent_update_delete();  
create trigger audit_no_mutation before update or delete  
on audit.audit_events for each row  
execute function private.prevent_update_delete();  
  
  
create or replace function public.handle_new_auth_user()  
returns trigger  
language plpgsql  
security definer  
set search_path = ''  
as $$  
begin  
insert into public.profiles (id, display_name)  
values (  
new.id,  
coalesce(nullif(new.raw_user_meta_data ->> 'display_name', ''), 'Usuário')  
) on conflict (id) do nothing;  
return new;  
end;  
$$;  
  
create trigger on_auth_user_created  
after insert on auth.users  
for each row execute function public.handle_new_auth_user();  

## 13.5 0004_views.sql

-- 0004_views.sql  
create or replace view public.v_current_roster  
with (security_invoker = true)  
as  
select  
arm.id as roster_membership_id,  
a.team_id,  
arm.season_id,  
a.id as athlete_id,  
a.profile_id,  
a.legacy_athlete_id,  
a.display_name,  
arm.status,  
arm.broad_function,  
arm.shirt_number,  
arm.starts_on,  
arm.ends_on  
from public.athlete_roster_memberships arm  
join public.athletes a on a.id = arm.athlete_id  
where arm.starts_on <= current_date  
and (arm.ends_on is null or arm.ends_on >= current_date)  
and arm.status in ('ATIVA', 'INATIVA_TEMPORARIA');  
  
create or replace view public.v_request_recipient_state  
with (security_invoker = true)  
as  
with latest_response as (  
select distinct on (request_recipient_id)  
request_recipient_id, id as response_id, option_id,  
responded_by_profile_id, responded_at  
from public.operational_responses  
order by request_recipient_id, responded_at desc, created_at desc  
), latest_correction as (  
select distinct on (request_recipient_id)  
request_recipient_id, id as correction_id, action,  
replacement_option_id, corrected_at  
from public.response_corrections  
order by request_recipient_id, corrected_at desc  
)  
select  
rr.id as request_recipient_id,  
r.team_id,  
r.id as request_id,  
r.commitment_id,  
rr.athlete_id,  
lr.response_id,  
lc.correction_id,  
case  
when rr.cancelled_at is not null then 'CANCELLED'  
when lc.action = 'VOID' then 'NOT_RESPONDED'  
when lc.action = 'REPLACE' then co.code  
when lr.response_id is null then 'NOT_RESPONDED'  
else ro.code  
end as effective_option_code,  
case  
when lc.action = 'REPLACE' then co.semantic_group  
when lc.action = 'VOID' or lr.response_id is null then null  
else ro.semantic_group  
end as effective_semantic_group,  
lr.responded_at,  
lc.corrected_at,  
r.deadline_at,  
(lr.response_id is null and lc.correction_id is null and rr.cancelled_at is null) as pending  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
left join latest_response lr on lr.request_recipient_id = rr.id  
left join latest_correction lc on lc.request_recipient_id = rr.id  
left join public.request_definition_options ro on ro.id = lr.option_id  
left join public.request_definition_options co on co.id = lc.replacement_option_id;  
  
create or replace view public.v_calendar  
with (security_invoker = true)  
as  
select  
c.id as commitment_id,  
c.team_id,  
c.season_id,  
c.commitment_type,  
c.title,  
c.starts_at,  
c.ends_at,  
c.timezone,  
c.location_name,  
c.status,  
c.published_at,  
c.cancelled_at,  
ts.id as training_session_id,  
ts.objective,  
ts.main_activity,  
ts.collective_goals,  
ts.athlete_guidance  
from public.commitments c  
left join public.training_sessions ts on ts.commitment_id = c.id;  
  
create or replace view public.v_current_published_lists  
with (security_invoker = true)  
as  
select  
l.id as list_id,  
l.team_id,  
l.commitment_id,  
l.list_type,  
l.version,  
l.title,  
l.published_at,  
m.athlete_id,  
m.display_name_snapshot,  
m.broad_function_snapshot,  
m.sort_order,  
m.public_note  
from public.operational_lists l  
join public.operational_list_members m on m.list_id = l.id  
where l.status = 'PUBLICADA';  
  
create or replace view public.v_training_expected_composition  
with (security_invoker = true)  
as  
select  
l.team_id,  
l.commitment_id,  
m.broad_function_snapshot as broad_function,  
count(*)::integer as expected_athletes  
from public.operational_lists l  
join public.operational_list_members m on m.list_id = l.id  
where l.status = 'PUBLICADA'  
and l.list_type = 'TRAINING_EXPECTED'  
group by l.team_id, l.commitment_id, m.broad_function_snapshot;  
  
create or replace view public.v_function_coverage  
with (security_invoker = true)  
as  
select  
s.team_id,  
s.request_id,  
s.commitment_id,  
r.broad_function,  
count(*) filter (where s.effective_semantic_group = 'AFFIRMATIVE')::integer as affirmative,  
count(*) filter (where s.effective_semantic_group = 'UNCERTAIN')::integer as uncertain,  
count(*) filter (where s.effective_semantic_group = 'NEGATIVE')::integer as negative,  
count(*) filter (where s.effective_option_code = 'NOT_RESPONDED')::integer as not_responded  
from public.v_request_recipient_state s  
join public.v_current_roster r on r.athlete_id = s.athlete_id  
group by s.team_id, s.request_id, s.commitment_id, r.broad_function;  
  
create or replace view public.v_availability_attendance_divergence  
with (security_invoker = true)  
as  
with latest_attendance as (  
select distinct on (training_session_id, athlete_id)  
training_session_id, athlete_id, status as attendance_status, recorded_at  
from public.attendance_records  
order by training_session_id, athlete_id, recorded_at desc, created_at desc  
)  
select  
rs.team_id,  
rs.request_id,  
rs.commitment_id,  
ts.id as training_session_id,  
rs.athlete_id,  
rs.effective_option_code as availability_code,  
la.attendance_status,  
la.recorded_at,  
case  
when la.attendance_status is null then 'ATTENDANCE_NOT_RECORDED'  
when rs.effective_semantic_group = 'AFFIRMATIVE'  
and la.attendance_status = 'AUSENTE' then 'CONFIRMED_BUT_ABSENT'  
when rs.effective_semantic_group = 'NEGATIVE'  
and la.attendance_status in ('PRESENTE','ATRASADA','SAIDA_ANTECIPADA') then 'UNAVAILABLE_BUT_ATTENDED'  
else 'NO_DIVERGENCE'  
end as divergence_code  
from public.v_request_recipient_state rs  
join public.training_sessions ts on ts.commitment_id = rs.commitment_id  
left join latest_attendance la  
on la.training_session_id = ts.id and la.athlete_id = rs.athlete_id;  
  
create or replace view public.v_athlete_inbox  
with (security_invoker = true)  
as  
select  
'REQUEST'::text as item_type,  
rr.athlete_id,  
r.team_id,  
r.id as item_id,  
r.title,  
r.opens_at as available_at,  
r.deadline_at as due_at,  
case when s.pending then 'PENDING' else 'ANSWERED' end as item_status  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.v_request_recipient_state s on s.request_recipient_id = rr.id  
where rr.cancelled_at is null  
union all  
select  
'COMMUNICATION'::text,  
cr.athlete_id,  
c.team_id,  
c.id,  
c.title,  
c.valid_from,  
c.valid_until,  
case  
when cr.acknowledged_at is not null then 'ACKNOWLEDGED'  
when cr.viewed_at is not null then 'VIEWED'  
else 'UNREAD'  
end  
from public.communication_recipients cr  
join public.communications c on c.id = cr.communication_id  
where c.status = 'PUBLICADA';  
  
create or replace view public.v_coach_pending_actions  
with (security_invoker = true)  
as  
select  
r.team_id,  
'REQUEST_RESPONSES'::text as action_type,  
r.id as entity_id,  
r.title,  
r.deadline_at as due_at,  
count(*) filter (where s.pending)::integer as pending_count  
from public.operational_requests r  
join public.v_request_recipient_state s on s.request_id = r.id  
where r.status = 'ABERTA'  
group by r.team_id, r.id, r.title, r.deadline_at  
having count(*) filter (where s.pending) > 0  
union all  
select  
c.team_id,  
'COMMUNICATION_ACK'::text,  
c.id,  
c.title,  
c.valid_until,  
count(*) filter (where cr.acknowledged_at is null)::integer  
from public.communications c  
join public.communication_recipients cr on cr.communication_id = c.id  
where c.status = 'PUBLICADA'  
group by c.team_id, c.id, c.title, c.valid_until  
having count(*) filter (where cr.acknowledged_at is null) > 0;  
  
create or replace view public.v_operational_state  
with (security_invoker = true)  
as  
select  
t.id as team_id,  
t.name as team_name,  
(select count(*) from public.v_current_roster r  
where r.team_id = t.id and r.status = 'ATIVA')::integer as active_roster_count,  
(select count(*) from public.commitments c  
where c.team_id = t.id and c.starts_at >= now()  
and c.status in ('PLANEJADO','PUBLICADO'))::integer as upcoming_commitments,  
(select count(*) from public.v_request_recipient_state s  
where s.team_id = t.id and s.pending)::integer as pending_responses,  
(select count(*) from public.communication_recipients cr  
join public.communications c on c.id = cr.communication_id  
where c.team_id = t.id and c.status = 'PUBLICADA'  
and cr.acknowledged_at is null)::integer as pending_acknowledgements  
from public.teams t;  
  
grant select on public.v_current_roster,  
public.v_request_recipient_state,  
public.v_calendar,  
public.v_current_published_lists,  
public.v_training_expected_composition,  
public.v_function_coverage,  
public.v_availability_attendance_divergence,  
public.v_athlete_inbox,  
public.v_coach_pending_actions,  
public.v_operational_state  
to authenticated;  

## 13.6 0005_rls.sql

-- 0005_rls.sql  
revoke all on schema private from anon, authenticated;  
revoke all on schema audit from anon, authenticated;  
grant usage on schema public to anon, authenticated;  
  
create or replace function private.is_team_member(p_team_id uuid)  
returns boolean  
language sql  
stable  
security definer  
set search_path = ''  
as $$  
select exists (  
select 1  
from public.team_access_memberships m  
join public.profiles p on p.id = m.profile_id  
where m.team_id = p_team_id  
and m.profile_id = auth.uid()  
and m.status = 'ACTIVE'  
and p.active  
and m.valid_from <= now()  
and (m.valid_until is null or m.valid_until > now())  
);  
$$;  
  
create or replace function private.is_team_coach(p_team_id uuid)  
returns boolean  
language sql  
stable  
security definer  
set search_path = ''  
as $$  
select exists (  
select 1  
from public.team_access_memberships m  
join public.profiles p on p.id = m.profile_id  
where m.team_id = p_team_id  
and m.profile_id = auth.uid()  
and m.role = 'COACH'  
and m.status = 'ACTIVE'  
and p.active  
and m.valid_from <= now()  
and (m.valid_until is null or m.valid_until > now())  
and coalesce(auth.jwt() ->> 'aal', 'aal1') = 'aal2'  
);  
$$;  
  
create or replace function private.is_own_athlete(p_athlete_id uuid)  
returns boolean  
language sql  
stable  
security definer  
set search_path = ''  
as $$  
select exists (  
select 1 from public.athletes a  
where a.id = p_athlete_id and a.profile_id = auth.uid()  
);  
$$;  
  
revoke all on function private.is_team_member(uuid) from public;  
revoke all on function private.is_team_coach(uuid) from public;  
revoke all on function private.is_own_athlete(uuid) from public;  
grant execute on function private.is_team_member(uuid) to authenticated;  
grant execute on function private.is_team_coach(uuid) to authenticated;  
grant execute on function private.is_own_athlete(uuid) to authenticated;  
  
alter table public.teams enable row level security;  
alter table public.seasons enable row level security;  
alter table public.profiles enable row level security;  
alter table public.team_access_memberships enable row level security;  
alter table public.athletes enable row level security;  
alter table public.athlete_roster_memberships enable row level security;  
alter table public.athlete_roster_events enable row level security;  
alter table public.commitments enable row level security;  
alter table public.training_sessions enable row level security;  
alter table public.request_definitions enable row level security;  
alter table public.request_definition_options enable row level security;  
alter table public.operational_requests enable row level security;  
alter table public.request_recipients enable row level security;  
alter table public.operational_responses enable row level security;  
alter table public.justification_categories enable row level security;  
alter table private.response_justifications enable row level security;  
alter table public.response_corrections enable row level security;  
alter table public.operational_lists enable row level security;  
alter table public.operational_list_members enable row level security;  
alter table public.attendance_records enable row level security;  
alter table public.communications enable row level security;  
alter table public.communication_recipients enable row level security;  
alter table audit.audit_events enable row level security;  
  
-- Equipe e temporada  
create policy teams_select_member on public.teams  
for select to authenticated using (private.is_team_member(id));  
create policy seasons_select_member on public.seasons  
for select to authenticated using (private.is_team_member(team_id));  
create policy seasons_write_coach on public.seasons  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
  
-- Perfil e acesso  
create policy profiles_select_self_or_coach on public.profiles  
for select to authenticated using (  
id = auth.uid() or exists (  
select 1 from public.team_access_memberships self_m  
join public.team_access_memberships target_m on target_m.team_id = self_m.team_id  
where self_m.profile_id = auth.uid()  
and self_m.role = 'COACH' and self_m.status = 'ACTIVE'  
and target_m.profile_id = profiles.id  
and private.is_team_coach(self_m.team_id)  
)  
);  
create policy team_access_select_self_or_coach on public.team_access_memberships  
for select to authenticated using (  
profile_id = auth.uid() or private.is_team_coach(team_id)  
);  
create policy team_access_write_coach on public.team_access_memberships  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
  
-- Atletas e elenco  
create policy athletes_select_own_or_coach on public.athletes  
for select to authenticated using (  
profile_id = auth.uid() or private.is_team_coach(team_id)  
);  
create policy athletes_write_coach on public.athletes  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy roster_select_own_or_coach on public.athlete_roster_memberships  
for select to authenticated using (  
private.is_own_athlete(athlete_id) or exists (  
select 1 from public.athletes a  
where a.id = athlete_id and private.is_team_coach(a.team_id)  
)  
);  
create policy roster_write_coach on public.athlete_roster_memberships  
for all to authenticated using (  
exists (select 1 from public.athletes a where a.id = athlete_id and private.is_team_coach(a.team_id))  
) with check (  
exists (select 1 from public.athletes a where a.id = athlete_id and private.is_team_coach(a.team_id))  
);  
create policy roster_events_select_own_or_coach on public.athlete_roster_events  
for select to authenticated using (  
exists (  
select 1 from public.athlete_roster_memberships m  
join public.athletes a on a.id = m.athlete_id  
where m.id = membership_id  
and (a.profile_id = auth.uid() or private.is_team_coach(a.team_id))  
)  
);  
  
-- Compromissos e treinos  
create policy commitments_select_authorized on public.commitments  
for select to authenticated using (  
private.is_team_coach(team_id)  
or (private.is_team_member(team_id) and status <> 'RASCUNHO')  
);  
create policy commitments_write_coach on public.commitments  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy training_select_authorized on public.training_sessions  
for select to authenticated using (  
exists (  
select 1 from public.commitments c  
where c.id = commitment_id  
and (private.is_team_coach(c.team_id)  
or (private.is_team_member(c.team_id) and c.status <> 'RASCUNHO'))  
)  
);  
create policy training_write_coach on public.training_sessions  
for all to authenticated using (  
exists (select 1 from public.commitments c where c.id = commitment_id and private.is_team_coach(c.team_id))  
) with check (  
exists (select 1 from public.commitments c where c.id = commitment_id and private.is_team_coach(c.team_id))  
);  
  
-- Definições e opções  
create policy request_def_select_member on public.request_definitions  
for select to authenticated using (private.is_team_member(team_id));  
create policy request_def_write_coach on public.request_definitions  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy request_options_select_member on public.request_definition_options  
for select to authenticated using (  
exists (select 1 from public.request_definitions d  
where d.id = request_definition_id and private.is_team_member(d.team_id))  
);  
create policy request_options_write_coach on public.request_definition_options  
for all to authenticated using (  
exists (select 1 from public.request_definitions d  
where d.id = request_definition_id and private.is_team_coach(d.team_id))  
) with check (  
exists (select 1 from public.request_definitions d  
where d.id = request_definition_id and private.is_team_coach(d.team_id))  
);  
  
-- Solicitações e respostas  
create policy requests_select_coach_or_recipient on public.operational_requests  
for select to authenticated using (  
private.is_team_coach(team_id)  
or exists (  
select 1 from public.request_recipients rr  
join public.athletes a on a.id = rr.athlete_id  
where rr.request_id = operational_requests.id  
and rr.cancelled_at is null and a.profile_id = auth.uid()  
)  
);  
create policy requests_write_coach on public.operational_requests  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy recipients_select_coach_or_self on public.request_recipients  
for select to authenticated using (  
exists (  
select 1 from public.operational_requests r  
join public.athletes a on a.id = athlete_id  
where r.id = request_id  
and (private.is_team_coach(r.team_id) or a.profile_id = auth.uid())  
)  
);  
create policy recipients_write_coach on public.request_recipients  
for all to authenticated using (  
exists (select 1 from public.operational_requests r where r.id = request_id and private.is_team_coach(r.team_id))  
) with check (  
exists (select 1 from public.operational_requests r where r.id = request_id and private.is_team_coach(r.team_id))  
);  
create policy responses_select_coach_or_self on public.operational_responses  
for select to authenticated using (  
exists (  
select 1 from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.athletes a on a.id = rr.athlete_id  
where rr.id = request_recipient_id  
and (private.is_team_coach(r.team_id) or a.profile_id = auth.uid())  
)  
);  
create policy categories_select_member on public.justification_categories  
for select to authenticated using (private.is_team_member(team_id));  
create policy categories_write_coach on public.justification_categories  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy corrections_select_coach_or_self on public.response_corrections  
for select to authenticated using (  
exists (  
select 1 from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.athletes a on a.id = rr.athlete_id  
where rr.id = request_recipient_id  
and (private.is_team_coach(r.team_id) or a.profile_id = auth.uid())  
)  
);  
  
-- Listas  
create policy lists_select_authorized on public.operational_lists  
for select to authenticated using (  
private.is_team_coach(team_id)  
or (status = 'PUBLICADA' and private.is_team_member(team_id))  
);  
create policy lists_write_coach on public.operational_lists  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy list_members_select_authorized on public.operational_list_members  
for select to authenticated using (  
exists (  
select 1 from public.operational_lists l  
where l.id = list_id  
and (private.is_team_coach(l.team_id)  
or (l.status = 'PUBLICADA' and private.is_team_member(l.team_id)))  
)  
);  
create policy list_members_write_coach on public.operational_list_members  
for all to authenticated using (  
exists (select 1 from public.operational_lists l where l.id = list_id and private.is_team_coach(l.team_id))  
) with check (  
exists (select 1 from public.operational_lists l where l.id = list_id and private.is_team_coach(l.team_id))  
);  
  
-- Presença  
create policy attendance_select_own_or_coach on public.attendance_records  
for select to authenticated using (  
private.is_own_athlete(athlete_id)  
or exists (  
select 1 from public.training_sessions ts  
join public.commitments c on c.id = ts.commitment_id  
where ts.id = training_session_id and private.is_team_coach(c.team_id)  
)  
);  
  
-- Comunicação  
create policy communications_select_coach_or_recipient on public.communications  
for select to authenticated using (  
private.is_team_coach(team_id)  
or exists (  
select 1 from public.communication_recipients cr  
where cr.communication_id = communications.id and cr.profile_id = auth.uid()  
)  
);  
create policy communications_write_coach on public.communications  
for all to authenticated using (private.is_team_coach(team_id))  
with check (private.is_team_coach(team_id));  
create policy communication_recipients_select_self_or_coach on public.communication_recipients  
for select to authenticated using (  
profile_id = auth.uid()  
or exists (  
select 1 from public.communications c  
where c.id = communication_id and private.is_team_coach(c.team_id)  
)  
);  
  
-- Auditoria: apenas treinador AAL2 lê; nenhum cliente escreve.  
create policy audit_select_coach on audit.audit_events  
for select to authenticated using (team_id is not null and private.is_team_coach(team_id));  
  
-- Grants mínimos. Escritas sensíveis ocorrem exclusivamente por RPC.  
grant select on all tables in schema public to authenticated;  
grant insert, update, delete on public.seasons,  
public.team_access_memberships,  
public.athletes,  
public.athlete_roster_memberships,  
public.commitments,  
public.training_sessions,  
public.request_definitions,  
public.request_definition_options,  
public.operational_requests,  
public.request_recipients,  
public.justification_categories,  
public.operational_lists,  
public.operational_list_members,  
public.communications  
to authenticated;  
  
grant select on audit.audit_events to authenticated;  
revoke all on private.response_justifications from anon, authenticated;  
revoke insert, update, delete on public.operational_responses,  
public.athlete_roster_events,  
public.response_corrections,  
public.attendance_records,  
public.communication_recipients  
from authenticated;  
  
  
revoke select on public.response_corrections from authenticated;  
grant select (  
id, request_recipient_id, response_id, action,  
replacement_option_id, corrected_at, supersedes_correction_id  
) on public.response_corrections to authenticated;  

## 13.7 0006_rpcs.sql

-- 0006_rpcs.sql  
create or replace function public.submit_operational_response(  
p_request_recipient_id uuid,  
p_option_code text,  
p_category_code text default null,  
p_justification text default null,  
p_client_submission_id uuid default gen_random_uuid()  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_request public.operational_requests%rowtype;  
v_athlete public.athletes%rowtype;  
v_option_id uuid;  
v_previous_id uuid;  
v_response_id uuid;  
v_category_id uuid;  
v_allow_justification boolean;  
begin  
select r, a into v_request, v_athlete  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
join public.athletes a on a.id = rr.athlete_id  
where rr.id = p_request_recipient_id  
and rr.cancelled_at is null;  
  
if not found or v_athlete.profile_id is distinct from auth.uid() then  
raise exception 'Destinatário não autorizado';  
end if;  
if v_request.status <> 'ABERTA'  
or now() < v_request.opens_at  
or now() > v_request.deadline_at then  
raise exception 'Solicitação fora da janela de resposta';  
end if;  
  
select o.id, d.allow_justification  
into v_option_id, v_allow_justification  
from public.request_definition_options o  
join public.request_definitions d on d.id = o.request_definition_id  
where o.request_definition_id = v_request.definition_id  
and o.code = upper(p_option_code)  
and o.active;  
if v_option_id is null then  
raise exception 'Opção inválida';  
end if;  
  
select id into v_previous_id  
from public.operational_responses  
where request_recipient_id = p_request_recipient_id  
order by responded_at desc, created_at desc  
limit 1;  
  
insert into public.operational_responses (  
request_recipient_id, option_id, responded_by_profile_id,  
client_submission_id, supersedes_response_id  
) values (  
p_request_recipient_id, v_option_id, auth.uid(),  
p_client_submission_id, v_previous_id  
)  
on conflict (client_submission_id) do update  
set client_submission_id = excluded.client_submission_id  
returning id into v_response_id;  
  
if p_category_code is not null or nullif(btrim(p_justification), '') is not null then  
if not v_allow_justification then  
raise exception 'Esta solicitação não admite justificativa';  
end if;  
if p_category_code is not null then  
select id into v_category_id  
from public.justification_categories  
where team_id = v_request.team_id  
and code = upper(p_category_code)  
and active;  
if v_category_id is null then  
raise exception 'Categoria de justificativa inválida';  
end if;  
end if;  
insert into private.response_justifications (  
response_id, category_id, free_text, submitted_by_profile_id  
) values (  
v_response_id, v_category_id,  
nullif(btrim(p_justification), ''), auth.uid()  
) on conflict (response_id) do nothing;  
end if;  
  
insert into audit.audit_events (  
team_id, actor_profile_id, actor_auth_uid, event_type,  
entity_schema, entity_table, entity_id, after_data  
) values (  
v_request.team_id, auth.uid(), auth.uid(), 'RESPONSE_SUBMITTED',  
'public', 'operational_responses', v_response_id::text,  
jsonb_build_object('request_recipient_id', p_request_recipient_id,  
'option_id', v_option_id)  
);  
return v_response_id;  
end;  
$$;  
  
create or replace function public.correct_operational_response(  
p_request_recipient_id uuid,  
p_action public.correction_action,  
p_replacement_option_code text,  
p_reason text  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_team_id uuid;  
v_definition_id uuid;  
v_response_id uuid;  
v_option_id uuid;  
v_previous_correction uuid;  
v_id uuid;  
begin  
select r.team_id, r.definition_id into v_team_id, v_definition_id  
from public.request_recipients rr  
join public.operational_requests r on r.id = rr.request_id  
where rr.id = p_request_recipient_id;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
if nullif(btrim(p_reason), '') is null then  
raise exception 'Motivo obrigatório';  
end if;  
  
select id into v_response_id  
from public.operational_responses  
where request_recipient_id = p_request_recipient_id  
order by responded_at desc, created_at desc limit 1;  
  
if p_action = 'REPLACE' then  
select id into v_option_id  
from public.request_definition_options  
where request_definition_id = v_definition_id  
and code = upper(p_replacement_option_code) and active;  
if v_option_id is null then raise exception 'Opção substituta inválida'; end if;  
elsif p_replacement_option_code is not null then  
raise exception 'VOID não aceita opção substituta';  
end if;  
  
select id into v_previous_correction  
from public.response_corrections  
where request_recipient_id = p_request_recipient_id  
order by corrected_at desc limit 1;  
  
insert into public.response_corrections (  
request_recipient_id, response_id, action, replacement_option_id,  
reason, corrected_by_profile_id, supersedes_correction_id  
) values (  
p_request_recipient_id, v_response_id, p_action, v_option_id,  
btrim(p_reason), auth.uid(), v_previous_correction  
) returning id into v_id;  
  
insert into audit.audit_events (  
team_id, actor_profile_id, actor_auth_uid, event_type,  
entity_schema, entity_table, entity_id, after_data  
) values (  
v_team_id, auth.uid(), auth.uid(), 'RESPONSE_CORRECTED',  
'public', 'response_corrections', v_id::text,  
jsonb_build_object('request_recipient_id', p_request_recipient_id,  
'action', p_action, 'replacement_option_id', v_option_id)  
);  
return v_id;  
end;  
$$;  
  
create or replace function public.record_training_attendance(  
p_training_session_id uuid,  
p_athlete_id uuid,  
p_status public.attendance_status,  
p_arrived_at timestamptz default null,  
p_departed_at timestamptz default null,  
p_source_note text default null,  
p_client_record_id uuid default gen_random_uuid()  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_team_id uuid;  
v_previous_id uuid;  
v_id uuid;  
begin  
select c.team_id into v_team_id  
from public.training_sessions ts  
join public.commitments c on c.id = ts.commitment_id  
where ts.id = p_training_session_id;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
if not exists (select 1 from public.athletes a where a.id = p_athlete_id and a.team_id = v_team_id) then  
raise exception 'Atleta fora da equipe';  
end if;  
  
select id into v_previous_id  
from public.attendance_records  
where training_session_id = p_training_session_id  
and athlete_id = p_athlete_id  
order by recorded_at desc, created_at desc limit 1;  
  
insert into public.attendance_records (  
training_session_id, athlete_id, status, arrived_at, departed_at,  
recorded_by_profile_id, client_record_id, supersedes_record_id, source_note  
) values (  
p_training_session_id, p_athlete_id, p_status, p_arrived_at, p_departed_at,  
auth.uid(), p_client_record_id, v_previous_id, nullif(btrim(p_source_note),'')  
)  
on conflict (client_record_id) do update  
set client_record_id = excluded.client_record_id  
returning id into v_id;  
  
insert into audit.audit_events (  
team_id, actor_profile_id, actor_auth_uid, event_type,  
entity_schema, entity_table, entity_id, after_data  
) values (  
v_team_id, auth.uid(), auth.uid(), 'ATTENDANCE_RECORDED',  
'public', 'attendance_records', v_id::text,  
jsonb_build_object('training_session_id', p_training_session_id,  
'athlete_id', p_athlete_id, 'status', p_status)  
);  
return v_id;  
end;  
$$;  
  
create or replace function public.change_roster_membership(  
p_membership_id uuid,  
p_status public.athlete_relationship_status,  
p_broad_function public.broad_player_function,  
p_shirt_number smallint,  
p_effective_on date,  
p_reason text default null  
)  
returns uuid  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_old public.athlete_roster_memberships%rowtype;  
v_team_id uuid;  
v_event_id uuid;  
begin  
select m.*, a.team_id into v_old, v_team_id  
from public.athlete_roster_memberships m  
join public.athletes a on a.id = m.athlete_id  
where m.id = p_membership_id for update;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
if p_shirt_number is not null and (p_shirt_number < 1 or p_shirt_number > 99) then  
raise exception 'Número de camisa deve estar entre 1 e 99';  
end if;  
  
update public.athlete_roster_memberships  
set status = p_status,  
broad_function = p_broad_function,  
shirt_number = p_shirt_number,  
ends_on = case when p_status = 'VINCULO_ENCERRADO' then p_effective_on else ends_on end  
where id = p_membership_id;  
  
insert into public.athlete_roster_events (  
membership_id, event_type, effective_on, from_state, to_state,  
reason, actor_profile_id  
) values (  
p_membership_id, 'MEMBERSHIP_CHANGED', p_effective_on,  
jsonb_build_object('status', v_old.status, 'broad_function', v_old.broad_function,  
'shirt_number', v_old.shirt_number, 'ends_on', v_old.ends_on),  
jsonb_build_object('status', p_status, 'broad_function', p_broad_function,  
'shirt_number', p_shirt_number),  
nullif(btrim(p_reason),''), auth.uid()  
) returning id into v_event_id;  
return v_event_id;  
end;  
$$;  
  
create or replace function public.mark_communication_viewed(p_recipient_id uuid)  
returns timestamptz  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare v_time timestamptz;  
begin  
update public.communication_recipients  
set viewed_at = coalesce(viewed_at, now())  
where id = p_recipient_id and profile_id = auth.uid()  
returning viewed_at into v_time;  
if v_time is null then raise exception 'Destinatário não autorizado'; end if;  
return v_time;  
end;  
$$;  
  
create or replace function public.acknowledge_communication(p_recipient_id uuid)  
returns timestamptz  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare v_time timestamptz;  
begin  
update public.communication_recipients  
set viewed_at = coalesce(viewed_at, now()),  
acknowledged_at = coalesce(acknowledged_at, now())  
where id = p_recipient_id and profile_id = auth.uid()  
returning acknowledged_at into v_time;  
if v_time is null then raise exception 'Destinatário não autorizado'; end if;  
return v_time;  
end;  
$$;  
  
create or replace function public.close_operational_request(p_request_id uuid)  
returns void  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare v_team_id uuid;  
begin  
select team_id into v_team_id from public.operational_requests where id = p_request_id;  
if v_team_id is null or not private.is_team_coach(v_team_id) then  
raise exception 'Ação não autorizada';  
end if;  
update public.operational_requests  
set status = 'ENCERRADA', closed_at = now()  
where id = p_request_id and status = 'ABERTA';  
end;  
$$;  
  
revoke all on function public.submit_operational_response(uuid,text,text,text,uuid) from public;  
revoke all on function public.correct_operational_response(uuid,public.correction_action,text,text) from public;  
revoke all on function public.record_training_attendance(uuid,uuid,public.attendance_status,timestamptz,timestamptz,text,uuid) from public;  
revoke all on function public.change_roster_membership(uuid,public.athlete_relationship_status,public.broad_player_function,smallint,date,text) from public;  
revoke all on function public.mark_communication_viewed(uuid) from public;  
revoke all on function public.acknowledge_communication(uuid) from public;  
revoke all on function public.close_operational_request(uuid) from public;  
  
grant execute on function public.submit_operational_response(uuid,text,text,text,uuid) to authenticated;  
grant execute on function public.correct_operational_response(uuid,public.correction_action,text,text) to authenticated;  
grant execute on function public.record_training_attendance(uuid,uuid,public.attendance_status,timestamptz,timestamptz,text,uuid) to authenticated;  
grant execute on function public.change_roster_membership(uuid,public.athlete_relationship_status,public.broad_player_function,smallint,date,text) to authenticated;  
grant execute on function public.mark_communication_viewed(uuid) to authenticated;  
grant execute on function public.acknowledge_communication(uuid) to authenticated;  
grant execute on function public.close_operational_request(uuid) to authenticated;  

## 13.8 0007_audit.sql

-- 0007_audit.sql  
create or replace function audit.capture_row_change()  
returns trigger  
language plpgsql  
security definer  
set search_path = ''  
as $$  
declare  
v_team_id uuid;  
v_entity_id text;  
v_before jsonb;  
v_after jsonb;  
begin  
v_before := case when tg_op in ('UPDATE','DELETE') then to_jsonb(old) else null end;  
v_after := case when tg_op in ('INSERT','UPDATE') then to_jsonb(new) else null end;  
v_entity_id := coalesce(v_after ->> 'id', v_before ->> 'id');  
v_team_id := nullif(coalesce(v_after ->> 'team_id', v_before ->> 'team_id'), '')::uuid;  
  
insert into audit.audit_events (  
team_id, actor_profile_id, actor_auth_uid, event_type,  
entity_schema, entity_table, entity_id, before_data, after_data  
) values (  
v_team_id, auth.uid(), auth.uid(), tg_op,  
tg_table_schema, tg_table_name, v_entity_id,  
v_before - array['updated_at'], v_after - array['updated_at']  
);  
return coalesce(new, old);  
end;  
$$;  
  
create trigger audit_teams after insert or update or delete on public.teams  
for each row execute function audit.capture_row_change();  
create trigger audit_seasons after insert or update or delete on public.seasons  
for each row execute function audit.capture_row_change();  
create trigger audit_team_access after insert or update or delete on public.team_access_memberships  
for each row execute function audit.capture_row_change();  
create trigger audit_athletes after insert or update or delete on public.athletes  
for each row execute function audit.capture_row_change();  
create trigger audit_roster after insert or update or delete on public.athlete_roster_memberships  
for each row execute function audit.capture_row_change();  
create trigger audit_commitments after insert or update or delete on public.commitments  
for each row execute function audit.capture_row_change();  
create trigger audit_training after insert or update or delete on public.training_sessions  
for each row execute function audit.capture_row_change();  
create trigger audit_requests after insert or update or delete on public.operational_requests  
for each row execute function audit.capture_row_change();  
create trigger audit_lists after insert or update or delete on public.operational_lists  
for each row execute function audit.capture_row_change();  
create trigger audit_communications after insert or update or delete on public.communications  
for each row execute function audit.capture_row_change();  

## 13.9 0008_seed_synthetic.sql

-- 0008_seed_synthetic.sql  
-- Somente ambiente sintético. Não importar nomes ou contatos reais.  
insert into public.teams (  
id, code, name, timezone, locale, synthetic_only, active  
) values (  
'11111111-1111-4111-8111-111111111111',  
'CEPRAEA', 'CEPRAEA', 'America/Sao_Paulo', 'pt-BR', true, true  
) on conflict (code) do nothing;  
  
insert into public.seasons (  
id, team_id, label, starts_on, ends_on, status, ruleset_code  
) values (  
'22222222-2222-4222-8222-222222222222',  
'11111111-1111-4111-8111-111111111111',  
'Temporada sintética 2026', date '2026-01-01', date '2026-12-31',  
'ATIVA', 'IHF_BEACH_2026-04-01'  
) on conflict (team_id, label) do nothing;  
  
insert into public.request_definitions (  
id, team_id, code, name, subject_type, description,  
allow_justification, active  
) values (  
'33333333-3333-4333-8333-333333333333',  
'11111111-1111-4111-8111-111111111111',  
'TRAINING_AVAILABILITY', 'Disponibilidade para treino', 'COMMITMENT',  
'Declaração antecipada; não comprova presença real.', true, true  
) on conflict (team_id, code) do nothing;  
  
insert into public.request_definition_options (  
request_definition_id, code, label, semantic_group, sort_order,  
requires_justification, active  
) values  
('33333333-3333-4333-8333-333333333333','YES','Sim','AFFIRMATIVE',10,false,true),  
('33333333-3333-4333-8333-333333333333','NO','Não','NEGATIVE',20,false,true),  
('33333333-3333-4333-8333-333333333333','UNCERTAIN','Talvez','UNCERTAIN',30,false,true)  
on conflict (request_definition_id, code) do nothing;  
  
insert into public.justification_categories (  
team_id, code, label, description, sensitive, sort_order, active  
) values  
('11111111-1111-4111-8111-111111111111','LOGISTICS','Logística','Deslocamento ou horário.',false,10,true),  
('11111111-1111-4111-8111-111111111111','PERSONAL','Questão pessoal','Detalhe opcional e privado.',true,20,true),  
('11111111-1111-4111-8111-111111111111','HEALTH_PRIVATE','Saúde - privado','Não solicitar diagnóstico.',true,30,true),  
('11111111-1111-4111-8111-111111111111','OTHER','Outro','Texto curto opcional.',false,40,true)  
on conflict (team_id, code) do nothing;  

# 14. Estratégia de implementação e validação

| **Marco** | **Conteúdo** | **Critério de aceite** |
| --- | --- | --- |
| M0 | Projeto Supabase local, migrations, lint SQL e testes de schema. | Migrations sobem do zero e fazem rollback controlado. |
| --- | --- | --- |
| M1 | Auth, profiles, acesso por equipe, atletas e elenco. | Testes RLS positivos e negativos; treinador exige AAL2. |
| --- | --- | --- |
| M2 | Compromissos, treinos, solicitações, respostas e inbox. | Quatro estados efetivos: sim, não, talvez, não respondeu; versões preservadas. |
| --- | --- | --- |
| M3 | Listas previstas, presença factual e cobertura. | Lista não implica presença; presença não é inferida. |
| --- | --- | --- |
| M4 | Comunicações, ciência, auditoria e privacidade. | Justificativa ausente de listas/logs; eventos auditáveis. |
| --- | --- | --- |
| Gate real | Nova decisão para dados reais, migração e produção. | Base legal, minimização, retenção, backup e plano de reversão aprovados. |
| --- | --- | --- |

-   Executar migrations em banco vazio no CI.
-   Aplicar pgTAP ou testes SQL para constraints, RPCs e RLS.
-   Testar duas atletas distintas para impedir leitura cruzada.
-   Testar treinador sem AAL2 para negar escrita privilegiada.
-   Testar retries offline usando client_submission_id/client_record_id.
-   Testar que listas e views nunca retornam justification/free_text.
-   Não iniciar importação das planilhas enquanto o gate de dados reais estiver fechado.

# 15. Contrato de extensibilidade futura

As entidades abaixo são previstas, mas não devem ser criadas no MVP atual. Elas entram por novas decisões e migrations, sem alterar o significado das 23 tabelas existentes.

| **Tabela/módulo futuro** | **Responsabilidade** |
| --- | --- |
| competitions | Cadastro de competições e organização externa; fora do MVP autorizado. |
| --- | --- |
| competition_stages | Etapas/fases e regras locais versionadas. |
| --- | --- |
| competition_rule_snapshots | Limites de inscrição e partida por competição, evitando constants globais. |
| --- | --- |
| matches | Partidas garantidas ou condicionais, adversário, fase e estado. |
| --- | --- |
| match_periods | Set 1, Set 2, Golden Goal quando aplicável e Shoot-out; resultado por período. |
| --- | --- |
| match_rosters | Atletas habilitadas para uma partida; convocação de etapa não equivale a escalação. |
| --- | --- |
| match_participations | Participação factual por partida; convocada não equivale a jogou. |
| --- | --- |
| match_role_assignments | Papel tático temporal. ESPECIALISTA é o código canônico e CORINGA é alias do mesmo papel. |
| --- | --- |
| result_validations | Fonte, revisor e versão do resultado oficial. |
| --- | --- |
| source_documents / record_provenance | Proveniência de migração e documentos oficiais. |
| --- | --- |
| import_batches / import_batch_items | Migração controlada e reprocessável de planilhas. |
| --- | --- |
| external_metric_snapshots | Contrato para métricas agregadas de Scout externo, sem misturar eventos brutos ao banco operacional. |
| --- | --- |

## Regra específica de especialista/coringa

-- Futuro módulo de partidas (não executar no MVP atual)  
-- Código canônico do papel tático: ESPECIALISTA  
-- Alias de domínio/legado: CORINGA  
-- Nunca adicionar ESPECIALISTA ou CORINGA ao enum broad_player_function.  
-- A atribuição deve possuir match_id, period_id/intervalo e athlete_id.

# 16. Matriz de substituição das planilhas

| **Origem atual** | **Destino no banco** | **Tratamento** |
| --- | --- | --- |
| DB_CONFIG | Configuração de ambiente/migrations | Não virar tabela genérica de chave-valor no domínio. |
| --- | --- | --- |
| DB_ATLETAS | athletes + athlete_roster_memberships | Nome deixa de ser chave; posição específica é adiada. |
| --- | --- | --- |
| DB_FUNCOES | enum broad_player_function | Remover CORINGA/ESPECIALISTA; manter quatro valores. |
| --- | --- | --- |
| DB_POSICOES e sistemas táticos | Módulo futuro | Não migrar para o MVP sem validação esportiva. |
| --- | --- | --- |
| DB_TREINOS + DB_CALENDARIO | commitments + training_sessions + v_calendar | Eliminar duplicidade de agenda. |
| --- | --- | --- |
| DB_PRESENCA | requests/recipients/responses | Tratar como disponibilidade antecipada. |
| --- | --- | --- |
| Presença observada | attendance_records | Novo fato posterior ao treino. |
| --- | --- | --- |
| DB_AVISOS | communications + communication_recipients | Separar publicação, entrega, leitura e ciência. |
| --- | --- | --- |
| DB_CONVOCACOES | operational_requests/lists no futuro de competição | Não criar participação por inferência. |
| --- | --- | --- |
| DB_JOGOS e participação | Módulo futuro de matches | Sets, shoot-out, roster e participação separados. |
| --- | --- | --- |
| DB_INDICADORES/EXPORTS | Views | Não persistir métricas deriváveis. |
| --- | --- | --- |
| DB_CHANGELOG | audit_events + históricos de domínio | Audit log não substitui eventos semânticos. |
| --- | --- | --- |

# 17. Conclusão técnica

A modelagem proposta é a base correta para o MVP sintético atual: reduz ambiguidade, mantém fatos distintos, preserva versões, aplica privacidade por desenho e permite módulos futuros sem remodelar identidades ou históricos. O banco não deve incorporar tabelas de scout, posições específicas, partidas ou importação real antes das decisões correspondentes.