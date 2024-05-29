import json
from src.settings import PATH_WITH_FIXTURES

def get_data(path):
    """
    Выгружает данные из указанного JSON файла.

    :param path: Путь к JSON файлу.
    :return: Возвращает список операций из JSON файла.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

data = get_data(PATH_WITH_FIXTURES)

def delete_empty_operations(operations):
    """
    Удаляет из списка операций пустые операции.

    :param operations: Список операций.
    :return: Список операций без пустых операций.
    """
    operations.remove({})
    return operations

new_data = delete_empty_operations(data)

def get_first_five_sorted_operations(operation_list):
    """
    Возвращает первые пять операций из списка, отсортированных по полю "state" и "date" в порядке убывания.

    :param operation_list: Список операций.
    :return: Первые пять отсортированных операций.
    """
    return sorted(
        operation_list,
        key=lambda operation_data: (operation_data['state'], operation_data['date']),
        reverse=True
    )[:5]

five_operations = get_first_five_sorted_operations(new_data)