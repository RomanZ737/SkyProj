import logging
import os
from typing import Union

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "../logs/")
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename=LOG_FILE_PATH + "masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str | int]) -> str:
    """Принимает номер карты в виде числа или строки и возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    logger.info(f"Преобразуем номер карты {card_number}")
    if not card_number:
        logger.error("Ошибка - отсутствует номер карты")
        return ""
    elif type(card_number) is str:  # проверяем тип данных
        card_num_mask = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    else:
        card_number_str = str(card_number)  # преобразуем числовую переменную в троку
        card_num_mask = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[12:16]}"
    logger.info(f"Номер карты преобразован: {card_num_mask}")
    return card_num_mask


def get_mask_account(account_number: Union[str | int]) -> str:
    """Принимает номер счета в виде числа или строки и возвращает маску номера по правилу
    **XXXX"""
    logger.info(f"Преобразуем номер счёта {account_number}")
    if not account_number:
        logger.error("Ошибка - отсутствует номер счёта")
        return ""
    elif type(account_number) is str:  # проверяем тип данных
        account_num_mask = f"**{account_number[-4:]}"
    else:
        account_number_str = str(account_number)  # преобразуем числовую переменную в троку
        account_num_mask = f"**{account_number_str[-4:]}"
    logger.info(f"Счёт преобразован: {account_num_mask}")
    return account_num_mask
