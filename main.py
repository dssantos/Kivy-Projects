# -*- coding: utf-8 -*-
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyRoot(BoxLayout):

    def get_token(self,instance):
        headers = {'Content-Type':'application/json'}
        body = """
        {
            "auth": {
                "identity": {
                    "methods": [
                    "password"
                    ],
                    "password": {
                        "user": {
                            "domain": {
                                "name": "Default"
                            },
                        "name": "admin",
                        "password": "123456"
                        }
                    }
                },
                "scope": {
                    "project": {
                        "domain": {
                            "name": "Default"
                        },
                        "name":  "admin"
                    }
                }
            }
        }
        """
        UrlRequest('http://controller:5000/v3/auth/tokens', self.print_token, req_headers=headers, req_body=body)
        
    def print_token(self, req, result):
        token = req.resp_headers['x-subject-token']
        print token

        self.ids.bt2.text = token

    
    def get_status_host(self, instance):
        headers = {'X-Auth-Token':'gAAAAABbSAIvetASpmo9wCUz5p3xXf3DNqL0N0lxaoqVQfGwMrqs3x6tQB_Ok6QVQmZYQaVfFPXfdpVUZM-mCFqfRqgz2ujRtGcdUsPhB7SHNI2QlmH48L8oqcf213GkJMMvQSez7akw6qbDXBwyMqoSn9R2v2tHeEj4y0EYV2CGsHv7P5XBWYE'}
        server = self.ids.server_name.text
        UrlRequest('http://%s/v2.1/os-hypervisors/1'%server, self.print_status_host, req_headers=headers)

    def print_status_host(self, req, result):
    	# tam_list = len(result['nomes'])
    	# x = 0
    	# lista = ''
    	# while(x < tam_list):
     #        lista += str(result['nomes'][x]['id'])
     #        lista += ' '
     #        lista += result['nomes'][x]['nome']
     #        lista += '\n'
     #        x += 1

        # msg = 'Lista:\n\n' + lista + '\nTotal: ' + str(tam_list)
        nome_host = str(result[u'hypervisor'][u'service'][u'host'])
        vms = str(result[u'hypervisor'][u'running_vms'])
        memoria_utilizada = str(result[u'hypervisor'][u'memory_mb_used'])
        memoria_total = str(result[u'hypervisor'][u'memory_mb'])
        percentual_utilizado = float(memoria_utilizada)/float(memoria_total)*100
        msg = \
        'Host: ' + nome_host + '\n' + \
        'VMs: ' + vms + '\n' + \
        'Memoria Utilizada: ' + memoria_utilizada + ' MB\n' + \
        'Memoria Total: ' + memoria_total + ' MB\n' + \
        'Percentual: ' + str(round(percentual_utilizado,1)) + '%\n'
        print msg

        self.ids.bt.text = msg

class MainApp(App):
	pass

if __name__ == '__main__':
    MainApp().run()