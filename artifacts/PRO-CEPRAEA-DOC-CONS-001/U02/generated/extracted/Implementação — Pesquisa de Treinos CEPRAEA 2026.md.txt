# Implementação — Pesquisa de Treinos CEPRAEA 2026

Converted from: Implementação — Pesquisa de Treinos CEPRAEA 2026.xlsx

---

## File Information

- **File Name**: Implementação — Pesquisa de Treinos CEPRAEA 2026.xlsx
- **File Size**: 226.23 KB
- **Modified Date**: 8/23/2026, 12:17:22 PM

## Content

## 📋 Worksheet: CONTROLE

**Data Dimensions**: 26 rows x 4 columns

| IMPLEMENTAÇÃO — PESQUISA DE TREINOS CEPRAEA 2026 |   |   |   |
| --- | --- | --- | --- |
| Campo | Valor | Estado | Observação |
| Versão | PESQ-CEPRAEA-2026-v1 | CONGELADA | Alterar somente com nova versão |
| Data da pesquisa | 04/08/2026 | ATIVA | Início da implementação |
| Etapa final — DATABASE | 25/09/2026 a 27/09/2026 | CANÔNICO | Fonte única operacional: CEPRAEA DATABASE → DB_COMPETICOES → COMP-2026-012. |
| Referência anterior — guia CBHb | 23/09/2026 a 27/09/2026 | SUPERADA | Preservada apenas para auditoria. Não usar operacionalmente; substituída pelo calendário canônico. |
| Local | São Miguel do Iguaçu/PR | CANÔNICO | Fonte única operacional: CEPRAEA DATABASE → DB_COMPETICOES. |
| Viagem | 17/09/2026 | PREMISSA | Quinta-feira anterior ao período competitivo |
| Inscrição | 10/09/2026 | FONTE GUIA | Página 6 |
| Lista nominal | 18/09/2026 | FONTE GUIA | Página 6 |
| Treino oficial | 90 minutos | CONFIRMADO | Duração fixa |
| Bloco extra | 30 minutos | OPCIONAL | Antes ou depois |
| Limite noturno | 22:15 | BLOQUEANTE | Nenhuma atividade após esse horário |
| Atletas ativas | 19 | VALIDADO | Ordem alfabética |
| Horários semanais candidatos | 35 | VALIDADO | 35 opções |
| Oportunidades extras até a viagem | 30 | VALIDADO | Sábado manhã e tarde separados |
| Treinos regulares até a viagem | 12 | VALIDADO | Quintas e domingos |
| Máximo teórico de sessões | 42 | CENÁRIO | 30 extras + 12 regulares |
| LINKS GERADOS PELO APPS SCRIPT |   |   |   |
| Recurso | URL/ID | Status | Preenchimento |
| Formulário A — responder | https://docs.google.com/forms/d/e/1FAIpQLScX3djb7H6EvO5SGI8yzpZR4DZqvJL8t0zLw5ldMGHUfYfcZA/viewform | EM USO — 13 RESPOSTAS | Estrutura V4 confirmada pelos 26 cabeçalhos e respostas recebidas. |
| Formulário A — editar | https://docs.google.com/forms/d/1ifypH0xqTVQR9Z8xFOu7TADQLG7aeQNLSJQJGgCCyRQ/edit | ARQUIVO TÉCNICO | Link de edição; não distribuir a respondentes. |
| Respostas A — planilha | https://docs.google.com/spreadsheets/d/16fWLMQr6ay1lqlgqGtRlthFTQhkM9NSIGlTfOsKD-vc/edit | CONECTADA — 13 RESPOSTAS | Fonte bruta preservada; normalização materializada em 09/08/2026. |
| Formulário B — responder | https://docs.google.com/forms/d/e/1FAIpQLScZrv7yN1OhsU5Xdq5oMeai86Pvcqr3B3PGvuMxbdnZsYzCmA/viewform | VALIDADO — ANÔNIMO | 12 respostas; nenhuma coluna de nome, conta ou e-mail. |
| Formulário B — editar | https://docs.google.com/forms/d/1BkB3ZPiVCwyCRMUdvRy9jUnYKDxIQU-l0nERzF0xXeI/edit | ARQUIVO TÉCNICO | Link de edição; configurações detalhadas requerem verificação manual no Forms. |
| Respostas B — planilha | https://docs.google.com/spreadsheets/d/1GrjeYxPDPw39vwAaP43CV-GVdpy7m_xvveabjVpZ--g/edit | CONECTADA — 12 RESPOSTAS | Fonte bruta preservada; normalização materializada em 09/08/2026. |

---

## 📋 Worksheet: CONFIG

**Data Dimensions**: 21 rows x 4 columns

| PARÂMETROS OPERACIONAIS |   |   |   |
| --- | --- | --- | --- |
| chave | valor | tipo | observacao |
| survey_version | PESQ-CEPRAEA-2026-v1 | texto | Versão congelada |
| survey_date | 8/4/2026 | data | Data de início |
| event_start_operational | 9/25/2026 | data | CEPRAEA DATABASE → DB_COMPETICOES / COMP-2026-012 |
| event_start_guide | 9/23/2026 | data | Histórico superado — não usar operacionalmente |
| event_end | 9/27/2026 | data | CEPRAEA DATABASE → DB_COMPETICOES / COMP-2026-012 |
| trip_date | 9/17/2026 | data | Premissa do treinador |
| last_candidate_training | 9/15/2026 | data | Último dia candidato pesquisado |
| official_duration_minutes | 90 | inteiro | Duração fixa |
| extra_duration_minutes | 30 | inteiro | Opcional |
| night_max_end | 22:15 | hora | Limite absoluto |
| recurrence_threshold | 4 de 6 | regra | Núcleo recorrente inicial |
| cqv_reference_athletes | 14 | inteiro | Referência vigente |
| response_absence | SEM_RESPOSTA | texto | Nunca converter em NÃO |
| raw_form_a_spreadsheet_id | 16fWLMQr6ay1lqlgqGtRlthFTQhkM9NSIGlTfOsKD-vc | texto | Fonte bruta nominal; 13 respostas preservadas. |
| raw_form_b_spreadsheet_id | 1GrjeYxPDPw39vwAaP43CV-GVdpy7m_xvveabjVpZ--g | texto | Fonte bruta anônima; 12 respostas preservadas. |
| normalization_mode | MATERIALIZADA_COM_RASTREABILIDADE | texto | Dados brutos preservados; apenas camadas derivadas foram gravadas. |
| normalization_last_run | 2026-08-09T16:18:09-03:00 | timestamp | Execução auditada pelo agente no Google Drive. |
| form_a_rows_normalized | 2730 | inteiro | 13 respondentes × 210 combinações de data/horário. |
| form_b_rows_normalized | 696 | inteiro | 12 respondentes × 58 itens; sem identidade nominal. |

---

## 📋 Worksheet: ATLETAS

**Data Dimensions**: 20 rows x 9 columns

| athlete_id | nome_exibicao | funcao_principal | ofensiva_principal | ofensiva_secundaria | defensiva_principal | defensiva_secundaria | goleira | status_validacao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ATH-0001 | Aline Augusto | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   | VALIDADO |
| ATH-0002 | Aline Kecia | ATAQUE | LATERAL DIREITA | CENTRAL DIREITA |   |   |   | VALIDADO |
| ATH-0003 | Aline Mello | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   | VALIDADO |
| ATH-0004 | Beatriz Correia | ATAQUE | LATERAL ESQUERDA | PIVÔ |   |   |   | VALIDADO |
| ATH-0005 | Bruna Xavier | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   | VALIDADO |
| ATH-0006 | Carolina Bezerra | GOLEIRA |   |   |   |   | GOLEIRA | VALIDADO |
| ATH-0007 | Carolina Peixinho | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   | VALIDADO |
| ATH-0008 | Fernanda Campbell | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   | VALIDADO |
| ATH-0009 | Gabi Peixinho | DEFESA |   |   | DEFENSORA SOLTA | DEFENSORA AVANÇADA |   | VALIDADO |
| ATH-0019 | Gilvania Balbino | GOLEIRA |   |   |   |   | GOLEIRA | VALIDADO |
| ATH-0010 | Jaiana Vasconcelos | ATAQUE | CENTRAL | LATERAL DIREITA |   |   |   | VALIDADO |
| ATH-0011 | Marleide Nunes | ATAQUE | PIVÔ | CENTRAL ESQUERDA |   |   |   | VALIDADO |
| ATH-0012 | Myllena Amado | ATAQUE | LATERAL ESQUERDA |   |   | DEFENSORA SOLTA |   | VALIDADO |
| ATH-0013 | Paloma Caneca | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   | VALIDADO |
| ATH-0014 | Paola Wolff | GOLEIRA |   |   |   |   | GOLEIRA | VALIDADO |
| ATH-0015 | Rafaela Dillmann | DEFESA |   | LATERAL DIREITA | DEFENSORA SOLTA |   |   | VALIDADO |
| ATH-0016 | Rita Seabra | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   | VALIDADO |
| ATH-0017 | Roberta Hernandez | ATAQUE | LATERAL ESQUERDA |   |   | DEFENSORA SOLTA |   | VALIDADO |
| ATH-0018 | Taís de Almeida | ATAQUE | LATERAL DIREITA | CENTRAL DIREITA |   |   |   | VALIDADO |

---

## 📋 Worksheet: SLOTS

**Data Dimensions**: 36 rows x 10 columns

| slot_id | dia | periodo | inicio | fim | duracao_min | extra_antes_inicio | extra_depois_fim | extra_depois_permitido | limite_noturno |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEG-NOITE-1930 | Segunda-feira | NOITE | 19:30 | 21:00 | 90 | 19:00 | 21:30 | SIM | 22:15 |
| SEG-NOITE-1945 | Segunda-feira | NOITE | 19:45 | 21:15 | 90 | 19:15 | 21:45 | SIM | 22:15 |
| SEG-NOITE-2000 | Segunda-feira | NOITE | 20:00 | 21:30 | 90 | 19:30 | 22:00 | SIM | 22:15 |
| SEG-NOITE-2015 | Segunda-feira | NOITE | 20:15 | 21:45 | 90 | 19:45 | 22:15 | SIM | 22:15 |
| SEG-NOITE-2030 | Segunda-feira | NOITE | 20:30 | 22:00 | 90 | 20:00 | NÃO PERMITIDO | NÃO | 22:15 |
| TER-NOITE-1900 | Terça-feira | NOITE | 19:00 | 20:30 | 90 | 18:30 | 21:00 | SIM | 22:15 |
| TER-NOITE-1915 | Terça-feira | NOITE | 19:15 | 20:45 | 90 | 18:45 | 21:15 | SIM | 22:15 |
| TER-NOITE-1930 | Terça-feira | NOITE | 19:30 | 21:00 | 90 | 19:00 | 21:30 | SIM | 22:15 |
| TER-NOITE-1945 | Terça-feira | NOITE | 19:45 | 21:15 | 90 | 19:15 | 21:45 | SIM | 22:15 |
| TER-NOITE-2000 | Terça-feira | NOITE | 20:00 | 21:30 | 90 | 19:30 | 22:00 | SIM | 22:15 |
| TER-NOITE-2015 | Terça-feira | NOITE | 20:15 | 21:45 | 90 | 19:45 | 22:15 | SIM | 22:15 |
| TER-NOITE-2030 | Terça-feira | NOITE | 20:30 | 22:00 | 90 | 20:00 | NÃO PERMITIDO | NÃO | 22:15 |
| SEX-NOITE-1900 | Sexta-feira | NOITE | 19:00 | 20:30 | 90 | 18:30 | 21:00 | SIM | 22:15 |
| SEX-NOITE-1915 | Sexta-feira | NOITE | 19:15 | 20:45 | 90 | 18:45 | 21:15 | SIM | 22:15 |
| SEX-NOITE-1930 | Sexta-feira | NOITE | 19:30 | 21:00 | 90 | 19:00 | 21:30 | SIM | 22:15 |
| SEX-NOITE-1945 | Sexta-feira | NOITE | 19:45 | 21:15 | 90 | 19:15 | 21:45 | SIM | 22:15 |
| SEX-NOITE-2000 | Sexta-feira | NOITE | 20:00 | 21:30 | 90 | 19:30 | 22:00 | SIM | 22:15 |
| SEX-NOITE-2015 | Sexta-feira | NOITE | 20:15 | 21:45 | 90 | 19:45 | 22:15 | SIM | 22:15 |
| SEX-NOITE-2030 | Sexta-feira | NOITE | 20:30 | 22:00 | 90 | 20:00 | NÃO PERMITIDO | NÃO | 22:15 |
| SAB-MANHA-0730 | Sábado | MANHA | 07:30 | 09:00 | 90 | 07:00 | 09:30 | SIM |   |
| SAB-MANHA-0745 | Sábado | MANHA | 07:45 | 09:15 | 90 | 07:15 | 09:45 | SIM |   |
| SAB-MANHA-0800 | Sábado | MANHA | 08:00 | 09:30 | 90 | 07:30 | 10:00 | SIM |   |
| SAB-MANHA-0815 | Sábado | MANHA | 08:15 | 09:45 | 90 | 07:45 | 10:15 | SIM |   |
| SAB-MANHA-0830 | Sábado | MANHA | 08:30 | 10:00 | 90 | 08:00 | 10:30 | SIM |   |
| SAB-TARDE-1600 | Sábado | TARDE | 16:00 | 17:30 | 90 | 15:30 | 18:00 | SIM |   |
| SAB-TARDE-1615 | Sábado | TARDE | 16:15 | 17:45 | 90 | 15:45 | 18:15 | SIM |   |
| SAB-TARDE-1630 | Sábado | TARDE | 16:30 | 18:00 | 90 | 16:00 | 18:30 | SIM |   |
| SAB-TARDE-1645 | Sábado | TARDE | 16:45 | 18:15 | 90 | 16:15 | 18:45 | SIM |   |
| SAB-TARDE-1700 | Sábado | TARDE | 17:00 | 18:30 | 90 | 16:30 | 19:00 | SIM |   |
| SAB-TARDE-1715 | Sábado | TARDE | 17:15 | 18:45 | 90 | 16:45 | 19:15 | SIM |   |
| SAB-TARDE-1730 | Sábado | TARDE | 17:30 | 19:00 | 90 | 17:00 | 19:30 | SIM |   |
| SAB-TARDE-1745 | Sábado | TARDE | 17:45 | 19:15 | 90 | 17:15 | 19:45 | SIM |   |
| SAB-TARDE-1800 | Sábado | TARDE | 18:00 | 19:30 | 90 | 17:30 | 20:00 | SIM |   |
| SAB-TARDE-1815 | Sábado | TARDE | 18:15 | 19:45 | 90 | 17:45 | 20:15 | SIM |   |
| SAB-TARDE-1830 | Sábado | TARDE | 18:30 | 20:00 | 90 | 18:00 | 20:30 | SIM |   |

---

## 📋 Worksheet: CALENDARIO

**Data Dimensions**: 43 rows x 8 columns

| data | dia | periodo | tipo_sessao | estado | horario_escolhido | finalidade | observacao |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8/6/2026 | Quinta-feira | NOITE | REGULAR | MANTER |   |   | Treino regular |
| 8/7/2026 | Sexta-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/8/2026 | Sábado | MANHA | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/8/2026 | Sábado | TARDE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/9/2026 | Domingo | MANHA | REGULAR | MANTER |   |   | Treino regular |
| 8/10/2026 | Segunda-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/11/2026 | Terça-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/13/2026 | Quinta-feira | NOITE | REGULAR | MANTER |   |   | Treino regular |
| 8/14/2026 | Sexta-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/15/2026 | Sábado | MANHA | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/15/2026 | Sábado | TARDE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/16/2026 | Domingo | MANHA | REGULAR | MANTER |   |   | Treino regular |
| 8/17/2026 | Segunda-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/18/2026 | Terça-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/20/2026 | Quinta-feira | NOITE | REGULAR | MANTER |   |   | Treino regular |
| 8/21/2026 | Sexta-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/22/2026 | Sábado | MANHA | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/22/2026 | Sábado | TARDE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/23/2026 | Domingo | MANHA | REGULAR | MANTER |   |   | Treino regular |
| 8/24/2026 | Segunda-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/25/2026 | Terça-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/27/2026 | Quinta-feira | NOITE | REGULAR | MANTER |   |   | Treino regular |
| 8/28/2026 | Sexta-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/29/2026 | Sábado | MANHA | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/29/2026 | Sábado | TARDE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 8/30/2026 | Domingo | MANHA | REGULAR | MANTER |   |   | Treino regular |
| 8/31/2026 | Segunda-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/1/2026 | Terça-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/3/2026 | Quinta-feira | NOITE | REGULAR | MANTER |   |   | Treino regular |
| 9/4/2026 | Sexta-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/5/2026 | Sábado | MANHA | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/5/2026 | Sábado | TARDE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/6/2026 | Domingo | MANHA | REGULAR | MANTER |   |   | Treino regular |
| 9/7/2026 | Segunda-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/8/2026 | Terça-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/10/2026 | Quinta-feira | NOITE | REGULAR | MANTER |   |   | Treino regular |
| 9/11/2026 | Sexta-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/12/2026 | Sábado | MANHA | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/12/2026 | Sábado | TARDE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/13/2026 | Domingo | MANHA | REGULAR | MANTER |   |   | Treino regular |
| 9/14/2026 | Segunda-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |
| 9/15/2026 | Terça-feira | NOITE | EXTRA_CANDIDATO | CANDIDATO |   |   | Até a viagem |

