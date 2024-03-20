import json
import os

from func.class_ import BankOperation

def load_operations_list(path_ = "..", path1_ = "operations.json"):
    '''Загружает список операций из файла'''
    with open(os.path.join(path_, path1_), 'r', encoding="utf-8") as file:
        operations_list = json.loads(file.read())
        return operations_list


def object_generator(operations_list):
    """Создает обьекты класса BankOperation"""
    for i in operations_list:
        if "id" not in i.keys():
            operations_list.remove(i)
    operations = []
    for i in range(len(operations_list)):
        if "from" not in operations_list[i].keys():
            operations.append(BankOperation(operations_list[i]['id'], operations_list[i]['state'], operations_list[i]['date'],
                                            operations_list[i]['operationAmount']['amount'],
                                            operations_list[i]['operationAmount']['currency']['name'],
                                            operations_list[i]['description'], operations_list[i]["to"]))
        else:
            operations.append(BankOperation(operations_list[i]['id'], operations_list[i]['state'], operations_list[i]['date'],
                                            operations_list[i]['operationAmount']['amount'],
                                            operations_list[i]['operationAmount']['currency']['name'],
                                            operations_list[i]['description'], operations_list[i]["to"],
                                            operations_list[i]["from"]))
    return operations


def rearrangement(last_transactions, place):
    "Выберает операцию их добавленных в список в зависимости от даты"
    if place > len(last_transactions) - 1:
        return "Не верное число"
    for last_transaction_ in last_transactions:
        counter = 0
        for i in range(len(last_transactions)):
            if last_transaction_.format_datatime() > last_transactions[i].format_datatime():
                counter += 1
        if counter == place:
            sort_last_transactions = last_transaction_
            break
    return sort_last_transactions
