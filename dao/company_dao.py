#!/usr/bin/python

import cgi, sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from PDO import PDO
from company_model import Company
from company_base_model import Company_base
from moving_average_model import Moving_average
from active_company_model import Active_company

class Company_dao:

    db = None

    def __init__(self):
        self.db =  PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)
                           
    def get_all_ask(self):
        result = self.db.query("select Symbol, Name, Ask from company_info;")
        if result:
            l=[]
            for i in range(len(result)):
                if result[i]['Ask'] != None:
                    c = Company_base()
                    c.set_name(result[i]['Name'])
                    c.set_ask(result[i]['Ask'])
                    c.set_symbol(result[i]['Symbol'])
                    l.append(c)
            return l
                
    def get_company_model(self, symbol):
        result = self.db.query("select * from company_info where symbol = ('%s')"%(symbol)+";")
        if result:
            c = Company()
            c.set_ask(result[0]['Ask'])
            c.set_name(result[0]['Name'])
            #c.set_percent_change(result[0]['PercentChange']) 
            c.set_symbol(symbol)
            #c.set_avg_daily_volume(result[0]['AverageDailyVolume'])
            c.set_volume(result[0]['Volume'])
            return c

    def get_all_companies_percentchange(self):
	    result = self.db.query("select symbol, PercentChange from company_info  WHERE PercentChange IS NOT NULL AND PercentChange!='None';")
	    if result:
	        l = []
	        for i in range(len(result)):
	    	    c = Active_company()
	    	    c.set_symbol(result[i]['symbol'])
	    	    #r = result[i]['PercentChange'].translate(None, '+%')
	    	    #c.set_percent_change(r)
	    	    c.set_percent_change(result[i]['PercentChange'])#.translate(None, '+%'))
	    	    #c.set_volume(result[i]['Volume'])
	    	    #c.set_avg_daily_volume(result[i]['AverageDailyVolume'])
	    	    l.append(c)
	        return l
	
    def get_all_companies_volume(self):
	     result = self.db.query("select symbol, Volume from company_info;")
	     if result:
	         l = []
	         for i in range(len(result)):
	     	    c = Active_company()
	     	    c.set_symbol(result[i]['symbol'])
	     	    c.set_volume(result[i]['Volume'])
	     	    l.append(c)
	         return l

    
    def get_all_companies_averagedailyvolume(self): #NOT TO SELF: fix the averagedailyvolume and avg_daily_volume difference
         result = self.db.query("select symbol, AverageDailyVolume from company_info;")
         if result:
             l = []
             for i in range(len(result)):
                 c = Active_company()
                 c.set_symbol(result[i]['symbol'])
                 c.set_avg_daily_volume(result[i]['AverageDailyVolume'])
                 l.append(c)
             return l


    def get_all_companies_stock(self):
        result = self.db.query("select Symbol from company_info;")
        if result:
            l = []
            for i in range(len(result)):
                c = Company_base()
                c.set_symbol(result[i]['Symbol'])
                l.append(c)
            return l   

    def get_moving_average(self):
	     result = self.db.query("SELECT Symbol, Ask, FiftydayMovingAverage, TwoHundreddayMovingAverage FROM company_info WHERE FiftydayMovingAverage!='None' and TwoHundreddayMovingAverage!='None' and ask!='None';")
	     if result:
	         l = []
	         for i in range(len(result)):
	     	    c = Moving_average()
	     	    c.set_symbol(result[i]['Symbol'])
	     	    c.set_ask(result[i]['Ask'])
	     	    c.set_fifty_day_ask(result[i]["FiftydayMovingAverage"])
	     	    c.set_two_hundred_day_ask(result[i]['TwoHundreddayMovingAverage'])
	     	    l.append(c)
	         return l
	     else: #DO THIS FOR ALL 
	         return False

    def get_ask_comp(self, symbols):
        result = self.db.query("select symbol, ask from company_info where symbol in (" + symbols + ");") 
        if result:
            l = []
            for i in range(len(result)):
                c = Company_base()
                c.set_ask(result[i]['ask'])
                c.set_symbol(result[i]['symbol'])
                l.append(c)
            return l
