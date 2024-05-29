from src.app.data import get_data, delete_empty_operations, get_first_five_sorted_operations
from src.app.operation import Operation
from settings import PATH_WITH_FIXTURES

data = get_data(PATH_WITH_FIXTURES)

new_data = delete_empty_operations(data)

five_operations = get_first_five_sorted_operations(new_data)

for oper in five_operations:
    oper = Operation(oper_id=oper['id'],
                     oper_date_=oper['date'],
                     transw_state=oper['description'],
                     operation_amount=oper['operationAmount'],
                     description_type=oper["description"],
                    _to_=oper['to'],
                    _from_=oper.get('from'))
    print(oper)

def main():
    pass

if __name__ == '__main__':
    main()