import datetime


class BankOperation:

    def __init__(self, id, state, date, amount, currency_name, description, to, from_=None):
        self.id = id
        self.state = state
        self.date = date
        self.amount = amount
        self.currency_name = currency_name
        self.description = description
        self.from_ = from_
        self.to = to

    def format_date(self):
        """Возвращает дату в формате str(ДД.ММ.ГГГГ)
        """
        return ".".join(self.date.split("T")[0].split("-")[::-1])

    def coding_from_(self):
        """Возвращает описание отправителя перевода
        в формате (Visa Platinum 0000 00** **** 0000)
        или (Счет *0000)
        """
        if self.from_ == None:
            return self.from_
        list_from_ = self.from_.split(" ")
        if "Счет" in list_from_[0]:
            encoded_number = list_from_[1].replace(list_from_[1][0:16], "*", 1)
            return " ".join([list_from_[0], encoded_number])
        else:
            for i in list_from_:
                if i.isdigit():
                    encoded_number = i.replace(i[6:12], "******", 1)
                    format_number = " ".join([encoded_number[0:4], encoded_number[4:8],
                                              encoded_number[8:12], encoded_number[12:16]])
                    list_from_.pop()
                    list_from_.append(format_number)
            return " ".join(list_from_)

    def coding_to(self):
        """Возвращает описание получателя перевода
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
                    format_number = " ".join(
                        [encoded_number[0:4], encoded_number[4:8], encoded_number[8:12], encoded_number[12:16]])
                    list_to.pop()
                    list_to.append(format_number)
            return " ".join(list_to)

    def send_amount(self):
        """
        Возвращает сумму перевода в формате
        (00000.00 ###)
        """
        return " ".join([self.amount, self.currency_name])

    def format_datatime(self):
        """Возвращает дату и время
        в виде класса datatime
        """
        date_time = self.date.split(".")[0]
        return datetime.datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S')

    def operation_verification(self):
        if "EXECUTED" in self.state:
            return True
        else:
            return False
