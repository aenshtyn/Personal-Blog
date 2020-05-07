from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Post
from .. import db

# Views
@main.route('/', methods = ['GET','POST'])
def index():

    users = User.query.all()
    posts = Post.query.filter_by(category = 'World News').all() 

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Aenshtyns Blog'
    return render_template('index.html', title = title, users = users, posts = posts)
