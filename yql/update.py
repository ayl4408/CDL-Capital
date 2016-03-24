#!/usr/bin/python

import sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao
from user_portfolio_dao import User_portfolio_dao
from user_stock_value_dao import User_stock_value_dao
from company_dao import Company_dao
from login_dao import Login_dao

cdao = Company_dao()
tdao = Transaction_dao()
ldao = Login_dao()
usvdao = User_stock_value_dao()
updao = User_portfolio_dao()

def update_profit_in_transaction(company_stock):
    user_stock = tdao.select()
    for c in company_stock:
        for cu in user_stock:
            if c.get_symbol() == cu.get_stock():
                current_price = c.get_ask()
                purchase_price = cu.get_price()
                profit = Decimal(current_price) - Decimal(purchase_price)
                if cu.get_sold() == 0:
                    tdao.update_profit(cu.get_user(), cu.get_trans_date(), cu.get_order_id(), profit)

def update_total_stock_value(company_stock):
    # get list of users
    user_list = ldao.get_user_list()
    if user_list:
        for i in range(len(user_list)): # user
            #print user_list[i].get_user()
            total_worth = 0
            user_companies = tdao.get_user_stock_list(user_list[i].get_user())
            if user_companies:
                for k in range(len(user_companies)): # companies owned by user
                    #print user_companies[i]
                    for j in range(len(company_stock)): # all companies in the DB
                        if company_stock[j].get_symbol() == user_companies[k]: # when they equal, you have the most up to date price
                            # create owned stocks model for each company
                            o = tdao.get_owned_stock_model(user_list[i].get_user(), company_stock[j].get_symbol(), company_stock[j].get_ask())
                            # accumulate total worth of stocks for the user
                            total_worth = total_worth + o.get_total_worth()
                            #print o.get_name()
                            #print o.get_volume()
                            #print o.get_price()
                            #print o.get_total_worth()
                            #print o.get_profit()
                            break
            # update total_stock_values in the user_stock_value table for user
            usvdao.update_total_stock_values(user_list[i].get_user(), total_worth)
            usv = tdao.get_user_stock_value_model(user_list[i].get_user())
            usvdao.update_profit(user_list[i].get_user(), usv.get_profit())
            # update total_portfolio (stock portfolio + available funds) in the user_portfolio table
            up = updao.get_user_portfolio_model(user_list[i].get_user())
            total_portfolio = up.get_available_funds() + total_worth
            updao.update_total_portfolio(user_list[i].get_user(), total_portfolio)
             
def main():
    l = cdao.get_all_ask()
    update_profit_in_transaction(l)
    update_total_stock_value(l)
    
main()
