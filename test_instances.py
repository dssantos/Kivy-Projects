#!/usr/bin/python
#coding: utf-8

import sys, instances, time

arg1 = sys.argv[1]
if len(sys.argv) > 2:
	arg2 = int(sys.argv[2])


if arg1 == 'on':
	instances.on(arg2)

if arg1 == 'off':
	instances.off(arg2)

if arg1 == 'list':
	instances.get()

if arg1 == 'auto':
	instances.auto_on(arg2)
		
