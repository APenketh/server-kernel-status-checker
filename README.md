# Check The Current Status Of Server Updates & The Kernel

This is a python script to check the status of both the server updates and the kernel, this allows you to easily identify if your server requires a reboot to get onto the latest kernel version or needs to download a new kernel if it is avalible from your package manager.

Currently is tested in the following Operating Systems: RHEL/CentOS 6 & 7.

Do note that Debian/Ubuntu systems are not supported, just yum based systems.

### Usage

Version 2 of the this script moves away from bash and onto python, this allows the script to do some further checking to make sure it is being run on a supported operating system as well as allowing for a better output format.

Example Output:

```
===============================================================================================
Server Name: localhost                                        OS Version: CentOS Linux 7.3.1611
-----------------------------------------------------------------------------------------------
Server Update Status:
--------------
    Avalible Updates To Download:       Zero. You Are Up To Date
    Last Package Update Time:           Thu Jun  1 06:58:55 2017
    Packages Excluded From Updating:    You Have No Exclusions Set Up
-----------------------------------------------------------------------------------------------
Kernel Version Status:
--------------
You Need To Reboot The Server To Make Use Of The Latest Kernel.
    Server is on the Kernel version:    kernel-3.10.0-514.16.1.el7.x86_64
    Latest Kernel installed is:         kernel-3.10.0-514.21.1.el7.x86_64
===============================================================================================
```

You can run this script stright from your command line by running the following.
```
curl https://raw.githubusercontent.com/APenketh/yum-kernel-status-checker/master/checker.py | python
```

### Version 1

For historical reasons version 1 of this script written in Bash is kept within the archive folder. V1 isavalible for historical reasons only and is not updated, I would avoid running it on any live servers.

```
---------------------
Server Name: localhost
---------------------
Yum Status:
---------------------
    Nightly Yum Update Is Disabled
    The last update occurred: Mar 15

    Yum Exclusions:
        You currently have the following exclusions set in your yum configuration: exclude=atop*
---------------------
Kernel Version Status:
---------------------
    Server Kernel Is Not Running On The Latest Version:
        You Need To Reboot The Server To Make Use Of The Latest Kernel.
        Server is on the Kernel version:      kernel-3.10.0-514.16.1.el7.x86_64
        Latest Kernel installed is:           kernel-3.10.0-514.21.1.el7.x86_64
---------------------
```

Note: This script is very much in a development phase and although has been tested to work it is understood that you will run it at your own risk.
