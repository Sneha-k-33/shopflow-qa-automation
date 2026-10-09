# utils/test_data.py

VALID_USER = {
    "username": "standard_user",
    "password": "secret_sauce",
}

INVALID_USER = {
    "username": "invalid_user",
    "password": "wrong_password",
}

EMPTY_USER = {
    "username": "",
    "password": "",
}

PARTIAL_USER = {
    "username": "standard_user",
    "password": "",
}

def validate_user(user):
    # Using 'and' logic to check conditions
    if not user["username"] and not user["password"]:
        return "Empty credentials"
    elif user["username"] == "standard_user" and user["password"] == "secret_sauce":
        return "Valid user"
    elif user["username"] and not user["password"]:
        return "Partial credentials"
    else:
        return "Invalid user"
