#coding: utf-8

import status

domain = 'Default'
login = 'admin'
password = '123456'
project = 'admin'

hosts = status.get(domain, login, password, project)
texto = ''
for host in hosts:

    nome = host['hostname']
    estado = host['state']
    ram = str(host['ram'])
    vms = str(host['vms'])

    msg =   '\n' + nome + \
            '\nEstado: ' + estado + \
            '\nRam: ' + ram + \
            '\nVMs: ' + vms + '\n'

    texto = texto + msg

print texto