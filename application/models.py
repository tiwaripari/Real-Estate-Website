from application.database import db

class Property(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    house = db.Column(db.Integer)
    street = db.Column(db.String(50))
    area = db.Column(db.String(50))
    pincode = db.Column(db.Numeric(4))
    area_sqft = db.Column(db.Integer)
    avail = db.Column(db.Integer)
    market_in = db.Column(db.Date)
    rent_price = db.Column(db.Integer)
    sell_price = db.Column(db.Integer)
    no_bedrooms = db.Column(db.Integer)
    build_year = db.Column(db.Integer)
    is_sold = db.Column(db.Boolean)
    is_rented = db.Column(db.Boolean)
