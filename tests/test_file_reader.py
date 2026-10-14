# tests/test_file_reader.py

import pytest
from utils.file_reader import load_json_data

def test_load_users_json():
    data = load_json_data("test_data/users.json")
    assert "valid_user" in data
    assert data["valid_user"]["username"] == "standard_user"


def test_load_products_json():
    data = load_json_data("test_data/products.json")
    assert "featured_product" in data
    assert data["featured_product"]["price"] == 29.99


def test_load_payments_json():
    data = load_json_data("test_data/payments.json")
    assert "valid_card" in data
    assert data["valid_card"]["cvv"] == "123"


def test_file_not_found_exception():
    with pytest.raises(FileNotFoundError):
        load_json_data("test_data/non_existent_file.json")