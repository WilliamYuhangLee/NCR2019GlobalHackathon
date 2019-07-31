import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """
    Factory method to create an app instance.

    :return: a Flask app instance
    :rtype: Flask
    """
    app = Flask(__name__, instance_relative_config=True)

    # Detect Config class from environment and import the specified Config class from config.py and instance/config.py
    config_class = os.getenv('FLASK_ENV', 'production')
    app.config.from_object(config.__name__ + '.' + config_class.capitalize() + 'Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app)

    # Register Blueprints
    from .gym import api_bp
    app.register_blueprint(api_bp)

    return app
