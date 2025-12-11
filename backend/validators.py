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


def require_fields(data, required):
    """
    Confirms that each required key is present and its value is not empty.
    """
    for key in required:
        if not data.get(key, None):
            return False
    return True


def is_valid_int(id_number):
    """
    Confirms that student_id or tutor_id is a valid integer data type.
    """
    try:
        int(id_number)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_email(student_email):
    """
    Confirms that email is valid.
    """
    try:
        validate_email(student_email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


def is_valid_major(major, valid_majors):
    """
    Confirms that student major is valid (depends on school).
    """
    return major in valid_majors


def get_token() -> str:
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


def student_exists(student_id=None, student_last_name=None):
    """
    Confirms that student exists before inserting a session.
    """
    if student_id is not None:
        return bool(models.search_student(student_id=student_id, student_last_name=None))
    elif student_last_name is not None:
        return bool(models.search_student(student_id=None, student_last_name=student_last_name))
    raise ValueError("Must provide at least of the parameters.")


def tutor_exists(tutor_last_name):
    """
    Confirms that tutor exists before inserting a session.
    """
    if tutor_last_name is not None:
        return bool(models.search_tutor(tutor_last_name))
    raise ValueError("Must provide at least of the parameters.")
