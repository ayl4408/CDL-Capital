#!/usr/bin/python

import MySQLdb,re
import MySQLdb.cursors

class DB:

    host = None
    user = None
    password = None
    database = None
    session = None
    connection = None

    def __init__(self, db_host, db_user, db_password, db_name):
        self.host = db_host
        self.user = db_user
        self.password = db_password
        self.database = db_name

    def connect(self):
        try:
            conn = MySQLdb.connect(self.host, self.user, self.password, self.database,cursorclass=MySQLdb.cursors.DictCursor)            self.connection = conn
            self.session = conn.cursor()
        except MySQLdb.Error as e:
            print e

    def query(self, query):
        self.connect()
        result = self.session.execute(query)
        self.connection.commit()
        result = self.session.fetchall()
        if len(result):
            result=list(result)
            self.disconnect()
            return result
        else:
            self.disconnect()
            return

    def disconnect(self):
        self.session.close()
        self.connection.close()

    def get_stock_symbols(self):
        self.connect()
        query="select symbol from company_info"
        result=self.session.execute(query)
        if result is not None:
            result=self.session.fetchall()
            self.disconnect()
            return result
        else:
            self.disconnect()
            return

    def get_column_names(self):
        get_column_names="select column_name from information_schema.columns where table_name='company_info'"
        column_result=str(self.query(get_column_names))
        column_result=re.sub("[()',]*",'',column_result)
        column_result=column_result.split(' ')
        return column_result
