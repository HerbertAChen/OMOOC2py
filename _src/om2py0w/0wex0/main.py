# -*- coding: utf-8 -*-
# Quick Python Script Explanation for Programmers
import os

def main():
	print "Hello World!"

	print u"这是Alice\'的问候。"
	print u'这是Bob\'的问候。'

	foo(5, 10)

	print '=' * 10
	print u'这将直接执行'+os.getcwd()

	counter = 0
	counter += 1

	food = [u'苹果', u'杏子', u'李子', u'梨']
	for i in food:
		print u'俺就爱整只:'+i

	print u'数到10'
	for i in range(10):
			print i
def foo(param1, secondParam):
	res = param1 + secondParam
	print u'%s 加 %s 等于 %s' % (param1, secondParam, res)
	if res < 50:
		print u'这个'
	elif (res>=50) and ((param1==42) or (secondParam==24)):
		print u'那个'
	else:
		print u'嗯...'
	return res # 这是单行注释
	
if __name__=='__main__':
	main()