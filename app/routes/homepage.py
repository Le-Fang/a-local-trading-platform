from flask import Flask, render_template, request, redirect, Blueprint, flash, url_for

homepage_bp = Blueprint('homepage_bp', __name__)

@homepage_bp.route('/homepage')
def homepage():
    return render_template('homepage.html')