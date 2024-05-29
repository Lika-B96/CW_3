import unittest
from app.operation import Operation, _encoded_date

class TestEncodedDate(unittest.TestCase):

    def test_encoded_date(self):
        oper_date = '2022-01-01T12:00:00.000000'
        expected_result = '01.01.2022'
        self.assertEqual(_encoded_date(oper_date), expected_result)

    def test_encoded_date_invalid_input(self):
        with self.assertRaises(ValueError):
            _encoded_date('invalid_date')

    def test_numbers_masking(self):
        account_number = 'Счет 1234567890123456'
        masked_number = Operation.numbers_masking(account_number)
        self.assertEqual(masked_number, '**123456')

        account_number = '4123456789012345'
        masked_number = Operation.numbers_masking(account_number)
        self.assertEqual(masked_number, '4123 45** **** 1234')

    def test_str(self):
        oper_date = '2023-02-24T12:34:56.789'
        operation = Operation(1, 'success', oper_date, 100, 'transfer', '1234567890123456', '4123456789012345')
        expected_output = '24.02.2023 transfer\nСчет 1234567890123456 -> 4123 45** **** 1234\n100 RUB'
        self.assertEqual(str(operation), expected_output)
