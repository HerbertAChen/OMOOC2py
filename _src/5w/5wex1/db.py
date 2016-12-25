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

def insert_note(text, author_id): # 把新笔记写入 kvdb
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('note') if key[4:].isdigit()]
	keys.sort()
	new_key = key_plus_one(keys[-1]) if keys else 'note00001'
	time = str(datetime.now())
	author_name = get_user_by_id(author_id).get('username', '')
	new_note = {'text':text, 'time':time, 'author_name':author_name}
	kv.set(new_key, new_note)
	kv.disconnect_all()

def get_notes_by_author(author_name): #  从 kvdb 获取指定用户的笔记列表
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('note') if key[4:].isdigit()]
	keys.sort()
	notes = [kv.get(key) for key in keys if \
			kv.get(key).get('author_name','')==author_name]
	kv.disconnect_all()	
	return notes if notes else [{}]

def get_all_notes(): #  从 kvdb 获取全部笔记列表
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('note') if key[4:].isdigit()]
	keys.sort()
	notes = [kv.get(key) for key in keys]
	kv.disconnect_all()	
	return notes if notes else [{}]

def get_num():
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('note') if key[4:].isdigit()]
	notes_num = len(keys)
	kv.disconnect_all()
	return notes_num

def delete_note(i):
	num = GetNum()
	if -num <= i < num:
		kv = sae.kvdb.Client()
		keys = [key for key in kv.getkeys_by_prefix('note') if key[4:].isdigit()]
		keys.sort()
		kv.delete(keys[i])
		kv.disconnect_all()
	else:
		pass

def delete_all_notes():
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('note') if key[4:].isdigit()]
	for key in keys:
		kv.delete(key)
	kv.disconnect_all()

def insert_user(username, pw_hash):
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('user') if key[4:].isdigit()]
	keys.sort()
	new_key = key_plus_one(keys[-1]) if keys else 'user00001'
	new_user = {'username':username, 'pw_hash':pw_hash}
	kv.set(new_key, new_user)
	kv.disconnect_all()	

def get_user(username):
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('user') if key[4:].isdigit()]
	user = None
	for key in keys:
		if kv.get(key).get('username', '') == username:
			user = kv.get(key)
			break
	kv.disconnect_all()	
	return user # as a dict, or None

def get_user_by_id(id):
	kv = sae.kvdb.Client()
	user_key = 'user%05u' % id
	user = kv.get(user_key)
	kv.disconnect_all()	
	return user

def get_userid_by_name(username):
	kv = sae.kvdb.Client()
	keys = [key for key in kv.getkeys_by_prefix('user') if key[4:].isdigit()]
	user = None
	for key in keys:
		if kv.get(key).get('username', '') == username:
			user_key = key
			break
	kv.disconnect_all()	
	return int(key[4:])

# user 字典的键：username, pw_hash