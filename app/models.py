from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    content = db.Column(db.Text(), nullable = False)
    category = db.Column(db.String(255), index = True,nullable = False)

    def save_p(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'Pitch {self.post}'

class Quote:

    def __init__(self,quote,author):
        self.quote = quote
        self.author = author
