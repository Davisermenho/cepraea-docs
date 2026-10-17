**Sessoes Claude Code e Codex**

Sessões Claude Code e Codex

# Resumo Executivo

Este documento detalha como ferramentas de linha de comando (CLI) e extensões de código utilizam métodos de autenticação web para permitir o uso de planos por assinatura (como Claude Pro/Max e ChatGPT Plus), evitando os custos diretos das APIs tradicionais.

-   **Claude Code:** Processo automatizado via fluxo **OAuth 2.0 com PKCE**, gerenciando a autenticação pelo navegador e armazenando tokens localmente para renovação contínua.
-   **ChatGPT / Codex:** Integração via extração manual de **cookies de sessão** (*__Secure-next-auth.session-token*), injetados no editor para emular interações web legítimas.

# 1. Claude Code (Anthropic CLI)

## Fluxo de Autenticação Web (OAuth 2.0 PKCE / Browser Handoff)

O **Claude Code** (CLI oficial da Anthropic) permite a utilização de assinaturas pessoais (Claude Pro e Claude Max) sem a necessidade de chaves de API pagas (*ANTHROPIC_API_KEY*).

### Passo a Passo de Autenticação

1.  **Início do Fluxo:** Ao executar *claude* ou *claude auth login* no terminal, o CLI inicia um servidor HTTP local de callback e abre o navegador redirecionando para o portal de login ([claude.ai](https://claude.ai) ou [platform.claude.com](https://platform.claude.com)).
2.  **Mecanismo PKCE:** Utiliza **OAuth 2.0 com PKCE** (Proof Key for Code Exchange), garantindo que o código de autorização retornado no navegador só possa ser trocado por tokens pelo próprio processo CLI local.
3.  **Fallback (Ambientes Sem Navegador):** Em ambientes remotos, Docker, WSL2 ou conexões SSH, use a opção *--no-browser* ou copie o código de autorização exibido na tela do navegador para colar manualmente no terminal.

### Armazenamento e Renovação de Tokens

-   **Persistência Local:** Após aprovação, o CLI recebe o *access_token* e o *refresh_token*, gravando-os em *~/.claude/.credentials.json* ou no cofre do sistema (macOS Keychain / Linux Secret Service).
-   **Renovação Transparente:** Quando o *access_token* expira, a CLI renova o acesso automaticamente usando o *refresh_token*, sem reabrir o navegador.
-   **Variáveis de Ambiente:** O token OAuth pode ser injetado via *CLAUDE_CODE_OAUTH_TOKEN*, ideal para automações (Google Colab, pipelines CI/CD).

# 2. Codex / Extensões VS Code para ChatGPT Plus

## Autenticação por Session Tokens (__Secure-next-auth.session-token)

Para utilizar planos pagos como o **ChatGPT Plus** no VS Code sem custos de API da OpenAI ([platform.openai.com](https://platform.openai.com)), extensões utilizam tokens de sessão web.

### Passo a Passo de Configuração

1.  **Captura do Cookie:** Faça login em sua conta no ChatGPT ([chatgpt.com](https://chatgpt.com) ou [chat.openai.com](https://chat.openai.com)). Abra as Ferramentas do Desenvolvedor (F12 > Application > Cookies) e copie o valor de *__Secure-next-auth.session-token*.
2.  **Injeção na Extensão:** Cole o valor do cookie nas configurações da extensão no VS Code (*settings.json*).

### Comunicação e Limitações

-   **Emulação de Navegador:** As chamadas usam endpoints internos (ex: */backend-api/conversation*) em vez da API pública (*/v1/chat/completions*).
-   **Gerenciamento de Contexto:** A extensão envia *conversation_id* e *parent_message_id* para manter o histórico da conversa.
-   **Expiração:** Como os cookies expirarem ou são invalidados ao fazer logout, é necessária atualização periódica do token.

# Resumo Comparativo

| **Característica** | **Claude Code (Anthropic)** | **Codex / VS Code (ChatGPT)** |
| --- | --- | --- |
| **Método de Autenticação** | OAuth 2.0 PKCE / Browser Handoff | Cookie de Sessão Web |
| --- | --- | --- |
| **Credencial Utilizada** | Access Token e Refresh Token | __Secure-next-auth.session-token |
| --- | --- | --- |
| **Configuração** | Automatizada via terminal / navegador | Manual (DevTools > settings.json) |
| --- | --- | --- |
| **Renovação** | Automática via refresh_token | Manual após expiração do cookie |
| --- | --- | --- |
| **Endpoint** | Portal de Autenticação Anthropic | Backend interno (/backend-api) |
| --- | --- | --- |

# Mapa de Navegação das Fontes

[Um Modelo de Especificação para a Era do Desenvolvimento de Software Guiado por IA](?tab=t.0#heading=h.df9l6p2t843c)

[Guia do Modelo ANMS (Specification-Driven Development)](?tab=t.j2x06nwefqq5)

[Relatório de Pesquisa: Padrões Sintáticos do EARS](?tab=t.c9d5v1li2i3h)

Sessões Claude Code e Codex → Você está aqui

[Guia de Fontes e Introdução ao EARS](?tab=t.fysxtsu3meds)

[claudecode-rules.md](?tab=t.8gg0j8f3wd99)