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

    def insert(self, user, trans_type, stock, price, total_price, volume, algo_id):
        self.db.query("insert into history (user, trans_type, stock, price, total_price, volume, algo_id) values ('%s','%s','%s','%s','%s',%s,'%s')"%(user, trans_type, stock, round(Decimal(price),2), round(Decimal(total_price),2), volume, algo_id)+";")

    def select_all(self, user):
        result = self.db.query("select * from history where user=('%s')"%(user)+";")
        if result:
            l=[]
            for i in range(len(result)):
                h = History(user, result[i]['trans_date'], result[i]['trans_type'], result[i]['stock'], result[i]['price'], result[i]['total_price'], result[i]['volume'], result[i]['algo_id'])
                l.append(h)
            return l

    def select_all_algo_trades(self, user):
        result = self.db.query("select * from history where user=('%s') and algo_id != '0'"%(user)+";")
        if result:
            l=[]
            for i in range(len(result)):
                h = History(user, result[i]['trans_date'], result[i]['trans_type'], result[i]['stock'], result[i]['price'], result[i]['total_price'], result[i]['volume'], result[i]['algo_id'])
                l.append(h)
            return l

    def select_all_user_trades(self, user):
        result = self.db.query("select * from history where user=('%s') and algo_id = '0'"%(user)+";")
        if result:
            l=[]
            for i in range(len(result)):
                h = History(user, result[i]['trans_date'], result[i]['trans_type'], result[i]['stock'], result[i]['price'], result[i]['total_price'], result[i]['volume'], result[i]['algo_id'])
                l.append(h)
            return l

    def select_algo_trades(self, user, algo_id):
        result = self.db.query("select * from history where user=('%s') and algo_id = '%s'"%(user, algo_id)+";")
        if result:
            l=[]
            for i in range(len(result)):
                h = History(user, result[i]['trans_date'], result[i]['trans_type'], result[i]['stock'], result[i]['price'], result[i]['total_price'], result[i]['volume'], result[i]['algo_id'])
                l.append(h)
            return l

        
