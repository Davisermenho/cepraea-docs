A implementação desses 20 refinamentos precisa ser feita com **controle de risco**, porque já ficou comprovado que reconstruir a página inteira gera regressão. A abordagem correta é dividir os ajustes em **blocos lógicos**, onde cada bloco mexe em uma área da página e passa por validação antes do próximo.

# **Premissa obrigatória**

A página 2 não deve ser redesenhada do zero.  
A base deve continuar sendo a **página 2 da versão 0.11**, porque ela já contém:

-   conteúdo correto;
-   logo correta;
-   tabela nominal correta;
-   dirigentes corretos;
-   observação correta;
-   arte lateral correta;
-   fundo branco;
-   identidade institucional coerente.

A próxima versão deve ser feita por **microintervenções locais**, não por reconstrução global.

# **Limitações consideradas**

## **Limitações da ferramenta**

Como estamos trabalhando sobre uma página renderizada em imagem/PDF, a edição não é como em um arquivo vetorial editável com camadas separadas. Isso significa que:

-   mover um bloco pode exigir apagar e redesenhar parte da página;
-   textos podem perder nitidez se forem manipulados como imagem;
-   alterações grandes em tabela e tipografia podem gerar desalinhamentos;
-   a logo e a arte lateral precisam ser aplicadas com cuidado para não parecerem coladas;
-   qualquer reconstrução ampla aumenta risco de mudar nomes, números ou posição dos elementos.

## **Limitações da IA**

A IA pode tentar “melhorar” visualmente e acabar alterando elementos aprovados. O risco principal é:

-   trocar a logo;
-   mudar grafia de nomes;
-   deformar a arte lateral;
-   recriar tabela;
-   alterar proporções;
-   transformar documento institucional em peça promocional;
-   criar uma versão visualmente bonita, mas fora do escopo aprovado.

## **Risco operacional**

O maior risco é regressão: a página parecer diferente da base aprovada.  
Por isso, cada bloco deve ter **critério de parada**.

Se um bloco alterar mais do que deveria, ele deve ser descartado e refeito.

# **Ordem lógica de implementação**

A implementação deve seguir esta sequência:

1.  cabeçalho;
2.  régua técnica;
3.  espaçamentos verticais;
4.  tabela;
5.  arte lateral;
6.  dirigentes;
7.  observação;
8.  rodapé;
9.  auditoria final.

Essa ordem evita que ajustes no rodapé ou tabela sejam feitos antes de estabilizar o topo da página.

# **Bloco 1 — Cabeçalho e logo**

## **Refinamentos incluídos**

1.  Reduzir o peso visual do título “Relação Nominal”.
2.  Melhorar a proporção entre título e subtítulo.
3.  Ajustar a posição da logo no cabeçalho.
4.  Reduzir levemente a logo.
5.  Aumentar o respiro direito da logo.

## **Objetivo**

Deixar o cabeçalho mais institucional, menos pesado e mais equilibrado.

## **Ações**

-   reduzir levemente o título;
-   manter “Relação Nominal” como informação principal;
-   ajustar o subtítulo para parecer subordinado;
-   posicionar a logo à direita com mais respiro;
-   preservar a cor original verde da logo;
-   reduzir a logo cerca de 8% a 12%;
-   alinhar a logo ao eixo óptico do cabeçalho.

## **Limitações**

Como o cabeçalho foi parcialmente reconstruído em imagem, qualquer ajuste exige apagar e redesenhar essa faixa. Isso precisa ser feito apenas na área superior, sem tocar na tabela.

## **Riscos**

-   logo voltar para versão errada;
-   logo ficar deformada;
-   título perder força;
-   cabeçalho parecer vazio demais;
-   desalinhamento entre título, subtítulo e logo.

## **Critério de validação**

O cabeçalho deve parecer uma única faixa institucional.  
A logo deve estar à direita, em verde original, sem deformação e sem competir com o título.

# **Bloco 2 — Régua de dados técnicos**

## **Refinamentos incluídos**

1.  Suavizar a régua de dados técnicos.
2.  Melhorar a hierarquia dos dados técnicos.
3.  Reduzir a altura da faixa de dados técnicos.
4.  Padronizar espessura e cor das linhas.

## **Objetivo**

Transformar a linha de Data, Equipe, Categoria e Local em uma ficha técnica elegante, sem aparência de planilha.

## **Ações**

-   manter os dados em linha única;
-   reduzir contraste dos separadores verticais;
-   deixar rótulos com peso menor;
-   manter valores mais destacados;
-   reduzir a altura da faixa;
-   padronizar linhas superiores e inferiores;
-   usar cinza/roxo discreto, sem excesso.

## **Limitações**

