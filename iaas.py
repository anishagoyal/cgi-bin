#!/usr/bin/python

import socket,cgi,os,sys,commands

print "Content-type:text/html\r\n\r\n"
print ""

a=cgi.FieldStorage()
os_name=a.getvalue('r')
os_ram=a.getvalue('a')
os_cpu=a.getvalue('b')
os_hdd=a.getvalue('k')


if os_name == 'kali':
	install_os='sudo virt-install  --graphics vnc,listen=192.168.122.1,port=5924 --cdrom /root/Downloads/kali5.iso  --ram '+os_ram+' --vcpu '+os_cpu+' --nodisk --name '+os_name

elif os_name == 'redhat':
	install_os='sudo virt-install  --graphics vnc,listen=192.168.122.1,port=5923 --cdrom /root/Downloads/redhat.iso  --ram '+os_ram+' --vcpu '+os_cpu+' --disk path=/var/lib/libvirt/images/'+os_name+'.qcow2,size='+os_hdd+ '  --name '+os_name

else:
	print "<script>alert('Incorrect Selection')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=/iaas.html'/>"


print commands.getstatusoutput(install_os)


 

