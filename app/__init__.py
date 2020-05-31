from flask import Flask


def create_app():
    app = Flask(__name__)

    app.secret_key = "1"

    from app import db
    db.init_app(app)

    from app.views import auth, index, posts
    app.register_blueprint(auth.bp, url_prefix="/user")
    app.register_blueprint(index.bp)
    app.register_blueprint(posts.bp, url_prefix="/post")

    app.add_url_rule("/", endpoint="index")
    return app