import os
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "../db/")

if os.getenv("DATABASE") != ":memory:":
    database = os.path.join(db_path, f"{os.getenv('DATABASE')}.sqlite")
else:
    database = ":memory:"

schema = os.path.join(db_path, "schema.sql")

class DB:
    def open_db():
        if "db" not in g:
            g.db = sqlite3.connect(database)
            g.db.row_factory = sqlite3.Row
        return g.db

    def close_db(e=None):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    def initialize():
        db = DB.open_db()
        with current_app.open_resource(schema) as f:
            db.executescript(f.read().decode("utf8"))

    def get_posts():
        db = DB.open_db()
        posts = db.execute("SELECT * FROM post").fetchall()
        return posts
    
    def get_post(post_id):
        db = DB.open_db()
        post = db.execute(f"SELECT * FROM post WHERE post_id = {post_id}").fetchone()
        return post
    
    def add_post(author_id, publised_at, header, article, visebility):
        db = DB.open_db()
        db.execute(f""" 
            INSERT INTO post ("post_id", "author_id", "publised_at", "edited_at", "header", "article", "visebility") 
            VALUES  ({author_id}, {publised_at}, {header}, {article}, {visebility})""")


@click.command("init-db")
@with_appcontext
def init_db_command():
    DB.initialize()
    click.echo("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(DB.close_db)
    app.cli.add_command(init_db_command)