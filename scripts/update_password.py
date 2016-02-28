#!/usr/bin/python
import cgi,LINK_HEADERS, sys, json
sys.path.insert(0 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
sys.path.insert(0 , str(LINK_HEADERS.MODELS_LINK))
from profile_model import Profile
sys.path.insert(0 , str(LINK_HEADERS.DAO_LINK))
sys.path.insert(0 , str(LINK_HEADERS.SERVICE_LINK))
from login_dao import Login_dao
from auth_service import Auth

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()
username = str(form.getvalue("username"))
old_passcode = str(form.getvalue("old_passcode"))
new_passcode = str(form.getvalue("new_passcode"))
verify_passcode = str(form.getvalue("verify_passcode"))

profile = Profile(username, new_passcode, "", "");
profile.prepare()


if(Auth().verify(username, old_passcode)=="False"):
    print json.dumps({"status":"Fail"})
else:
    Login_dao().update_passcode(profile)
    print json.dumps({"status":"Success"})






        
