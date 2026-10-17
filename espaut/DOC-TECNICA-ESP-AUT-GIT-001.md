# ESP-AUT-GIT-001 — Documentação Técnica

| Campo | Valor |
|-------|-------|
| Especificação | ESP-AUT-GIT-001 v0.2.0 |
| Pacote | `espaut` v0.1.0 |
| Linguagem | Python 3.12+ (stdlib-only) |
| Data | 2026-10-17 |
| Módulos | 17 |
| Testes | 303/303 checks (15 arquivos) |
| Subcomandos CLI | 18 |

---

## 1. Visão Geral

O `espaut` é uma ferramenta CLI que previne duas classes de falha no desenvolvimento assistido por IA:

- **PROB-001** — Esquecimento de commit/push: alterações ficam apenas no ambiente local e são irrecuperáveis.
- **PROB-002 a PROB-006** — Fechamento silencioso de PR: verificações de CI falhas, comentários não respondidos, correções não aplicadas ou pendências não resolvidas são ignorados.

A ferramenta opera como um wrapper sobre `git` e `gh` (GitHub CLI), mantendo estado local em `.espaut/` e impondo fluxos de trabalho baseados em máquinas de estado.

### Pré-requisitos

- Python 3.12 ou superior
- `git` instalado e configurado
- `gh` (GitHub CLI) instalado e autenticado (para operações de PR)
- Sem dependências externas (stdlib-only)

### Restrições de Design

- Todas as chamadas a processos externos usam `subprocess.run(["cmd", ...], capture_output=True, text=True, timeout=N, check=False)` — nunca `shell=True`.
- Persistência via JSON/JSONL com escritas atômicas (`.tmp` → `os.replace`).
- Enums implementados com `enum.StrEnum` (Python 3.12) para serialização natural em JSON.
- Integridade de evidências via SHA-256.

---

## 2. Instalação e Uso Rápido

```bash
# Dentro de um repositório git:
python -m espaut init

# Criar uma tarefa
python -m espaut task create "Implementar feature X" --objective "Descrição do objetivo"

# Preservar alterações (dry-run por padrão)
python -m espaut preserve
python -m espaut preserve --confirm   # executa de fato

# Criar PR
python -m espaut pr create --title "Feature X"

# Verificar estado
python -m espaut checks
python -m espaut reviews
python -m espaut merge-check

# Ajuda completa
python -m espaut --help
```

### Fluxo Básico

```
init → task create → [editar código] → preserve --confirm → pr create
  → checks → reviews → pendencies → merge-check
```

---

## 3. Arquitetura

```
┌─────────────────────────────────────────────────┐
│                    CLI (cli.py)                  │
│  18 subcomandos · argparse · códigos de saída   │
├────────────┬──────────────┬─────────────────────┤
│  Domínio   │  Governança  │   Recuperação       │
│  task.py   │ governance.py│   recovery.py       │
│ preserv.py │ invariants.py│   triggers.py       │
│  review.py │ correction.py│                     │
│  checks.py │              │                     │
│ pullreq.py │              │                     │
├────────────┴──────────────┴─────────────────────┤
│            Motor de Estados (engine.py)          │
├────────────┬────────────────────────────────────┤
│  Git Ops   │  GitHub Ops    │   Segurança       │
│ git_ops.py │  gh_ops.py     │  security.py      │
├────────────┴────────────────┴───────────────────┤
│         Persistência (store.py · events.py)      │
│           .espaut/ · JSON · JSONL · SHA-256       │
└──────────────────────────────────────────────────┘
```

### Módulos (17)

| Módulo | Linhas | Descrição |
|--------|-------:|-----------|
| `__init__.py` | 3 | Raiz do pacote; exporta `__version__` |
| `__main__.py` | 6 | Ponto de entrada `python -m espaut` |
| `cli.py` | 654 | CLI argparse com 18 subcomandos |
| `engine.py` | 103 | Motor genérico de máquina de estados |
| `store.py` | 135 | Persistência `.espaut/`, JSON/JSONL I/O |
| `events.py` | 105 | Log de eventos append-only e evidências |
| `security.py` | 64 | Validação de subprocess e detecção de segredos |
| `git_ops.py` | 194 | Wrappers para comandos git |
| `gh_ops.py` | 184 | Wrappers para GitHub CLI (gh) |
| `task.py` | 94 | Entidade Tarefa e SM#1 |
| `preservation.py` | 309 | Detecção, staging, commit, push — SM#4 |
| `pullrequest.py` | 198 | Ciclo de vida do Pull Request |
| `checks.py` | 172 | Monitoramento de CI — SM#3 |
| `review.py` | 263 | Reviews, comentários, pendências — SM#2 |
| `governance.py` | 192 | Políticas, decisões, elegibilidade C1–C8 |
| `invariants.py` | 151 | Predicados INV-001 a INV-014 |
| `correction.py` | 156 | Diagnóstico e ciclo de correção |
| `recovery.py` | 161 | Recuperação de sessão e auditoria |
| `triggers.py` | 166 | Triggers, sincronização e detecção de conflitos |

---

## 4. Estrutura de Dados Local (`.espaut/`)

Criada por `espaut init` via `init_store()`:

```
.espaut/
├── .gitignore          # Contém "*" — exclui tudo do versionamento
├── config.json         # Configuração (espaut-config.schema.json)
├── events.jsonl        # Log de eventos append-only
├── tasks/              # TASK-{id}.json — registros de tarefas
├── evidence/           # EVD-{id}.json — evidências com SHA-256
├── decisions/          # DEC-{id}.json — decisões humanas
└── cache/              # Dados efêmeros (checks, reviews por PR)
```

### Padrões de Identificadores

