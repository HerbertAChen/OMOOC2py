#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print 'Type "q" or "quit" to exit.'
print 'Type "l" or "list" to view all the notes.'
print 'Type anything else as a new note.'

while True:
	input = raw_input('$ ').strip()
	if input.lower() in ['quit','q']:
		break
	s.sendto(input, ('127.0.0.1', 9999))
	print s.recv(10240)
s.close