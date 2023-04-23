from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskBlog.modules import User

class Registrationform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=8)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=3)])
    cpassword = PasswordField('Confirm Password', validators=[DataRequired(),Length(min=3),EqualTo('password')])
    submit= SubmitField('Sign Up')

    def validate_username(self,username):
        if self.username.data == current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self,email):
        if self.email.data == current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=3)])
    remember = BooleanField('Remember Me')
    submit= SubmitField('Login')


class UpdateAccountform(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=8)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit= SubmitField('Update Account')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit= SubmitField('Post')