import sys
from pathlib import Path
import pytest

# Добавляем папку src в sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'src'))

from masks import get_mask_card_number, get_mask_account  # Импортируйте функции


# Тесты для get_mask_card_number
def test_get_mask_card_number_valid():
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"


def test_get_mask_card_number_invalid_length():
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(123456789)  # Длина номера меньше 16


def test_get_mask_card_number_invalid_characters():
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("1234 5678 1234 5678")  # Неправильный формат ввода


def test_get_mask_card_number_non_numeric():
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("abcdefghij123456")  # Неправильные символы в номере


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("")  # Пустая строка


# Тесты для get_mask_account
def test_get_mask_account_valid():
    assert get_mask_account(12345678901234567890) == "**7890"


def test_get_mask_account_invalid_length():
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account(123456789012)  # Длина номера меньше 20


def test_get_mask_account_invalid_characters():
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account("1234 5678 9012 3456 7890")  # Неправильный формат ввода


def test_get_mask_account_non_numeric():
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account("abcdefghij1234567890")  # Неправильные символы в номере


def test_get_mask_account_empty():
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account("")  # Пустая строка
