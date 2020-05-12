from flask import render_template,request,redirect,url_for, abort
from . import main
from ..models import User, Post
from .. import db,photos
from ..requests import get_quotes
from flask_login import login_required, current_user
from .forms import UpdateProfile
import markdown2
import os

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

    # quotes = get_quotes()
    users = User.query.all()
    posts = Post.query.all()


    # random_quotes = get_quotes()
    # print(random_quotes)

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Aenshtyns Blog'
    return render_template('index.html', title = title, users = users, posts = posts  )

    # return render_template('index.html', title = title, random_quotes = random_quotes, users = users, posts = posts)


@main.route('/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_post(id):

       return render_template('new_blog.html',title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comment/<int:id>')
def single_comment(id):
    comment=Comment.query.get(id)
    if comment is None:
        abort(404)
    format_comment = markdown2.markdown(comment.movie_comment,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('comment.html',comment = comment,format_comment=format_comment)
