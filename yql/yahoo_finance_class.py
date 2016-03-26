try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import simplejson,sys, time

# Yahoo! YQL API
PUBLIC_API_URL  = 'http://query.yahooapis.com/v1/public/yql'
OAUTH_API_URL   = 'http://query.yahooapis.com/v1/yql'
DATATABLES_URL  = 'store://datatables.org/alltableswithkeys'

#GLOBALS
ASK= "select Ask from yahoo.finance.quotes where symbol in ('"
END_YQL = "');"

class YQLQuery(object):

    connection = None

    def __enter__(self):
        self.connection = None

    def __init__(self):

        while True:
            self.connection = HTTPConnection('query.yahooapis.com')

            if self.connection != None:
                break
            else:
                time.sleep(1)
            
    def execute(self, yql, token = None):
        while True:
            self.connection.request('GET', PUBLIC_API_URL + '?' + urlencode({ 'q': yql, 'format': 'json', 'env': DATATABLES_URL }))
            try:
                return simplejson.loads(self.connection.getresponse().read())
            except Exception, e:
		error_log = open('/usr/lib/cgi-bin/kchang_cdlcapital/logs/yql_log.txt', 'a')
                error_log.write(str(e))
	        print str(e)
		error_log.close()
                time.sleep(1)

    def __del__(self):
        self.connection.close()
                
    def __exit__(self,type_, value, traceback):
        print "closing connection"
        self.connection.close()

    def get_ask_price(self, company):
        while True:
            result = self.execute(ASK + str(company) + END_YQL)
            if "query" in result.keys():
                return result['query']['results']['quote']['Ask']
            time.sleep(1)
            
#yql= YQLQuery()
#print yql.get_ask_price('TWTR')
#print yql.get_all_symbols()
