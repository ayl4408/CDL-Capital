#!/usr/bin/python

import cgi, LINK_HEADERS, sys
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao
from company_dao import Company_dao

print "Content-Type: text/html\r\n\r\n"

form=cgi.FieldStorage()

if form.getvalue("user_name") != None:
    username=form.getvalue("user_name")

#test
#username='al356'
pie_chart_list=[]
tdao=Transaction_dao()
user_stock_list=tdao.get_user_stock_list(username)
if user_stock_list != None:
    for stock in user_stock_list:
        cdao=Company_dao()
        company_model=cdao.get_company_model(stock)
        price=company_model.get_ask()
        owned_stock_model=tdao.get_owned_stock_model(username, stock, price)
        total_worth=owned_stock_model.get_total_worth()
        pie_chart_list.append([stock,float(total_worth)])   
    print json.dumps(pie_chart_list)
else:
    print json.dumps("")
