import pytest

# encoding tests


def test_get_encoding_returns_string(test_file):
    enc = test_file.get_encoding()
    assert type(enc) == str


def test_get_encoding(test_file):
    enc = test_file.get_encoding()
    assert enc == "ascii"
