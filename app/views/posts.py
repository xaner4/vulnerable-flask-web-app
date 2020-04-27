import time
from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from app.db import DB as db

bp = Blueprint("posts", __name__)

@bp.route("/<int:id>")
def post(id: int):
    post = db.get_post(id)
    return render_template("post/post.html", post=post)

@bp.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        publised_at = int(time.time())
        author_id = request.form["author"]
        header = request.form["header"]
        article = request.form["article"]
        visebility = request.form["visebility"]
        if not header or not article:
            return render_template("post/add.html", err="Header or Article missing")
        else
            db.add_post(author_id, publised_at, header, article, visebility)
            return redirect(url_for("posts.post"))
    else:
        pass
