import csv
import logging
import os

import pandas as pd

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "../logs/")

logger = logging.getLogger("data_load")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename=LOG_FILE_PATH + "data_load.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def csv_loader(file_path: str) -> list:
    """
    Функция принимает путь к файлу csv, возвращает список словарей с транзакциями
    """
    logger.info(f"Открываем файл CSV с транзакциями {file_path}")
    transactions = []
    try:
        with open(file_path, encoding="utf-8") as csvfile:
            reader = csv.DictReader(
                csvfile,
                delimiter=";",
            )
            logger.info(f"Файл CSV {file_path} успешно открыт")
            for row in reader:
                transactions.append(row)
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return transactions
    except TypeError as e:
        logger.error(f"Ошибка: {e}")
        return transactions
    except csv.Error as e:
        logger.error(f"Ошибка: {e}")
        return transactions
    return transactions


def xlsx_loader(file_path: str) -> list:
    """
    Функция принимает путь к файлу xlsx, возвращает список словарей с транзакциями
    """
    logger.info(f"Открываем файл XLSX с транзакциями {file_path}")
    try:
        excel_data = pd.read_excel(file_path)
        logger.info(f"Файл XLSX {file_path} успешно открыт")
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return []
    except TypeError as e:
        logger.error(f"Ошибка: {e}")
        return []
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []
    return excel_data.to_dict("records")
