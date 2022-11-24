#!/usr/bin/python

import subprocess
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface ", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac ", dest="mac", help="New MAC address")
	return parser.parse_args()

def change_mac_address(interface, mac):
	print("[!!] Changing MAC address to " + mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", mac])
	subprocess.call(["ifconfig", interface, "up"])
	print("...")
	subprocess.call(["ifconfig", interface])
	
(options, arguments) = get_arguments()
change_mac_address(options.interface, options.mac)
