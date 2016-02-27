#!/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(0,str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
from PDO import PDO

class Login_dao:#{
    db_connection = None
    
    def __init__(self):
        self.db_connection = PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)
        
    def create_user(self, profile):
        SQL="""
            INSERT INTO login 
            (username, salt, passcode, first_name, last_name)
            VALUES
            ('%s', '%s', '%s', '%s', '%s')
        """
        self.db_connection.query(SQL % profile.get_values());

    def update_user(self, profile):
        SQL="""
            UPDATE login SET
               first_name='%s',
               last_name='%s'

            WHERE username='%s'
        """
        first_name = profile.get_first_name()
        last_name = profile.get_last_name()
        username = profile.get_username()

        self.db_connection.query(SQL % (first_name, last_name, username));
        
    def get_salt(self, username):
        SQL="SELECT salt FROM login WHERE username='%s'"
        result=self.db_connection.query(SQL % (username,))

        if (result):return str(result[0]['salt'])
        return "False"

    def is_valid_user(self, username, passcode):
        SQL= "SELECT * FROM login WHERE username ='%s' AND passcode='%s'"
        result = self.db_connection.query(SQL % (username,passcode))

        if(result): return True
        return False
    
#}
    
