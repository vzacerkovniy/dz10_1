from src.widget import get_data, mask_account_card


def test_mask_account_card() -> None:
    assert mask_account_card("Карта 1111 1111 1111 1111") == "Карта 1111 11** **** 1111"

    assert mask_account_card("Карта1111111111111111") == "Карта 1111 11** **** 1111"

    assert mask_account_card("Visa 1111 1111 1111 1111") == "Visa 1111 11** **** 1111"

    assert mask_account_card("1111 1111 1111 1111") == "Неверный ввод"

    assert mask_account_card("") == "Неверный ввод"

    assert mask_account_card("Carl Jonson") == "Неверный ввод"

    assert mask_account_card("Карта 1111 1111 1111 1111 1111") == "Неверный ввод"

    assert mask_account_card("Карта 1111 1111 1111") == "Неверный ввод"

    assert mask_account_card("Счет 11111111111111111111") == "Счет **1111"

    assert mask_account_card("Счет11111111111111111111") == "Счет **1111"

    assert mask_account_card("Peppa") == "Неверный ввод"

    assert mask_account_card("11111111111111111111") == "Неверный ввод"

    assert mask_account_card("Счет 111") == "Неверный ввод"

    assert mask_account_card("Счет 123456789123456789123456789") == "Неверный ввод"

    assert mask_account_card("") == "Неверный ввод"


def test_get_data() -> None:
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"

    assert get_data("2024-03-11") == "11.03.2024"

    assert get_data("Tututu") == "Неверный ввод"

    assert get_data("") == "Неверный ввод"
