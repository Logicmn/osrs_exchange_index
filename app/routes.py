from flask import render_template, flash, request, redirect
from flask_nav.elements import *

from app import app, db, nav
from app.forms import SubmitForm
from app.exchange import GameItem
from app.db_update import update
from app.models import Item

@nav.navigation('runeberg_navbar')
def create_navbar():
    index_view = View('Home', 'index')
    return Navbar('Runeberg', index_view)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Update the database
    #update()

    form = SubmitForm()
    print(form.errors)
    print(form.validate_on_submit())

    if form.validate_on_submit():
        item_name = str.lower(form.input.data)
        items = Item.query.filter(Item.name.contains(item_name)).all()

        if not items:
            print('unlisted')
            flash('This item you have searched is not listed on the Grand Exchange.')
            return render_template('index.html', form=form)

        else:
            return render_template('index.html', form=form, items=items,
            item_name=item_name, number_of_results=len(items))

    return render_template('index.html', form=form)
