#!/usr/bin/python

from templite import Templite
import Cookie, LINK_HEADERS

f = open("login.tpl","r")
html = str(f.read())
f.close()

t = Templite(html)
print "Content-Type: text/html\r\n\r\n"
print t.render(validate_login_link=LINK_HEADERS.VALIDATE_LOGIN_LINK)
