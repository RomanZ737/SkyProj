import json
import logging
import os
from typing import Any

LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "../logs/")
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename=LOG_FILE_PATH + "utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def json_loader(file_path: str) -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список.
    """
    logger.info(f"Открываем файл с транзакциями {file_path}")
    try:
        with open(file_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
            logger.info(f"Файл {file_path} успешно открыт")
            return data
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
    except TypeError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
    except KeyError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
