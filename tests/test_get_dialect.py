from .test_misc import test_file

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
