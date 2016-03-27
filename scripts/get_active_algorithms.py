#!/usr/bin/python

import cgi,LINK_HEADERS, sys, json
import sys, LINK_HEADERS
sys.path.insert(0,str(LINK_HEADERS.MODELS_LINK))
from active_algorithms_model import Active_algorithms
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from active_algorithms_dao import Active_algorithms_dao

print "Content-Type: text/html\r\n\r\n"

form=cgi.FieldStorage()
username=str(form.getvalue("user_name"))

algo_dao=Active_algorithms_dao()
print(json.dumps(algo_dao.get_active(username)));
