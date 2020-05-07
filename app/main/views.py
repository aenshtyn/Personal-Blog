from flask import render_template,request,redirect,url_for
from . import main
from ..models import User
from .. import db

# Views
@main.route('/')
def index():

    user = User.query.all()

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Aenshtyns Blog'
    return render_template('index.html', title = title, user = user)
