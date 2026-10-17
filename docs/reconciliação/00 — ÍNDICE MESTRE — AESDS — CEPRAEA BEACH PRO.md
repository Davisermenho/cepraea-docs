# ÍNDICE MESTRE — AESDS — CEPRAEA BEACH PRO

Agent-Executable Software Development Specification

1. **OBJETIVO**
    - Este sistema documental existe para permitir que um desenvolvedor solo conduza a construção completa do frontend/PWA do CEPRAEA BEACH PRO com Codex e Claude Code como agentes de pesquisa, execução e revisão, reduzindo ao mínimo decisões implícitas, inferências não autorizadas, retrabalho e erros detectáveis.
    - A documentação não torna LLMs infalíveis. Ela reduz o espaço de decisão do agente, torna dependências explícitas e cria oráculos verificáveis de correção.
2. **META DE QUALIDADE**
    - Meta de eficácia dos agentes: >= 90% dos critérios de aceitação mensuráveis devem obter PASS na primeira revisão independente da implementação concluída.
    - Taxa de atendimento de primeira revisão = critérios PASS / (critérios PASS + critérios FAIL) x 100.
    - Critérios BLOCKED não entram no denominador, mas impedem DONE enquanto permanecerem bloqueados. Para conclusão de uma tarefa, 100% dos critérios MUST/CRITICAL devem estar PASS, nenhum finding CRITICAL/HIGH pode permanecer aberto e nenhuma evidência obrigatória pode estar ausente.
    - A meta de 90% é objetivo de engenharia e métrica de processo, não garantia de desempenho de LLM.
3. **PRINCÍPIO DE AUTORIDADE**
    - Davi decide: domínio, produto, comportamento observável, UX material, direção visual, adoção de dependências relevantes, mudanças arquiteturais e promoção.
    - Os agentes podem: pesquisar, comparar referências, decompor tarefas, implementar decisões já tomadas, decidir detalhes técnicos locais e reversíveis, executar testes e revisar evidências.
    - Os agentes não podem: inventar regra de domínio, escolher silenciosamente entre alternativas materiais, transformar referência em autoridade, alterar escopo para facilitar implementação ou declarar aprovação humana.
4. **REGRA PARA DECISÃO AUSENTE**
    - Se faltar decisão material, o agente deve apresentar opções com fonte, evidência, trade-offs, aplicabilidade ao CEPRAEA e recomendação identificada como recomendação. O agente só interrompe por decisão material; detalhes locais, reversíveis e sem impacto semântico podem ser resolvidos autonomamente.
5. **ARQUITETURA FÍSICA DO AESDS**
    - 00 — Índice Mestre
        Roteia autoridades, métricas, sequência de leitura e relação entre documentos.
    - 01 — Contrato de Produto e Domínio
        Consolida constituição do produto, requisitos, invariantes, autoridade e limites. Não substitui o Modelo Canônico; referencia-o.
    - 02 — Especificação de Experiência e Interação
        Define UX, IA, fluxos, estados, transições, componentes semânticos, mobile, acessibilidade e decisões de design.
    - 03 — Arquitetura Técnica e Contratos do Frontend
        Define arquitetura React/TypeScript/PWA, fronteiras de camada, integração, contratos de dados/API e padrões técnicos.
    - 04 — Roadmap de Implementação e Grafo de Tarefas
        Define ordem de execução, dependências, fases, bloqueios e caminho crítico para evitar retrabalho.
    - 05 — Padrão de Tarefas Atômicas e Critérios de Aceitação
Define a unidade de trabalho que Codex/Claude Code recebem e o formato de BDD/MUST/MUST NOT.
    - 06 — Especificação de Testes e Verificação
        Mapeia requisito -> prova -> comando -> resultado PASS/FAIL e estabelece evidência mínima.
    - 07 — Protocolo de Execução e Review dos Agentes
        Define Claude Code/Codex, handoff, autonomia, stop conditions e revisão independente proporcional ao risco.
    - 08 — Catálogo de Referências e Protocolo de Pesquisa
        Define como buscar documentação oficial, padrões, exemplos visuais e repositórios open source sem cargo cult.
    - 09 — Índice de Runbooks e Estado Operacional
        Roteia procedimentos executáveis e a fonte vigente do estado do projeto sem criar state machine paralela.
6. **MAPEAMENTO DAS 19 CAMADAS CONCEITUAIS**
    - Product Constitution -> 01
    - Canonical Domain Model -> fonte canônica existente + 01
    - Product Requirements -> 01
    - System Architecture -> 03
    - Data & API Contracts -> 03 + fontes executáveis do repo
    - UX / Interaction Specification -> 02
    - Design System Specification -> 02
    - State & Transition Model -> 02
    - Security / Authorization / Privacy -> 01 + 03
    - Engineering Standards -> 03Implementation Roadmap -> 04
    - Task Graph -> 04
    - Atomic Task Specifications -> 05
    - Acceptance Criteria -> 05
    - Test & Verification Specification -> 06Agent Execution Protocol -> 07
    - Review Protocol -> 07
    - Runbooks -> 09
    - Reference Catalog -> 08
    - Current Project State -> Git/GitHub + 09 como roteador, nunca espelho concorrente
7. **FONTES EXISTENTES A REUTILIZAR**
    - README — MODELAGEM CANÔNICA — CEPRAEA BEACH PRO: índice da modelagem canônica existente.
    - Modelagem de Domínio — Frontend CEPRAEA BEACH PRO: fonte de conteúdo para UX/UI/frontend a ser normalizada dentro do documento 02.
    - FLUXO COMPLETO DE DESENVOLVIMENTO — CEPRAEA BEACH PRO: referência para sequência geral e dependências.
    - Glossário de Dados — CEPRAEA v0.1 e artefatos de dados: fontes para contratos, nunca duplicados manualmente no frontend.
    - Manual de implantação segura — Codex e Claude Code no CEPRAEA BEACH PRO: referência para controles já existentes.
    - AGENT_POLICY.md, AGENTS.md e CLAUDE.md do repositório: política operacional vigente dos agentes.
8. **ORDEM DE LEITURA PARA AGENTE EXECUTOR**
    1. política operacional vigente do repositório;
    2. tarefa atômica atual;
    3. 01 somente nas seções citadas pela tarefa;
    4. 02 e/ou 03 conforme o tipo da tarefa;
    5. contratos executáveis diretamente relacionados;
    6. 06 para provas exigidas;
    7. 09 somente se houver procedimento/runbook aplicável.
        O agente não deve carregar todo o acervo por padrão. Contexto mínimo suficiente reduz ruído e conflito.
9. **ORDEM DE LEITURA PARA REVIEWER**
    1. tarefa e critérios de aceitação;
    2. diff completo;
    3. evidências produzidas;
    4. fontes normativas diretamente citadas;
    5. testes relevantes;
    6. riscos e stop conditions aplicáveis.
10. **REGRA DE DONE DO SISTEMA DOCUMENTAL**
    Um documento AESDS só é considerado operacional quando contém: objetivo, autoridade, escopo, entradas, saídas, decisões humanas, autonomia permitida, stop conditions, critérios de conclusão e relação com fontes executáveis.

Este índice é a porta de entrada. Nenhum documento subordinado pode criar uma autoridade concorrente às fontes canônicas ou ao estado registrado em Git/GitHub.
