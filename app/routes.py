from flask import render_template, flash, request, redirect

from app import app
from app.forms import SubmitForm
from app.exchange import GameItem



@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubmitForm()
    print(form.errors)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        id = form.input.data
        print("hello")
        try:
            name = GameItem.name(id)
            price = GameItem.price(id)
            members = GameItem.members(id)
            buy_avg = GameItem.buy_avg(id)
            sell_avg = GameItem.sell_avg(id)
            buy_vol = GameItem.buy_vol(id)
            sell_vol = GameItem.sell_vol(id)
            total_vol = GameItem.total_vol(id)
            return render_template('index.html',form=form, name=name, price=price, members=members,
            buy_avg=buy_avg, sell_avg=sell_avg, buy_vol=buy_vol, sell_vol=sell_vol,
            total_vol=total_vol)

        except KeyError:
            print("keyerror")
            flash('This item you have searched is not listed on the Grand Exchange.')
            return render_template('index.html', form=form)

    return render_template('index.html', form=form)
