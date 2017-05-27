from flask import Flask, redirect, request, render_template
from flask_script import Shell, Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YphciR469$$'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class AgeForm(Form):
    age = IntegerField('We need your age for the AI: ', validators=[DataRequired()])
    submit = SubmitField('Feed')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    form = AgeForm()
    if form.validate_on_submit():
        age = form.age.data
        form.age.data = ''
    return render_template('index.html', form=form, age=age, current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/redir')
def redir():
    return redirect('https://www.amazon.com')

if __name__ == '__main__':
    manager.run()
