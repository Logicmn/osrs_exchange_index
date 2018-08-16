from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    id = '2'
    request = requests.get('https://rsbuddy.com/exchange/summary.json')
    ge_data = request.json()
    return render_template('index.html', ge_data=ge_data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
