import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_date, result_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("21-11-2023T02:26:18.671407", "21.11.2023"),
        ("11-22-2012T02:26:18.671407", "22.11.2012"),
        (" ", "Нет даты")
    ],
)
def test_get_date(user_date: str, result_date: str) -> None:
    """
    Проверяет что функция get_date получает данные содержащие дату и возвращает в формате ("%d.%m.%Y")
    :param user_date: Получает данные содержащие дату.
    :param result_date: Получает ожидаемый резульлтат работы функции.
    """
    assert get_date(user_date) == result_date


@pytest.mark.parametrize("index", [i for i in range(8)])
def test_mask_account_card(user_data_list: list[str], result_user_data_list: list[str], index: int) -> None:
    """
    Проверяет что функция mask_account_card маскирует данные в зависимости от из формата.
    :param user_data_list: Получает список и изначальными данными из фикстуры.
    :param result_user_data_list: Получает список ожидаемых результатов из фикстуры.
    :param index: Получает значение из генератора индекса для прохождению по списку.
    """
    assert mask_account_card(user_data_list[index]) in result_user_data_list
