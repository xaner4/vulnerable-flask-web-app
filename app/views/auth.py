import time
import hashlib
import re
from functools import wraps

from flask import Blueprint, redirect, render_template, request, url_for, session, flash, g

from app.db import user_db

bp = Blueprint("auth", __name__)


@bp.before_request
def load_user():
    user_session = session.get("user_id")
    if user_session is None:
        g.user = None
    else:
        g.user = user_db.get_userID(user_session)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        username = username.lower()
        password = request.form["password"]

        err = None

        pattern = re.compile("[^a-z0-9.-_]")
        if pattern.search(username):
            err = "Username is not valid, Can only contain a-z, 0-9 and -_."

        if not username:
            err = "A username is required"
        elif not password:
            err = "A password is required"
        else:
            if user_db.get_username(username):
                err = "Username is already taken"
    
        if err is None:
            registered_at = int(time.time())
            hashed_password = hash_password(password)
            user_db.add_user(username, hashed_password, registered_at)
            flash(f"User: {username} have been succsefully made, you can now login", "success")
            return redirect(url_for("auth.login"))
        else:
            flash(err, "warning")
            return redirect(url_for("auth.register"))
    else:
        return render_template("auth/register.html")



@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        username = username.lower()
        password = request.form["password"]

        print(f"username={username}\nPassword={password}")

        err = None

        user = user_db.get_username(username)

        if user is None:
            err = "Wrong Username or Password"

        elif check_hash(username, password) != True:
            err = "Wrong Username or Password"

        if err is None:
            session.clear()
            session["user_id"] = user["user_id"]
            return redirect(url_for("index"))
        else:
            flash(err, "warning")
            return redirect(url_for("auth.login"))
    else:
        return render_template("auth/login.html")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

def login_required(f):
    @wraps(f)
    def check_login_status(*args, **kwargs):
        if "user_id" in session:
            return f(*args, **kwargs)
        else:
            flash("You must be logged in to see this page", "info")
            return redirect(url_for("auth.login"))
    return check_login_status

def hash_password(password):
    password = password.encode("utf-8")
    pass_hash = hashlib.md5(password).hexdigest()
    return pass_hash

def check_hash(username, password):
    user = user_db.get_username(username)
    if user["password"] == hash_password(password):
        return True
    else:
        return False