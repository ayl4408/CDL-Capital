#!/usr/bin/python

class History:
    def __init__(self, user, trans_date, trans_type, stock, price, total_price, volume, algo_id):
        self.user = user
        self.trans_date = trans_date
        self.trans_type = trans_type
        self.stock = stock
        self.price = price
        self.total_price = total_price
        self.volume = volume
        self.algo_id = algo_id

    def get_algo_id(self):
        return self.algo_id

    def set_algo_id(self, x):
        self.algo_id = x
        
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

    def get_total_price(self):
        return self.total_price

    def set_total_price(self,x):
        self.total_price = x

    def get_volume(self):
        return self.volume

    def set_volume(self,x):
        self.volume = x

    
        
