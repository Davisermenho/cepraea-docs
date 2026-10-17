Manual Operacional — CEPRAEA Beach Pro

Do legado ao software funcional

# FINALIDADE E MODO DE USO

Este manual ensina a transformar os arquivos do Google Drive, o conhecimento produzido com o NotebookLM e as fontes especializadas em documentação consumível por Codex e Claude Code, até obter funcionalidades do CEPRAEA BEACH PRO implementadas, verificadas e aceitas. Ele é destinado ao responsável pelo projeto, que conhece a equipe e está iniciando no desenvolvimento de software.

O percurso de trabalho é:

| **FLUXO DE TRABALHO SEQUENCIAL DE DESENVOLVIMENTO**  
**1. Reconhecer o ambiente**  
↓  
**2. Inventariar e preservar o legado**  
↓  
**3. Escolher uma necessidade**  
↓  
**4. Pesquisar o conhecimento necessário**  
↓  
**5. Definir e documentar o comportamento**  
↓  
**6. Entregar o contexto aos agentes**  
↓  
**7. Implementar**  
↓  
**8. Testar e validar**  
↓  
**9. Atualizar os documentos e continuar** |
| --- |

As pesquisas podem ocorrer em paralelo, e uma falha retorna à atividade responsável; não é necessário reiniciar todo o percurso.

Este manual orienta a operação. Não substitui as decisões humanas, a documentação técnica das ferramentas, as especificações do produto ou os controles já existentes no repositório. Não cria um novo sistema de governança, não exige documentação completa antes da primeira funcionalidade e não presume API paga de inferência, MCP ou integração automática entre NotebookLM e IDE.

**Como utilizar:** localize o procedimento correspondente à tarefa atual; confira suas entradas; execute as ações na ordem indicada; verifique o resultado; registre somente o que for necessário para continuar. Quando um procedimento mencionar uma capacidade ainda não testada no seu ambiente, execute primeiro a verificação indicada. Não transforme uma instrução sugerida por IA em autorização para alterar arquivos, dados ou configurações.

Convenções: [EXEMPLO] identifica valores ilustrativos; <VALOR> deve ser substituído por um valor real previamente confirmado; “confirmado no repositório” significa que o arquivo foi lido, não que o comando foi executado; “verificado localmente” exige saída observada no seu ambiente. Um resultado desconhecido não equivale a sucesso. Os prompts deste manual são instruções de trabalho, não mecanismos técnicos que garantem obediência.

# PONTO DE PARTIDA VERIFICADO

A leitura remota do repositório cepraea/beach-pro encontrou README.md, AGENT_POLICY.md, AGENTS.md, CLAUDE.md, .ai/control/README.md, .ai/decisions/INDEX.md e docs/operacao/agent-workflow.md. O README declara fundação local iniciada, dados exclusivamente sintéticos e ausência de autorização para migração real, piloto ou produção. As regras vigentes atribuem planejamento e execução a Claude Code, revisão independente a Codex e aprovação, Git privilegiado e release ao humano. A cópia local, o container e a execução dos controles não foram verificados nesta elaboração. Confirme o estado novamente antes de utilizá-lo.

# 1. COMEÇAR OU RETOMAR O TRABALHO

## 1.1 Reconhecer a pasta e o ambiente

**Objetivo:** descobrir onde está o projeto, qual estado está aberto e quais ferramentas realmente funcionam, sem recriar a fundação.

**Entrada:** VS Code, pasta existente do projeto e acesso ao repositório.

Procedimento:

1. Abra o VS Code e certifique-se de que ele esteja conectado à instância do WSL:Ubuntu. Use a opção Arquivo > Abrir Pasta para selecionar o diretório do projeto no ambiente Linux. Não utilize um caminho do Windows nem presuma que um diretório aberto anteriormente continue válido.

2. Se o projeto já utiliza Dev Container, verifique o indicador de ambiente do VS Code e a configuração .devcontainer. Use a Paleta de Comandos (Ctrl+Shift+P) e procure “Dev Containers: Reopen in Container” somente quando precisar abrir a configuração existente. Não reconstrua nem substitua o container antes de inspecionar seu estado. Em caso de falha, conserve o log e utilize o procedimento de recuperação da extensão.

3. Abra Terminal > Novo Terminal. Certifique-se de que o terminal esteja sendo executado no contexto do ambiente Linux (WSL:Ubuntu) e confirme que o diretório atual é a raiz do projeto. Execute os comandos de inspeção abaixo. Eles não modificam o repositório.

pwd



git rev-parse --show-toplevel



git status --short --branch



git branch --show-current



git log -1 --oneline



node --version



npm --version



4. Leia README.md, AGENT_POLICY.md, CLAUDE.md, AGENTS.md, .ai/control/README.md e .ai/decisions/INDEX.md. Examine .ai/control/control-plane.json, os runbooks relevantes e os scripts existentes. Confirme a branch, o commit, as alterações locais e os modos ativos. Não descarte alterações desconhecidas.

5. Verifique a disponibilidade de Docker e do container somente se a tarefa exigir serviços locais. Se precisar instalar ou corrigir uma ferramenta, obtenha uma proposta específica, avalie efeitos e custos e autorize a alteração separadamente.

Saída esperada: raiz correta, branch e alterações conhecidas, instruções vigentes identificadas e capacidades necessárias à próxima atividade disponíveis. Se um comando falhar, registre sua saída e identifique a causa antes de prosseguir com atividades que dependam dele. Não execute git reset, git clean, rebase, remoções ou recriação de ambientes como tentativa genérica de conserto.

Prompt de diagnóstico para o agente, sem escrita:

“Inspecione o repositório aberto e identifique a raiz, branch, commit, alterações locais, estrutura de documentação, instruções vigentes, modos de controle, scripts e dependências necessários à próxima tarefa. Use somente leitura. Diferencie fatos observados de capacidades não testadas. Não instale, edite, execute migrações ou altere Git. Entregue os caminhos corretos, os comandos de verificação e os impedimentos reais. Não proponha recriar o que já existe.”

## 1.2 Selecionar o próximo trabalho

Objetivo: escolher um problema real que possa produzir um resultado útil, sem exigir a especificação completa do produto.

Entrada: necessidades do CEPRAEA, inventário disponível, documentos existentes e estado do software.

Procedimento: descreva o problema em linguagem de treinador, identifique quem é afetado, qual atividade precisa melhorar e como perceberá a melhoria. Escolha uma funcionalidade delimitada e registre o que não faz parte dela. Consulte o repositório para descobrir se já existe especificação ou implementação relacionada. Não declare como decisão aprovada uma sugestão apenas porque apareceu em um documento anterior.

Saída esperada: necessidade escolhida, usuários envolvidos, resultado esperado e fronteira inicial. Se o comportamento essencial depender de uma regra ainda desconhecida, encaminhe a pergunta à pesquisa ou à sua decisão; isso não impede continuar outras atividades independentes.

