import pytest
import shutil
from src.csv_wizard import CSVWizard


# the last methods that will run as part of this tests,
# will overwrite the test_file. So we first make a copy from a backup file,
shutil.copyfile("tests/test_file_backup.csv", "tests/test_file.csv")


@pytest.fixture
def test_file():
    _test_file = CSVWizard(source="test_file", path="tests/")
    return _test_file

@pytest.fixture
def test_file_empty():
    _test_file_empty = CSVWizard(source="empty", path="tests/")
    return _test_file_empty

@pytest.fixture
def test_file_with_dups():
    _test_file_with_dups = CSVWizard(source="test_file_with_dups", path="tests/")
    return _test_file_with_dups

@pytest.fixture
def test_file_diff():
    _test_file_diff = CSVWizard(source="test_file_diff", path="tests/")
    return _test_file_diff