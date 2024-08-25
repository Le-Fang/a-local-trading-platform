from flask import Flask
from config import Config
from .routes.login import login_bp  # Import the Blueprint
from .routes.index import index_bp  # Import the Blueprint
from .routes.homepage import homepage_bp  # Import the Blueprint

def create_app():
    app = Flask(__name__, template_folder='templates')
    # app.config.from_object(Config)
    app.secret_key = Config.SECRET_KEY  # Set a secret key for session management

    # Register Blueprints
    app.register_blueprint(login_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(homepage_bp)

    return app