| Prefixo | Entidade | Padrão regex |
|---------|----------|-------------|
| `TASK-` | Tarefa | `^TASK-[0-9a-f]{12}$` |
| `EVT-` | Evento | `^EVT-[0-9a-f]{12}$` |
| `EVD-` | Evidência | `^EVD-[0-9a-f]{12}$` |
| `DEC-` | Decisão | `^DEC-[0-9a-f]{12}$` |
| `DGN-` | Diagnóstico | `^DGN-[0-9a-f]{12}$` |
| `ATT-` | Tentativa | `^ATT-[0-9a-f]{12}$` |
| `PND-` | Pendência | `^PND-[0-9a-f]{12}$` |

### Configuração Padrão (`config.json`)

| Chave | Tipo | Padrão | Descrição |
|-------|------|--------|-----------|
| `schema_version` | string | `"0.1.0"` | Versão do esquema de configuração |
| `trigger_mode` | string | `"explicit"` | Modo de disparo: `explicit`, `hook`, `watch` |
| `preservation_events` | array | `["explicit"]` | Eventos que disparam preservação |
| `eligible_patterns` | array | `[]` | Padrões fnmatch de arquivos elegíveis (vazio = todos) |
| `ai_enabled` | boolean | `false` | Integração com IA habilitada |
| `auto_commit` | boolean | `false` | Commit automático (requer `--confirm`) |
| `resolver_roles` | array | `["author", "assigned_reviewers"]` | Papéis autorizados a resolver pendências |
| `merge_policy` | string | `"manual"` | Política de merge: `manual`, `semi_auto`, `auto` |
| `correction_max_attempts` | integer | `3` | Máximo de tentativas de correção por pendência |
| `retention_policy` | string | `"retain_all"` | Política de retenção: `retain_all`, `retain_recent`, `archive` |
| `ci_required` | boolean | `false` | CI obrigatório para elegibilidade de merge |

---

## 5. Referência CLI — 18 Subcomandos

Ponto de entrada: `python -m espaut <subcomando> [argumentos]`

Flag global: `--version` — exibe a versão do pacote.

### 5.1 Core

#### `init`

```
espaut init
```

Inicializa o diretório `.espaut/` na raiz do repositório git corrente. Cria a estrutura de diretórios, `config.json` com valores padrão, `events.jsonl` vazio e `.gitignore` interno.

- **Código de saída**: 0 (sucesso), 1 (não é repositório git)

#### `status`

```
espaut status
```

Exibe o estado da árvore de trabalho (branch, HEAD SHA, contagem de mudanças) e lista tarefas ativas do `.espaut/`.

- **Código de saída**: 0

#### `task create`

```
espaut task create TITULO [--objective OBJETIVO]
```

Cria uma nova tarefa no estado `REGISTRADA`.

| Argumento | Obrigatório | Descrição |
|-----------|:-----------:|-----------|
| `TITULO` | sim | Título da tarefa (posicional) |
| `--objective` | não | Objetivo da tarefa |

- **Código de saída**: 0
- **Saída**: `task_id=TASK-... state=REGISTRADA title=...`

#### `preserve`

```
espaut preserve [--task TASK-ID] [--confirm] [--message MSG]
```

Detecta alterações no worktree, classifica arquivos elegíveis, e executa staging → commit → push. Sem `--confirm`, opera em modo dry-run.

| Argumento | Obrigatório | Descrição |
|-----------|:-----------:|-----------|
| `--task` | não | ID da tarefa (auto-resolve se houver apenas uma ativa) |
| `--confirm` | não | Executa de fato (sem flag = dry-run) |
| `--message`, `-m` | não | Mensagem de commit |

- **Código de saída**: 0 (sucesso/dry-run), 1 (falha no staging ou commit)

### 5.2 Pull Request

#### `pr create`

```
espaut pr create [--task TASK-ID] [--title TITULO] [--body CORPO] [--base BRANCH]
```

Cria um PR via `gh pr create` ou reutiliza um existente para a mesma branch. Atualiza o registro da tarefa com `pr_number` e URL.

| Argumento | Obrigatório | Descrição |
|-----------|:-----------:|-----------|
| `--task` | não | ID da tarefa |
| `--title` | não | Título do PR (padrão: título da tarefa) |
| `--body` | não | Corpo do PR |
| `--base` | não | Branch base |

- **Código de saída**: 0 (sucesso), 1 (erro)

#### `pr status`

```
espaut pr status [--task TASK-ID]
```

Consulta o estado do PR no GitHub via `gh pr view`.

- **Código de saída**: 0 (sucesso), 1 (tarefa sem PR)
- **Saída**: `github_state`, `head_sha`, `review_decision`, `url`

### 5.3 Verificação

#### `checks`

```
espaut checks [--task TASK-ID]
```

Consulta o estado dos checks de CI para o PR da tarefa. Exibe o agregado e cada check individual.

- **Código de saída**: 0
- **Requer**: tarefa com `pr_number` associado

#### `reviews`

```
espaut reviews [--task TASK-ID]
```

Coleta reviews, comentários e comentários de código do PR. Exibe contagem e classificação.

- **Código de saída**: 0

#### `pendencies`

```
espaut pendencies [--task TASK-ID]
```

Lista pendências extraídas dos reviews, indicando bloqueantes vs. informativas.

- **Código de saída**: 0 (sem bloqueantes), 1 (pendências bloqueantes ativas)

### 5.4 Governança

#### `merge-check`

```
espaut merge-check [--task TASK-ID]
```

Avalia todos os 8 critérios de elegibilidade para merge (C1–C8). Exibe resultado de cada critério e veredito final.

- **Código de saída**: 0 (`APTA_PARA_INTEGRACAO`), 1 (`NAO_APTA`)

#### `decide`

```
espaut decide --task TASK-ID --type TIPO --value VALOR [--authority AUTORIDADE] [--scope ESCOPO]
```

Registra uma decisão humana no diretório `decisions/`.

| Argumento | Obrigatório | Descrição |
|-----------|:-----------:|-----------|
| `--task` | sim | ID da tarefa |
| `--type` | sim | Tipo da decisão (`approve`, `reject`, `defer`, `override`) |
| `--value` | sim | Valor da decisão |
| `--authority` | não | Autoridade (padrão: `cli_user`) |
| `--scope` | não | Escopo da decisão |

