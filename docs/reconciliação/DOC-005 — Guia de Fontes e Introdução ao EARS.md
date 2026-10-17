**Guia de Fontes e Introdução ao EARS**

Guia de Fontes e Introdução ao EARS

O **Easy Approach to Requirements Syntax (EARS)** é um método estruturado para a redação de requisitos de sistemas em linguagem natural, garantindo clareza e precisão. A metodologia utiliza um conjunto limitado de palavras-chave e padrões de frases para reduzir ambiguidades e vaguezas, sem a complexidade de linguagens formais.

A estrutura do EARS organiza-se em cinco padrões principais que definem gatilhos e respostas do sistema:

-   **Ubíquo:** Requisitos que estão sempre ativos no sistema.
-   **Baseado em Eventos:** Respostas disparadas por um gatilho específico.
-   **Baseado em Estado:** Comportamentos ativos enquanto uma condição for verdadeira.
-   **Recurso Opcional:** Requisitos aplicáveis apenas a certas variações do sistema.
-   **Comportamento Indesejado:** Respostas do sistema a situações de erro ou falha.

Além do valor acadêmico e histórico, o EARS destaca-se na aplicação prática do **Desenvolvimento Orientado por Especificações (SDD)** e em ferramentas de inteligência artificial generativa (como o *Amazon Kiro*), convertendo intenções humanas em código testável e sem erros.

# Easy Approach to Requirements Syntax (EARS)

O **Easy Approach to Requirements Syntax (EARS)** é um método estruturado para redação de requisitos em linguagem natural utilizando um conjunto reduzido de palavras-chave e padrões de frases. Desenvolvido por Alistair Mavin e seus colegas na *Rolls-Royce plc* durante a análise de regulamentos para sistemas de controle de motores aeronáuticos, o EARS foi apresentado na conferência IEEE RE'09 em 2009.

O método impõe uma ordem de cláusulas consistente e um vocabulário restrito de palavras-chave estruturais, reduzindo ou eliminando problemas comuns como **ambiguidade**, **vagueza** e **incompletude**. Adotado por empresas como Airbus, Bosch, Honeywell, Intel, NASA e Siemens, o EARS também foi integrado a ferramentas de desenvolvimento guiado por IA, como o **Amazon Kiro IDE**.

## 1. Contexto (Background)

Requisitos de sistema são comumente escritos em linguagem natural não restrita, o que propaga erros para as fases de design, implementação e testes. O EARS ocupa um meio-termo ideal: mantém a linguagem natural acessível para todas as partes interessadas sem necessidade de treinamento especializado em linguagens formais, enquanto impõe estrutura sintática suficiente para eliminar defeitos.

## 2. Sintaxe e Padrões de Requisitos

A estrutura geral de um requisito no formato EARS segue a seguinte ordenação temporal:

**ENQUANTO <pré-condição>, QUANDO <gatilho>, O <nome do sistema> DEVE <resposta>**

Regras fundamentais de composição:

1.  Zero ou várias pré-condições;
2.  Zero ou um gatilho (trigger);
3.  Exatamente um nome de sistema;
4.  Uma ou mais respostas do sistema.

### Padrões Principais

| **Padrão** | **Palavras-chave** | **Estrutura Sintática** | **Exemplo Prático** |
| --- | --- | --- | --- |
| **Ubíquo** | DEVE (SHALL) | O <sistema> DEVE <resposta> | O celular DEVE ter massa inferior a 150g. |
| --- | --- | --- | --- |
| **Baseado em Eventos** | QUANDO (WHEN) | QUANDO <evento>, O <sistema> DEVE <resposta> | QUANDO 'mudar' for selecionado, o notebook DEVE silenciar o áudio. |
| --- | --- | --- | --- |
| **Baseado em Estado** | ENQUANTO (WHILE) | ENQUANTO <estado>, O <sistema> DEVE <resposta> | ENQUANTO não houver cartão no caixa eletrônico, o sistema DEVE exibir mensagem inicial. |
| --- | --- | --- | --- |
| **Recurso Opcional** | ONDE (WHERE) | ONDE <recurso>, O <sistema> DEVE <resposta> | ONDE o carro possuir teto solar, o painel DEVE conter o botão de controle. |
| --- | --- | --- | --- |
| **Comportamento Indesejado** | SE... ENTÃO (IF... THEN) | SE <falha>, ENTÃO O <sistema> DEVE <resposta> | SE um cartão inválido for digitado, ENTÃO o site DEVE solicitar a redigitação. |
| --- | --- | --- | --- |

