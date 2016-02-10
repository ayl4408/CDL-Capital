#!/usr/bin/python

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

    def get_user(self):
        return self.user
        
    def set_user(self,x):
        self.user = x
        
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
