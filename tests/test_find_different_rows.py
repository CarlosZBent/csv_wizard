from pytest import raises

from .test_misc import test_file, test_file2

# test find_different_rows()

def test_find_different_rows_returns_list():
    common = test_file.find_different_rows(test_file2)
    assert type(common) == list

def test_find_different_rows():
    common = test_file.find_different_rows(test_file2)
    assert common == []

def test_find_different_rows_incorrect_argument_type():
    with raises(AttributeError):
        test_file.find_different_rows(['dummy list'])