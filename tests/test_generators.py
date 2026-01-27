import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(
    input_filter_by_currency_and_transaction_descriptions: list, output_usd_filter_by_currency: list
) -> None:
    """Тестируем функцию filter_by_currency,
    стандартные входные данные и пустой список данных"""
    result = list(filter_by_currency(input_filter_by_currency_and_transaction_descriptions, "USD"))
    assert result == output_usd_filter_by_currency
    assert list(filter_by_currency([], "USD")) == []
    assert list(filter_by_currency([], "XXX")) == []


def test_transaction_descriptions(
    input_filter_by_currency_and_transaction_descriptions: list, output_transaction_descriptions: list
) -> None:
    """Тестируем функцию (генератор) transaction_descriptions,
    стандартные входные данные и пустой список данных"""
    result = list(
        transaction_descriptions(
            input_filter_by_currency_and_transaction_descriptions,
        )
    )
    assert result == output_transaction_descriptions
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "num_start, num_end, expected_result",
    [
        (0, 0, ["0000 0000 0000 0000"]),
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        (5, 1, []),
    ],
)
def test_card_number_generator(num_start: int, num_end: int, expected_result: list) -> None:
    """Тестируем функцию (генератор) card_number_generator,
    стандартные входные данные и пустой список данных"""
    assert list(card_number_generator(num_start, num_end)) == expected_result
