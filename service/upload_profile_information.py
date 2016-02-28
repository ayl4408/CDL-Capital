#!/usr/bin/python

import cgi, sys, LINK_HEADERS
import simplejson as json
from datetime import datetime
from dateutil import tz
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao
from user_portfolio_dao import User_portfolio_dao
from user_stock_value_dao import User_stock_value_dao
from company_dao import Company_dao
from history_dao import History_dao

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")

#username='al356'
    
tdao = Transaction_dao()
u2 = User_stock_value_dao()
u1 = User_portfolio_dao()
cdao = Company_dao()
hdao = History_dao()

usv = tdao.get_user_stock_value_model(username)
up = u1.get_user_portfolio_model(username)

data={}

data['users']={}
data['users']['profit'] = usv.get_profit()
data['users']['total_portfolio'] = up.get_total_portfolio()
data['users']['available_funds'] = up.get_available_funds()
data['users']['total_stock_values'] = usv.get_total_stock_values()
data['users']['total_deposited'] = up.get_total_deposited()

t = hdao.select_all(username)

if t:
    data['transactions']={}
    for i in range(len(t)):
        data['transactions'][i]={}
	
	#start date formatting
	from_zone = tz.tzutc()
	to_zone = tz.tzlocal()

        date_time = t[i].get_trans_date()

	date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
	date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')	

	date_time = date_time.replace(tzinfo=from_zone)
	updated_date_time = date_time.astimezone(to_zone)

	
	updated_date_time = updated_date_time.strftime('%Y-%m-%d %H:%M:%S')
	#end date formatting	

        data['transactions'][i]['trans_date'] = updated_date_time


        data['transactions'][i]['trans_type'] = t[i].get_trans_type()
        data['transactions'][i]['stock'] = t[i].get_stock()
        data['transactions'][i]['price'] = t[i].get_price()
        data['transactions'][i]['total_price'] = t[i].get_total_price()
        data['transactions'][i]['volume'] = t[i].get_volume()

l = tdao.get_user_stock_list(username)
        
if l:
    data['owned_stocks']={}
    for i in range(len(l)):
        c = cdao.get_company_model(l[i])
        o = tdao.get_owned_stock_model(username, l[i], c.get_ask()) 
        data['owned_stocks'][i]={}
        data['owned_stocks'][i]['stock'] = l[i]
        data['owned_stocks'][i]['current_shares'] = o.get_volume()
        data['owned_stocks'][i]['current_price'] = c.get_ask()
        data['owned_stocks'][i]['total_worth'] = o.get_total_worth()
        data['owned_stocks'][i]['profit'] = o.get_profit()

json_result = json.dumps(data)
print json_result

