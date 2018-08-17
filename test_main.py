#coding: utf-8

import status

hosts = status.get()
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