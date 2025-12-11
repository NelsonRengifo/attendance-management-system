# This code is responsible for:

# 1. models.py loads SQL files
# 2. Functions to perform queries (using the SQL files)
# 3. returning raw query result


import database
import sqlite3


def create_tables() -> None:
    """
    Creates 3 main tables: students, tutors, sessions.
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("schema")
    cursor.executescript(sql)
    connection.commit()


def load_sql(filename) -> str:
    """
    Extracts the SQL commands from a file

    :param filename: name of the .sql file

    :rtype: SQL command(s)
    """
    filepath = f"sql/{filename}.sql"
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def create_student(student_id, first_name, last_name, major, email) -> None:
    """
    Inserts a new student into the students table.
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("create_student")
    cursor.execute(sql, (student_id, first_name, last_name, major, email))
    connection.commit()


def create_tutor(tutor_id, tutor_last_name, subject_area, major) -> None:
    """
    Inserts a new tutor into the tutors table.
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("create_tutor")
    cursor.execute(sql, (tutor_id, tutor_last_name, subject_area, major))
    connection.commit()


def search_user(username) -> bool:
    """
    Checks if username valid.

    :rtype: int (0 or 1)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("search_user")
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    return result[0]


def search_tutor(tutor_last_name) -> bool:
    """
    Checks if a tutor exists in tutors table.

    :rtype: int (0 or 1)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("search_tutor")
    cursor.execute(sql, (tutor_last_name,))
    result = cursor.fetchone()
    return result[0]


def search_student(student_id=None, student_last_name=None) -> bool:
    """
    Checks if a student exists.

    :rtype: int (0 or 1)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("search_student")
    cursor.execute(sql, (student_id, student_last_name))
    result = cursor.fetchone()
    return result[0]


def get_student(student_id) -> sqlite3.Row | None:
    """
    Returns a single row with all the student data.

    :return: Row object (Dict & Tuple)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("get_student_by_id")
    cursor.execute(sql, (student_id,))
    return cursor.fetchone()


def get_user_id(username) -> sqlite3.Row | None:
    """
    Returns user_id.

    :return: Row object (Dict & Tuple)
    """

    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("get_user_id")
    cursor.execute(sql, (username,))
    return cursor.fetchone()


def get_user_password(username) -> sqlite3.Row | None:
    """
    Finds the password_hash of user.

    :return: Row object (Dict & Tuple)
    """

    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("get_user_password")
    cursor.execute(sql, (username,))
    return cursor.fetchone()


def create_session(student_id, tutor_last_name) -> None:
    """
    Inserts an unfinished/active session for student.
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("create_session")
    cursor.execute(sql, (student_id, tutor_last_name))
    connection.commit()


def create_session_token(session_id, user_id) -> None:
    """
    Inserts a new session_id for the user.
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("create_session_id")
    cursor.execute(sql, (session_id, user_id))
    connection.commit()


def close_session(student_id) -> int:
    """
    Closes a session if it exists.

    :rtype: int (0 = nothing updated, 1 = at least one row updated)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("close_session")
    cursor.execute(sql, (student_id,))
    return cursor.rowcount()


def close_session_id(session_id) -> int:
    """
    Deletes a row for a given session_id.

    :rtype: int (0 = no rows deleted, 1 = at least one row deleted)
    """

    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("close_session_id")
    cursor.execute(sql, (session_id,))
    return cursor.rowcount()


def has_active_session(student_id) -> bool:
    """
    Confirms if an active session exists.

    :rtype: bool (0 or 1)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("has_active_session")
    cursor.execute(sql, (student_id,))
    result = cursor.fetchone()
    return result[0]


def has_expired(session_id) -> bool:
    """
    Validates the session_id token.

    :rtype: bool (0 or 1)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("validate_session_id")
    cursor.execute(sql, (session_id,))
    result = cursor.fetchone()
    return result[0]


def has_session_id(session_id) -> bool:
    """
    Validates a session id.

    :rtype: bool (0 or 1)
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("search_session_id")
    cursor.execute(sql, (session_id,))
    result = cursor.fetchone()
    return result[0]
