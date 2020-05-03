from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort

from app.db import posts_db

bp = Blueprint("index", __name__)

@bp.route("/")
def index():
    posts = posts_db.get_posts()
    authors = posts_db.author_name()

    author_dict = dict()
    for author in authors:
        author_dict[author[0]] = dict(author)

    posts_dict = list()
    for post in posts:
        posts_dict.append(dict(post))

    return render_template("index.html", posts=reversed(posts_dict), authors=author_dict)