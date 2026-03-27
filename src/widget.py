from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card_number: str) -> str:
    """Принимает строку, содержащую тип и номер карты или счета,
    возвращает строку с замаскированным номером"""
    name_of_card_or_account = ""  # Название карты или счёт
    number_value_of_card_or_account = ""  # Номер карты или счёта
    card_or_account_mask = ""  # Маска номера карты или счёта
    if type(account_or_card_number) is not str:
        raise ValueError("Некорректные данные")
    for symbol in account_or_card_number:
        if symbol.isdigit():
            number_value_of_card_or_account += symbol
        else:
            name_of_card_or_account += symbol
    if name_of_card_or_account != "Счет ":
        card_or_account_mask = get_mask_card_number(number_value_of_card_or_account)
    else:
        card_or_account_mask = get_mask_account(number_value_of_card_or_account)

    return name_of_card_or_account + card_or_account_mask


def get_date(data_iso_format: str) -> str:
    """Принимает дату в формате ISO-8601, возвращает дату в стандартном формате: ДД.ММ.ГГГГ"""
    try:
        dt = datetime.strptime(data_iso_format, "%Y-%m-%dT%H:%M:%S.%f")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        try:
            dt = datetime.strptime(data_iso_format, "%Y-%m-%dT%H:%M:%SZ")
            return dt.strftime("%d.%m.%Y")
        except ValueError:
            return "Неверный формат даты"
