#!/usr/bin/python

import Cookie, os
from templite import Templite


def m(username):
    f = open("home.tpl","r")
    html = str(f.read())
    f.close()
    
    t = Templite(html)
    print "Content-Type: text/html\r\n\r\n"
    print t.render(user=username)

def check_cookie():
    cookie = Cookie.SimpleCookie()
    cookie_string = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))

    if cookie_string != None:
        cookie.load(cookie_string)
        login_result = str(cookie['login'].value)
    
        if login_result == "False":
            print "Location: http://cdl.ddns.net:4098/cgi-bin/alee_cdlcapital/front/login.py\r\n"
        else:
            username = login_result
            m(username)            
    else:
        print "Location: http://cdl.ddns.net:4098/cgi-bin/alee_cdlcapital/front/login.py\r\n"

check_cookie()


