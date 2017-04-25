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
        yumConfFile = yumB.conf.config_file_path
	package_list = yumB.doPackageLists(pkgnarrow='updates', patterns='', ignore_case=True)

        print "Yum Status:"
        print "---------------------"

        if package_list.updates:
                print 'updates available'
                for pkg in package_list.updates:
                        print pkg
        else:
                print "Their Are No Avalible Updates On This Server, You Are Up to Date"

        for old in yumB.history.old():
                if "Update" in (hpkg.state for hpkg in old.trans_data):
                        print "The last update occurred:", time.ctime(old.beg_timestamp)
                        break

        print ""
        print "    Yum Exclusions:"
        if os.path.exists("{0}".format(yumConfFile)):
                print "found it"
        else:
                print "        Cannot locate the yum configuration file to check for exclusions"

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
