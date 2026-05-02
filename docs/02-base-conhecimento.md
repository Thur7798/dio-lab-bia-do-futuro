# Base de Conhecimento

## Dados Utilizados

Os arquivos da pasta `data` foram usados como base mockada para simular informações financeiras e interações do cliente:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|----------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e manter histórico de conversas |
| `perfil_investidor.json` | JSON | Definir perfil de risco (conservador, moderado, arrojado) para personalizar explicações |
| `produtos_financeiros.json` | JSON | Listar produtos financeiros genéricos e exemplificar conceitos |
| `transacoes.csv` | CSV | Simular padrão de gastos do cliente e mostrar exemplos práticos |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

Os dados foram mantidos como **mockados** para fins de demonstração.  
- Pequenas alterações foram feitas para simplificar os exemplos (valores e categorias de transações).  
- O `perfil_investidor.json` foi expandido com descrições mais claras para cada perfil.  
- O `historico_atendimento.csv` foi usado apenas como referência, sem integração real com logs.  

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV são carregados no início da sessão e ficam disponíveis no contexto do agente.  

### Como os dados são usados no prompt?
- Os dados são consultados dinamicamente conforme a interação.  
- Informações relevantes (perfil, transações, histórico) são incluídas no **contexto do prompt** para que o agente responda de forma personalizada.  
- Não há inserção direta no *system prompt*, mas sim uso contextual durante a conversa.  

---

## Exemplo de Contexto Montado

```
Dados do Cliente:

Nome: João Silva
Idade: 32 anos
Perfil: Moderado
Objetivo: Construir reserva de emergência
Patrimônio total: R$ 15.000
Reserva atual: R$ 10.000
Saldo disponível: R$ 5.000

Últimas transações:

01/10: Salário – R$ 5.000 (entrada)
02/10: Aluguel – R$ 1.200 (saída)
03/10: Supermercado – R$ 450 (saída)
05/10: Netflix – R$ 55,90 (saída)
07/10: Farmácia – R$ 89 (saída)
10/10: Restaurante – R$ 120 (saída)
12/10: Uber – R$ 45 (saída)
15/10: Conta de Luz – R$ 180 (saída)
20/10: Academia – R$ 99 (saída)
25/10: Combustível – R$ 250 (saída)
28/10: Aplicação em Tesouro Selic – R$ 500 (saída)

Histórico de atendimento:

15/09: Perguntou sobre CDB Liquidez Diária
22/09: Problema no app (extrato)
01/10: Solicitou explicação sobre Tesouro Selic
12/10: Acompanhou progresso da reserva de emergência
25/10: Atualização cadastral (e-mail e telefone)

Produtos disponíveis:

Tesouro Selic → Risco baixo, aporte mínimo R$ 30, indicado para reserva de emergência
CDB Liquidez Diária → Risco baixo, aporte mínimo R$ 100, indicado para segurança com liquidez diária
LCI/LCA → Risco baixo, aporte mínimo R$ 1.000, indicado para quem pode esperar 90 dias
Fundo Multimercado → Risco médio, aporte mínimo R$ 500, indicado para perfil moderado
Fundo de Ações → Risco alto, aporte mínimo R$ 100, indicado para perfil arrojado
```
