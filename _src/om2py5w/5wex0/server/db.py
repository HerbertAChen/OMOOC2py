#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Database operation module.
'''
from datetime import datetime
import sae.kvdb

def key_plus_one(last_key):
	new_indx = int(last_key[4:]) + 1
	new_key = last_key[:4] + '%05u' % new_indx
	return new_key

def AddNote(text): # 把新笔记写入 kvdb
	kv = sae.kvdb.Client()
	keys = kv.getkeys_by_prefix('note')
	keys.sort()
	new_key = key_plus_one(keys[-1]) if keys else 'note00001'
	time = str(datetime.now())
	new_note = {'text':text, 'time':time}
	kv.set(new_key, new_note)
	kv.disconnect_all()

def GetNotes(): # 从 kvdb 获取全部笔记的列表
	kv = sae.kvdb.Client()
	keys = kv.getkeys_by_prefix('note')
	keys.sort()
	notes = [kv.get(key) for key in keys]
	return notes if notes else [{}]
	kv.disconnect_all()	

def GetNum():
	kv = sae.kvdb.Client()
	notes_num = len(kv.getkeys_by_prefix('note'))
	kv.disconnect_all()
	return notes_num

def Delete(i):
	num = GetNum()
	if -num <= i < num:
		kv = sae.kvdb.Client()
		keys = kv.getkeys_by_prefix('note')
		keys.sort()
		kv.delete(keys[i])
		kv.disconnect_all()
	else:
		pass

def DeleteAll():
	kv = sae.kvdb.Client()
	keys = kv.getkeys_by_prefix('note')
	for key in keys:
		kv.delete(key)
	kv.disconnect_all()