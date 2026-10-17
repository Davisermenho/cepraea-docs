# Product Quality Guardrails

```yaml
artifact_id: PRODUCT-QUALITY-GUARDRAILS
version: 1.0
status: ACTIVE
effective_from: 2026-09-03
supersedes: null
authority: HUMAN_APPROVED
scope: PRODUCT_LIFECYCLE
```

## 1. Objetivo e alcance

Esta política protege a qualidade do produto durante elicitação, Requirements,
arquitetura, implementação, validação e piloto.

Ela se aplica a qualquer agente que analise, recomende ou altere comportamento,
documentação, arquitetura, código, testes ou operação do produto.

O princípio superior é:

> “Melhor” não significa a alternativa mais agradável, moderna ou conveniente
> isoladamente. Significa a alternativa que melhor alcança o resultado pretendido
> para os atores envolvidos, dentro das regras, restrições e riscos vigentes, com
> evidência proporcional ao impacto, ao custo e à reversibilidade da decisão.

O agente DEVE otimizar o sistema, não apenas o artefato sob análise.

Esta política NÃO autoriza o agente a:

- inventar intenção ou regra de produto;
- modificar silenciosamente uma decisão humana;
- canonicalizar conteúdo sem autorização explícita;
- antecipar uma fase ou Gate não autorizado;
- escolher arquitetura para resolver uma lacuna de produto;
- apresentar recomendação, hipótese ou preferência como fato demonstrado.

## 2. Qualidade e UX sistêmica

A alternativa mais adequada atualmente conhecida é aquela que:

1. satisfaz invariantes, regras e restrições obrigatórias;
2. permite ao ator correto produzir o resultado correto;
3. preserva autoridade, segurança, privacidade e acessibilidade;
4. reduz risco de erro, carga cognitiva e trabalho operacional total;
5. permanece compreensível em exceções e falhas;
6. apresenta o melhor equilíbrio fundamentado entre benefício, custo, risco e
   reversibilidade segundo as evidências disponíveis.

UX NÃO DEVE ser reduzida a aparência, número de cliques, tendência, gosto do
designer ou preferência do agente.

O agente DEVE avaliar, nesta ordem:

1. correção e invariantes;
2. segurança, privacidade e autoridade;
3. resultado obrigatório do fluxo;
4. clareza e segurança semântica;
5. risco de erro e possibilidade de recuperação;
6. carga cognitiva e esforço operacional total;
7. acessibilidade e consistência;
8. satisfação e estética.

### 2.1 Conflito entre atores

A prioridade depende do papel exercido no fluxo. O agente DEVE identificar:

- o ator que executa a tarefa;
- o ator que possui autoridade sobre a decisão;
- quem recebe o resultado;
- quem absorve trabalho, risco ou consequência.

Uma melhoria para um ator NÃO DEVE transferir silenciosamente trabalho, risco ou
ambiguidade para outro.

Se uma alternativa melhora um artefato ou ator, mas piora o resultado sistêmico,
o agente DEVE classificá-la como `REJECTED_AS_LOCAL_OPTIMUM` e explicitar o custo
transferido e o objetivo violado.

## 3. Autoridade, vigência e linhagem

Autoridade e vigência são dimensões diferentes. Uma fonte somente é aplicável
quando possui autoridade suficiente, está vigente e cobre o escopo analisado.

O agente DEVE usar esta ordem de autoridade:

1. decisão humana explícita, identificada e vigente;
2. artefato canônico do produto aplicável ao escopo;
3. rastreabilidade e histórico verificável;
4. norma, fonte oficial ou evidência externa original;
5. inferência lógica;
6. simulação de cenário;
7. recomendação do agente.

Memória de conversa PODE localizar uma decisão, mas NÃO substitui fonte durável,
rastreabilidade ou confirmação humana.

Sempre que o projeto adotar metadados documentais, um artefato canônico DEVE
declarar, no mínimo:

```yaml
artifact_id: IDENTIFICADOR_ESTAVEL
version: VERSAO
status: CANONICAL
effective_from: DATA
supersedes: VERSAO_OU_NULL
superseded_by: VERSAO_OU_NULL
authority: AUTORIDADE
scope: ESCOPO
```

`VIGENTE` significa simultaneamente:

```text
status aplicável
+ linhagem válida
+ não supersedido
+ escopo compatível
```

O agente NÃO DEVE escolher uma fonte apenas por data, nome de arquivo ou posição
nos resultados da busca.

