from flask import Flask, redirect, request, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from pathlib import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# configure data base
app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'YphciR469$$'

bootstrap = Bootstrap(app)
moment = Moment(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

    users = db.relationship('User', backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

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
    form = AgeForm()
    if form.validate_on_submit():
        old_age = session.get('age')
        if old_age is not None and old_age != form.age.data:
            flash('You changed your age!')
        session['age'] = form.age.data
        form.age.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, age=session.get('age'),
                           current_time=datetime.utcnow())

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
    app.run()
