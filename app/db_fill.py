import sqlite3
from contextlib import closing
from app import app


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema_data.sql', mode='r') as f:
            rd = f.read()
            db.cursor().executescript(rd)
        db.commit()

init_db()