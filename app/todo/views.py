from flask import render_template
from . import todo
# from ..models import Item


@todo.route('/workspace', methods=['GET', 'POST'])
def workspace():
    return render_template('todo/workspace.html')