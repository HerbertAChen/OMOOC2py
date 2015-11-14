#/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, route, request, template
import sae, sae.kvdb
from datetime import datetime

def NewNote(text):
	kv = sae.kvdb.Client()
	notes = kv.get('notes')
	if not notes:
		notes = []

	time = str(datetime.now())
	new_note = {'content':text, 'time':time}
	notes.append(new_note)

	kv.set('notes', notes)
	kv.disconnect_all()

def GetNotes(): # 返回全部笔记的列表
	kv = sae.kvdb.Client()
	allnotes = kv.get('notes')
	if allnotes == None:
		return [{}]
	else:
		return allnotes
	kv.disconnect_all()	

app = Bottle()

@app.route('/')
def ShowPage():
	notes = GetNotes()
	notes.reverse()
	return template('easynote', notes=notes)

@app.route('/', method='POST')
def CreateNote():
	text = unicode(request.forms.get('newnote'), 'utf-8') 
	# 用 unicode() 可解决网页提交中文写入数据库的问题，但命令行下仍有问题	
	if text:
		NewNote(text)
	notes = GetNotes()
	notes.reverse()
	return template('easynote', notes=notes)

@app.route('/about')
def ShowPage():
	info = [u'极简笔记本应用 by sunoonlee', 'for omooc2py 5wex0']
	return template('info', info=info)

@app.route('/contact')
def ShowPage():
	info = ['Github: sunoonlee', 'Email: helloliming@gmail.com']
	return template('info', info=info)

#app.run(host='localhost', port=8080, debug=True, reloader=True)
application = sae.create_wsgi_app(app)