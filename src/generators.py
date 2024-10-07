from typing import Dict, Generator, List


def filter_by_currency(transactions_list: List[Dict], currency: str = "USD") -> Generator:
    """
    Генератор транзакции для получения отсортированного по валюте списка .
    :param transactions_list: Список словарей с транзакциями.
    :param currency: Ключ для фильтра, по умолчанию значение "USD"
    """
    for transaction in transactions_list:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions_list: List[Dict]) -> Generator:
    """
    Генератор возвращающий вид транзакций из списка словарей.
    :param transactions_list: Список словарей с транзакциями.
    """
    for transaction in transactions_list:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор для создания номера карты в формате ХХХХ ХХХХ ХХХХ ХХХХ.
    :param start: Начальное число диапозона номеров.
    :param end: Конечное число диапозона номеров.
    """
    for number in range(start, end + 1):
        format_numbers = f"{number:016d}"
        yield f"{format_numbers[:4]} {format_numbers[4:8]} {format_numbers[8:12]} {format_numbers[12:]}"
