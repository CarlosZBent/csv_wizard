from .test_misc import test_file

# test slice()
def test_slice_type_is_dict():
    parts = test_file.slice()
    assert type(parts) == dict

def test_slice():
    parts = test_file.slice()
    assert len(parts['First_Half']) == 123 and len(parts['Second_Half']) == 123