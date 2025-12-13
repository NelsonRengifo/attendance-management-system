# These all evaluate to False
# None
# ""
# []
# {}
# 0
# False


# REFACTOR: Proper function type annotations.

from email_validator import validate_email, EmailNotValidError
from flask import request
import models


def require_fields(data, required) -> bool:
    """
    Confirms that each required key is present and its value is not empty.
    """
    for key in required:
        if not data.get(key, None):
            return False
    return True


def is_valid_id(id_number) -> bool:
    """
    Validates school ID.
    """
    required_school_id_length = 9

    id_length = len(id_number)
    if id_length != required_school_id_length:
        return False

    try:
        int(id_number)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_phone_number(phone_number) -> tuple:
    """
    Docstring for is_valid_phone_number

    :param phone_number: A 10 digit sequence of digits.
    """

    has_letters = any((char.isalpha() for char in phone_number))
    if has_letters:
        return (False, "Phone number cannot have letters.")

    PHONE_FORMATTING_CHARS = [" ", "-", "(", ")", ".", "+", "\t", "\n"]

    # scan and remove special characters
    clean_number = "".join(char for char in phone_number if char not in PHONE_FORMATTING_CHARS)

    if not clean_number.isdigit():
        return (False, "Phone number contains invalid symbols.")

    if len(clean_number) != 10:
        return (False, "Phone number must be exatcly 10 digits (123 456 7890).")

    return (True, clean_number)


def is_valid_email(email) -> bool:
    """
    Confirms that email is valid.
    """
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


def is_strong_password(plain_password, first_name, last_name, username) -> tuple:
    """
    Validates password strength. Returns True if strong, otherwise returns a string message describing the weakness.
    """
    has_number = False
    has_letter = False
    plain_password_lowered = plain_password.lower()

    MIN_PASSWORD_LENGTH = 8

    COMMON_WEAK_PASSWORDS = [
        "password", "password1", "password123", "pass123", "admin", "admin123",
        "administrator", "root", "letmein", "welcome", "welcome1", "welcome123",
        "qwerty", "qwerty1", "qwerty123", "abc123", "abcd1234", "123456", "1234567",
        "12345678", "123456789", "1234567890", "000000", "111111", "11111111",
        "121212", "654321", "iloveyou", "monkey", "dragon", "sunshine", "football",
        "baseball", "princess", "computer", "shadow", "superman", "pokemon",
        "charlie", "daniel", "michael", "ashley", "buster", "soccer", "loveme",
        "trustno1", "starwars", "whatever", "hello", "hello123", "purple",
        "killer", "jordan", "jordan23", "harley", "cheese", "test", "test123",
        "temp", "default", "changeme"
    ]

    # Password is too easy/common.
    if plain_password_lowered in COMMON_WEAK_PASSWORDS:
        return (False, "Password is too common; choose something more unique.")
    # Password too short.
    if len(plain_password_lowered) < MIN_PASSWORD_LENGTH:
        return (False, "Password is too short (minimum 8 characters).")
    # Password needs at least 1 letter and 1 number.
    has_number = any(ch.isdigit() for ch in plain_password)
    has_letter = any(ch.isalpha() for ch in plain_password)

    if not has_number or not has_letter:
        return (False, "Password must contain at least 1 letter and 1 number.")
    # Password is too obvious.
    if plain_password_lowered in first_name.lower() or plain_password_lowered in last_name.lower() or plain_password_lowered in username.lower():
        return (False, "Password cannot contain your first name, last name, or username.")
    # Password is strong.
    return (True, "All good.")


def is_valid_major(major, valid_majors) -> bool:
    """
    Confirms that student major is valid (depends on school).
    """
    return major in valid_majors


def get_token() -> str | None:
    """
    Validates Authorization header and returns the token if valid.
    """

    # Missing key or value.
    header = request.headers.get("Authorization")

    if not header:
        return None

    # We don't have exatcly 2 values ("Bearer", "Token").
    value_list = header.split()
    if len(value_list) != 2:
        return None

    # The value is not "Bearer".
    if value_list[0] != "Bearer":
        return None

    # Missing token.
    if not value_list[1]:
        return None

    # Everything is valid and ready.
    return value_list[1]
