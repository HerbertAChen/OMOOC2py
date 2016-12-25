# -*- coding: utf-8 -*-
# 由 0wex1 EasyNote 修改而来，供 3wex0 调用
from datetime import datetime
from os.path import exists

filename = "mynotes.txt"
		
def NewNote(note):
	f = open(filename,'a')
	time = str(datetime.now())[0:19] # 去掉秒数的小数部分
	f.write('%s  %s\n' % (time, note))
	f.close()

def GetNotes(word): #根据筛选条件word，返回符合条件的笔记内容及编号
	if exists(filename):
		f = open(filename,'r')
		allnotes = f.readlines()
		f.close()

		filter = word.lower().strip()
		selected = {'notes':[], 'indexes':[]} #调用append方法前, 需要初始化为列表
		if filter == 'all':
			selected['notes'] = allnotes
			selected['indexes'] = range(len(allnotes))
			return selected
		elif filter.startswith('tag:'):
			tag = filter[4:]
			for i in range(len(allnotes)):
				note = allnotes[i]
				if '#' in note:
					if note.partition('#')[2][:-1].lower() == tag: 
					# 务必注意, 在比较时去掉note末尾的\n
						selected['notes'].append(note)
						selected['indexes'].append(i) 
			return selected
		elif filter.startswith('[') and filter.endswith(']'): # 此时filter为3wex0的hostname
			for i in range(len(allnotes)):
				note = allnotes[i]
				if note.startswith(filter,21): # 0-20位为日期和空格
					selected['notes'].append(note)
					selected['indexes'].append(i) 
			return selected
		else:
			return ''
	else:
		return ''