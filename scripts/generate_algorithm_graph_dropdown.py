#!/usr/bin/python

import cgi, LINK_HEADERS, sys
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao
from algorithms_dao import Algorithms_dao

print "Content-Type: text/html\r\n\r\n"


def main():
    form=cgi.FieldStorage()
    username = None    

    if form.getvalue("user_name") != None:
        username=form.getvalue("user_name")

    adao=Algorithms_dao()
    lst = adao.select_all_algorithms(username)
    
    d = {}
    d['User'] = {}
    d['User'] = 0
    d['All'] = {}
    d['All'] = 1
    d['Algorithms'] = {}
    d['Algorithms'] = 2

    if lst:
        for i in range(len(lst)):
            d[lst[i].get_algo_name()] = {}
            d[lst[i].get_algo_name()] = int(lst[i].get_algo_id()) 

    print json.dumps(d)


main()

