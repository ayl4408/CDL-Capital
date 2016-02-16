#!/usr/bin/python

import cgi, LINK_HEADERS, sys
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from owned_stocks_class import Owned_stocks

print "Content-Type: text/html\r\n\r\n"

form=cgi.FieldStorage()
o=Owned_stocks()

if form.getvalue("user_name") != None:
    username=form.getvalue("user_name")

def main():
    owned_stocks=o.get_portfolio(username)
    print json.dumps(owned_stocks)

main()
