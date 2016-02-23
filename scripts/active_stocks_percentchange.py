#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from company_class import Company
import quick_sort_companyinfo

print "Content-Type: text/html\r\n\r\n"

 

c = Company()

def main():

    result = c.get_all_percentchange()
    quick_sort_companyinfo.quick_sort(result, 0, len(result)-1, "PercentChange")

    json_object=[]

    for i in range(0, 5):
	json_object.append(result[i])

    for i in range(len(result)-1, len(result)-6, -1):
	json_object.append(result[i])

    json_object.append(len(result))
    json_result = json.dumps(json_object)
    print json_result

main()
