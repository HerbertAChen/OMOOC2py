#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://sunote.sinaapp.com/'

def main():
	print 'Type "q" or "quit" to exit.'
	print 'Type "l" or "list" to view all the notes.'
	print 'Type anything else as a new note.'

	while True:
		INPUT = raw_input('$ ').strip()
		inp = INPUT.lower()
		if inp in ['quit','q']:
			break
		elif inp in ['list','l']:
			print listnotes()
		else:
			addnote(INPUT)

def addnote(note):
	requests.post(url, data = {'newnote':note})
	print 'note added!'

def listnotes():
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	lis = soup.find_all('p')
	notes = ''
	for i in lis:
		notes += i.get_text()+'\n'
	return notes

if __name__ == '__main__':
	main()