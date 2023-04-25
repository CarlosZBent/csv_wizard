from pytest import raises

from .test_misc import test_file, test_file2

# test find_common_rows()


def test_find_common_rows_returns_list():
    common = test_file.find_common_rows(test_file2, "utf-8")
    assert type(common) == list


def test_find_common_rows_is_same_when_files_reversed():
    common0 = test_file.find_common_rows(test_file2, "utf-8")
    common1 = test_file2.find_common_rows(test_file, "utf-8")
    assert len(common0) == len(common1)


def test_find_common_rows_incorrect_argument_type():
    with raises(AttributeError):
        test_file.find_common_rows(["dummy list"], "utf-8")
