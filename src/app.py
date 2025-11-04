from flask import Flask
from src.routes.routes1 import bp as routes_bp  # import blueprint-a

def create_app():
    app = Flask(__name__)

    # registrujemo blueprint sa prefixom /api
    app.register_blueprint(routes_bp, url_prefix="/api")

    return app
