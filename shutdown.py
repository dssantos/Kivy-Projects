#coding: utf-8

from subprocess import Popen, PIPE, STDOUT

def run(host):

	command = "ssh user@%s 'sudo shutdown now'" %host

	p = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True) # Executa o comando e armazena o STDOUT
	output = p.stdout.read()
	print output

	# if output == 'Connection to %s closed by remote host.' %host:
	# 	print 'O host %s está sendo desligado' %host

	# else:
	# 	print 'O host %s não foi encontrado' %host