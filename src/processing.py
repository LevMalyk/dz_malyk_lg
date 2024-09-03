test_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(dict_banking_operations: list, state: str = "EXECUTED") -> list:
    return [
        dict_banking_operations
        for dict_banking_operations in dict_banking_operations
        if dict_banking_operations.get("state") == state
    ]


def sort_by_date(dict_banking_operations: dict, sort_param: bool = True) -> list:
    pass


print(filter_by_state(test_dict))
