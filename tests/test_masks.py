import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('index', [i for i in range(8)])
def test_get_mask_card_number(my_list, my_list_result, index):
    assert get_mask_card_number(my_list[index]) in my_list_result
