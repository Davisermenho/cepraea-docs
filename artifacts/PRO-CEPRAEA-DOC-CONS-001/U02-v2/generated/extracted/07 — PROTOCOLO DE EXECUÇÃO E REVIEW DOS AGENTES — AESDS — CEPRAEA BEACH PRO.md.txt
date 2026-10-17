PROTOCOLO DE EXECUÇÃO E REVIEW DOS AGENTES — CEPRAEA BEACH PRO

AESDS 07 — Fundação v0.1

1. OBJETIVO

Permitir desenvolvimento solo assistido por Codex e Claude Code no VS Code, sem depender de API paga, mantendo separação simples entre execução, verificação e decisão humana.

2. PAPÉIS

DAVI — autoridade de produto/domínio e decisão final.

EXECUTOR — agente que implementa a task atual.

REVIEWER — agente independente que revisa task, diff, testes e evidências sem corrigir silenciosamente.

MÁQUINA — lint, typecheck, testes, build e outros checks executáveis.

3. FLUXO PADRÃO

Davi define/seleciona task -> Executor lê contexto mínimo -> resolve apenas decisões técnicas permitidas -> implementa -> autoverifica -> checks determinísticos -> Reviewer tenta refutar -> Executor corrige findings -> Davi aceita/promove quando aplicável.

4. REGRA DE CONTEXTO

Ler somente o necessário:

1. política operacional vigente;

2. task;

3. fontes normativas citadas;

4. arquivos relacionados;

5. testes relacionados.

Não carregar todo o histórico do projeto por padrão.

5. AUTONOMIA DO EXECUTOR

Pode decidir: decomposição local, helpers, nomes internos, refatoração pequena, estratégia de teste compatível, reutilização evidente e outros detalhes reversíveis sem impacto material.

Não pode decidir silenciosamente: regra de domínio, UX material, arquitetura nova, dependência relevante, autorização, persistência, política de dados, informação visível, identidade visual ou alteração de escopo.

6. DECISÃO PENDENTE

Quando necessária, o Executor não abandona toda a task se existir trabalho independente seguro. Deve isolar o bloqueio, produzir opções conforme AESDS 08 e avançar somente nas partes não dependentes da decisão.

7. PREFLIGHT PROPORCIONAL

Antes da escrita, confirmar:

- branch/contexto permitido pela política vigente;

- task READY;

- fontes disponíveis;

- escopo previsível;

- dados sintéticos quando exigido;

- ausência de segredo/credencial indevida.

Não criar formulário de governança, manifesto, certificado ou gate novo para mudanças comuns.

8. EXECUÇÃO

- inspecionar antes de editar;

- reutilizar padrões existentes antes de criar novos;

- fazer mudança mínima suficiente;

- não corrigir itens adjacentes sem relação material;

- atualizar testes junto com comportamento;

- manter diff compreensível;

- não converter hipótese em decisão.

9. AUTOVERIFICAÇÃO DO EXECUTOR

Executar checks aplicáveis e corrigir falhas introduzidas. Relatar claramente o que foi e não foi executado. Nunca inventar resultado de comando.

10. HANDOFF PARA REVIEW

Entregar ao Reviewer:

- task e critérios;

- diff integral;

- testes/checks e resultados;

- fontes relevantes;

- decisões tomadas pelo humano;

- decisões técnicas locais tomadas pelo executor;

- limitações/riscos residuais.

11. REVIEWER INDEPENDENTE

O Reviewer deve procurar razões concretas pelas quais a solução está errada. Verificar:

- todos os critérios;

- regressões;

- inferência não autorizada;

- expansão de escopo;

- semântica do domínio;

- autorização/privacidade;

- estados impossíveis;

- erro/recuperação;

- teste que não prova o que afirma;

- abstração ou dependência desnecessária.

12. VERDICT

PASS: todos os critérios obrigatórios satisfeitos e evidência suficiente.

FAIL: existe critério obrigatório não satisfeito ou finding bloqueante.

HUMAN_DECISION_REQUIRED: somente quando a correção depende de decisão humana material não existente.

13. FINDING

Todo finding deve conter: problema, evidência, impacto, critério/regra afetado e correção requerida. Evitar recomendações cosméticas não vinculadas à task.

14. REGRA DE 90%

A primeira revisão independente mede quantos critérios o Executor acertou sem ciclo de correção. A meta >=90% é usada para melhorar especificação, contexto e decomposição. Não aumentar governança automaticamente quando a taxa cair; primeiro identificar a causa dominante.

15. CAUSAS DE FALHA A CLASSIFICAR

SPEC_GAP — tarefa ambígua/incompleta.

CONTEXT_GAP — fonte necessária não carregada.

IMPLEMENTATION_ERROR — agente errou apesar da especificação suficiente.

TEST_GAP — prova insuficiente.

HUMAN_DECISION_MISSING — decisão material não existente.

ENVIRONMENT_BLOCK — ambiente impediu prova.

16. PRINCÍPIO DE ECONOMIA

O protocolo deve custar menos que o erro que pretende evitar. Rigor cresce com impacto em domínio, dados, auth, privacidade, dependências, infraestrutura e irreversibilidade.

17. DONE

A task termina quando critérios obrigatórios estão PASS, checks exigidos foram executados, findings bloqueantes foram resolvidos, o diff permanece no escopo e a fonte oficial de estado registra a conclusão.