try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import simplejson,sys

# Yahoo! YQL API
PUBLIC_API_URL  = 'http://query.yahooapis.com/v1/public/yql'
OAUTH_API_URL   = 'http://query.yahooapis.com/v1/yql'
DATATABLES_URL  = 'store://datatables.org/alltableswithkeys'

#GLOBALS
ASK= "select Ask from yahoo.finance.quotes where symbol in ('"
END_YQL = "');"

class YQLQuery(object):
    
    def __init__(self):
        self.connection = HTTPConnection('query.yahooapis.com')
        
    def execute(self, yql, token = None):
        self.connection.request('GET', PUBLIC_API_URL + '?' + urlencode({ 'q': yql, 'format': 'json', 'env': DATATABLES_URL }))
        return simplejson.loads(self.connection.getresponse().read())

    def __del__(self):
        self.connection.close()

    def get_ask_price(self, company):
        result = self.execute(ASK + str(company) + END_YQL)
        return result['query']['results']['quote']['Ask']

#yql= YQLQuery()

#print yq.get_ask_price('TWTR')
#print yql.get_all_symbols()
