from datetime import datetime

class Operation:
    def __init__(self, oper_id, transw_state, oper_date_, operation_amount, description_type, _to_, _from_=''):
        """
        Инициализирует экземпляр класса Operation.

        :param oper_id: идентификатор операции
        :param oper_date_: дата операции в формате '%Y-%m-%dT%H:%M:%S.%f'
        :param transw_state: состояние перевода
        :param operation_amount: сумма операции
        :param description_type: тип описания операции
        :param _to_: номер счета или кредитной карты получателя
        :param _from_: номер счета или кредитной карты отправителя (по умолчанию пустая строка)
        """
        self.oper_id = oper_id
        self.transw_state = transw_state
        self.oper_date = self._encoded_date(oper_date_)
        self.operation_amount = operation_amount
        self.description_type = description_type
        self._to_ = self.numbers_masking(_to_)
        self._from_ = self.numbers_masking(_from_)if _from_ else ''

    def _encoded_date(self, oper_date):
        """
        Метод принимает на вход дату операции в одном формате
        и возвращает ее в другом формате.

        :param oper_date: дата операции в формате '%Y-%m-%dT%H:%M:%S.%f'
        :return: дата операции в формате '%d.%m.%Y'
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        oper_date = datetime.strptime(oper_date, date_format)
        return datetime.strftime(oper_date, '%d.%m.%Y')

    @staticmethod
    def numbers_masking(account_number: str) -> str:
        """
        Метод принимает на входе строку с номером кредитной карты
        или номером счета и возвращает их с частично замаскированными
        символом '*' цифрами

        :param account_number: номер кредитной карты или счета
        :return: номер кредитной карты или счета с частично замаскированными цифрами
        """
        if account_number.startswith('Счет'):
            list_card_number = account_number.split(' ')
            new_number = f'**{list_card_number[-1][-4:]}'
        else:
            list_card_number = account_number.split(' ')
            new_number = f'{list_card_number[-1][0: 4]} {list_card_number[-1][4: 6]}** **** {list_card_number[-1][-4:]}'
        list_card_number[-1] = new_number
        return ' '.join(list_card_number)

    def __str__(self):
        """
        Возвращает строковое представление объекта Operation

        :return: строковое представление объекта Operation
        """
        if isinstance(self.operation_amount, int):
            amount_str = str(self.operation_amount) + ' RUB'
        else:
            amount_str = self.operation_amount["amount"] + " " + self.operation_amount["currency"]["name"]
        return f'{self.oper_date} {self.description_type}\n{self._from_} -> {self._to_}\n{amount_str}'





