#!/usr/bin/python

import sys, LINK_HEADERS,datetime
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from transaction_model import Transaction
from owned_stock_model import Owned_stock
from user_stock_value_model import User_stock_value
from PDO import PDO

class Transaction_dao:

     db = None

     def __init__(self):
          self.db =  PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)

     def select(self):
          result = self.db.query("select * from transactions;")
          if result:
               l = []
               for i in range(len(result)):
                    t = Transaction(result[i]['user'],result[i]['trans_date'],result[i]['stock'],result[i]['price'],result[i]['sold'],result[i]['order_id'],result[i]['profit'],result[i]['algo_id'])
                    l.append(t)
               return l

     def update_profit(self, user, trans_date, order_id, profit, stock, algo_id):
          self.db.query("update transactions set profit=('%s') where user=('%s') and trans_date=('%s') and order_id=('%s') and stock=('%s') and algo_id=('%s')"%(round(Decimal(profit), 2), user, trans_date, order_id, stock, algo_id)+";")
          
     def select_all(self, user):
          result = self.db.query("select * from transactions where user=('%s')"%(user)+";")
          if result:
               l = []
               for i in range(len(result)):
                    t = Transaction(result[i]['user'],result[i]['trans_date'],result[i]['stock'],result[i]['price'],result[i]['sold'],result[i]['order_id'],result[i]['profit'],result[i]['algo_id'])
                    l.append(t)
               l.sort(key=lambda x: x.get_trans_date(), reverse=False)
               return l

     def select_all_active(self, user):
          result = self.db.query("select * from transactions where user=('%s') and sold='0'"%(user)+";")
          if result:
               l = []
               for i in range(len(result)):
                    t = Transaction(result[i]['user'],result[i]['trans_date'],result[i]['stock'],result[i]['price'],result[i]['sold'],result[i]['order_id'],result[i]['profit'],result[i]['algo_id'])
                    l.append(t)
               l.sort(key=lambda x: x.get_trans_date(), reverse=False)
               return l

     def select_all_sold(self, user):
          result = self.db.query("select * from transactions where user=('%s') and sold='1'"%(user)+";")
          if result:
               l = []
               for i in range(len(result)):
                    t = Transaction(result[i]['user'],result[i]['trans_date'],result[i]['stock'],result[i]['price'],result[i]['sold'],result[i]['order_id'],result[i]['profit'],result[i]['algo_id'])
                    l.append(t)
               l.sort(key=lambda x: x.get_trans_date(), reverse=False)
               return l

     def buy(self,user, trans_date, stock, volume, price, algo_id):
          for i in range(volume):
               self.db.query("insert into transactions (user, trans_date, stock, price, sold, order_id, profit, algo_id) values ('%s','%s','%s',%f,'%s',%d,%f,'%s')"%(user, trans_date, stock, round(Decimal(price), 2), 0, int(i), Decimal(0), algo_id)+";")

     def sell(self, user, stock, volume, price, algo_id):
          result = self.db.query("select * from transactions where user=('%s') and stock=('%s') and sold='0'"%(user, stock)+" ORDER BY trans_date ASC, order_id ASC LIMIT "+str(volume)+";")
          time = datetime.datetime.utcnow()
          if result:
               if len(result) >= volume:
                    for i in range(len(result)):
                         profit = round(Decimal(price) - Decimal(result[i]['price']), 2)
                         self.db.query("update transactions set sold='1', profit=('%s'), trans_date=('%s') where user=('%s') and stock=('%s') and trans_date=('%s') and order_id=(%d) and algo_id=('%s')"%(Decimal(profit), str(time), user, stock, result[i]['trans_date'], result[i]['order_id'], algo_id)+";")

     def get_user_stock_list(self, user):
          result = self.db.query("select distinct stock from transactions where user=('%s') and sold='0'"%(user)+";")
          if result:
              l=[]
              for i in range(len(result)):
                   l.append(result[i]['stock'])
              return l
     
     #def get_user_owned_stocks_list(self, user):
     #     result=self.db.query("select distinct stock from transactions where user=('%s') and sold='0'"%(user) + ";")
     #     if result:
     #         l=[]
     #         for i in range(len(result)):
     #             l.append(result[i]['stock'])
     #         return l

     def get_owned_stock_model(self, user, stock, price):
          volume_result= self.db.query("select count(*) from transactions where user=('%s') and stock=('%s') and sold='0'"%(user, stock)+";")
          profit_result = self.db.query("select sum(profit) from transactions where user=('%s') and stock=('%s') and sold='0'"%(user, stock)+";")
          if volume_result and profit_result:
               volume = int(volume_result[0]['count(*)'])
               total_worth = int(volume) * Decimal(price)
               if profit_result[0]['sum(profit)'] != None:
                    profit = Decimal(profit_result[0]['sum(profit)'])
               else:
                    profit = 0
               o = Owned_stock(stock, volume, price, total_worth, profit)
               return o

     def get_user_stock_value_model(self, user):
          result1 = self.db.query("select sum(profit) from transactions where user=('%s') and sold='1'"%(user)+";")
          result2 = self.db.query("select sum(price) from transactions where user=('%s') and sold='0'"%(user)+";")
          if result1[0]['sum(profit)'] != None:
               profit = Decimal(result1[0]['sum(profit)'])
          else:
               profit = 0
               
          if result2[0]['sum(price)'] != None:
               total_stock_values =  Decimal(result2[0]['sum(price)'])
          else:
               total_stock_values = 0
               
          u = User_stock_value(user, profit, total_stock_values)
          return u
