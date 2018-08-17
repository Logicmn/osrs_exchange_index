import requests

request = requests.get('https://rsbuddy.com/exchange/summary.json')
ge_data = request.json()
