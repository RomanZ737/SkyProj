import pytest


@pytest.fixture
def input_data_filter_by_state() -> list:
    """Фикстура возвращает данные для тестирования функции filter_by_state"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture
def output_data_filter_by_state_executed() -> list:
    """Фукстура возвращает выходные данные
    filter_by_state с условием EXECUTED"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]


@pytest.fixture
def output_data_filter_by_state_canceled() -> list:
    """Фукстура возвращает выходные данные
    filter_by_state с условием CANCELED"""
    return [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture
def input_data_sort_by_date_1() -> list:
    """Фукстура возвращает входные данные для функции sort_by_date"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
    ]


@pytest.fixture
def input_data_sort_by_date_2() -> list:
    """Фукстура возвращает входные данные
    для функции sort_by_date с одинаковой датой"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
    ]


@pytest.fixture
def output_data_sort_by_date_1() -> list:
    """Фукстура возвращает выходные данные для функции sort_by_date"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
    ]


@pytest.fixture
def output_data_sort_by_date_2() -> list:
    """Фукстура возвращает выходные данные
    для функции sort_by_date с одинаковой датой"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
        },
    ]


@pytest.fixture
def output_data_sort_by_date_1_reversed() -> list:
    """Фукстура возвращает выходные данные
    для функции sort_by_date с условием reverse=False"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
    ]


@pytest.fixture
def input_data_sort_by_date_wrong_dates() -> list:
    """Фукстура возвращает входные данные
    для функции sort_by_date с неверным форматом датам"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-3002:08:58.425572",
        },
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27"},
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
    ]


@pytest.fixture
def output_data_sort_by_date_wrong_dates() -> list:
    """Фукстура возвращает выходные данные
    для функции sort_by_date с неверным форматом датам"""
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
        },
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27"},
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-3002:08:58.425572",
        },
    ]


@pytest.fixture
def input_filter_by_currency_and_transaction_descriptions() -> list:
    """Фукстура возвращает входные данные
    для функций-генераторов filter_by_currency и
    transaction_descriptions с неверным форматом датам"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def output_usd_filter_by_currency() -> list:
    """Фукстура возвращает выходные данные
    для функций-генераторов filter_by_currency и
    transaction_descriptions с неверным форматом датам"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


@pytest.fixture
def output_transaction_descriptions() -> list:
    """Фукстура возвращает выходные данные
    для функций-генераторов transaction_descriptions"""
    return [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.fixture
def data_for_json_file_open() -> str:
    """
    Фукстура возвращает выходные данные
    для json_file_open
    """
    return """{"id": 441945886}"""


@pytest.fixture
def data_for_csv_and_xlsx_file_open() -> str:
    """
    Фукстура возвращает выходные данные
    для csv и xlsx фалов
    """
    return """id;state;
            650703;EXECUTED;"""
