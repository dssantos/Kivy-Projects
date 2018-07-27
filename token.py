import requests

def get_token(domain, login, password, project):

	# domain = 'Default'
	# login = 'admin'
	# password = '123456'
	# project = 'admin'

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
	
	#print r.headers['X-Subject-Token']
	return r.headers['X-Subject-Token']

# get_token('Default', 'admin', '123456', 'admin')

