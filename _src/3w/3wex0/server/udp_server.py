#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import Easynote as EZ

HOST = '10.0.0.3'
PORT = 9999
BUFSIZ = 10240

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))
print 'Bind UDP on %s...' % PORT
while True:
	data_recv, addr = s.recvfrom(BUFSIZ)
	data_low = data_recv.lower()
	if data_low.startswith('l'):
		filter = ''
		if data_low in ['l', 'list']:
			filter = 'all'
		elif data_low.endswith(']') and (data_low.startswith('l[') or data_low.startswith('list[')):
			filter = '[' + data_low.partition('[')[2]
		notes = EZ.GetNotes(filter) # 从 mynotes.txt 获取 notes
		if notes == '': # 该返回值表示 文件尚未创建，或筛选词 filter 不合要求，参Getnotes()定义
			data_send = 'Nothing on server.'
		else:
			data_send = ''.join(notes['notes'])
		print 'Request to list notes.\n - from: %s:%s' % addr
	else:
		EZ.NewNote(data_recv)
		data_send = 'Note added.'
		print 'Newnote: "%s"\n - from: %s:%s' % (data_recv, addr[0], addr[1])
	s.sendto(data_send, addr)