from flask import Flask
from .config import Config
from .extensions import db
from flask_cors import CORS
from flask_migrate import Migrate

migrate = Migrate()  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db) 

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .routes.expenses import expenses_bp
    from .routes.budget import budget_bp
    
    app.register_blueprint(expenses_bp)
    app.register_blueprint(budget_bp)

    return app
