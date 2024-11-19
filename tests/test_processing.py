import pytest

from src.processing import filter_by_state, sort_by_date

# Пример данных для тестов
data = [
    {"date": "2024-01-01T12:00:00.000000", "state": "EXECUTED", "amount": 100},
    {"date": "2024-01-05T12:00:00.000000", "state": "CANCELLED", "amount": 200},
    {"date": "2024-01-03T12:00:00.000000", "state": "EXECUTED", "amount": 300},
    {"date": "2024-01-02T12:00:00.000000", "state": "EXECUTED", "amount": 400},
]


@pytest.fixture
def test_data():
    return data


@pytest.mark.parametrize("state, expected_length", [("EXECUTED", 3), ("CANCELLED", 1)])
def test_filter_by_state(test_data, state, expected_length):
    # Тестирование фильтрации по состоянию
    filtered_transactions = filter_by_state(test_data, state)
    assert len(filtered_transactions) == expected_length
    assert all(item["state"] == state for item in filtered_transactions)


@pytest.mark.parametrize(
    "reverse_order, expected_dates",
    [
        (
            True,
            [
                "2024-01-05T12:00:00.000000",
                "2024-01-03T12:00:00.000000",
                "2024-01-02T12:00:00.000000",
                "2024-01-01T12:00:00.000000",
            ],
        ),
        (
            False,
            [
                "2024-01-01T12:00:00.000000",
                "2024-01-02T12:00:00.000000",
                "2024-01-03T12:00:00.000000",
                "2024-01-05T12:00:00.000000",
            ],
        ),
    ],
)
def test_sort_by_date(test_data, reverse_order, expected_dates):
    # Тестирование сортировки по дате
    sorted_data = sort_by_date(test_data, reverse_order)
    sorted_dates = [item["date"] for item in sorted_data]
    assert sorted_dates == expected_dates


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
