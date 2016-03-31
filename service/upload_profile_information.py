#!/usr/bin/python

import operator
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
from sector_info_dao import Sector_info_dao
print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")

#username='kad34'
    
tdao = Transaction_dao()
u2 = User_stock_value_dao()
u1 = User_portfolio_dao()
cdao = Company_dao()
hdao = History_dao()

data={}

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
else:
    data['transactions']={}
    data['transactions'][0]={}
    data['transactions'][0]['trans_date'] = ""
    data['transactions'][0]['trans_type'] = ""
    data['transactions'][0]['stock'] = ""
    data['transactions'][0]['price'] = ""
    data['transactions'][0]['total_price'] = ""
    data['transactions'][0]['volume'] = ""
    
l = tdao.get_user_stock_list(username)

'''
def update_profit_in_transaction(company_stock):
    user_stock = tdao.select()
    for c in company_stock:
        for cu in user_stock:
            if c.get_symbol() == cu.get_stock():
                current_price = c.get_ask()
                purchase_price = cu.get_price()
                profit = Decimal(current_price) - Decimal(purchase_price)
                if cu.get_sold() == 0:
                    tdao.update_profit(cu.get_user(), cu.get_trans_date(), cu.get_order_id(), profit)
'''                 
#lis = cdao.get_all_ask()
#update_profit_in_transaction(lis)
sector_dao=Sector_info_dao()
data['sector_volume']={}

if l:
    
    data['owned_stocks']={}
    total_stock_value = 0
    
    for i in range(len(l)):
        c = cdao.get_company_model(l[i])

        try:
            o = tdao.get_owned_stock_model(username, l[i], c.get_ask()) 
        except:
            continue;
            
        data['owned_stocks'][i]={}
        data['owned_stocks'][i]['stock'] = l[i]
        data['owned_stocks'][i]['current_shares'] = o.get_volume()
        data['owned_stocks'][i]['current_price'] = c.get_ask()
        data['owned_stocks'][i]['total_worth'] = o.get_total_worth()
        data['owned_stocks'][i]['profit'] = o.get_profit()
        total_stock_value = Decimal(total_stock_value) + Decimal(o.get_total_worth())

        #--------Code for chart - sector_volume:---
        volume=o.get_volume()
        symbol=l[i]
        try:
            sector=sector_dao.get_sector_by_symbol(symbol)
            if(sector.strip()==''):sector="Other"
        except:
            sector="Other"

        if(sector not in data['sector_volume']):
            data['sector_volume'][sector]=volume;
        else:
            data['sector_volume'][sector]+=volume;
        #----------end of code for chart--------
        
else:
    data['owned_stocks']={}
    data['owned_stocks'][0]={}
    data['owned_stocks'][0]['stock'] = ""
    data['owned_stocks'][0]['current_shares'] = ""
    data['owned_stocks'][0]['current_price'] = ""
    data['owned_stocks'][0]['total_worth'] = ""
    data['owned_stocks'][0]['profit'] = ""

usv = u2.get_user_stock_value_model(username)
up = u1.get_user_portfolio_model(username)

data['users']={}
data['users']['profit'] = usv.get_profit()
data['users']['total_portfolio'] = up.get_total_portfolio()
data['users']['available_funds'] = up.get_available_funds()
data['users']['total_stock_values'] = usv.get_total_stock_values()
data['users']['total_deposited'] = up.get_total_deposited()



#---------------------Code for Chart Generation-----------------------------
sectors=[]
volume=[]

sorted_volume=sorted(data['sector_volume'].items(),key=operator.itemgetter(1))
length=len(sorted_volume);

#Insertion Sort
for i in range(length):
    j=i
    while(j>0 and sorted_volume[j][1]>sorted_volume[j-1][1]):
        temp=sorted_volume[j-1]
        sorted_volume[j-1]=sorted_volume[j]
        sorted_volume[j]=temp
        j=j-1

MAX=35
for i in range(length):
    if(i>=MAX):break;
    if(sorted_volume[i][0]=='Other'):continue
    sectors.append(sorted_volume[i][0])
    volume.append(sorted_volume[i][1])


data['chart_axis']=sectors;
data['chart_data']=volume;
#--------------------------------end of code for chart--------------------#


json_result = json.dumps(data)
print json_result
