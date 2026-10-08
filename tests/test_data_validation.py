
from utils.test_data import (
    validate_user,
    VALID_USER,
    INVALID_USER,
    EMPTY_USER,
    PARTIAL_USER,
)


def test_valid_user():
    result = validate_user(VALID_USER)

    assert result == "Valid user"


def test_invalid_user():
    result = validate_user(INVALID_USER)

    assert result == "Invalid user"


def test_empty_user():
    result = validate_user(EMPTY_USER)

    assert result == "Unknown user"


def test_partial_user():
    result = validate_user(PARTIAL_USER)

    assert result == "Unknown user"