# 2. INVENTARIAR E PRESERVAR O GOOGLE DRIVE

## 2.1 Confirmar o inventário existente e delimitar a varredura

Objetivo: conhecer o legado sem excluir, mover ou alterar arquivos originais.

Entrada: Drive do CEPRAEA e acesso às unidades/pastas pertinentes.

Procedimento:

1. Abra o Drive com a conta correta. Identifique Meu Drive, drives compartilhados e pastas do projeto às quais sua conta tem acesso. Registre quais unidades entram na varredura e quais não puderam ser acessadas.

2. Localize primeiro o “MANIFESTO CANÔNICO DE MIGRAÇÃO — CEPRAEA BEACH PRO” e o “Registro_Mestre_de_Inventário_e_Mudanças_do_Google_Drive”, encontrados na busca anterior. Examine conteúdo, abrangência, atualização e autoridade antes de decidir reutilizá-los. A existência desses arquivos não comprova que estejam completos ou aprovados. Não crie um inventário concorrente sem necessidade.

3. Use a pesquisa do Drive para localizar CEPRAEA, DATABASE, AGOSTO, cronogramas, formulários, dashboards, regulamentos e outros assuntos relevantes. Utilize filtros por tipo, pessoa ou data quando forem úteis. Uma busca não substitui a varredura por pastas.

4. Percorra as pastas incluídas e registre os arquivos e subpastas encontrados. Quando utilizar uma ferramenta de listagem, confira se houve paginação ou limite de resultados e continue até encerrar o escopo definido. Registre atalhos e, quando possível, a identidade de seus destinos; não conte o atalho como uma cópia independente do conteúdo.

5. Compare os resultados com o inventário existente e registre diferenças. Marque como não verificados os arquivos inacessíveis, os conteúdos que não puderam ser lidos e as áreas fora do escopo.

Saída esperada: universo de arquivos delimitado, inventário atualizado ou validado e cobertura explicitamente descrita. Não declare “Drive completo” com base somente em resultados de busca ou ausência de novos arquivos.

## 2.2 Examinar cada arquivo e registrar seu papel

Para cada arquivo relevante, registre no inventário existente: ID e link, nome, tipo, localização, proprietário quando pertinente, período, finalidade, conteúdo relevante, relação com outros arquivos, possível autoridade, limitações de leitura e destino proposto. Acrescente apenas campos necessários que ainda não existam no inventário.

Em planilhas, examine as guias, cabeçalhos, tipos de valores, fórmulas, validações, intervalos nomeados, referências entre guias, proteções e abas ocultas quando acessíveis. Diferencie valores digitados de resultados calculados. Uma exportação CSV pode perder fórmulas, formatação, validações e múltiplas guias; não a utilize como prova de fidelidade integral. Em documentos, examine estrutura, tabelas, links, versões e anexos pertinentes. Em PDFs e arquivos armazenados, verifique se o conteúdo foi recuperado de maneira legível; não invente trechos ausentes. Em formulários e dashboards, identifique suas fontes, lógica e relações antes de considerá-los duplicados.

Classifique o conteúdo como dado operacional, regra candidata, evidência histórica, especificação, decisão, referência especializada ou material sem papel identificado. Um arquivo antigo pode continuar importante para reconstruir uma regra ou evento. Uma planilha que contém determinada fórmula demonstra uma implementação histórica, não necessariamente a regra desejada para o PWA.

A classificação de destino deve distinguir PRESERVAR, CONSOLIDAR, DUPLICADO CONFIRMADO, HISTÓRICO, PENDENTE e CANDIDATO A EXCLUSÃO FUTURA. Registre a justificativa e o destino previsto. Não exclua nenhum arquivo nesta atividade. As planilhas CEPRAEA AGOSTO e CEPRAEA DATABASE permanecem preservadas; qualquer mudança futura exige autorização específica.

## 2.3 Tratar dados pessoais antes de compartilhar com IA

Identifique se a fonte contém dados pessoais, informações de saúde, contato, identificação ou outros conteúdos que exijam proteção. Verifique a finalidade do tratamento, quem pode acessar, quais dados são realmente necessários e as condições aplicáveis à conta e ao serviço utilizado. Prefira trechos minimizados ou dados sintéticos quando o objetivo for aprender, especificar ou testar. Não publique dados reais em repositório público, prompts compartilhados ou ambientes de teste sem autorização e proteção adequadas. Se a classificação ou a permissão não estiver clara, preserve o arquivo e interrompa somente a transferência daquele conteúdo até resolver a questão.

Prompt para inventário assistido:

“Trabalhe somente em leitura. Delimite as unidades e pastas acessíveis do CEPRAEA, descubra e examine o inventário existente e produza uma relação de arquivos com ID, tipo, localização, finalidade, período, conteúdo relevante, relações, limitações e destino proposto. Trate paginação, atalhos e arquivos inacessíveis explicitamente. Não declare completude sem cobertura demonstrada. Não exclua, mova, renomeie, compartilhe ou modifique fontes. Não copie dados pessoais para outros serviços. Entregue a atualização proposta para revisão antes de qualquer escrita.”

Conclusão da parte: existe um inventário utilizável e preservado. A pesquisa de uma funcionalidade pode começar com fontes já identificadas enquanto a varredura mais ampla continua. A exclusão ou migração do legado não é pré-requisito para iniciar a documentação do software.

# 3. PESQUISAR E CONSTRUIR CONHECIMENTO

## 3.1 Formular a pesquisa de uma funcionalidade

Objetivo: transformar uma necessidade em perguntas que possam ser respondidas por fontes ou por decisão humana.

Entrada: problema selecionado, inventário e conhecimento do treinador.

Procedimento: descreva o processo atual, os usuários, os eventos que o iniciam e as dificuldades conhecidas. Separe perguntas sobre fatos do CEPRAEA, dúvidas sobre o comportamento desejado e dúvidas técnicas. Identifique as fontes prováveis. Não comece perguntando “qual é a melhor arquitetura do aplicativo inteiro” quando a necessidade é compreender uma funcionalidade específica.

Exemplo de perguntas para disponibilidade: como as atletas informam a disponibilidade hoje? Em quais arquivos essa informação é registrada? Quem pode alterá-la? Existe prazo real de resposta? Como uma ausência é identificada? Como o treinador utiliza a informação para planejar? Quais exceções ocorrem? O que é disponibilidade e o que é presença? Quais dessas regras são práticas atuais e quais são decisões já aprovadas para o novo sistema?

Saída esperada: perguntas agrupadas por assunto, com fontes prováveis e dúvidas que exigirão sua resposta.

## 3.2 Organizar fontes no NotebookLM

Objetivo: utilizar o NotebookLM para investigar um conjunto relevante de fontes, sem transformá-lo em repositório canônico do software.

Entrada: perguntas, arquivos selecionados e permissão adequada para tratamento dos conteúdos.

Procedimento:

