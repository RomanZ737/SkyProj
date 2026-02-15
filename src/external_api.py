from dotenv import load_dotenv
import requests
import os
from typing import Any

# Загрузка переменных из .env-файла
load_dotenv()


def exchange_request(from_currency: str, amount: float) -> Any:
    """
    Функция выполняет запрос к внешнему API для обмена валют.
    Принимает тип валюты из которого надо конвертировать и тип валюты, в который надо конвертировать
    Возвращает словарь с данными конвертации
    """
    api_token = os.getenv("EXCHANGE_RATES_API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"
    headers = {"apikey": api_token}
    response = requests.request("GET", url, headers=headers)
    return response.json()


def get_transaction_amount(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму
    транзакции (amount) в рублях
    """
    # amount = transaction['operationAmount']['amount']
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency != "RUB":
        amount = round(exchange_request(currency, amount)["result"], 2)
        return float(amount)
    else:
        return float(amount)


if __name__ == "__main__":
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    }
    print(get_transaction_amount(transaction))
