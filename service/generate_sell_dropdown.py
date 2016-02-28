#!/usr/bin/python

import cgi, LINK_HEADERS, sys
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao
from company_dao import Company_dao

print "Content-Type: text/html\r\n\r\n"

form=cgi.FieldStorage()

if form.getvalue("user_name") != None:
    username=form.getvalue("user_name")

#test
#username='al356'
tdao=Transaction_dao()
owned_stock_list=tdao.get_user_stock_list(username)
print json.dumps(owned_stock_list)
