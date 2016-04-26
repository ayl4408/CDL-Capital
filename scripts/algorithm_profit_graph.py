#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
#from transaction_dao import Transaction_dao
from transaction_dao import Transaction_dao
from algorithms_dao import Algorithms_dao

tdao = Transaction_dao()
adao = Algorithms_dao()

print "Content-Type: text/html\r\n\r\n"


def get_all(username):
    result = tdao.select_all_profit_per_day(username)    
    lst = []    
    if result:
        for day in result:
            lst.append([day.get_date(), day.get_profit()])      
        return {"name":"All", "data":lst} 
    return False


def get_all_algos(username):
    result = tdao.select_all_algorithms_profit_per_day(username)    
    lst = []    
    if result:
        for day in result:
            lst.append([day.get_date(), day.get_profit()])
        return {"name":"All Algorithms", "data":lst} 
    return False

def get_user(username):
    result = tdao.select_user_profit_per_day(username)    
    lst = []  
    if result:    
        for day in result:
            lst.append([day.get_date(), day.get_profit()])
        return {"name":"User", "data":lst} 
    return False

def get_each_algo(username, algo_id, algo_name):
    result = tdao.select_algorithm_profit_per_day(username, algo_id)    
    lst = []
    if result:    
        for day in result:
            lst.append([day.get_date(), day.get_profit()])
        return {"name":algo_name, "data":lst} 
    return False

def main():

    form = cgi.FieldStorage()
    username = None
    #username = "kad34"
    group = None

    if form.getvalue("username") != None:
        username = form.getvalue("username")

    lst = []
    result = ""

    result = get_all(username)
    if result:
        lst.append(result)
    
    result = get_all_algos(username)
    if result:
        lst.append(result)
    
    result = get_user(username)
    if result:
        lst.append(get_user(username))    

    algo_lst = adao.select_all_algorithms(username)
    for algo in algo_lst:
        algo_id = algo.get_algo_id()
        algo_name = algo.get_algo_name()
        algo_result = get_each_algo(username, algo_id, algo_name)
        if algo_result:
            lst.append(algo_result)   
 
    json_result = json.dumps(lst)
    #json_result = json.dumps(lst)
    print json_result    
 
main()    
#print get_all("al356")

