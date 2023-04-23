from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "3fa9474e966934f6beb89e5712162efe"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db=SQLAlchemy(app)
# db.create_all()
bcrypt=Bcrypt(app)
app.app_context().push()
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

from flaskBlog import routes
