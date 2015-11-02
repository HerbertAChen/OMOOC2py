#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print 'Type "exit" or "quit" or "q" to exit.'
print 'Type "list" to print existing notes.'
print 'Type anything else as a new note.'

while True:
	input = raw_input('$ ').strip()
	if input.lower() in ['exit','quit','q']:
		break
	s.sendto(input, ('127.0.0.1', 9999))
	print s.recv(1024)
s.close