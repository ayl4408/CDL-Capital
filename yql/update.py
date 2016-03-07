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

'''
def update_total_stock_value(company_stock):
    # get list of users
    user_list = ldao.get_user_list()
    if user_list:
        for i in range(len(user_list)):
            # get list of companies they own
            print user_list[i].get_user() 
            user_companies = tdao.get_user_stock_list(user_list[i].get_user())
            if user_companies:
                for i in range(len(user_companies)):
                    for j in range(len(company_stock)):
                        if company_stock[j].get_symbol() == user_companies[i]:
                            print company_stock[j].get_ask()
                    # create owned stocks model for each company
                    #tdao.get_owned_stock_model(self, user_list[i].get_user(), ......)
                    # accumulate total worth of stocks for the user
                    # update total_stock_values in the user_stock_value table for user
                    # update total_portfolio (stock portfolio + available funds) in the user_portfolio table
'''   
             
def main():
    l = cdao.get_all_ask()
    update_profit_in_transaction(l)
    #update_total_stock_value(l)
    
main()
