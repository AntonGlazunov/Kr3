from func.class_ import BankOperation
from func.functions import load_operations_list
from func.functions import object_generator
from func.functions import rearrangement

operations = object_generator(load_operations_list())
counter = 0
last_transactions = []
sort_last_transactions = []
old_transaction = BankOperation(0, "EXECUTED", "1970-01-01T00:00:00.00000", "100", "руб.",
                                "Открытие вклада", "Счет 77613226829885488381")

for i in range(len(operations)):
    sort_last_transactions.append(rearrangement(operations, i))

sort_last_transactions.reverse()

for sort_last_transaction in sort_last_transactions:
    if not sort_last_transaction.operation_verification():
        sort_last_transactions.remove(sort_last_transaction)

for num_ in range(5):
    if sort_last_transactions[num_].from_ != None:
        print(f"""{sort_last_transactions[num_].format_date()} {sort_last_transactions[num_].description}
{sort_last_transactions[num_].coding_from_()} -> {sort_last_transactions[num_].coding_to()}
{sort_last_transactions[num_].send_amount()}
""")
    else:
        print(f"""{sort_last_transactions[num_].format_date()} {sort_last_transactions[num_].description}
{sort_last_transactions[num_].coding_to()}
{sort_last_transactions[num_].send_amount()}
""")
