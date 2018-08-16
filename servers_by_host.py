#coding: utf-8

import requests, json, header

def get(host): # O método deve receber um host_id

	headers = header.get('Default', 'admin', '123456', 'admin')
	r = requests.get('http://controller:8774/v2.1/os-hypervisors/%s/servers'%host, headers=headers)
	servers = json.loads(r.content)
	servers= servers['hypervisors'][0]['servers']

	servers_ids = range(len(servers))
	for server in servers:
		servers_ids[servers.index(server)] = server['uuid']

	return servers_ids # Retorna uma lista com os ids dos servers em execução no host