- **Código de saída**: 0

### 5.5 Correção

#### `diagnose`

```
espaut diagnose --pendency PND-ID --cause "descrição" [--source human|ai]
```

Cria um registro de diagnóstico para uma pendência.

| Argumento | Obrigatório | Descrição |
|-----------|:-----------:|-----------|
| `--pendency` | sim | ID da pendência |
| `--cause` | sim | Causa suspeitada |
| `--source` | não | Origem do diagnóstico (padrão: `human`) |

- **Código de saída**: 0

#### `correct`

```
espaut correct --task TASK-ID --pendency PND-ID [--confirm]
```

Verifica se há tentativas de correção restantes e, com `--confirm`, executa a preservação das correções.

- **Código de saída**: 0 (sucesso/dry-run), 1 (bloqueado por limite de tentativas ou falha)

#### `verify-correction`

```
espaut verify-correction [--task TASK-ID]
```

Re-consulta checks e reviews após uma correção. Reporta se pendências bloqueantes foram resolvidas.

- **Código de saída**: 0 (sem bloqueantes), 1 (pendências bloqueantes persistem)

### 5.6 Recuperação

#### `recover`

```
espaut recover [--task TASK-ID]
```

Reconcilia o estado registrado da tarefa com o estado real do git (branch, HEAD, worktree). Reporta discrepâncias e ações recomendadas.

- **Código de saída**: 0

#### `audit`

```
espaut audit [--task TASK-ID] [--verbose|-v]
```

Gera relatório de auditoria: contagem de eventos, evidências, decisões, commits e PR.

| Argumento | Obrigatório | Descrição |
|-----------|:-----------:|-----------|
| `--task` | não | ID da tarefa |
| `--verbose`, `-v` | não | Exibe timeline completa de eventos |

- **Código de saída**: 0

### 5.7 Sincronização

#### `sync`

```
espaut sync [--task TASK-ID]
```

Verifica o estado de sincronização entre local e remoto, e detecta alterações pendentes de preservação.

- **Código de saída**: 0
- **Saída**: status de sync (`synchronized`, `local_ahead`, `remote_ahead`, `diverged`, `no_remote`) + status de preservação

#### `watch`

```
espaut watch [--task TASK-ID] [--base BRANCH]
```

Verificação única combinada: sync + atualização da branch base + detecção de conflitos de merge + preservação pendente.

| Argumento | Obrigatório | Descrição |
|-----------|:-----------:|-----------|
| `--task` | não | ID da tarefa |
| `--base` | não | Branch base (padrão: `main`) |

- **Código de saída**: 0

---

## 6. Máquinas de Estado

Todas implementadas pelo motor genérico `StateMachine` em `engine.py`, usando tabelas de transição `dict[(StrEnum, str), StrEnum]`.

### 6.1 SM#1 — Tarefa (`task.py`)

12 estados, 25 transições.

#### Estados

| Estado | Descrição |
|--------|-----------|
| `REGISTRADA` | Estado inicial ao criar a tarefa |
| `PREPARADA` | Branch e escopo definidos |
| `EM_EXECUCAO` | Desenvolvimento ativo |
| `PRESERVACAO_PENDENTE` | Alterações detectadas, aguardando preservação |
| `EM_REVISAO` | PR submetido para revisão |
| `EM_CORRECAO` | Correção em andamento após feedback |
| `AGUARDANDO_DECISAO` | Aguardando decisão humana |
| `APTA_PARA_INTEGRACAO` | Todos os critérios atendidos |
| `INTEGRADA` | PR integrado (terminal) |
| `ENCERRADA_SEM_MERGE` | Fechada sem merge (terminal) |
| `BLOQUEADA` | Tarefa bloqueada |
| `INTERROMPIDA` | Tarefa interrompida (terminal, resumível) |

#### Transições

| Estado Origem | Evento | Estado Destino |
|---------------|--------|----------------|
| REGISTRADA | `prepare` | PREPARADA |
| PREPARADA | `start` | EM_EXECUCAO |
| EM_EXECUCAO | `changes_detected` | PRESERVACAO_PENDENTE |
| PRESERVACAO_PENDENTE | `preserved` | EM_EXECUCAO |
| PRESERVACAO_PENDENTE | `submit_review` | EM_REVISAO |
| EM_EXECUCAO | `submit_review` | EM_REVISAO |
| EM_REVISAO | `request_correction` | EM_CORRECAO |
| EM_CORRECAO | `correction_applied` | EM_REVISAO |
| EM_REVISAO | `await_decision` | AGUARDANDO_DECISAO |
| AGUARDANDO_DECISAO | `approve_integration` | APTA_PARA_INTEGRACAO |
| AGUARDANDO_DECISAO | `reject` | EM_CORRECAO |
| APTA_PARA_INTEGRACAO | `merge_confirmed` | INTEGRADA |
| APTA_PARA_INTEGRACAO | `invalidated` | EM_REVISAO |
| EM_REVISAO | `new_changes` | PRESERVACAO_PENDENTE |
| EM_CORRECAO | `new_changes` | PRESERVACAO_PENDENTE |
| EM_REVISAO | `close_without_merge` | ENCERRADA_SEM_MERGE |
| AGUARDANDO_DECISAO | `close_without_merge` | ENCERRADA_SEM_MERGE |
| EM_EXECUCAO | `block` | BLOQUEADA |
| EM_REVISAO | `block` | BLOQUEADA |
| EM_CORRECAO | `block` | BLOQUEADA |
| BLOQUEADA | `unblock` | EM_EXECUCAO |
| EM_EXECUCAO | `interrupt` | INTERROMPIDA |
| EM_REVISAO | `interrupt` | INTERROMPIDA |
| EM_CORRECAO | `interrupt` | INTERROMPIDA |
| INTERROMPIDA | `resume` | EM_EXECUCAO |

