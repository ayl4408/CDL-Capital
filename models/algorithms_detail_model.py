#!/usr/bin/python

from algorithms_model import Algorithms

class Algorithm_details(Algorithms):
    
    def __init__(self, user=None, algo_id=None, total_trades=None, total_buys=None, total_sells=None, profit=None, total_stock_value=None):
        self.algo_id=algo_id
        self.user=user
        self.total_trades=total_trades
        self.total_buys=total_buys
        self.total_sells=total_sells
        self.profit=profit
        self.total_stock_value=total_stock_value


    def get_total_trades(self):
        return self.total_trades

    def set_total_trades(self, total_trades):
        self.total_trades=total_trades

    def get_total_buys(self):
        return self.total_buys

    def set_total_buys(self, total_buys):
        self.total_buys=total_buys

    def get_total_sells(self):
        return self.total_sells

    def set_total_sells(self, total_sells):
        self.total_sells=total_sells

    def get_profit(self):
        return self.profit

    def set_profit(self, profit):
        self.profit=profit

    def get_total_stock_value(self):
        return self.total_stock_value

    def set_total_stock_value(self, total_stock_value):
        self.total_stock_value=total_stock_value


