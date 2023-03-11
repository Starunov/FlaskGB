from wtforms import StringField, validators, TextAreaField, SubmitField, SelectMultipleField
from flask_wtf import FlaskForm


class CreateArticleForm(FlaskForm):
    title = StringField('Title', validators=[validators.InputRequired()])
    text = TextAreaField('Text', validators=[validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Create')
