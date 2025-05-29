import pytest
import os
from main import DataHandler, main


@pytest.fixture
def get_object():
    file = [os.path.abspath('data/data1.csv')]
    title = 'payout'
    obj = DataHandler(file, title)
    return obj


def test_reader(get_object):
    result = get_object._reader([os.path.abspath('data/data1.csv')])
    assert 'Alice Johnson' in result
    assert type(result) is str


def test_payout(get_object):
    result = get_object.payout()
    name = result[0].get('name')
    payout = result[0].get('payout')
    assert name == 'Alice Johnson'
    assert payout == '8000'


def test_output(get_object):
    result = get_object.print_console()
    assert type(result) is str


def test_main():
    test_args_without_title = 'main.py data1.csv data2.csv data3.csv'.split(' ')
    test_args_incorrect_type = 'main.py data1.csv data2.csv data3.jpg --report payout'.split(' ')
    test_correct = 'main.py data1.csv data2.csv data3.csv --report payout'.split(' ')
    result_1 = main(test_args_without_title)
    result_2 = main(test_args_incorrect_type)
    result_3 = main(test_correct)
    assert isinstance(result_1, ValueError)
    assert isinstance(result_2, TypeError)
    assert isinstance(result_3, DataHandler)
