#/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import get, post, request, run, jinja2_view
import Easynote

@get('/note')
@jinja2_view('note.html')
def ShowPage():
	notes = Easynote.GetNotes()
	return {'notes':notes}

@post('/note')
@jinja2_view('note.html')
def CreateNote():
	note = unicode(request.forms.get('newnote'), 'utf-8') 
	# 用 unicode() 可解决网页提交中文写入数据库的问题，但命令行下仍有问题
	
	if note:
		Easynote.NewNote(note)
	notes = Easynote.GetNotes()

	return {'notes':notes}

run(host='localhost', port=8080, debug=True, reloader=True)