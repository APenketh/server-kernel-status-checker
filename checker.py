#!/usr/bin/env python

import os, yum, time, socket, sys, platform

yumB = yum.YumBase()
serverHostname = socket.gethostname()

def getDist():
	distName = platform.linux_distribution()[0]
	global osVersion

	if distName.upper() in ["RHEL", "CENTOS", "FEDORA", "CENTOS LINUX"]:
		osVersion = distName
	elif distName.upper() in ["DEBIAN", "UBUNTU"]:
		print "{0} Based Systems Are Currently Not Compatible With This Script.".format(distName)
		exit()
	else:
		print "Platform {0} Is Not Compatible With This Script.".format(distName)
		exit()

def yumCheck():
        print "Yum Status:"
        print "---------------------"

def kernelCheck():
        print "Kernel Version Status:"
        print "---------------------"

getDist()
	
print "---------------------"
print "Server Name:", serverHostname
print "Operating System Version:", osVersion, platform.linux_distribution()[1]
print "---------------------"
yumCheck()
print "---------------------"
kernelCheck()
print "---------------------"