1. Abra o NotebookLM/Gemini Notebook pela conta do Workspace que utiliza no projeto. Confirme a conta e a variante disponibilizada. Utilize a interface web e consulte a seção correspondente da Pesquisa Documental NotebookLM quando precisar confirmar um recurso, limite ou comportamento específico.

2. Abra um notebook existente adequado à pesquisa ou crie um novo usando o controle de criação disponível. Dê um nome que identifique o assunto e o escopo. Não há exigência de uma quantidade fixa de notebooks nem de isolamento absoluto por categoria.

3. Use o controle de adicionar fontes para selecionar arquivos do Drive ou outros tipos suportados. Confirme que o tipo de fonte, o tamanho e a quantidade são aceitos na sua conta. Não presuma que um arquivo foi ingerido integralmente apenas porque aparece na lista.

4. Registre quais fontes foram utilizadas. Se uma planilha complexa não for recuperada com fidelidade suficiente, examine-a diretamente no Sheets e prepare uma representação adequada à pergunta, preservando identificação e vínculo com o original. Não substitua a planilha original por uma exportação incompleta.

5. Se uma fonte mudar, confira o comportamento de atualização aplicável à sua variante. Revalide a versão utilizada na pesquisa; não presuma que todas as fontes foram sincronizadas automaticamente.

Saída esperada: notebook e conjunto de fontes identificáveis, com cobertura suficiente para as perguntas escolhidas. Se o recurso não estiver disponível, não tente instalar uma API ou ferramenta não autorizada; utilize leitura direta das fontes e registre a limitação.

## 3.3 Extrair, confrontar e conferir respostas

No chat do notebook, faça perguntas delimitadas e solicite indicação das fontes e dos trechos relevantes. Abra as citações e confira o contexto original. Quando uma resposta reunir informações de vários arquivos, verifique se as fontes realmente sustentam a conclusão. Não trate uma síntese como prova de que todo o legado foi pesquisado.

Prompt para extração do processo atual:

“Utilize somente as fontes deste notebook para investigar [PROCESSO]. Identifique atores, eventos de início, atividades, dados utilizados, estados, regras candidatas, exceções e dificuldades observáveis. Para cada afirmação material, indique a fonte e o trecho que a sustenta. Diferencie funcionamento documentado, interpretação e informação não encontrada. Registre contradições sem escolher silenciosamente uma versão. Não proponha arquitetura nem invente regras do futuro sistema. Se as fontes não permitirem responder, declare a lacuna.”

Prompt para confronto:

“Compare as fontes [FONTE A] e [FONTE B] quanto a [ASSUNTO]. Identifique o que coincide, o que diverge, o período e o contexto de cada informação. Apresente os trechos de suporte e explique quais questões precisam ser confirmadas. Não considere a fonte mais recente automaticamente superior quando sua autoridade ou finalidade for diferente.”

Verificação: selecione as afirmações que influenciam regras, decisões ou requisitos e abra os respectivos trechos. Confirme se o texto não omite condições ou confunde datas, pessoas e processos. Se a fonte não estiver acessível ou o trecho não sustentar a afirmação, marque-a como não verificada. Quando o NotebookLM não conseguir executar a análise necessária, utilize as fontes originais e outra ferramenta autorizada, sem fabricar citações.

## 3.4 Transferir o conhecimento para a documentação

Não use a resposta do chat como especificação aprovada. Copie a síntese necessária para um documento de trabalho acessível ao processo de documentação, mantendo as referências às fontes, as questões abertas e o que foi conferido. Se houver opção de salvar uma nota, utilize-a apenas como apoio; confirme sua persistência e a maneira de recuperá-la antes de depender dela.

O caminho básico funciona sem MCP: NotebookLM → síntese conferida → documento de trabalho → documentação do repositório. O caminho pode ser executado por cópia revisada, exportação suportada ou ferramenta conectada que tenha sido verificada. Não coloque credenciais em prompts, não instale servidores MCP desconhecidos e não use APIs Enterprise como se fossem automaticamente disponíveis à sua conta Workspace.

# 4. PESQUISAR E APLICAR FONTES ESPECIALIZADAS

## 4.1 Identificar o domínio da dúvida

Objetivo: encontrar o conhecimento apropriado para resolver um problema específico, sem pesquisar todas as disciplinas antes de desenvolver.

Entrada: necessidade, requisito, dúvida de UX ou decisão técnica.

Procedimento: formule a pergunta e classifique o domínio principal. Por exemplo, entendimento do trabalho da equipe pertence ao domínio esportivo e à análise de processos; comportamento esperado pertence à engenharia de requisitos; interação com atletas e treinador pertence à UX e qualidade em uso; fronteiras e dependências pertencem à arquitetura; persistência e integridade pertencem à modelagem de dados; acesso e proteção pertencem à segurança; comportamento verificável pertence a testes. Uma pergunta pode exigir mais de uma disciplina.

Consulte primeiro as fontes pertinentes ao problema. Para regras do CEPRAEA, as fontes incluem o legado e sua decisão. Para funcionalidades de ferramentas e bibliotecas, prefira documentação oficial aplicável à versão utilizada. Para UX, combine referências reconhecidas, evidência de pesquisa quando pertinente e observação do uso real. Para arquitetura, considere os requisitos, as restrições, as decisões existentes e as alternativas necessárias. Uma recomendação encontrada na internet não se torna automaticamente regra do projeto.

## 4.2 Executar uma pesquisa delimitada

1. Escreva a pergunta, o contexto e o resultado que precisa decidir.

2. Identifique quais tipos de fonte podem respondê-la: documentação oficial, norma, guia técnico, pesquisa científica, referência de domínio ou experiência de usuários. Selecione a fonte pela adequação à pergunta, não pela popularidade isolada.

3. Confirme autor, versão, data relevante, escopo, condições de aplicação e eventuais limitações. Em tecnologias, confira a compatibilidade com a stack e com as decisões atuais do repositório.

4. Extraia somente as informações que respondem à pergunta, com referências suficientes para recuperá-las. Diferencie afirmação da fonte de interpretação aplicada ao CEPRAEA.

5. Quando houver escolha técnica material, identifique alternativas realmente pertinentes, seus custos, benefícios, riscos e consequências. Não invente uma segunda alternativa apenas para preencher um modelo de comparação.

6. Apresente a recomendação e as questões que dependem de sua decisão. Registre a decisão no documento canônico apropriado quando ela for aprovada.

Prompt para pesquisa especializada:

“Investigue [PERGUNTA] no contexto do CEPRAEA BEACH PRO e da arquitetura vigente. Identifique as fontes especializadas mais pertinentes e verifique versão, autoridade e aplicabilidade. Separe fatos documentados, interpretações e recomendações. Compare alternativas quando houver uma decisão real a tomar. Explique consequências para UX, segurança, manutenção, custo e compatibilidade conforme forem relevantes. Não reabra decisões existentes sem identificar a razão. Não proponha instalação ou API paga como requisito. Entregue referências verificáveis e uma recomendação que eu possa avaliar.”

