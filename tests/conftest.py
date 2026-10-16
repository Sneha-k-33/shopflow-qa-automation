# tests/conftest.py

import pytest
from utils.file_reader import load_json_data

@pytest.fixture(scope="session")
def users_data():
    """Fixture to load user test data from JSON."""
    return load_json_data("test_data/users.json")


@pytest.fixture(scope="session")
def products_data():
    """Fixture to load product test data from JSON."""
    return load_json_data("test_data/products.json")


@pytest.fixture(scope="session")
def payments_data():
    """Fixture to load payment test data from JSON."""
    return load_json_data("test_data/payments.json")


@pytest.fixture
def db_connection_simulation():
    """
    Demonstrates Pytest setup and teardown using yield.
    Code before yield runs during setup; code after yield runs during teardown.
    """
    print("\n[SETUP] Connecting to test database...")
    db_connection = {"status": "CONNECTED", "env": "sandbox"}
    
    yield db_connection  # Provides the resource to the test function
    
    print("\n[TEARDOWN] Closing test database connection...")
    db_connection["status"] = "DISCONNECTED"