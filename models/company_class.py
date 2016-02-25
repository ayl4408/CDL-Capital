#/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

db=DB("localhost", "root", "mmGr2016", "cdlcapital")

class Company:

    ask = None
    symbol = None
    name = None

    def __init__(self):
        self.ask = None
        self.symbol = None
        self.name = None

    def populate(self, symbol):
        sql="SELECT Ask, Name FROM company_info WHERE symbol=" +"'"+ symbol + "'" + ";"
        result=db.query(sql)
        if result:
            self.ask = result[0]['Ask']
            self.symbol = symbol
            self.name = result[0]['Name']

    def get_ask(self):
        return self.ask

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def get_all_percentchange(self):
	return db.query("SELECT symbol, PercentChange FROM company_info WHERE PercentChange IS NOT NULL AND PercentChange!='None';")

    def get_all_volume(self):
	return db.query("SELECT symbol, Volume FROM company_info WHERE Volume IS NOT NULL AND Volume!='None';")

    def get_all_averagedailyvolume(self):
	return db.query("SELECT symbol, AverageDailyVolume FROM company_info WHERE AverageDailyVolume IS NOT NULL AND AverageDailyVolume!='None';")
	
	
	
