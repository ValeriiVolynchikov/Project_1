import os

import pytest

from decorators import log


# Пример функции для тестирования
@log(filename="test_log.txt")
def add(x, y):
    """Функция сложения."""
    return x + y


@log()
def divide(x, y):
    """Функция деления."""
    return x / y


# Тестируем успешное выполнение функции
def test_add(capsys):
    result = add(1, 2)
    assert result == 3

    # Проверяем вывод в файл
    with open("test_log.txt", "r") as f:
        logs = f.readlines()
    assert any("add ok" in line for line in logs)


# Тестируем обработку исключений
def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    # Проверяем, что ошибка записана в логи
    with open("test_log.txt", "r") as f:
        logs = f.readlines()
    assert any("divide error: ZeroDivisionError" in line for line in logs)


# Удаляем тестовый лог-файл после тестов
@pytest.fixture(autouse=True)
def cleanup():
    yield
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
