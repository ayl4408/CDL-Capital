#!/usr/bin/python

import cgi, datetime,sys,LINK_HEADERS
import simplejson as json
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from algorithms_dao import Algorithms_dao

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

a = Algorithms_dao()

if form.getvalue("user_name") != None:
    username=form.getvalue("user_name")
    
def main():
    d = {}
    d['User']= {}
    d['User']= 0
    d['All']= {}
    d['All']= 1
    d['Algorithms']= {}
    d['Algorithms']= 2

    lst = a.select_all_algorithms(username)
    
    if lst:
        for i in range(len(lst)):
            d[lst[i].get_algo_name()] = {}
            d[lst[i].get_algo_name()] = int(lst[i].get_algo_id())            
    
    print json.dumps(d)
        
main()
                
