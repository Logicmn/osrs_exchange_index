import requests
from app import db
from app.models import Item

request = requests.get('https://rsbuddy.com/exchange/summary.json')
ge_data = request.json()

def update():
    for key in ge_data:
        new_item = Item(game_id=ge_data[key]['id'], name=str.lower(ge_data[key]['name']),
        price=ge_data[key]['overall_average'], members=ge_data[key]['members'],
        buy_avg=ge_data[key]['buy_average'], sell_avg=ge_data[key]['sell_average'],
        buy_vol=ge_data[key]['buy_quantity'], sell_vol=ge_data[key]['sell_quantity'],
        total_vol=ge_data[key]['overall_quantity'])

        if Item.query.filter_by(game_id=key).first() == None:
            db.session.add(new_item)
        else:
            old_item = Item.query.filter_by(game_id=key).first()

            db.session.delete(old_item)
            db.session.add(new_item)
    db.session.commit()
