#!/usr/bin/python

from company_model import Company

class Active_company(Company):

    def __init__(self):
	self.volume = None
	self.avg_daily_volume = None
	self.percent_change = None

    def get_avg_daily_volume(self):
	return self.avg_daily_volume

    def set_avg_daily_volume(self,x):
	self.avg_daily_volume = x

    def get_percent_change(self):
	return self.percent_change

    def set_percent_change(self,x):
	self.percent_change = x

