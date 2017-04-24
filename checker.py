#!/usr/bin/env python

import os, yum, time, socket, sys, platform

yumB = yum.YumBase()
serverHostname = socket.gethostname()

def yumCheck():
        echo "Yum Status:"
        echo "---------------------"

def kernelCheck():
        print "Kernel Version Status:"
        print "---------------------"
	
print "---------------------"
print "Server Name:", serverHostname
print "---------------------"
yumCheck()
print "---------------------"
kernelCheck()
print "---------------------"
