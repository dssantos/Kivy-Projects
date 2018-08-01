#coding: utf-8

import subprocess
import string
import ast
import host_list

def get_status(hosts): # O método deve receber um lista de hosts. Ex: ["ds","localhost", "66.55.64.169"]

	mem_status = range(len(hosts)) # Inicialiaza a lista que vai armazenar os dados de cada host

	for host in hosts:

		command = "ssh user@" + host + " 'free -m | grep Mem'" # Comando para obter informações de RAM do host remoto
		
		try:
			output = subprocess.check_output(command, shell=True)  # Recebe a saída do comando acima
			mem_info = string.split(output) # Transforma strings de valores separados por espaços em uma lista
			uso = float(mem_info[2])/float(mem_info[1])*100 # Calcula o percentual de uso da RAM

		except subprocess.CalledProcessError:
			uso = 0.0  # Caso o host não seja alcançado, o comando resultará erro, então o uso da RAM será zero

		key = host
		value = str(uso)

		mem_status[hosts.index(host)] = "\""+key+"\":"+value # Insere os valores em dicionários

	mem_status = ','.join(mem_status)	# Organiza os valores como um dicionário
	mem_status = "{"+mem_status+"}"		#
	mem_status = ast.literal_eval(mem_status) # Converte o tipo de string para dict

	print mem_status
	return mem_status

get_status(host_list.get_hosts())
