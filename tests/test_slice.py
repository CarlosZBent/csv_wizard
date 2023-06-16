import pytest


# test slice()

def test_slice_type_is_dict(test_file):
    parts = test_file.slice()
    assert type(parts) == dict


def test_slice(test_file):
    parts = test_file.slice()
    half = int(test_file.get_row_count() / 2)
    assert len(parts["First_Half"]) <= half and len(parts["Second_Half"]) >= half
