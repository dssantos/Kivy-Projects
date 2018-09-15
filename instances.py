#coding: utf-8

import requests, ast, header, subprocess, time, sys

r = requests.get('http://controller:8774/v2.1/servers', headers=header.get())
vm_list = ast.literal_eval(r.content) # Retorna o conteúdo da URL consultada
vm_list = vm_list['servers']
length = len(vm_list)

def get():
	vms = []
	pos = length -1

	while pos > -1:

		vm =  vm_list[pos]['name']
		pos -= 1
		vms.append(vm)

	print vms
	return vms

def on(qt_on):

	pos = len(get()) + 1
	while qt_on > 0:
		vm = 'vm-%s' %pos
		print 'ligando %s' %vm
		command = "ssh user@controller '. admin-openrc && openstack server create --image cirros --flavor=1CPU_128RAM %s'" %vm
		run = subprocess.check_output(command, shell=True)  # Recebe a saída do comando acima
		qt_on -= 1
		pos += 1

def off(qt_off):

	vms = get()
	pos = length	
	if qt_off <= length:

		while pos > length-qt_off:
			vm = vms[pos-1]
			print 'desligando %s' %vm
			command = "ssh user@controller '. admin-openrc && openstack server delete %s'" %vm # Comando para 
			run = subprocess.check_output(command, shell=True)  # Recebe a saída do comando acima
			pos -= 1


	else:
		print 'Só existem %s VMs para desligar' %length

def auto_on(limit):

	while True:

		pos = len(get()) + 1
		vms = []
		for x in range(limit):
			vm = 'vm-%s'%pos
			pos += 1
			print 'ligando %s' %vm
			command = "ssh user@controller '. admin-openrc && openstack server create --image cirros --flavor=1CPU_128RAM %s'" %vm
			run = subprocess.check_output(command, shell=True)  # Recebe a saída do comando acima
			vms.append(vm)
			for i in xrange(30,-1,-1):
				print "  Próxima inicialização: %3d\r"%i,
				time.sleep(1)
				sys.stdout.flush()

		for vm in reversed(vms):
			print 'desligando %s' %vm
			command = "ssh user@controller '. admin-openrc && openstack server delete %s'" %vm # Comando para 
			run = subprocess.check_output(command, shell=True)  # Recebe a saída do comando acima		

			for i in xrange(30,-1,-1):
				print "  Próxima inicialização: %3d\r"%i,
				time.sleep(1)
				sys.stdout.flush()
