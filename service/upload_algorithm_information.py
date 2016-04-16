#!/usr/bin/python

import cgi, sys, LINK_HEADERS
import simplejson as json
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from history_dao import History_dao
from company_dao import Company_dao
from algorithms_dao import Algorithms_dao
from transaction_dao import Transaction_dao

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
#username='al356'

hdao = History_dao()
cdao = Company_dao()
adao = Algorithms_dao()
tdao = Transaction_dao() 
result=[]
profit=0
stock_model_dict={}
stock_ask_dict={}    
volume_dict={}
distinct_stocks=hdao.get_distinct_traded_stocks(username)
algorithm_details_list = hdao.get_algorithm_buy_sell_volume(username) #len(result) =  number of algo_ids list of algorithm details models
symbols_string=""

if distinct_stocks:
    for i in range(len(distinct_stocks)):
        symbols_string+="'" + distinct_stocks[i].get_name() + "',"
    symbols_string=symbols_string[:-1]
    stock_ask=cdao.get_ask_comp(symbols_string) #list of company models

if stock_ask:
    for i in range(len(stock_ask)):
        stock_ask_dict[stock_ask[i].get_symbol()]=stock_ask[i].get_ask()
    profit_list=tdao.get_profit_per_algorithm(username) # list of owned_stocks_models with stock name, volume owned, profit
    algorithm_names=adao.select_used_algorithms(username) #list of algorithm  models

if algorithm_details_list:
    for i in range(len(algorithm_names)):
        owned_stocks_value = 0
        volume_list=tdao.get_owned_stock_volume_per_algorithm(username, algorithm_details_list[i].get_algo_id())
        for a in range(len(volume_list)):
            if volume_list[a].get_name() in stock_ask_dict.keys():
                owned_stocks_value += (Decimal(volume_list[a].get_volume()) * Decimal(stock_ask_dict[volume_list[a].get_name()]))
        data = {}
        data['algo_name']=algorithm_names[i].get_algo_name()
        data['total_trades']=algorithm_details_list[i].get_total_trades()
        data['total_buys']=algorithm_details_list[i].get_total_buys()
        data['total_sells']=algorithm_details_list[i].get_total_sells()
        data['total_profit']=profit_list[i].get_profit()
        data['total_owned_stocks_value']=owned_stocks_value
        result.append(data)
#print len(algorithm_details_list)
#print result
#print stock_ask[0].get_ask()
#print symbols_string
#print distinct_stocks[0].get_name()
#print json.dumps(result)
#print result

if algorithm_details_list and distinct_stocks and stock_ask:
    print json.dumps(result)
else:
    print False
