from datetime import datetime


def filter_by_state(dict_banking_operations: list, state: str = "EXECUTED") -> list:
    """
    Функция получет список словарей с данными и возвращает новый отсартированный список,
    Функция имеет значение для сортировки по умолчанию
    """
    return [
        dict_banking_operations
        for dict_banking_operations in dict_banking_operations
        if dict_banking_operations.get("state") == state
    ]


def sort_by_date(dict_banking_operations: list, sort_param: bool = True) -> list:
    """Функция получает список словарей с данными и возвращает новый список с данными выстроенными по дате"""
    return sorted(dict_banking_operations, key=lambda x: datetime.fromisoformat(x["date"]), reverse=sort_param)
