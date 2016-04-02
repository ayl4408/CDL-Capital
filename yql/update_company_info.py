#!/usr/bin/python
from datetime import datetime
import sys,simplejson,re,time,LINK_HEADERS, update, json
from yahoo_finance_class import YQLQuery
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
sys.path.insert(0, str(LINK_HEADERS.ALGORITHMS_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
from googlefinance import getQuotes
from types import *
from decimal import *
import algorithm
###global variables
column_query_result= None
column_names = None
num_columns = None
none_stock_list = []
         

###Sanitizes result of db query to retrieve ticker symbols from database and puts into list 
## @param result=all sticker symbols from db
def create_result_list(result):
    l=[]
    for i in range(len(result)):
        if "^" in result[i]['symbol'] or "." in result[i]['symbol']:
            continue
        else:
            l.append(result[i]['symbol'].replace(" ",""))
    return l

###converts ticker list into a string and executes yql query at intervals of 100 
## @param l = list of ticker symbols
## @param yql = YQLQuery object 
def request_yql(l,yql,db):
    START_YQL = "select " + column_names +  " from yahoo.finance.quotes where symbol in ('"
    END_YQL = "');"    
    result_string=""
    final=0
    counter=0
    for i in range(len(l)):
        result_string += l[i]
        counter+=1
        final+=1

	if counter==40 or final == len(l):
	    yql_query=START_YQL + result_string + END_YQL
            while True:
                yql_result=yql.execute(yql_query)
                if "query" in yql_result.keys():
		    break
                else:
                    time.sleep(1)
            #####analyze_ask(yql_result,db,result_string)        
            isGood=update_company_info(yql_result,result_string,db)
            result_string=""
	    counter=0
        else:
            result_string += ","
       
###updates company information in database
## @param yql_result = yql query result with stock data for all stock symbols in database 
## @param db = db object
def update_company_info(yql_result,result_string,db):
    global none_stock_list
    START_SQL="INSERT INTO company_info(" + column_names + ")" + "VALUES"
    END_SQL= ""
    VALUES_LIST=[]
    stored_stock_ask_dict={}
    result_string_list=result_string.split(",")
    for stock in result_string_list:
        stock = "'" + stock + "'"
    result_string = str(result_string_list).strip("[]")
    SQL="SELECT Symbol, Ask FROM company_info WHERE Symbol in (" + result_string + ")"
    previous_ask_list = db.query(SQL)
    for stock_ask in previous_ask_list:
        stored_stock_ask_dict[stock_ask['Symbol']]=stock_ask['Ask']
#    print stored_stock_ask_dict
    for x in range(int(yql_result['query']['count'])):
        values=[]
        ask = str(yql_result['query']['results']['quote'][x]['Ask'])
        symbol = str(yql_result['query']['results']['quote'][x]['Symbol'])
        goog_ask = ""
        try:
            previous_ask=stored_stock_ask_dict[symbol]
        except Exception, e:
            error="key doesn't exist"
            continue
        if ask == "None":          ##if yql ask is None
            try:
                goog_json=getQuotes(symbol)
                goog_ask = str(goog_json[0]['LastTradePrice'])
                print goog_ask + type(goog_ask)
                if goog_ask == "None":
                    SQL = "DELETE FROM company_info WHERE Symbol = '" + symbol + "';"
                    db.query(SQL)
                    continue
            except Exception, e:
                if previous_ask == 'None' or previous_ask == 'NULL':      ##if stored ask is null or None skip calculation
                    SQL = "DELETE FROM company_info WHERE Symbol ='" + symbol + "';"
                    db.query(SQL)
                    continue
        elif Decimal(ask) > 9000:           ##if yql ask is greater than 9000 
            try:
                goog_json=getQuotes(symbol)
                goog_ask = str(goog_json[0]['LastTradePrice'])
            except Exception, e:
                SQL = "DELETE FROM company_info WHERE Symbol = '" + symbol + "';"
                db.query(SQL)
                continue
                #error=str(e)
                #print str(e)
        if previous_ask != "None" and previous_ask != "NULL" and ask != "None":
            ask_difference =  Decimal(ask) - Decimal(previous_ask)
            try:
                percent_change = abs(ask_difference / Decimal(previous_ask))
            except Exception, e:
                print str(e)
            if percent_change > 1:
                if Decimal(ask) > 1 and Decimal(previous_ask) > 1:
                    try:
                        goog_json=getQuotes(symbol)
                        goog_ask = str(goog_json[0]['LastTradePrice'])
                    except Exception, e:
                        error=str(e)
                        #fail_stock_list.append(symbol)
                        #print str(e)
        for key, value in yql_result['query']['results']['quote'][x].iteritems():
            #print key
            if key == "Ask" and goog_ask != "":
                #print ("stock: " + yql_result['query']['results']['quote'][x]['Symbol'] + "    yql_value: " + str(value) + "   stored_value: " + str(previous_ask))
                value = goog_ask 
                #print ("value after: " + str(value))
            value=str(value).replace("'","\\'")
            values.append(value)
        values=tuple(values)
        VALUES_LIST.append(values)
    VALUES_LIST=str(VALUES_LIST).strip("[]")
    #print VALUES_LIST
    for x in range(num_columns):
        END_SQL+= str(column_query_result[x]) + "=VALUES(" + str(column_query_result[x]) + "),"        
    END_SQL=END_SQL[:-1] + ";"
    		
    SQL_QUERY=START_SQL + VALUES_LIST + " ON DUPLICATE KEY UPDATE " + END_SQL
    try:
#        print SQL_QUERY
        db.query(SQL_QUERY)
    except Exception, e :
        error_log = open('/usr/lib/cgi-bin/kchang_cdlcapital/logs/update_company_log.txt','a')
        error_log.write(str(e))
        print str(e) 
        error_log.close()

def main(): 
    global column_query_result, num_columns, column_names
    db = DB(LINK_HEADERS.DB_HOST, LINK_HEADERS.DB_USER, LINK_HEADERS.DB_PASSWORD, LINK_HEADERS.DB_NAME)
    result = db.get_stock_symbols()
    l = create_result_list(result)
    column_query_result=db.get_column_names()
    num_columns=len(column_query_result)
    column_names=str(column_query_result).strip("[]")
    column_names=column_names.replace("'","")
    #print column_names 
    opening_time = "13:30:00"
    closing_time = "20:00:00"
    while True:
        current_time = datetime.utcnow().strftime("%H:%M:%S")
        start=time.time()
        if current_time > opening_time or current_time < closing_time:
            yql= YQLQuery()
            print "request: " + str(current_time)
            request_yql(l,yql,db)
            update.main()
            algorithm.main()
            runtime=time.time()-start
            if runtime < 252:
                sleeptime=252 - runtime
                time.sleep(sleeptime)
        else:
            exit()

if __name__ == "__main__":        
    main()
