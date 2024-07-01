def mask_account_card(number: str) ->str:
    if "Счет" in number:
        mask_number = number[:-20] + "**" + number[-4:]
        return mask_number
    else:
        mask_number = number[:-16] + number[-16:-12] + " " + number[-12:-10] + "** **** " + number[-4:]
        return mask_number


def get_data(data: str) ->str:
    new_data = data[8:10] + "." + data[5:7] + "." + data[0:4]
    return new_data
