from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функция, возвращающая маску карты или счета"""
    if "Счет" in number:
        return get_mask_account(number)
    else:
        return get_mask_card_number(number)


def get_data(data: str) -> str:
    """Функция, возвращающая дату в фотраме дд.мм.гггг"""
    new_data = data[8:10] + "." + data[5:7] + "." + data[0:4]
    return new_data
