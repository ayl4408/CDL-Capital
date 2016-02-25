#!/usr/bin/python

import cgi, datetime, sys, LINK_HEADERS
import simplejson as json
from random import randint

 


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def quick_sort(array, left, right, field):
    if left >= right:
        return
    k = randint(left, right)
    swap(array, left, k)
    
    array[left][field] = array[left][field].translate(None, '+%') # Do this because float() won't read "+'s & %'s but it will read -'s, need to strip them
    pivot = float(array[left][field])
   
    l = left + 1
    r = right

    while(l<= r):
        
        array[l][field] = array[l][field].translate(None, '+%')
	while(l<=r and float(array[l][field]) <= pivot):
	    l += 1
	    if(l>r):
		break;
            array[l][field] = array[l][field].translate(None, '+%')

        array[r][field] = array[r][field].translate(None, '+%')
	while(l<=r and float(array[r][field]) >= pivot):
	    r -= 1
	    if(l>r):
		break;
            array[r][field] = array[r][field].translate(None, '+%')

	if(l<r):
	    swap(array, l, r)
	    l+=1
	    r-=1
    swap(array, left, r)
    quick_sort(array, left, r-1, field)
    quick_sort(array, r+1, right, field)

def quick_sort_nofloatconversion(array, left, right, field):
    if left >= right:
        return
    k = randint(left, right)
    swap(array, left, k)
    
    #pivot = float(array[left][field])
    pivot = array[left][field]

    l = left + 1
    r = right

    while(l<= r):
        
	while(l<=r and array[l][field] <= pivot):
	    l += 1
	    if(l>r):
		break;

	while(l<=r and array[r][field] >= pivot):
	    r -= 1
	    if(l>r):
		break;

	if(l<r):
	    swap(array, l, r)
	    l+=1
	    r-=1
    swap(array, left, r)
    quick_sort_nofloatconversion(array, left, r-1, field)
    quick_sort_nofloatconversion(array, r+1, right, field)

