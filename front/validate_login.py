#!/usr/bin/python

import cgi, Cookie, LINK_HEADERS
from database_class import DB

form = cgi.FieldStorage()

username = str(form.getvalue("username"))
password = str(form.getvalue("password"))


db = DB("localhost","root","mmGr2016","cdlcapital")
result = db.query("select * from users where login = '"+username+"' and password = '"+password+"'")

if result:
    result = username
else:
    result = "False"


cookie = Cookie.SimpleCookie()
cookie['login'] = result

print cookie
print "Location: ", LINK_HEADERS.HOME_LINK, "\r\n"
