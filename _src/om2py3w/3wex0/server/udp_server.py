#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import Easynote as EZ

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))
print 'Bind UDP on 9999...'
while True:
	data_recv, addr = s.recvfrom(10240)
	if data_recv.lower() in ['list', 'l']:
		notes = EZ.GetNotes('all') # 从 mynotes.txt 获取 notes
		if notes == '': # 该返回值表示 文件尚未创建
			data_send = 'Nothing on server.'
		else:
			data_send = ''.join(notes['notes'])
		print 'Request to list notes.\n- from: %s:%s' % addr
	else:
		EZ.NewNote(data_recv)
		data_send = 'Note added.'
		print 'Newnote: "%s"\n- from: %s:%s' % (data_recv, addr[0], addr[1])
	s.sendto(data_send, addr)