#!/usr/bin/python

import sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from user_stock_value_model import User_stock_value
from PDO import PDO

class User_stock_value_dao:
    
    db = None

    def __init__(self):
        self.db =  PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)
        
    def insert(self, user, profit, total_stock_values):
        self.db.query("insert into user_stock_value values ('%s','%s','%s')"%(user, profit, total_stock_values)+";")

    def update_profit(self, user, profit):
        self.db.query("update user_stock_value set profit=('%s') where user=('%s')"%(Decimal(profit), user)+";")
        
    def update_total_stock_values(self, user, total_stock_values):
        self.db.query("update user_stock_value set total_stock_values=('%s') where user=('%s')"%(Decimal(total_stock_values), user)+";")

    def get_user_stock_value_model(self, user):
        result = self.db.query("select * from user_stock_value where user = ('%s')"%(user)+";")
        if result:
            u = User_stock_value(user, result[0]['profit'],result[0]['total_stock_values'])
            return u
