#!/usr/bin/python

import cgi, datetime
import simplejson as json
from database_class import DB
from decimal import *

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
    
if form.getvalue("amount") != None:
    amount = form.getvalue("amount")

#username="al356"
#amount="100.00"

db = DB('localhost', 'root', 'mmGr2016', 'cdlcapital')

result1 = db.query("select total_portfolio, available_funds, total_deposited from users where login = ('%s')"%(str(username))+";")

if result1:
    total = Decimal(result1[0][0]) + Decimal(amount)
    available = Decimal(result1[0][1]) + Decimal(amount)
    deposited = Decimal(result1[0][2]) + Decimal(amount)
    db.query("update users set total_portfolio=('%s')"%(total) +" , available_funds=('%s')"%(available) +" , total_deposited=('%s')"%(deposited) +" where login=('%s')"%(str(username))+";")
