#/usr/bin/python

#import algorithm_1

import sys, LINK_HEADERS

sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
sys.path.insert(0, str(LINK_HEADERS.SERVICE_LINK))

from company_dao import Company_dao
from active_algorithms_dao import Active_algorithms_dao

from transaction_service import transaction

#from algorithm_class import Algorithm
from fifty_vs_two_hund_mving_avg_class import fifty_vs_two_hund_mving_avg

def main():
    #c = Company_dao()
    #company_model_list = c.get_all_ask()
    a = Active_algorithms_dao()
    active_algorithms_list = a.select_all()

    if active_algorithms_list:
	    fifty_vs_two_hund_mving_avg(active_algorithms_list)

    #algorithm_class = Algorithm(company_model_list)

    #for aam in active_algorithms_list:
	#if aam.get_algo_id() == "1":
	 #   algorithm_class.algorithm_1(aam.get_user())

