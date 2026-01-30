from flask import Flask
from .config import Config
from .extensions import db
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)

    from .routes.expenses import expenses_bp
    app.register_blueprint(expenses_bp)

    return app
