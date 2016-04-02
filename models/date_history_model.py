#!/usr/bin/python

class Date_history:

    def __init__(self):
        self.date = None;
        self.volume = None;

    def get_date(self):
        return self.date
    
    def set_date(self, x): 
        self.date = x
   
    def get_volume(self):
        return self.volume

    def set_volume(self, x):
        self.volume = x
