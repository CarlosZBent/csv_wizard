from ..csv_parser import CSVParser

test_file = CSVParser('everyone 248')
test_file_no_dups = CSVParser('everyone 246')

# test get_duplicates

def test_get_duplicates_returns_dict():
    dups = test_file.get_duplicates()
    assert type(dups) == dict

def test_get_duplicates_dict_values_are_int():
    dups = test_file.get_duplicates()
    for k, v in dups.items():
        assert type(v) == int

def test_get_duplicates_dict_keys_are_strings():
    dups = test_file.get_duplicates()
    for k, v in dups.items():
        assert type(k) == str

def test_get_duplicates_on_file_without_duplicates():
    dups = test_file_no_dups.get_duplicates()
    assert dups == {"Result": "No duplicate rows in the file"}

def test_get_duplicates():
    dups = test_file.get_duplicates()
    assert dups == {"[' ']": 3}
