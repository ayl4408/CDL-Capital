#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
#from transaction_dao import Transaction_dao
from history_dao import History_dao
from algorithms_dao import Algorithms_dao

hdao = History_dao()
adao = Algorithms_dao()

print "Content-Type: text/html\r\n\r\n"


def get_all(username):
    result = hdao.get_all_volume_per_day(username)    
    lst = []    
    if result:
        for day in result:
            lst.append([day.get_date(), day.get_volume()])      
        return {"name":"All", "data":lst} 
    return False


def get_all_algos(username):
    result = hdao.get_all_algorithms_volume_per_day(username)    
    lst = []    
    if result:
        for day in result:
            lst.append([day.get_date(), day.get_volume()])
        return {"name":"All Algorithms", "data":lst} 
    return False

def get_user(username):
    result = hdao.get_user_volume_per_day(username)    
    lst = []  
        
    for day in result:
        lst.append([day.get_date(), day.get_volume()])
    return {"name":"User", "data":lst} 

def get_each_algo(username, algo_id, algo_name):
    result = hdao.get_algorithm_volume_per_day(username, algo_id)    
    lst = []
    if result:    
        for day in result:
            lst.append([day.get_date(), day.get_volume()])
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

