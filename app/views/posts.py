import time
from flask import Blueprint, redirect, render_template, request, url_for, g
from werkzeug.exceptions import abort

from app.db import posts_db
from app.views.auth import login_required

bp = Blueprint("posts", __name__)

@bp.route("/<post_id>")
def post(post_id):
    post = posts_db.get_post(post_id)
    authors = posts_db.author_name()

    author_dict = dict()
    for author in authors:
        author_dict[author[0]] = dict(author)

    if post == None:
        abort(404, f"A post with id: '{post_id}' does not exsist")
    else:
        return render_template("post/post.html", post=post, authors=author_dict)

@bp.route("/add", methods=["GET", "POST"])
@login_required
def add_post():
    if request.method == "POST":
        publised_at = int(time.time())
        author_id = request.form["author"]
        title = request.form["title"]
        article = request.form["article"]
        visebility = request.form["visebility"]
        if not title or not article:
            return render_template("post/add.html", err="title or Article missing")
        else:
            posts_db.add_post(author_id, publised_at, title, article, visebility)
            return redirect("/", err=err)
    else:
        return render_template("post/add.html")

@bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id: int):
    if request.method == "POST":
        edited_at = int(time.time())
        title = request.form["title"]
        article = request.form["article"]
        visebility = request.form["visebility"]
        posts_db.edit_post(post_id, edited_at, title, article, visebility)
    else:
        post = posts_db.get_post(post_id)
        if post is None:
            abort(404, f"A post with id {post_id} does not exsist")
        else:
            return render_template("post/edit.html", post=post)