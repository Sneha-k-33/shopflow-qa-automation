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
    if user == VALID_USER:
        return "Valid user"
    elif user == INVALID_USER:
        return "Invalid user"
    else:
        return "Unknown user"