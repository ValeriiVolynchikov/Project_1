# tests/test_widget.py

import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card():
    # Примеры тестов для функции mask_account_card
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 700079******6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("MasterCard 5185373029202738") == "MasterCard 518537******2738"
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"
    assert mask_account_card("Invalid Card 1234") == "Ошибка: Неверный формат номера счета или карты"


def test_get_date():
    # Примеры тестов для функции get_date
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-25T15:45:30.123456") == "25.12.2023"
    assert get_date("invalid date") == ""  # Проверяем возврат пустой строки на неверном формате
