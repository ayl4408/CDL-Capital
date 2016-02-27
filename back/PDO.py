#!/usr/bin/python

from database_class import DB

class PDO:#{
    #Python Data Object (PDO)
    #use PDO().get_connect() to ensure exactly 1 instance of DB() object is created

    db_connection = None
    
    def get_connection(self, hostname, username, password, db):
        if(PDO.db_connection == None):
            
            PDO.db_connection=DB(hostname, username, password, db)
            return PDO.db_connection

        else:
            return PDO.db_connection
        
#}
