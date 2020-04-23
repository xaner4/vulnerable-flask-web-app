from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping()

    from app import db
    db.init_app(app)

    app.add_url_rule("/", endpoint="index")
    return app