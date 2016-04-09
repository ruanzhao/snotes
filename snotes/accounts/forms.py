
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    login = TextField("username or email", [Required()])
    password = PasswordField('Password', [Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')