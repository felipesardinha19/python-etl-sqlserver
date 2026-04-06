# 🛒 ecommerce-etl-pipeline

Pipeline ETL desenvolvido em Python para extração, transformação e carga de dados de vendas de e-commerce em um banco de dados SQL Server.

---

## 📋 Descrição

Script que realiza o processo completo de ETL a partir de um dataset fictício de vendas em formato CSV, aplicando tratamentos e padronizações nos dados antes de carregá-los em um banco relacional.

---

## 🏗️ Arquitetura

```
CSV (dados brutos)
      ↓
   Extract        → leitura do arquivo CSV com Pandas
      ↓
  Transform       → limpeza e padronização dos dados
      ↓
    Load          → carga no SQL Server via SQLAlchemy
      ↓
 SQL Server       → tabela Vendas
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

## 🗂️ Estrutura do projeto

```
ecommerce-etl-pipeline/
│
├── data/
│   └── vendas_tech.csv       # Dataset fictício de vendas
│
├── script/
│   └── etl.py                # Script principal do pipeline
│
├── .env.example              # Exemplo de configuração das variáveis de ambiente
├── .gitignore
└── README.md
```

---

## ⚙️ Como executar

### 1. Clone o repositório
```bash
git clone
cd ecommerce-etl-pipeline
```

### 2. Instale as dependências
```bash
pip install pandas sqlalchemy pyodbc python-dotenv
```

### 3. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:
```
DB_CONNECTION_STRING=mssql+pyodbc://@SEU_SERVIDOR/SEU_BANCO?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes
```

### 4. Execute o script
```bash
cd script
python etl.py
```

---

## 🛠️ Tecnologias utilizadas

- Python 3.12
- Pandas
- SQLAlchemy
- SQL Server Express
- python-dotenv