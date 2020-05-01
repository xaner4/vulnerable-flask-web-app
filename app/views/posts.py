import time
from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from app.db import posts_db

bp = Blueprint("posts", __name__)

@bp.route("/<int:id>")
def post(id: int):
    if id:
        post = posts_db.get_post(id)
        return render_template("post/post.html", post=post)
    else:
        abort(404, f"A post with id: '{post_id}' does not exsist")

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
        else:
            posts_db.add_post(author_id, publised_at, header, article, visebility)
            return redirect("/", err=err)
    else:
        return render_template("post/add.html")

@bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id: int):
    if request.method == "POST":
        edited_at = int(time.time())
        header = request.form["header"]
        article = request.form["article"]
        visebility = request.form["visebility"]
        posts_db.edit_post(post_id, edited_at, header, article, visebility)
    else:
        post = posts_db.get_post(id)
        if post is None:
            abort(404, f"A post with id {post_id} does not exsist")
        else:
            return render_template("post/edit.html", post=post)
        
