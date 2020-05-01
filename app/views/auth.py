import hashlib
from functools import wraps

from flask import Blueprint, redirect, render_template, request, url_for, session, flash, g

from app.db import user

bp = Blueprint("auth", __name__)

@bp.route("/registrer", methods=["GET", "POST"])
def registrer():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        err = None

        if not username:
            err = "A username is required"
        elif not password:
            err = "A password is required"
        else:
            if user.get_username(username):
                err = "Username is already taken"

        if err is None:
            hashed_password = hash_password(password)
            user.add_user(username, hashed_password)
            return redirect(url_for(auth.login))
        else:
            flash(err, error)
    else:
        return render_template("auth/registrer.html")



@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        err = None

        user = user.get_username(username)

        if user is None:
            err = "Wrong Username or Password"

        if not check_hash(username, password):
            err = "Wrong Username or Password"

        if err is None:
            session.clear()
            session["user_id"] = user["user_id"]
            return redirect(url_for("index"))
        else:
            flash(err, error)
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
            flash("You must be logged in to see this page")
            return redirect(url_for("auth.login"))
    return check_login_status

@bp.before_request
def load_user():
    user_session = session.get("user_id")
    if user_session is None:
        g.user = None
    else:
        g.user = user.get_userID(user_session)

def hash_password(password):
    password = password.encode("utf-8")
    pass_hash = hashlib.md5(password).hexdigest()
    return pass_hash

def check_hash(username, password):
    user = user.get_username(username)
    if user["password"] == hash_password(password):
        return True
    else:
        return False
