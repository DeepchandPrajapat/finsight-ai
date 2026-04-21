from flask import Flask
from .config import Config
from flask_cors import CORS
from flask_migrate import Migrate
from .extensions import jwt, bcrypt,db


migrate = Migrate()  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)     
    bcrypt.init_app(app)   

    migrate.init_app(app, db) 

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from .routes.expenses import expenses_bp
    from .routes.budget import budget_bp
    from .routes.auth import auth_bp
    
    app.register_blueprint(expenses_bp)
    app.register_blueprint(budget_bp)
    app.register_blueprint(auth_bp)

    return app
