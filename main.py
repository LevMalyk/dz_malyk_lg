from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

# Список для тестирования функции mask_account_card
test_bank_info_list = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

# Список словарей для проверки задания 10.1
test_list_for_processing_function = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Для проверки задания 9.1, для проверки раскоментировать код ниже
# print(get_mask_card_number(input()))
# print(get_mask_account(input()))


# Для проверки дадания 9.2, для проверки раскоментировать код ниже
# for i in test_bank_info_list:
#     print(mask_account_card(i))
#
# print(get_date("2024-03-11T02:26:18.671407"))

# Для проверки задания 10.1
print(filter_by_state(test_list_for_processing_function))
print(sort_by_date(test_list_for_processing_function))
