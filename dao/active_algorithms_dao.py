#!/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0,str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0,str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from active_algorithms_model import Active_algorithms
from PDO import PDO

class Active_algorithms_dao:#{
    db_connection = None

    def __init__(self):
       self.db_connection = PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)

    def execute(self, task):
        
        SQL="""
            INSERT INTO active_algorithms 
               (user, algo_id)
            VALUES
               ('%s','%s')
            """
        user = task.get_user()
        algo_id = task.get_algo_id()
        
        self.db_connection.query(SQL % (user, algo_id))

    def stop(self, task):
        SQL = "DELETE FROM active_algorithms WHERE user='%s' and algo_id='%s'";

        user = task.get_user()
        algo_id = task.get_algo_id()
        
        self.db_connection.query(SQL % (user, algo_id))

    def select_all(self):
	results = self.db_connection.query("SELECT * FROM active_algorithms;")
	if results:
	    lst = []
	    for i in range(len(results)):
		a = Active_algorithms(results[i]["user"], results[i]["algo_id"])
		lst.append(a)
	    return lst
	else:
	    return False
	    
#}
