#!/bin/bash

#modify nvram for single user
nvram boot-args="-v -s"

#modify Single User mode for auto fsck -fy
echo 'if [ $HOSTNAME = localhost ] || [ -z $SECURITYSESSIONID ]; then clear; echo "Starting File System Check in 5 seconds, Control-C to quit"; /bin/sleep 6; fsckResult=$(/sbin/fsck -fy); echo "$fsckResult"; /sbin/mount -uw /; echo "$fsckResult" >> /var/log/fsck.log; /bin/rm /var/root/.profile; nvram boot-args=""; echo "Rebooting in 10 seconds."; /bin/sleep 10; /sbin/shutdown -r now; fi' > /var/root/.profile

reboot