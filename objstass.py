#!/usr/bin/python2
import os,cgitb,sys,time
import commands
import cgi

#cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

a=cgi.FieldStorage()
drive=a.getvalue('a')
size=a.getvalue('f')

lvcreate='sudo lvcreate --name {} --size M mydevice'.format(drive,size)
createlv=getstatusoutput(lvcreate)

lvformat='sudo mkfs.ext4  /dev/mydevice/' +drive
formatlv=getstatusoutput(lvformat)

os.system('sudo mkdir  /mnt/' +drive)
os.system('sudo mount  /dev/mydevice/' +drive+ ' /mnt/' +drive)

os.system('sudo yum install nfs-utils -y')
x = getstatusoutput("sudo echo /mnt/" +drive+ " *'(rw,no_root_squash)' >> /etc/exports")
y = getstatusoutput("sudo echo mkdir /media/" +drive+ " >> /var/www/html/st.sh")
print y
z = getstatusoutput("sudo echo mount 192.168.122.1:/mnt/" +drive+ " /media/" +drive+ " >> /var/www/html/st.sh")
print z


os.system('sudo systemctl restart nfs-server')
os.system('sudo systemctl enable nfs-server')

print "<a href='http://192.168.122.1/st.sh'>"
print "click here to get storage"
print "</a>

check=os.system('exportfs -r')
if check==0:
	print "done"