#### Fluxo Principal (Happy Path)

```
REGISTRADA ──prepare──▶ PREPARADA ──start──▶ EM_EXECUCAO
    │                                            │
    │                              changes_detected
    │                                            ▼
    │                                   PRESERVACAO_PENDENTE
    │                                            │
    │                                     preserved │ submit_review
    │                                         │     │
    │                                         ▼     ▼
    │                                    EM_EXECUCAO / EM_REVISAO
    │                                                    │
    │                                              await_decision
    │                                                    ▼
    │                                         AGUARDANDO_DECISAO
    │                                                    │
    │                                         approve_integration
    │                                                    ▼
    │                                       APTA_PARA_INTEGRACAO
    │                                                    │
    │                                           merge_confirmed
    │                                                    ▼
    └─────────────────────────────────────────── INTEGRADA
```

### 6.2 SM#2 — Pendência (`review.py`)

8 estados, 11 transições.

#### Estados

| Estado | Descrição |
|--------|-----------|
| `IDENTIFICADA` | Pendência identificada a partir de review/comentário |
| `CLASSIFICADA` | Classificada por severidade |
| `EM_TRATAMENTO` | Sendo tratada pelo desenvolvedor |
| `CORRECAO_APLICADA` | Correção aplicada |
| `AGUARDANDO_VERIFICACAO` | Aguardando verificação do revisor |
| `RESOLVIDA` | Resolvida (terminal) |
| `JUSTIFICADA` | Justificada/dispensada (terminal) |
| `BLOQUEADA` | Bloqueada por impedimento externo |

#### Transições

| Estado Origem | Evento | Estado Destino |
|---------------|--------|----------------|
| IDENTIFICADA | `classify` | CLASSIFICADA |
| CLASSIFICADA | `start_treatment` | EM_TRATAMENTO |
| CLASSIFICADA | `justify` | JUSTIFICADA |
| EM_TRATAMENTO | `apply_fix` | CORRECAO_APLICADA |
| CORRECAO_APLICADA | `await_verify` | AGUARDANDO_VERIFICACAO |
| AGUARDANDO_VERIFICACAO | `resolve` | RESOLVIDA |
| AGUARDANDO_VERIFICACAO | `reject` | EM_TRATAMENTO |
| IDENTIFICADA | `block` | BLOQUEADA |
| CLASSIFICADA | `block` | BLOQUEADA |
| EM_TRATAMENTO | `block` | BLOQUEADA |
| BLOQUEADA | `unblock` | CLASSIFICADA |

### 6.3 SM#3 — Check (`checks.py`)

8 estados, mapeados via normalização de dados do GitHub.

#### Estados

| Estado | Descrição |
|--------|-----------|
| `NAO_CONFIGURADO` | Nenhum check de CI configurado |
| `NAO_OBSERVADO` | Ainda não observado |
| `PENDENTE` | Check em execução |
| `APROVADO` | Check aprovado |
| `REPROVADO` | Check reprovado |
| `CANCELADO` | Check cancelado |
| `IGNORADO` | Check ignorado (skipped) |
| `INDETERMINADO` | Resultado indeterminável |

#### Mapeamento GitHub → CheckState

| Estado/Conclusão GitHub | CheckState |
|--------------------------|------------|
| SUCCESS, neutral | APROVADO |
| FAILURE, startup_failure, timed_out | REPROVADO |
| PENDING, action_required | PENDENTE |
| CANCELLED | CANCELADO |
| SKIPPED | IGNORADO |
| STALE | INDETERMINADO |

#### Agregação

Prioridade: `REPROVADO` > `PENDENTE` > `CANCELADO` > `INDETERMINADO` > `APROVADO`. Se vazio: `NAO_CONFIGURADO`.

### 6.4 SM#4 — Preservação (`preservation.py`)

9 estados, 14 transições.

#### Estados

| Estado | Descrição |
|--------|-----------|
| `LIMPO` | Worktree limpo |
| `MODIFICACAO_DETECTADA` | Alterações detectadas |
| `PREPARACAO_PENDENTE` | Preparando staging |
| `PREPARADA` | Arquivos em staging |
| `COMMITADA_LOCALMENTE` | Commit local criado |
| `PUSH_PENDENTE` | Push pendente |
| `SINCRONIZADA` | Push confirmado, sincronizado com remoto |
| `CONFLITO` | Conflito de merge detectado |
| `FALHA` | Operação falhou |

#### Transições

| Estado Origem | Evento | Estado Destino |
|---------------|--------|----------------|
| LIMPO | `detect` | MODIFICACAO_DETECTADA |
| MODIFICACAO_DETECTADA | `prepare` | PREPARACAO_PENDENTE |
| PREPARACAO_PENDENTE | `stage` | PREPARADA |
| PREPARADA | `commit` | COMMITADA_LOCALMENTE |
| COMMITADA_LOCALMENTE | `push` | PUSH_PENDENTE |
| PUSH_PENDENTE | `push_confirmed` | SINCRONIZADA |
| PUSH_PENDENTE | `push_failed` | COMMITADA_LOCALMENTE |
| SINCRONIZADA | `detect` | MODIFICACAO_DETECTADA |
| PREPARADA | `conflict` | CONFLITO |
| COMMITADA_LOCALMENTE | `conflict` | CONFLITO |
| PUSH_PENDENTE | `conflict` | CONFLITO |
| PREPARACAO_PENDENTE | `fail` | FALHA |
| PREPARADA | `fail` | FALHA |
| COMMITADA_LOCALMENTE | `fail` | FALHA |

#### Fluxo Principal

