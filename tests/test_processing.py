from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_1(
    input_data_filter_by_state: list,
    output_data_filter_by_state_executed: list) -> None:
    """Функция тестирует функцию filter_by_state с условием EXECUTED
    и подачу на вход пустого списка"""
    assert (
        filter_by_state(input_data_filter_by_state)
        == output_data_filter_by_state_executed
    )
    assert filter_by_state([]) == []


def test_filter_by_state_2(
    input_data_filter_by_state: list,
    output_data_filter_by_state_canceled: list,
) -> None:
    """Функция тестирует функцию filter_by_state с условием CANCELED"""
    assert (
        filter_by_state(input_data_filter_by_state, "CANCELED")
        == output_data_filter_by_state_canceled
    )


def test_sort_by_date_1(
    input_data_sort_by_date_1: list, output_data_sort_by_date_1: list
) -> None:
    """Функция тестирует функцию sort_by_date и
    подачу пустого списка данных на вход"""
    assert (
        sort_by_date(input_data_sort_by_date_1) == output_data_sort_by_date_1
    )
    assert sort_by_date([]) == []


def test_sort_by_date_2(
    input_data_sort_by_date_2: list, output_data_sort_by_date_2: list
) -> None:
    """Функция тестирует функцию sort_by_date
    и подачу на вход списка с одинаковыми датами"""
    assert (
        sort_by_date(input_data_sort_by_date_2) == output_data_sort_by_date_2
    )


def test_sort_by_date_reversed(
    input_data_sort_by_date_1: list, output_data_sort_by_date_1_reversed: list
) -> None:
    """Функция тестирует функцию sort_by_date с условием reverse=False"""
    assert (
        sort_by_date(input_data_sort_by_date_1, reverse=False)
        == output_data_sort_by_date_1_reversed
    )


def test_sort_by_date_wrong_dates(
    input_data_sort_by_date_wrong_dates: list,
    output_data_sort_by_date_wrong_dates: list,
) -> None:
    """Функция тестирует функцию sort_by_date
    с подачей на вход списка дат с неверным форматом"""
    assert (
        sort_by_date(input_data_sort_by_date_wrong_dates)
        == output_data_sort_by_date_wrong_dates
    )
