ÍNDICE DE RUNBOOKS E ESTADO OPERACIONAL — CEPRAEA BEACH PRO

AESDS 09 — Fundação v0.1

1. OBJETIVO

Dar ao agente uma rota curta para executar procedimentos repetíveis e descobrir o estado atual do projeto sem criar uma segunda state machine ou manter snapshots concorrentes no Google Drive.

2. PRINCÍPIO

TASK + REPO STATE + RUNBOOK APLICÁVEL -> EXECUÇÃO.

Runbook explica COMO executar procedimento. Git/GitHub informa O QUE está vigente e qual trabalho está em curso. Este documento apenas roteia.

3. AUTORIDADE DO ESTADO

O estado operacional deve permanecer em Git/GitHub. O issue de preparação orientada ao MVP prevê GitHub Project como fonte oficial do estado das tarefas e CURRENT_STATE.md como resumo conciso quando implementado.

Enquanto essa transição não estiver materializada, o agente deve usar a task/issue corrente, branch/commit e estado observável do repositório. Não inferir que um documento do Drive é mais atual que Git.

4. PROIBIÇÃO DE ESTADO PARALELO

Não criar por padrão:

- STATE.md paralelo ao Git;

- log obrigatório por agente;

- pasta de approvals;

- registro de review duplicado;

- planilha manual de status que concorra com GitHub.

Criar artefato persistente somente quando ele possuir valor próprio além do estado já representado em Git/GitHub.

5. FUNÇÃO DOS RUNBOOKS

Runbook serve para procedimento repetível com passos, pré-condições, comandos, resultado esperado, diagnóstico de falha e recuperação.

Exemplos de categoria:

- iniciar ambiente local;

- validar aplicação;

- resetar banco sintético;

- executar migrations;

- testar RLS/autorização;

- executar suíte de testes;

- gerar build;

- verificar PWA;

- investigar falha de integração;

- validar runtime mobile;

- preparar evidência para review.

6. TEMPLATE DE RUNBOOK

Título

Objetivo

Quando usar

Quando NÃO usar

Pré-condições

Entradas

Procedimento passo a passo

Comandos exatos quando estáveis

Resultado esperado

Falhas conhecidas

Diagnóstico

Recuperação/rollback

Evidência produzida

Stop conditions

Referências

7. REGRA DE CARREGAMENTO

O agente lê apenas o runbook ligado à task atual. Não carregar todos os runbooks no contexto.

8. RUNBOOKS EXISTENTES

Priorizar o diretório runbooks/ e documentação operacional já existente no repositório. Antes de criar novo runbook, procurar procedimento equivalente e atualizá-lo quando apropriado.

9. CURRENT STATE — CAMPOS MÍNIMOS

Quando a fonte oficial de estado possuir resumo, ele deve permitir descobrir:

- fase atual;

- última tarefa concluída;

- tarefas READY;

- tarefa em execução;

- blockers;

- decisões humanas pendentes;

- branch/commit relevante;

- próxima ação.

10. REGRA DE FRESCOR

Informação de estado sem vínculo com Git/GitHub deve ser tratada como potencialmente obsoleta. Documentos conceituais não devem declarar branch atual ou próxima tarefa como verdade permanente.

11. HANDOFF ENTRE SESSÕES

Um agente novo deve conseguir iniciar lendo: política -> CURRENT_STATE/issue atual -> task -> fontes citadas -> runbook aplicável. Não reconstruir o projeto pelo histórico de chats.

12. RELAÇÃO COM O AESDS 04

AESDS 04 define dependências e regra do grafo. Git/GitHub armazena status concreto. AESDS 09 explica como localizar o estado e executar procedimentos; não duplica o grafo.

13. DONE DO ROTEADOR

Este documento está correto quando aponta para as fontes vigentes sem copiar seu conteúdo volátil e quando cada procedimento repetitivo material possui um runbook localizável ou uma instrução explícita de criação.