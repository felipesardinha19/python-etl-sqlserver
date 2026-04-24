from src.extract import extract
from src.transform import transform
from src.load import load
from src.utils.logger import get_logger

logger = get_logger('pipeline')

def main():
    try:
        logger.info("Iniciando pipeline de dados")

        file_path = "data/raw/vendas_tech.csv"

        #Extract
        df = extract(file_path)
        if df is None:
            logger.error("Erro na extração")
            return None
        
        #transform
        df = transform(df)
        if df is None:
            logger.error("Erro na transformação")
            return None

        #load
        load(df)
        logger.info("Pipeline executado com sucesso!")

    except Exception as e:
        logger.exception(f"Erro na execução do pipeline: {e}")

if __name__ == "__main__":
    main()