## 4.3 Aplicar o resultado ao projeto

Uma fonte especializada pode indicar que determinada solução é adequada em certo contexto, mas não decide sozinha a prioridade do produto. Relacione a recomendação ao problema concreto, aos requisitos e às restrições. Se o benefício depender de uma hipótese sobre atletas ou treinador, realize uma validação proporcional com os usuários. Se depender de desempenho, compatibilidade ou segurança, proponha um teste técnico apropriado. Registre como hipótese aquilo que ainda não foi demonstrado.

Referências iniciais para localizar conhecimento: ISO/IEC/IEEE 29148 para engenharia de requisitos; ISO/IEC 25010 e 25019 para qualidade do produto e qualidade em uso; WCAG 2.2 para acessibilidade; documentação oficial de React, TypeScript, Vite, Supabase, Vitest e Testing Library para implementação e testes. Consulte também documentação e regulamentos oficiais do handebol de praia quando a regra esportiva for relevante. Essas referências são pontos de partida, não um currículo obrigatório nem prova de conformidade com normas.

Conclusão da parte: existe conhecimento suficiente para responder às perguntas da funcionalidade, ou lacunas claramente identificadas que podem ser resolvidas por pesquisa adicional, teste ou decisão sua. Não é necessário esgotar toda a literatura antes de continuar.

# 5. TRANSFORMAR CONHECIMENTO EM DOCUMENTAÇÃO DE SOFTWARE

## 5.1 Localizar os documentos de autoridade antes de escrever

Objetivo: atualizar a documentação correta, evitando criar arquivos concorrentes ou contraditórios.

Entrada: conhecimento conferido, decisões pertinentes e repositório existente.

Procedimento:

1. Solicite ao agente uma inspeção somente de leitura dos documentos existentes. Ele deve localizar o índice de documentação, os documentos de domínio, requisitos, fluxos, arquitetura, dados, decisões e padrões aplicáveis. Deve ler AGENT_POLICY.md, .ai/decisions/INDEX.md e as instruções vigentes para identificar a autoridade e o modo de trabalho. Não utilize caminhos lembrados de conversas antigas como se fossem atuais.

2. Para cada informação que precisa ser registrada, identifique se já existe um proprietário documental. Atualize o documento adequado em vez de copiar a mesma regra para vários arquivos. Utilize referências entre documentos quando necessário.

3. Consulte o plano de modelagem canônica e as decisões arquiteturais atuais quando a atividade envolver domínio, bounded contexts ou modelo de dados. Não substitua essas decisões por uma nova taxonomia improvisada.

4. Quando não existir um local adequado, proponha o menor artefato necessário e sua relação com os existentes. A criação ou modificação deverá seguir o processo de autorização vigente no repositório.

Prompt de descoberta documental:

“Inspecione somente em leitura a documentação atual do repositório. Para a necessidade [FUNCIONALIDADE], identifique os documentos de autoridade, caminhos, seções, decisões ativas, requisitos existentes e lacunas. Mostre onde cada informação deverá ser consultada ou atualizada. Não crie arquivos, não copie regras para proprietários concorrentes e não utilize documentos históricos como autoridade atual. Informe as contradições materiais sem resolvê-las silenciosamente.”

## 5.2 Consolidar conhecimento sem transformar hipótese em regra

Para cada informação material, distinga sua natureza. FATO DOCUMENTADO é o que uma fonte efetivamente demonstra. INTERPRETAÇÃO é a conclusão derivada dessa evidência. HIPÓTESE é algo que ainda precisa ser confirmado. PROPOSTA é uma alternativa apresentada para decisão. DECISÃO APROVADA é a escolha registrada por sua autoridade. REQUISITO é o comportamento exigido para o produto, devidamente fundamentado por uma necessidade e decisão aplicáveis.

Uma regra histórica não se torna automaticamente requisito do novo software. Se um prazo, permissão ou comportamento ainda não foi definido, formule a pergunta e apresente alternativas quando úteis. Você pode criar uma regra nova para o produto; nesse caso, registre-a como decisão sua, não como fato extraído do Drive. Preserve a referência de origem e a justificativa quando forem necessárias para compreender ou revisar a informação.

## 5.3 Definir requisitos e fluxos de uma funcionalidade

Objetivo: descrever o comportamento necessário para que os agentes possam implementá-lo e você possa avaliá-lo.

Entrada: necessidade escolhida, conhecimento consolidado, regras e decisões relevantes.

Procedimento:

1. Identifique o ator, a necessidade, o evento que inicia o fluxo e o resultado esperado.

2. Descreva as pré-condições, as ações do usuário e as respostas do sistema. Explicite regras, estados, transições, permissões e exceções que sejam relevantes ao comportamento.

3. Diferencie o fluxo atual da equipe do fluxo desejado para o PWA. Não copie limitações de uma planilha como se fossem exigências permanentes.

4. Escreva critérios de aceite observáveis, incluindo cenários normais, erros e limites importantes. Use linguagem que permita ao agente e ao treinador reconhecer o mesmo resultado.

5. Verifique com você as regras e decisões de produto. Quando apropriado, confronte a proposta de UX com necessidades das atletas e referências especializadas. Não considere uma escolha de interface aprovada apenas porque o agente a recomendou.

6. Registre o resultado nos documentos de autoridade existentes. Mantenha identificadores e relações previstos pelo repositório; não crie uma numeração paralela desnecessária.

Exemplo ilustrativo, não especificação aprovada:

Necessidade: reduzir o esforço para saber quais atletas poderão participar de um treino.

Conceitos distintos: disponibilidade representa uma informação ou intenção relativa a uma atividade; presença representa o fato de participação registrado segundo uma regra definida. Uma não deve ser convertida automaticamente na outra.

Perguntas ainda necessárias: quem pode informar ou alterar disponibilidade? Existe prazo? O que acontece quando não há resposta? Quem registra presença? Como são corrigidos erros? Que informação cada usuária pode visualizar? Qual o comportamento quando não há conexão?

Exemplo de critério de aceite, dependente de aprovação: “Dada uma atividade e uma atleta autorizada, quando ela registra uma resposta válida, o sistema apresenta o resultado previsto pela regra aprovada; o registro de presença permanece independente.” O modelo de dados, os estados possíveis, as permissões e as regras de atualização precisam ser definidos antes de transformar esse exemplo em implementação.

## 5.4 Definir somente as decisões técnicas necessárias

Use requisitos, arquitetura existente e fontes especializadas para identificar mudanças necessárias em componentes, dados, integrações, autenticação, segurança e testes. Consulte as decisões ativas e os bounded contexts existentes antes de propor novas fronteiras. Uma decisão arquitetural significativa deve ser registrada conforme o padrão de ADR vigente; uma escolha trivial não precisa gerar um ADR novo.

