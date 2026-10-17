# DECISÕES DO RESPONSÁVEL PELO PROJETO CEPRAEA BEACH PRO

## DECISÃO 1 — Autoridade e vigência documental

Decido:

- Nenhum documento será considerado aprovado ou vigente apenas por seu nome, conteúdo ou indicação `[ATIVO]`.
- A Constituição terá precedência normativa sobre o Current State Index, exclusivamente após aprovação formal da versão correspondente.
- O Current State Index terá função de registro e consulta, sem autoridade para aprovar documentos.
- Adoto um registro único de aprovação, vinculado a identificador, versão, SHA-256, responsável e data de vigência.
- As versões atualmente conflitantes permanecem `AGUARDANDO_APROVACAO`. Sua aprovação dependerá da identificação e apresentação das versões exatas.
- Não haverá vigência retroativa presumida.

Fundamento declarado: divergências comprovadas entre os estados documentais; seção 1 do relatório.

## DECISÃO 2 — Regras de cancelamento D-5

Decido ratificar as seguintes regras:

- No checkpoint D-5, o cancelamento automático aplica-se exclusivamente às sessões em estado `PUBLICADO`, respeitadas as condições de cancelamento definidas para esse checkpoint.
- O cancelamento é terminal: a identidade da sessão cancelada não poderá ser reutilizada.
- Após a sessão alcançar `CONFIRMADO`, eventual perda de quórum não provocará cancelamento automático.
- Nesse caso, a decisão de manter ou cancelar a sessão será exclusivamente do treinador.
- Formulações anteriores incompatíveis ficam substituídas nesse escopo.

Fundamento declarado: PRD candidato, linhas 1104–1112; seção 4 do relatório.

## DECISÃO 3 — Requisitos e arquitetura do produto

Decido:

- O produto será orientado prioritariamente ao uso em dispositivos móveis, como PWA.
- Deverá contemplar os perfis de treinador e atleta, com autenticação e permissões adequadas.
- O orçamento operacional de referência será próximo de R$ 50 mensais, sujeito à verificação de viabilidade.
- O funcionamento conectado será a referência inicial. Funcionalidades offline completas e notificações push não serão consideradas obrigatórias sem necessidade funcional demonstrada.
- A arquitetura deverá privilegiar simplicidade operacional, manutenção por desenvolvedor único e aproveitamento do código existente.
- Não aprovo, neste momento, Next.js/Vercel nem React/Vite como arquitetura definitiva.
- A escolha dependerá da inspeção do repositório real e da comparação das alternativas segundo esses requisitos.

Fundamento declarado: PRD candidato, linhas 69, 80, 84, 664, 714, 726 e 820; seção 3 do relatório.

## DECISÃO 4 — Verificação da implementação e infraestrutura

Decido:

- Não reconhecer como comprovadas as declarações de implantação, testes aprovados ou infraestrutura pronta sem evidências técnicas verificáveis.
- Autorizar inspeção somente de leitura no repositório e no ambiente Supabase correspondente ao projeto.
- Autorizar testes reproduzíveis em ambiente local isolado, sem alterar dados ou serviços de produção.
- Adotar estados técnicos distintos: `GERADO`, `VALIDADO_ESTATICAMENTE`, `EXECUTADO_LOCALMENTE`, `IMPLANTADO_NO_ALVO`, `VERIFICADO_NO_ALVO` e `ACEITO_HUMANAMENTE`.
- Exigir evidências compatíveis com cada estado antes de reconhecer sua conclusão.
- Não autorizar implantação, alteração de banco de produção ou migração de dados sem nova aprovação expressa.

Fundamento declarado: relatório de execução, linhas 18 e 43; PRD candidato, linhas 832 e 903; seção 2 do relatório.

## DECISÃO 5 — Correção da segmentação documental

Decido autorizar:

- A correção do segmentador para preservar integralmente o conteúdo, inclusive trechos anteriores ao primeiro título Markdown.
- A implementação de validação de cobertura completa, sem lacunas ou sobreposições.
- A adoção de identificadores determinísticos para os segmentos, evitando renumerações desnecessárias.
- A criação e execução dos testes necessários à comprovação da correção.
- A reexecução versionada das etapas U02 e U03.
- A preservação integral dos resultados e evidências anteriores, sem sobrescrita.

A correção será considerada concluída somente quando os testes demonstrarem a reconstrução exata do conteúdo original e a consistência dos novos artefatos.

Fundamento declarado: `u02_extract.py`, linhas 445 e 500; teste T17; seção 5 do relatório.

## Determinação final

Fica autorizada a execução das atividades técnicas acima dentro dos limites estabelecidos.

As decisões de produto e governança aqui expressas não constituem aprovação automática de versões documentais não identificadas, nem atestado de funcionamento do sistema.

Não ficam autorizadas expansão de escopo, introdução de serviços adicionais, mudanças arquiteturais definitivas ou alterações em produção sem nova aprovação.

O trabalho deverá ser encerrado assim que os critérios de conclusão das atividades autorizadas forem satisfeitos, preservando as evidências produzidas.

## Metadados de captura

- Papel da autoridade: `RESPONSAVEL_PELO_PROJETO` (declarado diretamente pelo usuário).
- Meio: mensagem direta na sessão de execução.
- Data de registro: `2026-10-17`.
- Nível aplicável: `A2` para as decisões identificadas; não constitui `A3`.
- Publicação oficial autorizada: `não`.
