#!/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

db = DB("localhost","root","mmGr2016","cdlcapital")

class Users:

    login = None
    profit = None
    total_portfolio = None
    available_funds = None
    total_stock_values = None
    total_deposited = None

    def __init__(self,user):
        result = db.query("select * from users where login = ('%s')"%(user)+";")
        if result:
            self.login = result['login']
            self.profit = result['profit']
            self.total_portfolio = result['total_portfolio']
            self.available_funds = result['available_funds']
            self.total_stock_values = result['total_stock_values']
            self.total_deposited = result['total_deposited']

    def update_users_model(self, profit, total_portfolio, available_funds, total_stock_values, total_deposited):
        db.query("update users set profit=('%s')"%(profit)+", total_portfolio=('%s')"%(total_portfolio)+", available_funds=('%s')"%(available_funds)+", total_stock_values=('%s')"%(total_stock_values)+", total_deposited=('%s')"%(total_deposited)+" where login=('%s')"%(self.login)+";")
        
    def get_login(self):
        return self.login

    def get_profit(self):
        return self.profit

    def set_profit(self,x):
        db.query("update users set profit=('%s')"%(x)+";")
        self.profit = x

    def get_total_portfolio(self):
        return self.total_portfolio

    def set_total_portfolio(self,x):
        db.query("update users set total_portfolio=('%s')"%(x)+";")
        self.total_portfolio = x

    def get_available_funds(self):
        return self.available_funds

    def set_available_funds(self,x):
        db.query("update users set available_funds=('%s')"%(x)+";")
        self.available_funds = x

    def get_total_stock_values(self):
        return self.total_stock_values

    def set_total_stock_values(self,x):
        db.query("update users set total_stock_values=('%s')"%(x)+";")
        self.total_stock_values = x

    def get_total_deposited(self):
        return self.total_deposited

    def set_total_deposited(self,x):
        db.query("update users set total_deposited=('%s')"%(x)+";")
        self.total_deposited = x

#u = Users('al356')
#print u.get_profit()
