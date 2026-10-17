# Ambiente de DEsenvolvimento

Para estruturar um ambiente de desenvolvimento de alta performance que una **isolamento em contêiner Docker**, **integração com o VS Code e ferramentas de IA (Claude Code / Codex / Continue)** e **contexto frugal** (otimizado para evitar o desperdício de tokens), a melhor abordagem é criar um *boilerplate* padronizado diretamente na raiz do seu projeto.

Abaixo está o guia prático com todos os arquivos de configuração necessários para você copiar e colar no seu repositório.

---

## Estrutura de Arquivos Gerada na Raiz do Projeto

```text
seu-projeto/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .aiignore                 <-- Garante o contexto frugal (bloqueia lixo e builds)
├── .clinerules / CLAUDE.md   <-- Instruções comportamentais e de arquitetura para a IA
└── docker-compose.yml        <-- Orquestração opcional para serviços de apoio

```

---

## 1. O Motor de Isolamento `.devcontainer/Dockerfile`

Este arquivo define o ambiente de desenvolvimento completo dentro do contêiner, pré-instalando o Node.js, Python, Git e a ferramenta de linha de comando do Claude Code, além de ferramentas de produtividade.

```dockerfile
FROM mcr.microsoft.com/devcontainers/base:debian12

# Instala pacotes essenciais do sistema, git, curl e ferramentas de build
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive 
    && apt-get -y install --no-install-recommends 
    git 
    curl 
    build-essential 
    ripgrep 
    jq 
    && rm -rf /var/lib/apt/lists/*

# Instalação global do Claude Code (CLI da Anthropic)
RUN npm install -g @anthropic-ai/claude-code

# Configura o usuário padrão (geralmente 'vscode' nas imagens Microsoft)
USER vscode

# Define diretório de trabalho padrão
WORKDIR /workspace
```

---

## 2. A Ponte com o Editor: `.devcontainer/devcontainer.json`

Este arquivo configura o VS Code para abrir automaticamente dentro do contêiner Docker, injetando as extensões necessárias para o Claude Code, GitHub Copilot (Codex) e Continue.

```json
{
  "name": "AI-Assisted Frugal DevEnv",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "saoudrizwan.claude-dev",      // Extensão Cline (Claude Dev) para VS Code
        "continue.continue",          // Continue.dev (suporte a Claude, Codex e locais)
        "GitHub.copilot",             // GitHub Copilot / Codex
        "eamodio.gitlens",            // GitLens para rastreabilidade de código
        "ms-python.python"            // Suporte a Python (ajustar conforme sua stack)
      ],
      "settings": {
        "terminal.integrated.defaultProfile.linux": "bash",
        "editor.formatOnSave": true
      }
    }
  },
  "remoteUser": "vscode",
  "postCreateCommand": "echo 'Ambiente de desenvolvimento com IA inicializado com sucesso!'"
}
```

---

## 3. A Arquitetura de Contexto Frugal: `.aiignore`

Assim como o `.gitignore`, este arquivo impede que agentes de IA percam tokens preciosos indexando diretórios de dependências, artefatos gerados ou arquivos de dados pesados.

```text
# Dependências e Ambientes Virtuais
node_modules/
.venv/
venv/
target/
dist/
build/

# Logs e Dados Locais
*.log
logs/
data/
*.sqlite
*.db

# Artefatos de Build e Cache
.cache/
.turbo/
.next/
__pycache__/
.pytest_cache/

```

---

## 4. O Manual do Agente: `AGENTS.md`

Colocado na raiz do projeto, este arquivo funciona como o mapa de arquitetura de baixíssimo custo de tokens. Quando o Claude Code ou o Cline inicia, ele lê apenas este arquivo para entender as regras do projeto, impedindo que precise escanear a árvore inteira.

```markdown
# Diretrizes do Projeto para Agentes de IA

## Visão Geral
Este repositório utiliza arquitetura modular com isolamento em contêineres. O objetivo é manter máxima concisão e acoplamento frouxo.

## Comandos Essenciais (Não execute testes globais pesados)
- **Testes Unitários:** Rodar exclusivamente o arquivo alterado (ex: `pytest tests/test_modulo.py`)
- **Lint / Formatação:** `npm run lint` ou equivalente da stack.

## Regras de Contexto Frugal
1. **Busca Cirúrgica:** Utilize `ripgrep` (`grep`) para localizar símbolos ou funções antes de abrir arquivos inteiros.
2. **Escopo Restrito:** Edite apenas os arquivos estritamente necessários para a tarefa solicitada.
3. **Evite Leituras Massivas:** Nunca solicite o conteúdo de diretórios inteiros de dependências ou logs.
4. **Respostas Diretas:** Ao explicar alterações, seja conciso e foque no diff técnico.
```

---

## Como aplicar agora no seu fluxo

1. Crie uma pasta chamada `.devcontainer/` na raiz do seu projeto.
2. Cole os códigos do `Dockerfile` e do `devcontainer.json` dentro dela.
3. Crie os arquivos `.aiignore` e `CLAUDE.md` diretamente na raiz.
4. Abra o projeto no VS Code e clique na notificação que aparecerá no canto inferior direito: **"Reopen in Container"**.

Dessa forma, seu editor, o isolamento Docker e o controle rigoroso de tokens operam de maneira totalmente integrada.
