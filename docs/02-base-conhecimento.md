# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no Edu? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, ou seja, dar continuidae ao atendimento de forma mais eficiente. |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas e necessidaes de aprendizado do cliente. |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser ensinados ao cliente. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didática. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto Fundo Imbiliário (FII) substituiu o Fundo Multimercado, pois somente me sinto mais confiante em usar apenas produtos financeiros que eu conheço, assim poderei validar as respostas do Edu de forma mais acertiva.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.
>
> Existem duas possibilidades: injetar os dados diretamente no prompt ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
  produtos = json.load(f)
```
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplismente "injetar" os dados em nosso prompt, garantindo que o agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json):
{
  "nome": "Ivan Ivanovich",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 7000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}
:

TRANSAÇÕES DO CLIENTE (data/transacoes.csv):
data,descricao,categoria,valor,tipo
2025-10-01,Salário,receita,5200.00,entrada
2025-10-01,Aluguel,moradia,1300.00,saida
2025-10-02,Supermercado,alimentacao,380.50,saida
2025-10-03,Uber,transporte,42.00,saida
2025-10-04,Padaria,alimentacao,25.00,saida
2025-10-05,Netflix,lazer,55.90,saida
2025-10-06,Farmácia,saude,76.40,saida
2025-10-07,Restaurante,alimentacao,120.00,saida
2025-10-08,Combustível,transporte,230.00,saida
2025-10-09,Academia,saude,99.00,saida
2025-10-10,Conta de Luz,moradia,185.60,saida
2025-10-11,Supermercado,alimentacao,210.30,saida
2025-10-12,Assinatura Spotify,lazer,21.90,saida
2025-10-13,Ônibus,transporte,18.00,saida
2025-10-14,Almoço fora,alimentacao,45.00,saida
2025-10-15,Internet,moradia,120.00,saida
2025-10-16,Farmácia,saude,34.90,saida
2025-10-17,Lanche,lazer,22.00,saida
2025-10-18,Supermercado,alimentacao,198.75,saida
2025-10-19,Combustível,transporte,210.00,saida
2025-10-20,Restaurante,alimentacao,135.00,saida
2025-10-21,Conta de Água,moradia,75.40,saida
2025-10-22,Uber,transporte,38.00,saida
2025-10-23,Cinema,lazer,48.00,saida
2025-10-24,Supermercado,alimentacao,260.10,saida
2025-10-25,Farmácia,saude,62.00,saida
2025-10-26,Delivery,lazer,89.90,saida
2025-10-27,Ônibus,transporte,18.00,saida
2025-10-28,Almoço fora,alimentacao,52.00,saida
2025-10-29,Conta de Gás,moradia,95.00,saida
2025-10-30,Lanche,alimentacao,28.50,saida
2025-10-31,Presente,lazer,120.00,saida
2025-11-01,Salário,receita,5200.00,entrada
2025-11-01,Aluguel,moradia,1300.00,saida
2025-11-02,Supermercado,alimentacao,402.80,saida
2025-11-03,Uber,transporte,36.00,saida
2025-11-04,Padaria,alimentacao,19.50,saida
2025-11-05,Netflix,lazer,55.90,saida
2025-11-06,Farmácia,saude,88.20,saida
2025-11-07,Restaurante,alimentacao,110.00,saida
2025-11-08,Combustível,transporte,240.00,saida
2025-11-09,Academia,saude,99.00,saida
2025-11-10,Conta de Luz,moradia,172.30,saida
2025-11-11,Supermercado,alimentacao,225.40,saida
2025-11-12,Spotify,lazer,21.90,saida
2025-11-13,Ônibus,transporte,18.00,saida
2025-11-14,Almoço fora,alimentacao,48.00,saida
2025-11-15,Internet,moradia,120.00,saida
2025-11-16,Farmácia,saude,41.60,saida
2025-11-17,Lanche,lazer,24.00,saida
2025-11-18,Supermercado,alimentacao,215.90,saida
2025-11-19,Combustível,transporte,225.00,saida
2025-11-20,Restaurante,alimentacao,140.00,saida
2025-11-21,Conta de Água,moradia,78.20,saida
2025-11-22,Uber,transporte,40.00,saida
2025-11-23,Cinema,lazer,52.00,saida
2025-11-24,Supermercado,alimentacao,270.00,saida
2025-11-25,Farmácia,saude,69.90,saida
2025-11-26,Delivery,lazer,92.00,saida
2025-11-27,Ônibus,transporte,18.00,saida
2025-11-28,Almoço fora,alimentacao,54.00,saida
2025-11-29,Conta de Gás,moradia,98.00,saida
2025-11-30,Lanche,alimentacao,30.00,saida

HISTÓRICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS DISPONÍVEIS PARA ENSINO (data/produtos_financeiros.json):
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Tesouro IPCA+",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "IPCA + juros",
    "aporte_minimo": 30.00,
    "indicado_para": "Proteção contra inflação no longo prazo"
  },
  {
    "nome": "CDB Prefixado",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "Taxa fixa anual",
    "aporte_minimo": 500.00,
    "indicado_para": "Quem acredita em queda de juros"
  },
  {
    "nome": "Debêntures",
    "categoria": "renda_fixa",
    "risco": "medio",
    "rentabilidade": "CDI + prêmio",
    "aporte_minimo": 1000.00,
    "indicado_para": "Investidores que aceitam mais risco por maior retorno"
  },
  {
    "nome": "Fundo Imobiliário (FII)",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "Dividend Yield (DY) costuma ficar entre 6% de 12% ao ano",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil moderado que busca diversificação e renda recorrente mensal"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  },
  {
    "nome": "ETF de Renda Variável",
    "categoria": "renda_variavel",
    "risco": "alto",
    "rentabilidade": "Variável conforme índice",
    "aporte_minimo": 100.00,
    "indicado_para": "Diversificação em ações com baixo custo"
  },
  {
    "nome": "Ações",
    "categoria": "renda_variavel",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 50.00,
    "indicado_para": "Investidores experientes e de longo prazo"
  },
  {
    "nome": "FII - Fundo Imobiliário",
    "categoria": "renda_variavel",
    "risco": "medio",
    "rentabilidade": "Dividendos mensais + valorização",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca renda passiva mensal"
  },
  {
    "nome": "Previdência Privada PGBL/VGBL",
    "categoria": "previdencia",
    "risco": "baixo",
    "rentabilidade": "Variável conforme fundo",
    "aporte_minimo": 100.00,
    "indicado_para": "Planejamento de longo prazo e aposentadoria"
  },
  {
    "nome": "Conta Remunerada",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% do CDI",
    "aporte_minimo": 0.00,
    "indicado_para": "Dinheiro parado com liquidez imediata"
  }
]
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto abaixo, as baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizando assim o consumo de tokens. Entretanto, vale lembrar que mais importante do que economizar tokens, é ter todas as informações relevantes disponíveis em seu contexto.

```
Dados do Cliente:
- Nome: Ivan Ivanovich
- Perfil: Moderado
- Saldo disponível: R$ 7.000

Últimas transações:
- 01/01: Uber - R$ 50
- 03/01: Mercado - R$ 55
- 04/01: Sapaton Novo - R$ 100
- 04/01: Cinema - R$ 30
- 05/01: Fone de Ouvido - R$ 20
...
```
