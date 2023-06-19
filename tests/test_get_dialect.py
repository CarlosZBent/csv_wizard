import pytest

# dialect tests


def test_get_dialect_type_is_object(test_file):
    dialect = test_file.get_dialect()
    assert type(dialect) == type


def test_delimiter_type_is_string(test_file):
    delimiter = test_file.get_dialect().delimiter
    assert type(delimiter) == str


def test_quoting_type_is_int(test_file):
    quoting = test_file.get_dialect().quoting
    assert type(quoting) == int


def test_doublequote_type_is_bool(test_file):
    doublequote = test_file.get_dialect().doublequote
    assert type(doublequote) == bool


def test_lineterminator_type_is_string(test_file):
    lineterminator = test_file.get_dialect().lineterminator
    assert type(lineterminator) == str


def test_quotechar_type_is_string(test_file):
    quotechar = test_file.get_dialect().quotechar
    assert type(quotechar) == str


def test_skipinitialspace_type_is_bool(test_file):
    skipinitialspace = test_file.get_dialect().skipinitialspace
    assert type(skipinitialspace) == bool
