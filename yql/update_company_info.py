#!/usr/bin/python

import sys,simplejson,re,time,datetime,LINK_HEADERS
from yahoo_finance_class import YQLQuery
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

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
    START_YQL = "select * from yahoo.finance.quotes where symbol in ('"
    END_YQL = "');"    
    result_string=""
    final=0
    counter=0

    for i in range(len(l)):
        result_string += l[i]
        counter+=1
        final+=1

	if counter==50 or final == len(l):
	    yql_query=START_YQL + result_string + END_YQL

            while True:
                yql_result=yql.execute(yql_query)
                
                if "query" in yql_result.keys():
                    break
                else:
                    time.sleep(1)
                    
            isGood=update_company_info(yql_result,db)
            result_string=""
	    counter=0
        else:
            result_string += ","
            
###updates company information in database
## @param yql_result = yql query result with stock data for all stock symbols in database 
## @param db = db object
def update_company_info(yql_result,db):
    
    for x in range(int(yql_result['query']['count'])):
        START_SQL="UPDATE company_info SET "
        END_SQL="WHERE symbol=" + "'" + str(yql_result['query']['results']['quote'][x]['symbol']) + "'" + ";"

        for key, value in yql_result['query']['results']['quote'][x].iteritems():
            if key == "Change" or key == "Symbol":
                continue
            if "'" in str(value):
                value=str(value).replace("'","\\'")
            START_SQL+=str(key) + "=" + str("'{}'".format(value)) + ","

        START_SQL=START_SQL[:-1]
	sql_query=START_SQL + " " + END_SQL
        db.query(sql_query)   

def main(): 
    yql = YQLQuery()
    db = DB("localhost","root","mmGr2016","cdlcapital")
    result = db.get_stock_symbols()
    l = create_result_list(result)

    opening_time = "14:30:00"
    closing_time = "21:30:00"
    
    while True:
        current_time = datetime.datetime.utcnow().strftime("%H:%M:%S")

        if current_time > opening_time and current_time < closing_time:
            request_yql(l,yql,db)
            print "request: " + str(current_time)
        else:
            print "NO request: " + str(current_time)
            time.sleep(540)
        time.sleep(1)
    
main()
