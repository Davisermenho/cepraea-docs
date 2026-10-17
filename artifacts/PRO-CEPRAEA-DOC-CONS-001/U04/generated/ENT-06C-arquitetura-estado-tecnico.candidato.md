# ENT-06C — Arquitetura e estado técnico (candidato)

Status: `CANDIDATO_NAO_APROVADO`  
Unidade: `U04`  
Publicação oficial autorizada: `NÃO`

## Critérios e decisão ainda aberta

A arquitetura deve privilegiar simplicidade operacional, manutenção por uma pessoa e reuso do código existente. Nem Next.js/Vercel nem React/Vite está aprovado como arquitetura definitiva.

## Comparação sustentada pela inspeção

| Alternativa | Evidência atual | Reuso | Limite demonstrado |
| --- | --- | --- | --- |
| React/Vite/PWA | Observada no commit `73462b6098dc89bc00fa55bea5f6f26980889173` | Alto, porque é a base existente | Não executada localmente nesta atividade; custo e implantação não verificados |
| Next.js | Não observado como base do commit inspecionado | Exigiria mudança cuja necessidade não foi demonstrada | Sem evidência suficiente para selecionar ou estimar custo de migração |
| Vercel | `vercel.json` e URL declarada existem | Compatível com a base observada | Configuração não comprova implantação nem aprovação definitiva |
| Supabase | Projeto `fcnyjmrknqaomamdzabt` existe com estado `INACTIVE` | Cliente e configuração local observados | Banco e migrações não verificados por timeout |

A inspeção favorece o reuso de React/Vite como alternativa de menor mudança, mas isso é uma recomendação candidata, não escolha arquitetural aprovada. A decisão depende de custo atual e verificação executável.

## Estado técnico demonstrável

- Arquivos selecionados do repositório: `VALIDADO_ESTATICAMENTE`, limitado ao conteúdo observado no commit.
- Execução local do produto: não demonstrada nesta atividade.
- Projeto Supabase: existência observada; prontidão e esquema não verificados. O estado `INACTIVE` impede alegar `VERIFICADO_NO_ALVO`.
- Nenhuma implantação, migração ou alteração de produção foi executada.

## Rastreabilidade

Decisões humanas: `DEC-U04-003`, `DEC-U04-004`. Evidências: `OBS-U04-REPO-001`, `OBS-U04-SUPABASE-001`; U03 `CLM-U03-0018` a `CLM-U03-0021` e `CLM-U03-0010` a `CLM-U03-0013`. Afirmações: `STM-U04-011` a `STM-U04-014`.
