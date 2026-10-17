CATÁLOGO DE REFERÊNCIAS E PROTOCOLO DE PESQUISA — CEPRAEA BEACH PRO

AESDS 08 — Fundação v0.1

1. OBJETIVO

Fazer os agentes encontrarem referências técnicas e visuais de alta qualidade quando Davi precisar decidir, sem permitir que exemplos externos sejam copiados sem avaliação ou convertidos em autoridade do CEPRAEA.

2. REGRA CENTRAL

REFERÊNCIA -> EVIDÊNCIA OBSERVADA -> APLICABILIDADE -> TRADE-OFFS -> OPÇÕES -> DECISÃO HUMANA.

Referência não é requisito. Popularidade não é prova. Código em produção não garante adequação ao CEPRAEA.

3. HIERARQUIA DE FONTES

Nível A — fonte normativa/primária: documentação oficial, especificação, standard, repositório oficial.

Nível B — implementação de referência: projeto open source maduro e verificável, preferencialmente com produção/testes/documentação.

Nível C — especialista reconhecido: material técnico/UX especializado usado para interpretação e prática.

Nível D — inspiração visual: produto, galeria, case ou screenshot; serve para comparação visual, nunca como fonte de regra.

4. FONTES TÉCNICAS PRIMÁRIAS INICIAIS

Revalidar no momento do uso:

- React — documentação oficial react.dev;

- TypeScript — documentação oficial typescriptlang.org;

- W3C/WAI — WCAG e materiais oficiais de acessibilidade;

- Supabase — documentação oficial de Auth, RLS, Data API e React;

- web.dev — referência técnica para PWA/capacidades web;

- documentação oficial do navegador/API quando a feature depender de suporte específico;

- documentação oficial da biblioteca efetivamente adotada.

5. FONTES DE DESIGN E INTERAÇÃO

- Apple Human Interface Guidelines: referência de padrões, ergonomia e componentes de ecossistema mobile;

- Material Design: referência de padrões e componentes, sem obrigação de adotar a estética Material;

- W3C/WAI: acessibilidade e critérios verificáveis;

- design systems open source de produtos maduros quando houver relação real com o problema.

O agente deve buscar referências multiplataforma quando a decisão não for específica de iOS/Android.

6. TESTES E QUALIDADE

Testing Library é referência para testes orientados à forma como o usuário utiliza a interface. O agente deve priorizar fontes oficiais da stack e verificar versão/contexto antes de aplicar exemplo externo.

7. PESQUISA EM GITHUB

Ao buscar repositório open source, registrar:

- URL/repositório;

- licença;

- atividade/manutenção;

- stack e versão relevante;

- arquivo/pasta exata observada;

- comportamento/arquitetura comprovada;

- testes existentes;

- diferença de escala/domínio para o CEPRAEA;

- o que pode ser reutilizado como padrão;

- o que NÃO deve ser copiado;

- risco de cargo cult.

Separar sempre:

FATO OBSERVADO NO REPO

INFERÊNCIA DO AGENTE

RECOMENDAÇÃO PARA O CEPRAEA

8. PESQUISA VISUAL

Para decisões de UI, trazer preferencialmente 2–4 referências distintas e comparáveis. Informar qual aspecto observar: navegação, hierarquia, densidade, formulário, status, feedback, cards, timeline, calendário, motion, vazio, erro ou outro.

Não pedir ao humano para escolher entre referências sem explicar o impacto funcional e técnico de cada opção.

9. FORMATO CANÔNICO DE OPÇÕES

DECISÃO NECESSÁRIA

Critério que diferencia as opções

OPÇÃO A

Fonte/referência

Padrão observado

Vantagens

Desvantagens

Impacto mobile

Impacto técnico

Acessibilidade

Custo/retrabalho

Aplicabilidade ao CEPRAEA

OPÇÃO B / C / D

mesmos campos

RECOMENDAÇÃO DO AGENTE

Separada das evidências, com justificativa.

DECISÃO HUMANA

Pendente até escolha explícita.

10. QUANDO PESQUISAR

Pesquisar quando: tecnologia/standard atual é relevante; decisão material possui alternativas; usuário pede exemplos; existe risco de reinventar solução madura; implementação depende de API/biblioteca atual; referência visual facilita escolha.

11. QUANDO NÃO PESQUISAR

Não pesquisar por hábito para detalhe local óbvio, para justificar decisão já homologada ou para adicionar tecnologia não necessária.

12. REGRAS CONTRA CARGO CULT

- entender o problema resolvido pela referência;

- comparar contexto e restrições;

- não copiar arquitetura inteira por semelhança superficial;

- não copiar código sem licença e compatibilidade;

- não adotar dependência apenas porque projeto famoso usa;

- validar comportamento no contexto CEPRAEA.

13. CATÁLOGO VIVO

Este documento define o protocolo. Referências concretas selecionadas para decisões do projeto devem ser adicionadas com: tema, tipo, data de verificação, fonte, aplicabilidade, decisão associada e status ADOTADA/REJEITADA/REFERÊNCIA.

14. DONE DA PESQUISA

Pesquisa está pronta quando existem opções suficientes para uma decisão informada, fontes são verificáveis, evidência está separada de inferência e a recomendação não foi tratada como decisão humana.