### Requisitos Complexos

Os padrões podem ser combinados para cenários avançados:

*"ENQUANTO a aeronave estiver no solo, QUANDO o empuxo reverso for comandado, o sistema de controle do motor DEVE ativar o reverso."*

## 3. Benefícios e Limitações

### Benefícios:

-   **Redução da Ambiguidade:** Torna explícitos gatilhos, pré-condições e respostas esperadas.
-   **Baixa Barreira de Adoção:** Vocabulário simples sem necessidade de ferramentas complexas.
-   **Acessibilidade Linguística:** Eficiente para autores que não possuem o inglês como primeira língua.
-   **Melhoria na Testabilidade:** Facilita a criação direta de casos de teste derivados.

### Limitações:

-   Não recomendado para requisitos com mais de três pré-condições simultâneas (torna a leitura complexa).
-   Requisitos não-funcionais (como restrições arquiteturais) são mais bem representados por fórmulas, tabelas de decisão ou diagramas.

## 4. Uso no Desenvolvimento Orientado por Especificações (SDD)

No fluxo de trabalho do **Spec-Driven Development (SDD)**, especificações estruturadas direcionam a geração de código, testes e documentação. A sintaxe EARS conecta a intenção do produto a especificações legíveis por Modelos de Linguagem (LLMs).

### Fluxo no Amazon Kiro IDE

O Kiro adota a sintaxe EARS em um fluxo estruturado em 3 etapas:

1.  **1. Requisitos (requirements.md):** O desenvolvedor insere o prompt de intenção e o Kiro expande em Histórias de Usuário com critérios de aceitação em sintaxe EARS.
2.  **2. Design (design.md):** Geração de documentos técnicos, diagramas de sequência e decisões da pilha tecnológica.
3.  **3. Tarefas (tasks.md):** Decomposição do design em tarefas sequenciadas com critérios de teste claros e rastreabilidade de dependências.

## 5. Comparação com Outras Abordagens

| **Método** | **Formato** | **Uso Principal** | **Diferença para o EARS** |
| --- | --- | --- | --- |
| **EARS** | Linguagem natural com palavras-chave | Requisitos de sistemas/software | Padrões leves baseados em palavras-chave sintáticas. |
| --- | --- | --- | --- |
| **User Story** | Como [papel], eu quero [algo], para [benefício] | Descrição de funcionalidades ágeis | Foco no valor ao usuário; sem restrições sintáticas nos critérios de aceitação. |
| --- | --- | --- | --- |
| **Gherkin (BDD)** | Dado / Quando / Então | Cenários de testes executáveis | Orientado a cenários de teste, não a requisitos de sistema. |
| --- | --- | --- | --- |

## 6. Fontes e Links Relevantes

-   **Página Oficial do EARS (Alistair Mavin):** [https://www.eartraining.com](https://www.eartraining.com)
-   **Artigo Científico Original no IEEE Xplore:** [https://doi.org/10.1109/RE.2009.9](https://doi.org/10.1109/RE.2009.9)
-   **Documentação do Amazon Kiro IDE:** [https://kiro.dev/docs/specs](https://kiro.dev/docs/specs)

**Guia Definitivo da QRA Corp sobre EARS:** [https://qracorp.com/ears-guide](https://qracorp.com/ears-guide)

# Mapa de Navegação das Fontes

[Um Modelo de Especificação para a Era do Desenvolvimento de Software Guiado por IA](?tab=t.0#heading=h.df9l6p2t843c)

[Guia do Modelo ANMS (Specification-Driven Development)](?tab=t.j2x06nwefqq5)

[Relatório de Pesquisa: Padrões Sintáticos do EARS](?tab=t.c9d5v1li2i3h)

[Sessões Claude Code e Codex](?tab=t.7uylqawh7wm5)

Guia de Fontes e Introdução ao EARS → Você está aqui

[claudecode-rules.md](?tab=t.8gg0j8f3wd99)