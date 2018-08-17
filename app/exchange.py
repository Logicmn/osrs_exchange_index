import requests

request = requests.get('https://rsbuddy.com/exchange/summary.json')
ge_data = request.json()

class GameItem(object):
    def __init__(self, id):
        self.id = id

    def name(id):
        return ge_data[id]['name']

    def price(id):
        return ge_data[id]['overall_average']

    def members(id):
        return ge_data[id]['members']

    def buy_avg(id):
        return ge_data[id]['buy_average']

    def sell_avg(id):
        return ge_data[id]['sell_average']

    def buy_vol(id):
        return ge_data[id]['buy_quantity']

    def sell_vol(id):
        return ge_data[id]['sell_quantity']

    def total_vol(id):
        return ge_data[id]['overall_quantity']
