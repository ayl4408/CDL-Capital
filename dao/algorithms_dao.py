#!/usr/bin/python

import cgi, sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from database_class import DB
from PDO import PDO
from algorithms_model import Algorithms

class Algorithms_dao:

    db = None

    def __init__(self):
        self.db =  PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)

    def select_distinct_algorithms(self):
        result = self.db.query("select distinct algo_name from algorithms;")
        if result:
            l = []
            for i in range(len(result)):
                if result[i]['algo_name'] != None:
                    a = Algorithms(result[i]['algo_name'])
                    l.append(a)
            return l

    def insert_algorithm(self, user, algo_name, algo_id):
        self.db.query("insert into algorithms(user, algo_name, algo_id) values('%s','%s','%s')"%(user, algo_name, algo_id) + ";")

    def select_all_algorithms(self, user):
        result = self.db.query("select * from algorithms where user=('%s')"%(user) + ";")
        if result:
            l = []
            for i in range(len(result)):
                if result[i]['algo_name'] != None:
                    a = Algorithms(result[i]['user'], result[i]['algo_name'], result[i]['algo_id'])
                    l.append(a)
            return l

    def delete_algorithm(self, user, algo_name):
        result = self.db.query("delete from algorithms where user=('%s') and algo_name=('%s')"%(user, algo_name) + ";")

 
