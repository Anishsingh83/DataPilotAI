from flask import Flask

from config import Config
from src.routes.home import home_bp


def create_app():
    """
    Application Factory
    """

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    # Load configuration
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(home_bp)

    return app