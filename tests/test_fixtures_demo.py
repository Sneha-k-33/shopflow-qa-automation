# tests/test_fixtures_demo.py

import pytest

def test_users_fixture_integration(users_data):
    """Verify users data is correctly injected via conftest fixture."""
    assert "valid_user" in users_data
    assert users_data["valid_user"]["username"] == "standard_user"


def test_products_fixture_integration(products_data):
    """Verify products data is correctly injected via conftest fixture."""
    assert "featured_product" in products_data
    assert products_data["featured_product"]["price"] == 29.99


def test_payments_fixture_integration(payments_data):
    """Verify payments data is correctly injected via conftest fixture."""
    assert "valid_card" in payments_data
    assert payments_data["valid_card"]["cvv"] == "123"


def test_teardown_lifecycle_simulation(db_connection_simulation):
    """Verify that fixture setup and yield teardown execute correctly."""
    assert db_connection_simulation["status"] == "CONNECTED"
    assert db_connection_simulation["env"] == "sandbox"