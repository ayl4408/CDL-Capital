#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
from random import randint
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
sys.path.insert(0, str(LINK_HEADERS.DATABASE_LINK))
from database_class import DB
print "Content-Type: text/html\r\n\r\n"

 
db = DB("localhost","root","mmGr2016","cdlcapital")


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def percentchange_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    swap(array, left, k)
    array[left]["PercentChange"] = array[left]["PercentChange"].translate(None, '+%')
    pivot = float(array[left]["PercentChange"])
   
    l = left + 1
    r = right

    while(l<= r):
        
        array[l]["PercentChange"] = array[l]["PercentChange"].translate(None, '+%')
	while(l<=r and float(array[l]["PercentChange"]) <= pivot):
	    l += 1
	    if(l>r):
		break;
            array[l]["PercentChange"] = array[l]["PercentChange"].translate(None, '+%')

        array[r]["PercentChange"] = array[r]["PercentChange"].translate(None, '+%')
	while(l<=r and float(array[r]["PercentChange"]) >= pivot):
	    r -= 1
	    if(l>r):
		break;
            array[r]["PercentChange"] = array[r]["PercentChange"].translate(None, '+%')

	if(l<r):
	    swap(array, l, r)
	    l+=1
	    r-=1
    swap(array, left, r)
    percentchange_quick_sort(array, left, r-1)
    percentchange_quick_sort(array, r+1, right)


def main():

    result = db.query("SELECT symbol, PercentChange FROM company_info WHERE PercentChange IS NOT NULL AND PercentChange!='None';")

    percentchange_quick_sort(result, 0, len(result)-1)

    json_object=[]

    for i in range(0, 5):
	json_object.append(result[i])

    for i in range(len(result)-1, len(result)-6, -1):
	json_object.append(result[i])

    json_object.append(len(result))
    json_result = json.dumps(json_object)
    print json_result

main()
