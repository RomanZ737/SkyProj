import os
import unittest
from unittest.mock import patch

from src.external_api import exchange_request, get_transaction_amount


@patch("src.external_api.requests.request")
def test_exchange_request(mock_requests_get: unittest.mock.Mock) -> None:
    """
    Тестируем функцию обработки суммы транзакции и работу с внешним API
    """

    mock_requests_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 123, "rate": 91.6245},
        "date": "2026-02-14",
        "result": 2928097.28871,
    }

    assert exchange_request("EUR", 31957.58) == {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 123, "rate": 91.6245},
        "date": "2026-02-14",
        "result": 2928097.28871,
    }

    api_token = os.getenv("EXCHANGE_RATES_API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=31957.58"
    headers = {"apikey": api_token}
    mock_requests_get.assert_called_once_with("GET", url, headers=headers)


def test_get_transaction_amount() -> None:
    """
    Тестируем функцию get_transaction_amount.
    Фуекция принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях
    """
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }
    assert get_transaction_amount(transaction) == 31957.58
