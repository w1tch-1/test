# pip install flask-sqlalchemy flask-migrate

'''
flask db init
flask db migrate
flask db upgrade
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin

from .config import app

from datetime import datetime


__all__ = ('db', 'migrate', 'User', 'Post', 'Comments')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

# CRUD - Create Read Update Delete


# Integer, String, Text, DateTime, Boolean, Binary
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow())
    user = db.Column(db.Integer, db.ForeignKey('user.id'))


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_comments = db.Column(db.DateTime, default=datetime.utcnow)
    post = db.Column(db.Integer, db.ForeignKey('post.id'))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
