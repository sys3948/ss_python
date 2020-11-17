from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config


db = SQLAlchemy()
cors = CORS()


def create_app(config_name):
    app = Flask(__name__)
    db.init_app(app)
    cors.init_app(app)
    app.config.from_object(config[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app