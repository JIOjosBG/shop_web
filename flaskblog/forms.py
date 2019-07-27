from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',
    validators=[DataRequired(),Length(min=2, max=20)])
    email=StringField('Email',
    validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',
    validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email=StringField('Email',
    validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class NewItemForm(FlaskForm):
    name=StringField('Name',
    validators=[DataRequired(),Length(min=5, max=100)])
    price = StringField('price', validators = [DataRequired()])
    type=StringField('type',
    validators=[DataRequired(),Length(min=1, max=50)])

    picture = FileField('New Item picture',validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField('AddItem')
