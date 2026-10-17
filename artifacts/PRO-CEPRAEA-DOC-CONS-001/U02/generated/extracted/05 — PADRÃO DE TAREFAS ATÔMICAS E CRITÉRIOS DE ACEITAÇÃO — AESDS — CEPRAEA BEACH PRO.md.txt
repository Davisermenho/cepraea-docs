# PADRÃO DE TAREFAS ATÔMICAS E CRITÉRIOS DE ACEITAÇÃO — CEPRAEA BEACH PRO

**AESDS 05 — Fundação v0.1**

---

## 1. OBJETIVO

Definir a menor unidade de trabalho suficientemente explícita para que um agente implemente sem inventar requisito, alterar escopo ou depender de conversa extensa fora da tarefa.

---

## 2. PRINCÍPIO

Uma tarefa atômica deve possuir uma saída verificável e pequena o suficiente para permitir revisão integral do diff e dos critérios. “Implementar módulo X” normalmente é grande demais.

---

## 3. TEMPLATE CANÔNICO DE TASK

- ID
- Título
- Objetivo
- Ator
- Contexto válido
- Pré-condições
- Dependências
- Fonte normativa
- Entrada/contratos
- Comportamento esperado
- Estados relevantes
- Ações permitidas
- Ações proibidas
- Edge cases incluídos
- Fora de escopo
- Arquivos esperados ou área de escrita
- Decisões humanas já tomadas
- Decisões humanas pendentes
- Autonomia técnica permitida
- Stop conditions
- Critérios de aceitação
- Checks obrigatórios
- Evidência esperada
- Definição de DONE

---

## 4. REGRA DE TAMANHO

A tarefa deve ser dividida quando:

- possui mais de um resultado independente;
- mistura decisão de produto com execução;
- exige vários fluxos de usuário distintos;
- não cabe em um diff revisável integralmente;
- depende de duas decisões humanas não relacionadas;
- possui critérios que podem passar/falhar independentemente e não compartilham a mesma unidade funcional.

Não dividir artificialmente um fluxo simples em microtarefas que criem handoff sem valor.

---

## 5. CRITÉRIOS COMPORTAMENTAIS — BDD

Use Given/When/Then quando o critério descreve comportamento observável.

**Exemplo:**

- **Given*- uma solicitação de disponibilidade aberta
- **And*- a atleta ainda não respondeu
- **When*- ela abre o treino
- **Then*- a interface exibe “Não respondida”
- **And** não representa o estado como resposta “Não”.

---

## 6. RESTRIÇÕES — MUST / MUST NOT

Use requisitos declarativos quando não houver benefício em cenário BDD.

- **MUST:** preservar dados preenchidos após erro recuperável.
- **MUST NOT:** exibir UUID interno à atleta sem requisito explícito.
- **MUST NOT:** preencher presença automaticamente a partir de disponibilidade.

---

## 7. QUALIDADE MENSURÁVEL

Critérios de performance, acessibilidade ou cobertura precisam de métrica/condição objetiva quando aplicável. Evitar “rápido”, “bonito”, “intuitivo”, “moderno” sem definição verificável.

---

## 8. CLASSIFICAÇÃO DE CRITÉRIO

- **CRITICAL:** falha viola segurança, autorização, integridade de domínio ou requisito essencial.
- **MUST:** obrigatório para DONE.
- **SHOULD:** esperado, mas pode admitir exceção documentada e aprovada.
- **OPTIONAL:** melhoria não bloqueante e explicitamente fora do caminho crítico.

---

## 9. ORÁCULO DE ACEITAÇÃO

Cada critério deve indicar, direta ou indiretamente, como será provado: teste automatizado, typecheck, build, inspeção de contrato, runtime, acessibilidade, dispositivo real ou validação humana.

Critério sem mecanismo de prova deve ser refinado antes de implementação quando a ambiguidade puder alterar o resultado.

---

## 10. EXEMPLO DE TASK ATÔMICA

```text
ID: FE-AVAIL-003
Fonte normativa do exemplo: DEC-DATA-046 para prazo, fechamento, editabilidade e reabertura; demais contratos upstream continuam aplicáveis.
Objetivo: implementar seleção da resposta da própria atleta.
Ator: atleta.
Entrada: status UNANSWERED | YES | NO | UNCERTAIN + solicitação com `deadline_at` explícito + condição temporal da coleta. Não presumir prazo global.
Comportamento: apresentar prazo e opções permitidas; refletir resposta atual; permitir criação/alteração da própria declaração enquanto a coleta estiver aberta e antes do deadline; persistir somente por ação explícita e versionada; após o deadline, bloquear o self-service normal e exibir prazo encerrado sem converter UNANSWERED em NO nem apagar a última resposta válida; reabertura antes do início da sessão somente por ato autorizado/auditável.
MUST NOT: tratar UNANSWERED como NO; editar resposta de outra atleta; transformar resposta em presença.
Estados de interação: IDLE, DIRTY, SUBMITTING, SUCCESS, ERROR. O fechamento por deadline é condição temporal da solicitação/coleta, não semântica de “resposta expirada”; a nomenclatura executável concreta deve vir do contrato do repositório.
Checks: testes comportamentais relevantes + validação da aplicação.
DONE: todos os MUST PASS e nenhum finding alto aberto.

```

---

