# -*- coding: utf-8 -*-
# 0wex1 EasyNote
from datetime import datetime
from os.path import exists

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
			note  = raw_input('New note:\n>>> ').strip()
			if note != '':
				NewNote(note)
				print 'Note added!'
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
		
def NewNote(note):
	f = open(filename,'a')
	time = str(datetime.now())[0:19] # 去掉秒数的小数部分
	f.write('%s   %s\n' % (time, note))
	f.close()

def ListNotes(filter):
	result = GetNotes(filter)
	if result == '':
		print 'File not created!'
	elif result != -1:
		notes, indexes = result['notes'], result['indexes']
		if len(notes) == 0:
			print 'Nothing selected!'
		else:
			print '\n%s   %s   %s' % (
				' No', ' '*9+'CreateTime', 'Content')
			print '%s   %s   %s' % (' --', ' '*9+'-'*10, '-'*7) 
			for i in range(len(notes)):
				print '% 3d   %s' % (indexes[i], notes[i]),
			print '\n     %d notes listed.\n' % len(notes)
		
#def DelNotes(db, filter):

def GetNotes(word): #根据筛选条件word，返回符合条件的笔记内容及编号
	# 两种意外情况：1、错误输入，2、未找到符合条件的note
	if exists(filename):
		f = open(filename,'r')
		allnotes = f.readlines()
		f.close()

		filter = word.lower().strip()
		selected = {'notes':[], 'indexes':[]}
		if filter == 'all':
			selected['notes'] = allnotes
			selected['indexes'] = range(len(allnotes))
			return selected
		elif filter[0:4] == 'tag:':
			tag = filter[4:]
			for i in range(len(allnotes)):
				note = allnotes[i]
				if '#' in note:
					if note.partition('#')[2][0:-1].lower() == tag: 
					# 务必注意, 在比较时去掉note末尾的\n
						selected['notes'].append(note)
						selected['indexes'].append(i) #调用append方法前, 需要初始化为列表
			return selected
	#	elif filter.split(',') 都是 digit:
	#	elif (filter[0:4] = 'date:'):
		else:
			print 'Invalid command!\n'
			return -1
	else:
		return ''

if __name__=='__main__':
 	 main()