#!/usr/bin/python

import sys, LINK_HEADERS
from decimal import *
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao
from user_portfolio_dao import User_portfolio_dao
from user_stock_value_dao import User_stock_value_dao
from company_dao import Company_dao

cdao = Company_dao()
tdao = Transaction_dao()

def update_profit_in_transaction(company_stock):
    user_stock = tdao.select()
    for c in company_stock:
        for cu in user_stock:
            if c.get_symbol() == cu.get_stock():
                current_price = c.get_ask()
                purchase_price = cu.get_price()
                profit = Decimal(current_price) - Decimal(purchase_price)
                tdao.update_profit(cu.get_user(), cu.get_trans_date(), cu.get_order_id(), profit)
            
def main():
    l = cdao.get_all_ask()
    update_profit_in_transaction(l)
    
main()
