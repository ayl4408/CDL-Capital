#!/usr/bin/python

import cgi, Cookie, LINK_HEADERS, sys,os
sys.path.insert(0 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
sys.path.insert(1 , str(LINK_HEADERS.SCRIPTS_LINK))
sys.path.insert(1 , str(LINK_HEADERS.SERVICE_LINK))
from auth_service import Auth

form = cgi.FieldStorage()
username = str(form.getvalue("username"))
password = str(form.getvalue("password"))


cookie = Cookie.SimpleCookie()

cookie['username'] = username;
cookie['login'] = Auth().verify(username,password);

print cookie
print "Location: ", LINK_HEADERS.HOME_LINK, "\r\n"
