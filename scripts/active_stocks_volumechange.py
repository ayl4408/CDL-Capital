#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
from company_class import Company
import quick_sort_companyinfo

print "Content-Type: text/html\r\n\r\n"

c = Company()

def percent_differences_volumechange(volume_array, averagedailyvolume_array):
    percent_difference = []
    for i in range(len(volume_array)):
	volume = volume_array[i]["Volume"] 
	averagedailyvolume = averagedailyvolume_array[i]["AverageDailyVolume"]
	if((volume is not None and volume!="None") and (averagedailyvolume is not None and averagedailyvolume!="None")):
	    difference = (float(volume) / float(averagedailyvolume)) - 1 # the reason for -1 is b/c we want 0.00 to be the no change mark not 1.00
	    percent_difference.append({"symbol" : volume_array[i]["symbol"], "volume_change" : difference})

    return percent_difference

def main():
	
    volume_array = c.get_all_volume()
    averagedailyvolume_array = c.get_all_averagedailyvolume()

    quick_sort_companyinfo.quick_sort_nofloatconversion(volume_array, 0, len(volume_array)-1, "symbol")
    quick_sort_companyinfo.quick_sort_nofloatconversion(averagedailyvolume_array, 0, len(averagedailyvolume_array)-1, "symbol")	

    percent_difference_array = percent_differences_volumechange(volume_array, averagedailyvolume_array)

    quick_sort_companyinfo.quick_sort_nofloatconversion(percent_difference_array, 0, len(percent_difference_array) -1, "volume_change")

    result = []
    for i in range(len(percent_difference_array)-1, len(percent_difference_array)-11, -1):
	 result.append(percent_difference_array[i])

    json_result = json.dumps(result)	
    print json_result

main()    
