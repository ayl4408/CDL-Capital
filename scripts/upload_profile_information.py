#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from users_class import Users
from transactions_class import Transactions
from owned_stocks_class import Owned_stocks

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
   
u = Users()
u.populate(username)

t = Transactions()
result2=t.select_all(username)

o = Owned_stocks()
result3=o.select_all(username)

data={}

data['users']={}
data['users']['profit']=u.get_profit()
data['users']['total_portfolio']=u.get_total_portfolio()
data['users']['available_funds']=u.get_available_funds()
data['users']['total_stock_values']=u.get_total_stock_values()
data['users']['total_deposited']=u.get_total_deposited()

if result2:
    data['transactions']={}
    for i in range(len(result2)):
        data['transactions'][i]={}
        data['transactions'][i]['trans_date']=result2[i]['trans_date'].strftime('%Y-%m-%d %h:%m:%s')
        data['transactions'][i]['trans_type']=result2[i]['trans_type']
        data['transactions'][i]['stock']=result2[i]['stock']
        data['transactions'][i]['price']=result2[i]['price']
        data['transactions'][i]['volume']=result2[i]['volume']
        data['transactions'][i]['total_price']=result2[i]['total_price']

if result3:
    data['owned_stocks']={}
    for i in range(len(result3)):
        if result3[i]['current_shares'] > 0:
            data['owned_stocks'][i]={}
            data['owned_stocks'][i]['stock']=result3[i]['stock']
            data['owned_stocks'][i]['current_shares']=result3[i]['current_shares']
            data['owned_stocks'][i]['current_price']=result3[i]['current_price']
            data['owned_stocks'][i]['total_worth']=result3[i]['total_worth']
            data['owned_stocks'][i]['profit']=result3[i]['profit']

json_result = json.dumps(data)
print json_result
