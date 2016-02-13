#!/usr/bin/python

import cgi, datetime, LINK_HEADERS, sys
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from users_class import Users
from decimal import *

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
    
if form.getvalue("amount") != None:
    amount = form.getvalue("amount")

u = Users()
u.populate_users_model(username)

u.set_total_portfolio(Decimal(u.get_total_portfolio()) + Decimal(amount))
u.set_available_funds(u.get_available_funds() + Decimal(amount))
u.set_total_deposited(u.get_total_deposited() + Decimal(amount))
