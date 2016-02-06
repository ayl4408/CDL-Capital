#!/usr/bin/python

import cgi, Cookie
from database import DB


form = cgi.FieldStorage()

username = str(form.getvalue("username"))
password = str(form.getvalue("password"))

'''
print "Content-Type: text/html\r\n\r\n"
print username
print password
'''

db = DB("localhost","root","mmGr2016","cdlcapital")
result = db.query("select * from users where login = '"+username+"' and password = '"+password+"'")

if result:
    result = "True"
else:
    result = "False"

cookie = Cookie.SimpleCookie()
cookie['login'] = result

print cookie
print "Location: http://cdl.ddns.net:4098/cgi-bin/cdlcapital/home.py\r\n"
