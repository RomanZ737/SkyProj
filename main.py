import os

from src.data_load import csv_loader, xlsx_loader
from src.generators import filter_by_currency
from src.masks import get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.utils import json_loader, process_bank_search
from src.widget import get_date, mask_account_card

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data/")


def filter_chooses() -> str:
    """
    Ничего не принимает.
    Возвращает вариант фильтрации, выбранный пользователем
    """
    print("Введите статус, по которому необходимо выполнить фильтрацию.")

    while True:
        print("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING")
        choice = input("Введите значение: ")
        if choice.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            return choice.upper()
        else:
            print(f'Статус операции "{choice}" недоступен')
            print("Введите статус, по которому необходимо выполнить фильтрацию")


def sort_choices(data: list[dict]) -> list:
    """
    Принимает список словарей с транзакциями.
    Реализует функции по выбору пользователя:
    - Сортировка по дате (по возрастанию или убыванию)
    - Сортирует рублёвые транзакции
    - Сортирует по определённому слову
    -
    """
    user_choice = input("Отсортировать операции по дате? Да/Нет: ")
    if user_choice.lower() == "да":
        user_choice = input("Отсортировать по возрастанию или убыванию? ")
        if user_choice.lower() == "по возрастанию":
            data = sort_by_date(data, reverse=False)
        else:
            data = sort_by_date(data)
    user_choice = input("Выводить только рублёвые транзакции? Да/Нет: ")
    currency_filtered = []
    if user_choice.lower() == "да":
        for transaction in filter_by_currency(data, "RUB"):
            currency_filtered.append(transaction)
        data = currency_filtered
    user_choice = input("Отсортировать список транзакций по определённому слову в описании? Да/Нет: ")
    if user_choice.lower() == "да":
        user_choice = input("Введите слово: ")
        data = process_bank_search(data, user_choice)
    return data


def transactions_print(data: list[dict]) -> None:
    """
    Функция для форматированного вывода в консоль результатов сортировки.
    Принимает список транзакций со словарями.
    """
    print("Распечатываю итоговый список")
    total_num_of_transactions = len(data)
    if total_num_of_transactions > 0:
        print(f"Всего транзакций {total_num_of_transactions}")
        print()
        for transaction in data:

            if transaction["description"] == "Перевод с карты на карту":
                print(f'{get_date(transaction["date"])} Перевод с карты на карту')
                print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
                try:
                    print(
                        f'Сумма: {transaction["amount"]} '
                        f'{"руб." if transaction["currency_code"] == 'RUB' else transaction["currency_code"]}'
                    )
                except KeyError:
                    print(
                        f'Сумма: {transaction["operationAmount"]["amount"]} '
                        f'{"руб." if transaction["operationAmount"]["currency"]["code"] ==
                            'RUB' else transaction["operationAmount"]["currency"]["code"]}'
                    )
                print()
            elif transaction["description"] == "Открытие вклада":
                print(f'{get_date(transaction["date"])} Открытие вклада')
                print(f'Счёт: {get_mask_account(transaction["to"])}')
                try:
                    print(
                        f'Сумма: {transaction["amount"]} '
                        f'{"руб." if transaction["currency_code"] == 'RUB' else transaction["currency_code"]}'
                    )
                except KeyError:
                    print(
                        f'Сумма: {transaction["operationAmount"]["amount"]} '
                        f'{"руб." if transaction["operationAmount"]["currency"]["code"] ==
                            'RUB' else transaction["operationAmount"]["currency"]["code"]}'
                    )
                print()
            elif transaction["description"] == "Перевод со счета на счет":
                print(f'{get_date(transaction["date"])} Перевод со счета на счет')
                print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
                try:
                    print(
                        f'Сумма: {transaction["amount"]} '
                        f'{"руб." if transaction["currency_code"] == 'RUB' else transaction["currency_code"]}'
                    )
                except KeyError:
                    print(
                        f'Сумма: {transaction["operationAmount"]["amount"]} '
                        f'{"руб." if transaction["operationAmount"]["currency"]["code"] ==
                            'RUB' else transaction["operationAmount"]["currency"]["code"]}'
                    )

                print()
            else:
                print(f'{get_date(transaction["date"])} Перевод организации')
                print(f'{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}')
                try:
                    print(
                        f'Сумма: {transaction["amount"]} '
                        f'{"руб." if transaction["currency_code"] == 'RUB' else transaction["currency_code"]}'
                    )
                except KeyError:
                    print(
                        f'Сумма: {transaction["operationAmount"]["amount"]} '
                        f'{"руб." if transaction["operationAmount"]["currency"]["code"] ==
                            'RUB' else transaction["operationAmount"]["currency"]["code"]}'
                    )

                print()
    else:
        print("не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main() -> None:
    """
    Отвечает за основную логику программы.
    Связывает функциональности между собой.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями")
    print("Выберите пункт: ")
    while True:
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        print("4. Выйти из программы")
        choice = input("Пользователь: ")
        if choice == "1":
            print("Для обработки выбран JSON-файл")
            data = json_loader(DATA_FILE_PATH + "operations.json")
            user_filter_choice = filter_chooses()
            filtered_by_state_data = filter_by_state(data, user_filter_choice)
            print(f"Операции отфильтрованы по статусу {user_filter_choice}")
            transactions_to_print = sort_choices(filtered_by_state_data)
            transactions_print(transactions_to_print)
            break
        elif choice == "2":
            print("Для обработки выбран CSV-файл")
            data = csv_loader(DATA_FILE_PATH + "transactions.csv")
            user_filter_choice = filter_chooses()
            filtered_by_state_data = filter_by_state(data, user_filter_choice)
            print(f"Операции отфильтрованы по статусу {user_filter_choice}")
            transactions_to_print = sort_choices(filtered_by_state_data)
            transactions_print(transactions_to_print)
            break
        elif choice == "3":
            print("Для обработки выбран XLSX-файл")
            data = xlsx_loader(DATA_FILE_PATH + "transactions_excel.xlsx")
            user_filter_choice = filter_chooses()
            filtered_by_state_data = filter_by_state(data, user_filter_choice)
            print(f"Операции отфильтрованы по статусу {user_filter_choice}")
            transactions_to_print = sort_choices(filtered_by_state_data)
            transactions_print(transactions_to_print)
            break
        elif choice == "4":
            break
        else:
            print("Вы не выбрали действие")


if __name__ == "__main__":
    main()
