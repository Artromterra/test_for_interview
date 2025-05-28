import pytest
import os
from main import DataHandler


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