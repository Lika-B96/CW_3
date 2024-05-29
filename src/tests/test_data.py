import unittest
from src.app.data import get_data, get_first_five_sorted_operations, delete_empty_operations


class TestGetData(unittest.TestCase):
    def test_get_data(self):
        path = 'path/to/sample.json'
        sample_data = [
            {'id': 1, 'date': '2022-01-01', 'description': 'Test operation', 'operationAmount': 100.0, 'to': 'Account 1', 'from': 'Account 2'},
            {'id': 2, 'date': '2022-01-02', 'description': 'Test operation 2', 'operationAmount': 200.0, 'to': 'Account 3', 'from': 'Account 4'},

        ]
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(sample_data, file)

        result = get_data(path)
        self.assertEqual(result, sample_data)

        path = 'path/to/non-existent.json'
        with self.assertRaises(FileNotFoundError):
            get_data(path)

class TestDeleteEmptyOperations(unittest.TestCase):
    def test_delete_empty_operations(self):
        operations = [
            {'id': 1, 'date': '2022-01-01', 'description': 'Test operation', 'operationAmount': 100.0, 'to': 'Account 1', 'from': 'Account 2'},
            {'id': 2, 'date': '2022-01-02', 'description': 'Test operation 2', 'operationAmount': 200.0, 'to': 'Account 3', 'from': 'Account 4'},
            {},
            {'id': 3, 'date': '2022-01-03', 'description': 'Test operation 3', 'operationAmount': 300.0, 'to': 'Account 5', 'from': 'Account 6'},
        ]

        result = delete_empty_operations(operations)
        self.assertEqual(result, [
            {'id': 1, 'date': '2022-01-01', 'description': 'Test operation', 'operationAmount': 100.0, 'to': 'Account 1', 'from': 'Account 2'},
            {'id': 2, 'date': '2022-01-02', 'description': 'Test operation 2', 'operationAmount': 200.0, 'to': 'Account 3', 'from': 'Account 4'},
            {'id': 3, 'date': '2022-01-03', 'description': 'Test operation 3', 'operationAmount': 300.0, 'to': 'Account 5', 'from': 'Account 6'},
        ])

class TestGetFirstFiveSortedOperations(unittest.TestCase):
    def test_get_first_five_sorted_operations(self):
        operations = [
            {'id': 3, 'date': '2022-01-03', 'description': 'Test operation 3', 'operationAmount': 300.0, 'to': 'Account 5', 'from': 'Account 6'},
            {'id': 1, 'date': '2022-01-01', 'description': 'Test operation', 'operationAmount': 100.0, 'to': 'Account 1', 'from': 'Account 2'},
            {'id': 4, 'date': '2022-01-04', 'description': 'Test operation 4', 'operationAmount': 400.0, 'to': 'Account 7', 'from': 'Account 8'},
            {'id': 2, 'date': '2022-01-02', 'description': 'Test operation 2', 'operationAmount': 200.0, 'to': 'Account 3', 'from': 'Account 4'},
            {'id': 5, 'date': '2022-01-05', 'description': 'Test operation 5', 'operationAmount': 500.0, 'to': 'Account 9', 'from': 'Account 10'},
        ]

        result = get_first_five_sorted_operations(operations)
        self.assertEqual(result, [
            {'id': 1, 'date': '2022-01-01', 'description': 'Test operation', 'operationAmount': 100.0, 'to': 'Account 1', 'from': 'Account 2'},
            {'id': 2, 'date': '2022-01-02', 'description': 'Test operation 2', 'operationAmount': 200.0, 'to': 'Account 3', 'from': 'Account 4'},
            {'id': 3, 'date': '2022-01-03', 'description': 'Test operation 3', 'operationAmount': 300.0, 'to': 'Account 5', 'from': 'Account 6'},
            {'id': 4, 'date': '2022-01-04', 'description': 'Test operation 4', 'operationAmount': 400.0, 'to': 'Account 7', 'from': 'Account 8'},
            {'id': 5, 'date': '2022-01-05', 'description': 'Test operation 5', 'operationAmount': 500.0, 'to': 'Account 9', 'from': 'Account 10'},
        ])



