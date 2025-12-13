from flask import Blueprint, request, jsonify
import validators
import models
import required
import sqlite3

check = Blueprint("check", __name__)


@check.route("/sign_in", methods=['POST'])
def control():
    """
    Returns instructions for the front end UI
    """
    data = request.get_json()

    student_id = data.get("student_id")

    if not validators.is_valid_id(student_id):
        return jsonify({"status": "student id is invalid"}), 400

    has_profile = models.search_student(student_id=student_id, student_last_name=None)

    if has_profile:
        has_session = models.has_active_session(student_id)
        if has_session:
            return jsonify({"status": "active"}), 200
        return jsonify({"status": "inactive"}), 200

    return jsonify({"status": "no_profile"}), 404


@check.route("/checkin", methods=['POST'])
def login():
    """
    Logs in student if profile exists in studets table.
    """

    data = request.get_json()

    if not validators.require_fields(data, required.SESSIONS_REQUIRED):
        return jsonify({"status": "incorrect or missing key/value"}), 400

    student_id = data.get("student_id")
    tutor_last_name = data.get("tutor_last_name")

    if not validators.is_valid_id(student_id):
        return jsonify({"status": "student id is invalid"}), 400
    if not validators.tutor_exists(tutor_last_name):
        return jsonify({"status": "tutor does not exist"}), 404

    if models.has_active_session(student_id):
        return jsonify({"status": "already checked in"}), 409

    try:
        models.create_session(student_id, tutor_last_name)
    except sqlite3.IntegrityError:
        return jsonify({"status": "student does not exist"}), 404

    return jsonify({"status": "session created"}), 201


@check.route("/checkout", methods=['POST'])
def logout():
    """
    Logs out student using student_id.
    """

    data = request.get_json()

    student_id = data.get("student_id")

    if not validators.is_valid_id(student_id):
        return jsonify({"status": "student id is invalid"}), 400

    if not models.has_active_session(student_id):
        return jsonify({"status": "no active session"}), 409

    result = models.close_session(student_id)

    if not result:
        return jsonify({"status": "no session was closed"}), 500

    return jsonify({"status": "session closed"}), 200


@check.route("/student_form", methods=['POST'])
def insert_student():
    """
    Receives student data from submission form and creates a new student profile.
    """

    data = request.get_json()

    if not validators.require_fields(data, required.STUDENTS_REQUIRED):
        return jsonify({"message": "incorrect or missing key/value"}), 400

    student_id = data.get("student_id")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    major = data.get("major")
    email = data.get("email")

    if not validators.is_valid_id(student_id):
        return jsonify({"status": "student id is invalid"}), 400

    if not validators.is_valid_email(email):
        return jsonify({"status": "student email is invalid"}), 400

    if not validators.is_valid_major(major, required.VALID_MAJORS):
        return jsonify({"status": "student major is invalid"}), 400

    models.create_student(student_id, first_name, last_name, major, email)

    return jsonify({"status": "student successfully inserted"}), 201
