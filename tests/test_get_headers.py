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
    assert headers == ["NAME2","EMAIL2"]
