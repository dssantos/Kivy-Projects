#coding: utf-8

import status, shutdown, wake, ast

def run():
	
	hosts = status.get()
	ram = []
	running = []
	idle = []
	offline = []

	file = open("registered.txt", "r+")
	registered = file.read()	
	registered = ast.literal_eval(registered)

	for host in hosts:	# Insere os hosts que estão ligados (e possuem VMs) em uma lista de ativos 
		if host['state'] == 'up':
			if host['vms'] > 0:
				running.append(host['hostname'])
				ram.append(host['ram']) # Captura os consumos de memória e insere em uma lista

	for host in hosts: # Insere os hosts que estão ligados, mas não possuem VMs, em uma lista de ociosos
		if host['state'] == 'up':
			if host['vms'] == 0:
				idle.append(host['hostname'])

	for host in hosts: # Insere os hosts que estão desligados (e estão registrados) em uma lista de offline
		if host['state'] == 'down':
			if host['hostname'] in registered:
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

	if ram_avg >= 70:						## Se RAM estiver a partir de 75
		if len(idle) > 0:
			if len(idle) > 1:					## Mantêm 1 ocioso ligado, mas desliga os demais
				for i in range(len(idle)-1):	# Desliga todos menos 1
					shutdown.run(idle[i+1])
					print 'desligando %s' %idle[i+1]
		else:
			if len(offline) > 0:				# Se existir hosts offline ...
				print 'ligando %s' %offline[0]
				wake.run(offline[0]) 			# Acorda o primeiro host offline da lista
			else:
				print 'Não há mais hosts offline para ligar.\nO sistema está no limite!!!'
	else:
		if len(idle) > 0:
			if ram_avg >= 50:				## Se RAM estiver entre 50 e 75
				for i in range(len(idle)-1):	# Desliga todos menos 1
					shutdown.run(idle[i+1])
			else:
				if len(running) >= 1:		## Se houver pelo menos 1 host ativo
					for host in idle:				
						shutdown.run(host)		# Desliga todos os hosts ociosos
				else:
					for i in range(len(idle)-1):	# Desliga todos menos 1
						shutdown.run(idle[i+1])
						print 'desligando %s' %idle[i+1]


run()