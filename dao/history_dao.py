#!/usr/bin/python

import sys, LINK_HEADERS,datetime
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from history_model import History
from PDO import PDO

class History_dao:

    db = None

    def __init__(self):
        self.db =  PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)

    def insert(self, user, trans_date, trans_type, stock, price, total_price, volume):
        self.db.query("insert into history values ('%s','%s','%s','%s','%s','%s',%d)"%(user, trans_date, trans_type, stock, price, total_price, volume)+";")

    def select_all(self, user):
        result = self.db.query("select * from history where user=('%s')"%(user)+";")
        if result:
            l=[]
            for i in range(len(result)):
                h = History(user, result[i]['trans_date'], result[i]['trans_type'], result[i]['stock'], result[i]['price'], result[i]['total_price'], result[i]['volume'])
                l.append(h)
            return l

    
        
