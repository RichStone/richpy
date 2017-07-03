from flask_wtf import Form
from wtforms import StringField, SubmitField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, Length


class NewTaskForm(Form):
    title = StringField('Title', validators=[DataRequired(), Length(1, 64)])
    description = StringField('Description', validators=[DataRequired(), Length(1, 256)])
    due = DateTimeField('Due Date', render_kw={"placeholder":"Format: %Y-%m-%d %H:%M:%S"})
    submit = SubmitField('do it!')