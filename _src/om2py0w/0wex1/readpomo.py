# -*- coding: utf-8 -*-
# 读取个人番茄记录的csv文件，按项目与子项目输出番茄数

import unicodecsv as csv

with open('Pomotodo_History_test.csv','rb') as pomocsv:
	pomoreader = csv.reader(pomocsv, delimiter=',', )
	pomodes = [] #番茄description列表
	data = [] # data = [..., [projx,[subpx-1,subpx-2,...],[countx-1,countx-2,...]], ... ]
	projlist = [] # projlist = [proj1, proj2, ...]
	
	#读取pomo记录的description列
	for row in pomoreader:
		pomodes.append(row[2])
		#print row[2]
	del pomodes[0]

	#根据冒号分隔提取项目名和子项名
	for des in pomodes:
		a = des.partition(u'：')
		p = a[0] #提取冒号前的项目名
		s = a[2] #提取冒号后的子项名
		if (p in projlist) == 0:
			projlist.append(p)
			data.append([p, [s,],[1,]])
		else:
			i = projlist.index(p)
			if (s in data[i][1]) == 0:
				data[i][1].append(s)
				data[i][2].append(1)
			else:
				j = data[i][1].index(s)
				data[i][2][j] += 1
	
	#输出
	for pdata in data:
		print '\n%s:\n' %pdata[0]
		total = 0
		for n in range(len(pdata[1])):
			print '    %s  %d' % (pdata[1][n], pdata[2][n])
		#	print '    20%s ', pdata[1][n], ' ', pdata[2][n]
			total += pdata[2][n]
		print '    Total:   ', total, 'pomos.'
