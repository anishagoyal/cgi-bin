#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

#cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()
username=data.getvalue('usr')
password=data.getvalue('passwd')


#a=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $1}'")
#b=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $3}'")



if  username == 'root' and password == 'redhat' :
	#print "hello"	
	print "<META HTTP-EQUIV='refresh' content='0; url=/service.html'/>"
		
	
else:	
	print "<script>alert('Wrong Password')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=/login.html'/>"


