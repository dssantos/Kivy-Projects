#coding: utf-8

import time, sys, status, shutdown, wake, ast, mac

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
	
	lim_max = 70
	lim_med = 35

	if ram_avg > lim_max:						## Se RAM estiver acima do limite máximo
		if len(idle) > 0:
			if len(idle) > 1:					## Mantêm 1 ocioso ligado, mas desliga os demais
				for i in range(len(idle)-1):	# Desliga todos menos 1
					print 'desligando %s' %idle[i+1]
					shutdown.run(idle[i+1])
		else:
			if len(offline) > 0:				# Se existir hosts offline ...
				print 'ligando %s %s' %(offline[0], mac.get(offline[0]))
				wake.run(offline[0]) 			# Acorda o primeiro host offline da lista
			else:
				print 'Não há mais hosts offline para ligar.\nO sistema está no limite!!!'
	else:
		if len(idle) > 0:
			if ram_avg >= lim_med:				## Se RAM estiver entre os limites médio e máximo
				for i in range(len(idle)-1):	# Desliga todos menos 1
					print 'desligando %s' %idle[i+1]
					shutdown.run(idle[i+1])
			else:
				if len(running) >= 1:		## Se houver pelo menos 1 host ativo
					for host in idle:				
						print 'desligando %s' %host
						shutdown.run(host)		# Desliga todos os hosts ociosos
				else:								# Senão...
					for i in range(len(idle)-1):	# Desliga todos menos 1
						print 'desligando %s' %idle[i+1]
						shutdown.run(idle[i+1])

def start():
		
	while True:

		print '\n\nVerificando Hosts...\n'
		run()

		for i in xrange(120,-1,-1):
		     print "  Próxima verificação: %3d\r"%i,
		     time.sleep(1)
		     sys.stdout.flush()

