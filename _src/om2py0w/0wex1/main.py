# -*- coding: utf-8 -*-
# 0wex1 EasyNote
from datetime import datetime
import shelve

filename = "mynotes.txt"

def main():
	head = '''
## EasyNote v1.0 ##
Type "help" for more infomation.''' 
	
	helpmsg = u'''
### 命令说明
* "new" -- 新建笔记
* "exit" -- 退出
* "list [笔记集合]" -- 列出指定的笔记集合
* "del [笔记集合]" -- 删除指定的笔记集合
* 注：
    1. [笔记集合]可以是 "all" 或 "笔记编号(多个编号用逗号隔开)"
       或 "date:[yymmdd]-[yymmdd]" 或 "tag:[标签名]"
    2. [笔记集合] 中不应包含空格!
'''	
	print head
	cmd = raw_input('$ ').lower().strip()
	while (cmd not in ['exit','quit','q']):
		cmdwords = cmd.split(' ') # 分解用户指令
		length = len(cmdwords)

		if cmd in ['help', 'h', '?']:
			print helpmsg
		elif cmd in ['new', 'n']:
			NewNote()
		elif cmd == 'list':
			ListNotes('all')
		elif length >= 2:
			word1, word2 = cmdwords[0], cmdwords[1]
			if length == 2 and word1 == 'list':
				ListNotes(word2)
			#elif length == 2 and word1 == 'del':
			#	DelNotes(word2)
			else:
				print 'Invalid command!\n'
		else:
			print 'Invalid command!\n'
		cmd = raw_input('$ ').lower().strip()
		
def NewNote():
	f = open(filename,'a')
	note  = raw_input('New note:\n>>> ').strip()
	if input != '':
		time = str(datetime.now())[0:19] # 去掉秒数的小数部分
		f.write('%s   %s\n' % (time, note))
		f.close()
		print 'Note added!'

def ListNotes(filter):
	result = SelectNotes(filter)
	if result != -1:
		selected, indexes = result[0], result[1]
		if len(selected) == 0:
			print 'Nothing selected!中文' # 不加u会显示乱码, 为什么!
		else:
			print '\n%s   %s   %s' % (
				' No', ' '*9+'CreateTime', 'Content')
			print '%s   %s   %s' % (' --', ' '*9+'-'*10, '-'*7) 
			for i in range(len(selected)):
				print '% 3d   %s' % (indexes[i], selected[i]),
			print '\n     %d notes listed.\n' % len(selected)
		
#def DelNotes(db, filter):

#def Group():

def SelectNotes(filter): #输入filter，返回符合条件的笔记编号和内容
	# 如何区分两种意外情况：1、错误输入，2、未找到符合条件的note
	f = open(filename,'r')
	notes = f.readlines()
	f.close()
	selected, indexes = [], []
	if filter == 'all':
		selected = notes
		indexes = range(len(notes))
		return [selected, indexes]
#	elif filter.split(',') 都是 digit:
#		if 0 < num < len(notes):
#			for id in filter_nums：
#				selected[id] = db[id]
#			return [selected, indexes]
#		else:
#			print 'Note_index out of range.'
#			return -1
	elif filter[0:4] == 'tag:':
		tag = filter[4:]
		for i in range(len(notes)):
			note = notes[i]
			if '#' in note:
				if note.partition('#')[2][0:-1].lower() == tag: 
				# 务必注意, 在比较时去掉note末尾的\n
					selected.append(note)
					indexes.append(i)
		return [selected, indexes]
#	elif (filter[0:4] = 'date:'):
#		if filter[5:] 为有效的日期格式:
#			selected = notes within this date range
#			return [selected, indexes]
#		else:
#			print 'Invalid date format!'
#			return -1
	else:
		print 'Invalid command!\n'
		return -1
	

if __name__=='__main__':
 	 main()