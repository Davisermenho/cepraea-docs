# Mem0 Policy — `/home/davis/elic`

```yaml
artifact_id: MEM0-POLICY
version: 1.0
STATUS: RASCUNHO_FOR_WORKSPACE_GOVERNANCE
effective_from: 2026-09-03
authority: HUMAN_EXPLICIT
scope: CODEX_PERSISTENT_MEMORY_LAYER
project_scope:
  user: davis
  project: elic
```

## 1. Papel

Mem0 é uma camada auxiliar de memória persistente para o Codex. Ele pode recuperar entre sessões resumos, decisões, padrões e aprendizados relevantes, mas NÃO é:

- fonte canônica do projeto;
- treinamento do modelo;
- substituto do repositório;
- substituto de `AGENTS.md`, `AGENT_ELI.md` ou `governance/PRODUCT-QUALITY-GUARDRAILS.md`;
- registro de aprovação humana;
- prova de currentness, teste, Gate ou validação;
- fila de tarefas, histórico operacional ou handoff.

Memória recuperada é um **indício para localizar contexto**, não autoridade suficiente para uma conclusão material.

## 2. Escopo observado

A configuração operacional informada para este workspace é:

```text
user=davis
project=elic
global_search=false
```

A instalação do Mem0 é global no ambiente Codex, mas as memórias são separadas por projeto. Outros agentes do VS Code, inclusive Claude Code, NÃO devem ser presumidos como consumidores automáticos dessas memórias.

Esta política não copia nem versiona `~/.mem0/settings.json`, `~/.mem0/project_map.json`, credenciais, hooks ou configuração global do Codex. Esses itens permanecem externos ao repositório.

## 3. Autoridade

Mem0 NUNCA supera:

1. instrução humana explícita e atual;
2. políticas vigentes do workspace;
3. decisão humana vigente registrada no repositório;
4. fonte canônica aplicável e sua linhagem/currentness;
5. evidência primária verificável.

Se uma memória contradizer qualquer item acima, a memória deve ser tratada como `STALE_OR_CONFLICTING_MEMORY` e NÃO pode sustentar ação material.

`MEMORY_FOUND` não significa `CURRENT`, `CANONICAL`, `APPROVED`, `VALIDATED` nem `TRUE`.

## 4. Regra de re-grounding

Antes de usar uma memória para:

- formular ou evitar uma pergunta de elicitação;
- afirmar decisão de produto;
- alterar Requirement;
- determinar Gate/currentness;
- recomendar arquitetura;
- alterar código, teste ou documentação normativa;
- produzir handoff material;

o agente DEVE reabrir a fonte primária no workspace e verificar:

```text
path/ID
status
versão/linhagem
escopo
supersession
propagação pendente
Gate aplicável
```

Se a fonte não puder ser localizada ou revalidada, classificar o conteúdo como:

```text
MEMORY_UNVERIFIED
```

Nesse estado, ele pode orientar busca adicional, mas não pode ser promovido a fato ou decisão.

## 5. O que PODE ser lembrado

Quando não houver dado sensível e existir valor persistente entre sessões, Mem0 pode receber resumos concisos de:

- convenções estáveis de trabalho dos agentes;
- decisões humanas já confirmadas, preferencialmente com `decision_id` e path da fonte;
- padrões técnicos observados e validados que sejam reutilizáveis;
- soluções de erro já verificadas, com comando/arquivo de origem quando útil;
- preferências operacionais não sensíveis do usuário;
- pointers para fontes, runbooks, artefatos e caminhos relevantes;
- resumo de sessão estritamente necessário para retomada, sem substituir o estado do repositório.

Uma memória material deve preferir a forma:

```text
FACT/DECISION/PATTERN
source=<path|ID>
status=<confirmed|validated|pointer>
captured_at=<timestamp quando disponível>
revalidate_on_use=true
summary=<resumo mínimo>
```

Não copiar documentos inteiros quando um pointer e um resumo bastam.

## 6. O que NÃO DEVE ser lembrado

Não persistir no Mem0:

