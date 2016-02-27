#!/usr/bin/python

import cgi,LINK_HEADERS, sys, json
sys.path.insert(0 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
sys.path.insert(0 , str(LINK_HEADERS.MODELS_LINK))
from profile_model import Profile
sys.path.insert(0 , str(LINK_HEADERS.DAO_LINK))
sys.path.insert(0, str(LINK_HEADERS.SERVICE_LINK))
from login_dao import Login_dao
from auth_service import Auth

print "Content-Type: text/html\r\n\r\n"


form = cgi.FieldStorage()
username = str(form.getvalue("username"))
passcode = str(form.getvalue("passcode"))
first_name = str(form.getvalue("first_name"))
last_name = str(form.getvalue("last_name"))


profile = Profile(username, passcode, first_name, last_name);
login_dao=Login_dao()

try:
    login_dao.create_user(profile)
    
    #Verifying to see if the injection was successfuly
    if(Auth().verify(username,passcode)=="False"):
        print json.dumps({"status":"Fail"})
    else:
        print json.dumps({"status": "Success"})
        
except:
    print json.dumps({"status":"Fail"})
