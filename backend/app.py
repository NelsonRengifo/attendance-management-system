# This code is responsible for:

# 1. Creating Flask app
# 2. Registering blueprints/routes
# 3. Loading database
# 4. Starting server


from flask import Flask, request, jsonify
from routes.check_routes import check
from routes.auth_routes import auth
import database
import models
import logging

app = Flask(__name__)
app.config['DATABASE'] = "attendance.db"
logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')

app.register_blueprint(auth)
app.register_blueprint(check)


@app.route("/")
def health():
    return "Server is running"


@app.cli.command("create_tables")
def create_tables():
    models.create_tables()


@app.cli.command("create_super_admin")
def super_admin():
    models.create_super_admin()


app.teardown_appcontext(database.close_db)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
