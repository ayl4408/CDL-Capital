#!/usr/bin/python

import Cookie, os
from templite import Templite
from database_class import DB
from users_class import Users
from transactions_class import Transactions
from owned_stocks_class import Owned_stocks

def get_models():
    db = DB("localhost","root","mmGr2016","cdlcapital")
    row1 = db.query("select * from users where login = ('%s')"%(username)+";")
    row2 = db.query("select * from transactions where user = ('%s')"%(username)+";")
    row3 = db.query("select * from owned_stocks where stock_owner = ('%s')"%(username)+";")

    if row1:
        users.set_login(row1[0][1])
        users.set_role(row1[0][2])
        users.set_profit(row1[0][3])
        users.set_total_portfolio(row1[0][4])
        users.set_available_funds(row1[0][5])
        users.set_total_stock_values(row1[0][6])
        users.set_total_deposited(row1[0][7])

    '''
    if row2:
        trans.set_trans_date(row2[0][1])
        trans.set_trans_type(row2[0][2])
        trans.set_stock(row2[0][3])
        trans.set_price(row2[0][4])
        trans.set_volume(row2[0][5])
        trans.set_total_price(row2[0][6])
    '''
            
        
def main():
    get_models()
    print "Content-Type: text/html\r\n\r\n"
    #t = Template(html)
    #t.render(users=users, trans=trans, owned=owned)

def check_cookie():
    cookie = Cookie.SimpleCookie()
    cookie_string = Cookie.SimpleCookie(os.environ.get('HTTP_COOKIE'))

    if cookie_string != None:
        cookie.load(cookie_string)
        login_result = str(cookie['login'].value)
    
        if login_result == "False":
            print "Location: http://cdl.ddns.net:4098/cgi-bin/alee_cdlcapital/login.py\r\n"
        else:
            username = login_result
            main()
            
    else:
        print "Location: http://cdl.ddns.net:4098/cgi-bin/alee_cdlcapital/login.py\r\n"

username = "al356"
users=Users()
trans=[]
owned=[]
#check_cookie()
get_models()
