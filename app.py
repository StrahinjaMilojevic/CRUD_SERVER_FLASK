from flask import Flask
from routes.routes1 import bp as routes_bp


def create_app():
    app = Flask(__name__)
    # Registrujemo blueprint iz routes/routes1.py pod prefiksom /api
    app.register_blueprint(routes_bp, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    # Pokrećemo server lokalno na 127.0.0.1:5000
    app.run(debug=True, host='127.0.0.1', port=5000)
