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

class posts_db:

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
            INSERT INTO post ("author_id", "publised_at", "header", "article", "visebility") 
            VALUES  ("{author_id}", "{publised_at}", "{header}", "{article}", "{visebility}") """)
        db.commit()

    def edit_post(post_id, edited_at, header, article, visebility):
        db = DB.open_db()
        db.execute(f"""
        UPDATE post
        SET edited_at = {edited_at},
            header = "{header}",
            article = "{article}",
            visebility = "{visebility}"
        WHERE post_id = {post_id}
        """)
        db.commit()

    def delete_post(post_id):
        db = DB.open_db()
        db.execute(f"DELETE FROM post WHERE post_id = {post_id}")
        db.commit()
    
    def author_name():
        db = DB.open_db()
        cur = db.cursor()
        post_author_name = db.execute(f""" 
        select p.post_id, p.author_id, u.username
        from
        	"user" as u,
        	"post" as p
        where
        	u.user_id = p.author_id;
        """).fetchall()
        return post_author_name


class user:

    def get_users():
        db = DB.open_db()
        users = db.execute("SELECT * FROM user").fetchall()
        return users

    def get_username(username):
        db = DB.open_db()
        user = db.execute(f"SELECT * FROM user WHERE username = '{username}'").fetchone()
        return user

    def get_userID(user_id):
        db = DB.open_db()
        user = db.execute(f"SELECT * FROM user WHERE user_id = {user_id}").fetchone()
        return user

    def add_user(username, password, registerd_at):
        db = DB.open_db()
        db.execute(f"""INSERT INTO user (username, password, registerd_at)
                       VALUES ("{username}", "{password}", {registerd_at})""")
        db.commit()

    def edit_user(user_id, username):
        db = DB.open_db()
        db.execute(f"UPDATE user set username = '{username}' WHERE user_id = {user_id}")
        db.commit()

    def delete_user(user_id):
        db = DB.open_db()
        db.execute(f"DELETE FROM user WHERE user_id = {user_id} ")
        db.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    DB.initialize()
    click.echo("Initialized the database.")

def init_app(app):
    app.teardown_appcontext(DB.close_db)
    app.cli.add_command(init_db_command)