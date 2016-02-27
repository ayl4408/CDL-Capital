#!/usr/bin/python

class Company:
    name = None
    symbol = None
    ask = None
    volume = None
    avg_daily_volume = None
    percent_change = None

    def __init__(self):
        self.name = None
        self.symbol = None
        self.ask = None
        self.volume = None
        self.avg_daily_volume = None
        self.percent_change = None

    def get_name(self):
        return self.name

    def set_name(self,x):
        self.name = x

    def get_symbol(self):
        return self.symbol

    def set_symbol(self,x):
        self.symbol = x

    def get_ask(self):
        return self.ask

    def set_ask(self,x):
        self.ask = x

    def get_volume(self):
        return self.volume

    def set_volume(self,x):
        self.volume = x

    def get_avg_daily_volume(self):
        return self.avg_daily_volume

    def set_avg_daily_volume(self,x):
        self.avg_daily_volume = x

    def get_percent_change(self):
        return self.percent_change

    def set_percent_change(self,x):
        self.percent_change = x

    
