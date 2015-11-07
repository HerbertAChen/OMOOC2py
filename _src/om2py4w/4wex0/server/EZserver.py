#/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import * # get, post, template, request, run
import Easynote

@get('/note')
def ShowPage():
	notes = Easynote.GetNotes()
	return template('EZ_template', notes=notes)

@post('/note')
def CreateNote():
	note = request.forms.get('newnote')
	if note:
		Easynote.NewNote(note)
	notes = Easynote.GetNotes()
	return template('EZ_template', notes=notes)

run(host='localhost', port=8080, debug=True, reloader=True)