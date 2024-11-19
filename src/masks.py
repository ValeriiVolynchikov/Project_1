def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты и возвращает его маску
    в формате XXXX XX** **** XXXX, где X - это цифры
    """

    # Преобразуем номер карты в строку
    card_number_str = str(card_number)

    # Проверка, что номер карты составляет 16 цифр.
    if len(card_number_str) != 16 or not card_number_str.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Создание маски карты, видны первые 6 и последние 4 цифры
    mask_card = f"{card_number_str[:6]}******{card_number_str[-4:]}"

    return mask_card


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску в формате **XXXX,
    где X - это цифры
    """
    # Преобразуем номер счета в строку
    account_number_str = str(account_number)

    # Проверяем, что номер счета состоит как минимум из 4 цифр
    if len(account_number_str) != 20 or not account_number_str.isdigit():
        raise ValueError("Номер счета должен содержать 20 цифр.")

    # Создаем маску, видны последние 4 цифры
    mask_account = f"**{account_number_str[-4:]}"

    return mask_account
