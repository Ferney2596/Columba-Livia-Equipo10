from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired


class PostingForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    file = FileField('File', validators=[FileRequired()])
    submit = SubmitField('Send')
