from .test_misc import test_file
# encoding tests

def test_get_encoding_returns_string():
    enc = test_file.get_encoding()
    assert type(enc) == str

def test_get_encoding():
    enc = test_file.get_encoding()
    assert enc == 'UTF-8-SIG'