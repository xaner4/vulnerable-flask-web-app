import os
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "../db/")
database = os.path.join(db_path, f"{os.getenv('DATABASE')}.sqlite")
schema = os.path.join(db_path, "schema.sql")

class DB:
    def open_db():
        if "db" not in g:
            g.db = sqlite3.connect(database)
        return g.db

    def close_db(e=None):
        db = g.pop("db", None)
        if db is not None:
            db.close()
    
    def initialize():
        db = DB.open_db()
        with current_app.open_resource(schema) as f:
            db.executescript(f.read().decode("utf8"))



@click.command("init-db")
@with_appcontext
def init_db_command():
    DB.initialize()
    click.echo("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(DB.close_db)
    app.cli.add_command(init_db_command)