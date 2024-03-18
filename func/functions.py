import json
import os
import datetime
from func.class_ import BankOperation

def load_operations_list():
    '''Загружает список операций из файла'''
    with open(os.path.join("..", "operations.json"), 'r', encoding="utf-8") as file:
        operations_list = json.loads(file.read())
        return operations_list



def object_generator(operations_list):
    """Создает обьекты класса BankOperation"""
    for i in operations_list:
        if "id" not in i.keys():
            operations_list.remove(i)
    operations = []
    for i in range(len(operations_list)):
        if "id" not in operations_list[i].keys():
            operations_list.remove(operations_list[i])
        elif "from" not in operations_list[i].keys():
            operations.append(BankOperation(operations_list[i]['state'], operations_list[i]['date'],
                                            operations_list[i]['operationAmount']['amount'],
                                            operations_list[i]['operationAmount']['currency']['name'],
                                            operations_list[i]['description'], operations_list[i]["to"]))
        else:
            operations.append(BankOperation(operations_list[i]['state'], operations_list[i]['date'],
                                            operations_list[i]['operationAmount']['amount'],
                                            operations_list[i]['operationAmount']['currency']['name'],
                                            operations_list[i]['description'], operations_list[i]["to"],
                                            operations_list[i]["from"]))
    return operations