Para dados, descreva entidades, identificadores, relações, restrições, invariantes e autoridade de alteração conforme a necessidade. Não copie diretamente colunas históricas para tabelas sem compreender seu significado, mas também não descarte uma estrutura antiga que possa ser reutilizada justificadamente. Se houver migração, trate mapeamento, reconciliação, backup e recuperação como atividade própria.

## 5.5 Verificar se a documentação pode ser consumida

Antes do handoff, confira se o conjunto pertinente permite responder: qual problema será resolvido; quem executa o fluxo; qual comportamento é esperado; quais regras e exceções se aplicam; o que está fora do escopo; quais decisões técnicas já estão vigentes; quais critérios demonstrarão o resultado; e quais dúvidas materiais permanecem.

Não exija que todos os documentos do produto estejam completos. Uma lacuna fora da funcionalidade ativa pode permanecer registrada. Uma lacuna que impede determinar comportamento, segurança ou outra condição essencial precisa ser resolvida antes da implementação correspondente. A revisão deve verificar coerência e suficiência para a tarefa, não apenas a presença de arquivos ou títulos.

Prompt de revisão de especificação:

“Revise os documentos relativos a [FUNCIONALIDADE] contra a necessidade aprovada. Verifique rastreabilidade, consistência de conceitos e regras, fluxos normais e excepcionais, critérios de aceite, restrições e decisões existentes. Identifique ambiguidades que permitam implementações materialmente diferentes. Separe questões críticas para esta funcionalidade de lacunas que podem permanecer fora do escopo. Não altere documentos nem invente decisões. Entregue correções específicas e referências aos trechos envolvidos.”

Resultado esperado: documentação suficiente para uma tarefa delimitada. A aprovação da documentação não comprova que o software funciona; ela permite iniciar uma implementação cujo comportamento foi suficientemente definido.

# 6. ENTREGAR CONTEXTO E TRABALHAR COM CLAUDE CODE E CODEX

## 6.1 Confirmar o processo vigente no repositório

O manual não cria um novo fluxo de agentes. Na leitura realizada, AGENT_POLICY.md estabelece Claude Code como PLANNER/EXECUTOR e Codex como REVIEWER independente. A execução usa .ai/tasks/<TASK-ID>/proposal.json, approval.json e execution-result.json, com validadores e aprovação humana vinculada ao conteúdo da proposta. O operador humano é responsável pelo Git privilegiado. Confirme os arquivos e decisões atuais antes de utilizar esse procedimento.

Abra no VS Code o repositório correto e leia docs/operacao/agent-workflow.md, .ai/control/README.md, AGENT_POLICY.md, CLAUDE.md, AGENTS.md, .ai/decisions/INDEX.md e os runbooks aplicáveis. Não substitua o processo existente por um novo conjunto de estados, contratos ou pastas. Se desejar modificar os papéis ou controles, trate isso como uma decisão e tarefa específica, separada da implementação de uma funcionalidade.

## 6.2 Preparar a tarefa e o contexto

Entrada: documentação suficiente, resultado esperado e estado atual do repositório.

Procedimento:

1. Confirme que a branch e a base de trabalho são apropriadas. A política atual exige branch não-main para execução e reserva criação/mudança de branch ao humano. Se for necessária uma nova branch, primeiro examine o estado local e o procedimento vigente; não mande o agente alterar Git.

2. Identifique os documentos de autoridade e as seções aplicáveis. O handoff deve referenciar esses caminhos, não copiar toda a documentação para a conversa.

3. Descreva o objetivo, o que está incluído e excluído, os resultados observáveis, as restrições e os critérios de aceite. Use o mecanismo de TaskProposal já existente para representar o plano.

4. Solicite que Claude Code, em fase PLAN, inspecione o código e a documentação antes de propor alterações. Não autorize implementação durante essa fase.

Prompt para Claude Code — PLAN:

“Fase PLAN. Minha necessidade é [DESCREVER O RESULTADO]. Leia as instruções vigentes e localize a documentação de autoridade pertinente. Inspecione o estado real do repositório e o código relacionado. Preserve minha intenção sem ampliar escopo. Produza ou atualize somente o TaskProposal da TASK apropriada, conforme o contrato e os runbooks atuais. Defina outputs, critérios de aceite, ações, dependências, targets, restrições e riscos necessários. Não altere código, não crie aprovação e não execute Git mutável. Não invente regras de negócio ou decisões técnicas materiais. Execute o validador da proposta e informe o resultado, as evidências e os pontos que exigem minha decisão. Se houver impedimento, reporte BLOCKED.”

## 6.3 Revisar o plano e aprovar conscientemente

Após a proposta existir, informe no terminal Bash o ID da TASK já criada. A primeira linha abaixo solicita o ID; digite o valor real, sem os símbolos < >, e pressione Enter. Confirme que o arquivo existe antes de validar:

read -r -p 'ID da TASK existente: ' TASK_ID



node .ai/control/validate-task-proposal.mjs ".ai/tasks/${TASK_ID}/proposal.json"



O ID informado deve corresponder à tarefa existente no repositório. O validador verifica o contrato correspondente; seu sucesso não demonstra que o plano resolve corretamente sua necessidade. Solicite ao Codex uma revisão sem escrita:

“review_stage = PLAN. Revise a proposta da TASK [TASK-ID] de acordo com AGENTS.md, AGENT_POLICY.md, decisões ativas e controles existentes. Verifique se o objetivo preserva minha intenção, se os outputs e critérios de aceite demonstram o resultado, se ações e dependências são coerentes e se escopo, riscos e fontes estão corretos. Procure ambiguidades e premissas não sustentadas. Não modifique arquivos nem aprove por mim. Entregue PASS, FAIL ou HUMAN_DECISION_REQUIRED com evidências e correções necessárias.”

Em caso de FAIL, devolva os achados ao planejador para corrigir a proposta. Se houver decisão humana necessária, resolva-a e revise a proposta. Uma mudança material na proposta exige nova revisão e nova aprovação correspondente. Não crie uma cadeia ilimitada de reparos: corrija o problema identificado ou encerre a tarefa como bloqueada quando não houver condição de resolvê-lo.

Somente depois de compreender e aceitar o plano, produza a aprovação humana pelo procedimento vigente. O approval.json deve corresponder ao schema atual e vincular a proposta, sua revisão, o SHA-256 exato, o repositório, a branch e o commit-base. Não utilize um JSON improvisado nem peça ao agente que declare aprovação humana em seu lugar. Consulte o modelo, o schema e o runbook ativos para preencher os campos corretos. Valide o arquivo com o comando previsto:

node .ai/control/validate-task-approval.mjs ".ai/tasks/${TASK_ID}/proposal.json" ".ai/tasks/${TASK_ID}/approval.json"

node .ai/control/validate-task-approval.mjs ".ai/tasks/${TASK_ID}/proposal.json" ".ai/tasks/${TASK_ID}/approval.json"

Se a validação falhar, não execute. Confira o erro, a identidade da proposta, os vínculos e a aprovação. Nunca altere o hash ou o conteúdo aprovado apenas para forçar PASS.

