#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao

print "Content-Type: text/html\r\n\r\n"




def main():

    form = cgi.FieldStorage()
    username = None;
    group = None;    

    if form.getvalue("username") != None:
        username = form.getvalue("username")
    #if form.getvalue("group") != None:
    #    group = form.getvalue("group")

    tdao = Transaction_dao()

    trades_per_day = tdao.get_trades_per_day(username)
    
    lst = []
    
    for day in trades_per_day:
        #date = day.get_date()
        #lst.append({"date": str(day.get_date()), "num_trade": day.get_num_trades()})
        lst.append([str(day.get_date()), day.get_num_trades()])
    #print lst
    json_result = json.dumps(lst)
    print json_result    
    
main()    
