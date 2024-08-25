from flask import Flask, render_template, request, redirect, Blueprint, flash, url_for

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')