#!/usr/bin/python

import cgi,LINK_HEADERS, sys, json
import sys, LINK_HEADERS
sys.path.insert(0,str(LINK_HEADERS.MODELS_LINK))
from active_algorithms_model import Active_algorithms
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from active_algorithms_dao import Active_algorithms_dao


def execute(task, algo_dao):
    try:
        algo_dao.execute(task)
        print json.dumps({"status": "Success"})
    except:
        print json.dumps({"status":"Fail"})

def stop(task, algo_dao):
    try:
        algo_dao.stop(task)
        print json.dumps({"status": "Success"})
    except:
        print json.dumps({"status":"Fail"})


print "Content-Type: text/html\r\n\r\n"


#
form = cgi.FieldStorage()
user = str(form.getvalue("user"))
algo_id = str(form.getvalue("algo_id"))
status = str(form.getvalue("status"))

task = Active_algorithms(user, algo_id);
algo_dao = Active_algorithms_dao()


if(status=='1'):execute(task, algo_dao)
if(status=='2'):stop(task, algo_dao)
