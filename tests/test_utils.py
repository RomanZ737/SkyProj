from unittest.mock import mock_open, patch

from src.utils import json_loader, process_bank_operations, process_bank_search


def test_json_loader(data_for_json_file_open: str) -> None:
    """
    Тестируем функцию json_loader. Функция принимает на вход
    путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не
    список или не найден, функция возвращает пустой список
    """
    mock_open_file = mock_open(read_data=data_for_json_file_open)
    with patch("src.utils.open", mock_open_file):
        result = json_loader("operations.json")
        assert str(result) == data_for_json_file_open.replace('"', "'")
        mock_open_file.assert_called_once_with("operations.json", encoding="utf-8")


def test_process_bank_operations(output_usd_filter_by_currency: list[dict]) -> None:
    """
    Тестируем функцию process_bank_operations. Принимает список словарей с данными
    о банковских операциях и список с категорий операций.
    Возвращает словарь в котором ключи - это названия категорий, а значения
    это количество операций в каждой категории
    """
    categories = ["Перевод организации", "Перевод со счета на счет"]
    assert process_bank_operations(output_usd_filter_by_currency, categories) == {
        "Перевод организации": 1,
        "Перевод со счета на счет": 1,
    }


def test_process_bank_search(output_usd_filter_by_currency: list[dict]) -> None:
    """
    Тестируем функцию process_bank_search. Принимает список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.
    """
    search = "Перевод организации"
    assert process_bank_search(output_usd_filter_by_currency, search) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
