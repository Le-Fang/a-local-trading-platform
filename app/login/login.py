from flask import Flask, render_template, request, redirect, Blueprint, flash, url_for
from app.models import User
from app.extensions import db
from app import utils

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the user exists
    user = User.query.filter_by(username=username).first()
    if user is None:
        return {"message": "User does not exist"}

    # Check if the password is correct
    if user.password_hash != utils.hash_password(password):
        return {"message": "Incorrect password"}
    
    
    return {"message": "Logged in successfully"}


@login_bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Check if the username or email already exists
    if User.query.filter_by(username=username).first() is not None:
        return {"message": "username already exists"}
    
    if User.query.filter_by(email=email).first() is not None:
        return {"message": "email already exists"}

    # Create a new user
    new_user = User(username=username, password_hash=utils.hash_password(password), email=email)
    db.session.add(new_user)
    db.session.commit()
    
    return {"message": "User created successfully"}

