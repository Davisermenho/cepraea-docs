[METADADOS_SISTEMA]
ID_FONTE: GOV-004
TITULO_CANONICO: GOV-004 Mapeamento Mestre de Fontes e Metadados CEPRAEA
FILE_ID: 1OsZpqYak84xuvdNUo4FaIi_9n8tVjBlLxCSQeHbo4Fg
STATUS: RASCUNHO
VERSAO: v1.0.0
DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app
CATEGORIA: Governança
SUBCATEGORIA: Taxonomia e Metadados
DATA_HOMOLOGACAO: 2026-10-12
AUTORIDADE: Davi Sermenho
ESCOPO: Mapeamento biunívoco entre ID_FONTE (NotebookLM), TÍTULO_CANÔNICO e nome físico no Google Drive
[FIM_METADADOS]

---

# GOV-004 - Mapeamento Mestre de Fontes e Metadados CEPRAEA

# 1. Finalidade

Este documento estabelece a matriz unificada de rastreabilidade, catalogação e mapeamento mestre de metadados para todos os arquivos e artefatos pertencentes ao ecossistema **CEPRAEA Beach Pro**.

Sua finalidade principal é garantir a integridade referencial, eliminar ambiguidades de nomenclatura entre o ambiente físico do Google Drive e a camada conceitual de governança, além de fornecer aos agentes autorizados e aos revisores humanos um mapa determinístico de autoridade documental.

## 1.1. Arquivos PWA - CEPRAEA BEACH PRO

Para garantir a correta catalogação, rastreabilidade e reconciliação dos arquivos contendo pesquisas de arquitetura, documentação técnica, históricos e especificações do PWA do CEPRAEA, deve ser utilizado um campo de metadados dedicado denominado IS_PWA_SPEC (ou a definição do subdomínio/subcategoria apropriado), juntamente com o identificador de fonte no padrão de taxonomia do projeto.

Esta padronização assegura que a camada conceitual e os agentes automatizados de auditoria identifiquem univocamente as especificações pertencentes ao ecossistema da aplicação Web progressiva (PWA).

### 1.1.1. Exemplo de Bloco de Metadados PWA CEPRAEA

-   **Arquivo no Drive:** [ATIVO] Especificação Técnica e Contratos PWA v1.0.md
-   **Aplicação:** Insira no topo dos arquivos de documentação e arquitetura do PWA CEPRAEA.
-   **Escopo:** Documentação técnica, arquitetura de componentes, contratos de estado offline/online e histórico de requisitos do PWA CEPRAEA Beach Pro.

---

[METADADOS_SISTEMA]

ID_FONTE: PWA-001

TITULO_CANONICO: PWA-001 Especificação Técnica e Contratos do PWA CEPRAEA

FILE_ID: 1PWA_Example_File_ID_ CEPRAEA_Beach_Pro

IS_PWA_SPEC: TRUE

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: PWA / Frontend & Offline Capabilities

DATA_HOMOLOGACAO: 2026-10-13

AUTORIDADE: Davi Sermenho

ESCOPO: Documentação técnica, arquitetura de componentes, contratos de estado offline/online e histórico de requisitos do PWA CEPRAEA Beach Pro

[FIM_METADADOS]

---

# PWA-001 — Especificação Técnica e Contratos do PWA CEPRAEA Beach Pro

# 2. Regras de Taxonomia e Convenção de Nomenclatura

A padronização dos identificadores segue a sintaxe rigorosa AAA-xxx, onde o prefixo triliteral (AAA) determina o domínio funcional e o sufixo numérico (xxx) assegura a ordenação sequencial estável:

-   **GOV (Governança e Políticas):** Diretrizes operacionais, regimentos de comitê, controle de agentes e invariantes de sistema.
-   **PRD (Produto e Domínio):** Especificações de produto, charters, modelos de domínio e contratos lógicos de fluxo esportivo.
-   **REQ (Requisitos e Rastreabilidade):** Catálogos de requisitos funcionais, não funcionais e matrizes de rastreabilidade.
-   **ARQ (Arquitetura Técnica):** Decisões arquiteturais (ADRs), drivers, modelos lógicos/físicos de dados e opções estruturais.
-   **AES (Sistema AESDS):** Padrões do *Agent-Executable Software Development Specification* (camadas 00 a 10).
-   **DAT (Bases de Dados e Operacional):** Planilhas operacionais, *Single Source of Truth* (SSOT) de banco, cadastros e logs de treino.
-   **OPS (Operação e Manutenção):** Manuais operacionais, procedimentos executáveis e runbooks de sistema.
-   **AUD (Auditoria e Qualidade):** Relatórios de auditoria, inventários de fontes e verificações formais.
-   **REF (Referências e Pesquisa):** Relatórios de pesquisa externa, normas sintáticas (ex.: EARS) e referências técnicas.
-   **PRG (Código e Automação):** Scripts executáveis, automações do Google Apps Script e trechos de código.
-   **TPL (Modelos e Templates):** Modelos estruturados de documentos e formulários padrão.
-   **TST (Testes e Validação):** Cenários de validação, testes regressivos e propriedades de comportamento.
-   **DES (Design e Identidade Visual):** Especificações de marca, guia de estilo de documentos e refinamento de layout.
-   **HST (Histórico e Logs):** Transcrições e logs de sessões passadas de elicitação e auditoria.

# 3. Tabela Mestra de Mapeamento de Fontes

