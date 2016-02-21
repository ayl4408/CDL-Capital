#!/usr/bin/python

import hashlib;

class Auth:#{
    db_connection = None;
    
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_salt_from_db(self,username):
        SQL="SELECT salt FROM login WHERE username='%s'"
        result=self.db_connection.query(SQL % (username,))
        
        if (result):return str(result[0]['salt'])
        return "False"
        
    def get_hash_salted_username(self, username):
        salt=self.get_salt_from_db(username)
        return hashlib.sha1(username+salt).hexdigest()
    
    def verify(self, username, password):
        salt=self.get_salt_from_db(username)
        password=hashlib.sha256(password+salt).hexdigest()
        
        SQL= "SELECT * FROM login WHERE username ='%s' AND passcode='%s'"
        result=self.db_connection.query(SQL % (username,password))

        if(result): return self.get_hash_salted_username(username)
        return "False"
#}
