#!/usr/bin/python

import sys, LINK_HEADERS
sys.path.insert(1 , str(LINK_HEADERS.MODELS_LINK))
from login_class import Login_DAO
import hashlib

class Auth:#{
    login_dao = None;
    
    def __init__(self):
        self.login_dao = Login_DAO()

    def get_hashed_username(self, username):
        salt=self.login_dao.get_salt(username)
        return hashlib.sha1(username+salt).hexdigest()
    
    def verify(self, username, passcode):
        salt=self.login_dao.get_salt(username)
        passcode=hashlib.sha256(passcode+salt).hexdigest()
        verification_result=self.login_dao.is_valid_user(username, passcode)
        
        if(verification_result): return self.get_hashed_username(username)
        return "False"
#}
