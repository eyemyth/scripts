#!/bin/bash

# 2012-02-26 jay@techsuperpowers.com
# Disables "On My Mac" Address Book source

for USER in `ls -1 /Users | sed -e '/Shared/d' -e '/Deleted Users/d' -e '/.localized/d'`; do

defaults write /Users/$USER/Library/Application\ Support/AddressBook/Configuration disabled -int 1

exit 0