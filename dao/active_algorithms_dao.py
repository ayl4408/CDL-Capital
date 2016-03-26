#!/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0,str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0,str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from login_model import Login
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
#}
