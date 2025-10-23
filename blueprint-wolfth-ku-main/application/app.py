from flask import Flask
from bp.homepage.blueprint import homepage
app = Flask(__name__)
app.register_blueprint(homepage)


def init_app():
    return None