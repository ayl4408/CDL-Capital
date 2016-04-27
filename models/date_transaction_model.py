#/usr/bin/python

class Date_transaction:
    
    def __init__(self):
        self.date = None;
        self.num_trades = None;
        self.profit = None;
    
    def get_date(self):
        return self.date
    
    def set_date(self, x):
        self.date = x

    def get_num_trades(self):
        return self.num_trades
    
    def set_num_trades(self, x):
        self.num_trades = x

    def get_profit(self):
        return self.profit

    def set_profit(self, x):
        self.profit = x