```
LIMPO ──detect──▶ MODIFICACAO_DETECTADA ──prepare──▶ PREPARACAO_PENDENTE
                                                          │
                                                        stage
                                                          ▼
              SINCRONIZADA ◀──push_confirmed── PUSH_PENDENTE
                   │                               ▲
                 detect                           push
                   ▼                               │
         MODIFICACAO_DETECTADA       COMMITADA_LOCALMENTE
                                           ▲
                                         commit
                                           │
                                       PREPARADA
```

---

## 7. Critérios de Elegibilidade para Merge (C1–C8)

Avaliados por `evaluate_merge_eligibility()` em `governance.py`. Todos devem ser `PASS` para que o veredito seja `APTA_PARA_INTEGRACAO`.

| Critério | Função | O que avalia |
|----------|--------|-------------|
| C1 Preservação | `check_c1_preservation` | Todas as alterações locais commitadas e enviadas |
| C2 Sincronização | `check_c2_sync` | Branch atualizada com o remoto |
| C3 Verificação | `check_c3_verification` | Todos os checks de CI obrigatórios passam |
| C4 Revisão | `check_c4_review` | Pelo menos uma revisão aprovando o PR |
| C5 Pendências | `check_c5_pendencies` | Nenhuma pendência bloqueante não resolvida |
| C6 Aceitação | `check_c6_acceptance` | Critérios de aceitação comprovados |
| C7 Autoridade | `check_c7_authority` | Decisão de merge autorizada |
| C8 Atualidade | `check_c8_currency` | Checks avaliados na revisão corrente (HEAD atual) |

### Fórmula

```
Elegível = C1 ∧ C2 ∧ C3 ∧ C4 ∧ C5 ∧ C6 ∧ C7 ∧ C8
```

Se todos passam: `APTA_PARA_INTEGRACAO`. Caso contrário: `NAO_APTA`.

---

## 8. Invariantes (INV-001 a INV-014)

Predicados em `invariants.py`. Todos retornam `tuple[bool, str]` — `(atendido, detalhe)`.

| ID | Nome | Descrição |
|----|------|-----------|
| INV-001 | Identidade | Não confundir tarefas por nomes similares de branch/título |
| INV-002 | Preservação | Não descartar modificações pré-existentes sem autorização |
| INV-003 | Rastreabilidade | Alterações atribuídas à tarefa têm vínculo verificável |
| INV-004 | Validade de revisão | Check é válido apenas para a revisão a que corresponde |
| INV-005 | Evidência | Declaração de IA não é prova de execução ou sucesso |
| INV-006 | Pendências | Pendência bloqueante aplicável não pode ser omitida do fechamento |
| INV-007 | Conversas | Atualização de código não resolve automaticamente uma conversa |
| INV-008 | Autoridade | Decisões reservadas ao usuário requerem autorização |
| INV-009 | Idempotência | Retomada não deve duplicar efeitos indevidos |
| INV-010 | Recuperabilidade | Operações persistentes deixam referências recuperáveis |
| INV-011 | Segredos | Não encaminhar deliberadamente segredos identificados |
| INV-012 | Fechamento | Sucesso de subteste/check/commit sozinho não aprova a tarefa |
| INV-013 | Atualidade | Mudança de revisão invalida conclusões da revisão anterior |
| INV-014 | Fidelidade | Representações internas preservam referência à fonte original |

---

## 9. Modelo de Segurança

Implementado em `security.py`. Três primitivas:

### 9.1 Validação de Argumentos (`validate_subprocess_args`)

Rejeita qualquer argumento contendo metacaracteres de shell: `` ; & | ` $ ( ) { } ! \n \r ``. Levanta `ValueError` se detectado. Aplicada em `run_git()` e `run_gh()` antes de cada chamada subprocess.

### 9.2 Detecção de Segredos (`contains_secret`)

7 padrões regex para detectar segredos em texto:

| Padrão | O que detecta |
|--------|--------------|
| `ghp_/gho_/ghu_/ghs_/ghr_` + 36-255 chars | Tokens GitHub (PAT clássico) |
| `github_pat_` + 22-255 chars | GitHub PAT (formato novo) |
| `sk-` + 20+ chars | Chaves OpenAI |
| `AIza` + 35 chars | Chaves Google API |
| `AKIA/ASIA` + 16 chars | Chaves AWS |
| `-----BEGIN ... PRIVATE KEY-----` | Chaves privadas (RSA, EC, OPENSSH) |
| `api_key/secret/token/password/credential/auth` + valor | Padrão genérico de credenciais |

### 9.3 Sanitização de Texto (`sanitize_external_text`)

Remove caracteres de controle (< 0x20 ou 0x7F–0x9F) de textos externos (comentários de PR, logs), preservando `\n`, `\r`, `\t` e conteúdo Unicode.

---

## 10. Classificação de Reviews e Pendências

### Classificações (`CommentClassification`)

| Valor | Bloqueante | Descrição |
|-------|:----------:|-----------|
| `DEFEITO_CONFIRMADO` | sim | Defeito confirmado pelo revisor |
| `DEFEITO_POSSIVEL` | sim | Defeito possível/provável |
| `MUDANCA_REQUERIDA` | sim | Mudança explicitamente requerida |
| `IMPEDIMENTO_EXTERNO` | sim | Impedimento fora do escopo do desenvolvedor |
| `SUGESTAO_OPCIONAL` | não | Sugestão opcional de melhoria |
| `PERGUNTA` | não | Pergunta do revisor |
| `INFORMACAO` | não | Comentário informativo |
| `INDETERMINADO` | não | Não foi possível classificar (ambíguo) |

### Heurísticas

- `classify_review()` — mapeia o estado do review GitHub (`APPROVED` → aprovação, `CHANGES_REQUESTED` → mudança requerida)
- `classify_comment()` — analisa o texto do comentário por palavras-chave para classificar

### Ciclo de Correção

```
diagnose ──▶ [desenvolvedor corrige] ──▶ correct --confirm ──▶ verify-correction
   │                                          │                        │
   │                                     preservation              re-query
   │                                     automática              checks/reviews
   ▼                                          ▼                        ▼
