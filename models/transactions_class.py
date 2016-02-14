#!/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

db = DB("localhost","root","mmGr2016","cdlcapital")

class Transactions:
    user = None
    trans_date  = None
    trans_type  = None
    stock = None
    price = None
    volume = None
    total_price = None

    def __init__(self):
        self.user = None
        self.trans_date  = None
        self.trans_type  = None
        self.stock = None
        self.price = None
        self.volume = None
        self.total_price = None
    
    def populate(self, user, trans_date, trans_type, stock, price, volume, total_price):
        self.user = user
        self.trans_date  = trans_date
        self.trans_type  = trans_type
        self.stock = stock
        self.price = price
        self.volume = volume
        self.total_price = total_price
    
    def select_all(self,user):
        return db.query("select * from transactions where user=('%s')"%(user)+";")
        
    def insert_transactions_model(self):
        db.query("insert into transactions values ('%s','%s','%s','%s','%s',%d,'%s')"%(self.user, self.trans_date, self.trans_type, self.stock, self.price, self.volume, self.total_price)+";")
        
    def get_user(self):
        return self.user
                
    def get_trans_date(self):
        return self.trans_date
        
    def set_trans_date(self,x):
        self.trans_date = x

    def get_trans_type(self):
        return self.trans_type
        
    def set_trans_type(self,x):
        self.trans_type = x

    def get_stock(self):
        return self.stock
        
    def set_stock(self,x):
        self.stock = x

    def get_price(self):
        return self.price
        
    def set_price(self,x):
        self.price = x

    def get_volume(self):
        return self.volume
        
    def set_volume(self,x):
        self.volume = x

    def get_total_price(self):
        return self.total_price
        
    def set_total_price(self,x):
        self.total_price = x

'''
t = Transactions()
print t.select_all('al356')
'''
