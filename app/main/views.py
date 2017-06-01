from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import DataVultureForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = DataVultureForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'],
                           'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        old_age = session.get('age')
        if old_age is not None and old_age != form.age.data:
            flash('You changed your age!')
        session['age'] = form.age.data
        form.age.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'), age=session.get('age'),
                           known = session.get('known', False),
                           current_time=datetime.utcnow())

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@main.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@main.route('/redir')
def redir():
    return redirect('https://www.amazon.com')