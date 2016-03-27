#!/usr/bin/python

import cgi, sys, LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from algorithms_dao import Algorithms_dao
import simplejson as json
print "Content-Type: text/html\r\n\r\n"

form=cgi.FieldStorage()
a = Algorithms_dao()

if form.getvalue("user_name") != None:
    username = str(form.getvalue("user_name"))

#username = 'kc343'
algorithms_list=[]

def display_algorithms():
    try:
        algorithms = a.select_inactive_algorithms(username)
        for x in algorithms:
            algorithms_dict={}
            algorithms_dict['algo_id']=x.get_algo_id()
            algorithms_dict['algo_name']=x.get_algo_name()
            algorithms_list.append(algorithms_dict)
        print json.dumps(algorithms_list)
    except Exception, e:
        print str(e)


display_algorithms()

