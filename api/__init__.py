from flask import Flask

from .extensions import db
from .views import api


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(api)

    # Register commands
    app.cli.add_command(create)

    return app
