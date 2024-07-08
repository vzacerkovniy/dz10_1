def filter_by_state(input_list: list, state: str = "EXECUTED") -> list:
    """Функция фильтрации списка словарей по значению ключа"""
    executed = []
    canceled = []
    for operation in input_list:
        if operation["state"] == "CANCELED":
            canceled.append(operation)
        else:
            executed.append(operation)
    if state == "CANCELED":
        return canceled
    else:
        return executed


def sort_by_date(input_list: list) -> list:
    """Функция сортировки списка словарей по убыванию даты"""
    output_list = sorted(input_list, key=lambda dic: dic["date"], reverse=True)
    return output_list
