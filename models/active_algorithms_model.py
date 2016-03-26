#!/usr/bin/python

class Active_algorithms:#{

    user = None
    algo_id = None
    start_time = None

    def __init__(self, user, algo_id):
        self.user = user
        self.algo_id = algo_id

    def set_user(self,user):
        self.user = user

    def set_algo_id(self,algo_id):
        self.algo_id = algo_id

    def set_start_time(self, start_time):
        self.start_time = start_time
        
    def get_user(self):
        return self.user

    def get_algo_id(self):
        return self.algo_id

    def get_start_time(self):
        return self.start_time

#}
    
