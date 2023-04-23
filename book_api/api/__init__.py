from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']= 'flask-wtf'
db = SQLAlchemy(app)


from .models.books import Book
db.create_all()

from api import routes
from .forms.bookform import BookForm
