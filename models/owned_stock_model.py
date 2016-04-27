#!/usr/bin/python

class Owned_stock:

    def __init__(self, name=None, volume=None, price=None, total_worth=None, profit=None):
         self.name = name
         self.volume = volume
         self.price = price
         self.total_worth = total_worth
         self.profit = profit

    def set_name(self,x):
        self.name = x

    def get_name(self):
        return self.name

    def set_volume(self,x):
        self.volume = x

    def get_volume(self):
        return self.volume

    def set_price(self,x):
        self.price = x

    def get_price(self):
        return self.price

    def set_total_worth(self,x):
        self.total_worth = x

    def get_total_worth(self):
        return self.total_worth

    def set_profit(self,x):
        self.profit = x

    def get_profit(self):
        return self.profit
