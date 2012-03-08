#! /bin/bash

killall retroclient
rm -r /Applications/Retrospect\\ Client.app
rm -r /Library/StartupItems/RetroClient
rm /Library/Preferences/retroclient.state
rm -rf /Library/Receipts/retrospectClient.pkg
rm -rf /Library/Receipts/retroclient.pkg

exit 0