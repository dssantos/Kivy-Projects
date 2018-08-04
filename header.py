#coding: utf-8

import requests, ast

def get(domain, login, password, project):

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
	token = r.headers['X-Subject-Token']
	headers = ast.literal_eval("{'X-Auth-Token':'"+token+"'}")  # Dicionário com o Token que será utilizado no cabeçalho das consultas via API
	
	return headers