#!/usr/bin/python

import time, sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.SERVICE_LINK))
from transaction_service import transaction

class Algorithm:

    def __init__(self, company_model_list):
	self.company_model_list = company_model_list

    def algorithm_1(self, username):
	for company_model in self.company_model_list:
	    ask = company_model.get_ask()
	    if (ask is not None and ask!="None"):
	    	if Decimal(ask) > 50 and Decimal(ask) < 75:
		    transaction(username, 1, company_model.get_symbol(), "buy", "1")
   
