import os

class Config:
    SECRET_KEY = 'your_secret_key'  # Set a secret key for session management
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Set the database URI