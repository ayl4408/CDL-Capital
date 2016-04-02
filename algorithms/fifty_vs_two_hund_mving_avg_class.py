#!/usr/bin/python

import time, sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.SERVICE_LINK))
from transaction_service import transaction
from transaction_dao import Transaction_dao
from company_dao import Company_dao
from active_algorithms_dao import Active_algorithms_dao


class fifty_vs_two_hund_mving_avg:

    def __init__(self, active_algorithms_list):
        self.moving_list = None
	self.t = Transaction_dao()
	self.c = Company_dao()
	for aam in active_algorithms_list:
            if aam.get_algo_id() == "3":
		if self.moving_list == None:
		    self.moving_list = self.c.get_moving_average()
		if self.moving_list: 
        	    self.algorithm(aam.get_user())
		

    def algorithm(self, username):
	owned_stocks = self.t.get_user_stock_list(username)
	for moving in self.moving_list:
	    symbol = moving.get_symbol()
	    if owned_stocks:
	        if symbol in owned_stocks:
		    if moving.get_fifty_day_ask() > moving.get_two_hundred_day_ask():
		        transaction(username, 1, symbol, "sell", "2")
		if symbol not in owned_stocks:	
		    if moving.get_fifty_day_ask() < moving.get_two_hundred_day_ask():
		        transaction(username, 1, symbol, "buy", "2")
	    else:
		if moving.get_fifty_day_ask() < moving.get_two_hundred_day_ask():
		        transaction(username, 1, symbol, "buy", "2")
	    


   
