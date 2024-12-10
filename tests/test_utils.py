import unittest
from unittest.mock import mock_open, patch

from external_api import convert_to_rub
from utils import load_transactions


class TestUtils(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_transactions_empty_file(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    def test_load_transactions_valid_file(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(len(result), 1)  # Проверяем, что загружен один элемент
        self.assertEqual(result[0]["amount"], 100)  # Проверяем, что сумма равна 100

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    def test_load_transactions_invalid_json(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список при некорректном JSON

    @patch("os.path.isfile", return_value=False)
    def test_load_transactions_file_not_exist(self, mock_isfile):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список если файл не существует

    @patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100, "currency": "USD"}')
    def test_load_transactions_not_a_list(self, mock_file):
        result = load_transactions("data/operations.json")
        self.assertEqual(result, [])  # Проверяем, что результат пустой список если данные не список

    @patch("requests.get")
    def test_convert_to_rub(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 7500}  # Симулируем ответ API

        transaction = {"amount": 100, "currency": "USD"}  # Тестовая транзакция
        result = convert_to_rub(transaction)
        self.assertEqual(result, 7500.0)  # Проверяем, что результат конвертации равен 7500


if __name__ == "__main__":
    unittest.main()  # Запуск тестов