---

## 📋 Worksheet: FORM_A

**Data Dimensions**: 26 rows x 7 columns

| secao | item_id | pergunta | tipo | opcoes | obrigatoria | regra |
| --- | --- | --- | --- | --- | --- | --- |
| GERAL | A01 | Qual é o seu nome? | LISTA SUSPENSA | Lista alfabética de atletas | SIM | Identificação nominal |
| GERAL | A02 | Em uma semana normal, quantos treinos extras você consegue manter? | MÚLTIPLA ESCOLHA COM NAVEGAÇÃO | 1 \\| 2 \\| 3 \\| 4 \\| 5 \\| Depende \\| Nenhum | SIM | Nenhum pula todos os períodos |
| Segunda-feira à noite | A03 | Você consegue participar de pelo menos uma das datas de segunda-feira à noite? | MÚLTIPLA ESCOLHA COM NAVEGAÇÃO | Sim \\| Não | SIM | Sim abre detalhes; Não avança |
| Segunda-feira à noite | A04 | Segunda-feira à noite — em quais datas você consegue participar? | CAIXAS DE SELEÇÃO | 10/08 \\| 17/08 \\| 24/08 \\| 31/08 \\| 07/09 \\| 14/09 | SIM | Exibida somente após resposta Sim |
| Segunda-feira à noite | A05 | Segunda-feira à noite — em quais horários você consegue iniciar o treino? | CAIXAS DE SELEÇÃO | 19h30 às 21h \\| 19h45 às 21h15 \\| 20h às 21h30 \\| 20h15 às 21h45 \\| 20h30 às 22h | SIM | Exibida somente após resposta Sim |
| Segunda-feira à noite | A06 | Segunda-feira à noite — você consegue fazer 30 minutos extras? | MÚLTIPLA ESCOLHA | Antes \\| Depois \\| Antes ou depois \\| Não \\| Depende | SIM | Exibida somente após resposta Sim |
| Terça-feira à noite | A07 | Você consegue participar de pelo menos uma das datas de terça-feira à noite? | MÚLTIPLA ESCOLHA COM NAVEGAÇÃO | Sim \\| Não | SIM | Sim abre detalhes; Não avança |
| Terça-feira à noite | A08 | Terça-feira à noite — em quais datas você consegue participar? | CAIXAS DE SELEÇÃO | 11/08 \\| 18/08 \\| 25/08 \\| 01/09 \\| 08/09 \\| 15/09 | SIM | Exibida somente após resposta Sim |
| Terça-feira à noite | A09 | Terça-feira à noite — em quais horários você consegue iniciar o treino? | CAIXAS DE SELEÇÃO | 19h às 20h30 \\| 19h15 às 20h45 \\| 19h30 às 21h \\| 19h45 às 21h15 \\| 20h às 21h30 \\| 20h15 às 21h45 \\| 20h30 às 22h | SIM | Exibida somente após resposta Sim |
| Terça-feira à noite | A10 | Terça-feira à noite — você consegue fazer 30 minutos extras? | MÚLTIPLA ESCOLHA | Antes \\| Depois \\| Antes ou depois \\| Não \\| Depende | SIM | Exibida somente após resposta Sim |
| Sexta-feira à noite | A11 | Você consegue participar de pelo menos uma das datas de sexta-feira à noite? | MÚLTIPLA ESCOLHA COM NAVEGAÇÃO | Sim \\| Não | SIM | Sim abre detalhes; Não avança |
| Sexta-feira à noite | A12 | Sexta-feira à noite — em quais datas você consegue participar? | CAIXAS DE SELEÇÃO | 07/08 \\| 14/08 \\| 21/08 \\| 28/08 \\| 04/09 \\| 11/09 | SIM | Exibida somente após resposta Sim |
| Sexta-feira à noite | A13 | Sexta-feira à noite — em quais horários você consegue iniciar o treino? | CAIXAS DE SELEÇÃO | 19h às 20h30 \\| 19h15 às 20h45 \\| 19h30 às 21h \\| 19h45 às 21h15 \\| 20h às 21h30 \\| 20h15 às 21h45 \\| 20h30 às 22h | SIM | Exibida somente após resposta Sim |
| Sexta-feira à noite | A14 | Sexta-feira à noite — você consegue fazer 30 minutos extras? | MÚLTIPLA ESCOLHA | Antes \\| Depois \\| Antes ou depois \\| Não \\| Depende | SIM | Exibida somente após resposta Sim |
| Sábado pela manhã | A15 | Você consegue participar de pelo menos uma das datas de sábado pela manhã? | MÚLTIPLA ESCOLHA COM NAVEGAÇÃO | Sim \\| Não | SIM | Sim abre detalhes; Não avança |
| Sábado pela manhã | A16 | Sábado pela manhã — em quais datas você consegue participar? | CAIXAS DE SELEÇÃO | 08/08 \\| 15/08 \\| 22/08 \\| 29/08 \\| 05/09 \\| 12/09 | SIM | Exibida somente após resposta Sim |
| Sábado pela manhã | A17 | Sábado pela manhã — em quais horários você consegue iniciar o treino? | CAIXAS DE SELEÇÃO | 7h30 às 9h \\| 7h45 às 9h15 \\| 8h às 9h30 \\| 8h15 às 9h45 \\| 8h30 às 10h | SIM | Exibida somente após resposta Sim |
| Sábado pela manhã | A18 | Sábado pela manhã — você consegue fazer 30 minutos extras? | MÚLTIPLA ESCOLHA | Antes \\| Depois \\| Antes ou depois \\| Não \\| Depende | SIM | Exibida somente após resposta Sim |
| Sábado à tarde | A19 | Você consegue participar de pelo menos uma das datas de sábado à tarde? | MÚLTIPLA ESCOLHA COM NAVEGAÇÃO | Sim \\| Não | SIM | Sim abre detalhes; Não avança |
| Sábado à tarde | A20 | Sábado à tarde — em quais datas você consegue participar? | CAIXAS DE SELEÇÃO | 08/08 \\| 15/08 \\| 22/08 \\| 29/08 \\| 05/09 \\| 12/09 | SIM | Exibida somente após resposta Sim |
| Sábado à tarde | A21 | Sábado à tarde — em quais horários você consegue iniciar o treino? | CAIXAS DE SELEÇÃO | 16h às 17h30 \\| 16h15 às 17h45 \\| 16h30 às 18h \\| 16h45 às 18h15 \\| 17h às 18h30 \\| 17h15 às 18h45 \\| 17h30 às 19h \\| 17h45 às 19h15 \\| 18h às 19h30 \\| 18h15 às 19h45 \\| 18h30 às 20h | SIM | Exibida somente após resposta Sim |
| Sábado à tarde | A22 | Sábado à tarde — você consegue fazer 30 minutos extras? | MÚLTIPLA ESCOLHA | Antes \\| Depois \\| Antes ou depois \\| Não \\| Depende | SIM | Exibida somente após resposta Sim |
| FINAL | A23 | Existe algum problema fixo que pode dificultar sua participação? | CAIXAS DE SELEÇÃO | Trabalho \\| Estudo \\| Transporte \\| Família \\| Recuperação \\| Outro \\| Nenhum \\| Prefiro não informar | NÃO | Restrição geral |
| FINAL | A24 | Existe alguma informação importante sobre seus horários? | PARÁGRAFO |   | NÃO | Campo aberto |
| FINAL | A25 | Confirmação | CAIXA DE CONFIRMAÇÃO | Confirmo que marquei somente possibilidades reais | SIM | Aceite final |

---

## 📋 Worksheet: FORM_B

**Data Dimensions**: 59 rows x 8 columns

| secao | item_id | pergunta | tipo | opcoes_escala | obrigatoria | invertido | dimensao |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MOTIVAÇÃO | B01 | Quero participar desta preparação. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ICM |
| MOTIVAÇÃO | B02 | Buscar o bicampeonato é importante para mim. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ICM |
| MOTIVAÇÃO | B03 | Consigo manter meu esforço mesmo quando estou cansada. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ICM |
| MOTIVAÇÃO | B04 | Consigo continuar treinando quando uma atividade precisa ser repetida. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ICM |
| MOTIVAÇÃO | B05 | Estou disposta a treinar também o que ainda faço com dificuldade. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ICM |
| MOTIVAÇÃO | B06 | Entendo que este período será mais exigente do que o normal. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ICM |
| SUSTENTABILIDADE | B07 | Consigo manter presença regular nos novos treinos. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SUSTENTABILIDADE | B08 | Consigo organizar minha rotina para participar da preparação. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SUSTENTABILIDADE | B09 | Quando não puder treinar, consigo avisar com antecedência. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SUSTENTABILIDADE | B10 | Mesmo em uma semana difícil, tentarei cumprir o que combinei. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SUSTENTABILIDADE | B11 | Existe uma chance real de eu abandonar parte da preparação. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | SIM | ISC |
| SUSTENTABILIDADE | B12 | Estou assumindo mais treinos do que consigo cumprir. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | SIM | ISC |
| SUSTENTABILIDADE | B13 | Consigo me recuperar bem entre os treinos. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SUSTENTABILIDADE | B14 | Tenho dormido o suficiente para suportar uma carga maior. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SUSTENTABILIDADE | B15 | Consigo falar quando estou com dor ou muito cansada. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SUSTENTABILIDADE | B16 | Sinto que preciso esconder dor ou cansaço para continuar treinando. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | SIM | ISC |
| SUSTENTABILIDADE | B17 | O aumento dos treinos pode prejudicar minha saúde ou minha rotina. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | SIM | ISC |
| SUSTENTABILIDADE | B18 | A carga atual de treino está adequada para mim. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISC |
| SATISFAÇÃO | B19 | Gosto de participar dos treinos. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B20 | Os treinos me motivam. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B21 | Os treinos estão ajudando minha evolução. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B22 | Entendo o objetivo das atividades. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B23 | Os exercícios têm relação com situações de jogo. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B24 | Os treinos são variados. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B25 | Os treinos ficam repetitivos além do necessário. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | SIM | IST |
| SATISFAÇÃO | B26 | Algumas atividades são chatas e parecem não ter objetivo. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | SIM | IST |
| SATISFAÇÃO | B27 | O nível de dificuldade está adequado. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B28 | Os treinos são exigentes, mas produtivos. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B29 | Recebo orientações claras para corrigir meus erros. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SATISFAÇÃO | B30 | Saio dos treinos sentindo que aprendi ou evoluí. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | IST |
| SEGURANÇA PARA FALAR | B31 | Posso dizer quando não entendi uma atividade. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISV |
| SEGURANÇA PARA FALAR | B32 | Posso falar quando estou com dor ou sobrecarregada. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISV |
| SEGURANÇA PARA FALAR | B33 | Posso dar uma sugestão sem medo de ser julgada. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISV |
| SEGURANÇA PARA FALAR | B34 | Posso criticar uma atividade sem perder espaço na equipe. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISV |
| SEGURANÇA PARA FALAR | B35 | Sinto que minhas opiniões são ouvidas. | ESCALA 1–5 | 1 Discordo totalmente \\| 2 Discordo \\| 3 Neutro \\| 4 Concordo \\| 5 Concordo totalmente | SIM | NÃO | ISV |
| NOTAS | B36 | Qual é sua motivação atual para esta preparação? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | ICM |
| NOTAS | B37 | Qual é sua satisfação com os treinos atuais? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | IST |
| NOTAS | B38 | Quanto os treinos atuais são motivadores? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | IST |
| NOTAS | B39 | Quanto os treinos atuais são chatos ou repetitivos? | ESCALA 0–10 | 0 a 10 | SIM | SIM | IST_RISCO |
| NOTAS | B40 | Quanto você acredita que consegue suportar o aumento da carga? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | ISC |
| CONFIANÇA | B41 | Qual é sua confiança na sua condição física? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | CONF_FIS |
| CONFIANÇA | B42 | Qual é sua confiança nos fundamentos técnicos? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | CONF_TEC |
| CONFIANÇA | B43 | Qual é sua confiança no sistema ofensivo? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | CONF_OFE |
| CONFIANÇA | B44 | Qual é sua confiança no sistema defensivo? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | CONF_DEF |
| CONFIANÇA | B45 | Qual é sua confiança para decidir sob pressão? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | CONF_PRESSAO |
| CONFIANÇA | B46 | Qual é sua confiança para continuar jogando bem depois de um erro? | ESCALA 0–10 | 0 a 10 | SIM | NÃO | CONF_ERRO |
| COMPORTAMENTO | B47 | Quando está cansada e possui treino, o que normalmente faz? | MÚLTIPLA ESCOLHA | Participo normalmente \\| Participo com esforço reduzido \\| Aviso e peço adaptação \\| Decido perto do horário \\| Falto e aviso depois \\| Evito falar \\| Depende | SIM | NÃO | QUALITATIVO |
| COMPORTAMENTO | B48 | Quando uma atividade mostra uma dificuldade sua, o que normalmente faz? | MÚLTIPLA ESCOLHA | Peço ajuda \\| Continuo tentando \\| Fico frustrada, mas continuo \\| Tento evitar \\| Fico em silêncio \\| Sinto medo de errar \\| Depende | SIM | NÃO | QUALITATIVO |
| COMPORTAMENTO | B49 | Se os treinos ficarem repetitivos durante algumas semanas, o que provavelmente acontecerá? | MÚLTIPLA ESCOLHA | Mantenho o mesmo esforço \\| Mantenho o compromisso com menor motivação \\| Preciso entender melhor o objetivo \\| Posso reduzir a participação \\| Terei dificuldade para continuar \\| Não sei | SIM | NÃO | QUALITATIVO |
| COMPORTAMENTO | B50 | Em uma semana muito difícil, quantos treinos consegue fazer com qualidade? | MÚLTIPLA ESCOLHA | Todos \\| A maioria \\| Apenas os principais \\| Apenas um \\| Precisaria descansar \\| Depende | SIM | NÃO | QUALITATIVO |
| ABERTAS | B51 | Em que parte do jogo você se sente mais confiante hoje? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |
| ABERTAS | B52 | Em que parte do jogo você se sente mais insegura hoje? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |
| ABERTAS | B53 | O que gostaria de treinar mais? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |
| ABERTAS | B54 | Qual exercício ou tipo de treino deveria ser mudado? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |
| ABERTAS | B55 | O que deixa um treino chato para você? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |
| ABERTAS | B56 | O que faz um treino difícil continuar motivador? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |
| ABERTAS | B57 | Qual mudança melhoraria os treinos sem diminuir a exigência? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |
| ABERTAS | B58 | Existe algo que gostaria de falar sobre os treinos? | PARÁGRAFO |   | NÃO | NÃO | QUALITATIVO |

---

## 📋 Worksheet: NORMALIZADO_A

**Data Dimensions**: 2731 rows x 15 columns

*Note: Data rows exceed 1000 rows, showing only the first {1} rows*

