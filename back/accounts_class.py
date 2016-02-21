#!/usr/bin/python

class Accounts:#{
    db_connection = None
    
    def __init__(self,db_connection):
        self.db_connection = db_connection

    def create_user(self, profile):
        SQL="""
            INSERT INTO login 
            (username, salt, passcode, first_name, last_name)
            VALUES
            ('%s', '%s', '%s', '%s', '%s')
        """
        self.db_connection.query(SQL % profile.get_values());
#}
    
