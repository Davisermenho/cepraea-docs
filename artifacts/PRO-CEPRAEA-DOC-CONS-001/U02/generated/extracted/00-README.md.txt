# Beach Handball PWA — Kit de Engenharia Assistida por IA

Este kit organiza o trabalho com o ChatGPT como um processo de engenharia rastreável, em vez de uma sequência de prompts isolados.

## Objetivo

Aumentar a probabilidade de que requisitos, drivers e decisões arquiteturais correspondam ao contexto real do produto, reduzindo:

- respostas genéricas;
- arquitetura prematura;
- hipóteses tratadas como fatos;
- perda de significado entre intenção e implementação;
- decisões sem justificativa contextual;
- mudanças que quebram premissas antigas sem serem percebidas.

## Princípio central

O ChatGPT é um mecanismo de:
- elicitação;
- análise;
- síntese;
- crítica;
- comparação;
- geração de alternativas;
- validação.

Os **artefatos canônicos** são a fonte de verdade do projeto.

## Ordem recomendada

1. Configure as Instruções do Projeto com `01-PROJECT-INSTRUCTIONS.md`.
2. Abra o chat `00 — Intake e objetivos`.
3. Consolide `02-PROJECT-CHARTER.md`.
4. Faça elicitação no chat `01 — Elicitação`.
5. Atualize continuamente `03-SHARED-UNDERSTANDING.md`.
6. Execute o Gate de Entendimento.
7. Modele requisitos em `04-REQUIREMENTS.md`.
8. Execute o Gate de Requisitos.
9. Identifique drivers em `05-ARCHITECTURE-DRIVERS.md`.
10. Compare alternativas arquiteturais.
11. Registre decisões em `06-ADR-TEMPLATE.md`.
12. Mantenha o grafo em `07-TRACEABILITY.md`.
13. Valide usando `08-READINESS-AND-VALIDATION-GATES.md`.
14. Use `09-CHAT-OPENING-PROMPTS.md` para abrir chats especializados.
15. Quando houver mudança relevante, faça análise de impacto antes de alterar arquitetura.

## Fluxo principal

Intenção
→ Elicitação
→ Interpretação explícita
→ Confirmação humana
→ Entendimento compartilhado
→ Readiness Gate
→ Requisitos
→ Drivers arquiteturais
→ Alternativas
→ Decisões
→ Arquitetura
→ Validação
→ Realinhamento
→ Análise de impacto
→ novo ciclo

## Regra de autoridade

1. Decisão explícita do humano.
2. Artefatos canônicos confirmados.
3. Evidência externa confiável e aplicável.
4. Inferência da IA.
5. Memória/contexto de chats anteriores.

A IA nunca deve sobrescrever silenciosamente um item de maior autoridade com um de menor autoridade.

## Regra de proveniência

Use estas marcas quando necessário:

- `USR` — declaração direta do usuário.
- `CTX` — derivado do contexto confirmado.
- `REQ` — derivado de requisito.
- `DRV` — derivado de driver arquitetural.
- `CON` — derivado de restrição.
- `STD` — padrão ou prática conhecida.
- `GEN` — recomendação genérica da IA.
- `EXT` — evidência externa.
- `INF` — inferência da IA.

Uma decisão importante não deve ser aceita apenas com proveniência `GEN`, `STD` ou `INF`.

## Convenção de IDs

- `OBJ-001` — objetivo
- `SUCCESS-001` — critério de sucesso
- `ACT-001` — ator
- `CONCEPT-001` — conceito de domínio
- `RULE-001` — regra de negócio
- `CONST-001` — restrição
- `HYP-001` — hipótese
- `AMB-001` — ambiguidade
- `Q-001` — questão em aberto
- `RISK-001` — risco
- `FR-001` — requisito funcional
- `NFR-001` — requisito não funcional
- `DRV-001` — driver arquitetural
- `OPT-001` — alternativa arquitetural
- `ADR-001` — decisão arquitetural
- `VAL-001` — cenário de validação

## Definição de "informação suficiente"

Não significa que não existem mais perguntas.

Significa:

> Temos conhecimento suficiente para tomar a próxima classe de decisões com risco explícito e aceitável.

Uma questão aberta bloqueia avanço quando combina, em geral:

- alto impacto; e
- alta incerteza; e
- baixa reversibilidade ou alto custo de erro.

## Política de atualização

Nunca apague silenciosamente conhecimento confirmado.

Quando algo mudar:

1. marque o item anterior como `substituído`, `invalidado` ou `obsoleto`;
2. registre a nova informação;
3. atualize a rastreabilidade;
4. identifique requisitos impactados;
5. identifique drivers impactados;
6. identifique ADRs impactados;
7. identifique validações que precisam ser repetidas.
