#!/usr/bin/python


import Cookie, os, LINK_HEADERS,sys
from templite import Templite
sys.path.insert(1 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
from auth_class import Auth


def m(username):
    f = open("home.tpl","r")
    html = str(f.read())
    f.close()

    print "Content-Type: text/html\r\n\r\n"

    t = Templite(html)
    print t.render(username=username, login_link=LINK_HEADERS.LOGIN_LINK, home_link=LINK_HEADERS.HOME_LINK, transaction_link=LINK_HEADERS.TRANSACTION_LINK, deposit_link=LINK_HEADERS.DEPOSIT_LINK, upload_link=LINK_HEADERS.UPLOAD_LINK, dropdown_link=LINK_HEADERS.DROPDOWN_LINK, portfolio_link=LINK_HEADERS.PORTFOLIO_LINK)

def check_cookie():
    cookie = Cookie.SimpleCookie()
    cookie_string = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))

    if (cookie_string != None) and ("login" in cookie_string):
        cookie.load(cookie_string)

        username = str(cookie['username'].value);
        login_result = str(cookie['login'].value)
        hashed_username =  Auth(DB("localhost","root","mmGr2016","cdlcapital")).get_hash_salted_username(username);
        
        if (login_result == "False") or (not login_result==hashed_username):
            print "Location: "+str(LINK_HEADERS.LOGIN_LINK)+"\r\n"
        else:
            m(username)            
    else:
        print "Location: "+str(LINK_HEADERS.LOGIN_LINK)+"\r\n"

check_cookie()


