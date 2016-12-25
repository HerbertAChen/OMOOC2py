#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

HOST = '10.0.0.3'
PORT = 9999
BUFSIZ = 10240

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print 'Type "q" or "quit" to exit.'
print 'Type "l" or "list" to view all the notes.'
print 'Type "l[hostname]" or "list[hostname]" to view notes from specified host.'
print 'Type anything else as a new note.'

while True:
	INPUT = raw_input('$ ').strip()
	inp = INPUT.lower()
	if inp in ['quit','q']:
		break
	elif inp in ['list','l']:
		data_send = INPUT
	elif inp.endswith(']') and (inp.startswith('l[') or inp.startswith('list[')):
		data_send = INPUT
	else:
		data_send = '[%s] %s' % (socket.gethostname(), INPUT)
	s.sendto(data_send, (HOST, PORT))
	print s.recv(BUFSIZ)
s.close