## 11. STOP CONDITIONS DO EXECUTOR

Parar somente a parte afetada se descobrir: decisão material ausente; contrato incompatível; fonte canônica conflitante; dependência nova material; necessidade de ampliar escopo; comportamento não especificado que altera o produto.

---

## 12. REGRA PARA REFERÊNCIAS

Se a task exige escolha visual ou técnica ainda não homologada, não embutir a escolha como implementação. Criar um ponto de decisão com as opções obtidas segundo o AESDS 08.

---

## 13. META DE PRIMEIRA REVISÃO

As tasks devem ser especificadas em granularidade suficiente para buscar $\ge 90\%$ de critérios PASS na primeira revisão independente. Se uma classe de task falhar repetidamente, corrigir o template/contexto antes de aumentar governança.

---

## 14. INSTANCIAÇÃO DE TASKS DO MVP — PLANOS / SPECS

Este documento continua sendo o padrão das tasks; ele não passa a manter uma lista paralela de tarefas, status ou progresso. Instâncias executáveis devem ser criadas no sistema oficial Git/GitHub somente após grounding do repositório e quando a unidade correspondente satisfizer o critério READY do AESDS 04.

### 14.1. DERIVAÇÃO OBRIGATÓRIA DA TASK

Toda task MVP deve derivar explicitamente de:

Requisito `SR-*` -> entregável `DEL-*` -> fluxo/contrato aplicável no AESDS 02/03 -> task -> critério -> prova AESDS 06.

A task deve citar somente as fontes necessárias à sua unidade e não repetir integralmente o contrato upstream.

### 14.2. FRONTEIRAS CANDIDATAS DE TASK

As seguintes fronteiras são candidatas de decomposição, não IDs/status oficiais:

- resolver e apresentar identidade de domínio + vínculo vigente;
- consultar sessão e representar corretamente planejado vs realizado;
- consultar resposta corrente de disponibilidade;
- submeter resposta própria de disponibilidade;
- derivar cobertura a partir de respostas vigentes;
- criar draft, publicar, revisar/revalidar por nova versão, cancelar e encerrar Plano de Participação da Sessão conforme DEC-DATA-047/SGATE-0025, somente após grounding dos contratos executáveis aplicáveis;
- consultar presença factual de sessão realizada;
- confirmar/corrigir presença factual por ator autorizado;
 projetar workspace da atleta a partir de fontes já existentes;
- projetar workspace do treinador distinguindo fato, planejamento, derivação e pendência;
- integrar estados de erro/conectividade sem persistência offline não autorizada;
- verificar autorização negativa, invariantes de domínio e runtime mobile.

### 14.3. ESTADOS DECISÓRIOS QUE DEVEM APARECER NA TASK QUANDO APLICÁVEIS

- `DECIDED-AVAIL-01` — prazo, fechamento, editabilidade e reabertura são governados por DEC-DATA-046; a task deve consumir essa decisão por referência e não criar default temporal concorrente. Grounding técnico ainda é necessário para mecanismos concretos.
- `DECIDED-PLAN-01` — identidade/lifecycle do Plano de Participação da Sessão são governados por DEC-DATA-047/SGATE-0025. Tasks devem consumir por referência: `DRAFT` $\to$ `PUBLISHED` $\to$ `SUPERSEDED` | `CANCELLED` | `CLOSED`; no máximo uma `PUBLISHED` vigente; `PUBLISHED` imutável; revisão/revalidação material cria nova versão; `SOURCE_ALIGNMENT CONSISTENT` | `REVIEW_REQUIRED` é ortogonal e mudança material dos inputs não pode reescrever automaticamente a composição. A task não deve inventar nomes de endpoint, storage, schema ou mecanismo físico antes do grounding; `BLOCKED-DATA-01` continua prevalecendo sobre qualquer persistência física.
- `OPEN-UX-01` bloqueia task que precise fixar navegação/IA material.
- `OPEN-VIS-01` bloqueia task que precise fixar direção visual/tokens finais.
- `OPEN-A11Y-01` bloqueia critério que dependa do nível formal WCAG; requisitos básicos de semântica/acessibilidade já decididos continuam válidos.
- `OPEN-REPO-01` bloqueia afirmação sobre arquivos, comandos, stack real ou contratos físicos não inspecionados.
- `BLOCKED-DATA-01` bloqueia qualquer task de SQL/schema/migration/modelo físico enquanto o gate não for liberado.

### 14.4. REGRA PARA NÃO INVENTAR WRITE SCOPE

Enquanto `OPEN-REPO-01` existir, o campo “Arquivos esperados ou área de escrita” deve permanecer a ser resolvido pelo grounding do repositório, não por nomes de pastas inferidos do AESDS. Após grounding, a task deve registrar write scope concreto e revisável antes de READY.

### 14.5. PRIMEIRA SLICE

A primeira slice executável deve ser a menor unidade relevante cuja semântica esteja decidida, cujo contrato possa ser groundado no repositório e que não dependa de `OPEN` material. Não selecionar automaticamente disponibilidade apenas porque há exemplo `FE-AVAIL-003` neste documento: após `DEC-DATA-046`, o exemplo pode consumir a política temporal ratificada, mas continua sendo exemplo e não constitui status oficial de task. `READY` ainda depende do grounding do repositório, dos contratos concretos e dos demais blockers aplicáveis.
