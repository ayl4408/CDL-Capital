#!/usr/bin/python

import sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from PDO import PDO
from company_model import Company

class Company_dao:

    db = None

    def __init__(self):
        self.db =  PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)
                           
    def get_company_model(self, symbol):
        result = self.db.query("select * from company_info where symbol = ('%s')"%(symbol)+";")
        if result:
            c = Company()
            c.set_ask(result[0]['Ask'])
            c.set_name(result[0]['Name'])
            #c.set_ask(result[0]['']) #percent change
            c.set_symbol(symbol)
            c.set_avg_daily_volume(result[0]['AverageDailyVolume'])
            c.set_volume(result[0]['Volume'])
            return c
