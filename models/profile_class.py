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

    def generate_salt(self):
        return os.urandom(16).encode('hex')

    def prepare(self):
        self.salt = self.generate_salt();
        self.passcode=hashlib.sha256(self.passcode+self.salt).hexdigest()
        
    def get_values(self):
        self.prepare();
        return (self.username, self.salt, self.passcode, self.first_name, self.last_name);
#}
