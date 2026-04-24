import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from src.utils.logger import get_logger

logger = get_logger('load')

load_dotenv()

def load(df):
    # Configurações de conexão com o banco de dados
    logger.info("Iniciando conexão com o banco")

    connection = os.getenv("DB_CONNECTION_STRING")
    engine = create_engine(connection)
    
    logger.info("Conexão feita com sucesso.")
    try:
        df.to_sql(
            "Vendas",
            con = engine,
            if_exists="replace",
            index=False
        )
        logger.info("Dados carregados no banco com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados no banco de dados: {e}")