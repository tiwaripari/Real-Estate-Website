from application.database import db
from sqlalchemy import *

class Property(db.Model):
    __tablename__ = 'property'
    pid = db.Column(db.Integer, primary_key=True)
    house_no = db.Column(db.Integer)
    street = db.Column(db.String(50))
    area = db.Column(db.String(50))
    pincode = db.Column(db.Numeric(4))
    area_sqft = db.Column(db.Integer)
    avail = db.Column(db.String)
    market_in = db.Column(db.Date)
    rent_price = db.Column(db.Integer)
    sell_price = db.Column(db.Integer)
    no_bedrooms = db.Column(db.Integer)
    build_year = db.Column(db.Integer)
    is_sold = db.Column(db.Boolean)
    is_rented = db.Column(db.Boolean)


class Agent(db.Model):
    __tablename__ = 'agent'
    agent_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(50))
    agent_name = db.Column(db.String(50))
    contact_no = db.Column(db.Numeric(10))
    area = db.Column(db.String(50))
    rating = db.Column(db.Numeric(2, 1))
    no_rented = db.Column(db.Integer)
    no_sold = db.Column(db.Integer)
    rental_sales = db.Column(db.Integer)
    sold_sales = db.Column(db.Integer)
    base_commission = db.Column(db.Numeric(2, 1))


class Sells(db.Model):
    __tablename__ = 'sells'
    pid = db.Column(db.Integer, db.ForeignKey('property.pid'))
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.agent_id'))
    __table_args__ = (
        db.PrimaryKeyConstraint('pid', 'agent_id'),
    )

class Buyer(db.Model):
    __tablename__ = 'buyer'
    bid = db.Column(db.Integer, primary_key=True)
    password =	db.Column(db.String(50))
    buyer_name = db.Column(db.String(50))
    contact_no =  db.Column(db.Numeric(10,0))
    area =  db.Column(db.String(50))
    budget = db.Column(db.Integer)

class Seller(db.Model):
    tablename = 'seller'
    sid         = db.Column(db.Integer, primary_key = True)			
    password    = db.Column(db.String(50))	
    seller_name = db.Column(db.String(50))
    contact_no 	= db.Column(db.Numeric(10,0))   

class Buys(db.Model):
    __tablename__ = 'buys'
    pid = db.Column(db.Integer, db.ForeignKey('property.pid'))
    bid = db.Column(db.Integer, db.ForeignKey('buyer.bid'))
    year_sold = db.Column(db.Integer)
    market_out = db.Column(db.Date)
    __table_args__ = (
        db.PrimaryKeyConstraint('pid', 'bid'),
    )


class Owns(db.Model):
    __tablename__ = 'owns'
    sid = db.Column(db.Integer, db.ForeignKey('seller.sid'))
    pid = db.Column(db.Integer, db.ForeignKey('property.pid'))
    current_owner = db.Column(db.Integer)
    __table_args__ = (
        db.PrimaryKeyConstraint('sid', 'pid'),
    )

class Admin(db.Model):
    __tablename__ = 'admin'
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    __table_args__ = (
        db.PrimaryKeyConstraint('username', 'password'),
    )

def isValidUser(id, pass_word, user_type):
    print(id,pass_word,user_type)
    if(user_type == "user"):

        buyer = Buyer.query.filter_by(bid=id, password = pass_word).first()
        seller = Seller.query.filter_by(sid=id, password = pass_word).first()
        print(buyer)
        if(buyer is not None ):
            print("in buyer")
            return True
        elif(seller is not None):
            return True
        else:
            print("not in buyer or seller")
            return False
    elif(user_type == "agent"):
        agent = Agent.query.filter_by(agent_id = id, password = pass_word).first()
        
        if(agent is not None ):
            return True
        else:
            return False
        
    elif(user_type == "agent_office"):
        admin = Admin.query.filter_by(username = id , password = pass_word).first()
        if(admin is not None):
            return True
        else:
            return False
    