| response_id | athlete_id | slot_id | data_treino | resposta | elegivel_nucleo | extra_antes | extra_depois | respondido_em | funcao_principal | ofensiva_principal | ofensiva_secundaria | defensiva_principal | defensiva_secundaria | goleira |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RA-001 | ATH-0013 | SEG-NOITE-1930 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1945 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2000 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2015 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2030 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1930 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1945 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2000 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2015 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2030 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1930 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1945 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2000 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2015 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2030 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1930 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1945 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2000 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2015 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2030 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1930 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1945 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2000 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2015 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2030 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1930 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-1945 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2000 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2015 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEG-NOITE-2030 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1900 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1915 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1930 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1945 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2000 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2015 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2030 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1900 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1915 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1930 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1945 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2000 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2015 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2030 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1900 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1915 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1930 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1945 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2000 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2015 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2030 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1900 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1915 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1930 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1945 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2000 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2015 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2030 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1900 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1915 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1930 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1945 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2000 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2015 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2030 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1900 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1915 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1930 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-1945 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2000 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2015 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | TER-NOITE-2030 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1900 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1915 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1930 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1945 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2000 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2015 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2030 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1900 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1915 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1930 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1945 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2000 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2015 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2030 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1900 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1915 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1930 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1945 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2000 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2015 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2030 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1900 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1915 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1930 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1945 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2000 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2015 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2030 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1900 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1915 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1930 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1945 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2000 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2015 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2030 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1900 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1915 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1930 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-1945 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2000 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2015 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SEX-NOITE-2030 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0730 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0745 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0800 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0815 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0830 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0730 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0745 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0800 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0815 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0830 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0730 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0745 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0800 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0815 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0830 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0730 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0745 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0800 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0815 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0830 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0730 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0745 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0800 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0815 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0830 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0730 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0745 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0800 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0815 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-MANHA-0830 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1600 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1615 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1630 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1645 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1700 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1715 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1730 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1745 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1800 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1815 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1830 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1600 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1615 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1630 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1645 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1700 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1715 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1730 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1745 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1800 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1815 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1830 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1600 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1615 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1630 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1645 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1700 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1715 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1730 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1745 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1800 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1815 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1830 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1600 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1615 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1630 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1645 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1700 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1715 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1730 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1745 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1800 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1815 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1830 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1600 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1615 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1630 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1645 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1700 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1715 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1730 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1745 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1800 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1815 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1830 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1600 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1615 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1630 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1645 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1700 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1715 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1730 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1745 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1800 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1815 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-001 | ATH-0013 | SAB-TARDE-1830 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 0:14:10 | ATAQUE | PIVÔ | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1930 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1945 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2000 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2015 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2030 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1930 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1945 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2000 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2015 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2030 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1930 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1945 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2000 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2015 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2030 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1930 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1945 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2000 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2015 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2030 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1930 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1945 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2000 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2015 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2030 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1930 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-1945 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2000 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2015 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEG-NOITE-2030 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1900 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1915 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1930 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1945 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2000 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2015 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2030 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1900 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1915 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1930 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1945 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2000 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2015 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2030 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1900 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1915 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1930 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1945 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2000 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2015 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2030 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1900 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1915 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1930 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1945 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2000 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2015 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2030 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1900 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1915 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1930 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1945 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2000 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2015 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2030 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1900 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1915 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1930 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-1945 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2000 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2015 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | TER-NOITE-2030 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1900 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1915 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1930 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1945 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2000 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2015 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2030 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1900 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1915 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1930 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1945 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2000 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2015 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2030 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1900 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1915 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1930 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1945 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2000 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2015 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2030 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1900 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1915 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1930 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1945 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2000 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2015 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2030 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1900 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1915 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1930 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1945 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2000 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2015 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2030 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1900 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1915 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1930 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-1945 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2000 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2015 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SEX-NOITE-2030 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0730 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0745 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0800 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0815 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0830 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0730 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0745 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0800 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0815 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0830 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0730 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0745 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0800 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0815 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0830 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0730 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0745 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0800 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0815 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0830 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0730 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0745 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0800 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0815 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0830 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0730 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0745 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0800 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0815 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-MANHA-0830 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1600 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1615 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1630 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1645 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1700 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1715 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1730 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1745 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1800 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1815 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1830 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1600 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1615 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1630 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1645 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1700 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1715 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1730 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1745 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1800 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1815 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1830 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1600 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1615 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1630 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1645 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1700 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1715 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1730 | 2026-08-22 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1745 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1800 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1815 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1830 | 2026-08-22 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1600 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1615 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1630 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1645 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1700 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1715 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1730 | 2026-08-29 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1745 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1800 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1815 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1830 | 2026-08-29 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1600 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1615 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1630 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1645 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1700 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1715 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1730 | 2026-09-05 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1745 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1800 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1815 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1830 | 2026-09-05 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1600 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1615 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1630 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1645 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1700 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1715 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1730 | 2026-09-12 | SIM | 1 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1745 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1800 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1815 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-002 | ATH-0016 | SAB-TARDE-1830 | 2026-09-12 | NAO | 0 | 0 | 0 | 8/5/2026 2:21:16 | ATAQUE | CENTRAL | CENTRAL DIREITA |   |   |   |
| RA-003 | ATH-0006 | SEG-NOITE-1930 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1945 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2000 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2015 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2030 | 2026-08-10 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1930 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1945 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2000 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2015 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2030 | 2026-08-17 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1930 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1945 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2000 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2015 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2030 | 2026-08-24 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1930 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1945 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2000 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2015 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2030 | 2026-08-31 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1930 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1945 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2000 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2015 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2030 | 2026-09-07 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1930 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-1945 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2000 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2015 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEG-NOITE-2030 | 2026-09-14 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1900 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1915 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1930 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1945 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2000 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2015 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2030 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1900 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1915 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1930 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1945 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2000 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2015 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2030 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1900 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1915 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1930 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1945 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2000 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2015 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2030 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1900 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1915 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1930 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1945 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2000 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2015 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2030 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1900 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1915 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1930 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1945 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2000 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2015 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2030 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1900 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1915 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1930 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-1945 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2000 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2015 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | TER-NOITE-2030 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1900 | 2026-08-07 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1915 | 2026-08-07 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1930 | 2026-08-07 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1945 | 2026-08-07 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2000 | 2026-08-07 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2015 | 2026-08-07 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2030 | 2026-08-07 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1900 | 2026-08-14 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1915 | 2026-08-14 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1930 | 2026-08-14 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1945 | 2026-08-14 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2000 | 2026-08-14 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2015 | 2026-08-14 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2030 | 2026-08-14 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1900 | 2026-08-21 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1915 | 2026-08-21 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1930 | 2026-08-21 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1945 | 2026-08-21 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2000 | 2026-08-21 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2015 | 2026-08-21 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2030 | 2026-08-21 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1900 | 2026-08-28 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1915 | 2026-08-28 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1930 | 2026-08-28 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1945 | 2026-08-28 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2000 | 2026-08-28 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2015 | 2026-08-28 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2030 | 2026-08-28 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1900 | 2026-09-04 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1915 | 2026-09-04 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1930 | 2026-09-04 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1945 | 2026-09-04 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2000 | 2026-09-04 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2015 | 2026-09-04 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2030 | 2026-09-04 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1900 | 2026-09-11 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1915 | 2026-09-11 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1930 | 2026-09-11 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-1945 | 2026-09-11 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2000 | 2026-09-11 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2015 | 2026-09-11 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SEX-NOITE-2030 | 2026-09-11 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0730 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0745 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0800 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0815 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0830 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0730 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0745 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0800 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0815 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0830 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0730 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0745 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0800 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0815 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0830 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0730 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0745 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0800 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0815 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0830 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0730 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0745 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0800 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0815 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0830 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0730 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0745 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0800 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0815 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-MANHA-0830 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1600 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1615 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1630 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1645 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1700 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1715 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1730 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1745 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1800 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1815 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1830 | 2026-08-08 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1600 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1615 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1630 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1645 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1700 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1715 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1730 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1745 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1800 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1815 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1830 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1600 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1615 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1630 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1645 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1700 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1715 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1730 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1745 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1800 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1815 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1830 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1600 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1615 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1630 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1645 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1700 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1715 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1730 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1745 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1800 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1815 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1830 | 2026-08-29 | NAO | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1600 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1615 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1630 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1645 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1700 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1715 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1730 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1745 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1800 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1815 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1830 | 2026-09-05 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1600 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1615 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1630 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1645 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1700 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1715 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1730 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1745 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1800 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1815 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-003 | ATH-0006 | SAB-TARDE-1830 | 2026-09-12 | SIM | 0 | 1 | 1 | 8/5/2026 6:05:53 | GOLEIRA |   |   |   |   | GOLEIRA |
| RA-004 | ATH-0003 | SEG-NOITE-1930 | 2026-08-10 | NAO | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1945 | 2026-08-10 | NAO | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2000 | 2026-08-10 | NAO | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2015 | 2026-08-10 | NAO | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2030 | 2026-08-10 | NAO | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1930 | 2026-08-17 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1945 | 2026-08-17 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2000 | 2026-08-17 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2015 | 2026-08-17 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2030 | 2026-08-17 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1930 | 2026-08-24 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1945 | 2026-08-24 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2000 | 2026-08-24 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2015 | 2026-08-24 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2030 | 2026-08-24 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1930 | 2026-08-31 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1945 | 2026-08-31 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2000 | 2026-08-31 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2015 | 2026-08-31 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2030 | 2026-08-31 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1930 | 2026-09-07 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1945 | 2026-09-07 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2000 | 2026-09-07 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2015 | 2026-09-07 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2030 | 2026-09-07 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1930 | 2026-09-14 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-1945 | 2026-09-14 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2000 | 2026-09-14 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2015 | 2026-09-14 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEG-NOITE-2030 | 2026-09-14 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1900 | 2026-08-11 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1915 | 2026-08-11 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1930 | 2026-08-11 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1945 | 2026-08-11 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2000 | 2026-08-11 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2015 | 2026-08-11 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2030 | 2026-08-11 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1900 | 2026-08-18 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1915 | 2026-08-18 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1930 | 2026-08-18 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1945 | 2026-08-18 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2000 | 2026-08-18 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2015 | 2026-08-18 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2030 | 2026-08-18 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1900 | 2026-08-25 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1915 | 2026-08-25 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1930 | 2026-08-25 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1945 | 2026-08-25 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2000 | 2026-08-25 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2015 | 2026-08-25 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2030 | 2026-08-25 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1900 | 2026-09-01 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1915 | 2026-09-01 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1930 | 2026-09-01 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1945 | 2026-09-01 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2000 | 2026-09-01 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2015 | 2026-09-01 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2030 | 2026-09-01 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1900 | 2026-09-08 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1915 | 2026-09-08 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1930 | 2026-09-08 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1945 | 2026-09-08 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2000 | 2026-09-08 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2015 | 2026-09-08 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2030 | 2026-09-08 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1900 | 2026-09-15 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1915 | 2026-09-15 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1930 | 2026-09-15 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-1945 | 2026-09-15 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2000 | 2026-09-15 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2015 | 2026-09-15 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | TER-NOITE-2030 | 2026-09-15 | SIM | 1 | 1 | 0 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1900 | 2026-08-07 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1915 | 2026-08-07 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1930 | 2026-08-07 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1945 | 2026-08-07 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2000 | 2026-08-07 | NAO | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2015 | 2026-08-07 | NAO | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2030 | 2026-08-07 | NAO | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1900 | 2026-08-14 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1915 | 2026-08-14 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1930 | 2026-08-14 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1945 | 2026-08-14 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2000 | 2026-08-14 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2015 | 2026-08-14 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2030 | 2026-08-14 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1900 | 2026-08-21 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1915 | 2026-08-21 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1930 | 2026-08-21 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1945 | 2026-08-21 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2000 | 2026-08-21 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2015 | 2026-08-21 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2030 | 2026-08-21 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1900 | 2026-08-28 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1915 | 2026-08-28 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1930 | 2026-08-28 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1945 | 2026-08-28 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2000 | 2026-08-28 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2015 | 2026-08-28 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2030 | 2026-08-28 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1900 | 2026-09-04 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1915 | 2026-09-04 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1930 | 2026-09-04 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1945 | 2026-09-04 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2000 | 2026-09-04 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2015 | 2026-09-04 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2030 | 2026-09-04 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1900 | 2026-09-11 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1915 | 2026-09-11 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1930 | 2026-09-11 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-1945 | 2026-09-11 | NAO | 0 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2000 | 2026-09-11 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2015 | 2026-09-11 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SEX-NOITE-2030 | 2026-09-11 | SIM | 1 | 0 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0730 | 2026-08-08 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0745 | 2026-08-08 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0800 | 2026-08-08 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0815 | 2026-08-08 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0830 | 2026-08-08 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0730 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0745 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0800 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0815 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0830 | 2026-08-15 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0730 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0745 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0800 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0815 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0830 | 2026-08-22 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0730 | 2026-08-29 | SIM | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0745 | 2026-08-29 | SIM | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0800 | 2026-08-29 | SIM | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0815 | 2026-08-29 | SIM | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0830 | 2026-08-29 | SIM | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0730 | 2026-09-05 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0745 | 2026-09-05 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0800 | 2026-09-05 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0815 | 2026-09-05 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0830 | 2026-09-05 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0730 | 2026-09-12 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0745 | 2026-09-12 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0800 | 2026-09-12 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0815 | 2026-09-12 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-MANHA-0830 | 2026-09-12 | NAO | 0 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1600 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1615 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1630 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1645 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1700 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1715 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1730 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1745 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1800 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1815 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1830 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1600 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1615 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1630 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1645 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1700 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1715 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1730 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1745 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1800 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1815 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1830 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1600 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1615 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1630 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1645 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1700 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1715 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1730 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1745 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1800 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1815 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1830 | 2026-08-22 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1600 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1615 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1630 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1645 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1700 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1715 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1730 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1745 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1800 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1815 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1830 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1600 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1615 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1630 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1645 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1700 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1715 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1730 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1745 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1800 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1815 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1830 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1600 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1615 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1630 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1645 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1700 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1715 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1730 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1745 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1800 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1815 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-004 | ATH-0003 | SAB-TARDE-1830 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 6:55:04 | DEFESA |   |   | DEFENSORA COBERTURA | DEFENSORA BASE |   |
| RA-005 | ATH-0007 | SEG-NOITE-1930 | 2026-08-10 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1945 | 2026-08-10 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2000 | 2026-08-10 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2015 | 2026-08-10 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2030 | 2026-08-10 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1930 | 2026-08-17 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1945 | 2026-08-17 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2000 | 2026-08-17 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2015 | 2026-08-17 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2030 | 2026-08-17 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1930 | 2026-08-24 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1945 | 2026-08-24 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2000 | 2026-08-24 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2015 | 2026-08-24 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2030 | 2026-08-24 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1930 | 2026-08-31 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1945 | 2026-08-31 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2000 | 2026-08-31 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2015 | 2026-08-31 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2030 | 2026-08-31 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1930 | 2026-09-07 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1945 | 2026-09-07 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2000 | 2026-09-07 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2015 | 2026-09-07 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2030 | 2026-09-07 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1930 | 2026-09-14 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-1945 | 2026-09-14 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2000 | 2026-09-14 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2015 | 2026-09-14 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEG-NOITE-2030 | 2026-09-14 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1900 | 2026-08-11 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1915 | 2026-08-11 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1930 | 2026-08-11 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1945 | 2026-08-11 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2000 | 2026-08-11 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2015 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2030 | 2026-08-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1900 | 2026-08-18 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1915 | 2026-08-18 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1930 | 2026-08-18 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1945 | 2026-08-18 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2000 | 2026-08-18 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2015 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2030 | 2026-08-18 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1900 | 2026-08-25 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1915 | 2026-08-25 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1930 | 2026-08-25 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1945 | 2026-08-25 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2000 | 2026-08-25 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2015 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2030 | 2026-08-25 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1900 | 2026-09-01 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1915 | 2026-09-01 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1930 | 2026-09-01 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1945 | 2026-09-01 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2000 | 2026-09-01 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2015 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2030 | 2026-09-01 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1900 | 2026-09-08 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1915 | 2026-09-08 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1930 | 2026-09-08 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1945 | 2026-09-08 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2000 | 2026-09-08 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2015 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2030 | 2026-09-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1900 | 2026-09-15 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1915 | 2026-09-15 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1930 | 2026-09-15 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-1945 | 2026-09-15 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2000 | 2026-09-15 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2015 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | TER-NOITE-2030 | 2026-09-15 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1900 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1915 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1930 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1945 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2000 | 2026-08-07 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2015 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2030 | 2026-08-07 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1900 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1915 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1930 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1945 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2000 | 2026-08-14 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2015 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2030 | 2026-08-14 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1900 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1915 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1930 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1945 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2000 | 2026-08-21 | NAO | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2015 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2030 | 2026-08-21 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1900 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1915 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1930 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1945 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2000 | 2026-08-28 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2015 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2030 | 2026-08-28 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1900 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1915 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1930 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1945 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2000 | 2026-09-04 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2015 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2030 | 2026-09-04 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1900 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1915 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1930 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-1945 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2000 | 2026-09-11 | NAO | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2015 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SEX-NOITE-2030 | 2026-09-11 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0730 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0745 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0800 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0815 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0830 | 2026-08-08 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0730 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0745 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0800 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0815 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0830 | 2026-08-15 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0730 | 2026-08-22 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0745 | 2026-08-22 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0800 | 2026-08-22 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0815 | 2026-08-22 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0830 | 2026-08-22 | NAO | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0730 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0745 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0800 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0815 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0830 | 2026-08-29 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0730 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0745 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0800 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0815 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0830 | 2026-09-05 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0730 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0745 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0800 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0815 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-MANHA-0830 | 2026-09-12 | SIM | 1 | 1 | 1 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1600 | 2026-08-08 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1615 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1630 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1645 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1700 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1715 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1730 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1745 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1800 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1815 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1830 | 2026-08-08 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1600 | 2026-08-15 | SIM | 1 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1615 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1630 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |
| RA-005 | ATH-0007 | SAB-TARDE-1645 | 2026-08-15 | NAO | 0 | 0 | 0 | 8/5/2026 7:18:03 | DEFESA |   |   | DEFENSORA BASE | DEFENSORA COBERTURA |   |

