from flask import Flask
from bp.homepage.blueprint import homepage

def init_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)