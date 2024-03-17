import json
import os

def load_operations_list():
    '''Загружает список операций из файла'''
    with open(os.path.join("..", "operations.json"), 'r', encoding = "utf-8") as file:
        operations_list = json.loads(file.read())
        return operations_list
