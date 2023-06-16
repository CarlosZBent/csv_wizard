import pytest


# get headers tests
def test_get_headers_type_is_list(test_file):
    headers = test_file.get_headers()
    assert type(headers) == list


def test_get_headers_elems_types_is_string(test_file):
    headers = test_file.get_headers()
    for elem in headers:
        assert type(elem) == str


def test_get_headers(test_file):
    headers = test_file.get_headers()
    assert headers == ["name", "email"]