Os dados são texto rasterizado quando inseridos na imagem. Para manter qualidade, o ideal é redesenhar apenas essa faixa em alta resolução.

## **Riscos**

-   informações ficarem pequenas demais;
-   linha técnica perder legibilidade;
-   separadores ficarem fortes demais;
-   texto sair desalinhado.

## **Critério de validação**

A régua deve ser lida rapidamente e parecer parte do cabeçalho, sem cards, sem boxes e sem ícones.

# **Bloco 3 — Compressão vertical e alinhamento do corpo**

## **Refinamentos incluídos**

1.  Diminuir o espaço entre cabeçalho e corpo.
2.  Subir a tabela nominal.
3.  Subir a arte lateral junto com a tabela.
4.  Reduzir o vazio entre tabela e arte.

## **Objetivo**

Remover os espaços mortos marcados no print e deixar a página mais compacta, coesa e editorial.

## **Ações**

-   reduzir o espaço entre cabeçalho e tabela;
-   subir a tabela nominal;
-   subir a arte lateral na mesma proporção;
-   manter a distância entre tabela e arte suficiente para leitura;
-   não alterar conteúdo da tabela;
-   não trocar a arte lateral.

## **Limitações**

Subir a tabela e a arte pode exigir copiar blocos grandes da página. Isso é possível, mas deve ser feito como deslocamento controlado, não como redesenho.

## **Riscos**

-   cortar parte da arte lateral;
-   aproximar demais arte e tabela;
-   criar manchas/resíduos no fundo branco;
-   desalinhamento com dirigentes e observação.

## **Critério de validação**

A tabela e a arte devem começar mais próximas do cabeçalho, alinhadas visualmente, sem sensação de vazio morto.

# **Bloco 4 — Tabela nominal**

## **Refinamentos incluídos**

1.  Suavizar as linhas internas da tabela.
2.  Refinar o cabeçalho roxo da tabela.
3.  Ajustar o padding interno dos nomes.
4.  Padronizar espessura e cor das linhas.

## **Objetivo**

Elevar a tabela de “grade funcional” para “componente editorial institucional”.

## **Ações**

-   manter todos os nomes exatamente iguais;
-   manter os números exatamente iguais;
-   suavizar linhas internas;
-   melhorar espaçamento interno dos nomes;
-   manter o cabeçalho roxo, porém com acabamento mais limpo;
-   não alterar ordem, largura geral ou estrutura sem necessidade.

## **Limitações**

Este é o bloco mais arriscado, porque mexer na tabela pode alterar texto. Como a tabela está correta, o ideal é fazer apenas ajustes leves ou deixar para uma etapa posterior.

## **Riscos**

-   erro de grafia;
-   perda de nitidez;
-   desalinhamento de linhas;
-   tabela ficar diferente da versão aprovada;
-   regressão visual.

## **Critério de validação**

Se qualquer nome ou número mudar, o bloco reprova.  
A tabela deve continuar reconhecível como a mesma, apenas mais refinada.

## **Recomendação de segurança**

Este bloco deve ser aplicado somente depois de aprovar cabeçalho e espaçamentos. Se houver risco alto, manter a tabela intacta.

# **Bloco 5 — Arte lateral**

## **Refinamentos incluídos**

1.  Subir a arte lateral junto com a tabela.
2.  Reduzir o vazio entre tabela e arte.

## **Objetivo**

Melhorar a integração entre imagem e conteúdo, sem alterar a arte.

## **Ações**

-   manter a mesma arte;
-   mover apenas junto com o corpo;
-   preservar lance completo;
-   manter Roberta e defensora visíveis;
-   evitar que a areia invada a tabela;
-   preservar fundo branco.

## **Limitações**

A arte não está em camada editável separada. Se for deslocada, será necessário recortar e recompor a área. Isso pode gerar bordas se não for feito com cuidado.

## **Riscos**

-   corte nos pés/pernas;
-   areia parecer remendada;
-   defensora sair parcialmente da página;
-   arte ficar colada demais à tabela.

## **Critério de validação**

A arte deve continuar igual, apenas melhor posicionada e mais integrada.

# **Bloco 6 — Dirigentes**

## **Refinamentos incluídos**

1.  Reequilibrar o bloco “Dirigentes”.
2.  Reduzir o peso das células A/B.
3.  Aproximar a observação dos dirigentes.

## **Objetivo**

Fazer a seção de dirigentes parecer secundária, elegante e integrada à tabela.

## **Ações**

-   aproximar dirigentes da tabela;
-   reduzir peso visual do bloco;
-   suavizar roxo das células A/B ou diminuir a área preenchida;
-   manter nomes corretos;
-   alinhar com a largura da tabela.

## **Limitações**

