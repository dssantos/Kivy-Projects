#coding: utf-8

import requests
import token
import ast

#### Implementar persistência do token para não precisar renovar em toda consulta

def get_hosts():

	headers = token.token_renew() # Renova o token

	r = requests.get('http://controller:8774/v2.1/os-hypervisors', headers=headers)
	hosts = ast.literal_eval(r.content) # Retorna o conteúdo da URL consultada
	#hosts = ast.literal_eval("{'hypervisors': [{'status': 'enabled', 'state': 'up', 'id': 2, 'hypervisor_hostname': 'compute'}, {'status': 'enabled', 'state': 'up', 'id': 0, 'hypervisor_hostname': 'controller'}, {'status': 'enabled', 'state': 'up', 'id': 1, 'hypervisor_hostname': 'compute1'}]}")
	
	hosts = hosts['hypervisors'] # Armazena uma lista com informações dos hosts localizados
	host_list = range(len(hosts)) # Inicializa a lista que vai armazenar o nome dos hosts

	for host in hosts:
		host_list[hosts.index(host)] = host['hypervisor_hostname'] # Armazena os hostnames de cada host em uma lista

	return host_list