## 6.4 Executar a tarefa autorizada

Prompt para Claude Code — EXECUTE:

“Fase EXECUTE. Implemente somente a TASK [TASK-ID] cuja proposta e aprovação válidas estão no repositório. Leia os contratos e runbooks atuais, confirme o RuntimeAnchor, a branch, os targets e as pré-condições. Reexecute as validações obrigatórias antes da primeira escrita. Implemente somente as ações autorizadas, execute os testes pertinentes e registre evidências reais. Não altere a proposta aprovada, a aprovação, as decisões ou os controles fora da autorização. Não execute Git mutável, não utilize dados reais nem conecte serviços de produção. Se surgir necessidade de ampliar escopo ou tomar decisão material, interrompa a parte afetada e reporte BLOCKED. Entregue execution-result.json válido, diff, comandos, exit codes, resultados e limitações.”

O agente deve executar os validadores e testes previstos pela TASK. Não aceite saída fabricada, relato de comando que não foi executado ou aprovação simulada. Quando a execução depender de um serviço que não está disponível, registre o impedimento e preserve o trabalho já realizado; não substitua uma integração real por um mock e declare que a integração foi comprovada.

## 6.5 Revisar a implementação e realizar o Git privilegiado

Após o executor concluir, solicite ao Codex:

“review_stage = IMPLEMENTATION. Revise a TASK [TASK-ID], a proposta aprovada, o execution-result.json, o diff e as evidências materiais. Reexecute os validadores e os testes necessários dentro das permissões vigentes. Verifique correspondência entre ações, critérios de aceite, alterações e resultados, procure regressões e mudanças fora do escopo. Não modifique arquivos nem execute Git mutável. Entregue PASS, FAIL ou HUMAN_DECISION_REQUIRED com justificativas verificáveis.”

O comando de validação do resultado é:

node .ai/control/validate-execution-result.mjs ".ai/tasks/${TASK_ID}/proposal.json" ".ai/tasks/${TASK_ID}/approval.json" ".ai/tasks/${TASK_ID}/execution-result.json"



Se a revisão falhar, corrija somente o problema pertinente dentro da autoridade aprovada ou revise o plano quando houver mudança material. PASS do Codex não substitui sua aceitação do produto nem autoriza automaticamente merge ou deploy. Examine o diff, os testes e a funcionalidade antes de realizar qualquer operação privilegiada de Git. Utilize o procedimento humano do repositório para branch, commit, push e integração; não copie comandos de merge ou reset genéricos sem confirmar o estado e o destino.

## 6.6 Evitar problemas de contexto e de integração

Use referências a arquivos e trechos específicos para reduzir o custo de contexto. Quando o agente apresentar uma regra divergente, peça a origem e confronte o documento de autoridade. Se não conseguir acessar um arquivo do Drive ou NotebookLM, transfira o trecho necessário por um caminho autorizado e confirme que ele foi recebido. Não confunda uma citação na conversa com persistência no repositório.

AGENTS.md e CLAUDE.md orientam o comportamento dos agentes; os controles reais dependem das permissões, scripts, hooks, configurações e superfícies efetivamente existentes. A política atual não deve ser enfraquecida para acelerar uma tarefa. Se um controle estiver em modo diagnóstico ou piloto, descreva seu estado corretamente, sem anunciá-lo como enforcement obrigatório. Não instale um MCP para contornar permissões, aprovação humana ou as restrições de custo do projeto.

Resultado esperado: tarefa executada e revisada segundo o processo vigente, com evidências materiais e alterações conhecidas. A conclusão técnica ainda precisa ser confrontada com o comportamento esperado antes da aceitação final.

# 7. TESTAR, VALIDAR E DISPONIBILIZAR O SOFTWARE

## 7.1 Preparar a execução local sem alterar dados reais

Objetivo: executar as verificações previstas no repositório e conhecer exatamente o ambiente utilizado.

Entrada: cópia local correta, scripts existentes e tarefa autorizada quando houver alterações.

Procedimento:

1. Confirme a raiz e a branch com os comandos da seção 1. Examine README.md, package.json, o arquivo de lock e a configuração do container. Na leitura remota anterior, README.md documentava comandos npm, mas package.json não foi recuperado; portanto, confira sua existência e os scripts reais antes de executá-los.

2. Verifique se o Node e as dependências correspondem ao projeto. Se package.json e o lockfile estiverem presentes e a instalação for necessária, o README indica npm ci. Esse comando instala dependências e pode executar scripts do pacote; utilize-o somente no ambiente confiável e após conferir o projeto. Não execute instalação apenas para responder a uma pergunta documental.

3. Para iniciar o frontend, o README indica npm run dev. Antes, confira as variáveis necessárias e os arquivos de exemplo. Se precisar criar .env a partir de .env.example, verifique que o destino não contém configuração que deve ser preservada. Nunca sobrescreva um .env existente nem coloque chaves secretas ou de serviço no frontend. A configuração de teste deve utilizar somente valores autorizados.

4. Abra o endereço local informado pelo servidor. Registre qual ambiente está em uso e se a interface está desconectada, conectada a serviços sintéticos ou apenas demonstrando componentes. Não interprete uma página carregada como prova de integração funcional.

5. O README indica npm run validate para verificar fronteira sintética, lint, tipos, testes e build. Confirme que o script existe e execute-o no ambiente apropriado. Preserve o exit code e a saída relevante. Se falhar, identifique qual verificação falhou e sua causa; não suprima testes ou altere a configuração apenas para obter uma saída verde.

Comandos de referência, condicionados à existência dos arquivos e à confirmação do ambiente:

npm ci



npm run dev



npm run validate



Não execute esses comandos em uma pasta desconhecida. Não utilize npm install, atualização de dependências ou alteração de versão como tentativa automática de consertar qualquer falha.

## 7.2 Verificar serviços, dados e autorização

Quando a funcionalidade exigir Supabase, confirme a configuração em supabase/, o runtime Docker e o procedimento local vigente. O README documenta npx supabase start, mas sua execução não foi comprovada nesta elaboração. Execute-o somente após confirmar a instalação e a configuração corretas, em ambiente sintético.

Não execute db reset, db push, migrações remotas ou comandos de exclusão como parte de um roteiro genérico. db reset destrói e recria o banco local alvo; variantes vinculadas a projetos remotos podem ter efeitos ainda mais graves. Qualquer reset ou migração deve ter alvo confirmado, dados sintéticos, efeitos compreendidos e autorização específica. Não conecte o repositório atual a dados reais.

Para funcionalidades que dependam de autenticação e RLS, os testes devem verificar o comportamento permitido e o proibido. Por exemplo, um usuário autorizado deve conseguir executar a operação prevista, enquanto outro usuário sem permissão não deve conseguir ler ou alterar o mesmo recurso. Verifique também ausência de credenciais secretas no cliente, restrições do banco, erros e comportamento de sessão quando pertinentes. Um teste de interface com dados simulados não comprova automaticamente as políticas reais do banco.

