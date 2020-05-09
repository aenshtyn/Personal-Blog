from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Post, Quote
from .. import db
from ..requests import get_quotes

# @main.route('/')
# def index():
#
#     random_quotes = get_quotes()
#     print(random_quotes)
#
#     return render_template('index.html', random_quotes = random_quotes )

# Views
@main.route('/', methods = ['GET','POST'])
def index():

    users = User.query.all()
    posts = Post.query.filter_by(category = 'World News').all()


    # random_quotes = get_quotes()
    # print(random_quotes)

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Aenshtyns Blog'
    return render_template('index.html', title = title, users = users, posts = posts)

    # return render_template('index.html', title = title, random_quotes = random_quotes, users = users, posts = posts)
