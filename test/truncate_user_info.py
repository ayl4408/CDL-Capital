#!/usr/bin/python

import cgi, datetime,sys,LINK_HEADERS
import simplejson as json
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from user_portfolio_dao import User_portfolio_dao
from user_stock_value_dao import User_stock_value_dao
from transaction_dao import Transaction_dao

t = Transaction_dao()
up = User_portfolio_dao()
usv = User_stock_value_dao()

#portfolio = up.get_user_portfolio_model('al356')
#stock_value = usv.get_user_stock_value_model('al356')

username = 'kad34'

usv.update_profit(username,'0')
usv.update_total_stock_values(username,'0')

up.update_total_portfolio(username, '0')
up.update_total_deposited(username,'0')
up.update_available_funds(username,'0')
