from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort

from app.db import DB as db

bp = Blueprint("index", __name__)

@bp.route("/")
def index():
    posts = db.get_posts()
    return render_template("index.html", posts=posts)