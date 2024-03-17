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
        """Возвращает дату в формате str(ДД.ММ.ГГГГ)
        """
        return ".".join(self.date.split("T")[0].split("-")[::-1])

    def send_from_(self):
        """Возвращает описание отправителя перевода
        в формате (Visa Platinum 0000 00** **** 0000)
        :param payment_system: название платежной системы
        :param number_card: Номер карты
        :param encoded_number: Зашифрованный номер карты
        """
        payment_system = self.from_.split(' ')[0]
        number_card = self.from_.split(' ')[1]
        encoded_number = number_card.replace(number_card[6:12], "******", 1)
        return " ".join([payment_system, encoded_number[0:4], encoded_number[4:8], encoded_number[8:12], encoded_number[12:16]])
