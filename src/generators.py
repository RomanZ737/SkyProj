from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[dict]:
    """Принимает на вход список словарей, представляющих транзакции.
    Функция (генератор) возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[dict]:
    """Принимает список словарей с транзакциями и возвращает описание
    каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(num_start: int, num_end: int) -> Iterator[str]:
    """Принимает начальное и конечное значения для генерации диапазона номеров.
    Возвращает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты"""
    for num in range(num_start, num_end + 1):
        result = f"{num_start:016}"
        yield f"{result[0:4]} {result[4:8]} {result[8:12]} {result[12:16]}"
        num_start += 1
