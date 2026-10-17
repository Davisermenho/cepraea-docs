**claudecode-rules.md**

# claudecode-rules.md

# .claudecode / .cursorrules — REGRAS PERSISTENTES PARA AGENTES DE IDE

Especificação Governança: Modelo ANMS & Clean Architecture

## 1. DIRETRIZES DE ARQUITETURA E ESTRUTURA (CLEAN ARCHITECTURE + STFB)

```yaml

architecture_rules:

framework: "Clean Architecture (Robert C. Martin)"

hierarchy_principle: "STFB (Stable Top, Flexible Bottom)"

layers:

layer_1_entities:

path: "src/entities/"

description: "Regras de negócio corporativas e Value Objects puros."

constraints:

- "PROIBIDO importar qualquer framework (Express, TypeORM, Prisma, etc.) ou bibliotecas externas."

- "Validações de invariantes devem ocorrer na construção dos Value Objects/Entities."

layer_2_usecases:

path: "src/usecases/"

description: "Regras de negócio da aplicação e orquestração de fluxos."

constraints:

- "Depender APENAS de interfaces abstratas de repositórios/serviços (injeção de dependência)."

- "PROIBIDO acoplar com detalhes de banco de dados ou protocolo HTTP."

layer_3_adapters:

path: "src/adapters/"

subdirectories:

- "src/adapters/controllers/"

- "src/adapters/repositories/"

- "src/adapters/presenters/"

constraints:

- "Controllers validam DTOs de entrada e traduzem retornos para respostas HTTP padronizadas."

- "Repositories implementam as interfaces abstratas da Camada 2."

layer_4_framework:

path: "src/framework/"

subdirectories:

- "src/framework/http/"

- "src/framework/database/"

constraints:

- "Contém os drivers, servidores (Express/FastAPI/NestJS) e instâncias de banco de dados."

2. PADRÃO DE REQUISITOS (EARS SYNTAX - EASY APPROACH TO REQUIREMENTS SYNTAX)

ears_requirements_rules:

keywords_rfc_2119:

- "SHALL / MUST: Obrigatório"

- "SHOULD: Recomendado"

- "MAY: Opcional"

patterns:

ubiquitous:

syntax: "O <sistema> deve <ação>."

use_case: "Requisitos contínuos / invariantes globais."

event_driven:

syntax: "QUANDO <gatilho>, o <sistema> deve <ação>."

use_case: "Respostas a eventos ou chamadas de API."

state_driven:

syntax: "ENQUANTO <estado>, o <sistema> deve <ação>."

use_case: "Comportamento ativado por estado específico."

optional_feature:

syntax: "ONDE <Recurso Incluído>, o <sistema> deve <ação>."

use_case: "Recursos opcionais ou condicionais de infraestrutura."

unwanted_behaviour:

syntax: "SE <condição indesejada>, ENTÃO o <sistema> deve <ação>."

use_case: "Tratamento de exceções, erros e falhas de validação."

complex:

syntax: "QUANDO <gatilho>, ENQUANTO <estado>, o <sistema> deve <ação>."

use_case: "Condições compostas."

3. CONVENÇÃO DE DIAGRAMAS MERMAID.JS (CAPÍTULO 3 ARCHITECTURE)

mermaid_rules:

color_coding_required: true

layer_styles:

entity: "fill:#f8cecc,stroke:#b85450,stroke-width:2px,color:#000;"

usecase: "fill:#fff2cc,stroke:#d6b656,stroke-width:2px,color:#000;"

adapter: "fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px,color:#000;"

framework: "fill:#d5e8d4,stroke:#82b366,stroke-width:2px,color:#000;"

dependency_direction: "Todas as setas de dependência de código DEVEM apontar para dentro (em direção às Entities/UseCases)."

4. CONVENÇÃO DE TESTES E RASTREABILIDADE (GHERKIN / BDD)

gherkin_rules:

traceability_tag: "@REQ-EARS-XXX"

structure:

- "Dado [contexto inicial / estado preexistente]"

- "Quando [ação realizada / requisição HTTP enviada]"

- "Então [código de status e estado esperado]"

- "E [efeito colateral ou invariante estrita]"

constraint: "Todo cenário Gherkin no Capítulo 4 DEVE ter rastreabilidade direta com o ID do requisito EARS do Capítulo 2."

5. DIRETRIZES DE CÓDIGO E QUALIDADE

coding_standards:

typing: "Tipagem estrita obrigatória (sem uso de any em TypeScript ou tipos dinâmicos não anotados em Python)."

error_handling: "Tratamento explícito de exceções de domínio; proibições de engolir exceções (catch em branco)."

step_by_step_execution:

- "Construir 1 camada por vez."

- "Não tentar implementar o projeto inteiro em uma única resposta."

- "Seguir a ordem: Entities -> UseCases -> Adapters -> Framework -> Integration Tests."



# Mapa de Navegação das Fontes

[Um Modelo de Especificação para a Era do Desenvolvimento de Software Guiado por IA](?tab=t.0#heading=h.df9l6p2t843c)

[Guia do Modelo ANMS (Specification-Driven Development)](?tab=t.j2x06nwefqq5)

[Relatório de Pesquisa: Padrões Sintáticos do EARS](?tab=t.c9d5v1li2i3h)

[Sessões Claude Code e Codex](?tab=t.7uylqawh7wm5)

[Guia de Fontes e Introdução ao EARS](?tab=t.fysxtsu3meds)

claudecode-rules.md → Você está aqui