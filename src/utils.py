import json
from typing import Any


def json_loader(file_path: str) -> Any:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print("Ошибка: ", e)
        return []
