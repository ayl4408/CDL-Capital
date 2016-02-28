#!/usr/bin/python

import cgi, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from decimal import *
from user_portfolio_dao import User_portfolio_dao

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")

if form.getvalue("amount") != None:
    amount = form.getvalue("amount")

#username='al356'
#amount='1000000'
    
udao = User_portfolio_dao()
u = udao.get_user_portfolio_model(username)

final_deposited = Decimal(u.get_total_deposited()) + Decimal(amount)
final_portfolio = Decimal(u.get_total_portfolio()) + Decimal(amount)
final_available = Decimal(u.get_available_funds()) + Decimal(amount)

udao.update_total_deposited(username, final_deposited)
udao.update_total_portfolio(username, final_portfolio)
udao.update_available_funds(username, final_available)
