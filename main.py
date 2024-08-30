from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

# Список для тестирования функции mask_account_card
test_bank_info_list = ['Maestro 1596837868705199',
'Счет 64686473678894779589',
'MasterCard 7158300734726758',
'Счет 35383033474447895560',
'Visa Classic 6831982476737658',
'Visa Platinum 8990922113665229',
'Visa Gold 5999414228426353',
'Счет 73654108430135874305']

# Для проверки задания 9.1
# print(get_mask_card_number(input()))
# print(get_mask_account(input()))


# Для проверки дадания 9.2
for i in test_bank_info_list:
    print(mask_account_card(i))

print(get_date("2024-03-11T02:26:18.671407"))
