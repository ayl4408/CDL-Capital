#!/usr/bin/python

import sys, LINK_HEADERS,datetime
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from history_model import History
from date_history_model import Date_history
from PDO import PDO
from algorithms_detail_model import Algorithm_details
from company_model import Company

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
    
    def get_algorithm_buy_sell_volume(self, user):
        result1= self.db.query("select count(trans_type) as buy, algo_id, sum(volume) as volume from history where user=('%s') and trans_type = 'buy' group by algo_id order by algo_id"%(user) + ";")
        result2= self.db.query("select count(trans_type) as sell, algo_id, sum(volume) as volume from history where user=('%s') and trans_type = 'sell' group by algo_id order by algo_id"%(user) + ";")
        if result1 or result2:
            l=[]
            iterations=max(len(result1), len(result2))
            for i in range(iterations):
                ad=Algorithm_details(user, result1[i]['algo_id'],str(int(result1[i]['volume']) + int(result2[i]['volume'])), result1[i]['buy'], result2[i]['sell'])
                l.append(ad)
            return l 
           
    def get_distinct_traded_stocks(self, user):
        result = self.db.query("select distinct stock from history where user=('%s')"%(user) + ";")
        if result:
            l=[]
            for i in range(len(result)):
                c = Company()
                c.set_name(result[i]['stock'])
                l.append(c)
        return l 

    def get_all_volume_per_day(self,user):
        result = self.db.query("select UNIX_TIMESTAMP(DATE(trans_date))*1000 as date, sum(volume) as volume from history where user=('%s') group by DATE(trans_date)"%(user)+";");
        if result:
            l = []
            for i in range(len(result)):
                t = Date_history()
                t.set_date(result[i]['date'])
                t.set_volume(result[i]['volume'])
                l.append(t)
            return l
        else:
            return False

    def get_user_volume_per_day(self,user):
        result = self.db.query("select UNIX_TIMESTAMP(DATE(trans_date))*1000 as date, sum(volume) as volume from history where user=('%s') and algo_id='0' group by DATE(trans_date)"%(user)+";");
        if result:
            l = []
            for i in range(len(result)):
                t = Date_history()
                t.set_date(result[i]['date'])
                t.set_volume(result[i]['volume'])
                l.append(t)
            return l
        else:
            return False

    def get_all_algorithms_volume_per_day(self,user):
        result = self.db.query("select UNIX_TIMESTAMP(DATE(trans_date))*1000 as date, sum(volume) as volume from history where user=('%s') and algo_id!='0' group by DATE(trans_date)"%(user)+";");
        if result:
            l = []
            for i in range(len(result)):
                t = Date_history()
                t.set_date(result[i]['date'])
                t.set_volume(result[i]['volume'])
                l.append(t)
            return l
        else:
            return False

    def get_algorithm_volume_per_day(self,user,algo_id):
        result = self.db.query("select UNIX_TIMESTAMP(DATE(trans_date))*1000 as date, sum(volume) as volume from history where user=('%s') and algo_id=('%s') group by DATE(trans_date)"%(user, algo_id)+";");
        if result:
            l = []
            for i in range(len(result)):
                t = Date_history()
                t.set_date(result[i]['date'])
                t.set_volume(result[i]['volume'])
                l.append(t)
            return l
        else:
            return False




#h = History_dao()
#print h.get_algorithm_volume_per_day("al356", '3')
            
        
