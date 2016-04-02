#!/usr/bin/python

import Cookie, os, LINK_HEADERS,sys
from templite import Templite
sys.path.insert(0 , str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
sys.path.insert(1 , str(LINK_HEADERS.SCRIPTS_LINK))
sys.path.insert(1 , str(LINK_HEADERS.SERVICE_LINK))
from auth_service import Auth


def m(username):
    f = open("home.tpl","r")
    html = str(f.read())
    f.close()

    print "Content-Type: text/html\r\n\r\n"

    t = Templite(html)
    print t.render(username=username, login_link=LINK_HEADERS.LOGIN_LINK, home_link=LINK_HEADERS.HOME_LINK, transaction_link=LINK_HEADERS.TRANSACTION_LINK, deposit_link=LINK_HEADERS.DEPOSIT_LINK, upload_link=LINK_HEADERS.UPLOAD_LINK, dropdown_link=LINK_HEADERS.DROPDOWN_LINK, portfolio_link=LINK_HEADERS.PORTFOLIO_LINK, active_stocks_percentchange_link=LINK_HEADERS.ACTIVE_STOCKS_PERCENTCHANGE_LINK, create_user_link=LINK_HEADERS.CREATE_USER_LINK, update_user_link=LINK_HEADERS.UPDATE_USER_LINK, active_stocks_volumechange_link=LINK_HEADERS.ACTIVE_STOCKS_VOLUMECHANGE_LINK, update_password_link=LINK_HEADERS.UPDATE_PASSWORD_LINK, stock_symbol_link=LINK_HEADERS.STOCK_LINK, display_algorithms_link=LINK_HEADERS.DISPLAY_ALGORITHMS_LINK,execute_algo_link=LINK_HEADERS.EXECUTE_ALGORITHMS_LINK, get_active_algorithms_link=LINK_HEADERS.GET_ACTIVE_ALGORITHMS_LINK, filter_link=LINK_HEADERS.FILTER_DROPDOWN_LINK, algorithm_graph_link=LINK_HEADERS.ALGORITHM_GRAPH_LINK, algorithm_graph_dropdown_link=LINK_HEADERS.ALGORITHM_GRAPH_DROPDOWN_LINK)
def check_cookie():
    cookie = Cookie.SimpleCookie()
    cookie_string = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))

    if (cookie_string != None) and ("login" in cookie_string):
        cookie.load(cookie_string)

        username = str(cookie['username'].value);
        login_result = str(cookie['login'].value)
        hashed_username =  Auth().get_hashed_username(username);
        
        if (login_result == "False") or (not login_result==hashed_username):
            print "Location: "+str(LINK_HEADERS.LOGIN_LINK)+"\r\n"
        else:
            m(username)            
    else:
        print "Location: "+str(LINK_HEADERS.LOGIN_LINK)+"\r\n"

check_cookie()


