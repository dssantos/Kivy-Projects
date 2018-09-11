#coding: utf-8

import test_status, shutdown, wake

def run():
	
	hosts = test_status.get()
	ram = []
	running = []
	idle = []
	offline = []

	for host in hosts:	# Insere os hosts que estão ligados (e possuem VMs) em uma lista de ativos 
		if host['vms'] > 0:
			running.append(host['hostname'])
			ram.append(host['ram']) # Captura os consumos de memória e insere em uma lista

	for host in hosts: # Insere os hosts que estão ligados, mas não possuem VMs, em uma lista de ociosos
		if host['vms'] == 0:
			idle.append(host['hostname'])

	for host in hosts: # Insere os hosts que estão desligados em uma lista de offline
		if host['vms'] < 0:
			offline.append(host['hostname'])

	try:
		ram_avg = sum(ram) / len(ram) # Calcula a média de memória em uso dos hosts ativos
	except:
		ram_avg = 0
	
	print 'ativos: ' + str(running)
	print 'ociosos: ' + str(idle)
	print 'offline: ' + str(offline)
	print 'média de ram: %s' %ram_avg

## Lógica do gerenciamento dos hosts a serem ligados e desligados
	if ram_avg >= 75:
		if len(idle) > 0:
			if len(idle) > 1:
				print 'desligar %s' %idle[0]
				shutdown.run(idle[0])		
		else:
			print 'ligando %s' %offline[0]
			wake.run(offline[0]) 			# Acorda o primeiro host offline da lista
	else:
		if len(idle) > 0:
			# for host in idle:				# Desliga todos os hosts ociosos
			# 	shutdown.run(host)
			for i in range(len(idle)-1):	# Desliga todos menos 1
				shutdown.run(idle[i+1])

run()