Como o bloco já está funcional, mudanças excessivas podem piorar. A intervenção deve ser mínima.

## **Riscos**

-   nomes desalinharem;
-   bloco parecer desconectado;
-   A/B ficarem pequenos demais;
-   criar excesso de espaço à direita.

## **Critério de validação**

O bloco deve parecer continuação da relação nominal, não um elemento solto.

# **Bloco 7 — Observação**

## **Refinamentos incluídos**

1.  Aproximar a observação dos dirigentes.
2.  Remover excesso de vazio no rodapé.

## **Objetivo**

Transformar a observação em nota editorial integrada, reduzindo espaço vazio inferior.

## **Ações**

-   subir a observação;
-   manter sem box pesado;
-   alinhar com a coluna principal;
-   manter texto integral;
-   usar linha discreta ou recuo lateral;
-   evitar que pareça alerta ou card.

## **Limitações**

O texto precisa continuar legível. Reduzir demais o espaço pode deixar a página apertada.

## **Riscos**

-   observação ficar espremida;
-   perder hierarquia;
-   parecer rodapé improvisado;
-   criar desequilíbrio com a arte lateral.

## **Critério de validação**

A observação deve fechar o documento com sobriedade, sem parecer perdida no espaço inferior.

# **Bloco 8 — Rodapé e fechamento visual**

## **Refinamentos incluídos**

1.  Remover excesso de vazio no rodapé.
2.  Padronizar espessura e cor das linhas.

## **Objetivo**

Dar acabamento final institucional ao documento.

## **Ações**

-   reduzir espaço morto no rodapé;
-   manter linha inferior discreta;
-   evitar duas linhas fortes;
-   se necessário, usar apenas uma linha de fechamento;
-   não adicionar novos elementos sem aprovação.

## **Limitações**

O rodapé deve continuar limpo. Acrescentar muito texto pode poluir.

## **Riscos**

-   página parecer apertada;
-   rodapé competir com observação;
-   visual ficar pesado.

## **Critério de validação**

O fim da página deve parecer intencional, limpo e institucional.

# **Bloco 9 — Auditoria final**

## **Objetivo**

Garantir que nenhuma regressão foi introduzida.

## **Verificações obrigatórias**

### **Conteúdo**

-   nomes corretos;
-   números corretos;
-   Davi Sermenho correto;
-   Thiago Willian de Almeida correto;
-   observação correta;
-   data, equipe, categoria e local corretos.

### **Visual**

-   logo correta;
-   logo verde original;
-   logo à direita;
-   título legível;
-   cabeçalho unificado;
-   sem boxes nos dados técnicos;
-   tabela legível;
-   arte lateral preservada;
-   observação sem box pesado;
-   espaços mortos reduzidos.

### **Estrutura**

-   PDF com 2 páginas;
-   página 1 preservada;
-   página 2 refinada;
-   sem uso da v0.7;
-   sem reconstrução total.

# **Estratégia de execução recomendada**

Para reduzir risco, eu recomendo dividir em **duas versões**, não aplicar tudo de uma vez.

## **Versão 0.12 — ajustes de alto impacto e baixo risco**

Aplicar:

-   Bloco 1: cabeçalho e logo;
-   Bloco 2: régua técnica;
-   Bloco 3: redução de espaço entre cabeçalho e corpo;
-   Bloco 8: rodapé/fechamento leve.

Essa versão resolve o maior problema visual sem mexer muito na tabela.

## **Versão 0.13 — ajustes finos do corpo**

Depois de aprovar a v0.12, aplicar:

-   Bloco 4: tabela;
-   Bloco 5: arte lateral;
-   Bloco 6: dirigentes;
-   Bloco 7: observação.

Essa separação evita repetir o erro da v0.7.

# **Ordem de implementação lógica**

## **Fase 1 — estabilização do topo**

1.  Cabeçalho.
2.  Logo.
3.  Régua técnica.
4.  Espaço entre cabeçalho e corpo.

## **Fase 2 — equilíbrio do corpo**

1.  Tabela.
2.  Arte lateral.
3.  Espaço entre colunas.

## **Fase 3 — fechamento institucional**

1.  Dirigentes.
2.  Observação.
3.  Rodapé.

## **Fase 4 — validação**

1.  Renderizar.
2.  Comparar com a base.
3.  Conferir conteúdo.
4.  Entregar PDF.

# **Conclusão**

O caminho mais seguro é implementar os 20 refinamentos em blocos, com validação entre eles. A próxima execução recomendada deve ser a **v0.12**, aplicando apenas os ajustes de **cabeçalho, régua técnica, espaçamento superior e rodapé**, porque esses são os refinamentos de maior impacto visual e menor risco de regressão.