---

## 📋 Worksheet: ANALISE_SLOTS

**Data Dimensions**: 36 rows x 15 columns

| slot_id | dia | periodo | inicio | fim | total_nucleo | goleiras | defesa | ataque | nao | cqv | faixa_cqv | status_amplo | matching_tatico | decisao |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEG-NOITE-1930 | Segunda-feira | NOITE | 19:30 | 21:00 | 5 | 1 | 3 | 2 | 7 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SEG-NOITE-1945 | Segunda-feira | NOITE | 19:45 | 21:15 | 6 | 1 | 3 | 2 | 5 | 61 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SEG-NOITE-2000 | Segunda-feira | NOITE | 20:00 | 21:30 | 5 | 1 | 3 | 2 | 6 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SEG-NOITE-2015 | Segunda-feira | NOITE | 20:15 | 21:45 | 4 | 1 | 3 | 1 | 8 | 54 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SEG-NOITE-2030 | Segunda-feira | NOITE | 20:30 | 22:00 | 4 | 1 | 3 | 1 | 8 | 54 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| TER-NOITE-1900 | Terça-feira | NOITE | 19:00 | 20:30 | 5 | 1 | 3 | 2 | 7 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| TER-NOITE-1915 | Terça-feira | NOITE | 19:15 | 20:45 | 5 | 1 | 3 | 2 | 7 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| TER-NOITE-1930 | Terça-feira | NOITE | 19:30 | 21:00 | 5 | 1 | 3 | 2 | 7 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| TER-NOITE-1945 | Terça-feira | NOITE | 19:45 | 21:15 | 5 | 1 | 3 | 2 | 7 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| TER-NOITE-2000 | Terça-feira | NOITE | 20:00 | 21:30 | 5 | 1 | 3 | 2 | 6 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| TER-NOITE-2015 | Terça-feira | NOITE | 20:15 | 21:45 | 4 | 1 | 2 | 2 | 8 | 54 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| TER-NOITE-2030 | Terça-feira | NOITE | 20:30 | 22:00 | 4 | 1 | 2 | 2 | 8 | 54 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SEX-NOITE-1900 | Sexta-feira | NOITE | 19:00 | 20:30 | 3 | 1 | 1 | 2 | 8 | 41 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SEX-NOITE-1915 | Sexta-feira | NOITE | 19:15 | 20:45 | 3 | 1 | 1 | 2 | 8 | 41 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SEX-NOITE-1930 | Sexta-feira | NOITE | 19:30 | 21:00 | 4 | 1 | 1 | 2 | 7 | 44 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SEX-NOITE-1945 | Sexta-feira | NOITE | 19:45 | 21:15 | 3 | 1 | 1 | 2 | 8 | 41 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SEX-NOITE-2000 | Sexta-feira | NOITE | 20:00 | 21:30 | 5 | 1 | 3 | 2 | 6 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SEX-NOITE-2015 | Sexta-feira | NOITE | 20:15 | 21:45 | 3 | 1 | 2 | 1 | 8 | 51 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SEX-NOITE-2030 | Sexta-feira | NOITE | 20:30 | 22:00 | 3 | 1 | 2 | 1 | 7 | 51 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SAB-MANHA-0730 | Sábado | MANHA | 07:30 | 09:00 | 7 | 1 | 2 | 4 | 1 | 70 | Atenção | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | TESTAR 2 SEMANAS |
| SAB-MANHA-0745 | Sábado | MANHA | 07:45 | 09:15 | 6 | 1 | 2 | 4 | 2 | 66 | Atenção | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | TESTAR 2 SEMANAS |
| SAB-MANHA-0800 | Sábado | MANHA | 08:00 | 09:30 | 6 | 1 | 2 | 4 | 2 | 66 | Atenção | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | TESTAR 2 SEMANAS |
| SAB-MANHA-0815 | Sábado | MANHA | 08:15 | 09:45 | 5 | 1 | 2 | 3 | 4 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SAB-MANHA-0830 | Sábado | MANHA | 08:30 | 10:00 | 5 | 1 | 2 | 3 | 4 | 58 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SAB-TARDE-1600 | Sábado | TARDE | 16:00 | 17:30 | 3 | 1 | 2 | 1 | 5 | 51 | Crítico | OPERACIONAL | MATCHING BÁSICO VIÁVEL — ATLETAS DISTINTAS | NÃO PRIORIZAR |
| SAB-TARDE-1615 | Sábado | TARDE | 16:15 | 17:45 | 2 | 1 | 1 | 1 | 6 | 37 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1630 | Sábado | TARDE | 16:30 | 18:00 | 2 | 1 | 1 | 1 | 6 | 37 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1645 | Sábado | TARDE | 16:45 | 18:15 | 2 | 1 | 1 | 1 | 7 | 37 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1700 | Sábado | TARDE | 17:00 | 18:30 | 2 | 1 | 1 | 1 | 7 | 37 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1715 | Sábado | TARDE | 17:15 | 18:45 | 2 | 1 | 1 | 1 | 7 | 37 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1730 | Sábado | TARDE | 17:30 | 19:00 | 2 | 1 | 1 | 1 | 8 | 37 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1745 | Sábado | TARDE | 17:45 | 19:15 | 1 | 1 | 1 | 1 | 8 | 34 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1800 | Sábado | TARDE | 18:00 | 19:30 | 1 | 1 | 1 | 1 | 8 | 34 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1815 | Sábado | TARDE | 18:15 | 19:45 | 1 | 1 | 1 | 1 | 8 | 34 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |
| SAB-TARDE-1830 | Sábado | TARDE | 18:30 | 20:00 | 1 | 1 | 1 | 1 | 8 | 34 | Crítico | DEFESA CURTA | INVIÁVEL — DEFESA CURTA | NÃO PRIORIZAR |

---

## 📋 Worksheet: RESPOSTAS_B_NORM

**Data Dimensions**: 697 rows x 7 columns

