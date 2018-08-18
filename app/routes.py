from flask import render_template, flash, request, redirect

from app import app, db
from app.forms import SubmitForm
from app.exchange import GameItem
from app.db_update import update
from app.models import Item



@app.route('/', methods=['GET', 'POST'])
def index():
    # Update the database
    update()

    form = SubmitForm()
    print(form.errors)
    print(form.validate_on_submit())

    if form.validate_on_submit():
        item_name = str.lower(form.input.data)
        item = Item.query.filter_by(name=item_name).first()
        if item != None:
            return render_template('index.html',form=form, id=item.game_id, name=item.name.capitalize(), price=item.price, members=item.members,
            buy_avg=item.buy_avg, sell_avg=item.sell_avg, buy_vol=item.buy_vol, sell_vol=item.sell_vol,
            total_vol=item.total_vol)

        else:
            flash('This item you have searched is not listed on the Grand Exchange.')
            return render_template('index.html', form=form)

    return render_template('index.html', form=form)
