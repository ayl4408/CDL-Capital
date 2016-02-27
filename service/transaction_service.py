#!/usr/bin/python

import cgi, datetime,sys,LINK_HEADERS
import simplejson as json
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao
from user_portfolio_dao import User_portfolio_dao
from user_stock_value_dao import User_stock_value_dao
from company_dao import Company_dao
from history_dao import History_dao

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
if form.getvalue("volume") != None:
    volume = int(form.getvalue("volume"))
if form.getvalue("company") != None:
    company = form.getvalue("company")
if form.getvalue("trans_type") != None:
    trans_type = form.getvalue("trans_type")
    
#test variables

#username="al356"
#company='tsla'
#volume=10
#trans_type='buy'
#trans_type='sell'

udao1 = User_stock_value_dao()
udao2 = User_portfolio_dao()
cdao = Company_dao()
tdao = Transaction_dao()
hdao = History_dao()

c = cdao.get_company_model(company)

ask = Decimal(c.get_ask())
time = datetime.datetime.utcnow()

def calculate_price():
    return Decimal(ask) * int(volume)

def main():
    final = calculate_price()
    if trans_type == 'buy':
        u = udao2.get_user_portfolio_model(username)
        if final <= u.get_available_funds():
            tdao.buy(username, time, company, volume, ask)
            hdao.insert(username, time, 'buy', company, ask, final, volume)
            
            o = tdao.get_user_stock_value_model(username)
            
            if o.get_total_stock_values():
                udao1.update_total_stock_values(username, o.get_total_stock_values())

            if o.get_profit():
                udao1.update_profit(username, o.get_profit())
            
            up = udao2.get_user_portfolio_model(username)
            udao2.update_available_funds(username, Decimal(up.get_available_funds()) - final)
            
    elif trans_type == 'sell':

        o = tdao.get_owned_stock_model(username, company, ask)
        
        if o.get_volume() >= volume:
            tdao.sell(username, company, volume, ask)
            hdao.insert(username, time, 'buy', company, ask, final, volume)

            u = tdao.get_user_stock_value_model(username)    
            udao1.update_total_stock_values(username, u.get_total_stock_values())
            udao1.update_profit(username, u.get_profit())

            portfolio = udao2.get_user_portfolio_model(username)
            udao2.update_available_funds(username, Decimal(final) + Decimal(portfolio.get_available_funds()))
            udao2.update_total_portfolio(username, Decimal(final) + Decimal(portfolio.get_available_funds()) + Decimal(u.get_total_stock_values()))
            
            
main()
