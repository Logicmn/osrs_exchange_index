from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    price = db.Column(db.Integer, index=True)
    members = db.Column(db.Boolean, index=True)
    buy_avg = db.Column(db.Integer, index=True)
    sell_avg = db.Column(db.Integer, index=True)
    buy_vol = db.Column(db.Integer, index=True)
    sell_vol = db.Column(db.Integer, index=True)
    total_vol = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<Item name: {}>'.format(self.name)