| response_id | item_id | valor_numerico | valor_corrigido | dimensao | texto | respondido_em |
| --- | --- | --- | --- | --- | --- | --- |
| RB-001 | B01 | 1 | 1 | ICM |   | 8/4/2026 23:36:16 |
| RB-001 | B02 | 2 | 2 | ICM |   | 8/4/2026 23:36:16 |
| RB-001 | B03 | 3 | 3 | ICM |   | 8/4/2026 23:36:16 |
| RB-001 | B04 | 3 | 3 | ICM |   | 8/4/2026 23:36:16 |
| RB-001 | B05 | 3 | 3 | ICM |   | 8/4/2026 23:36:16 |
| RB-001 | B06 | 2 | 2 | ICM |   | 8/4/2026 23:36:16 |
| RB-001 | B07 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B08 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B09 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B10 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B11 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B12 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B13 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B14 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B15 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B16 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B17 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B18 | 3 | 3 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B19 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B20 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B21 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B22 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B23 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B24 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B25 | 2 | 4 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B26 | 2 | 4 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B27 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B28 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B29 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B30 | 3 | 3 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B31 | 4 | 4 | ISV |   | 8/4/2026 23:36:16 |
| RB-001 | B32 | 4 | 4 | ISV |   | 8/4/2026 23:36:16 |
| RB-001 | B33 | 3 | 3 | ISV |   | 8/4/2026 23:36:16 |
| RB-001 | B34 | 3 | 3 | ISV |   | 8/4/2026 23:36:16 |
| RB-001 | B35 | 2 | 2 | ISV |   | 8/4/2026 23:36:16 |
| RB-001 | B36 | 8 | 8 | ICM |   | 8/4/2026 23:36:16 |
| RB-001 | B37 | 2 | 2 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B38 | 1 | 1 | IST |   | 8/4/2026 23:36:16 |
| RB-001 | B39 | 1 | 9 | IST_RISCO |   | 8/4/2026 23:36:16 |
| RB-001 | B40 | 1 | 1 | ISC |   | 8/4/2026 23:36:16 |
| RB-001 | B41 | 2 | 2 | CONF_FIS |   | 8/4/2026 23:36:16 |
| RB-001 | B42 | 2 | 2 | CONF_TEC |   | 8/4/2026 23:36:16 |
| RB-001 | B43 | 2 | 2 | CONF_OFE |   | 8/4/2026 23:36:16 |
| RB-001 | B44 | 2 | 2 | CONF_DEF |   | 8/4/2026 23:36:16 |
| RB-001 | B45 | 3 | 3 | CONF_PRESSAO |   | 8/4/2026 23:36:16 |
| RB-001 | B46 | 2 | 2 | CONF_ERRO |   | 8/4/2026 23:36:16 |
| RB-001 | B47 |   |   | QUALITATIVO | Participo com esforço reduzido | 8/4/2026 23:36:16 |
| RB-001 | B48 |   |   | QUALITATIVO | Peço ajuda | 8/4/2026 23:36:16 |
| RB-001 | B49 |   |   | QUALITATIVO | Terei dificuldade para continuar | 8/4/2026 23:36:16 |
| RB-001 | B50 |   |   | QUALITATIVO | Precisaria descansar | 8/4/2026 23:36:16 |
| RB-001 | B51 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-001 | B52 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-001 | B53 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-001 | B54 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-001 | B55 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-001 | B56 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-001 | B57 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-001 | B58 |   |   | QUALITATIVO |   | 8/4/2026 23:36:16 |
| RB-002 | B01 | 1 | 1 | ICM |   | 8/5/2026 2:33:52 |
| RB-002 | B02 | 5 | 5 | ICM |   | 8/5/2026 2:33:52 |
| RB-002 | B03 | 3 | 3 | ICM |   | 8/5/2026 2:33:52 |
| RB-002 | B04 | 4 | 4 | ICM |   | 8/5/2026 2:33:52 |
| RB-002 | B05 | 3 | 3 | ICM |   | 8/5/2026 2:33:52 |
| RB-002 | B06 | 5 | 5 | ICM |   | 8/5/2026 2:33:52 |
| RB-002 | B07 | 3 | 3 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B08 | 3 | 3 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B09 | 3 | 3 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B10 | 4 | 4 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B11 | 3 | 3 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B12 | 2 | 4 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B13 | 4 | 4 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B14 | 2 | 2 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B15 | 4 | 4 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B16 | 4 | 2 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B17 | 2 | 4 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B18 | 4 | 4 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B19 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B20 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B21 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B22 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B23 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B24 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B25 | 2 | 4 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B26 | 2 | 4 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B27 | 4 | 4 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B28 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B29 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B30 | 5 | 5 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B31 | 5 | 5 | ISV |   | 8/5/2026 2:33:52 |
| RB-002 | B32 | 5 | 5 | ISV |   | 8/5/2026 2:33:52 |
| RB-002 | B33 | 5 | 5 | ISV |   | 8/5/2026 2:33:52 |
| RB-002 | B34 | 5 | 5 | ISV |   | 8/5/2026 2:33:52 |
| RB-002 | B35 | 5 | 5 | ISV |   | 8/5/2026 2:33:52 |
| RB-002 | B36 | 5 | 5 | ICM |   | 8/5/2026 2:33:52 |
| RB-002 | B37 | 10 | 10 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B38 | 10 | 10 | IST |   | 8/5/2026 2:33:52 |
| RB-002 | B39 | 9 | 1 | IST_RISCO |   | 8/5/2026 2:33:52 |
| RB-002 | B40 | 6 | 6 | ISC |   | 8/5/2026 2:33:52 |
| RB-002 | B41 | 3 | 3 | CONF_FIS |   | 8/5/2026 2:33:52 |
| RB-002 | B42 | 5 | 5 | CONF_TEC |   | 8/5/2026 2:33:52 |
| RB-002 | B43 | 8 | 8 | CONF_OFE |   | 8/5/2026 2:33:52 |
| RB-002 | B44 | 8 | 8 | CONF_DEF |   | 8/5/2026 2:33:52 |
| RB-002 | B45 | 3 | 3 | CONF_PRESSAO |   | 8/5/2026 2:33:52 |
| RB-002 | B46 | 5 | 5 | CONF_ERRO |   | 8/5/2026 2:33:52 |
| RB-002 | B47 |   |   | QUALITATIVO | Participo com esforço reduzido | 8/5/2026 2:33:52 |
| RB-002 | B48 |   |   | QUALITATIVO | Tento evitar | 8/5/2026 2:33:52 |
| RB-002 | B49 |   |   | QUALITATIVO | Mantenho o compromisso com menor motivação | 8/5/2026 2:33:52 |
| RB-002 | B50 |   |   | QUALITATIVO | Depende | 8/5/2026 2:33:52 |
| RB-002 | B51 |   |   | QUALITATIVO | Ataque | 8/5/2026 2:33:52 |
| RB-002 | B52 |   |   | QUALITATIVO | Shootout | 8/5/2026 2:33:52 |
| RB-002 | B53 |   |   | QUALITATIVO | Situações específicas de ataque | 8/5/2026 2:33:52 |
| RB-002 | B54 |   |   | QUALITATIVO | Acho q nenhum | 8/5/2026 2:33:52 |
| RB-002 | B55 |   |   | QUALITATIVO | Shootout demorado | 8/5/2026 2:33:52 |
| RB-002 | B56 |   |   | QUALITATIVO | sentir que está evoluindo (competência), que escolheu estar ali (autonomia) e que faz parte de algo ou tem apoio (conexão com um treinador, parceiro ou grupo). | 8/5/2026 2:33:52 |
| RB-002 | B57 |   |   | QUALITATIVO | Definir uma meta clara para cada treino /     Mostrar evolução / Oferecer níveis de desafio /     Dar feedback positivo específico | 8/5/2026 2:33:52 |
| RB-002 | B58 |   |   | QUALITATIVO | Não 🧡 | 8/5/2026 2:33:52 |
| RB-003 | B01 | 5 | 5 | ICM |   | 8/5/2026 7:16:06 |
| RB-003 | B02 | 5 | 5 | ICM |   | 8/5/2026 7:16:06 |
| RB-003 | B03 | 5 | 5 | ICM |   | 8/5/2026 7:16:06 |
| RB-003 | B04 | 5 | 5 | ICM |   | 8/5/2026 7:16:06 |
| RB-003 | B05 | 5 | 5 | ICM |   | 8/5/2026 7:16:06 |
| RB-003 | B06 | 5 | 5 | ICM |   | 8/5/2026 7:16:06 |
| RB-003 | B07 | 4 | 4 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B08 | 5 | 5 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B09 | 5 | 5 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B10 | 5 | 5 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B11 | 1 | 5 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B12 | 1 | 5 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B13 | 5 | 5 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B14 | 3 | 3 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B15 | 3 | 3 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B16 | 1 | 5 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B17 | 4 | 2 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B18 | 2 | 2 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B19 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B20 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B21 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B22 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B23 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B24 | 4 | 4 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B25 | 4 | 2 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B26 | 2 | 4 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B27 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B28 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B29 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B30 | 5 | 5 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B31 | 5 | 5 | ISV |   | 8/5/2026 7:16:06 |
| RB-003 | B32 | 5 | 5 | ISV |   | 8/5/2026 7:16:06 |
| RB-003 | B33 | 4 | 4 | ISV |   | 8/5/2026 7:16:06 |
| RB-003 | B34 | 5 | 5 | ISV |   | 8/5/2026 7:16:06 |
| RB-003 | B35 | 4 | 4 | ISV |   | 8/5/2026 7:16:06 |
| RB-003 | B36 | 10 | 10 | ICM |   | 8/5/2026 7:16:06 |
| RB-003 | B37 | 8 | 8 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B38 | 8 | 8 | IST |   | 8/5/2026 7:16:06 |
| RB-003 | B39 | 3 | 7 | IST_RISCO |   | 8/5/2026 7:16:06 |
| RB-003 | B40 | 10 | 10 | ISC |   | 8/5/2026 7:16:06 |
| RB-003 | B41 | 7 | 7 | CONF_FIS |   | 8/5/2026 7:16:06 |
| RB-003 | B42 | 9 | 9 | CONF_TEC |   | 8/5/2026 7:16:06 |
| RB-003 | B43 | 10 | 10 | CONF_OFE |   | 8/5/2026 7:16:06 |
| RB-003 | B44 | 10 | 10 | CONF_DEF |   | 8/5/2026 7:16:06 |
| RB-003 | B45 | 8 | 8 | CONF_PRESSAO |   | 8/5/2026 7:16:06 |
| RB-003 | B46 | 10 | 10 | CONF_ERRO |   | 8/5/2026 7:16:06 |
| RB-003 | B47 |   |   | QUALITATIVO | Participo normalmente | 8/5/2026 7:16:06 |
| RB-003 | B48 |   |   | QUALITATIVO | Continuo tentando | 8/5/2026 7:16:06 |
| RB-003 | B49 |   |   | QUALITATIVO | Mantenho o mesmo esforço | 8/5/2026 7:16:06 |
| RB-003 | B50 |   |   | QUALITATIVO | A maioria | 8/5/2026 7:16:06 |
| RB-003 | B51 |   |   | QUALITATIVO | Marcação por cobertura | 8/5/2026 7:16:06 |
| RB-003 | B52 |   |   | QUALITATIVO | Marcar coringa que chega na velocidade | 8/5/2026 7:16:06 |
| RB-003 | B53 |   |   | QUALITATIVO | Marcar coringa que chega na velocidade | 8/5/2026 7:16:06 |
| RB-003 | B54 |   |   | QUALITATIVO | Não vejo nada a ser mudado | 8/5/2026 7:16:06 |
| RB-003 | B55 |   |   | QUALITATIVO | Parar toda hora | 8/5/2026 7:16:06 |
| RB-003 | B56 |   |   | QUALITATIVO | As atletas motivarem umas às outras falando fora de quadra. | 8/5/2026 7:16:06 |
| RB-003 | B57 |   |   | QUALITATIVO | - Mentalidade foi a chave para sermos campeãs, tentar fazer igual ano passado, priorizando em cada treino mexer com a metalidade das atletas<br> - Beber água com mais frequência | 8/5/2026 7:16:06 |
| RB-003 | B58 |   |   | QUALITATIVO | Chegar antes do horário marcado, nem que seja 10 minutos. | 8/5/2026 7:16:06 |
| RB-004 | B01 | 5 | 5 | ICM |   | 8/5/2026 9:25:28 |
| RB-004 | B02 | 5 | 5 | ICM |   | 8/5/2026 9:25:28 |
| RB-004 | B03 | 5 | 5 | ICM |   | 8/5/2026 9:25:28 |
| RB-004 | B04 | 5 | 5 | ICM |   | 8/5/2026 9:25:28 |
| RB-004 | B05 | 5 | 5 | ICM |   | 8/5/2026 9:25:28 |
| RB-004 | B06 | 5 | 5 | ICM |   | 8/5/2026 9:25:28 |
| RB-004 | B07 | 5 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B08 | 5 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B09 | 5 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B10 | 5 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B11 | 1 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B12 | 1 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B13 | 5 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B14 | 4 | 4 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B15 | 4 | 4 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B16 | 1 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B17 | 1 | 5 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B18 | 1 | 1 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B19 | 5 | 5 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B20 | 5 | 5 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B21 | 5 | 5 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B22 | 5 | 5 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B23 | 5 | 5 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B24 | 4 | 4 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B25 | 2 | 4 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B26 | 1 | 5 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B27 | 4 | 4 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B28 | 4 | 4 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B29 | 4 | 4 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B30 | 4 | 4 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B31 | 4 | 4 | ISV |   | 8/5/2026 9:25:28 |
| RB-004 | B32 | 5 | 5 | ISV |   | 8/5/2026 9:25:28 |
| RB-004 | B33 | 4 | 4 | ISV |   | 8/5/2026 9:25:28 |
| RB-004 | B34 | 5 | 5 | ISV |   | 8/5/2026 9:25:28 |
| RB-004 | B35 | 4 | 4 | ISV |   | 8/5/2026 9:25:28 |
| RB-004 | B36 | 10 | 10 | ICM |   | 8/5/2026 9:25:28 |
| RB-004 | B37 | 8 | 8 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B38 | 8 | 8 | IST |   | 8/5/2026 9:25:28 |
| RB-004 | B39 | 3 | 7 | IST_RISCO |   | 8/5/2026 9:25:28 |
| RB-004 | B40 | 10 | 10 | ISC |   | 8/5/2026 9:25:28 |
| RB-004 | B41 | 8 | 8 | CONF_FIS |   | 8/5/2026 9:25:28 |
| RB-004 | B42 | 9 | 9 | CONF_TEC |   | 8/5/2026 9:25:28 |
| RB-004 | B43 | 9 | 9 | CONF_OFE |   | 8/5/2026 9:25:28 |
| RB-004 | B44 | 9 | 9 | CONF_DEF |   | 8/5/2026 9:25:28 |
| RB-004 | B45 | 9 | 9 | CONF_PRESSAO |   | 8/5/2026 9:25:28 |
| RB-004 | B46 | 9 | 9 | CONF_ERRO |   | 8/5/2026 9:25:28 |
| RB-004 | B47 |   |   | QUALITATIVO | Participo normalmente | 8/5/2026 9:25:28 |
| RB-004 | B48 |   |   | QUALITATIVO | Continuo tentando | 8/5/2026 9:25:28 |
| RB-004 | B49 |   |   | QUALITATIVO | Mantenho o mesmo esforço | 8/5/2026 9:25:28 |
| RB-004 | B50 |   |   | QUALITATIVO | A maioria | 8/5/2026 9:25:28 |
| RB-004 | B51 |   |   | QUALITATIVO | Passe e arremesso de 1. | 8/5/2026 9:25:28 |
| RB-004 | B52 |   |   | QUALITATIVO | Giro | 8/5/2026 9:25:28 |
| RB-004 | B53 |   |   | QUALITATIVO | Especialista | 8/5/2026 9:25:28 |
| RB-004 | B54 |   |   | QUALITATIVO | 1 contra o goleiro. Manter a mudança de fazer muitas repetições e depois realidade de jogo. | 8/5/2026 9:25:28 |
| RB-004 | B55 |   |   | QUALITATIVO | Falta de concentração | 8/5/2026 9:25:28 |
| RB-004 | B56 |   |   | QUALITATIVO | Perceber o avanço | 8/5/2026 9:25:28 |
| RB-004 | B57 |   |   | QUALITATIVO | Concentração e foco coletivo | 8/5/2026 9:25:28 |
| RB-004 | B58 |   |   | QUALITATIVO | Fazer atividades coletivas com disputa no aquecimento me estimulam e ajudam para a concentração no treino e acho que faz o mesmo com outras mulheres. Deveríamos fazer mais vezes. | 8/5/2026 9:25:28 |
| RB-005 | B01 | 5 | 5 | ICM |   | 8/5/2026 13:23:01 |
| RB-005 | B02 | 5 | 5 | ICM |   | 8/5/2026 13:23:01 |
| RB-005 | B03 | 5 | 5 | ICM |   | 8/5/2026 13:23:01 |
| RB-005 | B04 | 5 | 5 | ICM |   | 8/5/2026 13:23:01 |
| RB-005 | B05 | 5 | 5 | ICM |   | 8/5/2026 13:23:01 |
| RB-005 | B06 | 5 | 5 | ICM |   | 8/5/2026 13:23:01 |
| RB-005 | B07 | 5 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B08 | 5 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B09 | 5 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B10 | 5 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B11 | 1 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B12 | 1 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B13 | 5 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B14 | 3 | 3 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B15 | 3 | 3 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B16 | 1 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B17 | 1 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B18 | 5 | 5 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B19 | 5 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B20 | 5 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B21 | 5 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B22 | 4 | 4 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B23 | 5 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B24 | 5 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B25 | 1 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B26 | 1 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B27 | 3 | 3 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B28 | 5 | 5 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B29 | 4 | 4 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B30 | 3 | 3 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B31 | 3 | 3 | ISV |   | 8/5/2026 13:23:01 |
| RB-005 | B32 | 4 | 4 | ISV |   | 8/5/2026 13:23:01 |
| RB-005 | B33 | 2 | 2 | ISV |   | 8/5/2026 13:23:01 |
| RB-005 | B34 | 2 | 2 | ISV |   | 8/5/2026 13:23:01 |
| RB-005 | B35 | 3 | 3 | ISV |   | 8/5/2026 13:23:01 |
| RB-005 | B36 | 8 | 8 | ICM |   | 8/5/2026 13:23:01 |
| RB-005 | B37 | 9 | 9 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B38 | 8 | 8 | IST |   | 8/5/2026 13:23:01 |
| RB-005 | B39 | 2 | 8 | IST_RISCO |   | 8/5/2026 13:23:01 |
| RB-005 | B40 | 9 | 9 | ISC |   | 8/5/2026 13:23:01 |
| RB-005 | B41 | 9 | 9 | CONF_FIS |   | 8/5/2026 13:23:01 |
| RB-005 | B42 | 7 | 7 | CONF_TEC |   | 8/5/2026 13:23:01 |
| RB-005 | B43 | 8 | 8 | CONF_OFE |   | 8/5/2026 13:23:01 |
| RB-005 | B44 | 8 | 8 | CONF_DEF |   | 8/5/2026 13:23:01 |
| RB-005 | B45 | 6 | 6 | CONF_PRESSAO |   | 8/5/2026 13:23:01 |
| RB-005 | B46 | 6 | 6 | CONF_ERRO |   | 8/5/2026 13:23:01 |
| RB-005 | B47 |   |   | QUALITATIVO | Participo normalmente | 8/5/2026 13:23:01 |
| RB-005 | B48 |   |   | QUALITATIVO | Continuo tentando | 8/5/2026 13:23:01 |
| RB-005 | B49 |   |   | QUALITATIVO | Mantenho o mesmo esforço | 8/5/2026 13:23:01 |
| RB-005 | B50 |   |   | QUALITATIVO | A maioria | 8/5/2026 13:23:01 |
| RB-005 | B51 |   |   | QUALITATIVO | Quando sinto que o time da engajado. | 8/5/2026 13:23:01 |
| RB-005 | B52 |   |   | QUALITATIVO | Quando acontece uma seguecia de falhas minha. | 8/5/2026 13:23:01 |
| RB-005 | B53 |   |   | QUALITATIVO | Confiança | 8/5/2026 13:23:01 |
| RB-005 | B54 |   |   | QUALITATIVO | Nenhum | 8/5/2026 13:23:01 |
| RB-005 | B55 |   |   | QUALITATIVO | Quando percebo que algumas pessoas vontade de treinar. | 8/5/2026 13:23:01 |
| RB-005 | B56 |   |   | QUALITATIVO | O engajamento do time | 8/5/2026 13:23:01 |
| RB-005 | B57 |   |   | QUALITATIVO | Não mudaria nada | 8/5/2026 13:23:01 |
| RB-005 | B58 |   |   | QUALITATIVO | Acho que você tenta abranger o máximo possível de possibilidades. | 8/5/2026 13:23:01 |
| RB-006 | B01 | 5 | 5 | ICM |   | 8/5/2026 16:13:03 |
| RB-006 | B02 | 5 | 5 | ICM |   | 8/5/2026 16:13:03 |
| RB-006 | B03 | 5 | 5 | ICM |   | 8/5/2026 16:13:03 |
| RB-006 | B04 | 5 | 5 | ICM |   | 8/5/2026 16:13:03 |
| RB-006 | B05 | 5 | 5 | ICM |   | 8/5/2026 16:13:03 |
| RB-006 | B06 | 5 | 5 | ICM |   | 8/5/2026 16:13:03 |
| RB-006 | B07 | 5 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B08 | 5 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B09 | 5 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B10 | 5 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B11 | 5 | 1 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B12 | 1 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B13 | 4 | 4 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B14 | 5 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B15 | 5 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B16 | 1 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B17 | 1 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B18 | 5 | 5 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B19 | 5 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B20 | 5 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B21 | 5 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B22 | 4 | 4 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B23 | 5 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B24 | 4 | 4 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B25 | 2 | 4 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B26 | 1 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B27 | 5 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B28 | 5 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B29 | 5 | 5 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B30 | 4 | 4 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B31 | 5 | 5 | ISV |   | 8/5/2026 16:13:03 |
| RB-006 | B32 | 5 | 5 | ISV |   | 8/5/2026 16:13:03 |
| RB-006 | B33 | 3 | 3 | ISV |   | 8/5/2026 16:13:03 |
| RB-006 | B34 | 5 | 5 | ISV |   | 8/5/2026 16:13:03 |
| RB-006 | B35 | 3 | 3 | ISV |   | 8/5/2026 16:13:03 |
| RB-006 | B36 | 10 | 10 | ICM |   | 8/5/2026 16:13:03 |
| RB-006 | B37 | 10 | 10 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B38 | 8 | 8 | IST |   | 8/5/2026 16:13:03 |
| RB-006 | B39 | 0 | 10 | IST_RISCO |   | 8/5/2026 16:13:03 |
| RB-006 | B40 | 10 | 10 | ISC |   | 8/5/2026 16:13:03 |
| RB-006 | B41 | 10 | 10 | CONF_FIS |   | 8/5/2026 16:13:03 |
| RB-006 | B42 | 8 | 8 | CONF_TEC |   | 8/5/2026 16:13:03 |
| RB-006 | B43 | 8 | 8 | CONF_OFE |   | 8/5/2026 16:13:03 |
| RB-006 | B44 | 7 | 7 | CONF_DEF |   | 8/5/2026 16:13:03 |
| RB-006 | B45 | 9 | 9 | CONF_PRESSAO |   | 8/5/2026 16:13:03 |
| RB-006 | B46 | 10 | 10 | CONF_ERRO |   | 8/5/2026 16:13:03 |
| RB-006 | B47 |   |   | QUALITATIVO | Participo normalmente | 8/5/2026 16:13:03 |
| RB-006 | B48 |   |   | QUALITATIVO | Peço ajuda | 8/5/2026 16:13:03 |
| RB-006 | B49 |   |   | QUALITATIVO | Mantenho o compromisso com menor motivação | 8/5/2026 16:13:03 |
| RB-006 | B50 |   |   | QUALITATIVO | A maioria | 8/5/2026 16:13:03 |
| RB-006 | B51 |   |   | QUALITATIVO | Contra ataque e transição | 8/5/2026 16:13:03 |
| RB-006 | B52 |   |   | QUALITATIVO | Finalização, shoot out | 8/5/2026 16:13:03 |
| RB-006 | B53 |   |   | QUALITATIVO | Específico e finalização | 8/5/2026 16:13:03 |
| RB-006 | B54 |   |   | QUALITATIVO | Nenhum | 8/5/2026 16:13:03 |
| RB-006 | B55 |   |   | QUALITATIVO | Parar muitas vezes pra explicar ou corrigir | 8/5/2026 16:13:03 |
| RB-006 | B56 |   |   | QUALITATIVO | A motivação é interna. A atleta que tem que lembrar do objetivo final que é ser campeã brasileira e não desistir ou fazer de qualquer jeito o treino só porque está difícil. | 8/5/2026 16:13:03 |
| RB-006 | B57 |   |   | QUALITATIVO | Explicar o objetivo do exercício antes da gente fazer ele errado kkkk | 8/5/2026 16:13:03 |
| RB-006 | B58 |   |   | QUALITATIVO |   | 8/5/2026 16:13:03 |
| RB-007 | B01 | 4 | 4 | ICM |   | 8/5/2026 17:22:21 |
| RB-007 | B02 | 5 | 5 | ICM |   | 8/5/2026 17:22:21 |
| RB-007 | B03 | 4 | 4 | ICM |   | 8/5/2026 17:22:21 |
| RB-007 | B04 | 5 | 5 | ICM |   | 8/5/2026 17:22:21 |
| RB-007 | B05 | 5 | 5 | ICM |   | 8/5/2026 17:22:21 |
| RB-007 | B06 | 5 | 5 | ICM |   | 8/5/2026 17:22:21 |
| RB-007 | B07 | 4 | 4 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B08 | 5 | 5 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B09 | 5 | 5 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B10 | 5 | 5 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B11 | 2 | 4 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B12 | 4 | 2 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B13 | 3 | 3 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B14 | 4 | 4 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B15 | 5 | 5 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B16 | 3 | 3 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B17 | 3 | 3 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B18 | 4 | 4 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B19 | 5 | 5 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B20 | 5 | 5 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B21 | 5 | 5 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B22 | 4 | 4 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B23 | 5 | 5 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B24 | 4 | 4 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B25 | 2 | 4 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B26 | 1 | 5 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B27 | 4 | 4 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B28 | 5 | 5 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B29 | 5 | 5 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B30 | 4 | 4 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B31 | 5 | 5 | ISV |   | 8/5/2026 17:22:21 |
| RB-007 | B32 | 4 | 4 | ISV |   | 8/5/2026 17:22:21 |
| RB-007 | B33 | 3 | 3 | ISV |   | 8/5/2026 17:22:21 |
| RB-007 | B34 | 2 | 2 | ISV |   | 8/5/2026 17:22:21 |
| RB-007 | B35 | 2 | 2 | ISV |   | 8/5/2026 17:22:21 |
| RB-007 | B36 | 7 | 7 | ICM |   | 8/5/2026 17:22:21 |
| RB-007 | B37 | 8 | 8 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B38 | 9 | 9 | IST |   | 8/5/2026 17:22:21 |
| RB-007 | B39 | 2 | 8 | IST_RISCO |   | 8/5/2026 17:22:21 |
| RB-007 | B40 | 8 | 8 | ISC |   | 8/5/2026 17:22:21 |
| RB-007 | B41 | 6 | 6 | CONF_FIS |   | 8/5/2026 17:22:21 |
| RB-007 | B42 | 8 | 8 | CONF_TEC |   | 8/5/2026 17:22:21 |
| RB-007 | B43 | 8 | 8 | CONF_OFE |   | 8/5/2026 17:22:21 |
| RB-007 | B44 | 10 | 10 | CONF_DEF |   | 8/5/2026 17:22:21 |
| RB-007 | B45 | 8 | 8 | CONF_PRESSAO |   | 8/5/2026 17:22:21 |
| RB-007 | B46 | 8 | 8 | CONF_ERRO |   | 8/5/2026 17:22:21 |
| RB-007 | B47 |   |   | QUALITATIVO | Aviso e peço adaptação | 8/5/2026 17:22:21 |
| RB-007 | B48 |   |   | QUALITATIVO | Continuo tentando | 8/5/2026 17:22:21 |
| RB-007 | B49 |   |   | QUALITATIVO | Mantenho o mesmo esforço | 8/5/2026 17:22:21 |
| RB-007 | B50 |   |   | QUALITATIVO | Depende | 8/5/2026 17:22:21 |
| RB-007 | B51 |   |   | QUALITATIVO | Finalização | 8/5/2026 17:22:21 |
| RB-007 | B52 |   |   | QUALITATIVO | Na tomada de decisão | 8/5/2026 17:22:21 |
| RB-007 | B53 |   |   | QUALITATIVO | Movimentação como especialista ou playmaker | 8/5/2026 17:22:21 |
| RB-007 | B54 |   |   | QUALITATIVO |   | 8/5/2026 17:22:21 |
| RB-007 | B55 |   |   | QUALITATIVO | Quanto o time erra muito a mesma coisa | 8/5/2026 17:22:21 |
| RB-007 | B56 |   |   | QUALITATIVO | Entender que  aquele treino é necessário | 8/5/2026 17:22:21 |
| RB-007 | B57 |   |   | QUALITATIVO |   | 8/5/2026 17:22:21 |
| RB-007 | B58 |   |   | QUALITATIVO | Acho que ainda tem muita conversa paralela na hora de realizar os exercícios e isso atrapalha bastante | 8/5/2026 17:22:21 |
| RB-008 | B01 | 4 | 4 | ICM |   | 8/5/2026 17:44:58 |
| RB-008 | B02 | 5 | 5 | ICM |   | 8/5/2026 17:44:58 |
| RB-008 | B03 | 4 | 4 | ICM |   | 8/5/2026 17:44:58 |
| RB-008 | B04 | 5 | 5 | ICM |   | 8/5/2026 17:44:58 |
| RB-008 | B05 | 5 | 5 | ICM |   | 8/5/2026 17:44:58 |
| RB-008 | B06 | 5 | 5 | ICM |   | 8/5/2026 17:44:58 |
| RB-008 | B07 | 4 | 4 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B08 | 4 | 4 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B09 | 5 | 5 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B10 | 5 | 5 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B11 | 2 | 4 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B12 | 1 | 5 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B13 | 5 | 5 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B14 | 4 | 4 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B15 | 5 | 5 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B16 | 1 | 5 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B17 | 3 | 3 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B18 | 3 | 3 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B19 | 5 | 5 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B20 | 4 | 4 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B21 | 4 | 4 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B22 | 4 | 4 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B23 | 5 | 5 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B24 | 5 | 5 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B25 | 1 | 5 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B26 | 3 | 3 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B27 | 5 | 5 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B28 | 3 | 3 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B29 | 5 | 5 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B30 | 3 | 3 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B31 | 5 | 5 | ISV |   | 8/5/2026 17:44:58 |
| RB-008 | B32 | 5 | 5 | ISV |   | 8/5/2026 17:44:58 |
| RB-008 | B33 | 3 | 3 | ISV |   | 8/5/2026 17:44:58 |
| RB-008 | B34 | 3 | 3 | ISV |   | 8/5/2026 17:44:58 |
| RB-008 | B35 | 3 | 3 | ISV |   | 8/5/2026 17:44:58 |
| RB-008 | B36 | 7 | 7 | ICM |   | 8/5/2026 17:44:58 |
| RB-008 | B37 | 8 | 8 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B38 | 8 | 8 | IST |   | 8/5/2026 17:44:58 |
| RB-008 | B39 | 0 | 10 | IST_RISCO |   | 8/5/2026 17:44:58 |
| RB-008 | B40 | 8 | 8 | ISC |   | 8/5/2026 17:44:58 |
| RB-008 | B41 | 6 | 6 | CONF_FIS |   | 8/5/2026 17:44:58 |
| RB-008 | B42 | 8 | 8 | CONF_TEC |   | 8/5/2026 17:44:58 |
| RB-008 | B43 | 6 | 6 | CONF_OFE |   | 8/5/2026 17:44:58 |
| RB-008 | B44 | 8 | 8 | CONF_DEF |   | 8/5/2026 17:44:58 |
| RB-008 | B45 | 8 | 8 | CONF_PRESSAO |   | 8/5/2026 17:44:58 |
| RB-008 | B46 | 10 | 10 | CONF_ERRO |   | 8/5/2026 17:44:58 |
| RB-008 | B47 |   |   | QUALITATIVO | Participo com esforço reduzido | 8/5/2026 17:44:58 |
| RB-008 | B48 |   |   | QUALITATIVO | Continuo tentando | 8/5/2026 17:44:58 |
| RB-008 | B49 |   |   | QUALITATIVO | Mantenho o compromisso com menor motivação | 8/5/2026 17:44:58 |
| RB-008 | B50 |   |   | QUALITATIVO | A maioria | 8/5/2026 17:44:58 |
| RB-008 | B51 |   |   | QUALITATIVO | Posicionamento e leitura técnica | 8/5/2026 17:44:58 |
| RB-008 | B52 |   |   | QUALITATIVO | Transição defesa ataque | 8/5/2026 17:44:58 |
| RB-008 | B53 |   |   | QUALITATIVO | Posicionamento, defesa e transição defesa ataque | 8/5/2026 17:44:58 |
| RB-008 | B54 |   |   | QUALITATIVO | Repetição de algo que o time ainda não consegue executar | 8/5/2026 17:44:58 |
| RB-008 | B55 |   |   | QUALITATIVO | Pessoas irritadas e intolerantes aos erros coletivos | 8/5/2026 17:44:58 |
| RB-008 | B56 |   |   | QUALITATIVO | Orientação e motivação por parte do técnico | 8/5/2026 17:44:58 |
| RB-008 | B57 |   |   | QUALITATIVO | Fragmentar as tarefas “novas/ difíceis” para mudar a ação final e êxodo na execução | 8/5/2026 17:44:58 |
| RB-008 | B58 |   |   | QUALITATIVO | Acredito que em algum momentos o treinador espero que o time alcance algumas ações que o time ainda não é capaz de realizar, isso gera frustração, acho que dividir os processos possa ajudar na mudança e evolução das ações de ataque e defesa. | 8/5/2026 17:44:58 |
| RB-009 | B01 | 4 | 4 | ICM |   | 8/6/2026 14:34:50 |
| RB-009 | B02 | 4 | 4 | ICM |   | 8/6/2026 14:34:50 |
| RB-009 | B03 | 3 | 3 | ICM |   | 8/6/2026 14:34:50 |
| RB-009 | B04 | 3 | 3 | ICM |   | 8/6/2026 14:34:50 |
| RB-009 | B05 | 4 | 4 | ICM |   | 8/6/2026 14:34:50 |
| RB-009 | B06 | 4 | 4 | ICM |   | 8/6/2026 14:34:50 |
| RB-009 | B07 | 3 | 3 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B08 | 3 | 3 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B09 | 5 | 5 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B10 | 5 | 5 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B11 | 3 | 3 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B12 | 2 | 4 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B13 | 3 | 3 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B14 | 2 | 2 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B15 | 3 | 3 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B16 | 4 | 2 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B17 | 3 | 3 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B18 | 2 | 2 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B19 | 5 | 5 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B20 | 4 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B21 | 5 | 5 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B22 | 4 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B23 | 4 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B24 | 4 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B25 | 2 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B26 | 2 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B27 | 4 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B28 | 5 | 5 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B29 | 2 | 2 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B30 | 4 | 4 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B31 | 4 | 4 | ISV |   | 8/6/2026 14:34:50 |
| RB-009 | B32 | 3 | 3 | ISV |   | 8/6/2026 14:34:50 |
| RB-009 | B33 | 1 | 1 | ISV |   | 8/6/2026 14:34:50 |
| RB-009 | B34 | 2 | 2 | ISV |   | 8/6/2026 14:34:50 |
| RB-009 | B35 | 1 | 1 | ISV |   | 8/6/2026 14:34:50 |
| RB-009 | B36 | 7 | 7 | ICM |   | 8/6/2026 14:34:50 |
| RB-009 | B37 | 9 | 9 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B38 | 8 | 8 | IST |   | 8/6/2026 14:34:50 |
| RB-009 | B39 | 2 | 8 | IST_RISCO |   | 8/6/2026 14:34:50 |
| RB-009 | B40 | 7 | 7 | ISC |   | 8/6/2026 14:34:50 |
| RB-009 | B41 | 6 | 6 | CONF_FIS |   | 8/6/2026 14:34:50 |
| RB-009 | B42 | 8 | 8 | CONF_TEC |   | 8/6/2026 14:34:50 |
| RB-009 | B43 | 9 | 9 | CONF_OFE |   | 8/6/2026 14:34:50 |
| RB-009 | B44 | 8 | 8 | CONF_DEF |   | 8/6/2026 14:34:50 |
| RB-009 | B45 | 6 | 6 | CONF_PRESSAO |   | 8/6/2026 14:34:50 |
| RB-009 | B46 | 8 | 8 | CONF_ERRO |   | 8/6/2026 14:34:50 |
| RB-009 | B47 |   |   | QUALITATIVO | Participo normalmente | 8/6/2026 14:34:50 |
| RB-009 | B48 |   |   | QUALITATIVO | Continuo tentando | 8/6/2026 14:34:50 |
| RB-009 | B49 |   |   | QUALITATIVO | Mantenho o compromisso com menor motivação | 8/6/2026 14:34:50 |
| RB-009 | B50 |   |   | QUALITATIVO | A maioria | 8/6/2026 14:34:50 |
| RB-009 | B51 |   |   | QUALITATIVO | velocidade | 8/6/2026 14:34:50 |
| RB-009 | B52 |   |   | QUALITATIVO | ansiedade é gestão de tempo | 8/6/2026 14:34:50 |
| RB-009 | B53 |   |   | QUALITATIVO | visão de jogo | 8/6/2026 14:34:50 |
| RB-009 | B54 |   |   | QUALITATIVO | gosto do treino | 8/6/2026 14:34:50 |
| RB-009 | B55 |   |   | QUALITATIVO | ficar parada | 8/6/2026 14:34:50 |
| RB-009 | B56 |   |   | QUALITATIVO | me deixar em movimento | 8/6/2026 14:34:50 |
| RB-009 | B57 |   |   | QUALITATIVO |   | 8/6/2026 14:34:50 |
| RB-009 | B58 |   |   | QUALITATIVO |   | 8/6/2026 14:34:50 |
| RB-010 | B01 | 5 | 5 | ICM |   | 8/6/2026 18:52:49 |
| RB-010 | B02 | 5 | 5 | ICM |   | 8/6/2026 18:52:49 |
| RB-010 | B03 | 4 | 4 | ICM |   | 8/6/2026 18:52:49 |
| RB-010 | B04 | 4 | 4 | ICM |   | 8/6/2026 18:52:49 |
| RB-010 | B05 | 5 | 5 | ICM |   | 8/6/2026 18:52:49 |
| RB-010 | B06 | 5 | 5 | ICM |   | 8/6/2026 18:52:49 |
| RB-010 | B07 | 4 | 4 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B08 | 4 | 4 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B09 | 5 | 5 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B10 | 5 | 5 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B11 | 1 | 5 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B12 | 1 | 5 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B13 | 5 | 5 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B14 | 3 | 3 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B15 | 5 | 5 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B16 | 1 | 5 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B17 | 3 | 3 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B18 | 3 | 3 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B19 | 5 | 5 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B20 | 4 | 4 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B21 | 4 | 4 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B22 | 5 | 5 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B23 | 5 | 5 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B24 | 3 | 3 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B25 | 3 | 3 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B26 | 2 | 4 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B27 | 4 | 4 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B28 | 4 | 4 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B29 | 5 | 5 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B30 | 5 | 5 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B31 | 5 | 5 | ISV |   | 8/6/2026 18:52:49 |
| RB-010 | B32 | 5 | 5 | ISV |   | 8/6/2026 18:52:49 |
| RB-010 | B33 | 5 | 5 | ISV |   | 8/6/2026 18:52:49 |
| RB-010 | B34 | 5 | 5 | ISV |   | 8/6/2026 18:52:49 |
| RB-010 | B35 | 5 | 5 | ISV |   | 8/6/2026 18:52:49 |
| RB-010 | B36 | 9 | 9 | ICM |   | 8/6/2026 18:52:49 |
| RB-010 | B37 | 8 | 8 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B38 | 7 | 7 | IST |   | 8/6/2026 18:52:49 |
| RB-010 | B39 | 5 | 5 | IST_RISCO |   | 8/6/2026 18:52:49 |
| RB-010 | B40 | 8 | 8 | ISC |   | 8/6/2026 18:52:49 |
| RB-010 | B41 | 9 | 9 | CONF_FIS |   | 8/6/2026 18:52:49 |
| RB-010 | B42 | 9 | 9 | CONF_TEC |   | 8/6/2026 18:52:49 |
| RB-010 | B43 | 9 | 9 | CONF_OFE |   | 8/6/2026 18:52:49 |
| RB-010 | B44 | 10 | 10 | CONF_DEF |   | 8/6/2026 18:52:49 |
| RB-010 | B45 | 9 | 9 | CONF_PRESSAO |   | 8/6/2026 18:52:49 |
| RB-010 | B46 | 9 | 9 | CONF_ERRO |   | 8/6/2026 18:52:49 |
| RB-010 | B47 |   |   | QUALITATIVO | Participo com esforço reduzido | 8/6/2026 18:52:49 |
| RB-010 | B48 |   |   | QUALITATIVO | Peço ajuda | 8/6/2026 18:52:49 |
| RB-010 | B49 |   |   | QUALITATIVO | Mantenho o compromisso com menor motivação | 8/6/2026 18:52:49 |
| RB-010 | B50 |   |   | QUALITATIVO | A maioria | 8/6/2026 18:52:49 |
| RB-010 | B51 |   |   | QUALITATIVO | Transição | 8/6/2026 18:52:49 |
| RB-010 | B52 |   |   | QUALITATIVO | Nenhuma | 8/6/2026 18:52:49 |
| RB-010 | B53 |   |   | QUALITATIVO | Específico | 8/6/2026 18:52:49 |
| RB-010 | B54 |   |   | QUALITATIVO | Mais coletivo | 8/6/2026 18:52:49 |
| RB-010 | B55 |   |   | QUALITATIVO | Pausas desnecessárias. | 8/6/2026 18:52:49 |
| RB-010 | B56 |   |   | QUALITATIVO | Energia | 8/6/2026 18:52:49 |
| RB-010 | B57 |   |   | QUALITATIVO | Concentração e motivação de todas | 8/6/2026 18:52:49 |
| RB-010 | B58 |   |   | QUALITATIVO | Não | 8/6/2026 18:52:49 |
| RB-011 | B01 | 5 | 5 | ICM |   | 8/6/2026 20:25:46 |
| RB-011 | B02 | 5 | 5 | ICM |   | 8/6/2026 20:25:46 |
| RB-011 | B03 | 5 | 5 | ICM |   | 8/6/2026 20:25:46 |
| RB-011 | B04 | 5 | 5 | ICM |   | 8/6/2026 20:25:46 |
| RB-011 | B05 | 5 | 5 | ICM |   | 8/6/2026 20:25:46 |
| RB-011 | B06 | 5 | 5 | ICM |   | 8/6/2026 20:25:46 |
| RB-011 | B07 | 4 | 4 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B08 | 3 | 3 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B09 | 5 | 5 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B10 | 5 | 5 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B11 | 3 | 3 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B12 | 4 | 2 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B13 | 4 | 4 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B14 | 1 | 1 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B15 | 5 | 5 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B16 | 1 | 5 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B17 | 3 | 3 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B18 | 4 | 4 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B19 | 5 | 5 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B20 | 5 | 5 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B21 | 5 | 5 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B22 | 4 | 4 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B23 | 5 | 5 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B24 | 5 | 5 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B25 | 2 | 4 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B26 | 2 | 4 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B27 | 5 | 5 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B28 | 5 | 5 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B29 | 3 | 3 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B30 | 4 | 4 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B31 | 5 | 5 | ISV |   | 8/6/2026 20:25:46 |
| RB-011 | B32 | 5 | 5 | ISV |   | 8/6/2026 20:25:46 |
| RB-011 | B33 | 5 | 5 | ISV |   | 8/6/2026 20:25:46 |
| RB-011 | B34 | 5 | 5 | ISV |   | 8/6/2026 20:25:46 |
| RB-011 | B35 | 3 | 3 | ISV |   | 8/6/2026 20:25:46 |
| RB-011 | B36 | 8 | 8 | ICM |   | 8/6/2026 20:25:46 |
| RB-011 | B37 | 9 | 9 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B38 | 9 | 9 | IST |   | 8/6/2026 20:25:46 |
| RB-011 | B39 | 2 | 8 | IST_RISCO |   | 8/6/2026 20:25:46 |
| RB-011 | B40 | 7 | 7 | ISC |   | 8/6/2026 20:25:46 |
| RB-011 | B41 | 7 | 7 | CONF_FIS |   | 8/6/2026 20:25:46 |
| RB-011 | B42 | 8 | 8 | CONF_TEC |   | 8/6/2026 20:25:46 |
| RB-011 | B43 | 8 | 8 | CONF_OFE |   | 8/6/2026 20:25:46 |
| RB-011 | B44 | 9 | 9 | CONF_DEF |   | 8/6/2026 20:25:46 |
| RB-011 | B45 | 10 | 10 | CONF_PRESSAO |   | 8/6/2026 20:25:46 |
| RB-011 | B46 | 10 | 10 | CONF_ERRO |   | 8/6/2026 20:25:46 |
| RB-011 | B47 |   |   | QUALITATIVO | Participo normalmente | 8/6/2026 20:25:46 |
| RB-011 | B48 |   |   | QUALITATIVO | Continuo tentando | 8/6/2026 20:25:46 |
| RB-011 | B49 |   |   | QUALITATIVO | Mantenho o mesmo esforço | 8/6/2026 20:25:46 |
| RB-011 | B50 |   |   | QUALITATIVO | A maioria | 8/6/2026 20:25:46 |
| RB-011 | B51 |   |   | QUALITATIVO | Leitura do jogo | 8/6/2026 20:25:46 |
| RB-011 | B52 |   |   | QUALITATIVO | Física | 8/6/2026 20:25:46 |
| RB-011 | B53 |   |   | QUALITATIVO | Bloqueio é físico | 8/6/2026 20:25:46 |
| RB-011 | B54 |   |   | QUALITATIVO |   | 8/6/2026 20:25:46 |
| RB-011 | B55 |   |   | QUALITATIVO | Desmotivação das pessoas, não entenderem o que está sendo pedido | 8/6/2026 20:25:46 |
| RB-011 | B56 |   |   | QUALITATIVO | Esforço coletivo | 8/6/2026 20:25:46 |
| RB-011 | B57 |   |   | QUALITATIVO | Beber mais água | 8/6/2026 20:25:46 |
| RB-011 | B58 |   |   | QUALITATIVO | Treinos mais específicos de defesa | 8/6/2026 20:25:46 |
| RB-012 | B01 | 4 | 4 | ICM |   | 8/6/2026 20:30:47 |
| RB-012 | B02 | 5 | 5 | ICM |   | 8/6/2026 20:30:47 |
| RB-012 | B03 | 3 | 3 | ICM |   | 8/6/2026 20:30:47 |
| RB-012 | B04 | 5 | 5 | ICM |   | 8/6/2026 20:30:47 |
| RB-012 | B05 | 5 | 5 | ICM |   | 8/6/2026 20:30:47 |
| RB-012 | B06 | 3 | 3 | ICM |   | 8/6/2026 20:30:47 |
| RB-012 | B07 | 3 | 3 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B08 | 3 | 3 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B09 | 5 | 5 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B10 | 5 | 5 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B11 | 3 | 3 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B12 | 1 | 5 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B13 | 4 | 4 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B14 | 4 | 4 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B15 | 4 | 4 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B16 | 3 | 3 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B17 | 3 | 3 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B18 | 2 | 2 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B19 | 5 | 5 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B20 | 5 | 5 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B21 | 5 | 5 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B22 | 4 | 4 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B23 | 4 | 4 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B24 | 4 | 4 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B25 | 3 | 3 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B26 | 2 | 4 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B27 | 3 | 3 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B28 | 4 | 4 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B29 | 2 | 2 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B30 | 3 | 3 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B31 | 4 | 4 | ISV |   | 8/6/2026 20:30:47 |
| RB-012 | B32 | 5 | 5 | ISV |   | 8/6/2026 20:30:47 |
| RB-012 | B33 | 3 | 3 | ISV |   | 8/6/2026 20:30:47 |
| RB-012 | B34 | 2 | 2 | ISV |   | 8/6/2026 20:30:47 |
| RB-012 | B35 | 2 | 2 | ISV |   | 8/6/2026 20:30:47 |
| RB-012 | B36 | 7 | 7 | ICM |   | 8/6/2026 20:30:47 |
| RB-012 | B37 | 9 | 9 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B38 | 10 | 10 | IST |   | 8/6/2026 20:30:47 |
| RB-012 | B39 | 5 | 5 | IST_RISCO |   | 8/6/2026 20:30:47 |
| RB-012 | B40 | 8 | 8 | ISC |   | 8/6/2026 20:30:47 |
| RB-012 | B41 | 7 | 7 | CONF_FIS |   | 8/6/2026 20:30:47 |
| RB-012 | B42 | 7 | 7 | CONF_TEC |   | 8/6/2026 20:30:47 |
| RB-012 | B43 | 8 | 8 | CONF_OFE |   | 8/6/2026 20:30:47 |
| RB-012 | B44 | 9 | 9 | CONF_DEF |   | 8/6/2026 20:30:47 |
| RB-012 | B45 | 10 | 10 | CONF_PRESSAO |   | 8/6/2026 20:30:47 |
| RB-012 | B46 | 9 | 9 | CONF_ERRO |   | 8/6/2026 20:30:47 |
| RB-012 | B47 |   |   | QUALITATIVO | Participo com esforço reduzido | 8/6/2026 20:30:47 |
| RB-012 | B48 |   |   | QUALITATIVO | Fico frustrada, mas continuo | 8/6/2026 20:30:47 |
| RB-012 | B49 |   |   | QUALITATIVO | Mantenho o mesmo esforço | 8/6/2026 20:30:47 |
| RB-012 | B50 |   |   | QUALITATIVO | Todos | 8/6/2026 20:30:47 |
| RB-012 | B51 |   |   | QUALITATIVO | Quando conseguimos construir um ataque em que eu consiga entrar com velocidade | 8/6/2026 20:30:47 |
| RB-012 | B52 |   |   | QUALITATIVO | Quando nao tem espaço para pegar a bola em movimento | 8/6/2026 20:30:47 |
| RB-012 | B53 |   |   | QUALITATIVO | giro | 8/6/2026 20:30:47 |
| RB-012 | B54 |   |   | QUALITATIVO | nao acho produtivo o novo aquecimento de goleira | 8/6/2026 20:30:47 |
| RB-012 | B55 |   |   | QUALITATIVO | treinos a noite | 8/6/2026 20:30:47 |
| RB-012 | B56 |   |   | QUALITATIVO | ver a evolução ou entender o que eu preciso ajustar | 8/6/2026 20:30:47 |
| RB-012 | B57 |   |   | QUALITATIVO | treinos de manhã | 8/6/2026 20:30:47 |
| RB-012 | B58 |   |   | QUALITATIVO | Nao | 8/6/2026 20:30:47 |

