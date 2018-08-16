from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from wtforms import StringField
from flask_wtf import Form
from grand_exchange.exchange import Item

app = Flask(__name__)
app.secret_key = 'supersecret'
bootstrap = Bootstrap(app)

class SubmitForm(Form):
    input = StringField('Item search')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SubmitForm()
    if form.validate_on_submit():
        id = form.input.data
        try:
            name = Item.name(id)
            price = Item.price(id)
            members = Item.members(id)
            buy_avg = Item.buy_avg(id)
            sell_avg = Item.sell_avg(id)
            buy_vol = Item.buy_vol(id)
            sell_vol = Item.sell_vol(id)
            total_vol = Item.total_vol(id)
            return render_template('index.html',form=form, name=name, price=price, members=members,
            buy_avg=buy_avg, sell_avg=sell_avg, buy_vol=buy_vol, sell_vol=sell_vol,
            total_vol=total_vol)
        except KeyError:
            flash('This item you have searched is not listed on the Grand Exchange.')
            return render_template('index.html', form=form)
    else:
        return render_template('index.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
