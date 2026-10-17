# Diretrizes Globais do Projeto para Agentes de IA (Codex, Claude, Cline)

## Repositório de Documentos

Este repositorio tem como objetivo produzir a documentação do CEPRAEA BEACH PRO. Todos os documentos são rascunhos e devem ser tratados como base par produção de novos documentos consolidados.

A documentação deve ser automatizada pelo puython.

## Contexto do Ambiente

- **Ambiente:** WSL2 (Ubuntu 24.04) integrado com Docker Desktop.
- **Diretório:** `/home/davis/cepraea-docs`
- **Ferramentas Nativas:** Node.js 24, Python 3.12, `rg` (ripgrep), `jq`, `git`, Docker.

## Regras de Contexto Frugal

1. **Busca Cirúrgica:** Utilize `rg` (ripgrep) para buscar símbolos ou funções antes de ler o arquivo todo.
2. **Escopo Restrito:** Edite estritamente os arquivos necessários.
3. **Leitura de Arquivos:** Respeite o `.aiignore`. Nunca leia diretórios de dependências ou caches.
4. **Respostas Diretas:** Ao explicar ações, foque no raciocínio técnico e no *diff* das alterações.