---

## 📋 Worksheet: METRICAS_B

**Data Dimensions**: 6 rows x 8 columns

| MÉTRICAS AGREGADAS — FORMULÁRIO ANÔNIMO |   |   |   |   |   |   |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dimensao | media_1_5 | indice_0_100 | mediana_0_100 | favoraveis | desfavoraveis | estado | observacao |
| ICM | 4.904761905 | 97.61904762 | 100 | 0.8452380952 | 0.04761904762 | FORTE | Compromisso e motivação |
| ISC | 4.224358974 | 80.60897436 | 75 | 0.641025641 | 0.08974358974 | INTERMEDIÁRIO | Sustentabilidade da carga |
| IST | 4.779761905 | 94.49404762 | 100 | 0.8452380952 | 0.08333333333 | FORTE | Satisfação com o treinamento |
| ISV | 3.85 | 71.25 | 75 | 0.6166666667 | 0.1666666667 | INTERMEDIÁRIO | Segurança para falar |

---

## 📋 Worksheet: CHECKLIST

**Data Dimensions**: 13 rows x 6 columns

| acao | descricao | responsavel | status | evidencia | criterio_aceite |
| --- | --- | --- | --- | --- | --- |
| ACT-PESQ-01 | Congelar escopo, datas, horários e versão | Treinador | CONCLUÍDO | Escopo e datas congelados. Referência operacional vinculada ao DATABASE: 25/09/2026 a 27/09/2026, São Miguel do Iguaçu/PR. A referência histórica de 23/09 permanece apenas para auditoria. | Nenhuma alteração silenciosa após envio |
| ACT-PESQ-02 | Confirmar quadra, iluminação, segurança e treinador em todos os slots | Treinador | PENDENTE — AÇÃO HUMANA | Quadra, iluminação, segurança e presença do treinador não são verificáveis pelo conector. | Nenhum horário impossível no formulário |
| ACT-PESQ-03 | Validar atletas e cadastro tático | Treinador | CONCLUÍDO | 19 atletas e cadastro tático presentes em ATLETAS. | 19 atletas ativas e posições validadas |
| ACT-PESQ-04 | Criar Formulário A nominal | Apps Script | CONCLUÍDO | 13 respostas nominais V4 recebidas; 26 cabeçalhos correspondem ao FORM_A. | 35 horários e cinco blocos corretos |
| ACT-PESQ-05 | Criar Formulário B anônimo | Apps Script | CONCLUÍDO | 12 respostas recebidas; base possui Timestamp + 58 respostas e nenhuma coluna de nome/e-mail. | Sem nome ou e-mail |
| ACT-PESQ-06 | Testar privacidade do Formulário B | Treinador | CONCLUÍDO | Teste estrutural de privacidade aprovado na base de respostas anônimas. | Resposta teste não revela identidade |
| ACT-PESQ-07 | Testar ambos no celular | Treinador | BLOQUEADO — TESTE HUMANO | Teste em celular exige abertura manual dos Forms e não foi inferido. | Perguntas, obrigatoriedade e gravação corretas |
| ACT-PESQ-08 | Enviar links com prazo | Treinador | PARCIAL | 13/19 respostas nominais e 12 respostas anônimas registradas; cobertura total depende de envio/cobrança humana. | Finalidades nominal/anônima claras |
| ACT-PESQ-09 | Normalizar respostas nominais | Planilha/Script | CONCLUÍDO | NORMALIZADO_A materializado com 2.730 linhas; origem e horário preservados. | Uma linha por atleta, slot e data |
| ACT-PESQ-10 | Aplicar CQV e treinabilidade | Planilha/Script | CONCLUÍDO | CQV, treinabilidade e matching básico por atletas distintas ativos em ANALISE_SLOTS. | Matching tático ainda deve ser executado |
| ACT-PESQ-11 | Calcular ICM, ISC, IST e ISV | Planilha | CONCLUÍDO | RESPOSTAS_B_NORM materializado com 696 linhas; métricas ICM/ISC/IST/ISV recalculadas. | Dimensões separadas |
| ACT-PESQ-12 | Produzir decisão e iniciar teste de duas semanas | Treinador | PENDENTE — DECISÃO HUMANA | A planilha agora produz decisão recomendada; iniciar teste de duas semanas depende do treinador. | Decisão registrada e validada por presença real |

