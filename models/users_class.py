#!/usr/bin/python

import sys
sys.path.insert(0, '/usr/lib/cgi-bin/alee_cdlcapital/back')
from database_class import DB

db = DB("localhost","root","mmGr2016","cdlcapital")

class Users:

    login = None
    password = None
    role = None
    profit = None
    total_portfolio = None
    available_funds = None
    total_stock_values = None
    total_deposited = None

    def __init__(self):
        self.login = None
        self.password = None
        self.role = None
        self.profit = None
        self.total_portfolio = None
        self.available_funds = None
        self.total_stock_values = None
        self.total_deposited = None

    def populate_users_model(self, user):
        result = db.query("select * from users where login = ('%s')"%(user)+";")
        if result:
            self.login = result[0][1]
            self.password = result[0][2]
            self.role = result[0][3]
            self.profit = result[0][4]
            self.total_portfolio = result[0][5]
            self.available_funds = result[0][6]
            self.total_stock_values = result[0][7]
            self.total_deposited = result[0][8]

    def get_login(self):
        return self.login

    def set_login(self, x):
        self.login = x

    def get_password(self):
        return self.password

    def set_password(self,x):
        self.password = x

    def get_role(self):
        return self.role

    def set_role(self,x):
        #user, admin, owner
        self.role = x

    def get_profit(self):
        return self.profit

    def set_profit(self,x):
        self.profit = x

    def get_total_portfolio(self):
        return self.total_portfolio

    def set_total_portfolio(self,x):
        self.total_portfolio = x

    def get_available_funds(self):
        return self.available_funds

    def set_available_funds(self,x):
        self.available_funds = x

    def get_total_stock_values(self):
        return self.total_stock_values

    def set_total_stock_values(self,x):
        self.total_stock_values = x

    def get_total_deposited(self):
        return self.total_deposited

    def set_total_deposited(self,x):
        self.total_deposited = x

#u = Users()
#u.populate_users_model('al356')
#print u.get_profit()
