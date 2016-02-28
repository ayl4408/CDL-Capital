#!/usr/bin/python

import os
import hashlib

class Profile:#{
    username = None
    passcode = None
    first_name = None
    last_name = None
    salt = None

    def __init__(self, username, passcode, first_name, last_name):
        self.username = username
        self.passcode = passcode
        self.first_name = first_name
        self.last_name = last_name

    #-------------------------
        
    def get_username(self):
        return self.username

    def get_passcode(self):
        return self.passcode

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_salt(self):
        return self.salt
    #-------------------------

    def set_username(self, username):
        self.username = username

    def set_passcode(self, passcode):
        self.passcode = passcode

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_salt(self, salt):
        self.salt=salt
        
    #-------------------------
        
    def generate_salt(self):
        return os.urandom(16).encode('hex')

    def prepare(self):
        self.salt = self.generate_salt();
        self.passcode=hashlib.sha256(self.passcode+self.salt).hexdigest()
        
    def get_values(self):
        self.prepare();
        return (self.username, self.salt, self.passcode, self.first_name, self.last_name);
#}
