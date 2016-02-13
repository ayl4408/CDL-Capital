#!/usr/bin/python

import sys,simplejson,re,time,datetime,LINK_HEADERS
from yahoo_finance_class import YQLQuery
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB

def get_column_names():
    get_column_names="select column_name from information_schema.columns where table_name='company_info'"
    column_result=str(db.query(get_column_names))
    column_result=re.sub("[()',]*",'',column_result)
    column_result=column_result.split(' ')
    return column_result

###Sanitizes result of db query to retrieve ticker symbols from database and puts into list 
## @param result=all sticker symbols from db
def create_result_list(result):
    l=[]
    for i in result:
        if "^" in i[0] or "." in i[0]:
            continue
        else:
            l.append(i[0].replace(" ",""))
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
	    yql_result=yql.execute(yql_query)
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
        #END_SQL="WHERE symbol=" + re.sub("['*]",)'',str(yql_result['query']['results']['quote'][x]['symbol']))
        END_SQL="WHERE symbol=" + "'" + str(yql_result['query']['results']['quote'][x]['symbol']) + "'" + ";"
        for key, value in yql_result['query']['results']['quote'][x].iteritems():
            if key == "Change" or key == "Symbol":
                continue
            if "'" in str(value):
                value=str(value).replace("'","\\'")
            START_SQL+=str(key) + "=" + str("'{}'".format(value)) + ","
	START_SQL=START_SQL[:-1]
	sql_query=START_SQL + " " + END_SQL
	if "ZTR" in sql_query:
            print sql_query
        db.query(sql_query)   

def main(): 
    yql = YQLQuery()
    db = DB("localhost","root","mmGr2016","cdlcapital")
    result = db.get_stock_symbols()
    l = create_result_list(result)

    while(1):
        opening_time = "14:30:00"
        closing_time = "22:30:00"
        current_time = datetime.datetime.utcnow().strftime("%H:%M:%S")

        if current_time > opening_time and current_time < closing_time:
            request_yql(l,yql,db)
        time.sleep(120)
            
    #print "Stocks in the DB: " + str(len(result))
    #print "Stocks after Parse: " + str(len(l))
    
main()
