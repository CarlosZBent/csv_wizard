from .test_misc import test_file


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
    assert len(all_rows) == 248
