from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length



class NewItemForm(FlaskForm):
    name=StringField('Name',
    validators=[DataRequired(),Length(min=5, max=100)])
    price = StringField('price', validators = [DataRequired()])
    type=StringField('type',
    validators=[DataRequired(),Length(min=1, max=50)])

    picture = FileField('New Item picture',validators=[FileAllowed(['jpg','png'])])

    submit = SubmitField('AddItem')
