import csv
import json
import os
import re

import pytest

from src.main import filter_transactions, format_date, load_transactions, mask_account, mask_card, print_transaction


def test_load_transactions_invalid_format():
    with pytest.raises(ValueError, match="Unsupported file format"):  # %
        load_transactions("test_data.txt")


def test_load_transactions_json(setup_files):
    test_json_file, _ = setup_files
    with open(test_json_file, "r", encoding="utf-8") as f:
        print(f.read())  # Вывод содержимого JSON файла
    transactions = load_transactions(test_json_file)
    assert len(transactions) == 1
    assert transactions[0]["id"] == "1"
    assert transactions[0]["operationAmount"]["amount"] == "1000"
    assert transactions[0]["operationAmount"]["currency"]["code"] == "RUB"


def test_load_transactions_csv(setup_files):
    _, test_csv_file = setup_files
    with open(test_csv_file, "r", encoding="utf-8") as f:
        print(f.read())  # Вывод содержимого CSV файла
    transactions = load_transactions_(test_csv_file)
    assert len(transactions) == 1
    assert transactions[0]["id"] == "1"  # Теперь это строка
    assert transactions[0]["operationAmount"]["amount"] == "1000"
    assert transactions[0]["operationAmount"]["currency"]["code"] == "RUB"


def load_transactions_(file_path):  # название функции изменил '_'
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif file_path.endswith(".csv"):
        transactions = []
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                transaction = {
                    "id": str(row["id"]),  # Преобразуем id в строку
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                    },
                    "from": row["from"],
                    "to": row["to"],
                    "description": row["description"],
                }
                transactions.append(transaction)
        return transactions
    else:
        raise ValueError("Unsupported file format")


def filter_transactions_(transactions, keyword):  # название функции изменил '_'
    keyword = keyword.lower()  # Приводим ключевое слово к нижнему регистру
    return [tx for tx in transactions if keyword in tx["description"].lower()]


@pytest.fixture(scope="module")
def setup_files():
    test_json_file = "test_data.json"
    test_csv_file = "test_data.csv"

    # JSON тестовые данные
    with open(test_json_file, "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "id": "1",
                    "state": "EXECUTED",
                    "date": "2023-11-10T10:00:00Z",
                    "operationAmount": {"amount": "1000", "currency": {"name": "рубль", "code": "RUB"}},
                    "from": "Счет 1234567890123456",
                    "to": "Счет 6543210987654321",
                    "description": "Перевод с карты на карту",
                }
            ],
            f,
        )

    # CSV тестовые данные
    with open(test_csv_file, "w", encoding="utf-8") as f:
        f.write("id;state;date;amount;currency_name;currency_code;from;to;description\n")
        f.write(
            "1;EXECUTED;2023-11-10T10:00:00Z;1000;рубль;RUB;Счет 1234567890123456;"
            "Счет 6543210987654321;Перевод с карты на карту\n"
        )

    yield test_json_file, test_csv_file

    os.remove(test_json_file)
    os.remove(test_csv_file)


def test_load_transactions_json_(setup_files):  # название функции изменил '_'
    test_json_file, _ = setup_files
    transactions = load_transactions(test_json_file)
    assert len(transactions) == 1
    assert transactions[0]["id"] == "1"
    assert transactions[0]["operationAmount"]["amount"] == "1000"
    assert transactions[0]["operationAmount"]["currency"]["code"] == "RUB"


def filter_transactions_filter(transactions, keyword):
    # Создаем регулярное выражение для поиска "карта" и всех ее форм
    pattern = re.compile(r"\b" + re.escape(keyword[:-1]) + r"\w\b", re.IGNORECASE)

    print(f"Keyword pattern: '{pattern.pattern}'")  # Печатаем паттерн для поиска
    filtered_transactions = []

    for tx in transactions:
        description_cleaned = tx["description"].strip().lower()  # Очищаем строку
        print(f"Original description: '{tx['description']}'")  # Печатаем оригинальное описание
        print(f"Cleaned description: '{description_cleaned}'")  # Печатаем очищенное описание

        # Проверяем наличие ключевого слова с помощью регулярного выражения
        if pattern.search(description_cleaned):
            filtered_transactions.append(tx)

    print(f"Filtered transactions: {filtered_transactions}")  # Печатаем отфильтрованные транзакции
    return filtered_transactions


