# Check The Current Status Of Yum & The Kernel

This is a bash script to check the status of both yum and the kernel, this allows you to easily identify if your server requires a reboot to get onto the latest kernel version or needs to download a new kernel if it is avalible from your package manager.

Currently supports RHEL/CentOS 6 & 7

Example Output:

```
Server : example.localhost

Kernel Version Status:
---------------------
Server Kernel Is Not Running On The Latest Version
    Server is on the Kernel version:      3.10.0-514.6.1.el7.x86_64
    Latest Kernel installed is:           kernel-3.10.0-514.10.2.el7.x86_64
```

Note: This script is very much in a development phase and although has been tested to work it is understood that you will run it at your own risk.
