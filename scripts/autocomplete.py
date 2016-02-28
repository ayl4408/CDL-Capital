#!/usr/bin/python

import cgi, datetime, LINK_HEADERS, sys
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from company_dao import Company_dao

print "Content-Type: text/html\r\n\r\n"




cdao=Company_dao()
company_stock_list=[]
company_stock_symbols=cdao.get_all_companies_stock()
for company in company_stock_symbols:
    company_stock_list.append(company.get_symbol())
print json.dumps(company_stock_list)
