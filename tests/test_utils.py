from unittest.mock import mock_open, patch

from src.utils import json_loader


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
