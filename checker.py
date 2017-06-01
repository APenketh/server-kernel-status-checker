#!/usr/bin/env python

import os, yum, time, socket, sys, platform, rpm, subprocess, re
from rpmUtils.miscutils import stringToVersion

yumB = yum.YumBase()
yumB.preconf.debuglevel = 0
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

def kernelCheck():
	currentKernel = "kernel-" + platform.release()
	latestInstalledKernel = subprocess.check_output(["rpm -q kernel | tail -n 1"], shell=True).strip()
        package_list = yumB.doPackageLists(pkgnarrow='updates', patterns='', ignore_case=True)

        if package_list.updates:
                for pkg in package_list.updates:
			if pkg == "kernel*":
				latestKernel = pkg
				print latestKernel
        else:
		latestKernel = "non"

        print "Kernel Version Status:"
        print "---------------------"
        if latestKernel == "non":
                if currentKernel == latestInstalledKernel:
                        print "    Server Kernel Is On The Latest Version: {0}".format(currentKernel)
                else:
                        print "    Server Kernel Is Not Running On The Latest Version:"
			print "      You Need To Reboot The Server To Make Use Of The Latest Kernel."
                        print "        Server is on the Kernel version:      {0}".format(currentKernel)
                        print "        Latest Kernel installed is:           {0}".format(latestInstalledKernel)
        else:
                if currentKernel != latestNewKernel:
                        print "    Their Is A Newer Kernel Avalible To Download:"
			print "      You Need To Download The Latest Kernel And Reboot The Server."
                        print "        Server is on the Kernel version:          {0}".format(currentKernel)
                        print "        Latest Kernel available via download is:  {0}".format(latestNewKernel)
                else:
                        print ""

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
                print "    Their Are No Avalible Updates On This Server, You Are Up to Date"

        for old in yumB.history.old():
                if "Update" in (hpkg.state for hpkg in old.trans_data):
                        print "    The last update occurred:", time.ctime(old.beg_timestamp)
                        break

        print ""
        print "    Yum Exclusions:"
        if os.path.exists("{0}".format(yumConfFile)):
                print "found it"
        else:
                print "        Cannot locate the yum configuration file to check for exclusions"

getDist()
	
print "---------------------"
print "Server Name:", serverHostname
print "Operating System Version:", osVersion, platform.linux_distribution()[1]
print "---------------------"
yumCheck()
print "---------------------"
kernelCheck()
print "---------------------"
