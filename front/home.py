#!/usr/bin/python

import Cookie, os
from templite import Templite

def main():
    print "Content-Type: text/html\r\n\r\n"
    print "LOGIN SUCCESSFUL"

def check_cookie():
    cookie = Cookie.SimpleCookie()
    cookie_string = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))

    if cookie_string != None:
        cookie.load(cookie_string)
        login_result = str(cookie['login'].value)
    
        if login_result == "True":
            main()
        else:
            print "Location: http://cdl.ddns.net:4098/cgi-bin/kdowney_cdlcapital/front/login.py\r\n"
    else:
        print "Location: http://cdl.ddns.net:4098/cgi-bin/kdowney_cdlcapital/front/login.py\r\n"

check_cookie()