- senhas, tokens, cookies, chaves de API, secrets, códigos de recuperação ou credenciais;
- conteúdo de `.env`, keychains ou arquivos equivalentes;
- dados pessoais de atletas, contatos, endereços ou identificadores privados;
- wellness, saúde, condição física, avaliações médicas ou informação pessoal sensível;
- disponibilidade, presença, participação ou justificativas individualizadas de atletas;
- conversas completas, transcrições extensas ou dumps de contexto;
- logs brutos, traces extensos, diffs completos ou saídas temporárias;
- conteúdo inteiro de arquivos canônicos;
- propostas não aprovadas como se fossem decisões;
- hipóteses, inferências ou recomendações como se fossem fatos;
- estado transitório de task, fila, checklist operacional ou handoff como única cópia;
- Gate/currentness efêmero sem pointer para a fonte e revalidação obrigatória;
- qualquer conteúdo cuja persistência externa não seja necessária para o trabalho.

## 7. Auto-save e resumos de sessão

Como o ambiente possui salvamento automático, o agente principal DEVE evitar colocar conteúdo proibido em resumos destinados à persistência.

Antes de resumir uma sessão para memória:

1. remover secrets e dados pessoais;
2. remover conteúdo temporário já representado no Git/repositório;
3. separar decisão humana de inferência;
4. preferir pointer + resumo mínimo;
5. marcar necessidade de revalidação quando o item puder mudar;
6. não salvar uma nova memória apenas porque a informação apareceu na conversa.

O fato de hooks poderem salvar automaticamente não transforma todo conteúdo da sessão em memória apropriada.

## 8. Subagentes

Não desenhar o workflow supondo que subagentes persistirão memória. O comportamento informado para este ambiente impede salvamento de sessão por subagentes.

Subagentes podem usar contexto herdado ou ferramentas disponíveis, mas qualquer conclusão material deve retornar ao agente principal e ser grounded nas fontes normativas antes de persistência ou ação.

## 9. Claude ↔ Codex

Claude Code não recebe Mem0 automaticamente. Portanto:

```text
MEM0_ONLY_INFORMATION
!=
SHARED_AGENT_CONTEXT
```

Qualquer informação necessária para Claude, Codex, revisor ou sessão futura deve existir em um destes meios apropriados:

- fonte canônica do repositório;
- registro de decisão/proposta devidamente classificado;
- evidência verificável;
- handoff transitório com pointers para fontes primárias.

Nunca usar Mem0 como canal oculto para transferir decisão entre agentes.

## 10. Handoff e Mem0

Se Mem0 ajudou a localizar informação usada em um handoff, o handoff deve citar a **fonte primária revalidada**, não a memória como autoridade.

Se não houver fonte primária recuperável, declarar:

```text
memory_dependency = UNVERIFIED
```

E a informação dependente não pode ser apresentada como fato vigente.

## 11. Currentness

Memórias podem envelhecer. Para qualquer item sujeito a mudança:

```text
RETRIEVED_MEMORY
→ locate primary source
→ currentness check
→ supersession check
→ pending propagation check
→ only then use
```

Quando uma memória estiver comprovadamente desatualizada, corrigir ou excluir a memória quando a ferramenta disponível permitir, sem alterar silenciosamente a fonte canônica.

## 12. Relação com BYOS e custo

Mem0 é um serviço externo persistente e não é automaticamente proibido pela política BYOS, porque a restrição central não é “não usar APIs”.

Entretanto, seu uso econômico deve ser classificado separadamente conforme `governance/BYOS-ECONOMIC-CONSTRAINT.md`.

Enquanto o custo incremental do serviço não estiver demonstrado neste workspace, classificar novas dependências ou expansão de uso do Mem0 como:

```text
CONDICIONAL — CUSTO_EXTERNO_NAO_VERIFICADO
```

Não confundir a existência de uma API key do serviço com violação automática. Também não afirmar custo zero sem evidência.

## 13. Regra central

> Mem0 pode ajudar o agente a lembrar **onde procurar** e **o que pode ser relevante**. A verdade operacional e semântica continua no humano, nas políticas vigentes, nas fontes canônicas e nas evidências verificáveis do workspace.
