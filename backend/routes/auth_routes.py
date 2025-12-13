# Routes related to logging in or verifying identity:

# /login
# /logout
# /register
# Handles everything related to users signing in or out.


from flask import Blueprint, request, jsonify
import argon2
import models
import logging
import secrets
import validators


auth = Blueprint("auth", __name__)
password_hasher = argon2.PasswordHasher(hash_len=32)
logger = logging.getLogger(__name__)

# REFACTOR ROUTE /user/login: TOO MANY DB REQUESTS. DO ONE AND GET ALL DATA IN THAT QUERY.


@auth.route("/user/login", methods=['POST'])
def validate_username_password():
    """
    Validates credentials and returns a session_id token.
    """
    data = request.get_json()

    username = data.get("username")
    plain_password = data.get("password")

    if not models.search_user(username):
        logger.warning(f"invalid username attempt for {username}")
        return jsonify({"status": "invalid username or password"}), 401

    row_object = models.get_user_password(username)
    password_hash = row_object.get("password_hash")

    try:
        password_hasher.verify(password_hash, plain_password)
    except argon2.exceptions.VerifyMismatchError:
        logger.warning(f"invalid password attempt for {username}")
        return jsonify({"status": "invalid username or password"}), 401
    except (argon2.exceptions.VerificationError, argon2.exceptions.InvalidHashError) as e:
        logger.error(f"internal error: {e}", exc_info=True)
        return jsonify({"status": "internal error"}), 500

    session_id = secrets.token_urlsafe(32)
    row_object = models.get_user_id(username)
    user_id = row_object.get("user_id")
    models.create_session_token(session_id, user_id)
    return jsonify({"session_id": session_id}), 201


@auth.route("/user/logout", methods=['POST'])
def terminate_session():
    """
    Closes a session token.
    """
    token = validators.get_token()
    models.close_session_id(token)
    return jsonify({"status": "session closed"}), 200

# only for the super admin and admin. tutors never hit this


@auth.route("/user/register", methods=['POST'])
def create_account():
    pass
