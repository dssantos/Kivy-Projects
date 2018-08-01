#coding: utf-8

import requests
import ast

def get_token(domain, login, password, project):

	headers = {'Content-Type':'application/json'}
	payload = """
	{
	    "auth": {
	        "identity": {
	            "methods": [
	            "password"
	            ],
	            "password": {
	                "user": {
	                    "domain": {
	                        "name": \""""+ domain +"""\"
	                    },
	                "name": \""""+ login +"""\",
	                "password": \""""+ password +"""\"
	                }
	            }
	        },
	        "scope": {
	            "project": {
	                "domain": {
	                    "name": \""""+ domain +"""\"
	                },
	                "name": \""""+ project +"""\"
	            }
	        }
	    }
	}
	"""

	r = requests.post('http://controller:5000/v3/auth/tokens', data=payload, headers=headers)

	return r.headers['X-Subject-Token']


def token_renew():

	token = get_token('Default', 'admin', '123456', 'admin')  # Credenciais de autenticação para obtenção do token do Openstack
	token = ast.literal_eval("{'X-Auth-Token':'"+token+"'}")  # Dicionário com o Token que será utilizado no cabeçalho das consultas via API
	
	return token