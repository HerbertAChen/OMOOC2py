#/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, route, request, jinja2_view
import sae, sae.kvdb
from datetime import datetime

def NewNote(text): # 把新笔记写入 kvdb
	kv = sae.kvdb.Client()
	notes = kv.get('notes')
	if not notes: notes = []

	time = str(datetime.now())
	new_note = {'content':text, 'time':time}
	notes.append(new_note)

	kv.set('notes', notes)
	if text == 'cleaR':
		kv.delete('notes')
	kv.disconnect_all()

def GetNotes(): # 从 kvdb 获取全部笔记的列表
	kv = sae.kvdb.Client()
	allnotes = kv.get('notes')
	result = allnotes if allnotes else [{}]
	return result
	kv.disconnect_all()	


app = Bottle()

@app.route('/')
@jinja2_view('easynote.html')
def ShowPage():
	notes = GetNotes()
	notes_reverse = list(reversed(notes))
	return {'notes':notes_reverse}

@app.route('/', method='POST')
@jinja2_view('easynote.html')
def CreateNote():
	text = unicode(request.forms.get('newnote'), 'utf-8') 
	if text: NewNote(text)
	notes = GetNotes()
	notes_reverse = list(reversed(notes))
	return {'notes':notes_reverse}

@app.route('/tags') # 待完善：标签浏览和管理
@jinja2_view('info.html')
def Export():
	info = [u'功能开发中...']
	return {'info': info}

@app.route('/about')
@jinja2_view('info.html')
def ShowAbout():
	about = [u'极简笔记本应用 by sunoonlee','- for omooc2py 5wex0', '',
			'Contact:','- Github/weibo: sunoonlee','- Email: helloliming@gmail.com']
	return {'info': about}

@app.route('/admin') # 供管理员用：统计笔记数量等
@jinja2_view('info.html')
def Admin():
	kv = sae.kvdb.Client()
	get_notes = kv.get('notes')
	notes_num = len(get_notes) if get_notes else 0
	kv.disconnect_all()
	return {'info': ['%s notes in total.' % notes_num]}

#@app.route('/delete_all') # 供管理员用：清空笔记！
#def delete_all():
#	kv = sae.kvdb.Client()
#	kv.delete('notes')
#	kv.disconnect_all()
#	return "All notes deleted!"

application = sae.create_wsgi_app(app)