from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField("login", validators = [DataRequired()])
    senha = PasswordField("senha", validators = [DataRequired()])
    remember_me = BooleanField("remember_me")