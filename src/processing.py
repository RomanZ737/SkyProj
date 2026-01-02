def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа
    state. Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    new_filtered_list = []
    for item in data:
        if item["state"] == state:
            new_filtered_list.append(item)

    return new_filtered_list


def sort_by_date(list_for_sort: list, reverse: bool = True) -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок
    сортировки (по умолчанию — убывание). Возвращает новый список,
    отсортированный по дате (date)."""

    sorted_list = sorted(list_for_sort, key=lambda item: item["date"], reverse=reverse)

    return sorted_list
