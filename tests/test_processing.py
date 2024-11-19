import pytest

from src.processing import filter_by_state, sort_by_date

# Пример данных для тестов
data = [
    {"date": "2024-01-01T12:00:00.000000", "state": "EXECUTED", "amount": 100},
    {"date": "2024-01-05T12:00:00.000000", "state": "CANCELLED", "amount": 200},
    {"date": "2024-01-03T12:00:00.000000", "state": "EXECUTED", "amount": 300},
    {"date": "2024-01-02T12:00:00.000000", "state": "EXECUTED", "amount": 400},
]


def test_filter_by_state() -> None:
    # Тестирование фильтрации по состоянию
    executed_transactions = filter_by_state(data, "EXECUTED")
    assert len(executed_transactions) == 3
    assert all(item["state"] == "EXECUTED" for item in executed_transactions)

    cancelled_transactions = filter_by_state(data, "CANCELLED")
    assert len(cancelled_transactions) == 1
    assert cancelled_transactions[0]["state"] == "CANCELLED"


def test_sort_by_date() -> None:
    # Тестирование сортировки по дате
    sorted_data = sort_by_date(data)
    assert sorted_data[0]["date"] == "2024-01-05T12:00:00.000000"  # Последняя по дате
    assert sorted_data[3]["date"] == "2024-01-01T12:00:00.000000"  # Первая по дате

    # Проверка сортировки в обратном порядке
    sorted_data_desc = sort_by_date(data, reverse_order=False)
    assert sorted_data_desc[0]["date"] == "2024-01-01T12:00:00.000000"  # Первая по дате
    assert sorted_data_desc[3]["date"] == "2024-01-05T12:00:00.000000"  # Последняя по дате


# Запуск тестов
if __name__ == "__main__":
    pytest.main()
