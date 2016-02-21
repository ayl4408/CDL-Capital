#!/usr/bin/python

import cgi, Cookie, LINK_HEADERS, sys
sys.path.insert(0 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
from auth_class import Auth

form = cgi.FieldStorage()
username = str(form.getvalue("username"))
password = str(form.getvalue("password"))

cookie = Cookie.SimpleCookie()

cookie['username'] = username;
cookie['login'] = Auth(DB("localhost","root","mmGr2016","cdlcapital")).verify(username,password);

print cookie
print "Location: ", LINK_HEADERS.HOME_LINK, "\r\n"
