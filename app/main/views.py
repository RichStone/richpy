from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash, current_app
from .. import db
from ..models import User
from ..email import send_email
from . import main
from .forms import DataVultureForm


@main.route('/', methods=['GET', 'POST'])
def index():
    name = 'AFD!'
    return render_template('user.html', name=name)


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