import pytest

from masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    # Базовый тест с корректным номером карты
    assert get_mask_card_number(7000792289606361) == "700079******6361"
    # Тест с другим корректным номером карты
    assert get_mask_card_number(1234567890123456) == "123456******3456"

    # Тест с некорректным номером (менее 16 цифр)
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(123456)

    # Тест с некорректным номером (более 16 цифр)
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number(12345678901234567)

    # Тест с некорректным номером (не числовой)
    with pytest.raises(ValueError, match="Номер карты должен содержать 16 цифр."):
        get_mask_card_number("abcdefabcdefghijklmno")


def test_get_mask_account() -> None:
    # Базовый тест с корректным номером счета
    assert get_mask_account(73654108430135874305) == "**4305"
    # Тест с другим корректным номером счета
    assert get_mask_account(12345678901234567890) == "**7890"

    # Тест с некорректным номером (менее 20 цифр)
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account(1234567890123456)

    # Тест с некорректным номером (более 20 цифр)
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account(1234567890123456789012345)

    # Тест с некорректным номером (не числовой)
    with pytest.raises(ValueError, match="Номер счета должен содержать 20 цифр."):
        get_mask_account("abcdefabcdefabcdefghij")
