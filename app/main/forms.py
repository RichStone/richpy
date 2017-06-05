from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class DataVultureForm(FlaskForm):
    name = StringField('Name required for the database: ',
                       validators=[DataRequired(), Length(min=1, max=20)])
    age = IntegerField('We need your age for the AI: ', validators=[DataRequired()])
    submit = SubmitField('Feed')