## 7.3 Relacionar testes aos critérios de aceite

Entrada: requisitos e critérios aprovados, implementação e ambiente de teste.

Procedimento: identifique quais verificações demonstram cada comportamento material. Utilize testes unitários para regras isoladas quando adequado, testes de integração para interações entre componentes e serviços e testes de interface para fluxos do usuário. Inclua verificações técnicas de segurança, dados, build e regressão quando forem relevantes, mesmo que não estejam vinculadas a um requisito funcional específico.

Registre o comando executado, o ambiente, o resultado, os testes que passaram, os que falharam e as limitações. Não aceite “todos os testes passaram” sem evidência de execução e sem saber quais testes foram realmente executados. Testes com mocks demonstram o comportamento simulado sob aquelas condições; não substituem testes de integração quando a integração é necessária ao resultado.

## 7.4 Validar o comportamento com o treinador e as atletas

A validação responde se a funcionalidade atende à necessidade real, não apenas se o código satisfaz os testes. Prepare um pequeno roteiro de tarefas reais, utilizando dados sintéticos no ambiente atual. Apresente a funcionalidade e peça que o usuário execute a tarefa sem receber explicações que escondam problemas de compreensão. Observe dificuldades, erros, informações ausentes e esforço necessário.

Exemplo ilustrativo para disponibilidade: uma atleta acessa a atividade, identifica o que precisa informar, registra ou altera sua resposta conforme as regras aprovadas e consegue reconhecer o resultado. O treinador consulta as informações necessárias para planejar a atividade. Verifique separadamente o comportamento de presença, permissões, ausência de resposta, erros e exceções definidos. Não considere esses exemplos regras aprovadas do CEPRAEA.

Registre o que foi aceito, o que precisa ser corrigido e o que constitui uma nova necessidade. Uma preferência nova ou alteração de escopo deve ser avaliada antes de entrar na implementação. Não altere silenciosamente requisitos aprovados para acomodar um comportamento inesperado do código.

Critério de aceitação: você confirma que os comportamentos acordados foram demonstrados no ambiente apropriado e que os problemas impeditivos foram resolvidos ou receberam tratamento explícito. A aceitação deve identificar a funcionalidade e a versão avaliada; não é uma declaração de que todo o produto está livre de defeitos.

## 7.5 Integrar e disponibilizar conforme o estágio do produto

Depois da revisão e aceitação, o humano verifica a branch, o diff, os testes e as alterações que serão integradas. Utilize o procedimento vigente de Git e as proteções efetivamente configuradas. Não presuma que uma branch está protegida apenas porque essa regra aparece em AGENTS.md. Não execute push, merge ou rebase sem identificar destino, efeitos e autorização.

Distinga quatro situações: implementação local; ambiente de teste; piloto com usuários reais; produção. Cada uma exige condições próprias. A fundação atual está declarada como sintética e não autorizada para piloto ou produção. Não utilize a aceitação de uma funcionalidade local como autorização automática para mudar esse estado.

Antes de disponibilizar uma funcionalidade a usuários reais, confirme o ambiente, domínio e configuração, autenticação e permissões, tratamento de dados, migrações necessárias, backup/recuperação, monitoramento mínimo, suporte e procedimento de reversão. A profundidade deve ser proporcional ao risco e à funcionalidade. O destino futuro de hospedagem indicado no README não significa que o deploy já esteja configurado ou autorizado.

# 8. CONTINUIDADE, MIGRAÇÃO E RECUPERAÇÃO

## 8.1 Atualizar o conhecimento após cada entrega

Depois de uma funcionalidade aceita, atualize somente os documentos afetados: requisitos e fluxos quando o comportamento aprovado mudou; decisões técnicas quando uma decisão relevante foi tomada; arquitetura ou modelo de dados quando a implementação alterou suas responsabilidades; instruções operacionais quando o procedimento real mudou. Preserve o histórico necessário e evite copiar logs de conversa para documentos de autoridade.

A documentação deve representar o comportamento aprovado e implementado, sem ocultar divergências. Quando um teste revelar defeito, corrija o código ou a especificação responsável conforme a causa. Não reescreva a documentação para declarar correto um comportamento incorreto. A próxima funcionalidade deve reutilizar o conhecimento existente e atualizar somente o que for necessário.

## 8.2 Planejar migração e consolidação do legado quando forem necessárias

A migração real não está autorizada pelo estado atual da fundação. Quando houver decisão específica para prepará-la, utilize o inventário e examine primeiro os manifestos de migração existentes. Defina fonte, destino, mapeamento de campos, transformações, identificadores, tratamento de duplicidades, valores ausentes, integridade referencial e regras de reconciliação. Diferencie preservar histórico de reproduzir todas as colunas e fórmulas antigas no novo banco.

Antes de qualquer escrita em dados reais, deve existir autorização adequada, backup verificável, ambiente e permissões definidos, procedimento testado em dados sintéticos e forma de detectar e recuperar falhas. Compare quantidades, identidades e valores relevantes antes e depois, registrando diferenças justificadas. Não elimine a fonte após uma importação apenas porque o comando terminou sem erro. A exclusão de arquivos do Drive é uma decisão posterior e separada, vinculada a uma relação de arquivos específica e à confirmação da preservação necessária.

## 8.3 Resolver falhas sem reiniciar todo o processo

Se um arquivo não foi encontrado, revise escopo, permissões, pasta, filtros e atalhos; registre a limitação. Se uma fonte foi recuperada parcialmente, examine o original e use uma representação adequada, sem declarar fidelidade não comprovada. Se o NotebookLM não sustentar uma resposta, volte às fontes ou registre a pergunta pendente. Se houver conflito de regras, apresente as alternativas e a evidência a você, sem escolher silenciosamente.

Se o agente não encontrar a documentação, confirme a raiz, os caminhos e as permissões; forneça o trecho necessário por uma transferência autorizada. Se o plano falhar na revisão, corrija o achado específico e reavalie. Se uma aprovação não corresponder à proposta, não force o hash; revise e aprove a versão correta. Se o container ou um serviço não iniciar, preserve os logs e diagnostique a dependência antes de reinstalar. Se testes falharem, identifique a causa e repita as verificações afetadas. Se uma alteração exceder o escopo, interrompa a parte afetada e retorne à autorização apropriada.

Não crie uma nova cadeia de governança a cada falha. O registro necessário é o que permite compreender o problema, preservar o trabalho e continuar com segurança.

## 8.4 Acompanhar se o processo está economizando trabalho

Observe indicadores ligados ao objetivo: tempo necessário para localizar informações; tempo para especificar e entregar uma funcionalidade; quantidade de retrabalho por ambiguidade; atualizações manuais que o PWA substitui; erros operacionais; facilidade de uso para atletas e treinador; e tempo gasto com procedimentos de controle. Registre uma situação inicial e compare com os resultados após entregas reais. Não invente metas numéricas sem conhecer o baseline.

