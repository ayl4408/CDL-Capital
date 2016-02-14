#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
else:
    print "Location: http://cdl.ddns.net:4098/cgi-bin/alee_cdlcapital/home.py"

username="al356"

db = DB('localhost', 'root', 'mmGr2016', 'cdlcapital')

result1 = db.query("select * from users where login = ('%s')"%(str(username))+";")
result2 = db.query("select * from transactions where user = ('%s')"%(str(username))+";")
result3 = db.query("select * from owned_stocks where stock_owner = ('%s')"%(str(username))+";")

data={}

if result1:
    data['users']={}
    data['users']['profit']=result1[0]['profit']
    data['users']['total_portfolio']=result1[0]['total_portfolio']
    data['users']['available_funds']=result1[0]['available_funds']
    data['users']['total_stock_values']=result1[0]['total_stock_values']
    data['users']['total_deposited']=result1[0]['total_deposited']

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
        data['owned_stocks'][i]={}
        data['owned_stocks'][i]['stock']=result3[i]['stock']
        data['owned_stocks'][i]['current_shares']=result3[i]['current_shares']
        data['owned_stocks'][i]['current_price']=result3[i]['current_price']
        data['owned_stocks'][i]['total_worth']=result3[i]['total_worth']
        data['owned_stocks'][i]['profit']=result3[i]['profit']

json_result = json.dumps(data)
print json_result
