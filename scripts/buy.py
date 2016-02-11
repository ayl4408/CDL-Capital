#!/usr/bin/python

import cgi, datetime,sys
import simplejson as json
from decimal import *
from yahoo_finance_class import YQLQuery
sys.path.insert(0,'/usr/lib/cgi-bin/alee_cdlcapital/models')
from users_class import Users
from transactions_class import Transactions
from owned_stocks_class import Owned_stocks

print "Content-Type: text/html\r\n\r\n"

#Get form data
form = cgi.FieldStorage()
if form.getvalue("username") != None:
    username = form.getvalue("username")
if form.getvalue("volume") != None:
    volume = int(form.getvalue("volume"))
if form.getvalue("company") != None:
    company = form.getvalue("company")
    
#test variables
#username="al356"
#company='GOOG'
#volume=1

#Declare globals objects
yql = YQLQuery()
u = Users()
u.populate_users_model(username)

#Declare global variables
time = datetime.datetime.utcnow()
trans_type = 'buy'


def calculate_price():
    ask_price = yql.get_ask_price(str(company))
    final_price = Decimal(ask_price) * int(volume)
    return ask_price, final_price

def update_transactions(ask_price, final_price):
    t = Transactions(username, time, trans_type, company, ask_price, volume, final_price)
    t.insert_transactions_model()
    
def calculate_portfolio(final_price):
    u.set_available_funds(str(Decimal(u.get_available_funds()) - Decimal(final_price)))
    u.set_total_stock_values(str(Decimal(u.get_total_stock_values()) + Decimal(final_price)))

def update_owned_stocks(ask_price, final_price):
    o = Owned_stocks()
    exists = o.populate_owned_stocks_model(username, company)
    if exists == True:
        o.set_current_shares(o.get_current_shares() + volume)
        o.set_current_price(ask_price)
        o.set_total_worth(o.get_current_shares() * o.get_current_price())
    else:
        o.insert_owned_stocks_model(company, volume, ask_price, final_price, username)
        
def main():
    ask_price, final_price = calculate_price()
    
    if final_price <= u.get_available_funds():
        update_transactions(ask_price, final_price)
        calculate_portfolio(final_price)
        update_owned_stocks(ask_price, final_price)

main()
    

    
