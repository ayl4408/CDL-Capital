#!/usr/bin/python

class Users:
    user = None
    total_portfolio = None
    available_funds = None
    total_deposited = None

    def __init__(self, user, total_portfolio, available_funds, total_deposited):
        self.user = user
        self.total_portfolio = total_portfolio
        self.available_funds = available_funds
        self.total_deposited = total_deposited
    
    def get_user(self):
        return self.user

    def set_user(self,x):
        self.user = x

    def get_total_portfolio(self):
        return self.total_portfolio

    def set_total_portfolio(self,x):
        self.total_portfolio = x

    def get_available_funds(self):
        return self.available_funds

    def set_available_funds(self,x):
        self.available_funds = x

    def get_total_deposited(self):
        return self.total_deposited

    def set_total_deposited(self,x):
        self.total_deposited = x
