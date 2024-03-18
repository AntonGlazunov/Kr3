from func.functions import object_generator
from func.functions import load_operations_list
import datetime

operations = object_generator(load_operations_list())
time_last_transactions = datetime.datetime.strptime("1970-01-01T00:00:00", '%Y-%m-%dT%H:%M:%S')
sort_operation = []
counter = 0
last_transactions = []

for operation in operations:
    if counter < 5:
        last_transactions.append(operation)
        counter += 1
    else:
        for last_transaction in last_transactions:
            if operation.format_datatime() > last_transaction.format_datatime():
                last_transactions.remove(last_transaction)
                last_transactions.append(operation)
                break



