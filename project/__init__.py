from flask import Flask
from project.blueprint import api_bp

def register_blueprints(app):
    app.register_blueprint(api_bp, )

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app