#!/usr/bin/python


import Cookie, os, LINK_HEADERS
from templite import Templite

print "Content-Type: text/html\r\n\r\n"

def m(username):
    f = open("home.tpl","r")
    html = str(f.read())
    f.close()
    
    t = Templite(html)
    print t.render(username=username, login_link=LINK_HEADERS.LOGIN_LINK, home_link=LINK_HEADERS.HOME_LINK, transaction_link=LINK_HEADERS.TRANSACTION_LINK, deposit_link=LINK_HEADERS.DEPOSIT_LINK, upload_link=LINK_HEADERS.UPLOAD_LINK, yql_link=LINK_HEADERS.YQL_LINK, dropdown_link=LINK_HEADERS.DROPDOWN_LINK)

def check_cookie():
    cookie = Cookie.SimpleCookie()
    cookie_string = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))

    if cookie_string != None:
        cookie.load(cookie_string)
        login_result = str(cookie['login'].value)
    
        if login_result == "False":
            print "Location: "+str(LINK_HEADERS.LOGIN_LINK)+"\r\n"
        else:
            username = login_result
            m(username)            
    else:
        print "Location: "+str(LINK_HEADERS.LOGIN_LINK)+"\r\n"

check_cookie()


