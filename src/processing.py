def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа
    state. Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению"""

    new_filtered_list = []
    for item in data:
        if item["state"] == state:
            new_filtered_list.append(item)

    return new_filtered_list
