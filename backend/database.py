import sqlite3
from flask import current_app, g


def get_db():
    """
    Establishes connection to database & returns the connection object
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.execute("PRAGMA foreign_keys = ON")
        g.db.row_factory = sqlite3.Row  # returns SQL objects from SELECT
    return g.db


def close_db(e=None):
    """
    Closes connections after request finishes
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()
