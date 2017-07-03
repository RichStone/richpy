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
        db.session.commit()
        flash('Great!')
        return redirect(url_for('todo.workspace'))
    items = Item.query.all()
    return render_template('todo/workspace.html', form=form, items=items)


@todo.route('/delete/<item_id>', methods=['POST'])
def delete(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('todo.workspace'))


@todo.route('/change_state/<item_id>/<state>', methods=['POST'])
def change_state(item_id, state):
    item = Item.query.get(item_id)
    item.state = state
    db.session.commit()
    return redirect(url_for('todo.workspace'))