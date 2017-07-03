from flask_wtf import Form
from wtforms import StringField, SubmitField, DateTimeField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length


class NewTaskForm(Form):
    title = StringField('Title', validators=[DataRequired(), Length(1, 64)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(1, 256)])
    due = DateTimeField('Due Date', render_kw={"placeholder":"Format: YYYY-mm-DD hh:MM:ss"})
    submit = SubmitField('do it!', render_kw={"class":"btn btn-info"})