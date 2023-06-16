import pytest


# test divide()

def test_divide_raises_error_for_float_argument(test_file):
    with pytest.raises(TypeError):
        test_file.divide(4.5)


def test_divide_raises_error_for_number_of_parts_greater_than_row_count(test_file):
    with pytest.raises(IndexError):
        test_file.divide(300)


def test_divide_type_is_list(test_file):
    parts = test_file.divide(4)
    assert type(parts) == list


def test_divide_elem_type_is_list(test_file):
    parts = test_file.divide(4)
    for elem in parts:
        assert type(elem) == list


def test_divide(test_file):
    parts = test_file.divide(3)
    for elem in parts:
        assert len(elem) <= 4
