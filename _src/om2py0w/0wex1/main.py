# -*- coding: utf-8 -*-
# 0wex1 EasyNote
from datetime import datetime
filename = 'mynotes.txt'

def main():
	head = '\n### EasyNote ###' 
	prompt = '''
[A] adding a new note
[L] listing all notes
[H] help
[E] exit
 '''
 	helpmsg = '''
 #### Help ####
 1. The notes are stored in mynotes.txt in current directory.
 2. For more info, please refer to README.md.
 '''
	print head
	input = raw_input(prompt).upper()
	while (input != 'E'):
		if input == 'A':
			AddNote()
		elif input == 'L':
			ListNotes()
		elif input == 'H':
			print helpmsg
		else:
			print 'Warning: Not a legal option!\n'
		raw_input('Press Enter to continue')
		input = raw_input(prompt).upper()

def AddNote():
	f = open(filename,'a')
	newnote = raw_input('New note:\n> ')
	curdatetime = str(datetime.now())[0:19]
	f.write('[%s] %s\n' % (curdatetime, newnote))
	f.close()
	print 'Note added!'

def ListNotes():
	f = open(filename,'r')
	notes = f.readlines()
	print '#### List of Notes ####\n'
	for note in notes:
		print note
	print '#### Total Num: %d ####' % len(notes)

if __name__=='__main__':
 	 main()