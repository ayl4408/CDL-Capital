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

#        try:
#            data['transactions'][i]['name']=cdao.get_company_model(t[i].get_stock()).get_name()
#        except:
#            data['transactions'][i]['name']=""
            
        data['transactions'][i]['stock'] = t[i].get_stock()
        data['transactions'][i]['price'] = t[i].get_price()
        data['transactions'][i]['total_price'] = t[i].get_total_price()
        data['transactions'][i]['volume'] = t[i].get_volume()
else:
    data['transactions']={}
    data['transactions'][0]={}
    data['transactions'][0]['trans_date'] = ""
    data['transactions'][0]['trans_type'] = ""
    data['transactions'][0]['name']=""
    data['transactions'][0]['stock'] = ""
    data['transactions'][0]['price'] = ""
    data['transactions'][0]['total_price'] = ""
    data['transactions'][0]['volume'] = ""
    


# OWNED STOCKS
sector_dao=Sector_info_dao()
data['sector_volume']={}
if l:
    
    data['owned_stocks']={}
    #total_stock_value = 0
    
#    for i in range(len(l)):
#        c = cdao.get_company_model(l[i])
    
    c = cdao.get_list_of_company_models(l)
    if c:
        for i in range(len(c)):
            try:
                o = tdao.get_owned_stock_model(username, c[i].get_symbol(), c[i].get_ask()) 
            except:
                continue
            
            data['owned_stocks'][i]={}
            data['owned_stocks'][i]['name']=c[i].get_name()
            data['owned_stocks'][i]['stock'] = c[i].get_symbol()
            data['owned_stocks'][i]['current_shares'] = o.get_volume()
            data['owned_stocks'][i]['current_price'] = c[i].get_ask()
            data['owned_stocks'][i]['total_worth'] = o.get_total_worth()
            data['owned_stocks'][i]['profit'] = o.get_profit()
            #total_stock_value = Decimal(total_stock_value) + Decimal(o.get_total_worth())

            #--------Code for chart - sector_volume:---
            volume=o.get_volume()
            symbol=c[i].get_symbol()
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
    data['owned_stocks'][0]['name'] =""
    data['owned_stocks'][0]['stock'] = ""
    data['owned_stocks'][0]['current_shares'] = ""
    data['owned_stocks'][0]['current_price'] = ""
    data['owned_stocks'][0]['total_worth'] = ""
    data['owned_stocks'][0]['profit'] = ""

# PORTFOLIO INFORMATION
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
    




#----------------------------------code owned Stocks chart-----------------------------#

owned_stocks=data['owned_stocks']
owned_stocks_graph_data={}

sorted_owned_stocks_chart_axis=[]
sorted_owned_stocks_chart_value=[]

for i in owned_stocks:
    owned_stocks_graph_data[owned_stocks[i]['stock']]=owned_stocks[i]['total_worth']

length=len(owned_stocks_graph_data);
sorted_data=sorted(owned_stocks_graph_data.items(),key=operator.itemgetter(1))


for i in range(length-1,-1,-1):
    if(length-i>MAX):break
    sorted_owned_stocks_chart_axis.append(sorted_data[i][0])
    sorted_owned_stocks_chart_value.append(sorted_data[i][1])

data['owned_stocks_chart_axis']=sorted_owned_stocks_chart_axis;
data['owned_stocks_chart_value']=sorted_owned_stocks_chart_value;

json_result = json.dumps(data)
print json_result

                    
