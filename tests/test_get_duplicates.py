import pytest

# test get_duplicates


def test_get_duplicates_returns_dict(test_file_with_dups):
    dups = test_file_with_dups.get_duplicates()
    assert type(dups) == dict


def test_get_duplicates_dict_values_are_int(test_file_with_dups):
    dups = test_file_with_dups.get_duplicates()
    for k, v in dups.items():
        assert type(v) == int


def test_get_duplicates_dict_keys_are_strings(test_file_with_dups):
    dups = test_file_with_dups.get_duplicates()
    for k, v in dups.items():
        assert type(k) == str


def test_get_duplicates_on_file_without_duplicates(test_file):
    dups = test_file.get_duplicates()
    assert dups == {"Result": "No duplicate rows in the file"}


def test_get_duplicates(test_file_with_dups):
    dups = test_file_with_dups.get_duplicates()
    assert dups == {
        "['Bastian', 'bastian@yahoo.com']": 3,
        "['Eva', 'eva@gmail.com']": 2,
    }
