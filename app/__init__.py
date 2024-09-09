from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from .login.login import login_bp  # Import the Blueprint


app = Flask(__name__, template_folder='templates')
# app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY  # Set a secret key for session management

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register Blueprints
app.register_blueprint(login_bp)

db = SQLAlchemy(app)