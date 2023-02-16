from .test_misc import test_file

# get headers tests
def test_get_headers_type_is_list():
    headers = test_file.get_headers()
    assert type(headers) == list

def test_get_headers_elems_types_is_string():
    headers = test_file.get_headers()
    for elem in headers:
        assert type(elem) == str

def test_get_headers():
    headers = test_file.get_headers()
    assert headers == ["Name","Work Email"]

# test get_all_rows()
def test_get_all_rows_type_is_list():
    result = test_file.get_all_rows()
    assert type(result) == list

def test_get_all_rows_element_type_is_list():
    result = test_file.get_all_rows()
    for elem in result:
        assert type(elem) == list

def test_get_all_rows_element_type_child_is_string():
    result = test_file.get_all_rows()
    for elem in result:
        for child in elem:
            assert type(child) == str

def test_get_all_rows():
    all_rows = test_file.get_all_rows()
    assert len(all_rows) == 9