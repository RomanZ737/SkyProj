from typing import Union


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Принимает номер карты в виде числа или строки и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    if not card_number:
        return ""
    elif type(card_number) is str:  # проверяем тип данных
        card_num_mask = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    else:
        card_number_str = str(card_number)  # преобразуем числовую переменную в троку
        card_num_mask = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:16]}"

    return card_num_mask


def get_mask_account(account_number: Union[str | int]) -> str:
    """Принимает номер счета в виде числа или строки и возвращает маску номера по правилу
    **XXXX"""
    if not account_number:
        return ""
    elif type(account_number) is str:  # проверяем тип данных
        account_num_mask = f"**{account_number[-4:]}"
    else:
        account_number_str = str(account_number)  # преобразуем числовую переменную в троку
        account_num_mask = f"**{account_number_str[-4:]}"

    return account_num_mask


if __name__ == "__main__":
    print(get_mask_card_number("792289606361"))
    print(get_mask_account(""))