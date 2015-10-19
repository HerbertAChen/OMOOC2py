## 0wex1 EasyNote 说明书

### 主要功能

记录单行日记

列出过往日记

### 程序介绍

输入的日记文本将存储在程序所在目录下的 mynotes.txt 文件中

运行程序后，用户有如下4个选项：

* A: add note
* L: list notes
* H: help
* E: exit

保存日记时，程序会自动在文本之前添加当前日期和时间，如：
> [2015-10-18 22:41:07] This is a note.

### 程序代码

```
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
```

### 进展

151018 创建文档
