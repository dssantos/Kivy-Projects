#coding: utf-8

def get(host):

	file = open("%s.txt"%host, "r+")
	mac = file.read()
	return mac