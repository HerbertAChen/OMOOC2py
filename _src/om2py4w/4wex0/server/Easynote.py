# -*- coding: utf-8 -*-
# SQLite 数据库版
from os.path import exists
import sqlite3
from datetime import datetime

dbfilename = "mynotes.db"
		
def NewNote(note):
	con = sqlite3.connect(dbfilename)
	time = str(datetime.now())[:19] # 去掉秒数的小数部分
	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Notes(Id INTEGER PRIMARY KEY, Time TEXT, Content TEXT)")
		cur.execute("INSERT INTO Notes(Time, Content) VALUES(?,?)", (time, note))

def GetNotes(): # 返回全部笔记的列表
	if exists(dbfilename):
		con = sqlite3.connect(dbfilename)
		allnotes = []
		with con:
			con.row_factory = sqlite3.Row
			cur = con.cursor()
			cur.execute("SELECT * FROM Notes")
			rows = cur.fetchall()		
			for row in rows:
				allnotes.append('%s  %s' % (row['Time'], row['Content']))
		return allnotes
	else:
		return ['No data on server']