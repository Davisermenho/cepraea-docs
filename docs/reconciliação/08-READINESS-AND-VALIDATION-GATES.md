# READINESS & VALIDATION GATES

## Gate A — Prontidão da intenção

Avançar para elicitação profunda quando:

- [ ] problema inicial está explícito;
- [ ] objetivos iniciais existem;
- [ ] principais stakeholders foram identificados;
- [ ] escopo e não objetivos iniciais existem;
- [ ] restrições críticas conhecidas estão visíveis.

---

## Gate B — Prontidão do entendimento

Avançar para formalização de requisitos quando:

- [ ] conceitos de domínio críticos estão suficientemente definidos;
- [ ] principais atores foram explorados;
- [ ] fluxos críticos foram percorridos;
- [ ] regras críticas estão identificadas;
- [ ] ambiguidades de alto impacto foram resolvidas;
- [ ] hipóteses de alto impacto estão validadas, mitigadas ou aceitas;
- [ ] contradições relevantes foram tratadas;
- [ ] não existem questões de alto impacto + alta incerteza sem tratamento.

---

## Gate C — Prontidão dos requisitos

Avançar para drivers arquiteturais quando:

- [ ] requisitos críticos têm origem;
- [ ] requisitos críticos são verificáveis;
- [ ] NFRs importantes estão suficientemente mensuráveis;
- [ ] soluções técnicas prematuras foram removidas ou justificadas;
- [ ] conflitos entre requisitos foram tratados;
- [ ] prioridades estão suficientemente claras.

---

## Gate D — Prontidão arquitetural

Avançar para alternativas/decisões quando:

- [ ] drivers críticos foram identificados;
- [ ] cada driver tem rastreabilidade;
- [ ] tensões entre drivers estão visíveis;
- [ ] restrições operacionais, custo, equipe e tempo foram consideradas;
- [ ] riscos arquiteturais relevantes estão explícitos;
- [ ] recomendações genéricas foram separadas de necessidades contextuais.

---

## Gate E — Aceitação de decisão arquitetural

Uma ADR importante pode ser aceita quando:

- [ ] contexto está claro;
- [ ] origem é rastreável;
- [ ] pelo menos uma alternativa relevante foi considerada;
- [ ] trade-offs estão explícitos;
- [ ] a decisão não depende apenas de "boa prática";
- [ ] o teste contrafactual foi realizado;
- [ ] sabemos o que faria reconsiderar a decisão;
- [ ] existe cenário de validação associado.

---

# VALIDAÇÃO DA ARQUITETURA

## Tipo 1 — Cenário

### VAL-001 — [nome]

**Contexto:**  
[A confirmar]

**Estado inicial:**  
[A confirmar]

**Evento:**  
[A confirmar]

**Comportamento esperado:**  
[A confirmar]

**ADRs envolvidos:**  
[A confirmar]

**Componentes envolvidos:**  
[A confirmar]

**Resultado:** passou | falhou | parcial

**Falhas observadas:**  
[A confirmar]

---

## Tipo 2 — Adversarial

Tente criar condições plausíveis que façam a arquitetura falhar.

Perguntas:
- E se dois atores agirem simultaneamente?
- E se a conexão cair?
- E se uma mensagem for repetida?
- E se o cliente enviar dado inválido?
- E se uma operação for parcialmente concluída?
- E se houver informação contraditória?
- E se o serviço externo estiver indisponível?
- E se uma permissão mudar durante a operação?

---

## Tipo 3 — Contrafactual

Para cada decisão importante:

> Se removermos o requisito/driver que justificou a decisão, ela ainda seria escolhida?

Se sim, investigar genericidade ou preferência injustificada.

---

## Tipo 4 — Simplicidade

Perguntar:

- Que camada poderia ser removida?
- Que componente poderia ser fundido?
- Que abstração existe sem necessidade atual?
- Que complexidade foi adicionada apenas para futuro hipotético?
- Qual alternativa satisfaz os mesmos drivers com menor custo?

---

## Tipo 5 — Rastreabilidade

- [ ] todo componente importante tem origem;
- [ ] toda ADR importante tem drivers;
- [ ] todo driver tem requisitos/restrições/riscos;
- [ ] todo requisito crítico se conecta a objetivo;
- [ ] nenhum item crítico depende silenciosamente de hipótese invalidada.

---

## Resultado da Architecture Readiness Review

**Status:**  
- NÃO PRONTO
- PRONTO COM RISCOS
- PRONTO

**Questões bloqueadoras:**  
- 

**Riscos aceitos:**  
- 

**Decisões que podem avançar agora:**  
- 

**Decisões que devem esperar:**  
- 

**Próxima melhor pergunta:**  
[A confirmar]
