#coding: utf-8

import requests
import token
import ast

#### Validar se o token está válido, caso contrário renovar !!



def get_hosts():

	headers = token_renew()

	r = requests.get('http://controller:8774/v2.1/os-hypervisors', headers=headers)
	result = ast.literal_eval(r.content)
	#result = ast.literal_eval("{'hypervisors': [{'status': 'enabled', 'state': 'up', 'id': 0, 'hypervisor_hostname': 'compute'}, {'status': 'enabled', 'state': 'up', 'id': 1, 'hypervisor_hostname': 'compute1'}]}")
	result = result['hypervisors']
	for host in result:
		print host['hypervisor_hostname']

	return result

def token_renew():

	tk = token.get_token('Default', 'admin', '123456', 'admin')
	#headers = {'X-Auth-Token':'gAAAAABbWoWjrxQyzF9cUM5p0ZNfqsPLosTUI8MInNmiI7HnBDp9sttSK2FSo7wTs-XWBTx6ecI-PCEpIuI572x_iJJnJEOuJRk-lj58WUxxgn4a97gPdFMnzlXarWONnQfIhcxf-D5b5D53HkaX58mmfmMqL1Y-EzGDljrCS-4LTMk2ADgwwVo'}
	headers = ast.literal_eval("{'X-Auth-Token':'"+tk+"'}")
	return headers

get_hosts()