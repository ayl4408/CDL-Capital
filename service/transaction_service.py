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


def calculate_price(ask, volume):
    return Decimal(ask) * int(volume)

def transaction(username, volume, company, trans_type, algo_id):
    
    udao1 = User_stock_value_dao()
    udao2 = User_portfolio_dao()
    cdao = Company_dao()
    tdao = Transaction_dao()
    hdao = History_dao()

    c = cdao.get_company_model(company)

    ask = Decimal(c.get_ask())
    time = datetime.datetime.utcnow()

    final = calculate_price(ask, volume)

    if trans_type == 'buy':
        u = udao2.get_user_portfolio_model(username)
        if final <= u.get_available_funds():
            tdao.buy(username, time, company, volume, ask, algo_id)
            hdao.insert(username, time, 'buy', company, ask, final, volume, algo_id)
            
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
            tdao.sell(username, company, volume, ask, algo_id)
            hdao.insert(username, time, 'sell', company, ask, final, volume, algo_id)

            u = tdao.get_user_stock_value_model(username)    
            udao1.update_total_stock_values(username, u.get_total_stock_values())
            udao1.update_profit(username, u.get_profit())

            portfolio = udao2.get_user_portfolio_model(username)
            udao2.update_available_funds(username, Decimal(final) + Decimal(portfolio.get_available_funds()))
            udao2.update_total_portfolio(username, Decimal(final) + Decimal(portfolio.get_available_funds()) + Decimal(u.get_total_stock_values()))
            
            
