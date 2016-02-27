#!/usr/bin/python

import cgi,LINK_HEADERS, sys, json
sys.path.insert(0 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
sys.path.insert(0 , str(LINK_HEADERS.MODELS_LINK))
from profile_model import Profile
sys.path.insert(0 , str(LINK_HEADERS.DAO_LINK))
from login_dao import Login_dao
from auth_class import Auth

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()
username = str(form.getvalue("username"))
passcode = str(form.getvalue("passcode"))
first_name = str(form.getvalue("first_name"))
last_name = str(form.getvalue("last_name"))

profile = Profile(username, passcode, first_name, last_name);

if(Auth().verify(username,passcode)=="False"):
    #If authorization failed, we do not update the user info
    print json.dumps({"status":"Fail"})
else:
    #update information
    Login_dao().update_user(profile)
    print json.dumps({"status":"Success"})
