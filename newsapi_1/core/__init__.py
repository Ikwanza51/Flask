from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from core import route