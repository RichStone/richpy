from flask import render_template, flash, redirect, url_for
from . import todo
from .forms import NewTaskForm
from ..models import Item
from app import db


@todo.route('/workspace', methods=['GET', 'POST'])
def workspace():
    form = NewTaskForm()
    if form.validate_on_submit():
        item = Item(title=form.title.data,
                    description=form.description.data,
                    due=form.due.data if form.due.data else None,
                    state=0)
        db.session.add(item)
        flash('Great!')
        return redirect(url_for('todo.workspace'))
    items = Item.query.all()
    return render_template('todo/workspace.html', form=form, items=items)