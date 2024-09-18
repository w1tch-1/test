from flask import Flask
from flask_login import LoginManager


__all__ = ('app', 'login_manager',)


app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
