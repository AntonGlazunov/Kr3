class BankOperations:

    def __init__(self, id_operations, state, date, amount, currency_code, description, from_, to):
        self.id_operations = id_operations
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_code = currency_code
        self.description = description
        self.from_ = from_
        self.to = to

    def send_format_date(self):
        """Возвращает дату в формате ДД.ММ.ГГГГ
        """
        return ".".join(self.date.split("T")[0].split("-")[::-1])
