import os
import sqlite3

import click

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "../db/")
database = os.path.join(db_path, f"{os.getenv('DATABASE')}.sqlite")
schema = os.path.join(db_path, "schema.sql")

class DB:
    def open_db():
        db = sqlite3.connect(database)
        return db

    def close_db():
        pass

    def initialize():
        db = DB.open_db()
        with open(schema, mode="r", encoding="utf-8") as f:
            DB.open_db().executescript(f.read())


@click.command("init-db")
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")