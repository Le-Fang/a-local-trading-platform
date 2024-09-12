from flask import Flask
from app.config import Config
from app.login.login import login_bp  # Import the Blueprint
from app.extensions import db


app = Flask(__name__)
app.secret_key = Config.SECRET_KEY  # Set a secret key for session management

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register Blueprints
app.register_blueprint(login_bp)

db.init_app(app)