import logging
from typing import Dict, List

import pandas as pd

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV файла.

    Args:
        file_path (str): Путь к файлу CSV.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    logger.info(f"Попытка прочитать данные из CSV файла: {file_path}")
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считано {len(transactions)} транзакций из файла: {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel файла.

    Args:
        file_path (str): Путь к файлу Excel.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    logger.info(f"Попытка прочитать данные из Excel файла: {file_path}")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считано {len(transactions)} транзакций из файла: {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise
