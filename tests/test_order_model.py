# tests/test_order_model.py

import pytest
from utils.order_model import (
    calculate_order_total,
    validate_order,
    update_order_status
)

@pytest.fixture
def sample_order():
    """Fixture providing a standard order dictionary for tests."""
    return {
        "order_id": "ORD-1001",
        "customer_email": "sneha@example.com",
        "items": [
            {"name": "Backpack", "price": 29.99, "quantity": 2},
            {"name": "Bike Light", "price": 9.99, "quantity": 1}
        ],
        "status": "PENDING"
    }


def test_calculate_order_total(sample_order):
    # Subtotal: (29.99 * 2) + (9.99 * 1) = 69.97
    # Total with 8% tax: 69.97 + (69.97 * 0.08) = 75.5676 -> 75.57
    total = calculate_order_total(sample_order["items"])
    assert total == 75.57


def test_calculate_order_total_with_discount(sample_order):
    # 10% discount on 69.97 subtotal = 62.973
    # Total with 8% tax: 68.01
    total = calculate_order_total(sample_order["items"], discount_percent=10)
    assert total == 68.01


def test_validate_order_success(sample_order):
    assert validate_order(sample_order) == "VALID"


def test_validate_order_missing_fields(sample_order):
    sample_order["customer_email"] = ""
    assert validate_order(sample_order) == "INVALID_MISSING_FIELDS"


def test_validate_order_empty_items(sample_order):
    sample_order["items"] = []
    assert validate_order(sample_order) == "INVALID_EMPTY_ITEMS"


def test_order_status_transitions(sample_order):
    # Test valid transition: PENDING -> PROCESSING
    assert update_order_status(sample_order, "PROCESSING") is True
    assert sample_order["status"] == "PROCESSING"

    # Test valid transition: PROCESSING -> COMPLETED
    assert update_order_status(sample_order, "COMPLETED") is True
    assert sample_order["status"] == "COMPLETED"

    # Test invalid transition: COMPLETED -> PENDING
    assert update_order_status(sample_order, "PENDING") is False
    assert sample_order["status"] == "COMPLETED"
