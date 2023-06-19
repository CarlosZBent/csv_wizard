import pytest

# test empty file


def test_opening_empty_file_returns_attributeerror(test_file_empty):
    with pytest.raises(LookupError):
        test_file_empty.get_headers()


# test delete_blanks


def test_delete_blanks(test_file):
    parser_iterable = []
    e = test_file.delete_blanks()
    rows = test_file.get_all_rows()
    for line in rows:
        parser_iterable.append(line)
    for row in parser_iterable:
        assert all("" != i and not i.isspace() for i in row)


# test_write_headers()


def test_write_headers(test_file):
    new_headers = ["NAMENEW", "EMAILNEW"]
    test_file.write_headers(new_headers)
    assert test_file.get_headers() == new_headers


# test overwrite


def test_overwrite(test_file):
    new_body = [["column1", "column1"], ["column2", "column2"]]
    test_file.overwrite(new_body)
    assert test_file.get_all_rows() == new_body


# test append


def test_append_rows(test_file):
    rows = [["column1", "column1"], ["column2", "column2"]]
    test_file.append_rows(rows)
    assert test_file.get_all_rows()[:-2] == rows


def test_append_rows_at_top_of_file(test_file):
    rows = [["column1", "column1"], ["column2", "column2"]]
    test_file.append_rows(rows, True)
    assert test_file.get_all_rows()[1:3] == [
        ["column2", "column2"],
        ["column1", "column1"],
    ]
