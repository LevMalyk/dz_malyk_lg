from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: Union[str, int]) -> str:
    """
    Функция получает данные от пользователя и маскирует их.
    :param user_data: Данные полученные от пользователя
    :return: Результат маскировки данных или сообщение об ошибке
    """
    user_data = str(user_data)
    if user_data[-20:].isdigit() and not user_data[-21:].isdigit():
        return f"{user_data[:-20]}{get_mask_account(user_data[-20:])}"
    elif user_data[-16:].isdigit() and not user_data[-17:].isdigit():
        return f"{user_data[:-16]}{get_mask_card_number(user_data[-16:])}"
    else:
        return "Введены неправельные данные"
