from flask import Blueprint,render_template,redirect,url_for
from Project import db
from Project.models import Puppy

about_blueprint = Blueprint('about', __name__,template_folder='templates')

@about_blueprint.route("/info")
def info():
    """Testing a method that what is shown"""
    return render_template('info.html')
    
@about_blueprint.route("/")
def info2():
    """Testing a method that what is shown"""
    return render_template('info.html')