import pandas as pd
import numpy as np
from src.utils.logger import get_logger
from datetime import datetime
from pathlib import Path

logger = get_logger("transform")

def clean_data(df):
    try:
        if df is None:
            return None
        
        SILVER_PATH = Path("data/silver")
        
        df = df.drop(columns=["Data_Base"])
        df = df.drop_duplicates(subset=["ID_Pedido"])

        df["Data"] = pd.to_datetime(df["Data"], errors="coerce")

        df["Loja"] = df["Loja"].fillna("Online").str.strip().str.title()

        df["Produto"] = df["Produto"].str.replace('"', "", regex=False)
        
        SILVER_PATH.mkdir(parents=True, exist_ok=True)

        output_file = SILVER_PATH / f"data_clean_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"

        df.to_parquet(output_file, index=False)
        logger.info(f"Limpeza concluida e dados salvos em {output_file}, no formato parquet")

        return df

    except Exception as e:
        logger.exception(f"Erro ao realizar limpeza dos dados: {e}")
        return None

def create_metrics(df):
    try:
        GOLD_PATH = Path("data/gold")
        logger.info("Criando métricas para análise")

        df["Faturamento"] = df['Qtd'] * df['Preco_Unitario']
        df['Ano'] = df['Data'].dt.year
        df['Mes'] = df['Data'].dt.month

        GOLD_PATH.mkdir(parents=True, exist_ok=True)

        output_file = GOLD_PATH / f"data_clean_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"

        df.to_parquet(output_file, index=False)
        logger.info(f"Métricaspara análise criadas com sucesso e salvas em {output_file}")

        return df
    
    except Exception as e:
        logger.exception(f"Erro ao construir métricas: {e}")
        return None

def transform(df_bruto):
    try:
        logger.info("Iniciando transformação e criação de métricas.")

        df = df_bruto.copy()

        df = clean_data(df)
        if df is None:
            return None
        df = create_metrics(df)
        if df is None:
            return None

        return df
        
    except Exception as e:
        logger.exception(f"Erro ao realizar tratamento dos dados: {e}")