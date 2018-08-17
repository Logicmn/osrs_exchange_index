import requests

request = requests.get('https://rsbuddy.com/exchange/summary.json')
ge_data = request.json()

class Item(object):
    def __init__(self, id, name, price, members, buy_avg, sell_avg, buy_vol, sell_vol, total_vol):
        self.id = id
        self.name = name
        self.price = price
        self.members = members
        self.buy_avg = buy_avg
        self.sell_avg = sell_avg
        self.buy_vol = buy_vol
        self.sell_vol = sell_vol
        self.total_vol = total_vol

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
