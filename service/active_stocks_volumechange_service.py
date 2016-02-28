#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
sys.path.insert(0, str(LINK_HEADERS.SCRIPTS_LINK))
from company_dao import Company_dao
#import quick_sort_companyinfo

print "Content-Type: text/html\r\n\r\n"

cdao = Company_dao()

def percent_differences_volumechange(volume_array, averagedailyvolume_array):
    percent_difference = []
    for i in range(len(volume_array)):
	volume = volume_array[i].get_volume() 
	averagedailyvolume = averagedailyvolume_array[i].get_avg_daily_volume()
	if((volume is not None and volume!="None") and (averagedailyvolume is not None and averagedailyvolume!="None")):
	    difference = (float(volume) / float(averagedailyvolume)) - 1 # the reason for -1 is b/c we want 0.00 to be the no change mark not 1.00
	    percent_difference.append({"symbol" : volume_array[i].get_symbol(), "volume_change" : difference})

    return percent_difference

def main():
	
    volume_array = cdao.get_all_companies_volume()
    averagedailyvolume_array = cdao.get_all_companies_averagedailyvolume()

    #quick_sort_companyinfo.quick_sort_nofloatconversion(volume_array, 0, len(volume_array)-1, "symbol")
    volume_array.sort(key=lambda x: x.get_symbol(), reverse=False)
    #quick_sort_companyinfo.quick_sort_nofloatconversion(averagedailyvolume_array, 0, len(averagedailyvolume_array)-1, "symbol")	
    averagedailyvolume_array.sort(key=lambda x: x.get_symbol(), reverse=False)

    percent_difference_array = percent_differences_volumechange(volume_array, averagedailyvolume_array)

    #quick_sort_companyinfo.quick_sort_nofloatconversion(percent_difference_array, 0, len(percent_difference_array) -1, "volume_change")
    percent_difference_array.sort(key=lambda x: x["volume_change"])

    result = []
    for i in range(len(percent_difference_array)-1, -1, -1):
    	 result.append(percent_difference_array[i])

    json_result = json.dumps(result)
    #json_result = json.dumps(percent_difference_array)	
    print json_result

main()    
