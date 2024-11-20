import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_test_data():
    return [
        (7000792289606361, "700079******6361"),
        (1234567890123456, "123456******3456"),
        (123456, ValueError, "Номер карты должен содержать 16 цифр."),
        (12345678901234567, ValueError, "Номер карты должен содержать 16 цифр."),
        ("abcdefabcdefghijklmno", ValueError, "Номер карты должен содержать 16 цифр."),
    ]


@pytest.fixture
def account_test_data():
    return [
        (73654108430135874305, "**4305"),
        (12345678901234567890, "**7890"),
        (1234567890123456, ValueError, "Номер счета должен содержать 20 цифр."),
        (1234567890123456789012345, ValueError, "Номер счета должен содержать 20 цифр."),
        ("abcdefabcdefabcdefghij", ValueError, "Номер счета должен содержать 20 цифр."),
    ]


@pytest.mark.parametrize(
    "card_number,expected",
    [
        (7000792289606361, "700079******6361"),
        (1234567890123456, "123456******3456"),
    ],
)
def test_get_mask_card_number_success(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number,expected_exception,expected_message",
    [
        (123456, ValueError, "Номер карты должен содержать 16 цифр."),
        (12345678901234567, ValueError, "Номер карты должен содержать 16 цифр."),
        ("abcdefabcdefghijklmno", ValueError, "Номер карты должен содержать 16 цифр."),
    ],
)
def test_get_mask_card_number_failure(card_number, expected_exception, expected_message):
    with pytest.raises(expected_exception, match=expected_message):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number,expected",
    [
        (73654108430135874305, "**4305"),
        (12345678901234567890, "**7890"),
    ],
)
def test_get_mask_account_success(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize(
    "account_number,expected_exception,expected_message",
    [
        (1234567890123456, ValueError, "Номер счета должен содержать 20 цифр."),
        (1234567890123456789012345, ValueError, "Номер счета должен содержать 20 цифр."),
        ("abcdefabcdefabcdefghij", ValueError, "Номер счета должен содержать 20 цифр."),
    ],
)
def test_get_mask_account_failure(account_number, expected_exception, expected_message):
    with pytest.raises(expected_exception, match=expected_message):
        get_mask_account(account_number)
