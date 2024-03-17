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

    def coding_from_(self):
        """Возвращает описание отправителя перевода
        в формате (Visa Platinum 0000 00** **** 0000)
        или (Счет *0000)
        """
        list_from_ = self.from_.split(" ")
        if "Счет" in list_from_[0]:
            encoded_number = list_from_[1].replace(list_from_[1][0:16], "*", 1)
            return " ".join([list_from_[0], encoded_number])
        else:
            for i in list_from_:
                if i.isdigit():
                    encoded_number = i.replace(i[6:12], "******", 1)
                    list_from_.pop()
                    list_from_.append(encoded_number)
            return " ".join(list_from_)

    def coding_to(self):
        """Возвращает описание отправителя перевода
        в формате (Visa Platinum 0000 00** **** 0000)
        или (Счет *0000)
        """
        list_to = self.to.split(" ")
        if "Счет" in list_to[0]:
            encoded_number = list_to[1].replace(list_to[1][0:16], "*", 1)
            return " ".join([list_to[0], encoded_number])
        else:
            for i in list_to:
                if i.isdigit():
                    encoded_number = i.replace(i[6:12], "******", 1)
                    list_to.pop()
                    list_to.append(encoded_number)
            return " ".join(list_to)

