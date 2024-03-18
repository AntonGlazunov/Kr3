from func.functions import load_operations_list
from func.functions import object_generator
from func.functions import rearrangement

operations = object_generator(load_operations_list())
counter = 0
last_transactions = []
sort_last_transactions = []

for operation in operations:
    if counter < 5 and operation.operation_verification():
        last_transactions.append(operation)
        counter += 1
    else:
        for last_transaction in last_transactions:
            if operation.format_datatime() > last_transaction.format_datatime() and operation.operation_verification():
                last_transactions.remove(last_transaction)
                last_transactions.append(operation)
                break

for i in range(len(last_transactions)):
    sort_last_transactions.append(rearrangement(last_transactions, i))

sort_last_transactions.reverse()

for one_last_transaction in sort_last_transactions:
    if one_last_transaction.from_ != None:
        print(f"""{one_last_transaction.format_date()} {one_last_transaction.description}
{one_last_transaction.coding_from_()} -> {one_last_transaction.coding_to()}
{one_last_transaction.send_amount()}
""")
    else:
        print(f"""{one_last_transaction.format_date()} {one_last_transaction.description}
{one_last_transaction.coding_to()}
{one_last_transaction.send_amount()}
""")
