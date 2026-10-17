**[METADADOS_SISTEMA]**
STATUS: RASCUNHO
FILE_ID: 1i9XtjdPMGJhYSbV6Al5QdzV1iWRMNJ9c58zZXUK-z8g
DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app
CATEGORIA: Mapeamento e Governança de Dados
SUBCATEGORIA: Índice de Documentos
VERSAO: v1.0.0
SUBSTITUI: N/A
DATA_HOMOLOGACAO: 2026-10-11
AUTORIDADE: Davi Sermenho
ESCOPO: Índice de documentos e metadados de governança
ULTIMA_REVISAO: 2026-10-11
**[FIM_METADADOS]**

---

# Registro de Governança de Arquivos e Mapeamento de Dados

Estruturação completa dos metadados de governança, taxonomia de status e índice de documentos cadastrados no repositório, em conformidade com a Constituição do Projeto de Reorganização do Google Drive (v4.0.0) e a Arquitetura do Contexto Mínimo Suficiente.

O registro a seguir consolida a estrutura de governança de dados e o índice de documentos do repositório, garantindo conformidade com a Fonte Única da Verdade (SSOT) no Google Drive e a rastreabilidade por Matriz Requisito-Evidência.

# Informações Gerais de Governança

-   **Esquema:** [https://json-schema.org/draft/2020-12/schema](https://json-schema.org/draft/2020-12/schema)
-   **Versão do Índice:** 1.0.0
-   **Última Atualização:** 11/10/2026 às 19:11:15 (-03:00)
-   **Custódio dos Dados (Data Steward):** davisermenho@handballtrack.app
-   **Ação Padrão de Governança:** Bloquear execução se status for desconhecido
-   **Verificação Estrita de Linhagem:** Ativada (true)

# Taxonomia de Status

| Status | Descrição e Aplicação |
| --- | --- |
| [ATIVO] | Documento oficial, aprovado, atualizado e ativo. Fonte de verdade para tomada de decisão e consulta por LLMs/NotebookLM. |
| --- | --- |
| [ARQUIVADO] | Documento histórico, desatualizado ou substituído por versão mais recente. Mantido apenas para fins de auditoria e memória técnica. Deve ser ignorado em consultas operacionais ativas. |
| --- | --- |
| [RASCUNHO] | Documento em elaboração, revisão ou pendente de aprovação. Não possui força normativa ou decisória. |
| --- | --- |
| REVIEW_REQUIRED | Documento pendente de revisão de conteúdo e validação técnica ou quando o conteúdo não puder ser lido de modo suficiente. |
| --- | --- |

# Catálogo de Documentos Registrados

| Nome do Arquivo | Identificador (File ID) | Status | Nível | Tópico Canônico | Caminho no Repositório | Última Validação |
| --- | --- | --- | --- | --- | --- | --- |
| [ATIVO] Constituição_do_Projeto_de_Reorganização_do_Google_Drive | 1ytvfgxUr6w05ChXTc6u-3X_r8UduoqAUKglJqoSeo3o | ATIVO | 1 | SSOT da Governança | /Governança | 11/10/2026 00:00:00 |
| --- | --- | --- | --- | --- | --- | --- |
| [ATIVO] Arquitetura do Contexto Mínimo Suficiente | 1Y5FSd-TUzwVo_K10vK66PSPFvct_tMkYHADX7Sq6rfg | ATIVO | 1 | Arquitetura de Contexto | /Governança/Arquitetura | 11/10/2026 00:00:00 |
| --- | --- | --- | --- | --- | --- | --- |
| [ATIVO] 20-CURRENT-STATE-INDEX.json | 1i9XtjdPMGJhYSbV6Al5QdzV1iWRMNJ9c58zZXUK-z8g | ATIVO | 1 | Mapeamento e Governança de Dados | /Governança | 11/10/2026 19:11:15 |
| --- | --- | --- | --- | --- | --- | --- |

## Detalhamento dos Registros

-   **Conformidade e Princípios de Governança:**
    -   **Princípio Primário:** Identidade do arquivo definida exclusivamente pelo File ID universal.
    -   **Rastreabilidade Contextual:** Mapeamento biunívoco entre requisitos de informação, rotas e evidências.
-   **Constituição_do_Projeto_de_Reorganização_do_Google_Drive (v4.0.0)**
    -   **Resumo:** Diretriz soberana de governança multiambiante e Fonte Única da Verdade (SSOT) do repositório.
    -   **Predecessores:** v3.1.1
    -   **Substituído por:** Ausente (Versão mais recente ativa)
-   **Arquitetura do Contexto Mínimo Suficiente**
    -   **Resumo:** Especificação da arquitetura orientada por requisitos de informação, seleção e recuperação de contexto irredundante.
    -   **Predecessores:** MAP-CTX-001
    -   **Substituído por:** Ausente (Versão mais recente ativa)

# Estrutura JSON Incorporada

{

"$schema": "https://json-schema.org/draft/2020-12/schema",

"index_version": "1.0.0",

"last_updated": "2026-10-11T19:11:15-03:00",

"data_steward": "davisermenho@handballtrack.app",

"repository_governance": {

"default_action": "BLOCK_EXECUTION_IF_STATUS_UNKNOWN",

"strict_lineage_check": true

},

"status_taxonomy": {

"ATIVO": "Documento oficial, aprovado, atualizado e ativo. Fonte de verdade para tomada de decisão e consulta por LLMs/NotebookLM.",

"ARQUIVADO": "Documento histórico, desatualizado ou substituído por versão mais recente. Mantido apenas para fins de auditoria e memória técnica. Deve ser ignorado em consultas operacionais ativas.",

"RASCUNHO": "Documento em elaboração, revisão ou pendente de aprovação. Não possui força normativa ou decisória.",

"REVIEW_REQUIRED": "Documento pendente de revisão de conteúdo e validação técnica."

},

"documents": [

{

"file_id": "1ytvfgxUr6w05ChXTc6u-3X_r8UduoqAUKglJqoSeo3o",

"file_name": "[ATIVO] Constituição_do_Projeto_de_Reorganização_do_Google_Drive",

"status": "ATIVO",

"authority_level": 1,

"canonical_topic": "SSOT da Governança",

"superseded_by": null,

"predecessor_ids": [],

"path_or_folder": "/Governança",

"summary": "Diretriz soberana de governança multiambiante e Fonte Única da Verdade (SSOT) do repositório.",

"last_validated_at": "2026-10-11T00:00:00-03:00"

},

{

"file_id": "1Y5FSd-TUzwVo_K10vK66PSPFvct_tMkYHADX7Sq6rfg",

"file_name": "[ATIVO] Arquitetura do Contexto Mínimo Suficiente",

"status": "ATIVO",

"authority_level": 1,

"canonical_topic": "Arquitetura de Contexto",

"superseded_by": null,

"predecessor_ids": [],

"path_or_folder": "/Governança/Arquitetura",

"summary": "Especificação da arquitetura orientada por requisitos de informação, seleção e recuperação de contexto irredundante.",

"last_validated_at": "2026-10-11T00:00:00-03:00"

},

{

"file_id": "1i9XtjdPMGJhYSbV6Al5QdzV1iWRMNJ9c58zZXUK-z8g",

"file_name": "[ATIVO] 20-CURRENT-STATE-INDEX.json",

"status": "ATIVO",

"authority_level": 1,

"canonical_topic": "Mapeamento e Governança de Dados",

"superseded_by": null,

"predecessor_ids": [],

"path_or_folder": "/Governança",

"summary": "Estruturação completa dos metadados de governança, taxonomia de status e índice de documentos cadastrados.",

"last_validated_at": "2026-10-11T19:11:15-03:00"

}

]

}