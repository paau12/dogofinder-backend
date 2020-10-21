from flask import Flask

from .extensions import db
from .views import api
from .models import *


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # Create db schema
    with app.test_request_context():
        db.init_app(app)
        db.create_all()

    # Register blueprints
    app.register_blueprint(api)

    return app