DGN-{id}                              commit + push          pendências resolvidas?
```

Limite configurável: `correction_max_attempts` (padrão: 3).

---

## 11. Referência de API por Módulo

### 11.1 `engine.py` — Motor de Máquina de Estados

```python
class TransitionError(Exception)

class StateMachine:
    __init__(name: str, transitions: TransitionTable,
             guards: dict[tuple[StrEnum, str], Guard] | None = None,
             on_transition: Callable | None = None) -> None
    transitions -> TransitionTable                    # property
    valid_events(state: StrEnum) -> list[str]
    can_transition(state: StrEnum, event: str,
                   context: dict[str, Any] | None = None) -> bool
    transition(state: StrEnum, event: str,
               context: dict[str, Any] | None = None) -> StrEnum
```

### 11.2 `store.py` — Persistência

```python
init_store(root: Path) -> Path
find_store(start: Path | None = None) -> Path | None
require_store(start: Path | None = None) -> Path
new_id(prefix: str = "") -> str
read_json(path: Path) -> Any
write_json(path: Path, value: Any) -> None
read_jsonl(path: Path) -> list[dict[str, Any]]
append_jsonl(path: Path, record: dict[str, Any]) -> None
write_jsonl(path: Path, records: list[dict[str, Any]]) -> None
load_config(store: Path) -> dict[str, Any]
```

### 11.3 `events.py` — Log de Eventos e Evidências

```python
make_event(event_type: str, *, task_id: str | None = None,
           execution_id: str | None = None, actor: str = "espaut",
           object_reference: str | None = None,
           old_state: str | None = None, new_state: str | None = None,
           outcome: str | None = None, evidence_id: str | None = None,
           detail: str | None = None) -> dict[str, Any]
emit_event(store: Path, event: dict[str, Any]) -> None
log_event(store: Path, event_type: str, **kwargs) -> dict[str, Any]
make_evidence(source_system: str, source_reference: str,
              observation: str, *, task_id: str | None = None,
              related_revision: str | None = None) -> dict[str, Any]
save_evidence(store: Path, evidence: dict[str, Any]) -> Path
```

### 11.4 `security.py` — Primitivas de Segurança

```python
validate_subprocess_args(args: list[str]) -> list[str]
contains_secret(text: str) -> list[str]
sanitize_external_text(text: str) -> str
```

### 11.5 `git_ops.py` — Wrappers Git

```python
run_git(*args: str, timeout: int = 30, cwd: str | None = None)
    -> subprocess.CompletedProcess[str]
is_git_repo(cwd: str | None = None) -> bool
repo_root(cwd: str | None = None) -> str | None
current_branch(cwd: str | None = None) -> str | None
head_sha(cwd: str | None = None) -> str | None
worktree_status(cwd: str | None = None) -> list[dict[str, str]]
has_changes(cwd: str | None = None) -> bool
staged_diff(cwd: str | None = None) -> str
staged_files(cwd: str | None = None) -> list[str]
stage_files(paths: list[str], cwd: str | None = None)
    -> subprocess.CompletedProcess[str]
create_commit(message: str, cwd: str | None = None)
    -> subprocess.CompletedProcess[str]
push(remote: str = "origin", branch: str | None = None,
     cwd: str | None = None, set_upstream: bool = False)
    -> subprocess.CompletedProcess[str]
remote_head_sha(remote: str = "origin", branch: str | None = None,
                cwd: str | None = None) -> str | None
branch_exists(name: str, cwd: str | None = None) -> bool
create_branch(name: str, start_point: str | None = None,
              cwd: str | None = None) -> subprocess.CompletedProcess[str]
checkout_branch(name: str, cwd: str | None = None)
    -> subprocess.CompletedProcess[str]
is_ref_valid(ref: str, cwd: str | None = None) -> bool
has_incomplete_operation(cwd: str | None = None) -> str | None
```

### 11.6 `gh_ops.py` — Wrappers GitHub CLI

```python
run_gh(*args: str, timeout: int = 60, cwd: str | None = None)
    -> subprocess.CompletedProcess[str]
gh_available() -> bool
pr_list_json(fields: list[str] | None = None, state: str = "open",
             cwd: str | None = None) -> list[dict[str, Any]]
pr_view_json(pr_ref: str | int, fields: list[str] | None = None,
             cwd: str | None = None) -> dict[str, Any] | None
pr_create(title: str, body: str, base: str | None = None,
          head: str | None = None, cwd: str | None = None)
    -> dict[str, Any] | None
pr_checks_json(pr_ref: str | int, cwd: str | None = None)
    -> list[dict[str, Any]]
pr_reviews_json(pr_number: int, cwd: str | None = None)
    -> list[dict[str, Any]]
pr_comments_json(pr_number: int, cwd: str | None = None)
    -> list[dict[str, Any]]
pr_review_comments_json(pr_number: int, cwd: str | None = None)
    -> list[dict[str, Any]]
pr_merge(pr_ref: str | int, method: str = "merge",
         cwd: str | None = None) -> subprocess.CompletedProcess[str]
```

### 11.7 `task.py` — Entidade Tarefa + SM#1

```python
class TaskState(StrEnum)  # 12 valores (ver seção 6.1)
TASK_TRANSITIONS: dict    # 25 transições
build_task_machine(on_transition: Any = None) -> StateMachine
make_task(task_id: str, repository_id: str, title: str,
          *, objective: str = "",
          acceptance_criteria: list[str] | None = None,
          authorized_scope: list[str] | None = None) -> dict[str, Any]
```

### 11.8 `preservation.py` — Preservação + SM#4

```python
class PreservationState(StrEnum)  # 9 valores (ver seção 6.4)
PRESERVATION_TRANSITIONS: dict   # 14 transições
build_preservation_machine(on_transition: Any = None) -> StateMachine
classify_changes(status_entries: list[dict[str, str]],
                 eligible_patterns: list[str]) -> tuple[list[str], list[str]]
