import pytest
from src.csv_wizard import CSVWizard

@pytest.fixture
def create_csvwizard_fixture_for_tests():
    test_file = CSVWizard("test_file")
    return test_file

@pytest.fixture
def create_empty_csvwizard_fixture_for_tests():
    empty_test_file = CSVWizard("empty")
    return empty_test_file