import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("index", [i for i in range(8)])
def test_get_mask_card_number(my_list_masks_test: list[str], result_list_card_number: list[str], index: int) -> None:
    """
    Проверяет что функция get_mask_card_number правильно маскирует номер карты
    :param my_list_masks_test: Список значений для маскировки
    :param result_list_card_number: Список ожидаемых значений
    :param index: Получает значение генератора для прохождения теста
    """
    assert get_mask_card_number(my_list_masks_test[index]) in result_list_card_number


@pytest.mark.parametrize("index", [i for i in range(8)])
def test_get_mask_account(my_list_masks_test: list[str], result_list_account_number: list[str], index: int) -> None:
    """
    Проверяет что функция get_mask_account правильно маскирует номер счета
    :param my_list_masks_test: Список значений для маскировки
    :param result_list_account_number: Список ожидаемых значений
    :param index: Получает значение генератора для прохождения теста
    """
    assert get_mask_account(my_list_masks_test[index]) in result_list_account_number
