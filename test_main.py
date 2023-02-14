from pytest import raises

from main import FileReader

test_file = FileReader('')
test_file2 = FileReader('')

# encoding tests

def test_get_encoding_returns_string():
    enc = test_file.get_encoding()
    assert type(enc) == str

def test_get_encoding():
    enc = test_file.get_encoding()
    assert enc == 'ascii'

# dialect tests
def test_get_dialect_type_is_object():
    dialect = test_file.get_dialect()
    assert type(dialect) == type

def test_delimiter_type_is_string():
    delimiter = test_file.get_dialect().delimiter
    assert type(delimiter) == str

def test_quoting_type_is_int():
    quoting = test_file.get_dialect().quoting
    assert type(quoting) == int

def test_doublequote_type_is_bool():
    doublequote = test_file.get_dialect().doublequote
    assert type(doublequote) == bool

def test_lineterminator_type_is_string():
    lineterminator = test_file.get_dialect().lineterminator
    assert type(lineterminator) == str

def test_quotechar_type_is_string():
    quotechar = test_file.get_dialect().quotechar
    assert type(quotechar) == str

def test_skipinitialspace_type_is_bool():
    skipinitialspace = test_file.get_dialect().skipinitialspace
    assert type(skipinitialspace) == bool

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

# test slice()

def test_slice_type_is_dict():
    parts = test_file.slice()
    assert type(parts) == dict

def test_slice():
    parts = test_file.slice()
    assert len(parts['First_Half']) == 5 and len(parts['Second_Half']) == 4

# test find_common_rows()

def test_find_common_rows_returns_list():
    common = test_file.find_common_rows(test_file2)
    assert type(common) == list

def test_find_common_rows():
    common = test_file.find_common_rows(test_file2)
    assert common == [['Wade, Amber', 'amber@firstduesizeup.com'], ['Williams, Michael', 'michael.williams@firstdue.com'], ['Williams, Stephen', 'stephen@firstduesizeup.com'], ['York, Todd', 'todd.york@firstdue.com'], ['Young, Brandon', 'brandon.young@firstdue.com'], ['Zeller, Phill', 'phil.zeller@firstdue.com']]

def test_find_common_rows_incorrect_argument_type():
    with raises(AttributeError):
        test_file.find_common_rows(['dummy list'])

# test find_different_rows()

def test_find_different_rows_returns_list():
    common = test_file.find_different_rows(test_file2)
    assert type(common) == list

def test_find_different_rows():
    common = test_file.find_different_rows(test_file2)
    assert common == [['Name', 'Work Email'], ['Madeline Lorch', 'madeline.lorch@firstdue.com'], ['Alex Faust', 'alex.faust@firstdue.com ']]

def test_find_different_rows_incorrect_argument_type():
    with raises(AttributeError):
        test_file.find_different_rows(['dummy list'])

# test divide()

def test_divide_raises_error_for_float_argument():
    with raises(TypeError):
        test_file.divide(4.5)

def test_divide_raises_error_for_number_of_parts_greater_than_row_count():
    with raises(IndexError):
        test_file.divide(95)

def test_divide_type_is_list():
    parts = test_file.divide(4)
    assert type(parts) == list

def test_divide_elem_type_is_list():
    parts = test_file.divide(4)
    for elem in parts:
        assert type(elem) == list

def test_divide():
  parts = test_file.divide(3)
  for elem in parts:
      assert len(elem) <= 3

# test_write_headers()

def test_write_headers():
    new_headers = ["NAME","EMAIL"]
    test_file.write_headers(new_headers)
    assert test_file.get_headers() == new_headers

# test overwrite

def test_overwrite():
    new_body = [
        ['name1','email1'], 
        ['name2','email2']
    ]
    test_file.overwrite(new_body)
    assert test_file.get_all_rows() == new_body

# test append

def test_append_rows():
    rows = [
        ['name1','email1'], 
        ['name2','email2']
    ]
    test_file.append_rows(rows)
    assert test_file.get_all_rows()[:-2] == rows

def test_append_rows_at_top_of_file():
    rows = [
        ['name1','email1'], 
        ['name2','email2']
    ]
    test_file.append_rows(rows, True)
    assert test_file.get_all_rows()[1:3] == [['name2','email2'], ['name1','email1']]