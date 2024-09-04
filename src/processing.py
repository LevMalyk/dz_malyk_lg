from datetime import datetime
from typing import Dict, List


def filter_by_state(banking_operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует банковские операции по состаянию.
    :param banking_operations: Список словарей с банковскими операциями.
    :param state: Состояние, по которому необходимо призвести фильтрацию (по умолчанию "EXECUTED").
    :return: Список словарей, отфильтрованных по состаянию.
    """
    return [operations for operations in banking_operations if operations.get("state") == state]


def sort_by_date(banking_operations: List[Dict], sort_param: bool = True) -> List[Dict]:
    """
    Сортирует банковские операции по дате.
    :param banking_operations: Список словарей с банковскими операциями.
    :param sort_param: Порядок, по которому необходимо призвести сортировку (по умолчанию True).
    :return: Отсартированный список словарей по дате.
    """
    return sorted(banking_operations, key=lambda x: datetime.fromisoformat(x["date"]), reverse=sort_param)
