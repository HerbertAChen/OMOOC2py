# -*- coding: utf-8 -*-
# 0wex1 EasyNote
from datetime import datetime
import shelve

def main():
	head = '''
## EasyNote v1.0 ##
Type "help" for more infomation.''' 
	
	helpmsg = u'''
### 命令说明
* "new" -- 创建新笔记
* "exit" -- 退出
* "list [笔记集合]" -- 列出指定的笔记集合
* "del [笔记集合]" -- 删除指定的笔记集合
* "exp [笔记集合] [filename].txt" -- 把指定的笔记集合导出到指定文件
* 注：
    1. [笔记集合]可以是 "all" 或 "笔记编号(多个编号用逗号隔开)"
       或 "date:[yymmdd]-[yymmdd]" 或 "tag:[标签名]"
    2. [笔记集合] 或 [文件名] 中均不应包含空格!
'''	
	
	print head
	cmd = raw_input('$ ').lower().strip()
	database = shelve.open('mynotes.dat', flag='c', protocol=None, writeback=True)
	try:
		while (cmd not in ['exit','quit','q']):
			cmdwords = cmd.split(' ') # 分解用户指令
			length = len(cmdwords)

			if cmd == 'help':
				print helpmsg
			elif cmd == 'new':
				NewNote(database)
			elif cmd == 'list':
				ListNotes(database, 'all')
			elif length == 2:
				word1, word2 = cmdwords[0], cmdwords[1]
				if word1 == 'list':
					ListNotes(database, word2)
				#elif word1 == 'del':
				#	DelNotes(database, word2)
				else:
					print 'Invalid command!\n'
			#elif length == 3:
			#	word1, word2, word3 = cmdwords[0], cmdwords[1], cmdwords[2]
			#	if word1 == 'exp':
			#		ExpNotes(database, word2, word3)
			#	else:
			#		print 'Invalid command!\n'
			else:
				print 'Invalid command!\n'
			cmd = raw_input('$ ').lower().strip()
	finally:
		database.close()
		
def NewNote(db):
	key = str(len(db)+1)
	note = {}
	input = raw_input('New note:\n>>> ')
	note['content'] = input
	#note['content'] = input.partition('#')[0]
	#note['tag'] = input.partition('#')[2]
	note['datetime'] = str(datetime.now())[0:19]
	db[key] = note
	#print db #测试用
	print 'Note added!'

def ListNotes(db, filter):
	notes = SelectNotes(db, filter)
	if notes != -1:
		print '\n#### List of Notes ####\n'
		for key in notes:
			note = notes[key]
			print '[%s] %s ' % (
				note['datetime'], note['content'])
		print '\n#### Total Num: %d ####' % len(notes)
		
#def DelNotes(db, filter):
#	print 'notes deleted!' #测试用
#
#def ExpNotes(db, filter, filename):
#	print 'notes exported!' #测试用

#def Group():

def SelectNotes(db, filter): #输入filter，返回 selected notes
	# 如何区分两种意外情况：1、错误输入，2、未找到符合条件的note
	selected = {}
	if filter == 'all':
		return db
#	elif filter.split(',') 都是 digit:
#		if 满足条件：0 < num < len(db):
#			for key in filter_nums：
#				selected[key] = db[key]
#			return selected
#		else:
#			print 'Note_index out of range.'
#			return -1
#	elif filter[0:3] = 'tag:':
#		tag = filter[4:]
#		if tag in tags:
#			selected = notes with this tag
#			return selected
#		else:
#			print 'tag doesn\'t exist!'
#			return -1
#	elif (filter[0:4] = 'date:'):
#		if filter[5:] 为有效的日期格式:
#			selected = notes within this date range
#			return selected
#		else:
#			print 'Invalid date format!'
#			return -1
	else:
		print 'Invalid command!\n'
		return -1
	

if __name__=='__main__':
 	 main()