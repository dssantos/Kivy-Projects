# -*- coding: utf-8 -*-
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyRoot(BoxLayout):

    def get_token(self,instance):
        password = self.ids.password.text
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
                                "name": \""""+ self.ids.domain.text +"""\"
                            },
                        "name": \""""+ self.ids.login.text +"""\",
                        "password": \""""+ self.ids.password.text +"""\"
                        }
                    }
                },
                "scope": {
                    "project": {
                        "domain": {
                            "name": \""""+ self.ids.domain.text +"""\"
                        },
                        "name": \""""+ self.ids.project.text +"""\"
                    }
                }
            }
        }
        """
        UrlRequest('http://controller:5000/v3/auth/tokens', self.print_token, req_headers=headers, req_body=body)
        print body
    def print_token(self, req, result):
        token = req.resp_headers['x-subject-token']
        print token

        self.ids.token.text = token

    
    def get_status_host(self, instance):
        server = self.ids.server_name.text
        headers = {'X-Auth-Token':self.ids.token.text}
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

        self.ids.status.text = msg

class MainApp(App):
	pass

if __name__ == '__main__':
    MainApp().run()