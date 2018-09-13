#coding: utf-8

import subprocess

def get(host):

	file = open("%s.txt"%host, "r+")
	mac = file.read()
	return mac

def set(host):

	interface = 'enp0s3'
	command = "ssh user@%s 'cat /sys/class/net/%s/address'" %(host, interface) # Comando para obter mac address
	
	try:
		mac = subprocess.check_output(command, shell=True)  # Recebe a saída do comando acima

	except subprocess.CalledProcessError:
		mac = ''
		print 'Interface %s não encontrada em %s' %(interface, host)

	file = open("%s.txt"%host, "w+")
	file.write(mac)
	file.close()