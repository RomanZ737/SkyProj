import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.data_load import csv_loader, xlsx_loader


def test_csv_loader(data_for_csv_and_xlsx_file_open: str) -> None:
    """
    Тестируем функцию json_loader. Функция принимает на вход
    путь до CSV-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не
    список или не найден, функция возвращает пустой список
    """
    mock_open_file = mock_open(read_data=data_for_csv_and_xlsx_file_open)
    with patch("src.data_load.open", mock_open_file):
        result = csv_loader("transactions.csv")
        assert str(result) == """[{'id': '            650703', 'state': 'EXECUTED', '': ''}]"""
        mock_open_file.assert_called_once_with("transactions.csv", encoding="utf-8")


@patch("src.data_load.pd.read_excel")
def test_xlsx_loader(mock_read_excel: unittest.mock.Mock) -> None:
    """
    Тестируем функцию json_loader. Функция принимает на вход
    путь до XLSX-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не
    список или не найден, функция возвращает пустой список
    """
    mock_df = pd.DataFrame({"existing_col": [1, 2, 3]})
    mock_read_excel.return_value = mock_df
    result_df = pd.DataFrame(xlsx_loader("transactions_excel.xlsx"))
    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")
    expected_df = pd.DataFrame({"existing_col": [1, 2, 3]})
    pd.testing.assert_frame_equal(result_df, expected_df)
