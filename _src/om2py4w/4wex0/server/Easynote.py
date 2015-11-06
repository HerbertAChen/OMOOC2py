# -*- coding: utf-8 -*-
# 由 0wex1 EasyNote 修改而来，供 4wex0 调用
from datetime import datetime
from os.path import exists

filename = "mynotes.txt"
		
def NewNote(note):
	f = open(filename,'a')
	time = str(datetime.now())[:19] # 去掉秒数的小数部分
	f.write('%s  %s\n' % (time, note))
	f.close()

def GetNotes(): # 根据4wex0的需求简化了，仅返回全部笔记的列表
	if exists(filename):
		f = open(filename,'r')
		allnotes = f.readlines()
		f.close()
		return allnotes
	else:
		return ['No notes on server']