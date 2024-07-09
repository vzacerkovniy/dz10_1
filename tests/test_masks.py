from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("Карта 1111 1111 1111 1111") == "Карта 1111 11** **** 1111"

    assert get_mask_card_number("Карта1111111111111111") == "Карта 1111 11** **** 1111"

    assert get_mask_card_number("Visa 1111 1111 1111 1111") == "Visa 1111 11** **** 1111"

    assert get_mask_card_number("1111 1111 1111 1111") == "Неверный ввод"

    assert get_mask_card_number("") == "Неверный ввод"

    assert get_mask_card_number("Carl Jonson") == "Неверный ввод"

    assert get_mask_card_number("Карта 1111 1111 1111 1111 1111") == "Неверный ввод"

    assert get_mask_card_number("Карта 1111 1111 1111") == "Неверный ввод"


def test_get_mask_account() -> None:
    assert get_mask_account("Счет 11111111111111111111") == "Счет **1111"

    assert get_mask_account("Счет11111111111111111111") == "Счет **1111"

    assert get_mask_account("Peppa") == "Неверный ввод"

    assert get_mask_account("11111111111111111111") == "Неверный ввод"

    assert get_mask_account("Счет 111") == "Неверный ввод"

    assert get_mask_account("Счет 123456789123456789123456789") == "Неверный ввод"

    assert get_mask_account("") == "Неверный ввод"