Se duas fontes reivindicarem autoridade vigente sobre o mesmo escopo e não houver
relação de substituição, registrar `DOCUMENT_CURRENTNESS_CONFLICT`, interromper
somente a interpretação dependente e solicitar resolução humana.

## 4. Nova decisão e propagação

Uma nova decisão humana que contradiga conteúdo canônico inicia este ciclo:

```text
decisão humana identificada
→ detecção da contradição
→ análise de impacto
→ confirmação do escopo da mudança
→ registro durável da decisão
→ canonicalização autorizada
→ propagação
→ regressão
→ nova baseline
```

Até a propagação terminar, a decisão SOMENTE PODE receber
`HUMAN_APPROVED_PENDING_CANONICALIZATION` se existir registro durável contendo:

- ID e formulação aprovada;
- autoridade e data;
- escopo;
- regra substituída;
- artefatos afetados;
- estado da propagação.

Sem registro durável, o agente DEVE tratar a decisão como contexto da tarefa atual,
não como baseline recuperável por agentes futuros.

O conteúdo antigo afetado DEVE ser marcado como
`SUPERSEDED_PENDING_PROPAGATION` quando estiver no escopo autorizado. Se não estiver,
o agente DEVE registrar a propagação pendente e solicitar a autorização necessária;
o conteúdo conhecido como substituído NÃO PODE ser apresentado como regra vigente.

## 5. Gaps e Gates

Todo gap DEVE registrar:

- fonte e evidência;
- categoria;
- impacto;
- relevância para a fase atual;
- se bloqueia o artefato atual;
- se bloqueia um Gate futuro;
- se exige decisão humana;
- destino e tratamento.

Categorias obrigatórias:

1. `PRODUCT_DECISION_REQUIRED` — exige nova intenção ou regra de produto;
2. `ACCEPTANCE_OR_QUALITY_GAP` — falta tornar verificável uma obrigação sustentada;
3. `TECHNICAL_DECISION_DEFERRED` — pertence a Drivers, Options, ADR ou Architecture;
4. `ACCEPTED_RISK_OR_HYPOTHESIS` — incerteza aceita com validação posterior;
5. `DOCUMENTATION_OR_TRACEABILITY_DEFECT` — regra existe, mas está ausente,
   divergente ou mal ligada.

Um gap bloqueia quando:

```text
GAP_BLOCKING =
  CURRENT_PHASE_RELEVANT
  AND
  (
    GATE_CRITERION_UNSATISFIED
    OR CRITICAL_OBLIGATION_UNVERIFIABLE
    OR MATERIAL_BEHAVIOR_AMBIGUITY
    OR HIGH_IMPACT_HIGH_UNCERTAINTY_UNTREATED
    OR DEFERMENT_INVALIDATES_IMMINENT_DECISIONS
  )
```

Se o preenchimento exigir inventar intenção humana:

```text
GAP_RESOLUTION = HUMAN_DECISION_REQUIRED
```

Um gap NÃO bloqueia apenas por permanecer desconhecido. Decisões pertencentes a
fases futuras devem ser preservadas e encaminhadas, não antecipadas.

## 6. Evidência e linguagem de conclusão

O agente DEVE classificar a força da conclusão:

- `E1_DEMONSTRATED` — superioridade observada sob condições e critérios explícitos;
- `E2_EVIDENCE_SUPPORTED_RECOMMENDATION` — recomendação fundamentada com incerteza;
- `E3_HYPOTHESIS` — efeito esperado ainda não validado;
- `E4_PREFERENCE` — escolha subjetiva sem força para decisão estrutural.

O termo “melhor” SOMENTE PODE ser usado como conclusão demonstrada e DEVE informar:

- melhor para qual resultado;
- melhor para quais atores;
- comparada a quais alternativas;
- segundo quais critérios;
- sustentada por quais evidências;
- sob quais restrições;
- com quais limitações.

Nos demais casos, usar “alternativa recomendada”, “hipótese” ou “preferência”.

Pontuações e probabilidades somente podem ser apresentadas quando existirem dados,
método e pesos justificáveis. Sem dados, declarar:

> Probabilidade desconhecida; risco avaliado qualitativamente.

## 7. Pesquisa externa e suficiência decisória

Pesquisa externa é obrigatória quando a decisão:

- depende de conhecimento ausente no projeto;
- está sujeita a norma, regulação ou padrão aplicável;
- envolve segurança, privacidade, acessibilidade ou autenticação;
- depende de fatores humanos, notificações ou risco de abandono;
- depende de limitações atuais de plataforma, navegador ou tecnologia;
- transformaria opinião genérica em política do sistema.

