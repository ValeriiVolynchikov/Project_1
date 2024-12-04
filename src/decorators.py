import functools
import logging


def log(filename=None):
    """Декоратор, который логирует начало и конец выполнения функции,
    ее результаты, а также возникающие ошибки.

    Аргументы:
    filename -- Имя файла для записи логов (если не указано, логи выводятся в консоль).
    """

    # Установка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Обертка для логирования вызовов функции."""
            try:
                logging.info(f"Starting {func.__name__}: Inputs: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok: Result: {result}")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise  # повторно выбрасываем исключение

        return wrapper

    return decorator
