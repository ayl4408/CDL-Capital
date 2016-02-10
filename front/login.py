#!/usr/bin/python

from templite import Templite
import Cookie

f = open("login.tpl","r")
html = str(f.read())
f.close()

t = Templite(html)
print "Content-Type: text/html\r\n\r\n"
print t.render()
