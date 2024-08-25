from flask import Flask, render_template, request, redirect, Blueprint, flash, url_for

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Add your authentication logic here
        if username == 'admin' and password == 'password':
            flash('You were successfully logged in', 'success')
            return redirect(url_for('homepage_bp.homepage'))
        else:
            flash("Invalid credentials. Please try again.", 'failure')
            return redirect(url_for('login_bp.login'))
    
    return render_template('login.html')


@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Add your registration logic here
        pass
    return render_template('register.html')

