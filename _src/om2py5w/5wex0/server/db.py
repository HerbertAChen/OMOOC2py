#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Database operation module.
'''
from datetime import datetime
import sae.kvdb

def NewNote(text): # 把新笔记写入 kvdb
	kv = sae.kvdb.Client()
	notes = kv.get('notes')
	if not notes: notes = []

	time = str(datetime.now())
	new_note = {'content':text, 'time':time}
	notes.append(new_note)

	kv.set('notes', notes)
	#if text == 'cleaR':
	#	kv.delete('notes')
	kv.disconnect_all()

def GetNotes(): # 从 kvdb 获取全部笔记的列表
	kv = sae.kvdb.Client()
	allnotes = kv.get('notes')
	result = allnotes if allnotes else [{}]
	return result
	kv.disconnect_all()	

def GetNum():
	kv = sae.kvdb.Client()
	notes = kv.get('notes')
	notes_num = len(notes) if notes else 0
	kv.disconnect_all()
	return notes_num

def delete_all():
	kv = sae.kvdb.Client()
	kv.delete('notes')
	kv.disconnect_all()