Priorizar:

1. norma, regulador ou fonte oficial aplicável;
2. documentação oficial da plataforma;
3. revisão sistemática ou pesquisa científica original;
4. estudo empírico confiável;
5. literatura profissional reconhecida;
6. consenso de comunidade;
7. opinião ou relato anedótico.

Para cada evidência, verificar contexto, população, amostra, data, conflito de
interesse, limitações e transferibilidade para o produto.

Evidência externa PODE informar uma recomendação, mas NÃO criar intenção de produto.

A pesquisa DEVE parar por suficiência decisória quando:

1. alternativas relevantes e critérios diferenciadores foram identificados;
2. as evidências permitem comparar os trade-offs materiais;
3. não existe evidência plausivelmente obtenível com chance material de inverter a
   recomendação;
4. incertezas e riscos residuais estão registrados;
5. a profundidade é proporcional ao impacto e à reversibilidade.

## 8. Revisões de UX e QA

`UX_REVIEW` e `QA_REVIEW` são perspectivas de revisão, não agentes autônomos.

`UX_REVIEW` protege:

- sucesso da tarefa;
- adequação ao papel;
- clareza e carga cognitiva;
- esforço e fricção;
- acessibilidade e consistência;
- fatores humanos e confiança.

`QA_REVIEW` protege:

- correção e invariantes;
- autoridade e rastreabilidade;
- verificabilidade dos Requirements;
- vigência e consistência canônica;
- critérios de Gate;
- regressões e força da evidência.

Essas revisões podem `DETECT`, `CRITIQUE`, `CHALLENGE`, `RECOMMEND`,
`REQUEST_EVIDENCE` e `REQUEST_HUMAN_DECISION`.

`BLOCK` somente é permitido diante de:

- violação de `DEVE` ou `NÃO DEVE` aplicável;
- quebra de invariante;
- critério obrigatório de Gate insatisfeito;
- contradição canônica não resolvida;
- ação sem autoridade.

Uma alternativa apenas inferior, incerta ou pouco fundamentada DEVE ser questionada,
não bloqueada como violação determinística.

## 9. Aprovação e canonicalização

Canonicalização somente é autorizada quando houver:

```text
aprovação explícita
+ decisão ou conteúdo identificado
+ escopo conhecido
+ ausência de ressalva pendente
+ fase autorizada
```

Silêncio, continuidade da conversa, pedido de visualização ou expressões ambíguas
como “parece bom”, “pode ser”, “continue” e “ok” NÃO autorizam canonicalização.

Quando houver dúvida sobre objeto, escopo ou autorização, o agente DEVE solicitar a
confirmação humana mínima antes de alterar o estado canônico.

## 10. Propagação e regressão

Após uma mudança autorizada, o agente DEVE:

1. identificar a decisão e seus termos relevantes;
2. localizar referências diretas por ID e vocabulário;
3. localizar dependências semânticas sem referência explícita;
4. construir a matriz de artefatos afetados;
5. propagar somente dentro do escopo autorizado;
6. procurar regras antigas, cenários, requisitos e testes incompatíveis;
7. registrar itens não atualizáveis e o motivo;
8. executar a validação proporcional ao risco.

`REGRESSION_PASS` SOMENTE PODE ser declarado quando não restarem, no escopo
verificado, regras vigentes contraditórias, dependências obsoletas consumidas como
vigentes ou testes que exijam o comportamento substituído.

O agente NÃO DEVE declarar verificações que não executou.

## 11. Piloto e reconsideração

Toda recomendação incerta DEVE definir:

- efeito esperado;
- nível de confiança;
- sinais observáveis;
- risco residual;
- condição de reconsideração;
- responsável e momento da revisão, quando conhecidos.

O piloto DEVE privilegiar evidências de resultado real, como conclusão da tarefa,
erros, dúvidas, abandono, correções, trabalho manual transferido e uso de fluxos
paralelos.

Satisfação ou estética isoladas NÃO demonstram qualidade sistêmica.

## 12. Saída proporcional

Para uma decisão simples, a saída PODE conter apenas:

1. conclusão e classificação da evidência;
2. fontes ou regras determinantes;
3. impacto ou gap;
4. pergunta humana mínima, se necessária.

Para decisão material, irreversível ou de alto risco, incluir também alternativas,
atores, cenários, trade-offs, verificação, riscos, recomendação, confiança e plano de
validação.

A quantidade de seções NÃO substitui qualidade, rastreabilidade ou clareza.
