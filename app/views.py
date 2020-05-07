from flask import render_template,request,redirect,url_for
from . import main


# Views
@main.route('/')
def index():

    user = User.Query.all()

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Aenshtyns Blog'
    return render_template('index.html', title = title, user = user)
