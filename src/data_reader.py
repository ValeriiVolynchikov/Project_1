import logging
import os
import re
from typing import Dict, List

import pandas as pd

# Создание папки logs, если она не существует
if not os.path.exists("logs"):
    os.makedirs("logs")

# Настройка логирования
log_file_path = "../logs/transactions.log"
logging.basicConfig(filename=log_file_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
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
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден.")
        raise FileNotFoundError(f"Файл {file_path} не найден.")
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
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден.")
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считано {len(transactions)} транзакций из файла: {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        raise


def filter_transactions(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Фильтрует список транзакций по строке поиска в описании.

    Args:
        transactions (List[Dict]): Список транзакций.
        search_string (str): Строка для поиска в описании.

    Returns:
        List[Dict]: Список транзакций, соответствующих строке поиска.
    """
    logger.info(f"Попытка фильтрации транзакций по строке: {search_string}")
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    filtered_transactions = [
        transaction for transaction in transactions if pattern.search(transaction.get("description", ""))
    ]
    logger.info(f"Найдено {len(filtered_transactions)} транзакций, соответствующих строке: {search_string}")
    return filtered_transactions


def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций по категориям.

    Args:
        transactions (List[Dict]): Список транзакций.
        categories (List[str]): Список категорий.

    Returns:
        Dict[str, int]: Словарь с количеством транзакций для каждой категории.
    """
    logger.info("Подсчет транзакций по категориям.")
    category_count = {category: 0 for category in categories}
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1
    logger.info(f"Подсчет завершен. Результаты: {category_count}")
    return category_count
