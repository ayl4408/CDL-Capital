#!/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

db = DB("localhost","root","mmGr2016","cdlcapital")

class Owned_stocks:
    stock = None
    current_shares = None
    current_price = None
    total_worth = None
    stock_owner = None
    profit = None
    
    def __init__(self,user,company):
        result = db.query("select * from owned_stocks where stock_owner=('%s')"%(user)+" and stock = ('%s')"%(company)+";")
        if result:
            self.stock = result[0]['stock']
            self.current_shares = result[0]['current_shares']
            self.current_price = result[0]['current_price']
            self.total_worth = result[0]['total_worth']
            self.stock_owner = result[0]['stock_owner']
            self.profit = result[0]['profit']
        
    def insert_owned_stocks_model(self, company, current_shares, current_price, total_worth, stock_owner):
        db.query("insert into owned_stocks values ('%s',%d,'%s','%s','%s','%s')"%(company, current_shares, current_price, total_worth, stock_owner, "0.00")+";")
        
    def get_stock(self):
        return self.stock

    def get_current_shares(self):
        return self.current_shares

    def set_current_shares(self,x):
        db.query("update owned_stocks set current_shares=('%s')"%(x)+";")
        self.current_shares = x

    def get_current_price(self):
        return self.current_price

    def set_current_price(self,x):
        db.query("update owned_stocks set current_price=('%s')"%(x)+";")
        self.current_price = x

    def get_total_worth(self):
        return self.total_worth

    def set_total_worth(self,x):
        db.query("update owned_stocks set total_worth=('%s')"%(x)+";")
        self.total_worth = x

    def get_stock_owner(self):
        return self.stock_owner

    def set_stock_owner(self,x):
        self.stock_owner = x

    def get_profit(self):
        return self.profit

    def set_profit(self,x):
        db.query("update owned_stocks set profit=('%s')"%(x)+";")
        self.profit = x

#o = Owned_stocks('al356', 'nflx')
#print o.get_profit()