Se uma atividade documental ou de controle não reduzir risco relevante nem contribuir para uma entrega, examine a possibilidade de simplificá-la. Se um risco exigir maior rigor, aumente a profundidade daquela atividade. O objetivo é software útil com conhecimento preservado e esforço proporcional, não maximizar o número de documentos ou aprovações.

# ROTEIRO DE PRIMEIRO USO DO MANUAL

Para iniciar uma nova funcionalidade, reconheça o ambiente pela seção 1; confirme o inventário e selecione fontes pertinentes pela seção 2; investigue o funcionamento real e as dúvidas especializadas pelas seções 3 e 4; defina requisitos, fluxo, aceite e decisões necessárias pela seção 5; utilize o processo vigente dos agentes na seção 6; execute e valide pela seção 7; atualize o conhecimento e escolha a próxima entrega pela seção 8. A conclusão de uma atividade deve ser registrada no artefato que ela produz, não em uma declaração global de que todo o projeto está pronto.

# FONTES E CAMINHOS DE CONSULTA

As fontes abaixo permitem conferir as capacidades e procedimentos mencionados. Consulte suas versões atuais antes de executar operações que dependam de comportamento específico. A leitura de uma documentação não comprova que o recurso está habilitado na sua conta ou funcionando no seu ambiente.

Fontes do próprio projeto:

GitHub: [https://github.com/cepraea/beach-pro](https://github.com/cepraea/beach-pro)

README e estado do produto: [https://github.com/cepraea/beach-pro/blob/main/README.md](https://github.com/cepraea/beach-pro/blob/main/README.md)

Política dos agentes: [https://github.com/cepraea/beach-pro/blob/main/AGENT_POLICY.md](https://github.com/cepraea/beach-pro/blob/main/AGENT_POLICY.md)

Instruções Claude: [https://github.com/cepraea/beach-pro/blob/main/CLAUDE.md](https://github.com/cepraea/beach-pro/blob/main/CLAUDE.md)

Instruções Codex: [https://github.com/cepraea/beach-pro/blob/main/AGENTS.md](https://github.com/cepraea/beach-pro/blob/main/AGENTS.md)

Controles e validadores: [https://github.com/cepraea/beach-pro/blob/main/.ai/control/README.md](https://github.com/cepraea/beach-pro/blob/main/.ai/control/README.md)

Decisões ativas: [https://github.com/cepraea/beach-pro/blob/main/.ai/decisions/INDEX.md](https://github.com/cepraea/beach-pro/blob/main/.ai/decisions/INDEX.md)

Runbook do operador: [https://github.com/cepraea/beach-pro/blob/main/docs/operacao/agent-workflow.md](https://github.com/cepraea/beach-pro/blob/main/docs/operacao/agent-workflow.md)

Pesquisa Documental NotebookLM: [Pesquisa Documental NotebookLM](https://docs.google.com/document/d/1DGF1_hiXQaoIyJwnauWsIISoDEQ761hjUhJS3UwGRTw/edit)

CEPRAEA AGOSTO 2026: [CEPRAEA AGOSTO 2026](https://docs.google.com/spreadsheets/d/14d3vIfkvhkTvjjTxkM7CxA9Oo1etHAgC2KUzGzzEn88/edit)

CEPRAEA DATABASE: [CEPRAEA DATABASE](https://docs.google.com/spreadsheets/d/10Dv1oBIKdodWEWsK8qUeLPyazzdg4hdRkVi4gjvVSno/edit)

Manifesto de migração existente: [MANIFESTO CANÔNICO DE MIGRAÇÃO — CEPRAEA BEACH PRO — v1.8 — AUDITORIA GATE 2 / SHORTCUT TARGET_ID — PT-BR](https://docs.google.com/spreadsheets/d/1JrjiESnBc-ftPITUBxrOhW9_J4CJydKrOcmnaMpIadU/edit)

Registro mestre de inventário existente: [Registro_Mestre_de_Inventário_e_Mudanças_do_Google_Drive](https://docs.google.com/spreadsheets/d/1TYtvSVH8JvFfIDdync0-wWbuv6IqWAuezLAx0YeBfhU/edit)

Fontes técnicas oficiais:

Google Drive — pesquisa e filtros: [https://support.google.com/drive/answer/2375114?hl=pt-br](https://support.google.com/drive/answer/2375114?hl=pt-br)

VS Code — Dev Containers: [https://code.visualstudio.com/docs/devcontainers/containers](https://code.visualstudio.com/docs/devcontainers/containers)

Claude Code — integração com VS Code: [https://code.claude.com/docs/en/ide-integrations](https://code.claude.com/docs/en/ide-integrations)

Claude Code — permissões: [https://code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)

Claude Code — hooks: [https://code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide)

Codex — instruções AGENTS.md: [https://developers.openai.com/codex/guides/agents-md](https://developers.openai.com/codex/guides/agents-md)

Codex — IDE: [https://developers.openai.com/codex/ide](https://developers.openai.com/codex/ide)

GitHub — proteção de branches: [https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

Supabase — desenvolvimento local: [https://supabase.com/docs/guides/local-development/cli-workflows](https://supabase.com/docs/guides/local-development/cli-workflows)

Supabase — RLS: [https://supabase.com/docs/guides/database/postgres/row-level-security](https://supabase.com/docs/guides/database/postgres/row-level-security)

React: [https://react.dev/](https://react.dev/)

TypeScript: [https://www.typescriptlang.org/docs/](https://www.typescriptlang.org/docs/)

Vite: [https://vite.dev/guide/](https://vite.dev/guide/)

Vitest: [https://vitest.dev/guide/](https://vitest.dev/guide/)

Testing Library: [https://testing-library.com/docs/](https://testing-library.com/docs/)

Engenharia de requisitos — ISO/IEC/IEEE 29148: [https://www.iso.org/standard/72089.html](https://www.iso.org/standard/72089.html)

Qualidade do produto — ISO/IEC 25010: [https://www.iso.org/standard/78176.html](https://www.iso.org/standard/78176.html)

Qualidade em uso — ISO/IEC 25019: [https://www.iso.org/standard/78177.html](https://www.iso.org/standard/78177.html)

Acessibilidade — WCAG 2.2: [https://www.w3.org/TR/WCAG22/](https://www.w3.org/TR/WCAG22/)

Princípios ágeis: [https://agilemanifesto.org/principles.html](https://agilemanifesto.org/principles.html)

Limite desta versão: o manual foi redigido e suas fontes principais foram inspecionadas, mas o pipeline completo ainda não foi executado no ambiente local do usuário. A inspeção remota não valida instalações, scripts, hooks, integrações, banco, deploy ou UX. A primeira execução real deverá confirmar os procedimentos e permitir ajustes pontuais. Nenhum dado real foi migrado, nenhum arquivo do legado foi excluído e nenhuma funcionalidade foi implementada por esta elaboração do manual.