#coding: utf-8

import subprocess, mac

def run(host):

	mac_address = mac.get(host)
	command = "sudo etherwake -i eno1 %s" %mac_address
	output = subprocess.check_output(command, shell=True)