| ID_FONTE | TÍTULO_CANÔNICO | NOME LIMPO DO ARQUIVO (GOOGLE DRIVE) | CATEGORIA |
| --- | --- | --- | --- |
| GOV-901 | Diretrizes operacionais de fontes e reconciliação — Gemini Notebook CEPRAEA | GOV-901 — Diretrizes operacionais do Gemini Notebook — CANDIDATA v0.2 | Governança / Diretrizes |
| --- | --- | --- | --- |
| GOV-001 | Registro Mestre de Artefatos e Funcionamento — Sistema CEPRAEA | REGISTRO MESTRE DE ARTEFATOS E FUNCIONAMENTO — SISTEMA CEPRAEA.docx | Governança / Inventário |
| --- | --- | --- | --- |
| GOV-002 | Fluxo Completo de Desenvolvimento — SDLC Agêntico Governança | FLUXO COMPLETO DE DESENVOLVIMENTO — CEPRAEA BEACH PRO.docx | Governança / SDLC |
| --- | --- | --- | --- |
| GOV-003 | Mem0 Policy — Camada Auxiliar de Memória Persistente do Codex | mem0.md | Governança / Memória |
| --- | --- | --- | --- |
| GOV-004 | GOV-004 Mapeamento Mestre de Fontes e Metadados | GOV-004 Mapeamento Mestre de Fontes e Metadados | Governança / Mapeamento |
| --- | --- | --- | --- |
| GOV-005 | Base Documental Derivada — Escopo e Invariantes v0.1 | BASE CEPRAEA BEACH PRO — CANÔNICA — v0.1.docx | Governança / Base Derivada |
| --- | --- | --- | --- |
| GOV-006 | Readiness & Validation Gates — Critérios de Transição | 08-READINESS-AND-VALIDATION-GATES.md | Governança / Gates |
| --- | --- | --- | --- |
| GOV-007 | Regras Operacionais Derivadas para Agentes | DOC-006 — Regras Operacionais Derivadas para Agentes.docx | Governança / Agentes |
| --- | --- | --- | --- |
| PRD-001 | CEPRAEA BEACH PRO — Elicitação de Produto e Regras do Domínio | PRODUCT-DOMAIN-SPEC | Produto / Domínio |
| --- | --- | --- | --- |
| PRD-002 | Diagramas e Contrato do Fluxo de Treinamentos | TRAINING_FLOW_CONTRACT.md | Produto / Fluxos |
| --- | --- | --- | --- |
| PRD-003 | Project Charter — CEPRAEA Beach Pro | 02-PROJECT-CHARTER.md | Produto / Visão |
| --- | --- | --- | --- |
| PRD-004 | Shared Understanding — Entendimento Compartilhado | 03-SHARED-UNDERSTANDING.md | Produto / Entendimento |
| --- | --- | --- | --- |
| PRD-005 | Descrição Operacional e Visão da Planilha CEPRAEA | DESC-CEPRAEA.docx | Produto / Legado |
| --- | --- | --- | --- |
| REQ-001 | CEPRAEA BEACH PRO — Fase 04 — REQUIREMENTS (Proposta) | Proposta de Requirements | Requisitos |
| --- | --- | --- | --- |
| REQ-002 | TRACEABILITY — Matriz de Rastreabilidade | 07-TRACEABILITY.md | Requisitos / Rastreabilidade |
| --- | --- | --- | --- |
| REQ-003 | REQUIREMENTS — Especificação Canônica de Requisitos | 04-REQUIREMENTS.md | Requisitos |
| --- | --- | --- | --- |
| ARQ-001 | BANCO CEPRAEA — Modelagem Completa Corrigida do Banco de Dados | BancoCEPRAEA.docx | Arquitetura de Dados |
| --- | --- | --- | --- |
| ARQ-002 | Architecture Drivers — Direcionadores Arquiteturais | 05-ARCHITECTURE-DRIVERS.md | Arquitetura / Drivers |
| --- | --- | --- | --- |
| ARQ-003 | Especificação Arquitetural Consolidada | 12-ARCHITECTURE.md | Arquitetura |
| --- | --- | --- | --- |
| ARQ-004 | Matriz de Alternativas e Opções Arquiteturais | 11-ARCHITECTURE-OPTIONS.md | Arquitetura / Opções |
| --- | --- | --- | --- |
| AES-000 | AESDS 00 — Índice Mestre | 00 — ÍNDICE MESTRE — AESDS — CEPRAEA BEACH PRO.docx | AESDS / Índice |
| --- | --- | --- | --- |
| AES-002 | AESDS 02 — Especificação de Experiência e Interação | 02 — ESPECIFICAÇÃO DE EXPERIÊNCIA E INTERAÇÃO — AESDS — CEPRAEA BEACH PRO.docx | AESDS / UX & UI |
| --- | --- | --- | --- |
| AES-003 | AESDS 03 — Arquitetura Técnica e Contratos do Frontend | 03 — ARQUITETURA TÉCNICA E CONTRATOS DO FRONTEND — AESDS — CEPRAEA BEACH PRO.docx | AESDS / Frontend |
| --- | --- | --- | --- |
| AES-004 | AESDS 04 — Roadmap de Implementação e Grafo de Tarefas | 04 — ROADMAP DE IMPLEMENTAÇÃO E GRAFO DE TAREFAS — AESDS — CEPRAEA BEACH PRO.docx | AESDS / Tarefas |
| --- | --- | --- | --- |
| AES-007 | AESDS 07 — Protocolo de Execução e Review dos Agentes | 07 — PROTOCOLO DE EXECUÇÃO E REVIEW DOS AGENTES — AESDS — CEPRAEA BEACH PRO.docx | AESDS / Agentes |
| --- | --- | --- | --- |
| AES-008 | AESDS 08 — Catálogo de Referências e Protocolo de Pesquisa | 08 — CATÁLOGO DE REFERÊNCIAS E PROTOCOLO DE PESQUISA — AESDS — CEPRAEA BEACH PRO.docx | AESDS / Pesquisa |
| --- | --- | --- | --- |
| AES-009 | AESDS 09 — Índice de Runbooks e Estado Operacional | 09 — ÍNDICE DE RUNBOOKS E ESTADO OPERACIONAL — AESDS — CEPRAEA BEACH PRO.docx | AESDS / Runbooks |
| --- | --- | --- | --- |
| AES-010 | AESDS 10 — Catálogo Canônico de Artefatos, Papéis e Enforcement | 10 — CATÁLOGO CANÔNICO DE ARTEFATOS, PAPÉIS E ENFORCEMENT — AESDS — CEPRAEA BEACH PRO.docx | AESDS / Catálogo |
| --- | --- | --- | --- |
| DAT-001 | CEPRAEA DATABASE — SSOT Operacional | CEPRAEA DATABASE.xlsx | Bases de Dados / SSOT |
| --- | --- | --- | --- |
| DAT-002 | Controle de Implementação — Pesquisa de Treinos CEPRAEA 2026 | Implementação — Pesquisa de Treinos CEPRAEA 2026.xlsx | Bases de Dados / Pesquisa |
| --- | --- | --- | --- |
| DAT-003 | CEPRAEA 2026 — Controle Inicial de Atletas e Senhas | CEPRAEA 2026(1).xlsx | Bases de Dados / Legado |
| --- | --- | --- | --- |
| DAT-004 | CEPRAEA Wellness — Configuração e Respostas | CEPRAEA — Wellness — Configuração e Respostas.xlsx | Bases de Dados / Wellness |
| --- | --- | --- | --- |
| DAT-005 | Glossário de Dados CEPRAEA v0.1 | Glossário de Dados — CEPRAEA v0.1.xlsx | Bases de Dados / Dicionário |
| --- | --- | --- | --- |
| DAT-006 | Planilha Operacional Mensal — CEPRAEA ABRIL 2026 | CEPRAEA ABRIL 2026.xlsx | Bases de Dados / Operacional |
| --- | --- | --- | --- |
| DAT-007 | Respostas de Formulários e Ajuste de Times Shootout | CEPRAEA 2026(2).xlsx | Bases de Dados / Pesquisa |
| --- | --- | --- | --- |
| DAT-008 | Matriz Consolidada de Disponibilidade de Competições | CEPRAEA_.xlsx | Bases de Dados / Operacional |
| --- | --- | --- | --- |
| DAT-009 | Planilha Operacional Mensal — CEPRAEA AGOSTO 2026 | CEPRAEA AGOSTO 2026.xlsx | Bases de Dados / Operacional |
| --- | --- | --- | --- |
| OPS-001 | Manual Operacional — Do Legado ao Software Funcional | Manual Operacional — CEPRAEA Beach Pro.docx | Operação / Guia |
| --- | --- | --- | --- |
| PLN-001 | Roadmap de Implementação dos Dashboards v2.3 | CEPRAEA — Roadmap de Implementação dos Dashboards.docx | Planejamento / Dashboards |
| --- | --- | --- | --- |
| PRM-001 | Prompts de Abertura dos Chats | 09-CHAT-OPENING-PROMPTS.md | Prompts / Workflow |
| --- | --- | --- | --- |
| AUD-001 | Auditoria de Fidelidade de Escopo — Relatório de Achados | SFA-20260906-001 — Auditoria de Fidelidade de Escopo — Execução Inicial.docx | Auditoria / Fidelidade |
| --- | --- | --- | --- |
| AUD-002 | Inventário Auditável das 71 Fontes | SFA-20260906-001 — Inventário auditável das 71 fontes.csv | Auditoria / Inventário |
| --- | --- | --- | --- |
| REF-001 | Relatório de Pesquisa — Padrões Sintáticos do EARS | DOC-003 — Relatório de Pesquisa_ Padrões Sintáticos do EARS.docx | Referências / Engenharia |
| --- | --- | --- | --- |
| PRG-001 | CEPRAEA Wellness Apps Script — Automação Mobile (Cópia) | Cópia de CEPRAEA — Wellness — Apps Script Mobile.txt | Scripts / Automação |
| --- | --- | --- | --- |
| PRG-002 | CEPRAEA Wellness Apps Script — Automação Mobile | CEPRAEA — Wellness — Apps Script Mobile.txt | Scripts / Automação |
| --- | --- | --- | --- |
| DES-001 | Diretrizes de Refinamento Visual da Relação Nominal | CEPRAEA-pdf.docx | Design & Identidade |
| --- | --- | --- | --- |
| TPL-001 | Modelo Canônico de Registro de Decisão Arquitetural (ADR) | 06-ADR-TEMPLATE.md | Templates / Arquitetura |
| --- | --- | --- | --- |
| TST-001 | Cenários de Validação e Testes Regressivos | 10-VALIDATION-SCENARIOS.md | Testes & Validação |
| --- | --- | --- | --- |
| HST-000 | Histórico de Conversa — Chat 00 (Intake e Objetivos) | HISTÓRICO-Chat-00-—-Intake-e-objetivos (1).json | Histórico / Logs |
| --- | --- | --- | --- |
| HST-001 | Histórico de Conversa — Chat 01 (Elicitação) | HISTÓRICO-Chat-01-—-Elicitação.json | Histórico / Logs |
| --- | --- | --- | --- |
| HST-002 | Histórico de Conversa — Chat 02 (Auditoria do Entendimento) | HISTÓRICO-Chat-02-—-Auditoria-do-entendimento.json | Histórico / Logs |
| --- | --- | --- | --- |
| HST-003 | Histórico de Conversa — Chat 03 (Modelagem do Domínio) | HISTÓRICO-Chat-03-—-Modelagem-do-domínio.json | Histórico / Logs |
| --- | --- | --- | --- |
| HST-004 | Histórico de Conversa — Chat 04 (Requisitos) | HISTÓRICO-Chat-04-—-Requisitos.json | Histórico / Logs |
| --- | --- | --- | --- |

