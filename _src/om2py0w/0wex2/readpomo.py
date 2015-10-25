# -*- coding: utf-8 -*-
# 读取个人番茄记录的csv文件，按任务与子任务输出番茄数
#151016 初版

import unicodecsv as csv

filename = 'Pomotodo_History_test.csv'
# 待改进：文件名的指定

with open(filename,'rb') as pomocsv:
	pomoreader = csv.reader(pomocsv, delimiter=',', )
	pomodes = [] #番茄description列表
	data = [] # data = [..., [taska,[subta-1,subta-2,...],[counta-1,counta-2,...]], ... ]
	tasklist = [] # tasklist = [task1, task2, ...]
	
	#读取pomo记录的description列
	for row in pomoreader:
		pomodes.append(row[2])
		#print row[2]
	del pomodes[0] # 删去表头行

	for des in pomodes:
		a = des.partition(u'：')
		p = a[0] #提取冒号前的任务名
		s = a[2] #提取冒号后的子任务名
		if (p in tasklist) == 0:
			tasklist.append(p)
			data.append([p, [s,],[1,]])
		else:
			i = tasklist.index(p)
			if (s in data[i][1]) == 0:
				data[i][1].append(s)
				data[i][2].append(1)
			else:
				j = data[i][1].index(s)
				data[i][2][j] += 1
	
	#输出
	for tdata in data:
		print '\n%s:\n' %tdata[0]
		total = 0
		for n in range(len(tdata[1])):
			print '    %s  %d' % (tdata[1][n], tdata[2][n])
			total += tdata[2][n]
		print '    Total:   ', total, 'pomos.'