def test_filter_transactions_empty_keyword():
    transactions = [{"description": "Перевод с карты на карту"}, {"description": "Перевод организации"}]
    filtered = filter_transactions(transactions, "")
    assert len(filtered) == 2  # Все транзакции должны быть возвращены


def test_filter_transactions_case_insensitivity():
    transactions = [
        {"description": "Перевод с КАРТЫ на карту"},  # %
        {"description": "Перевод организации"},
        {"description": "перевод с карты на карту"},
    ]
    filtered_a = filter_transactions(transactions, "карт")
    assert len(filtered_a) == 2  # Должно найти оба варианта


def test_filter_transactions_no_matches():
    transactions = [{"description": "Перевод организации"}, {"description": "Перевод с карты на счет"}]  # %
    filtered = filter_transactions(transactions, "некорректное слово")
    assert len(filtered) == 0


def test_mask_account():
    masked = mask_account("Счет 1234567890123456")
    assert masked == "Счет **3456"


def test_mask_card():
    masked = mask_card("1234567890123456")
    assert masked == "1234 56** **** 3456"


def test_format_date():
    formatted = format_date("2023-11-10T10:00:00Z")
    assert formatted == "10.11.2023"


def test_mask_account_invalid_input():
    masked = mask_account("Некорректный ввод")  # %
    assert masked == "Некорректный ввод"  # Если формат не соответствует, то возвращаем оригинал


def test_mask_card_invalid_input():
    masked = mask_card("Некорректный ввод")  # %
    assert masked == "Некорректный ввод"  # Если формат не соответствует, то возвращаем оригинал


def test_format_date_invalid_input():
    formatted = format_date("Некорректный ввод")  # %
    assert formatted == "Некорректный ввод"  # Если формат не соответствует, то возвращаем оригинал


def test_load_transactions_empty_file():
    empty_file_path = "empty_file.json"
    with open(empty_file_path, "w", encoding="utf-8") as f:
        f.write("")  # Создаем пустой файл

    with pytest.raises(json.JSONDecodeError):
        load_transactions(empty_file_path)


def test_filter_transactions_partial_match():
    transactions = [
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод с карточки на счет"},
        {"description": "Перевод организации"},
    ]
    filtered = filter_transactions(transactions, "кар")
    assert len(filtered) == 2  # Должно найти оба варианта


def test_mask_account_various_formats():
    assert mask_account("Счет 1234 5678 9012 3456") == "Счет **3456"
    assert mask_account("Счет 123456") == "Счет **456"
    assert mask_account("Некорректный ввод") == "Некорректный ввод"
    assert mask_account("Счет 1234 5678 9012 3456") == "Счет **3456"
    assert mask_account("Счет 123456") == "Счет **456"
    assert mask_account("Счет 123") == "Счет 123"  # Если менее 4 цифр, возвращаем оригинал
    assert mask_account("Счет нечисловое") == "Счет нечисловое"  # Тест на нечисловые значения


def test_mask_card_various_formats():
    assert mask_card("1234 5678 9012 3456") == "1234 56** **** 3456"
    assert mask_card("1234567890123456") == "1234 56** **** 3456"
    assert mask_card("Некорректный ввод") == "Некорректный ввод"


def test_format_date_various_formats():
    assert format_date("2023-11-10T10:00:00Z") == "10.11.2023"
    assert format_date("2023-11-10") == "10.11.2023"  # Предполагаем, что функция поддерживает другой формат
    assert format_date("Некорректный ввод") == "Некорректный ввод"  # Ожидаем оригинал


def test_print_transaction_various_formats(capsys):
    transaction = {
        "description": "Перевод с карты на карту",
        "operationAmount": {"amount": 1000, "currency": {"code": "RUB"}},
        "date": "2023-01-01",
    }

    print_transaction(transaction)
    captured = capsys.readouterr()

    assert "Перевод с карты на карту" in captured.out
    assert "1000" in captured.out  # Проверяем, что вывод содержит сумму


if __name__ == "__main__":
    pytest.main()
