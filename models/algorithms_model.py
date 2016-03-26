#!/usr/bin/python

class Algorithms:
    
    def __init__(self, user=None, algo_name=None, algo_id=None):
        self.user = user
        self.algo_name = algo_name
        self.algo_id = algo_id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    def get_algo_name(self):
        return self.algo_name

    def set_algo_name(self, algo_name):
        self.algo_name = algo_name

    def get_algo_id(self):
        return self.algo_id

    def set_algo_id(self, algo_id):
        self.algo_id = algo_id
    

    
