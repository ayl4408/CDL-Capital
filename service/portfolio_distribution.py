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
pie_chart_list=[]
tdao=Transaction_dao()
user_stock_list=tdao.get_user_stock_list(username)
for stock in user_stock_list:
    cdao=Company_dao()
    company_model=cdao.get_company_model(stock)
    ask=company_model.get_ask()
    pie_chart_list.append([stock,float(ask)])   

print json.dumps(pie_chart_list)


