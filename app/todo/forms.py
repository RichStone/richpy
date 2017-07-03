from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NewTaskForm(Form):
    new_task = StringField('New Task: ', validators=[DataRequired(), Length(1, 264)])
    submit = SubmitField('do it!')