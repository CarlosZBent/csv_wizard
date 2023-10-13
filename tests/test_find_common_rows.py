import pytest

# test find_common_rows()


def test_find_common_rows_returns_list(test_file, test_file_diff):
    common = test_file.find_common_rows(test_file_diff)
    assert type(common) == list


def test_find_common_rows_is_same_when_files_reversed(test_file, test_file_diff):
    common0 = test_file.find_common_rows(test_file_diff)
    common1 = test_file_diff.find_common_rows(test_file)
    assert len(common0) == len(common1)


def test_find_common_rows_incorrect_argument_type(test_file):
    with pytest.raises(AttributeError):
        test_file.find_common_rows(["dummy list"])


def test_find_common_rows_doesnt_return_file_headers(test_file, test_file_diff):
    common = test_file.find_common_rows(test_file_diff)
    headers0 = test_file.get_all_rows()[0]
    headers1 = test_file_diff.get_all_rows()[0]
    assert common[0] != headers0 and common[0] != headers1
