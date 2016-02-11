#!/usr/bin/python

import sys
sys.path.insert(0, '/usr/lib/cgi-bin/alee_cdlcapital/back')
from database_class import DB

db = DB("localhost","root","mmGr2016","cdlcapital")

class Owned_stocks:
    stock = None
    current_shares = None
    current_price = None
    total_worth = None
    stock_owner = None
    profit = None

    def __init__(self):
        self.stock = None
        self.current_shares = None
        self.current_price = None
        self.total_worth = None
        self.stock_owner = None
        self.profit = None

    def populate_owned_stocks_model(self, user, company):
        result = db.query("select * from owned_stocks where stock_owner=('%s')"%(user)+" and stock = ('%s')"%(company)+";")
        if result:
            self.stock = result[0][0]
            self.current_shares = result[0][1]
            self.current_price = result[0][2]
            self.total_worth = result[0][3]
            self.stock_owner = result[0][4]
            self.profit = result[0][5]
        
    def get_stock(self):
        return self.stock

    def set_stock(self,x):
        self.stock = x

    def get_current_shares(self):
        return self.current_shares

    def set_current_shares(self,x):
        self.current_shares = x

    def get_current_price(self):
        return self.current_price

    def set_current_price(self,x):
        self.current_price = x

    def get_total_worth(self):
        return self.total_worth

    def set_total_worth(self,x):
        self.total_worth = x

    def get_stock_owner(self):
        return self.stock_owner

    def set_stock_owner(self,x):
        self.stock_owner = x

    def get_profit(self):
        return self.profit

    def set_profit(self,x):
        self.profit = x

#o = Owned_stocks()
#o.populate_owned_stocks_model('al356', 'nflx')
#print o.get_profit()
