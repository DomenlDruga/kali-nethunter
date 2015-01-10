#!/usr/bin/python
import argparse
import sys
sys.path.append("/sdcard/files/modules/")
from keyseed import *

parser = argparse.ArgumentParser(description='Nethunter HID language/launcher')
parser.add_argument('--us', help='Select US keyboard mapping', action='store_true')
parser.add_argument('--fr', help='Select FR keyboard mapping', action='store_true')
parser.add_argument('--es', help='Select ES keyboard mapping', action='store_true')
parser.add_argument('--de', help='Select DE keyboard mapping', action='store_true')
parser.add_argument('--sv', help='Select SV keyboard mapping', action='store_true')
parser.add_argument('--dk', help='Select DK keyboard mapping', action='store_true')
parser.add_argument('--be', help='Select BE keyboard mapping', action='store_true')
parser.add_argument('--no', help='Select NO keyboard mapping', action='store_true')
parser.add_argument('--wincmd', '-w', help='Windows CMD', action='store_true')
parser.add_argument('--win7cmd', '-w7', help='Windows 7 CMD elevated', action='store_true')
parser.add_argument('--win8cmd','-w8', help='Windows 8 CMD elevated', action='store_true')
parser.add_argument('--win_met','-win_met', help='Reverse Windows CMD', action='store_true')
parser.add_argument('--win8_met','-w8met', help='Reverse Windows 8 CMD', action='store_true')
parser.add_argument('--win7_met','-w7met', help='Reverse Windows 7 CMD', action='store_true')

args = parser.parse_args()

# LANGUAGE OPTIONS

if (args.us):
	locale='us'
elif (args.fr):
	locale='fr'
elif (args.de):
	locale='de'
elif (args.es):
	locale='es'
elif (args.sv):
	locale='sv'
elif (args.dk):
        locale='dk'
elif (args.be):
	locale='be'
elif (args.no):
	locale='no'

def read_file(filename):
	try:
		f = open(filename, "rb")
		byte = f.read(1)
		while byte != "":
			byte = f.read(1)
			if byte:
				findinlist(byte, locale)
	finally:
		f.close()

# HID Command Options
if (args.wincmd):
	wincmd(locale)
	print "sleep 2"
	read_file(filename = "/sdcard/files/hid-cmd.conf")
elif (args.win7cmd):
	win7cmd_elevated(locale)
	print "sleep 2"
	read_file(filename = "/sdcard/files/hid-cmd.conf")
elif (args.win8cmd):
	win8cmd_elevated(locale)
	print "sleep 2"
	read_file(filename = "/sdcard/files/hid-cmd.conf")
elif (args.win_met):
	wincmd(locale)
	print "sleep 2"
	read_file(filename = "/sdcard/files/rev-met")
elif (args.win7_met):
	win7cmd_elevated(locale)
	print "sleep 2"
	read_file(filename = "/sdcard/files/rev-met")
elif (args.win8_met):
	win8cmd_elevated(locale)
	print "sleep 2"
	read_file(filename = "/sdcard/files/rev-met")

# All finished - Hit enter
enterb()
