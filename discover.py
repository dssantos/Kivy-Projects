#coding: utf-8

import requests, header, ast, mac

def run():

	r = requests.get('http://controller:8774/v2.1/os-hypervisors', headers=header.get())
	hosts = ast.literal_eval(r.content) # Retorna o conteúdo da URL consultada
	hosts = hosts['hypervisors']

	discovered = []

	for host in hosts:

		state = host['state']
		if state == 'up':
			hostname = host['hypervisor_hostname']
			discovered.append(hostname)
			mac.set(hostname)
			mac_address = mac.get(hostname)
			print hostname + " " + mac_address

	file = open("registered.txt", "w+")
	file.write(str(discovered))
	file.close()

	return discovered

run()