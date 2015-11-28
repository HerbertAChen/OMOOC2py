#/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, render_template,\
	session, url_for, g, flash, abort
from werkzeug import check_password_hash, generate_password_hash
import db

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app = Flask(__name__)
app.debug = True 


@app.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = db.get_user_by_id(session['user_id'])


@app.route('/')
def notes():
	if not g.user:
		return redirect(url_for('all_notes'))
	cur_username = db.get_user_by_id(session['user_id'])['username']
	return render_template('notes.html',notes=reversed(db.get_notes_by_author(cur_username)))


@app.route('/allnotes')
def all_notes():
	return render_template('notes.html',notes=reversed(db.get_all_notes()))


@app.route('/<username>')
def user_notes(username):
	profile_user = db.get_user(username)
	if profile_user is None:
		abort(404)
	return render_template('notes.html',
							notes=reversed(db.get_notes_by_author(username)),
							profile_user=profile_user)


@app.route('/add_note', methods=['POST'])
def add_note():
	if 'user_id' not in session:
		abort(401)
	if request.form['text']:
		text = request.form['text']
		db.insert_note(text, session['user_id'])
		#flash('New note added.')
	return redirect(url_for('notes'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if g.user:
		return redirect(url_for('notes'))
	error = None
	if request.method == 'POST':
		if not request.form['username']:
			error = 'You have to enter a username'
		elif not request.form['password']:
			error = 'You have to enter a password'
		elif request.form['password'] != request.form['password2']:
			error = 'The two passwords do not match'
		elif db.get_user(request.form['username']) is not None:
			error = 'The username is already taken'
		else:
			db.insert_user(request.form['username'],generate_password_hash(request.form['password']))
			#flash('You were successfully registered and can login now')
			return redirect(url_for('login'))
	return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if g.user:
		return redirect(url_for('notes'))
	error = None
	if request.method == 'POST':
		user = db.get_user(request.form['username'])
		if user is None:
			error = 'Invalid username'
		elif not check_password_hash(user['pw_hash'], request.form['password']):
			error = 'Invalid password'
		else:
			#flash('You were logged in')
			session['user_id'] = db.get_userid_by_name(user['username'])
			return redirect(url_for('notes'))
	return render_template('login.html', error=error)


@app.route('/logout')
def logout():
	#flash('You were logged out')
	session.pop('user_id', None)
	return redirect(url_for('all_notes'))

app.secret_key = SECRET_KEY