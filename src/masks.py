def get_mask_card_number(card: str) -> str:
    """Функция, возвращающая маску карты"""
    no_space_card = card.replace(" ", "")
    if card != "" and len(no_space_card) == 16 and no_space_card.isdigit():
        card_mask = no_space_card[0:4] + " " + no_space_card[4:6] + "** **** " + no_space_card[12:]
        return card_mask
    else:
        return "Некорректный номер карты"


def get_mask_account(account: str) -> str:
    """Функция, возвращающая маску счета"""
    no_space_account = account.replace(" ", "")
    if account != "" and no_space_account.isdigit():
        account_mask = "**" + no_space_account[-4:]
        return account_mask
    else:
        return "Некорректный номер счета"
