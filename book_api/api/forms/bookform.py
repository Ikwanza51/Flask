from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Name',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    price = IntegerField('Price',validators=[DataRequired()])
    submit=SubmitField(('Submit'))