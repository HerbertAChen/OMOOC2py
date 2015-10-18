# -*- coding: utf-8 -*-
# 0wex1 EasyNote
from datetime import datetime

def main():
	print '\n### EasyNote ###'
	prompt = '''[A]: adding a new note
[L]: listing all notes
[H]: help
[E]: exit
 '''
 	helpmsg = '''#### Help ####
 1. The notes are stored in log.txt in current directory.
 2. For more info, please contact sunoonlee@github.
 '''
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
	f = open('log.txt','a')
	newnote = raw_input('New note:\n> ')
	curtimedate = str(datetime.now())[0:19]
	f.write('[' + curtimedate + '] ' + newnote + '\n')
	f.close()
	print 'Note added!'

def ListNotes():
	f = open('log.txt','r')
	notes = f.readlines()
	print '#### List of Notes ####\n'
	for note in notes:
		print '  '+note
	print '#### Total Num: %d ####' % len(notes)

if __name__=='__main__':
 	 main()      