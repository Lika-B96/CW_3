import unittest
from app.models.operation import Operation

class TestOperationCreation(unittest.TestCase):
    def test_operation_creation(self):
        oper_data = {
            'id': 1,
            'date': '2022-01-01',
            'description': 'Test operation',
            'operationAmount': 100.0,
            'to': 'Account 1',
            'from': 'Account 2'
        }

        oper = Operation(oper_id=oper_data['id'],
                         oper_date_=oper_data['date'],
                         transw_state=oper_data['description'],
                         operation_amount=oper_data['operationAmount'],
                         description_type=oper_data["description"],
                         _to_=oper_data['to'],
                         _from_=oper_data.get('from'))

        self.assertIsInstance(oper, Operation)
        self.assertEqual(oper.oper_id, oper_data['id'])
        self.assertEqual(oper.oper_date_, oper_data['date'])
        self.assertEqual(oper.transw_state, oper_data['description'])
        self.assertEqual(oper.operation_amount, oper_data['operationAmount'])
        self.assertEqual(oper.description_type, oper_data["description"])
        self.assertEqual(oper._to_, oper_data['to'])
        self.assertEqual(oper._from_, oper_data.get('from'))

        self.assertEqual(str(oper),
                         f"Operation(id={oper_data['id']}, date={oper_data['date']}, description={oper_data['description']}, operationAmount={oper_data['operationAmount']}, to={oper_data['to']}, from={oper_data.get('from')})")
