# ARCHITECTURE DRIVERS

**Propósito:** identificar quais forças realmente devem influenciar a arquitetura.

Nem todo requisito é um driver.

**Versão:** 0.1  
**Última atualização:** YYYY-MM-DD

---

## 1. Critério de driver

Um item é candidato a driver quando tem potencial de alterar significativamente:

- estrutura do sistema;
- fronteiras de componentes;
- modelo de dados;
- consistência;
- integração;
- segurança;
- distribuição;
- disponibilidade;
- persistência;
- sincronização;
- estratégia de deployment;
- custo operacional;
- complexidade;
- tecnologia base.

---

## 2. Drivers

### DRV-001 — [nome]

**Descrição:**  
[A confirmar]

**Origem:**  
NFR/FR/CON/RISK/OBJ/etc.

**Por que é arquiteturalmente significativo:**  
[A confirmar]

**Prioridade:** crítica | alta | média | baixa

**Força que exerce:**  
[A confirmar]

**Decisões potencialmente afetadas:**  
[A confirmar]

**Conflita com:**  
DRV-xxx

**Consequência se ignorado:**  
[A confirmar]

**Nível de evidência:** alto | médio | baixo

**Status:** candidato | confirmado | substituído

---

## 3. Tensões entre drivers

### TENSION-001

**Driver A:** DRV-xxx  
**Driver B:** DRV-xxx

**Tensão:**  
[A confirmar]

**Exemplo:**  
"alta resiliência offline" versus "baixa complexidade para equipe de 2 pessoas"

**Trade-off ainda em aberto:**  
[A confirmar]

---

## 4. Drivers rejeitados

| Item | Parecia driver porque | Por que não é driver | Destino |
|---|---|---|---|
| | | | requisito/boa prática/ideia futura |

---

## 5. Recomendações genéricas detectadas

| ID | Recomendação | Proveniência | Existe driver? | Decisão |
|---|---|---|---|---|
| GEN-001 | | GEN/STD | Sim/Não | rejeitar/investigar |

---

## 6. Ranking

| Driver | Impacto | Incerteza | Custo de erro | Reversibilidade | Prioridade final |
|---|---|---|---|---|---|
| DRV-001 | | | | | |

---

## 7. Gate para explorar arquitetura

- [ ] drivers críticos estão identificados;
- [ ] cada driver tem origem rastreável;
- [ ] tensões principais entre drivers estão explícitas;
- [ ] recomendações genéricas não foram confundidas com drivers;
- [ ] riscos arquiteturalmente significativos estão representados;
- [ ] restrições de equipe, tempo, custo e operação foram consideradas;
- [ ] questões de alto impacto restantes foram tratadas.
