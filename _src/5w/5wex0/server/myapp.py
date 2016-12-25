#/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, render_template
import db

app = Flask(__name__)
app.debug = True 

@app.route('/', methods=['GET', 'POST'])
def Note():
	if request.method == 'POST':
		if request.form['newnote']:
			text = request.form['newnote']
			if text == '$d':
				db.Delete(-1)
			elif text.startswith('$d ') and text[3:].isdigit():
				i = int(text[3:])
				db.Delete(i)
			elif text.startswith('$d -') and text[4:].isdigit():
				j = int(text[4:])
				db.Delete(-j)
			else:
				db.AddNote(text)
		return redirect('/')
	notes = db.GetNotes()
	notes_reverse = list(reversed(notes))
	return render_template('note.html',notes=notes_reverse)

@app.route('/tags') # 待完善：标签浏览和管理
def Export():
	info = u' \n 功能开发中...'
	return render_template('info.html', info=info)

@app.route('/about')
def ShowAbout():
	info = u' \n极简笔记本应用 by sunoonlee\n\
		- for omooc2py 5wex0  \nContact:\n- Github/weibo: sunoonlee\n\
		- Email: helloliming@gmail.com'
	return render_template('info.html', info=info)

@app.route('/count') # 统计笔记数量
def Count():
	notes_num = db.GetNum()
	info = ' \n%s notes in total.' % notes_num
	return render_template('info.html', info=info)
