import pytest


# test find_different_rows()

def test_find_different_rows_returns_list(test_file, test_file_diff):
    diff = test_file.find_different_rows(test_file_diff)
    assert type(diff) == list


def test_find_different_rows(test_file, test_file_diff):
    diff = test_file_diff.find_different_rows(test_file)
    # diff results don't have an established order
    assert diff == [('Samira', 'samira@protonmail.com'), ('Manuel', 'manuel@hotmail.com')] or diff == [('Manuel', 'manuel@hotmail.com'), ('Samira', 'samira@protonmail.com')]


def test_find_different_rows_incorrect_argument_type(test_file):
    with pytest.raises(AttributeError):
        test_file.find_different_rows(["dummy list"])
