import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('index', [i for i in range(8)])
def test_get_mask_card_number(my_list_masks_test, result_list_card_number, index):
    assert get_mask_card_number(my_list_masks_test[index]) in result_list_card_number


@pytest.mark.parametrize('index', [i for i in range(8)])
def test_get_mask_account(my_list_masks_test, result_list_account_number, index):
    assert get_mask_account(my_list_masks_test[index]) in result_list_account_number