---

## 📋 Worksheet: ROTEIRO

**Data Dimensions**: 9 rows x 4 columns

| ROTEIRO DE LANÇAMENTO — 20 MINUTOS |   |   |   |
| --- | --- | --- | --- |
| Janela | Ação | Saída | Bloqueio |
| 0–2 min | Confirmar versão, prazo e viabilidade dos 35 horários | Escopo congelado | Não oferecer horário inviável |
| 2–5 min | Abrir Apps Script, colar o arquivo e executar criarPesquisaCompleta() | Dois Forms e duas planilhas | Autorizar Forms, Drive e Sheets |
| 5–8 min | Abrir os links gravados na aba CONTROLE | Formulários acessíveis | Falha de criação ou publicação |
| 8–12 min | Revisar Formulário A no celular | Horários, datas e obrigatoriedade corretos | Lista incompleta ou fora de ordem |
| 12–16 min | Revisar Formulário B no celular | Sem nome/e-mail e com perguntas corretas | Qualquer identificação automática |
| 16–18 min | Enviar uma resposta fictícia em cada formulário | Respostas gravadas | Destino incorreto |
| 18–20 min | Excluir ou marcar testes e enviar links às atletas | Pesquisa em produção | Não enviar Form B se anonimato falhar |

---

## 📋 Worksheet: FONTES

**Data Dimensions**: 10 rows x 3 columns

| fonte | conteudo_utilizado | estado |
| --- | --- | --- |
| Imagem de calendário enviada em 04/08/2026 | Etapa Final 24/09 a 27/09; São Miguel do Iguaçu/PR | PROVISÓRIO — diverge do guia |
| GUIA CBHBPRAIA 2026, página 6 | Etapa Final 23/09 a 27/09; inscrição 10/09; lista nominal 18/09; local São Miguel do Iguaçu/PR | FONTE ANEXADA |
| CEPRAEA DATABASE — DB_ATLETAS | 19 atletas ativas, função e posição principal | VALIDADO |
| CEPRAEA DATABASE — DB_ATLETA_POSICOES_TATICAS | Posições ofensivas, defensivas, goleiras e status de validação | VALIDADO |
| Plano de Implementação — Google Doc | Regras, métricas, riscos e critérios de aceite | ATUALIZANDO |
| Documentação oficial Google Apps Script Forms | Criação, publicação, destino, coleta de e-mail e limite de respostas | VALIDADO |
| Respostas do Formulário A — planilha 16fW… | 13 respostas nominais V4; fonte de NORMALIZADO_A | VALIDADO — BRUTO PRESERVADO |
| Respostas do Formulário B — planilha 1Grj… | 12 respostas anônimas; Timestamp + 58 itens sem nome/e-mail | VALIDADO — BRUTO PRESERVADO |
| Execução de normalização 2026-08-09 16:18 BRT | 2.730 linhas em NORMALIZADO_A e 696 em RESPOSTAS_B_NORM | EXECUTADO E REVALIDADO |

---

## 📋 Worksheet: DB_IMPORT

**Data Dimensions**: 107 rows x 9 columns

