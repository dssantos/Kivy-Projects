#coding: utf-8

import requests, header, ast, vms, ram_usage

def get(domain, login, password, project):

	headers = header.get(domain, login, password, project)  # Credenciais de autenticação para obtenção do token do Openstack

	r = requests.get('http://controller:8774/v2.1/os-hypervisors', headers=headers)
	hosts = ast.literal_eval(r.content) # Retorna o conteúdo da URL consultada
	hosts = hosts['hypervisors']
	## Testes
	# hosts = [{'status': 'enabled', 'state': 'up', 'id': 1, 'hypervisor_hostname': 'compute1'},{'status': 'enabled', 'state': 'up', 'id': 1, 'hypervisor_hostname': 'compute2'},{'status': 'enabled', 'state': 'up', 'id': 1, 'hypervisor_hostname': 'compute3'},{'status': 'enabled', 'state': 'up', 'id': 1, 'hypervisor_hostname': 'compute4'},{'status': 'enabled', 'state': 'up', 'id': 1, 'hypervisor_hostname': 'compute5'}]

	status = range(len(hosts))

	for host in hosts:
		host_id = host['id']
		hostname = host['hypervisor_hostname']
		state = host['state']
		vms_runnig = vms.get(host_id, headers)
		ram = ram_usage.get(hostname)
		host_status = "{'id': " + str(host_id) + ", 'hostname': '" + hostname + "', 'state': '" + state + "', 'vms': " + str(vms_runnig) + ", 'ram': " + str(ram) + "}"
		host_status = ast.literal_eval(host_status)

		status[hosts.index(host)] = host_status

	return status