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
