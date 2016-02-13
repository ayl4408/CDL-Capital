#!/usr/bin/python

import cgi, datetime, sys
import simplejson as json
sys.path.insert(0,'/usr/lib/cgi-bin/alee_cdlcapital/back')
from database_class import DB

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
else:
    print "Location: http://cdl.ddns.net:4098/cgi-bin/alee_cdlcapital/home.py"

#username="al356"
    
db = DB('localhost', 'root', 'mmGr2016', 'cdlcapital')

result1 = db.query("select * from users where login = ('%s')"%(str(username))+";")
result2 = db.query("select * from transactions where user = ('%s')"%(str(username))+";")
result3 = db.query("select * from owned_stocks where stock_owner = ('%s')"%(str(username))+";")

data={}

if result1:
    data['users']={}
    data['users']['profit']=result1[0][4]
    data['users']['total_portfolio']=result1[0][5]
    data['users']['available_funds']=result1[0][6]
    data['users']['total_stock_values']=result1[0][7]
    data['users']['total_deposited']=result1[0][8]

if result2:
    data['transactions']={}
    for i in range(len(result2)):
        data['transactions'][i]={}
        data['transactions'][i]['trans_date']=result2[i][1].strftime('%Y-%m-%d %h:%m:%s')
        data['transactions'][i]['trans_type']=result2[i][2]
        data['transactions'][i]['stock']=result2[i][3]
        data['transactions'][i]['price']=result2[i][4]
        data['transactions'][i]['volume']=result2[i][5]
        data['transactions'][i]['total_price']=result2[i][6]

if result3:
    data['owned_stocks']={}
    for i in range(len(result3)):
        data['owned_stocks'][i]={}
        data['owned_stocks'][i]['stock']=result3[i][0]
        data['owned_stocks'][i]['current_shares']=result3[i][1]
        data['owned_stocks'][i]['current_price']=result3[i][2]
        data['owned_stocks'][i]['total_worth']=result3[i][3]
        data['owned_stocks'][i]['profit']=result3[i][5]

json_result = json.dumps(data)
print json_result
