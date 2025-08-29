import os
from flask import Flask
from .services.db import db


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Config
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-change-me")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///reviews.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Init DB
    db.init_app(app)

    # Blueprints
    from .routes.public import bp as public_bp
    app.register_blueprint(public_bp)

    # Create tables on first run (dev convenience)
    with app.app_context():
        db.create_all()

    return app