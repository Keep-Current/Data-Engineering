from flask import Flask

from keep_current_storage.rest import document
from keep_current_storage.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(document.blueprint)
    return app