#!/bin/bash

serverHostname=$(hostname)

kernelCheck()   {
        currentKernel=$(uname -r)
        currentKernel="kernel-$currentKernel"
        latestInstalledKernel=$(rpm -q kernel | tail -n 1)
        latestKernel=$(yum list updates kernel -q --disableexcludes=all 2>&1)

        echo "Kernel Version Status:"
        echo "---------------------"
        if [ "$latestKernel" == "Error: No matching Packages to list" ] ; then
                if [ "$currentKernel" == "$latestInstalledKernel" ] ; then
                        echo "    Server Kernel Is On The Latest Version: $currentKernel"
                else
                        echo "    Server Kernel Is Not Running On The Latest Version"
                        echo "        Server is on the Kernel version:      $currentKernel"
                        echo "        Latest Kernel installed is:           $latestInstalledKernel"
                fi
        else
                latestNewKernel=$(echo $latestKernel | awk '{print $4}')
                latestNewKernel="kernel-$latestNewKernel"
                if [ "$currentKernel" != "$latestNewKernel" ] ; then
                        echo "    Their Is A Newer Kernel Avalible To Download:"
                        echo "        Server is on the Kernel version:          $currentKernel"
                        echo "        Latest Kernel available via download is:  $latestNewKernel"
                else
                        echo ""
                fi
        fi
                }

yumCheck()      {
        echo "Yum Status:"
        echo "---------------------"
        if [[ ! -f /var/lock/subsys/yum-cron ]]; then
                echo "    Nightly Yum Update Is Disabled"
        else
                echo "    Nightly Yum Update Is Enabled"
        fi

        if [[ ! -f /var/log/yum.log ]]; then
                echo "    Can't find the yum log to check when the last update occoured"
        else
                lastUpdateCheck=$(tail -n1 /var/log/yum.log | awk '{print $1, $2}')
                echo "    The last update occoured: $lastUpdateCheck"
        fi

        echo ""

        echo "    Yum Exclusions:"
        if [[ ! -f /etc/yum.conf ]]; then
                echo "        Cannot locate your yum configuration file to check for exclusions"
        elif grep --quiet ^exclude= /etc/yum.conf; then
                yumExcludesCheck=$(grep ^exclude= /etc/yum.conf)
                echo "        You currently have the following exclusions set in your yum configuration: $yumExcludesCheck"
        else
                echo "        You Have No Exclusions Set Up"
        fi
                }

echo "---------------------"
echo "Server Name: $serverHostname"
echo "---------------------"
yumCheck;
echo "---------------------"
kernelCheck;
echo "---------------------"
