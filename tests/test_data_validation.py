# tests/test_user_validation.py

import pytest
from utils.test_data import (
    validate_user,
    VALID_USER,
    INVALID_USER,
    EMPTY_USER,
    PARTIAL_USER,
)

# Individual tests
def test_valid_user():
    assert validate_user(VALID_USER) == "Valid user"

def test_invalid_user():
    assert validate_user(INVALID_USER) == "Invalid user"

def test_empty_user():
    assert validate_user(EMPTY_USER) == "Empty credentials"

def test_partial_user():
    assert validate_user(PARTIAL_USER) == "Partial credentials"


# Practicing FOR loop
def test_validate_all_users_with_for_loop():
    test_cases = [
        (VALID_USER, "Valid user"),
        (INVALID_USER, "Invalid user"),
        (EMPTY_USER, "Empty credentials"),
        (PARTIAL_USER, "Partial credentials"),
    ]

    for user, expected in test_cases:
        result = validate_user(user)
        assert result == expected, f"Failed for user: {user}"


# Practicing WHILE loop (Retry simulation)
def test_retry_login_simulation_with_while_loop():
    attempts = 0
    max_retries = 3
    login_successful = False

    while attempts < max_retries and not login_successful:
        attempts += 1
        status = validate_user(VALID_USER)
        if status == "Valid user":
            login_successful = True

    assert login_successful is True
    assert attempts == 1

