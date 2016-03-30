#!/usr/bin/python

import cgi, sys, LINK_HEADERS
import simplejson as json
from datetime import datetime
from dateutil import tz
from decimal import *
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
if form.getvalue("filter") != None:
    portfolio_filter = form.getvalue("filter")

    if portfolio_filter == '1':
        filter_flag = "ALL"
    elif portfolio_filter == '2':
        filter_flag = "ALGOS"
    elif portfolio_filter == '0':
        filter_flag = "USER"
    else:
        filter_flag = portfolio_filter
        
tdao = Transaction_dao()
u2 = User_stock_value_dao()
u1 = User_portfolio_dao()
cdao = Company_dao()
hdao = History_dao()

data={}

if filter_flag == "ALL":
    t = hdao.select_all(username)
    l = tdao.get_user_stock_list(username)
elif filter_flag == "ALGOS":
    t = hdao.select_all_algo_trades(username)
    l = tdao.get_all_algo_stock_list(username)
elif filter_flag == "USER":
    t = hdao.select_all_user_trades(username)
    l = tdao.get_only_user_stock_list(username)
else:
    t = hdao.select_algo_trades(username, filter_flag)
    l = tdao.get_algo_stock_list(username, filter_flag)

# HISTORY
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
else:
    data['transactions']={}
    data['transactions'][0]={}
    data['transactions'][0]['trans_date'] = ""
    data['transactions'][0]['trans_type'] = ""
    data['transactions'][0]['stock'] = ""
    data['transactions'][0]['price'] = ""
    data['transactions'][0]['total_price'] = ""
    data['transactions'][0]['volume'] = ""

# OWNED STOCKS
if l:
    data['owned_stocks']={}
    total_stock_value = 0
    
    for i in range(len(l)):
        c = cdao.get_company_model(l[i])
        o = tdao.get_owned_stock_model(username, l[i], c.get_ask()) 
        data['owned_stocks'][i]={}
        data['owned_stocks'][i]['stock'] = l[i]
        data['owned_stocks'][i]['current_shares'] = o.get_volume()
        data['owned_stocks'][i]['current_price'] = c.get_ask()
        data['owned_stocks'][i]['total_worth'] = o.get_total_worth()
        data['owned_stocks'][i]['profit'] = o.get_profit()
        total_stock_value = Decimal(total_stock_value) + Decimal(o.get_total_worth())
else:
    data['owned_stocks']={}
    data['owned_stocks'][0]={}
    data['owned_stocks'][0]['stock'] = ""
    data['owned_stocks'][0]['current_shares'] = ""
    data['owned_stocks'][0]['current_price'] = ""
    data['owned_stocks'][0]['total_worth'] = ""
    data['owned_stocks'][0]['profit'] = ""

# PORTFOLIO INFORMATION
up = u1.get_user_portfolio_model(username)
usv = u2.get_user_stock_value_model(username)

data['users']={}

if up:
    data['users']['total_portfolio'] = up.get_total_portfolio()
    data['users']['total_deposited'] = up.get_total_deposited()
    data['users']['available_funds'] = up.get_available_funds()
else:
    data['users']['total_portfolio'] = 0
    data['users']['total_deposited'] = 0
    data['users']['available_funds'] = 0  

if usv:
    data['users']['total_stock_values'] = usv.get_total_stock_values()
    data['users']['profit'] = usv.get_profit() 
else:
    data['users']['total_stock_values'] = 0
    data['users']['profit'] = 0
    
json_result = json.dumps(data)
print json_result
