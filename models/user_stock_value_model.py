#!/usr/bin/python

class User:
    user = None
    profit = None
    total_stock_values = None
    
    def __init__(self, user, profit, total_stock_values):
        self.user = user
        self.profit = profit
        self.total_stock_values = total_stock_values
        
    def set_user(self,x):
        self.user = x

    def get_user(self):
        return self.user

    def set_profit(self,x):
        self.profit = x

    def get_profit(self):
        return self.profit
    
    def set_total_stock_values(self,x):
        self.total_stock_values = x

    def get_total_stock_values(self):
        return self.total_stock_values
    