## 4. Governança e Diretrizes do Projeto (GOV-*)

Metadados padronizados para aplicação no cabeçalho dos documentos de **Governança (GOV-*)**. Copie o bloco de metadados correspondente e insira-o na primeira linha do arquivo-alvo.

## 4.1. GOV-001 — Project Charter CEPRAEA

-   **Arquivo no Drive:** [ATIVO] Project Charter v0.9.md
-   **Aplicação:** Insira no topo do arquivo do Project Charter.
-   **Escopo:** Termo de abertura, objetivos estratégicos e governança inicial do projeto CEPRAEA.

---

[METADADOS_SISTEMA]

ID_FONTE: GOV-001

TITULO_CANONICO: GOV-001 Project Charter CEPRAEA

STATUS: RASCUNHO

VERSAO: v0.9.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Governança

SUBCATEGORIA: Escopo e Diretrizes de Projeto

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Termo de abertura, objetivos estratégicos e governança inicial do projeto CEPRAEA

[FIM_METADADOS]

---

# GOV-001 — Project Charter CEPRAEA



## 4.2. GOV-002 — Política de Memória Persistente Mem0

-   **Arquivo no Drive:** [ATIVO] Política de Memória Persistente Mem0 v1.0.md
-   **Aplicação:** Insira no topo do documento de política de memória do agente.
-   **Escopo:** Regras de persistência, atualização e sincronização da camada de memória dos agentes (Mem0 / Codex).

---

[METADADOS_SISTEMA]

ID_FONTE: GOV-002

TITULO_CANONICO: GOV-002 Mem0 Policy Codex Memory Layer

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Governança

SUBCATEGORIA: Governança de IA e Memória

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Regras de persistência, atualização e sincronização da camada de memória dos agentes (Mem0 / Codex)

[FIM_METADADOS]

---

# GOV-002 — Política de Memória Persistente Mem0 (Codex Memory Layer)



## 4.3. GOV-003 — Registro Mestre de Artefatos

-   **Arquivo no Drive:** [ATIVO] Registro Mestre de Artefatos v1.7.docx
-   **Aplicação:** Insira no topo da primeira página do Google Docs.
-   **Escopo:** Catálogo consolidado e histórico de versão de todos os artefatos do repositório.

---

[METADADOS_SISTEMA]

ID_FONTE: GOV-003

TITULO_CANONICO: GOV-003 Registro Mestre de Artefatos CEPRAEA

STATUS: RASCUNHO

VERSAO: v1.7.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Governança

SUBCATEGORIA: Inventário e Rastreabilidade

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Catálogo consolidado e histórico de versão de todos os artefatos do repositório

[FIM_METADADOS]

---

# GOV-003 — Registro Mestre de Artefatos CEPRAEA



## 4.4. GOV-004 — Mapeamento Mestre de Fontes e Metadados

