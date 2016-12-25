#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://sunote.sinaapp.com/'

def main():
	print '''Type:
- "q" or "quit" to exit
- "l" or "list" to view all the notes
- "num" to get the number of notes
- "clear" to delete all the notes
- "exp" to export notes to "exported_notes.txt"
- or anything else as a new note
'''
	while True:
		INPUT = raw_input('$ ').strip()
		inp = INPUT.lower()
		if inp in ['quit','q']:
			break
		elif inp in ['list','l']:
			print get_notes()
		elif inp == 'num':
			print get_numofnotes()
		elif inp == 'clear':
			delete_notes()
		elif inp == 'exp':
			export_notes()
		else:
			addnote(INPUT)

def addnote(note):
	requests.post(url, data = {'newnote':note})
	print 'Note added!'

def get_notes():
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	lis = soup.find_all('p')
	notes = ''
	for i in lis:
		notes += i.get_text()+'\n'
	return notes

def get_numofnotes():
	r = requests.get(url+'admin')
	soup = BeautifulSoup(r.text,'html.parser')
	info = soup.find_all('p')[0].get_text()
	return info

def delete_notes():
	requests.get(url+'delete_all')
	print 'All notes deleted!'

def export_notes():
	notes = get_notes()
	f = open('exported_notes.txt', 'w')
	f.write(notes)
	f.close()
	print 'Notes exported to "exported_notes.txt"'

if __name__ == '__main__':
	main()