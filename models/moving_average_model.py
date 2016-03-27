#!/usr/bin/python

from company_model import Company

class Moving_average(Company):

    def __init__(self):
        self.fifty_day_ask = None
        self.two_hundred_day_ask = None

    def set_fifty_day_ask(self, x):
        self.fifty_day_ask = x

    def get_fifty_day_ask(self):
        return self.fifty_day_ask

    def set_two_hundred_day_ask(self, x):
        self.two_hundred_day_ask = x

    def get_two_hundred_day_ask(self):
        return self.two_hundred_day_ask
