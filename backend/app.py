# This code is responsible for:

# 1. Creating Flask app
# 2. Registering blueprints/routes
# 3. Loading database
# 4. Starting server


from flask import Flask, request, jsonify
import database
import models
import click


app = Flask(__name__)
app.config['DATABASE'] = "attendance.db"


@app.route("/insert_student", methods=['POST'])
def insert_student():
    data = request.get_json()

    student_id = data['student_id']
    first_name = data['first_name']
    last_name = data['last_name']
    major = data['major']
    email = data['email']

    models.create_student(student_id, first_name, last_name, major, email)


@app.cli.command("create_tables")
def create_command():
    models.create_tables()
    click.echo("Database initialized.")


app.teardown_appcontext(database.close_db)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
