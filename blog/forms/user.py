from wtforms import StringField, validators, PasswordField, SubmitField
from flask_wtf import FlaskForm


class UserRegisterForm(FlaskForm):
    username = StringField('Username', validators=[validators.InputRequired()])
    email = StringField('E-mail', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=6)])
    confirm_password = PasswordField('Confirm password', validators=[validators.EqualTo('password')])
    submit = SubmitField('Register')


class UserLoginForm(FlaskForm):
    email = StringField('E-mail', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.length(min=6)])
    submit = SubmitField('Login')
