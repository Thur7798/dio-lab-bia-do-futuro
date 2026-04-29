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

'''
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

---

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Transporte - R$ 120

---

Histórico de atendimento:
- Perguntou sobre reserva de emergência
- Solicitou explicação sobre perfil de investido
'''