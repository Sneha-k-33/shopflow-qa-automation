# tests/unit/test_payment_unit.py

import pytest

@pytest.mark.smoke
def test_valid_payment_amount():
    """Verify that a positive payment amount is valid."""
    assert 100 > 0


@pytest.mark.smoke
def test_invalid_payment_amount():
    """Verify that a negative or zero payment amount is invalid."""
    assert -1 <= 0


# Parametrization: Run this single test function against 4 different data sets automatically!
@pytest.mark.payment
@pytest.mark.parametrize("amount, expected_valid", [
    (150.00, True),
    (0.01, True),
    (0.00, False),
    (-25.50, False)
])
def test_payment_boundary_amounts(amount, expected_valid):
    """Data-driven test validating various payment amount boundaries."""
    is_valid = amount > 0
    assert is_valid == expected_valid