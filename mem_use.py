#coding: utf-8

import subprocess
import string

def get_status(hosts): # O método deve receber um lista de hosts. Ex: ["ds","localhost", "66.55.64.169"]

	result = range(len(hosts)) # Inicialiaza a lista que vai armazenar os dados de cada host

	for host in hosts:

		command = "ssh " + host + " 'free -m | grep Mem'" # Comando para obter informações de RAM do host remoto

		output = subprocess.check_output(command, shell=True)  # Recebe a saída do comando acima

		mem_info = string.split(output) # Transforma os valores de uma strig para uma lista

		uso = float(mem_info[2])/float(mem_info[1])*100 # Calcula o percentual de uso da RAM

		key = host
		value = str(uso)

		result[hosts.index(host)] = "{'"+key+"':"+value+"}" # Insere os valores em dicionários

	result = ','.join(result)	# Formata os dicionários em uma lista
	result = "["+result+"]"		#

	print result

	return result
