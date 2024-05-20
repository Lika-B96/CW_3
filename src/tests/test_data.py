from src.app.models.data import get_data
from src.app.models.operation import Operation
from src.settings import PATH_WITH_FIXTURES


def test_get_data():
    data = get_data(PATH_WITH_FIXTURES)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)

def test_numbers_masking():
    number_1 = Operation
    assert number_1.numbers_masking('1596837868705199') == '1596 83** **** 5199'

