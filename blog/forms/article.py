from wtforms import StringField, validators, TextAreaField, SubmitField
from flask_wtf import FlaskForm


class CreateArticleForm(FlaskForm):
    title = StringField('Title', validators=[validators.InputRequired()])
    text = TextAreaField('Text', validators=[validators.DataRequired()])
    submit = SubmitField('Create')
