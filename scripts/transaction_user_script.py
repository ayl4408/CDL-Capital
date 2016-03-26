#!/usr/bin/python

import cgi, datetime,sys,LINK_HEADERS
sys.path.insert(0, str(LINK_HEADERS.MODELS_LINK))
sys.path.insert(0, str(LINK_HEADERS.DAO_LINK))
sys.path.insert(0, str(LINK_HEADERS.SERVICE_LINK))

from transaction_service import transaction

print "Content-Type: text/html\r\n\r\n"

form = cgi.FieldStorage()

if form.getvalue("username") != None:
    username = form.getvalue("username")
if form.getvalue("volume") != None:
    volume = int(form.getvalue("volume"))
if form.getvalue("company") != None:
    company = form.getvalue("company")
if form.getvalue("trans_type") != None:
    trans_type = form.getvalue("trans_type")
if form.getvalue("algo_id") !=None:
    algo_id = form.getvalue("algo_id")

            
transaction(username, volume, company, trans_type, algo_id)