-   **Arquivo no Drive:** [[ATIVO] Mapeamento Mestre de Fontes e Metadados CEPRAEA v1.0](https://docs.google.com/document/d/1OsZpqYak84xuvdNUo4FaIi_9n8tVjBlLxCSQeHbo4Fg/edit?usp=drivesdk&ouid=107431542739502884125)
-   **Aplicação:** *Já applied diretamente no documento criado.*
-   **Escopo:** Mapeamento biunívoco entre ID_FONTE (NotebookLM), TÍTULO_CANÔNICO e nome físico no Google Drive.

---

[METADADOS_SISTEMA]

ID_FONTE: GOV-004

TITULO_CANONICO: GOV-004 Mapeamento Mestre de Fontes e Metadados CEPRAEA

FILE_ID: 1OsZpqYak84xuvdNUo4FaIi_9n8tVjBlLxCSQeHbo4Fg

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Governança

SUBCATEGORIA: Taxonomia e Metadados

DATA_HOMOLOGACAO: 2026-10-12

AUTORIDADE: Davi Sermenho

ESCOPO: Mapeamento biunívoco entre ID_FONTE (NotebookLM), TÍTULO_CANÔNICO e nome físico no Google Drive

[FIM_METADADOS]

---

# GOV-004 — Mapeamento Mestre de Fontes e Metadados CEPRAEA



## 4.5. GOV-901 — Diretrizes Operacionais do Gemini Notebook

-   **Arquivo no Drive:** GOV-901 — Diretrizes operacionais do Gemini Notebook — CANDIDATA v0.2 (ID: 1detrZxrjGQOFsm0AhvY65-Y0aDKdgY6F)
-   **Aplicação:** Insira no topo do arquivo de diretrizes operacionais do notebook.
-   **Escopo:** Procedimentos propostos para preparação, auditoria e reconciliação de fontes no Gemini Notebook.

---

[METADADOS_SISTEMA]

ID_FONTE: GOV-901

TITULO_CANONICO: GOV-901 Diretrizes Operacionais Gemini Notebook

FILE_ID: 1detrZxrjGQOFsm0AhvY65-Y0aDKdgY6F

STATUS: RASCUNHO

VERSAO: v0.2.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Governança

SUBCATEGORIA: Procedimentos Operacionais Propostos

DATA_HOMOLOGACAO: 2026-10-10

AUTORIDADE: REGRA_INTERNA

ESCOPO: Procedimentos propostos para preparação, auditoria e reconciliação de fontes no Gemini Notebook

[FIM_METADADOS]

---

# GOV-901 — Diretrizes Operacionais do Gemini Notebook CEPRAEA



## 5. Especificações de Produto e Contratos de Domínio (CEP-*)

Metadados padronizados para aplicação no cabeçalho dos documentos de Especificações de Produto e Contratos de Domínio (CEP-*). Copie o bloco correspondente e insira-o na **primeira linha** do arquivo-alvo.

## 5.1. CEP-001 — Product Domain Spec

-   **Arquivo no Drive:** [ATIVO] Elicitação de Produto e Regras do Domínio v2.10.md
-   **Aplicação:** Insira no topo da especificação de domínio do produto.
-   **Escopo:** Elicitação completa das regras de negócio, invariantes de domínio e comportamento operacional do CEPRAEA.

---

[METADADOS_SISTEMA]

ID_FONTE: CEP-001

TITULO_CANONICO: CEP-001 Product Domain Spec

STATUS: RASCUNHO

VERSAO: v2.10.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Domínio do Produto

SUBCATEGORIA: Elicitação e Regras de Negócio

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Elicitação completa das regras de negócio, invariantes de domínio e comportamento operacional do CEPRAEA

[FIM_METADADOS]

---

# CEP-001 — CEPRAEA BEACH PRO — Elicitação de Produto e Regras do Domínio



## 5.2. CEP-002 — Base Cepraea Beach Pro Canônica

-   **Arquivo no Drive:** [PROPOSED] Base Cepraea Beach Pro Canônica v0.1.docx
-   **Aplicação:** Insira no topo da primeira página do modelo canônico proposto.
-   **Escopo:** Modelo conceitual canônico do produto, entidades e invariantes operacionais de referência.

---

[METADADOS_SISTEMA]

ID_FONTE: CEP-002

TITULO_CANONICO: CEP-002 Base Cepraea Beach Pro Canônica

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Domínio do Produto

SUBCATEGORIA: Especificação Canônica

DATA_HOMOLOGACAO: 2026-10-12

AUTORIDADE: Davi Sermenho

ESCOPO: Modelo conceitual canônico do produto, entidades e invariantes operacionais de referência

[FIM_METADADOS]

---

# CEP-002 — Base Cepraea Beach Pro Canônica



## 5.3. CEP-003 — Contrato de Produto e Domínio (AESDS 01)

-   **Arquivo no Drive:** 01 — CONTRATO DE PRODUTO E DOMÍNIO — AESDS — CEPRAEA BEACH PRO.docx (ID: 1Hs2BoOFWBTodY5uVXgnpzYhew-uwEO4m)
-   **Aplicação:** Insira no topo da primeira página do documento de Contrato de Produto (AESDS 01).
-   **Escopo:** Diretrizes de integridade, autoridade semântica, regras de autonomia de agentes e invariantes do PWA CEPRAEA BEACH PRO (AESDS 01).

---

[METADADOS_SISTEMA]

ID_FONTE: CEP-003

TITULO_CANONICO: CEP-003 Contrato de Produto e Domínio AESDS 01

FILE_ID: 1Hs2BoOFWBTodY5uVXgnpzYhew-uwEO4m

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Domínio do Produto

SUBCATEGORIA: Contrato Operacional

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Diretrizes de integridade, autoridade semântica, regras de autonomia de agentes e invariantes do PWA CEPRAEA BEACH PRO (AESDS 01)

[FIM_METADADOS]

---

# CEP-003 — Contrato de Produto e Domínio (AESDS 01)



## 5.4. CEP-004 — Contrato do Fluxo de Treinamentos

-   **Arquivo no Drive:** [ATIVO] Contrato do Fluxo de Treinamentos v1.6.md
-   **Aplicação:** Insira no topo do contrato do fluxo de treinos.
-   **Escopo:** Regras de negócio, ciclo de vida, solicitações de disponibilidade e presenças no fluxo de treinamentos.

---

[METADADOS_SISTEMA]

ID_FONTE: CEP-004

TITULO_CANONICO: CEP-004 Contrato do Fluxo de Treinamentos

STATUS: RASCUNHO

VERSAO: v1.6.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Domínio do Produto

SUBCATEGORIA: Fluxos e Operação de Treinos

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Regras de negócio, ciclo de vida, solicitações de disponibilidade e presenças no fluxo de treinamentos

[FIM_METADADOS]

---

# CEP-004 — Contrato do Fluxo de Treinamentos



## 5.5. CEP-005 — Descrição Operacional CEPRAEA

-   **Arquivo no Drive:** [ATIVO] Descrição Operacional CEPRAEA v1.0.docx
-   **Aplicação:** Insira no topo da primeira página da Descrição Operacional.
-   **Escopo:** Mapeamento operacional dos papéis de comissão técnica, elenco, atletas e gestão do clube.

---

[METADADOS_SISTEMA]

ID_FONTE: CEP-005

TITULO_CANONICO: CEP-005 Descrição Operacional CEPRAEA

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Domínio do Produto

SUBCATEGORIA: Visão Operacional da Equipe

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Mapeamento operacional dos papéis de comissão técnica, elenco, atletas e gestão do clube

[FIM_METADADOS]

---

# CEP-005 — Descrição Operacional CEPRAEA

## 6. Arquitetura Técnica e Engenharia do Sistema (ARQ-*)

## Metadados padronizados para aplicação no cabeçalho dos documentos de Arquitetura Técnica (ARQ-*). Copie o bloco correspondente e insira-o na primeira linha do arquivo-alvo.

## 6.1. ARQ-001 — Human Governed Dual Agent SDLC Architecture

-   **Arquivo no Drive:** [ATIVO] Arquitetura SDLC Agêntico v1.0.md
-   **Aplicação:** Insira no topo do documento de arquitetura SDLC agêntica.
-   **Escopo:** Arquitetura de desenvolvimento humano-agente com papéis separados entre Executor (Claude Code), Reviewer (Codex) e Autoridade Humana.

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-001

TITULO_CANONICO: ARQ-001 Human Governed Dual Agent SDLC Architecture

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: SDLC & Governança Agêntica

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Arquitetura de desenvolvimento humano-agente com papéis separados entre Executor (Claude Code), Reviewer (Codex) e Autoridade Humana

[FIM_METADADOS]

---

# ARQ-001 — Human Governed Dual Agent SDLC Architecture



## 6.2. ARQ-010 — Índice Mestre (AESDS 00)

-   **Arquivo no Drive:** 00 — ÍNDICE MESTRE — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 1UUAenfd7_iFb7OmGU5xpPG-2lzUQtqQz
-   **Aplicação:** Insira no topo da primeira página do Índice Mestre AESDS.
-   **Escopo:** Roteador principal de autoridades, métricas de revisão, sequência de leitura e mapeamento de camadas conceituais da especificação AESDS.

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-010

TITULO_CANONICO: ARQ-010 Índice Mestre AESDS 00

FILE_ID: 1UUAenfd7_iFb7OmGU5xpPG-2lzUQtqQz

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: Roteamento e Estrutura AESDS

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Roteador principal de autoridades, métricas de revisão, sequência de leitura e mapeamento de camadas conceituais da especificação AESDS

[FIM_METADADOS]

---

# ARQ-010 — Índice Mestre — AESDS 00



## 6.3. ARQ-012 — Especificação de Experiência e Interação (AESDS 02)

-   **Arquivo no Drive:** 02 — ESPECIFICAÇÃO DE EXPERIÊNCIA E INTERAÇÃO — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 1cLr8XR8tLouarqCrxeB9g2OBm0zYt3sv
-   **Aplicação:** Insira no topo da primeira página da Especificação de Experiência e Interação.
-   **Escopo:** Especificação de tarefas, fluxos de usuário, estados de interação, arquitetura da informação, componentes semânticos, acessibilidade e mobile-first (AESDS 02).

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-012

TITULO_CANONICO: ARQ-012 Especificação de Experiência e Interação AESDS 02

FILE_ID: 1cLr8XR8tLouarqCrxeB9g2OBm0zYt3sv

STATUS: RASCUNHO

VERSAO: v0.11.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: UX/UI & Design System

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Especificação de tarefas, fluxos de usuário, estados de interação, arquitetura da informação, componentes semânticos, acessibilidade e mobile-first (AESDS 02)

[FIM_METADADOS]

---

# ARQ-012 — Especificação de Experiência e Interação (AESDS 02)



## 6.4. ARQ-013 — Arquitetura Técnica e Contratos do Frontend (AESDS 03)

-   **Arquivo no Drive:** 03 — ARQUITETURA TÉCNICA E CONTRATOS DO FRONTEND — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 1RHyLJV8iA1RD9PrKqDUtvqB8GuLIFuJh
-   **Aplicação:** Insira no topo da primeira página da Arquitetura Técnica do Frontend.
-   **Escopo:** Arquitetura técnica da stack React 19 + TypeScript + Vite + Supabase, PWA estático, camadas conceituais, tratamento de erros e contratos de dados (AESDS 03).

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-013

TITULO_CANONICO: ARQ-013 Arquitetura Técnica e Contratos Frontend AESDS 03

FILE_ID: 1RHyLJV8iA1RD9PrKqDUtvqB8GuLIFuJh

STATUS: RASCUNHO

VERSAO: v0.11.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: Frontend & Contratos de Dados

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Arquitetura técnica da stack React 19 + TypeScript + Vite + Supabase, PWA estático, camadas conceituais, tratamento de erros e contratos de dados (AESDS 03)

[FIM_METADADOS]

---

# ARQ-013 — Arquitetura Técnica e Contratos do Frontend (AESDS 03)



## 6.5. ARQ-014 — Catálogo Canônico de Artefatos, Papéis e Enforcement (AESDS 10)

-   **Arquivo no Drive:** 10 — CATÁLOGO CANÔNICO DE ARTEFATOS, PAPÉIS E ENFORCEMENT — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 1Ao95Uu4SmoJtVgeAg46H9vzT6crJIETK
-   **Aplicação:** Insira no topo da primeira página do Catálogo Canônico.
-   **Escopo:** Consolidação navegável de artefatos do SDLC agêntico, autoridades, precedências conceituais, classes e critérios de verificação (AESDS 10).

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-014

TITULO_CANONICO: ARQ-014 Catálogo Canônico de Artefatos AESDS 10

FILE_ID: 1Ao95Uu4SmoJtVgeAg46H9vzT6crJIETK

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: Catálogo de Artefatos e Governança

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Consolidação navegável de artefatos do SDLC agêntico, autoridades, precedências conceituais, classes e critérios de verificação (AESDS 10)

[FIM_METADADOS]

---

# ARQ-014 — Catálogo Canônico de Artefatos, Papéis e Enforcement (AESDS 10)



## 6.6. ARQ-015 — Padrão de Tarefas Atômicas e Critérios de Aceitação (AESDS 05)

-   **Arquivo no Drive:** 05 — PADRÃO DE TAREFAS ATÔMICAS E CRITÉRIOS DE ACEITAÇÃO — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 1Mv7HjMWZalL0fS_BayjvWXfykJvhRRu1
-   **Aplicação:** Insira no topo da primeira página do Padrão de Tarefas Atômicas.
-   **Escopo:** Definidor da unidade mínima de trabalho atômico, templates de task, cenários BDD, restrições MUST/MUST NOT e oráculos de aceitação (AESDS 05).

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-015

TITULO_CANONICO: ARQ-015 Padrão de Tarefas Atômicas e Critérios AESDS 05

FILE_ID: 1Mv7HjMWZalL0fS_BayjvWXfykJvhRRu1

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: Especificação de Tasks & BDD

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Definidor da unidade mínima de trabalho atômico, templates de task, cenários BDD, restrições MUST/MUST NOT e oráculos de aceitação (AESDS 05)

[FIM_METADADOS]

---

# ARQ-015 — Padrão de Tarefas Atômicas e Critérios de Aceitação (AESDS 05)



## 6.7. ARQ-016 — Arquitetura de Auditoria e Assurance Agêntico (AESDS 11)

-   **Arquivo no Drive:** 11 — ARQUITETURA DE AUDITORIA E ASSURANCE AGÊNTICO — IMPLANTAÇÃO E EXECUÇÃO — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 1x1_uKzarnVqD9COQX8J5_EOU5vG0InTK
-   **Aplicação:** Insira no topo da primeira página do documento de Assurance.
-   **Escopo:** Protocolo de auditoria local baseado em evidência para Claude Code e Codex, taxonomia de verdicts e verificações determinísticas (AESDS 11).

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-016

TITULO_CANONICO: ARQ-016 Arquitetura de Auditoria e Assurance AESDS 11

FILE_ID: 1x1_uKzarnVqD9COQX8J5_EOU5vG0InTK

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: Assurance & Auditoria Agêntica

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Protocolo de auditoria local baseado em evidência para Claude Code e Codex, taxonomia de verdicts e verificações determinísticas (AESDS 11)

[FIM_METADADOS]

---

# ARQ-016 — Arquitetura de Auditoria e Assurance Agêntico (AESDS 11)



## 6.8. ARQ-017 — Implantação da Arquitetura Formal de Verificação e Assurance

-   **Arquivo no Drive:** CEPRAEA BEACH PRO — Implantação da Arquitetura Formal de Verificação e Assurance.docx
-   **File ID:** 14Dd79BXzHRf6_Ee7UkD14WVCFqOH6MGk
-   **Aplicação:** Insira no topo da primeira página do plano de implantação da verificação formal.
-   **Escopo:** Protocolo e plano de implantação da camada formal de contrato e verificação (FVR) e harness de testes no SDLC.

---

[METADADOS_SISTEMA]

ID_FONTE: ARQ-017

TITULO_CANONICO: ARQ-017 Implantação da Arquitetura Formal de Verificação

FILE_ID: 14Dd79BXzHRf6_Ee7UkD14WVCFqOH6MGk

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Arquitetura Técnica

SUBCATEGORIA: Verificação Formal & FVR

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Protocolo e plano de implantação da camada formal de contrato e verificação (FVR) e harness de testes no SDLC

[FIM_METADADOS]

---

# ARQ-017 — CEPRAEA BEACH PRO — Implantação da Arquitetura Formal de Verificação e Assurance



## 7. Engenharia de Requisitos, Quality Gates e Testes (REQ-* / TST-*)

Metadados padronizados para aplicação no cabeçalho dos documentos de Requisitos e Testes (REQ-* / TST-*). Copie o bloco correspondente e insira-o na **primeira linha** do arquivo-alvo.

## 7.1. REQ-001 — Especificação de Requisitos da Fase 04

-   **Arquivo no Drive:** 04-REQUIREMENTS.md / [PROPOSED] Especificação de Requisitos v0.1.docx
-   **File ID:** 18z6ow4K8uWTziw_hxTc4JMuHpaU3oc_W
-   **Aplicação:** Insira no topo do documento de Requisitos.
-   **Escopo:** Catálogo proposto de requisitos funcionais (FR-001..FR-025), não funcionais (NFR) e restrições (CON) derivado das decisões de produto.

---

[METADADOS_SISTEMA]

ID_FONTE: REQ-001

TITULO_CANONICO: REQ-001 Especificação de Requisitos da Fase 04

FILE_ID: 18z6ow4K8uWTziw_hxTc4JMuHpaU3oc_W

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Requisitos e Testes

SUBCATEGORIA: Requisitos Funcionais e Não Funcionais

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Catálogo proposto de requisitos funcionais (FR-001..FR-025), não funcionais (NFR) e restrições (CON) derivado das decisões de produto

[FIM_METADADOS]

---

# REQ-001 — Especificação de Requisitos da Fase 04



## 7.2. TST-001 — Readiness and Validation Gates

-   **Arquivo no Drive:** 08-READINESS-AND-VALIDATION-GATES.md
-   **File ID:** 1Pys2IP33AwBOqs5M-D3V6vr6sCSGI0uK
-   **Aplicação:** Insira no topo do documento de Readiness & Validation Gates.
-   **Escopo:** Critérios e checklists dos Gates A a E para validação de prontidão de intenção, entendimento, requisitos, arquitetura e decisões (ADRs).

---

[METADADOS_SISTEMA]

ID_FONTE: TST-001

TITULO_CANONICO: TST-001 Readiness and Validation Gates

FILE_ID: 1Pys2IP33AwBOqs5M-D3V6vr6sCSGI0uK

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Requisitos e Testes

SUBCATEGORIA: Quality Gates & Validação

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Critérios e checklists dos Gates A a E para validação de prontidão de intenção, entendimento, requisitos, arquitetura e decisões (ADRs)

[FIM_METADADOS]

---

# TST-001 — Readiness and Validation Gates



## 7.3. TST-002 — Especificação de Testes e Verificação (AESDS 06)

-   **Arquivo no Drive:** 06 — ESPECIFICAÇÃO DE TESTES E VERIFICAÇÃO — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 15xvEXOZZ5C-vnq1w3E1kyfmw92hqAJTV
-   **Aplicação:** Insira no topo da primeira página da Especificação de Testes (AESDS 06).
-   **Escopo:** Matriz de provas, camadas de verificação (estática, unit, interação, e2e, mobile, acessibilidade), protocolo PASS/FAIL/BLOCKED e meta de 90% na primeira revisão (AESDS 06).

---

[METADADOS_SISTEMA]

ID_FONTE: TST-002

TITULO_CANONICO: TST-002 Especificação de Testes e Verificação AESDS 06

FILE_ID: 15xvEXOZZ5C-vnq1w3E1kyfmw92hqAJTV

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Requisitos e Testes

SUBCATEGORIA: Matriz de Provas & Verificação

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Matriz de provas, camadas de verificação (estática, unit, interação, e2e, mobile, acessibilidade), protocolo PASS/FAIL/BLOCKED e meta de 90% na primeira revisão (AESDS 06)

[FIM_METADADOS]

---

# TST-002 — Especificação de Testes e Verificação (AESDS 06)



## 7.4. TST-003 — Auditoria de Fidelidade de Escopo (SFA-20260906-001)

-   **Arquivo no Drive:** SFA-20260906-001 — Auditoria de Fidelidade de Escopo — Execução Inicial.docx
-   **File ID:** 18JOrD9Kjk7Uvgt8iPlb8xRI9mGIOM69q
-   **Aplicação:** Insira no topo da primeira página do relatório de auditoria de escopo.
-   **Escopo:** Relatório de auditoria e verificação de fidelidade dos nove resultados desejados do projeto contra o inventário de fontes.

---

[METADADOS_SISTEMA]

ID_FONTE: TST-003

TITULO_CANONICO: TST-003 Auditoria de Fidelidade de Escopo SFA 001

FILE_ID: 18JOrD9Kjk7Uvgt8iPlb8xRI9mGIOM69q

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Requisitos e Testes

SUBCATEGORIA: Compliance & Auditoria de Escopo

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Relatório de auditoria e verificação de fidelidade dos nove resultados desejados do projeto contra o inventário de fontes

[FIM_METADADOS]

---

# TST-003 — SFA-20260906-001 — Auditoria de Fidelidade de Escopo



## 7.5. TST-004 — Validation Scenarios

-   **Arquivo no Drive:** 10-VALIDATION-SCENARIOS.md
-   **File ID:** 1eREzIAuQS4trIPX-PcBHnZ-oY7JqVfdR
-   **Aplicação:** Insira no topo do catálogo de cenários de validação.
-   **Escopo:** Catálogo de cenários arquiteturais persistentes, testes adversariais, exceções, testes contrafactuais e regressão (VAL-001+).

---

[METADADOS_SISTEMA]

ID_FONTE: TST-004

TITULO_CANONICO: TST-004 Validation Scenarios

FILE_ID: 1eREzIAuQS4trIPX-PcBHnZ-oY7JqVfdR

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Requisitos e Testes

SUBCATEGORIA: Cenários e Testes de Regressão

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Catálogo de cenários arquiteturais persistentes, testes adversariais, exceções, testes contrafactuais e regressão (VAL-001+)

[FIM_METADADOS]

---

# TST-004 — Validation Scenarios

## 8. Planejamento Estratégico e Procedimentos Operacionais (PLN-* / MAN-*)

## Metadados padronizados para aplicação no cabeçalho dos documentos de Planejamento e Procedimentos Operacionais (PLN-* / MAN-*). Copie o bloco correspondente e insira-o na primeira linha do arquivo-alvo.

## 8.1. PLN-001 — Roadmap de Implementação dos Dashboards

-   **Arquivo no Drive:** [ATIVO] Roadmap de Implementação dos Dashboards v2.3.docx
-   **Aplicação:** Insira no topo do documento de roadmap de dashboards.
-   **Escopo:** Cronograma de implementação, marcos de evolução e priorização dos painéis e dashboards operacionais.

---

[METADADOS_SISTEMA]

ID_FONTE: PLN-001

TITULO_CANONICO: PLN-001 Roadmap de Implementação dos Dashboards

STATUS: RASCUNHO

VERSAO: v2.3.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Planejamento

SUBCATEGORIA: Entregas & Dashboards

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Cronograma de implementação, marcos de evolução e priorização dos painéis e dashboards operacionais

[FIM_METADADOS]

---

# PLN-001 — Roadmap de Implementação dos Dashboards



## 8.2. PLN-002 — Roadmap e Grafo de Dependências de Tarefas (AESDS 04)

-   **Arquivo no Drive:** 04 — ROADMAP E GRAFO DE DEPENDÊNCIAS DE TAREFAS — AESDS — CEPRAEA BEACH PRO.docx
-   **Aplicação:** Insira no topo da primeira página do Roadmap e Grafo (AESDS 04).
-   **Escopo:** Sequenciamento de entregas, mapeamento de precedências, ordens de execução e critérios de prontidão por vertical slice (AESDS 04).

---

[METADADOS_SISTEMA]

ID_FONTE: PLN-002

TITULO_CANONICO: PLN-002 Roadmap e Grafo de Tarefas AESDS 04

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Planejamento

SUBCATEGORIA: Grafo de Dependências & Vertical Slices

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Sequenciamento de entregas, mapeamento de precedências, ordens de execução e critérios de prontidão por vertical slice (AESDS 04)

[FIM_METADADOS]

---

# PLN-002 — Roadmap e Grafo de Dependências de Tarefas (AESDS 04)



## 8.3. PLN-003 — Fluxo Completo de Desenvolvimento

-   **Arquivo no Drive:** [ATIVO] Fluxo Completo de Desenvolvimento v1.0.docx
-   **Aplicação:** Insira no topo do documento de Fluxo Completo de Desenvolvimento.
-   **Escopo:** Mapeamento ponta a ponta do ciclo de desenvolvimento humano-agente, do planejamento à homologação.

---

[METADADOS_SISTEMA]

ID_FONTE: PLN-003

TITULO_CANONICO: PLN-003 Fluxo Completo de Desenvolvimento

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Planejamento

SUBCATEGORIA: Ciclo de Vida & SDLC

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Mapeamento ponta a ponta do ciclo de desenvolvimento humano-agente, do planejamento à homologação

[FIM_METADADOS]

---

# PLN-003 — Fluxo Completo de Desenvolvimento



## 8.4. MAN-001 — Manual Operacional CEPRAEA Beach Pro

-   **Arquivo no Drive:** [ATIVO] Manual Operacional v1.0.docx
-   **Aplicação:** Insira no topo do Manual Operacional do sistema.
-   **Escopo:** Guia de operação da equipe, uso da aplicação por atletas e comissão técnica e procedimentos do dia a dia.

---

[METADADOS_SISTEMA]

ID_FONTE: MAN-001

TITULO_CANONICO: MAN-001 Manual Operacional CEPRAEA Beach Pro

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Procedimentos

SUBCATEGORIA: Runbook & Manual de Operação

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Guia de operação da equipe, uso da aplicação por atletas e comissão técnica e procedimentos do dia a dia

[FIM_METADADOS]

---

# MAN-001 — Manual Operacional CEPRAEA Beach Pro



## 8.5. MAN-002 — Protocolo de Execução e Review dos Agentes (AESDS 07)

-   **Arquivo no Drive:** 07 — PROTOCOLO DE EXECUÇÃO E REVIEW DOS AGENTES — AESDS — CEPRAEA BEACH PRO.docx
-   **Aplicação:** Insira no topo da primeira página do Protocolo de Execução e Review (AESDS 07).
-   **Escopo:** Regras de execução para o Executor, protocolo de freeze para o Reviewer, regras de stop condition e handoff entre sessões (AESDS 07).

---

[METADADOS_SISTEMA]

ID_FONTE: MAN-002

TITULO_CANONICO: MAN-002 Protocolo de Execução e Review dos Agentes AESDS 07

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Procedimentos

SUBCATEGORIA: Operação Agêntica & Handoff

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Regras de execução para o Executor, protocolo de freeze para o Reviewer, regras de stop condition e handoff entre sessões (AESDS 07)

[FIM_METADADOS]

---

# MAN-002 — Protocolo de Execução e Review dos Agentes (AESDS 07)



## 8.6. MAN-003 — Índice de Runbooks e Estado Operacional (AESDS 09)

-   **Arquivo no Drive:** 09 — ÍNDICE DE RUNBOOKS E ESTADO OPERACIONAL — AESDS — CEPRAEA BEACH PRO.docx
-   **File ID:** 1QrA82AnyJdInWFuRCYAnTlTOoAz-fAfD
-   **Aplicação:** Insira no topo da primeira página do Índice de Runbooks (AESDS 09).
-   **Escopo:** Roteador de procedimentos repetíveis, consulta ao estado operacional no Git/GitHub e regras para inicialização de sessões de agentes (AESDS 09).

---

[METADADOS_SISTEMA]

ID_FONTE: MAN-003

TITULO_CANONICO: MAN-003 Índice de Runbooks e Estado Operacional AESDS 09

FILE_ID: 1QrA82AnyJdInWFuRCYAnTlTOoAz-fAfD

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Procedimentos

SUBCATEGORIA: Roteamento Operacional & Runbooks

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Roteador de procedimentos repetíveis, consulta ao estado operacional no Git/GitHub e regras para inicialização de sessões de agentes (AESDS 09)

[FIM_METADADOS]

---

# MAN-003 — Índice de Runbooks e Estado Operacional (AESDS 09)

## 9. Engenharia de Dados, Referências e Prompts (DAT-* / REF-* / PRM-*)

## Metadados padronizados para aplicação no cabeçalho dos documentos de Dados, Referências e Prompts (DAT-* / REF-* / PRM-*). Copie o bloco correspondente e insira-o na primeira linha do arquivo-alvo.

## 9.1. DAT-001 — CEPRAEA Database SSOT

-   **Arquivo no Drive:** [ATIVO] CEPRAEA DATABASE SSOT v1.0.xlsx
-   **Aplicação:** Insira na primeira aba ou no cabeçalho de documentação da planilha SSOT.
-   **Escopo:** Fonte de verdade operacional dos dados da equipe, atletas, eventos, presenças e avaliações.

---

[METADADOS_SISTEMA]

ID_FONTE: DAT-001

TITULO_CANONICO: DAT-001 CEPRAEA Database SSOT

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Dados

SUBCATEGORIA: Planilha Canônica e Dados Operacionais

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Fonte de verdade operacional dos dados da equipe, atletas, eventos, presenças e avaliações

[FIM_METADADOS]

---

# DAT-001 — CEPRAEA DATABASE SSOT



## 9.2. DAT-002 — Modelagem do Banco PostgreSQL Supabase

-   **Arquivo no Drive:** [ATIVO] Modelagem do Banco CEPRAEA v1.0.docx
-   **Aplicação:** Insira no topo da primeira página do documento de modelagem relacional.
-   **Escopo:** Modelagem física de tabelas, relacionamentos, chaves estrangeiras, políticas RLS e funções do banco Supabase.

---

[METADADOS_SISTEMA]

ID_FONTE: DAT-002

TITULO_CANONICO: DAT-002 Modelagem do Banco PostgreSQL Supabase

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Dados

SUBCATEGORIA: Schema Físico e RLS

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Modelagem física de tabelas, relacionamentos, chaves estrangeiras, políticas RLS e funções do banco Supabase

[FIM_METADADOS]

---

# DAT-002 — Modelagem do Banco PostgreSQL Supabase



## 9.3. DAT-003 — Plano Mestre do Banco de Dados PWA

-   **Arquivo no Drive:** CEPRAEA-DB.docx
-   **File ID:** 1FKOk0-lhgdnlTOAsjdCBuzf97_2gRp3v
-   **Aplicação:** Insira no topo da primeira página do Plano Mestre do Banco de Dados.
-   **Escopo:** Plano congelado de ações para criação, migração e controle semântico-operacional do banco de dados do PWA.

---

[METADADOS_SISTEMA]

ID_FONTE: DAT-003

TITULO_CANONICO: DAT-003 Plano Mestre do Banco de Dados PWA

FILE_ID: 1FKOk0-lhgdnlTOAsjdCBuzf97_2gRp3v

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Dados

SUBCATEGORIA: Plano de Migração e Engenharia de Dados

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Plano congelado de ações para criação, migração e controle semântico-operacional do banco de dados do PWA

[FIM_METADADOS]

---

# DAT-003 — CEPRAEA-DB — Plano Mestre para Criação do Banco de Dados do PWA



## 9.4. DAT-004 — Glossário de Dados CEPRAEA

-   **Arquivo no Drive:** Glossário de Dados — CEPRAEA v0.1.xlsx
-   **File ID:** 1sm_pHLoSIjWXzTQHAKxKZp22yYqx6Y2L
-   **Aplicação:** Insira no topo da aba de definições ou na aba do Glossário.
-   **Escopo:** Definição normalizada dos 30 campos, tipos semânticos, privacidade, fontes autoritativas e regras do glossário de dados.

---

[METADADOS_SISTEMA]

ID_FONTE: DAT-004

TITULO_CANONICO: DAT-004 Glossário de Dados CEPRAEA

FILE_ID: 1sm_pHLoSIjWXzTQHAKxKZp22yYqx6Y2L

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Dados

SUBCATEGORIA: Dicionário e Taxonomia de Dados

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Definição normalizada dos 30 campos, tipos semânticos, privacidade, fontes autoritativas e regras do glossário de dados

[FIM_METADADOS]

---

# DAT-004 — Glossário de Dados CEPRAEA



## 9.5. REF-001 — Catálogo de Referências e Protocolo de Pesquisa (AESDS 08)

-   **Arquivo no Drive:** 08 — CATÁLOGO DE REFERÊNCIAS E PROTOCOLO DE PESQUISA — AESDS — CEPRAEA BEACH PRO.docx
-   **Aplicação:** Insira no topo da primeira página do Catálogo de Referências (AESDS 08).
-   **Escopo:** Protocolo de pesquisa técnica, consulta a documentações oficiais, padrões e catálogo de referências externas (AESDS 08).

---

[METADADOS_SISTEMA]

ID_FONTE: REF-001

TITULO_CANONICO: REF-001 Catálogo de Referências e Pesquisa AESDS 08

STATUS: RASCUNHO

VERSAO: v0.1.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Pesquisa e Referências

SUBCATEGORIA: Catálogo de Fontes e Protocolos

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Protocolo de pesquisa técnica, consulta a documentações oficiais, padrões e catálogo de referências externas (AESDS 08)

[FIM_METADADOS]

---

# REF-001 — Catálogo de Referências e Protocolo de Pesquisa (AESDS 08)



## 9.6. REF-002 — Relatório de Pesquisa: Padrões Sintáticos do EARS

-   **Arquivo no Drive:** DOC-005 — Relatório de Pesquisa_ Padrões Sintáticos do EARS.docx
-   **File ID:** 133QjenL7BlD-ydfUHnonsoCEp-SzYXWs
-   **Aplicação:** Insira no topo da primeira página do relatório de pesquisa sobre EARS.
-   **Escopo:** Mapeamento dos 5 padrões sintáticos do EARS para especificação sem ambiguidade em Spec-Driven Development.

---

[METADADOS_SISTEMA]

ID_FONTE: REF-002

TITULO_CANONICO: REF-002 Relatório de Pesquisa Padrões EARS

FILE_ID: 133QjenL7BlD-ydfUHnonsoCEp-SzYXWs

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Pesquisa e Referências

SUBCATEGORIA: Pesquisa de Requisitos & EARS Syntax

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Mapeamento dos 5 padrões sintáticos do EARS para especificação sem ambiguidade em Spec-Driven Development

[FIM_METADADOS]

---

# REF-002 — Relatório de Pesquisa: Padrões Sintáticos do EARS



## 9.7. REF-003 — Benchmark Visual UX/UI dos Dashboards

-   **Arquivo no Drive:** CEPRAEA — Benchmark Visual UX_UI dos Dashboards.pptx
-   **File ID:** 17eL1JqkbliCqezp7CvZC1JZh4s-naU79
-   **Aplicação:** Insira nas notas da apresentação ou no primeiro slide de especificação visual.
-   **Escopo:** Análise comparativa de 15 screenshots de produtos esportivos e diretrizes de UI/UX do Design System CEPRAEA.

---

[METADADOS_SISTEMA]

ID_FONTE: REF-003

TITULO_CANONICO: REF-003 Benchmark Visual UX UI dos Dashboards

FILE_ID: 17eL1JqkbliCqezp7CvZC1JZh4s-naU79

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Pesquisa e Referências

SUBCATEGORIA: Design System & Referências Visuais

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Análise comparativa de 15 screenshots de produtos esportivos e diretrizes de UI/UX do Design System CEPRAEA

[FIM_METADADOS]

---

# REF-003 — CEPRAEA — Benchmark Visual UX/UI dos Dashboards



## 9.8. REF-004 — Inventário Auditável das 71 Fontes

-   **Arquivo no Drive:** [ATIVO] Inventário Auditável de Fontes v1.0.csv
-   **Aplicação:** Insira no cabeçalho das notas ou no topo da planilha/CSV de inventário de fontes.
-   **Escopo:** Inventário consolidado e auditável das 71 fontes bibliográficas, normativas e técnicas utilizadas no projeto.

---

[METADADOS_SISTEMA]

ID_FONTE: REF-004

TITULO_CANONICO: REF-004 Inventário Auditável das 71 Fontes

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Pesquisa e Referências

SUBCATEGORIA: Mapeamento e Rastreabilidade de Fontes

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Inventário consolidado e auditável das 71 fontes bibliográficas, normativas e técnicas utilizadas no projeto

[FIM_METADADOS]

---

# REF-004 — Inventário Auditável das 71 Fontes



## 9.9. REF-010 — Relatório Executivo e de Governança (Agosto 2026)

-   **Arquivo no Drive:** CEPRAEA_Beach_Pro_Relatorio_Executivo_Agosto_2026.pdf
-   **File ID:** 1Zx5yYc5MKkUk5c2131HIdlu7tjQs2_HO
-   **Aplicação:** Insira no cabeçalho de metadados do relatório executivo.
-   **Escopo:** Síntese executiva da operação esportiva, disponibilidade, SDLC agêntico, formal verification e próximos gates (Agosto 2026).

---

[METADADOS_SISTEMA]

ID_FONTE: REF-010

TITULO_CANONICO: REF-010 Relatório Executivo e de Governança

FILE_ID: 1Zx5yYc5MKkUk5c2131HIdlu7tjQs2_HO

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Pesquisa e Referências

SUBCATEGORIA: Relatórios Executivos & Governança

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Síntese executiva da operação esportiva, disponibilidade, SDLC agêntico, formal verification e próximos gates (Agosto 2026)

[FIM_METADADOS]

---

# REF-010 — CEPRAEA BEACH PRO — Relatório Executivo e de Governança (Agosto 2026)



## 9.10. PRM-001 — Prompts de Abertura dos Chats

-   **Arquivo no Drive:** 09-CHAT-OPENING-PROMPTS.md
-   **File ID:** 183Uo9NOEKbBvJx-w8NUMh0JZjlDYhsEm
-   **Aplicação:** Insira no topo do arquivo de prompts de abertura dos chats.
-   **Escopo:** Prompts estruturados para abertura de chats especializados (Intake, Elicitação, Auditoria, Requisitos, Readiness).

---

[METADADOS_SISTEMA]

ID_FONTE: PRM-001

TITULO_CANONICO: PRM-001 Prompts de Abertura dos Chats

FILE_ID: 183Uo9NOEKbBvJx-w8NUMh0JZjlDYhsEm

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Prompts e Agentes

SUBCATEGORIA: Prompts de Elicitação e Inicialização

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Prompts estruturados para abertura de chats especializados (Intake, Elicitação, Auditoria, Requisitos, Readiness)

[FIM_METADADOS]

---

# PRM-001 — Prompts de Abertura dos Chats



## 9.11. PRM-002 — Instruções do Projeto (Protocolo de Engenharia Assistida por IA)

-   **Arquivo no Drive:** 01-PROJECT-INSTRUCTIONS.md
-   **File ID:** 1D1-UdDpIVB7emaVW56Oqmy5d0oebMVnG
-   **Aplicação:** Insira no topo das instruções do projeto.
-   **Escopo:** Regras fundamentais, protocolo de elicitação, estratégia de perguntas, controle de genericidade e critérios de avanço para IA.

---

[METADADOS_SISTEMA]

ID_FONTE: PRM-002

TITULO_CANONICO: PRM-002 Instruções do Projeto e Protocolo Agêntico

FILE_ID: 1D1-UdDpIVB7emaVW56Oqmy5d0oebMVnG

STATUS: RASCUNHO

VERSAO: v1.0.0

DOMINIO_PROPRIETARIO: davisermenho@handballtrack.app

CATEGORIA: Prompts e Agentes

SUBCATEGORIA: Instruções de Sistema e Protocolo de Engenharia

DATA_HOMOLOGACAO: 2026-10-11

AUTORIDADE: Davi Sermenho

ESCOPO: Regras fundamentais, protocolo de elicitação, estratégia de perguntas, controle de genericidade e critérios de avanço para IA

[FIM_METADADOS]

---

# PRM-002 — Instruções do Projeto — Protocolo de Engenharia Assistida por IA

