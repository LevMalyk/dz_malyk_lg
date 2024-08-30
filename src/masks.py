from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Функция получает от пользователя данные,
    проверяет их на соответствие формы номера карты и возвращает
    замаскированый номер карты
    :param card_number: получает от пользователя предпологаемый номер карты
    :return: Возвращает замаскированый номер карты
    """
    card_number = str(card_number).replace(" ", "")
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return "Введен некоректный номер карты"


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Функция получает от пользователя данные,
    проверяет их на соответствие формы номера счета и возвращает
    замаскированый номер счета
    :param account_number: получает от пользователя предпологаемый номер счета
    :return: Возвращает замаскированый номер счета
    """
    account_number = str(account_number).replace(" ", "")
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Введен некоректный номер счета"
