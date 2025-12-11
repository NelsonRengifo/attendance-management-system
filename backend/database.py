import sqlite3
from flask import current_app, g


def get_db():
    """
    Establishes connection to database & returns the connection object
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES  # data types of sql column to python
        )
        g.db.execute("PRAGMA foreign_keys = ON")
        # returns SQL objects from SELECT. Remembers/matches keys(col) and values!
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """
    Closes connections after request finishes
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()
