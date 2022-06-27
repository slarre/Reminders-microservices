from flask import Flask

from reminder.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from reminder.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
