"""Initialize app."""

from flask import Flask
#import flask_login 
from flask_sqlalchemy import SQLAlchemy 
from Flask_Login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Construct application object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from flask_login_tutorial import auth, routes
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_blueprint)
        app.register_blueprint(auth.auth_blueprint)

        # Create Database Models
        db.create_all()

        # Compile static assets
        if app.config["ENVIRONMENT"] == "development":
            compile_static_assets(app)

        return app
