from flask import render_template
from . import todo
from .forms import NewTaskForm
# from ..models import Item


@todo.route('/workspace', methods=['GET', 'POST'])
def workspace():
    form = NewTaskForm()
    return render_template('todo/workspace.html', form=form)