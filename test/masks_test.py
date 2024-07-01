from src.masks import get_mask_account, get_mask_card_number

card = input("Введите номер карты: \n")
account = input("Введите номер счета: \n")
print(f"Номер карты: {get_mask_card_number(card)}")
print(f"Номер счета: {get_mask_account(account)}")
