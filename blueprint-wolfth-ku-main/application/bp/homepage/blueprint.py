"""blueprint"""
from flask import Blueprint, render_template
homepage = Blueprint('homepage', __name__,template_folder='templates')
@homepage.route('/', defaults={'homepage': 'about'})
@homepage.route('/homepage')
def home():
    """Shows homepage"""
    return render_template(f'pages/{homepage}.html')
@homepage.route('/about')
def about():
    """shows about page"""
    return render_template(f'pages/{about}.html')
