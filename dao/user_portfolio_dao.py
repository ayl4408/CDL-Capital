#!/usr/bin/python

import sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from user_portfolio_model import User_portfolio
from PDO import PDO

class User_portfolio_dao:

    db = None

    def __init__(self):
        self.db =  PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)
        
    def insert(self, user, total_portfolio, available_funds, total_deposited):
        self.db.query("insert into user_portfolio values ('%s','%s','%s','%s')"%(user, total_portfolio, available_funds, total_deposited)+";")

    def update_total_portfolio(self, user, total):
        self.db.query("update user_portfolio set total_portfolio=('%s') where user=('%s')"%(Decimal(total), user)+";")

    def update_available_funds(self, user, available_funds):
        self.db.query("update user_portfolio set available_funds=('%s') where user=('%s')"%(Decimal(available_funds), user)+";")

    def update_total_deposited(self, user, funds):
        self.db.query("update user_portfolio set total_deposited=('%s') where user=('%s')"%(Decimal(funds), user)+";")
        
    def get_user_portfolio_model(self, user):
        result = self.db.query("select * from user_portfolio where user = ('%s')"%(user)+";")
        if result:
            u = User_portfolio(user,result[0]['total_portfolio'],result[0]['available_funds'],result[0]['total_deposited'])
            return u
