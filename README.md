# Check The Current Status Of Yum & The Kernel

This is a bash script to check the status of both yum and the kernel, this allows you to easily identify if your server requires a reboot to get onto the latest kernel version or needs to download a new kernel if it is avalible from your package manager.

Currently supports RHEL/CentOS 6 & 7

Example Output:

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
    Their Is A Newer Kernel Avalible To Download:
        Server is on the Kernel version:          kernel-3.10.0-327.36.3.el7.x86_64
        Latest Kernel available via download is:  kernel-3.10.0-514.10.2.el7
---------------------
```

### Usage:
You can run this script stright from your command line by running the following.
```
curl https://raw.githubusercontent.com/APenketh/yum-kernel-status-checker/master/checker.sh | sh
```
Note: This script is very much in a development phase and although has been tested to work it is understood that you will run it at your own risk.
