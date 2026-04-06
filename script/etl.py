import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def extract(file_path):
    "Função para extrair csv e retornar um DataFrame"
    try:
        df_bruto = pd.read_csv(file_path, low_memory=False)
        return df_bruto
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")

def transform(df_bruto):
    try:
        df = df_bruto.copy()

        df = df.drop(columns=["Data_Base",])
        df = df.drop_duplicates(subset=["ID_Pedido"])
        df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
        df["Loja"] = df["Loja"].fillna("Online").str.title()
        df["Loja"] = df["Loja"].str.strip()
        df["Produto"] = df["Produto"].str.replace('"', "")
        return df
    except Exception as e:
        print(f"Erro ao realizar tratamento dos dados: {e}")

def load(df):
    # Configurações de conexão com o banco de dados
    connection = os.getenv("DB_CONNECTION_STRING")
    engine = create_engine(connection)
    try:
        df.to_sql(
            "Vendas",
            con = engine,
            if_exists="replace",
            index=False
        )
    except Exception as e:
        print(f"Erro ao carregar dados no banco de dados: {e}")

def main():
    file_path = "../data/vendas_tech.csv"

    df_bruto = extract(file_path)
    df = transform(df_bruto)
    load(df)

if __name__ == "__main__":
    main()