detect_changes(store: Path, task_id: str,
               cwd: str | None = None) -> dict[str, Any]
stage_eligible(store: Path, task_id: str, eligible_paths: list[str],
               cwd: str | None = None) -> dict[str, Any]
commit_staged(store: Path, task_id: str, message: str,
              cwd: str | None = None) -> dict[str, Any]
push_and_verify(store: Path, task_id: str, remote: str = "origin",
                branch: str | None = None,
                cwd: str | None = None) -> dict[str, Any]
run_preservation(store: Path, task_id: str, message: str,
                 *, dry_run: bool = True,
                 cwd: str | None = None) -> dict[str, Any]
```

### 11.9 `pullrequest.py` — Ciclo de Vida do PR

```python
find_existing_pr(task: dict[str, Any],
                 cwd: str | None = None) -> dict[str, Any] | None
create_or_reuse_pr(store: Path, task: dict[str, Any], title: str,
                   body: str, base: str | None = None,
                   cwd: str | None = None) -> dict[str, Any]
query_pr_state(pr_number: int,
               cwd: str | None = None) -> dict[str, Any]
reconcile_pr_state(store: Path, task: dict[str, Any],
                   cwd: str | None = None) -> dict[str, Any]
update_task_pr(task: dict[str, Any], pr_number: int,
               url: str | None = None,
               head_sha: str | None = None) -> dict[str, Any]
```

### 11.10 `checks.py` — Monitoramento CI + SM#3

```python
class CheckState(StrEnum)    # 8 valores (ver seção 6.3)
GH_STATE_MAP: dict           # Mapeamento GitHub → CheckState
normalize_check_state(raw: dict[str, Any]) -> CheckState
make_check_record(raw: dict[str, Any], *, pr_number: int,
                  evaluated_revision: str | None = None) -> dict[str, Any]
query_checks(store: Path, task_id: str, pr_number: int,
             evaluated_revision: str | None = None,
             cwd: str | None = None) -> dict[str, Any]
compute_aggregate(checks: list[dict[str, Any]]) -> CheckState
```

### 11.11 `review.py` — Reviews/Pendências + SM#2

```python
class PendencyState(StrEnum)       # 8 valores (ver seção 6.2)
class CommentClassification(StrEnum)  # 8 valores (ver seção 10)
PENDENCY_TRANSITIONS: dict         # 11 transições
BLOCKING_CLASSIFICATIONS: set      # 4 classificações bloqueantes
build_pendency_machine(on_transition: Any = None) -> StateMachine
classify_review(review: dict[str, Any]) -> CommentClassification
classify_comment(comment: dict[str, Any]) -> CommentClassification
make_pendency(origin_type: str, origin_reference: str,
              description: str, classification: CommentClassification,
              *, task_id: str, pr_number: int | None = None,
              author: str | None = None,
              related_file: str | None = None,
              related_line: int | None = None) -> dict[str, Any]
collect_reviews(store: Path, task_id: str, pr_number: int,
                cwd: str | None = None) -> dict[str, Any]
extract_pendencies(review_report: dict[str, Any],
                   *, task_id: str) -> list[dict[str, Any]]
has_blocking_pendencies(pendencies: list[dict[str, Any]]) -> bool
```

### 11.12 `governance.py` — Governança + Elegibilidade

```python
make_decision(task_id: str, decision_type: str, authority: str,
              value: str, *, scope: str = "",
              evidence_reference: str | None = None) -> dict[str, Any]
record_decision(store: Path, decision: dict[str, Any]) -> Path
evaluate_criterion(name: str, passed: bool, detail: str) -> dict[str, Any]
check_c1_preservation(task: dict, cwd: str | None = None) -> dict
check_c2_sync(task: dict, cwd: str | None = None) -> dict
check_c3_verification(checks_report: dict) -> dict
check_c4_review(reviews_report: dict) -> dict
check_c5_pendencies(pendencies: list[dict]) -> dict
check_c6_acceptance(task: dict) -> dict
check_c7_authority(task: dict, decisions: list[dict]) -> dict
check_c8_currency(checks_report: dict, current_head: str | None) -> dict
evaluate_merge_eligibility(store: Path, task: dict,
    checks_report: dict, reviews_report: dict,
    pendencies: list[dict], decisions: list[dict],
    cwd: str | None = None) -> dict[str, Any]
```

### 11.13 `invariants.py` — Predicados INV-001 a INV-014

Todas as funções retornam `tuple[bool, str]`:

```python
inv_001_identity(task: dict, other_tasks: list[dict])
inv_002_preservation(changes_eligible: list[str], changes_committed: list[str])
inv_003_traceability(task: dict)
inv_004_revision_validity(check_revision: str | None, current_revision: str | None)
inv_005_evidence(claim: str, evidence: dict | None)
inv_006_pendencies(pendencies: list[dict])
inv_007_conversations(threads: list[dict])
inv_008_authority(operation: str, required_permission: str, granted_permissions: set[str])
inv_009_idempotency(operation_id: str, completed_operations: set[str])
inv_010_recoverability(operation: dict)
inv_011_secrets(content: str)
inv_012_closure(subtests_passed: bool, checks_passed: bool, criteria_met: bool)
inv_013_currency(evaluated_revision: str | None, current_revision: str | None)
inv_014_fidelity(record: dict)
```

### 11.14 `correction.py` — Ciclo de Correção

```python
make_diagnosis(pendency_id: str, suspected_cause: str,
               *, evidence_references: list[str] | None = None,
               proposed_intervention: str = "",
               scope_impact: list[str] | None = None,
               uncertainties: str = "",
               source: str = "human") -> dict[str, Any]
make_attempt(pendency_id: str, attempt_number: int,
             *, input_revision: str | None = None,
             proposed_changes: list[str] | None = None) -> dict[str, Any]
can_attempt_correction(store: Path, pendency_id: str,
                       previous_attempts: list[dict]) -> tuple[bool, str]
