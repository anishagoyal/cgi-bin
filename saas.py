#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

print "Content-type:text/html\r\n\r\n"
print ""


a=cgi.FieldStorage()

f=a.getvalue('f')
v=a.getvalue('f')
g=a.getvalue('f')
w=a.getvalue('f')
s=a.getvalue('f')
c=a.getvalue('f')
i=a.getvalue('f')
o=a.getvalue('f')


if f=='firefox':
	print "<META HTTP-EQUIV='refresh'  content ='0;url=/firefox.sh'/>"
	#print "<a HTTP-EQUIV='refresh' content ='0;url=/firefox.sh'/>"

elif v=='vlc':
	print "<meta http-equiv='refresh'  content ='0;url=/vlc.sh'/>"

elif g=='gedit':
	print "<meta http-equiv='refresh'  content ='0; url=/gedit.sh'/>"

elif w=='webcam':
	print "<meta http-equiv='refresh'  content ='0; url=/webcam.sh'/>"

elif s=='screenshot':
	print "<meta http-equiv='refresh'  content ='0; url=/screenshot.sh'/>"

elif c=='calculator':
	print "<meta http-equiv='refresh'  content ='0; url=/calculator.sh'/>"

elif i=='imageviewer':
	print "<meta http-equiv='refresh'  content ='0; url=/imageviewer.sh'/>"

elif o=='openoffice':
	print "<meta http-equiv='refresh'  content ='0; url=/openoffice.sh'/>"

else:
	
	print "<script>alert('You have not selected anything')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=/saas.html'/>"

