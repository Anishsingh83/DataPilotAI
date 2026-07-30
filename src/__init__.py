from flask import Flask

from config import Config

from src.routes.home import home_bp
from src.routes.explorer import explorer_bp
from src.routes.cleaning import cleaning_bp


def create_app():

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    app.config.from_object(Config)

    app.register_blueprint(home_bp)
    app.register_blueprint(explorer_bp)
    app.register_blueprint(cleaning_bp)

    return app