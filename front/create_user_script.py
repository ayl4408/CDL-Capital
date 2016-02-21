#!/usr/bin/python

import cgi,LINK_HEADERS, sys
sys.path.insert(0 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
from accounts_class import Accounts
sys.path.insert(0 , str(LINK_HEADERS.MODELS_LINK))
from profile_class import Profile

"""NOTE: 
******************************************************************************************************************************************************************************************************************************************
This is just a quick (PRIVATE) script for you guys to create a login. Since the passcode requires hasing, you can't manually create them. Use this script to create one for yourself. We can later edit this and clean it up for allowing users to sign SIGN-UP

#Sample: ......front/test.py? username=irallycdl &password=1234 &first_name=imraaz &last_name=rally
******************************************************************************************************************************************************************************************************************************************
"""



print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()
username = str(form.getvalue("username"))
password = str(form.getvalue("password"))
first_name = str(form.getvalue("first_name"))
last_name = str(form.getvalue("last_name"))


db = DB("localhost","root","mmGr2016","cdlcapital");
profile = Profile(username, password, first_name, last_name);
account_handler= Accounts(db);

account_handler.create_user(profile);

print "Profile Created: "
print(profile.get_values())
