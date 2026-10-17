**Guia do Modelo ANMS (Specification-Driven Develop…**

# Guia do Modelo ANMS (Specification-Driven Development)

O modelo **ANMS** funciona como um *template de especificação sofisticado*, projetado para otimizar a colaboração entre desenvolvedores humanos e ferramentas de inteligência artificial no contexto do **Desenvolvimento Guiado por Especificação (SDD — Specification-Driven Development)**.

Ao utilizar metodologias estruturadas como **EARS** para requisitos e **Gherkin** para testes, o sistema estabelece uma linguagem padronizada que organiza o escopo do projeto sob os princípios da **Clean Architecture**. Essa abordagem transforma prompts iniciais em diretrizes técnicas precisas que podem ser lidas e executadas sem ambiguidades por modelos de linguagem (LLMs, como Claude Code, Cursor ou Windsurf).

O objetivo final dessa estrutura é atuar como um sistema de segurança contra o *"quality collapse"* (a degradação da qualidade do código gerado por IA ao longo do tempo em projetos extensos), garantindo que o código gerado permaneça íntegro e funcional.

## Visão Geral e Definições

-   **Definição:** Modelo de especificação (spec template) projetado especificamente para o desenvolvimento guiado por inteligência artificial (AI-driven development).
-   **Objetivo:** Padronizar a definição de requisitos por humanos para que modelos de linguagem (LLMs) possam interpretá-los e executá-los com clareza e sem ambiguidades.
-   **Contexto de Uso (SDD):** Utilizado no Desenvolvimento Guiado por Especificação, onde o prompt inicial é transformado em uma especificação estruturada antes da geração de código, prevenindo a degradação da qualidade do software em projetos de longa duração.

## Links e Referências

Para mais detalhes e artigos sobre o modelo ANMS no DEV.to, consulte:

-   Artigo sobre criação de software a partir de um memorando de 5 linhas: [AI turned my 5-line memo into specs and software in 45 minutes](https://dev.to/goodrelax/ai-turned-my-5-line-memo-into-specs-and-software-in-45-minutes-1l95)
-   Artigo detalhando o modelo de especificação criado para IA: [A spec template built for AI](https://dev.to/goodrelax/a-spec-template-built-for-ai-3bkp)
-   Perfil do autor no DEV.to: [goodrelax no DEV.to](https://dev.to/goodrelax)

**Estrutura das Camadas**

O ANMS organiza o escopo do projeto alinhando notações específicas aos princípios da **Clean Architecture**:

| **Camada / Foco** | **Notação Utilizada** | **Finalidade** |
| --- | --- | --- |
| **Requisitos** | EARS (Easy Approach to Requirements Syntax) | Definir regras comportamentais com clareza |
| --- | --- | --- |
| **Arquitetura** | Mermaid.js | Desenhar fluxos e diagramas visuais |
| --- | --- | --- |
| **Critérios de Aceitação** | Gherkin (Given/When/Then) | Validar testes funcionais |
| --- | --- | --- |

## Nota sobre Ambiguidade do Termo

**Nota:** Em outros contextos de TI, a sigla ANMS pode referir-se ao *Asynchronous Network Management System* (da NASA-AMMOS). Contudo, no âmbito da plataforma DEV.to, refere-se estritamente ao template de especificação para IA descrito neste guia.

# Mapa de Navegação das Fontes

[Um Modelo de Especificação para a Era do Desenvolvimento de Software Guiado por IA](?tab=t.0#heading=h.df9l6p2t843c)

Guia do Modelo ANMS (Specification-Driven Development) → Você está aqui

[Relatório de Pesquisa: Padrões Sintáticos do EARS](?tab=t.c9d5v1li2i3h)

[Sessões Claude Code e Codex](?tab=t.7uylqawh7wm5)

[Guia de Fontes e Introdução ao EARS](?tab=t.fysxtsu3meds)

[claudecode-rules.md](?tab=t.8gg0j8f3wd99)