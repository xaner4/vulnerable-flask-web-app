import os
import sqlite3

from flask import Flask, request, json, views
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)

import db


@app.route("/")
def index():
    pass

@app.route("/posts")
def posts():
    pass

@app.route("/posts/<int:id>")
def post(id: int):
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)