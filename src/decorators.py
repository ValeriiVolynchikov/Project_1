import logging
import os
from datetime import datetime


# Настройка логирования
def setup_logger(filename=None):
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(message)s")

    if filename is not None:
        log_file = os.path.join("logs", filename)
        os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Создание папки, если не существует
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def log(filename=None):
    logger = setup_logger(filename)

    def decorator(func):
        def wrapper(*args, **kwargs):
            function_name = func.__name__
            start_time = datetime.now()
            logger.info(f"{function_name} called at {start_time.isoformat()} with args: {args} and kwargs: {kwargs}")

            try:
                result = func(*args, **kwargs)
                logger.info(f"{function_name} result: {result}")
                return result
            except Exception as e:
                error_message = f"{function_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                logger.error(error_message)
                raise

        return wrapper

    return decorator
