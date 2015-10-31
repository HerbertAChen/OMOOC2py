## 0wEx2 PomoHistoryReader

### 背景
平时习惯用 pomotodo.com 记录日常工作及学习的番茄（网页版+安卓端），我很喜欢这个小巧精致的应用，但苦恼的是它对番茄历史数据的整理功能比较弱，不能满足我的需求，比如：
* 不能记录**子任务**的番茄数
* 手动补记的番茄无法计入任务番茄总数
* 不能用灵活的方式输出任务番茄数汇总表

我个人使用 pomotodo 的一个习惯是，在番茄描述文字中用中文冒号隔开任务与子任务名，比如：

> 读某书：读某章

学编程最大的动力之一就是实现符合个性化需求的数据管理。原本觉得编这样的代码应该是在学习一段时间之后，但在“立即开始编程”的口号号召下，我想这功能不复杂，何不动手一试？可以先从导出的 csv 文件开始，下一步再考虑从网页上直接抓取。

### 功能设计
* 读取 pomotodo.com 输出的番茄记录 csv 文件，按任务及子任务汇总番茄数
  * 番茄记录的 csv 文件有三列：date,time,description；暂只需要 description 这一项。
  * description 的格式 "任务：子任务"
  * [样例csv文件](0wex0dot5/Pomotodo_History_test.csv)

### 技术要点
* 读取 csv 文件，读入 description 列
  * python 官方文档中就有 [csv 模块](https://docs.python.org/2/library/csv.html)，但不支持 unicode
  * 经搜索，找到支持 uinicode 的替换模块：[python-unicodecsv](https://github.com/jdunck/python-unicodecsv)。
* 按冒号区分任务名和子任务名
  * 翻了一本 python 参考书，找到一个合适的字符串函数：`string.partition()`
* 三种变量：任务名、子任务名、子任务番茄数。该用什么样的数据结构？
  * 最笨的方法，就列表呗
  * 大列表的每一项都是这样一个子列表：
    * `[任务a, [子任务a-1, 子任务a-2, ...], [子任务a-1番茄数, 子任务a-2番茄数, ...]]`
* 输出：按任务、子任务二级结构输出 番茄数，同时汇总任务番茄数

### 实现难点
* read csv文件
  * 实际上找到合适的模块后，只需读模块的使用说明
* 读取和输出时对中文字符的支持
  * 虽然勉强把代码写出来了，但我对 `unicode, utf-8, ASCII` 等概念还是迷迷糊糊，急待进一步学习

### 代码
```
# -*- coding: utf-8 -*-
# 读取个人番茄记录的csv文件，按任务与子任务输出番茄数
#151016 初版

import unicodecsv as csv

with open('Pomotodo_History_test.csv','rb') as pomocsv:
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
```

### 进展

151017 创建文档
