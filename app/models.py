from . import db

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

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
