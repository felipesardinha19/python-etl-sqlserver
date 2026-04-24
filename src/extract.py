import pandas as pd
from src.utils.logger import get_logger

logger = get_logger("extract")

def extract(file_path):
    "Função para extrair csv e retornar um DataFrame"
    try:
        logger.info("Extraindo dados do arquivo csv.")
        
        df_bruto = pd.read_csv(file_path, low_memory=False)
        
        logger.info("Dados extraidos com sucesso!")
        
        return df_bruto
        
    except Exception as e:
        logger.exception(f"Erro ao extrair dados: {e}")