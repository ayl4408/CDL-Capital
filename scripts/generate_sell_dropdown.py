#!/usr/bin/python

import cgi, datetime,sys,LINK_HEADERS
import simplejson as json
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from owned_stocks_class import Owned_stocks

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

o=Owned_stocks()

if form.getvalue("user_name") != None:
    username=form.getvalue("user_name")

def main():
    owned_stocks=o.get_all_stocks(username)
    print json.dumps(owned_stocks)

main()    
