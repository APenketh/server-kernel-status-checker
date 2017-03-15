#!/bin/bash

serverHostname=$(hostname)

kernelCheck()   {
        currentKernel=$(uname -r)
        latestInstalledKernel=$(rpm -q kernel | tail -n 1)
        latestKernel=$(yum list updates kernel -q --disableexcludes=all 2>&1)

        isLatestVersion()      {
                if [ "$latestKernel" == "Error: No matching Packages to list" ] ; then
                        echo "    Server is on the Kernel version:      $currentKernel"
                        echo "    Latest Kernel installed is:           $latestInstalledKernel"
                else
                        latestNewKernel=$(echo $latestKernel | awk '{print $4}')
                        if [ "$currentKernel" != "$latestNewKernel" ] ; then
                                echo "    Server is on the Kernel version:          $currentKernel"
                                echo "    Latest Kernel installed is:               $latestInstalledKernel"
                                echo "    Latest Kernel available via download is:  $latestNewKernel"
                        else
                                echo ""
                        fi
                fi
                                }

        echo "Kernel Version Status:"
        echo "---------------------"
        if [ "$currentKernel" == "$latestInstalledKernel" ] ; then
                echo "Server Kernel Is On The Lastest Installed Version: $currentKernel"
                isLatestVersion;
        else
                echo "Server Kernel Is Not Running On The Latest Version"
                isLatestVersion;
        fi
                }

echo "Server : $serverHostname"
echo ""
kernelCheck;
