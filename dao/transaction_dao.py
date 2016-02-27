#!/usr/bin/python

import sys, LINK_HEADERS,datetime
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from transaction_model import Transaction
from owned_stock_model import Owned_stock
from user_stock_value_model import User_stock_value

class Transaction_dao:

     db = None

     def __init__(self):
         self.db = DB(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)                     
     def select_all(self, user):
          result = self.db.query("select * from transactions where user=('%s')"%(user)+";")
          if result:
               l = []
               for i in range(len(result)):
                    t = Transaction(result[i]['user'],result[i]['trans_date'],result[i]['stock'],result[i]['price'],result[i]['sold'],result[i]['order_id'],result[i]['profit'])
                    l.append(t)
               l.sort(key=lambda x: x.get_trans_date(), reverse=False)
               return l

     def select_all_active(self, user):
          result = self.db.query("select * from transactions where user=('%s') and sold='0'"%(user)+";")
          if result:
               l = []
               for i in range(len(result)):
                    t = Transaction(result[i]['user'],result[i]['trans_date'],result[i]['stock'],result[i]['price'],result[i]['sold'],result[i]['order_id'],result[i]['profit'])
                    l.append(t)
               l.sort(key=lambda x: x.get_trans_date(), reverse=False)
               return l

     def select_all_sold(self, user):
          result = self.db.query("select * from transactions where user=('%s') and sold='1'"%(user)+";")
          if result:
               l = []
               for i in range(len(result)):
                    t = Transaction(result[i]['user'],result[i]['trans_date'],result[i]['stock'],result[i]['price'],result[i]['sold'],result[i]['order_id'],result[i]['profit'])
                    l.append(t)
               l.sort(key=lambda x: x.get_trans_date(), reverse=False)
               return l

     def buy(self,user, trans_date, stock, volume, price):
          for i in range(volume):
               self.db.query("insert into transactions values ('%s','%s','%s',%f,'%s',%d,%f)"%(user, trans_date, stock, Decimal(price), 0, int(i), Decimal(0))+";")

     def sell(self, user, stock, volume, price):
          result = self.db.query("select * from transactions where user=('%s') and stock=('%s') and sold='0'"%(user, stock)+" ORDER BY trans_date ASC, order_id ASC LIMIT "+str(volume)+";")
          time = datetime.datetime.utcnow()
          if result:
               if len(result) >= volume:
                    for i in range(len(result)):
                         profit = Decimal(price) - Decimal(result[i]['price'])
                         self.db.query("update transactions set sold='1', profit=('%s'), trans_date=('%s') where user=('%s') and stock=('%s') and trans_date=('%s') and order_id=(%d)"%(Decimal(profit), str(time), user, stock, result[i]['trans_date'], result[i]['order_id'])+";")

     def get_user_stock_list(self, user):
          result = self.db.query("select distinct stock from transactions where user=('%s')"%(user)+";")
          if result:
               l=[]
               for i in range(len(result)):
                    l.append(result[i]['stock'])
               return l
     
     def get_user_owned_stocks_list(self, user):
          result=self.db.query("select distinct stock from transactions where user=('%s') and sold='0'"%(user) + ";")
          return result

     def get_owned_stock_model(self, user, stock, price):
          volume_result= self.db.query("select count(*) from transactions where user=('%s') and stock=('%s') and sold='0'"%(user, stock)+";")
          profit_result = self.db.query("select sum(profit) from transactions where user=('%s') and stock=('%s')"%(user, stock)+";")
          if volume_result and profit_result:
               volume = int(volume_result[0]['count(*)'])
               total_worth = int(volume) * Decimal(price)
               profit = Decimal(profit_result[0]['sum(profit)'])
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
