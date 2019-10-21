from flask import Flask
from flask_mongoengine import MongoEngine
from . import config
db = MongoEngine()

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object(config.DevConfig)
    else:
        app.from_mapping(test_config)

    db.init_app(app)
    
    register_blueprints(app)

    return app


def register_blueprints(app):
    from . import home
    app.register_blueprint(home.bp)