#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
#from transaction_dao import Transaction_dao
from history_dao import History_dao
#from algorithms_dao import Algorithms_dao

print "Content-Type: text/html\r\n\r\n"
'''
def get_all():
    print     

def get_all_algos():
    print

def get_each_algo():
    print
'''

def main():

    form = cgi.FieldStorage()
    username = None
    #username = "kad34"
    group = None

    if form.getvalue("username") != None:
        username = form.getvalue("username")
    #if form.getvalue("group") != None:
    #    group = form.getvalue("group")

    hdao = History_dao()
    #tdao = Transaction_dao()
    #adao = Algorithms_dao()
    #lst = adao.select_all_algorithms(username)

    #algo_ids = []
    #for i in range(len(lst)):
    #    algo_ids.append(lst[i].get_algo_id())
    
        

    #print algo_ids

    #trades_per_day = tdao.get_trades_per_day(username)
    volume_per_day = hdao.get_volume_per_day(username)    

    lst = []
    
    for day in volume_per_day:
        #date = day.get_date()
        #lst.append({"date": str(day.get_date()), "num_trade": day.get_num_trades()})
        lst.append([str(day.get_date()), day.get_volume()])
    #print lst
    json_result = json.dumps(lst)
    print json_result    
    
main()    