| export_key | categoria | titulo | valor_1 | valor_2 | valor_3 | status | updated_at | origem_db |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TEAM_TOTAL_ATLETAS | ELENCO | Total de atletas ativas | 19 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| TEAM_GOLEIRAS | ELENCO | Goleiras ativas | 3 |   |   | ATIVO | 2026-08-10 14:20:00 | DB_ATLETAS |
| TEAM_DEFESAS | ELENCO | Defesas ativas | 7 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| TEAM_ATAQUES | ELENCO | Ataques ativas | 12 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| POS_CENTRAL | POSICAO | Centrais ativas | 5 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| POS_LATERAL_ESQUERDA | POSICAO | Laterais esquerdas ativas | 3 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| POS_LATERAL_DIREITA | POSICAO | Laterais direitas ativas | 2 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| POS_PIVO | POSICAO | Pivôs ativas | 2 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| POS_DEF_SOLTA | POSICAO | Defensoras soltas ativas | 2 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| POS_DEF_BASE | POSICAO | Defensoras base ativas | 1 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| POS_DEF_COBERTURA | POSICAO | Defensoras cobertura ativas | 1 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_ATLETAS |
| NEXT_TRAINING_DATE | TREINO | Próximo treino | SEM_PROXIMO_TREINO |   |   | ATIVO | 2026-08-09 16:18:09 | DB_CALENDARIO |
| JUNE_TRAINING_COUNT | TREINO | Treinos cadastrados em junho | 8 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_CALENDARIO |
| FRONTEND_CONNECTION_STATUS | SISTEMA | Conexão com frontend | CONECTADO | IMPORTRANGE autorizado e importando no frontend. |   | ATIVO | 2026-08-09 16:18:09 | DB_CONFIG |
| TACT_NEXT_TRAINING_DATE | COBERTURA_TATICA | Próximo treino avaliado | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_DEF_30_COVERAGE | COBERTURA_TATICA | Defesa 3:0 coberta | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_DEF_21_COVERAGE | COBERTURA_TATICA | Defesa 2:1 coberta | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_OF_31_COVERAGE | COBERTURA_TATICA | Ataque 3:1 coberto | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_OF_21_COVERAGE | COBERTURA_TATICA | Ataque 2:1 coberto | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_GARGALOS_NEXT | COBERTURA_TATICA | Gargalos do próximo treino | DADOS_AUSENTES — NÃO É POSSÍVEL AVALIAR GARGALOS |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_EXPORT_STATUS | COBERTURA_TATICA | Exportação cobertura tática | INTERNO_NAO_PUBLICAR |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_DEF_30_GAPS_COUNT | COBERTURA_TATICA | Defesa 3:0 gargalos | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_DEF_21_GAPS_COUNT | COBERTURA_TATICA | Defesa 2:1 gargalos | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_OF_31_GAPS_COUNT | COBERTURA_TATICA | Ataque 3:1 gargalos | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_OF_21_GAPS_COUNT | COBERTURA_TATICA | Ataque 2:1 gargalos | DADOS_AUSENTES |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| TACT_GARGALOS_SUMMARY | COBERTURA_TATICA | Resumo curto de gargalos | DADOS_AUSENTES — SEM BASE FUTURA |   |   | TECNICO_INTERNO | 2026-08-10 04:56:07 |   |
| NEXT_TRAINING_DAY | TREINO_PUBLICO | Dia da semana do próximo treino |   |   |   |   | 2026-08-09 16:18:09 |   |
| NEXT_TRAINING_TIME | TREINO_PUBLICO | Horário do próximo treino |   |   |   |   | 2026-08-09 16:18:09 |   |
| NEXT_TRAINING_LOCATION | TREINO_PUBLICO | Local do próximo treino | SEM_PROXIMO_TREINO |   |   |   | 2026-08-09 16:18:09 |   |
| NEXT_TRAINING_ACTIVITY | TREINO_PUBLICO | Atividade principal | SEM_PROXIMO_TREINO |   |   |   | 2026-08-09 16:18:09 |   |
| NEXT_TRAINING_OBJECTIVE | TREINO_PUBLICO | Objetivo do treino | SEM_PROXIMO_TREINO |   |   |   | 2026-08-09 16:18:09 |   |
| NEXT_TRAINING_COLLECTIVE_GOALS | TREINO_PUBLICO | Metas coletivas | SEM_PROXIMO_TREINO |   |   |   | 2026-08-09 16:18:09 |   |
| NEXT_TRAINING_ORIENTATION | TREINO_PUBLICO | Orientação para atletas | SEM_PROXIMO_TREINO |   |   |   | 2026-08-09 16:18:09 |   |
| NEXT_TRAINING_PUBLIC_STATUS | TREINO_PUBLICO | Status do bloco público | SEM_PROXIMO_TREINO |   |   |   | 2026-08-09 16:18:09 |   |
| GAMES_TOTAL_VALIDOS | ANALISE_JOGOS | Jogos com resultado válido | 34 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_VITORIAS | ANALISE_JOGOS | Vitórias CEPRAEA | 23 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_DERROTAS | ANALISE_JOGOS | Derrotas CEPRAEA | 10 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_APROVEITAMENTO | ANALISE_JOGOS | Aproveitamento em jogos válidos | 68% |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_SETS_VENCIDOS | ANALISE_JOGOS | Sets vencidos | 51 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_SETS_PERDIDOS | ANALISE_JOGOS | Sets perdidos | 26 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_SHOOTOUTS | ANALISE_JOGOS | Jogos decididos em shoot-out | 11 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_PENDENCIAS | ANALISE_JOGOS | Pendências de dados dos jogos | 6 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_RESULTADOS_PENDENTES | ANALISE_JOGOS | Resultados pendentes | 8 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_SETS_INCOMPLETOS | ANALISE_JOGOS | Jogos com sets incompletos | 5 |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| GAMES_ANALYSIS_STATUS | ANALISE_JOGOS | Status da análise de jogos | CONECTADO_COM_PENDENCIAS |   |   | ATIVO | 2026-08-09 16:18:09 | DB_JOGOS |
| STAGE4_COMPETITION_ID | ETAPA_23_08 | ID da 4ª Etapa Estadual | COMP-2026-006 |   |   |   |   |   |
| STAGE4_NAME | ETAPA_23_08 | Nome da 4ª Etapa | Circuito Estadual de Handebol de Praia 2026 - 4ª Etapa |   |   |   |   |   |
| STAGE4_DATE | ETAPA_23_08 | Data da 4ª Etapa | 23/08/2026 |   |   |   |   |   |
| STAGE4_LOCATION | ETAPA_23_08 | Local da 4ª Etapa | Icaraí - Niterói/RJ |   |   |   |   |   |
| STAGE4_STATUS | ETAPA_23_08 | Status canônico da competição | REALIZADA |   |   |   |   |   |
| STAGE4_PARTICIPATION | ETAPA_23_08 | Participação CEPRAEA | PARTICIPOU |   |   |   |   |   |
| STAGE4_GAMES | ETAPA_23_08 | Jogos realizados na etapa | 5 |   |   |   |   |   |
| STAGE4_WINS | ETAPA_23_08 | Vitórias na etapa | 5 |   |   |   |   |   |
| STAGE4_LOSSES | ETAPA_23_08 | Derrotas na etapa | 0 |   |   |   |   |   |
| STAGE4_SETS_WON | ETAPA_23_08 | Sets vencidos na etapa | 10 |   |   |   |   |   |
| STAGE4_SETS_LOST | ETAPA_23_08 | Sets perdidos na etapa | 2 |   |   |   |   |   |
| STAGE4_SHOOTOUTS | ETAPA_23_08 | Shoot-outs na etapa | 2 |   |   |   |   |   |
| STAGE4_DATA_PENDING | ETAPA_23_08 | Jogos com qualidade de dados pendente | 5 |   |   |   |   |   |
| STAGE4_GROUP_GAMES | ETAPA_23_08 | Jogos de grupos realizados | 3 |   |   |   |   |   |
| STAGE4_GROUP_WINS | ETAPA_23_08 | Vitórias na fase de grupos | 3 |   |   |   |   |   |
| STAGE4_J1 | ETAPA_23_08 | J1 — código, resultado, status | J1 | CEPRAEA 2 x 0 Campinas 360° Nas Areias | REALIZADO |   |   |   |
| STAGE4_J6 | ETAPA_23_08 | J6 — código, resultado, status | J6 | NR Beach 1 x 2 CEPRAEA | REALIZADO |   |   |   |
| STAGE4_J12 | ETAPA_23_08 | J12 — código, resultado, status | J12 | Niterói Rugby F.C. 1 x 2 CEPRAEA | REALIZADO |   |   |   |
| STAGE4_SEMIFINAL | ETAPA_23_08 | Semifinal — código, resultado, status | J20 | CEPRAEA 2 x 0 RioHandBeach | REALIZADO |   |   |   |
| STAGE4_FINAL | ETAPA_23_08 | Final — código, resultado, status | J24 | IDEC 0 x 2 CEPRAEA | REALIZADO |   |   |   |
| STAGE4_STATE | ETAPA_23_08 | Estado operacional da etapa | CAMPEAO |   |   |   |   |   |
| STAGE4_RESULT_LABEL | ETAPA_23_08 | Resultado geral da etapa | 🏆 CEPRAEA campeão da 4ª Etapa Estadual. |   |   |   |   |   |
| STAGE4_ROSTER_GOLEIRAS | ETAPA_23_08 | Convocadas — goleiras | #85 Carolina Bezerra  •  #25 Paola Wolff |   |   |   |   |   |
| STAGE4_ROSTER_DEFESA | ETAPA_23_08 | Convocadas — defesa | #3 Aline Mello  •  #6 Carolina Peixinho  •  #7 Gabi Peixinho  •  #22 Rafaela Dillmann |   |   |   |   |   |
| STAGE4_ROSTER_ATAQUE | ETAPA_23_08 | Convocadas — ataque | #19 Aline Augusto  •  #8 Aline Kecia  •  #10 Beatriz Correia  •  #9 Bruna Xavier  •  #14 Fernanda Campbell  •  #16 Marleide Nunes |   |   |   |   |   |
| FINAL_BR_COMPETITION_ID | FINAL_BR | ID da Final BR | COMP-2026-012 |   |   |   |   |   |
| FINAL_BR_NAME | FINAL_BR | Nome da Final BR | Etapa Final — Circuito Brasileiro de Handebol de Praia 2026 |   |   |   |   |   |
| FINAL_BR_DATE_RANGE | FINAL_BR | Período da Final BR | 25–27/09 |   |   |   |   |   |
| FINAL_BR_LOCATION | FINAL_BR | Local da Final BR | São Miguel do Iguaçu/PR |   |   |   |   |   |
| FINAL_BR_PARTICIPATION | FINAL_BR | Participação na Final BR | PARTICIPOU |   |   |   |   |   |
| FINAL_BR_STATUS | FINAL_BR | Status da Final BR | REALIZADA |   |   |   |   |   |
| FINAL_BR_ROSTER_DEADLINE | FINAL_BR | Prazo da relação nominal da Final BR | 18/09 |   |   |   |   |   |
| STAGE4_KNOCKOUT_SUMMARY | ETAPA_23_08 | Resumo do mata-mata | Semifinal e final concluídas. |   |   |   |   |   |
| STAGE4_STATUS_LABEL | ETAPA_23_08 | Rótulo de status da etapa | 🏆 ETAPA ENCERRADA — CEPRAEA CAMPEÃO |   |   |   |   |   |
| STAGE4_NEXT_STEP | ETAPA_23_08 | Próximo passo operacional | Recuperar, responder ao fechamento da etapa e preparar o próximo ciclo de treinos. |   |   |   |   |   |
| STAGE4_GROUP_SUMMARY | ETAPA_23_08 | Resumo da fase de grupos | ✅ 3 jogos • 3 vitórias • classificação em 1º do grupo |   |   |   |   |   |
| STAGE4_RESULT_OR_NEXT | ETAPA_23_08 | Resultado final ou próximo jogo | 🏆 IDEC 0 x 2 CEPRAEA |   |   |   |   |   |
| STAGE4_DATA_PENDING_LABEL | ETAPA_23_08 | Texto de qualidade de dados da etapa | 5 jogo(s) com parciais pendentes. |   |   |   |   |   |
| STAGE4_COURTS | ETAPA_23_08 | Quadras utilizadas na etapa | Quadra 1 e Quadra 2 |   |   |   |   |   |
| STAGE4_LOCATION_FULL | ETAPA_23_08 | Local completo da etapa | Icaraí - Niterói/RJ — Quadra 1 e Quadra 2 |   |   |   |   |   |
| FINAL_BR_START_DATE | FINAL_BR | Data inicial completa da Final BR | 25/09/2026 |   |   |   |   |   |
| FINAL_BR_END_DATE | FINAL_BR | Data final completa da Final BR | 27/09/2026 |   |   |   |   |   |
| NEXT_TRAINING_ID | TREINO_PUBLICO | ID estável do próximo treino | SEM_PROXIMO_TREINO |   |   | ATIVO | 2026-08-24 12:11:00 | DB_TREINOS |
| FINAL_BR_REGISTRATION_DEADLINE | FINAL_BR | Prazo de inscrição da Final BR | 10/09 |   |   | ATIVO | 2026-09-08T22:26:29-03:00 | Classificacao Geral .pdf — CBHb 01/09/2026 |
| INTERNATIONAL_J1 | INTERNACIONAL | J2 — Costa Beach BMP × CEPRAEA | 10/09 | 08:45 | Costa Beach BMP × CEPRAEA | PREVISTO_RESULTADO_PENDENTE | 2026-09-08T22:26:29-03:00 | DB_JOGOS |
| INTERNATIONAL_J2 | INTERNACIONAL | J8 — La Muni × CEPRAEA | 10/09 | 15:45 | La Muni × CEPRAEA | PREVISTO_RESULTADO_PENDENTE | 2026-09-08T22:26:29-03:00 | DB_JOGOS |
| INTERNATIONAL_J3 | INTERNACIONAL | J16 — CATS × CEPRAEA | 11/09 | 10:15 | CATS × CEPRAEA | PREVISTO_RESULTADO_PENDENTE | 2026-09-08T22:26:29-03:00 | DB_JOGOS |
| INTERNATIONAL_J4 | INTERNACIONAL | J21 — CEPRAEA × IDEC | 11/09 | 16:30 | CEPRAEA × IDEC | PREVISTO_RESULTADO_PENDENTE | 2026-09-08T22:26:29-03:00 | DB_JOGOS |
| INTERNATIONAL_J5 | INTERNACIONAL | J25 — CEPRAEA × Niterói Rugby F.C. | 12/09 | 08:00 | CEPRAEA × Niterói Rugby F.C. | PREVISTO_RESULTADO_PENDENTE | 2026-09-08T22:26:29-03:00 | DB_JOGOS |
| COMP-2026-001 | COMPETICAO | Copa Brasil Adulto de Handebol de Praia 2026 | 26-29/03 | João Pessoa - PB | PARTICIPOU | REALIZADA |   | DB_COMPETICOES |
| COMP-2026-002 | COMPETICAO | Circuito Estadual de Handebol de Praia 2026 - 1ª Etapa | 26/04 | Niterói - RJ | PARTICIPOU | REALIZADA |   | DB_COMPETICOES |
| COMP-2026-003 | COMPETICAO | 2ª Etapa — Circuito Brasileiro de Handebol de Praia 2026 | 04-07/06 | Paranaguá - PR | PARTICIPOU | REALIZADA |   | DB_COMPETICOES |
| COMP-2026-004 | COMPETICAO | Circuito Estadual de Handebol de Praia 2026 - 2ª Etapa | 31/05 | Niterói - RJ | PARTICIPOU | REALIZADA |   | DB_COMPETICOES |
| COMP-2026-005 | COMPETICAO | Circuito Estadual de Handebol de Praia 2026 - 3ª Etapa | 05/07 | Niterói - RJ | PARTICIPOU | REALIZADA |   | DB_COMPETICOES |
| COMP-2026-006 | COMPETICAO | Circuito Estadual de Handebol de Praia 2026 - 4ª Etapa | 23/08 | Niterói - RJ | PARTICIPOU | REALIZADA |   | DB_COMPETICOES |
| COMP-2026-007 | COMPETICAO | 4ª Etapa — Circuito Brasileiro de Handebol de Praia 2026 | 27-30/08 | João Pessoa - PB | NAO_PARTICIPARA | PREVISTA |   | DB_COMPETICOES |
| COMP-2026-008 | COMPETICAO | Campeonato Internacional de Clubes de Handebol de Praia | 10-13/09 | Niterói - RJ | PARTICIPARA | PREVISTA |   | DB_COMPETICOES |
| COMP-2026-009 | COMPETICAO | Circuito Estadual de Handebol de Praia 2026 - 5ª Etapa | 20/09 | Niterói - RJ | PARTICIPARA | PREVISTA |   | DB_COMPETICOES |
| COMP-2026-010 | COMPETICAO | Circuito Estadual de Handebol de Praia 2026 - 6ª Etapa | 22/11 | Niterói - RJ | PARTICIPARA | PREVISTA |   | DB_COMPETICOES |
| COMP-2026-011 | COMPETICAO | 3ª Etapa — Circuito Brasileiro de Handebol de Praia 2026 | 23-26/07 | Matinhos - PR | NAO_PARTICIPOU | REALIZADA |   | DB_COMPETICOES |
| COMP-2026-012 | COMPETICAO | Etapa Final — Circuito Brasileiro de Handebol de Praia 2026 | 25-27/09 | São Miguel do Iguaçu - PR | PARTICIPOU | REALIZADA |   | DB_COMPETICOES |

---

