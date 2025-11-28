# This code is responsible for:

# 1. models.py loads SQL files
# 2. Functions to perform queries (using the SQL files)
# 3. returning raw query result

# talk to the database
# load the SQL files
# return the raw database results

import database


def create_tables():
    """
    Creates 3 main tables: students, tutors, sessions
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("schema")
    cursor.execute(sql)  # use cursor.executescript() once you do all 3 tables
    connection.commit()


def load_sql(filename):
    """
    Extracts the SQL commands from a file

    :param filename: name of the .sql file
    """
    filepath = f"sql/{filename}.sql"
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def create_student(student_id, first_name, last_name, major, email):
    """
    Inserts a new student into the students table
    """
    connection = database.get_db()
    cursor = connection.cursor()
    sql = load_sql("create_student")
    cursor.execute(sql, (student_id, first_name, last_name, major, email))
    connection.commit()
