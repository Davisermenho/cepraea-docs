# Runtime estável da ESPAUT

A ESPAUT usa um dispatcher global único para Claude Code e Codex. O código
ativo fica em releases imutáveis sob `~/.local/share/espaut-runtime/versions/`;
o caminho `current` é trocado atomicamente e não aponta para clones temporários.

O instalador Python:

- exige um checkout Git limpo no SHA informado;
- executa a suíte antes da ativação;
- gera e verifica hashes SHA-256 dos arquivos da release;
- preserva configurações e hooks de terceiros;
- substitui somente handlers ESPAUT antigos;
- mantém backup das configurações e a release anterior para rollback.

Os hooks de projeto foram removidos desta versão porque Codex e Claude carregam
as camadas global e local cumulativamente. O dispatcher global mantém projetos
desconhecidos em modo monitor e só executa Git/GitHub quando existe uma política
`.espaut/config.json` explícita, uma única tarefa ativa e uma branch não
protegida.

Comandos administrativos (executados pelo agente, não pelo usuário final):

```text
python3 -B -m espaut.runtime --runtime-root CAMINHO deploy \
  --source CHECKOUT_LIMPO --implementation-sha SHA \
  --claude-settings ~/.claude/settings.json \
  --codex-hooks ~/.codex/hooks.json

python3 -B -m espaut.runtime --runtime-root CAMINHO status
python3 -B -m espaut.runtime --runtime-root CAMINHO rollback
```

Cada evento registra provedor, sessão, worktree, hook, versão, SHA da
implementação, política e resultado em `state/events.jsonl`, sem armazenar o
texto do prompt ou credenciais.

Depois de comprovar o dispatcher global, a função Python
`decommission_project_hook_config` remove somente handlers ESPAUT locais e
guarda a configuração original em `backups/project-hook-configs/`. Hooks de
terceiros e demais chaves permanecem intactos.
