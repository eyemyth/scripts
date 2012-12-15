#!/usr/bin/python
# coding: utf-8

"""2012-12-10 jay@techsuperpowers.com"""
"""python script to enable FileVault2 via Casper Self Service"""

import getpass
import os
import commands
import plistlib
import tempfile
import subprocess
import base64
import sys

# if enabling via command line, use 2 and 3 instead of 4 and 5
adminName = sys.argv[4]
adminPass = sys.argv[5]

# we have to decode the already base64 encoded cert since plistlib.Data re-encodes any string as base64

certificate = base64.standard_b64decode('paste your base64 encoded cert from FileVaultMaster.keychain here')

def passwordPrompt():
	global name
	global password
	# assuming cocoadialog exists at this path...
	CocoaDialog = "/Library/Application\ Support/CocoaDialog.app/Contents/MacOS/CocoaDialog"
	console_owner = "ls -l /dev/console"
	result = commands.getoutput(console_owner)
	name = result.split(' ')[3]
	# I should probably add some logic to make it at least ask for password twice
	cmd = CocoaDialog + " standard-inputbox --title \"FileVault Enabler\" --no-newline --informative-text \"Enter password for "+name+"\" --no-cancel --float --no-show"
	results = commands.getoutput(cmd)
	password = results.split('\n')[1]
	credentials = [name, password]
	return credentials

passwordPrompt()

# this is the plist template

d = {	'Username':adminName,	
		'Password':adminPass,
		'AdditionalUsers':[ { 'Username':name, 'Password':password } ],
		'Certificate':plistlib.Data(certificate)
		}

def createPlist():
	global output_file
	output_file = tempfile.NamedTemporaryFile(suffix='.plist')
	plistlib.writePlist(d, output_file)
	output_file.seek(0)

def encryptVolume():
	output_file = tempfile.NamedTemporaryFile(suffix='.plist', delete=False)
	plistlib.writePlist(d, output_file)
	output_file.seek(0)
	plist = output_file.name
	# subprocess.check_call("fdesetup enable -inputplist %s" % plist, shell=True)
	subprocess.check_call("fdesetup enable -norecoverykey -forcerestart -inputplist < %s" % plist, shell=True)



encryptVolume()
