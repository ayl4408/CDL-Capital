#/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

db=DB("localhost", "root", "mmGr2016", "cdlcapital")

class Company:
    ask = None
    symbol = None
    name = None


    def __init__(self, ask, symbol, name):
        self.ask = ask
        self.symbol = symbol
        self.name = name

    def get_ask(self):
        return self.ask

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name