record_attempt_result(attempt: dict, *, applied_changes: list[str],
                      output_revision: str | None = None,
                      validation_result: str | None = None,
                      state: str = "CONCLUIDA") -> dict[str, Any]
run_correction_check(store: Path, task_id: str, pendency_id: str,
                     previous_attempts: list[dict]) -> dict[str, Any]
check_scope_compliance(proposed_files: list[str],
                       authorized_scope: list[str]) -> tuple[bool, list[str]]
```

### 11.15 `recovery.py` — Recuperação de Sessão

```python
recover_task_state(store: Path, task: dict,
                   cwd: str | None = None) -> dict[str, Any]
reconstruct_timeline(store: Path, task_id: str) -> list[dict[str, Any]]
find_last_checkpoint(store: Path, task_id: str) -> dict[str, Any] | None
audit_task(store: Path, task: dict,
           cwd: str | None = None) -> dict[str, Any]
check_idempotency(store: Path, task_id: str, operation_type: str,
                  operation_reference: str) -> tuple[bool, str]
```

### 11.16 `triggers.py` — Triggers e Sincronização

```python
check_sync_state(store: Path, task_id: str, remote: str = "origin",
                 branch: str | None = None,
                 cwd: str | None = None) -> dict[str, Any]
check_base_branch_updated(store: Path, task_id: str,
                          base_branch: str,
                          last_known_base_sha: str | None = None,
                          remote: str = "origin",
                          cwd: str | None = None) -> dict[str, Any]
check_merge_conflict(task_id: str, base_branch: str,
                     cwd: str | None = None) -> dict[str, Any]
detect_pending_preservation(store: Path, task_id: str,
                            cwd: str | None = None) -> dict[str, Any]
```

---

## 12. Configuração e Decisões Pendentes

10 decisões humanas com padrões conservadores que desbloqueiam o progresso:

| ID | Decisão | Padrão | Chave | Opções |
|----|---------|--------|-------|--------|
| DEC-001 | Mecanismo de disparo | Explícito via CLI | `trigger_mode` | `explicit`, `hook`, `watch` |
| DEC-002 | Momento da preservação | Sob comando explícito | `preservation_events` | Lista de eventos |
| DEC-003 | Critérios de elegibilidade de arquivos | Todos os não-ignorados | `eligible_patterns` | Padrões fnmatch |
| DEC-004 | Integração com IA | Desabilitada | `ai_enabled` | `true`, `false` |
| DEC-005 | Autorização de alteração automática | Requer `--confirm` | `auto_commit` | `true`, `false` |
| DEC-006 | Resolução de conversas | Autor + revisores atribuídos | `resolver_roles` | Lista de papéis |
| DEC-007 | Política de merge | Apenas manual | `merge_policy` | `manual`, `semi_auto`, `auto` |
| DEC-008 | Limite de correções | 3 tentativas, sem limite de tempo | `correction_max_attempts` | Inteiro ≥ 1 |
| DEC-009 | Retenção de registros | Reter tudo | `retention_policy` | `retain_all`, `retain_recent`, `archive` |
| DEC-010 | Tarefas sem CI | `NAO_CONFIGURADO`, não bloqueia | `ci_required` | `true`, `false` |

Para alterar, edite `.espaut/config.json` diretamente.

---

## 13. Testes

### Visão Geral

- **Total**: 303 checks passando em 15 arquivos de teste
- **Padrão**: funções `test_*()` retornando `dict[str, str]` onde valor `"PASS"` indica sucesso
- **Infraestrutura**: repositórios git temporários reais para testes de integração; `unittest.mock.patch` para operações GitHub

### Execução

```bash
# Todos os testes
for f in tests/espaut/test_*.py; do python3 "$f"; done

# Teste individual
python3 tests/espaut/test_engine.py
```

### Cobertura por Arquivo

| Arquivo de Teste | Módulo Testado | Checks |
|------------------|---------------|-------:|
| `test_engine.py` | `engine.py` | 11 |
| `test_store.py` | `store.py` | 23 |
| `test_events.py` | `events.py` | 19 |
| `test_security.py` | `security.py` | 17 |
| `test_git_ops.py` | `git_ops.py` | 19 |
| `test_task.py` | `task.py` | 19 |
| `test_preservation.py` | `preservation.py` | 18 |
| `test_pullrequest.py` | `pullrequest.py` | 16 |
| `test_checks.py` | `checks.py` | 21 |
| `test_review.py` | `review.py` | 30 |
| `test_governance.py` | `governance.py` + `invariants.py` | 44 |
| `test_correction.py` | `correction.py` | 16 |
| `test_recovery.py` | `recovery.py` | 13 |
| `test_triggers.py` | `triggers.py` | 7 |
| `test_cli.py` | `cli.py` | 30 |
| **Total** | | **303** |

---

## 14. Schemas JSON

Três schemas em `schemas/`, seguindo JSON Schema Draft 2020-12 com URN `$id` e títulos em português.

| Schema | `$id` | Entidade | Módulo Produtor |
|--------|-------|----------|-----------------|
| `espaut-task.schema.json` | `urn:cepraea:esp-aut-git-001:espaut-task:0.1.0` | Registro de tarefa | `task.py` → `make_task()` |
| `espaut-event.schema.json` | `urn:cepraea:esp-aut-git-001:espaut-event:0.1.0` | Registro de evento | `events.py` → `make_event()` |
| `espaut-config.schema.json` | `urn:cepraea:esp-aut-git-001:espaut-config:0.1.0` | Configuração local | `store.py` → `DEFAULT_CONFIG` |

### Convenções

- `"additionalProperties": false` em todos os objetos
- `"const"` para campos com valor fixo (ex.: `schema_version`)
- `"enum"` com valores em português para estados
- `"type": ["string", "null"]` para campos anuláveis
- `"pattern"` para validação de formato de IDs
- `"format": "date-time"` para timestamps ISO 8601
