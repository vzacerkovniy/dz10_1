def get_mask_card_number(number: str) -> str:
    """Функция, возвращающая маску карты"""
    card_mask = number[:-17] + " " + number[-16:-12] + " " + number[-12:-10] + "** **** " + number[-4:]
    return card_mask


def get_mask_account(number: str) -> str:
    """Функция, возвращающая маску счета"""
    account_mask = "Счет **" + number[-4:]
    return account_mask
