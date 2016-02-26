#!/usr/bin/python

import sys,simplejson,re,time,datetime,LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from users_class import Users
from owned_stocks_class import Owned_stocks
from company_class import Company
from decimal import *

u = Users()
o = Owned_stocks()
c = Company()

user = {}
user['username']={}

def initialize_dictionary():
    result1 = u.select_all_users()
    stock_list = []
    user_list = []
    
    if result1:
        for i in result1:
            username = i['login']

            if username not in user_list:
                user_list.append(username)
            
            result2 = o.select_all(username)
            u.populate(username)

            if result2:
                user['username'][username]={}
                user['username'][username]['stocks']={}
                user['username'][username]['total_portfolio']=u.get_total_portfolio()
                user['username'][username]['total_stock_values']=u.get_total_stock_values()
                user['username'][username]['total_deposited']=u.get_total_deposited()
                user['username'][username]['available_funds']=u.get_available_funds()
                
                for j in result2:
                    stock = j['stock']
                    current_shares = j['current_shares']
                    total_worth = j['total_worth']
                    user['username'][username]['stocks'][stock]={}
                    user['username'][username]['stocks'][stock]['new_price']=0
                    user['username'][username]['stocks'][stock]['total_worth']=total_worth
                    user['username'][username]['stocks'][stock]['current_shares']=current_shares
                    
                    if stock not in stock_list:
                        stock_list.append(stock)
    return stock_list, user_list

def populate_dictionary(dict, stock_list, user_list):
    for users in user_list:
        total_stock_worth = 0

        for stock in stock_list:
            if stock in user['username'][users]['stocks'].keys():
                o.populate(users, stock)

                user['username'][users]['stocks'][stock]['new_price'] = Decimal(dict['stock'][stock])
                o.set_current_price(user['username'][users]['stocks'][stock]['new_price'])
                
                user['username'][users]['stocks'][stock]['total_worth'] = user['username'][users]['stocks'][stock]['new_price'] * user['username'][users]['stocks'][stock]['current_shares']
                o.set_total_worth(user['username'][users]['stocks'][stock]['total_worth'])
                
                total_stock_worth = total_stock_worth + user['username'][users]['stocks'][stock]['total_worth']
                
        user['username'][users]['total_stock_values'] = Decimal(total_stock_worth)
        user['username'][users]['total_portfolio'] = Decimal(total_stock_worth)+Decimal(user['username'][users]['available_funds'])

        u.populate(users)
        u.set_total_portfolio(user['username'][users]['total_portfolio'])
        u.set_total_stock_values(user['username'][users]['total_stock_values'])
        
def main():
    stock_list, user_list = initialize_dictionary()
    dict = c.select_in_list(stock_list)
    populate_dictionary(dict, stock_list, user_list)
    
main()
