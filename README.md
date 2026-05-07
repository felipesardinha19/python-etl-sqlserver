# 🛒 Pipeline ETL End-to-End com Dashboard

Pipeline ETL desenvolvido em Python para extração, transformação e carga de dados de vendas de e-commerce em um banco de dados SQL Server e com um Dashboard e Insights no Power BI.

---

## 📋 Descrição

Script que realiza o processo completo de ETL a partir de um dataset fictício de vendas em formato CSV, aplicando tratamentos e padronizações nos dados antes de carregá-los em um banco relacional e posteriormente gerar insights com dashboard no Power BI.

---

## 🏗️ Arquitetura

```
   RAW/CSV 
      ↓
   Extract        → leitura do arquivo CSV com Pandas
      ↓
  Transform       → Etapa de limpeza e criação de métricas
      ↓
   Limpeza        → limpeza e padronização dos dados
      ↓
    Silver        → Salva na pasta/camada Silver
      ↓
   Metrics        → Cria métricas para analise
      ↓
     Gold         → Salva na pasta/camada Gold
      ↓
     Load          → carga no SQL Server via SQLAlchemy
      ↓
 SQL Server       → tabela Vendas
      ↓
   Power BI       → Dashboards & Insights
```

---

## 🔧 Transformações aplicadas

- Remoção de colunas desnecessárias
- Remoção de duplicatas com base no `ID_Pedido`
- Conversão e padronização da coluna `Data`
- Preenchimento de valores nulos na coluna `Loja` com `"Online"`
- Padronização dos nomes das lojas (capitalização e remoção de espaços)
- Remoção de aspas desnecessárias na coluna `Produto`

---

## 📊 Dashboard (Power BI)

Os dados processados pelo pipeline são consumidos no Power BI para criação de dashboards analíticos.

KPIs desenvolvidos:

 - Faturamento total
 - Total de pedidos
 - Ticket médio

Visualizações:
 - Faturamento por mês
 - Faturamento por loja
 - Faturamento por produto

![Dashboard Power BI](docs/image/dashboard_powerbi.png)

### 📈 Insights gerados
 - A loja de Salvador apresentou o maior volume de vendas, enquanto a loja Online teve o menor desempenho no período analisado
 - O produto mais vendido foi o iPhone 14, enquanto o cabo HDMI apresentou menor demanda
 - O faturamento total do período foi de aproximadamente R$ 299,4 mi
 - Foram registrados cerca de 100 mil pedidos, com ticket médio de aproximadamente R$ 2,99 mil
 - Outubro foi o mês com maior volume de vendas, enquanto fevereiro apresentou o menor desempenho

---

## 🗂️ Estrutura do projeto

```
Data_Pipeline_Vendas/
│
├── data/
│   └── raw/
│       └── vendas_tech.csv
│   └── silver/
│       └── data_clean.parquet
│   └── gold/
│       └── metrrics.parquet
│
├── docs/
│   └── image/
│       └── dashboard_powerbi.png
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── utils/
│   │   └── logger.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── .env
├── .env.example
├── .gitignore
└── README.md
```
---

## ⚙️ Como executar

# 1. Clonar o repositório
```
git clone <https://github.com/felipesardinha19/python-etl-sqlserver>
```

# 2. Instalar dependências
```
pip install pandas sqlalchemy pyodbc python-dotenv
```

# 3. Configurar variáveis de ambiente
```
cp .env.example .env
```

# 4. Executar pipeline
```
python -m src.pipeline
```

---

## 🛠️ Tecnologias utilizadas

- Python 3.12
- Pandas
- SQLAlchemy
- SQL Server Express
- Power BI
- python-dotenv
