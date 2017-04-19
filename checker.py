#!/usr/bin/env python

import yum

yumB = yum.YumBase()

def kernelCheck():
	print yumB.conf.logfile

	print yumB.conf.config_file_path

def yumCheck():
	print yumB.conf.logfile
	
if __name__ == '__main__':
	print "---------------------"
	print "Server Name: $serverHostname"
	print "---------------------"
	yumCheck()
	print "---------------------"
	kernelCheck()
	print "---------------------"
