import pytest


# test get_all_rows()

def test_get_all_rows_type_is_list(test_file):
    result = test_file.get_all_rows()
    assert type(result) == list


def test_get_all_rows_element_type_is_list(test_file):
    result = test_file.get_all_rows()
    for elem in result:
        assert type(elem) == list


def test_get_all_rows_element_type_child_is_string(test_file):
    result = test_file.get_all_rows()
    for elem in result:
        for child in elem:
            assert type(child) == str


def test_get_all_rows(test_file):
    all_rows = test_file.get_all_rows()
    assert len(all_rows) == 12
