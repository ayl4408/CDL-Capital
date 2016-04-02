#!/usr/bin/python

import time
import sys, LINK_HEADERS
sys.path.insert(0,str(LINK_HEADERS.DATABASE_LINK))
sys.path.insert(0,str(LINK_HEADERS.MODELS_LINK))
from company_model import Company
from company_dao import Company_dao
from database_class import DB
from login_model import Login
from PDO import PDO
sys.path.insert(0 , str(LINK_HEADERS.DAO_LINK))
from transaction_dao import Transaction_dao

class Sector_info_dao:#{
    db_connection = None

    def __init__(self):
        self.db_connection = PDO().get_connection(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)

    def get_sector_by_symbol(self, symbol):
        SQL="SELECT sector FROM sector_info WHERE symbol='%s'";
        result=self.db_connection.query(SQL % (symbol))
        return result[0]['sector']
            
    def group_by_sector(self,username):
    
        t_dao=Transaction_dao()
        c_dao=Company_dao()
        distinct_stocks=t_dao.get_user_stock_list(username)

    
        sector_volume={}
        
        for symbol in distinct_stocks:
            company_info=c_dao.get_company_model(symbol)
            volume=t_dao.get_owned_stock_model(username,symbol,company_info.get_ask()).get_volume()

            try:
                sector=self.get_sector_by_symbol(symbol);
                if(sector.strip()==''):sector="Other"
            except:
                sector="Other"
                
            
            if(sector not in sector_volume):
                sector_volume[sector]=volume;
            else:
                sector_volume[sector]+=volume
        
        return sector_volume;
#}
    
