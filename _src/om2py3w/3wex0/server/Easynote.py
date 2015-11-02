# -*- coding: utf-8 -*-
# 由 0wex1 EasyNote 精简而来，供 3wex0 调用
from datetime import datetime
from os.path import exists

filename = "mynotes.txt"
		
def NewNote(note):
	f = open(filename,'a')
	time = str(datetime.now())[0:19] # 去掉秒数的小数部分
	f.write('%s   %s\n' % (time, note))
	f.close()

def GetNotes(word): #根据筛选条件word，返回符合条件的笔记内容及编号
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
		else:
			print 'Invalid command!\n'
			return -1
	else:
		return ''