import pytest

from src.processing import filter_by_state, sort_by_date

# Функция
# sort_by_date
# Тесты на работу функции с некорректными или нестандартными форматами дат.


@pytest.mark.parametrize(
    "state, result",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-02T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-02T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-02T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-02T08:21:33.419441"},
            ],
        ),
        (" ", []),
        ("TESTING", []),
    ],
)
def test_filter_by_state(operation_test_list: list[dict], result: list[dict], state: str) -> None:
    """
    Проверяется что функция фозвращает банковские операции по состаянию.
    :param operation_test_list: Список словарей с банковскими операциями.
    :param result: Ожидаемый список словарей с результатами.
    :param state: Состояние, по которому необходимо призвести фильтрацию
    """
    assert filter_by_state(operation_test_list, state) == result


@pytest.mark.parametrize(
    "sort_param, result_sort",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-02T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-02T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-02T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-02T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-02T02:08:58.425572"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-02T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-02T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-02T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(operation_test_list: list[dict], sort_param: bool, result_sort: list[dict]) -> None:
    """
    Проверяет что функция сортерует списое по дате а также если дата операций одинаковая.
    :param operation_test_list: Список словарей с банковскими операциями
    :param sort_param: Определяет порядок сортировки.
    :param result_sort: Ожидаемый список словарей с результатами.
    """
    assert sort_by_date(operation_test_list, sort_param) == result_sort


@pytest.mark.parametrize(
    "sort_param, result_sort",
    [
        (True, "Не верно указана дата"),
        (False, "Не верно указана дата"),
    ],
)
def test_wrong_date_sort_by_date(
    operation_test_list_wrong_date: list[dict], sort_param: bool, result_sort: str
) -> None:
    """
    Проверяет что функция выводит сообщение если в списке словарей есть нестандартная или неправильная дата
    :param operation_test_list_wrong_date: Список словарей с банковскими операциями
    :param sort_param: Определяет порядок сортировки.
    :param result_sort: Ожидается сообщение о неверно указанной дате.
    """
    assert sort_by_date(operation_test_list_wrong_date, sort_param) == result_sort
