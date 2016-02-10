#!/usr/bin/python

import cgi, Cookie
<<<<<<< HEAD
#from database import DB
import sys
import os
sys.path.append(os.path.abspath("/usr/lib/cgi-bin/kdowney_cdlcapital"))
=======
>>>>>>> upstream/master
from database_class import DB

form = cgi.FieldStorage()

username = str(form.getvalue("username"))
password = str(form.getvalue("password"))

<<<<<<< HEAD
#print "Content-Type: text/html\r\n\r\n"
#print username
#print password


=======
>>>>>>> upstream/master
db = DB("localhost","root","mmGr2016","cdlcapital")
result = db.query("select * from users where login = '"+username+"' and password = '"+password+"'")

if result:
    result = username
else:
    result = "False"


cookie = Cookie.SimpleCookie()
cookie['login'] = result

print cookie
<<<<<<< HEAD
print "Location: http://cdl.ddns.net:4098/cgi-bin/kdowney_cdlcapital/front/home.py\r\n"

=======
print "Location: http://cdl.ddns.net:4098/cgi-bin/alee_cdlcapital/front/home.py\r\n"
>>>>>>> upstream/master
