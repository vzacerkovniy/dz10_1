def filter_by_state(input_list: list, state: str = "EXECUTED") -> str:
    """Функция фильтрации списка словарей по значению ключа"""
    executed = []
    canceled = []
    for operation in input_list:
        if operation["state"] != state:
            canceled.append(operation)
        else:
            executed.append(operation)
    return f"{executed}\n{canceled}"


def sort_by_date(input_list: list) -> list:
    """Функция сортировки списка словарей по убыванию даты"""
    output_list = sorted(input_list, key=lambda dic: dic["date"], reverse=True)
    return output_list
