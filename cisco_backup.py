#!/usr/bin/env python
#-*- coding: utf-8 -*-import sys


import time
import getpass
import os
import sys
import cmd
import datetime
import telnetlib
print "Default encoding : " + sys.getdefaultencoding()
print " "

#
username = raw_input("Enter your telnet username : ")
print " "
password = getpass.getpass()
print " "

#set date and time
now = datetime.datetime.now()

#PRINT FILES LOCATION
cwd = os.getcwd()
print("This script and all input files are located in : ") + cwd

print (" ")

def banner():
        cisco_config_backup_automation = """\033[92m



                    *                               *
                   ***                             ***
                   ***                             ***
                   ***                             ***
            *      ***      *               *      ***      *
           ***     ***     ***             ***     ***     ***
    *      ***     ***     ***      *      ***     ***     ***      *
   ***     ***     ***     ***     ***     ***     ***     ***     ***
   ***     ***     ***     ***     ***     ***     ***     ***     ***
   ***     ***     ***     ***     ***     ***     ***     ***     ***
    *       *      ***      *       *       *      ***      *       *
                   ***                             ***
                   ***                             ***
                    *                               *


\033[0m"""
        return cisco_config_backup_automation


print banner()
print " "



## DEPEND THE IP ADDRESS DECLARED IN THE FILE - THE LOOP
## .......WILL CONNECT TO EACH MATERIALS.

## YOU SHOULD HAVE SAME USER & PASSWORD 


#START
f = open('cisco_hosts')
for fline in f:
	#BACKUP FILE NAME
	filename_prefix ='backup_cisco_HOST_' + fline
	print "Connecting to host " + (fline)
	HOST = fline
	tn = telnetlib.Telnet(HOST)
	#session start
	tn.read_until("Username:")
	tn.write(username+"\n")
	tn.read_until("Password:")
	tn.write(password+"\n")
        print " "
        print ("Successful connection to host : ") + fline
        print " "
	#Warning: Setting the length to 0, which disables paging, can be useful,
        #...but it can present a problem on long output.
	tn.write("terminal length 0"+"\n")
        #show running configuration and write output
	tn.write("sh run"+"\n")
	tn.write("exit"+"\n")
	print " "
        #show output config and write file with prefix, date and time
	output=tn.read_all()
        print (output)
	filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)

	fp=open(filename,"w")
	fp.write(output)
	fp.close()

	print tn.read_all()

f.close()
