#/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import html2text
from scrapy.selector import Selector

from urlparse import urljoin
import sys

reload(sys)
sys.setdefaultencoding('UTF8')

def get_page_urls(url):
	r = requests.get(url)
	if r.status_code != 200:
		print 'status: %d' % r.status_code
		return None
	entire_html = r.text
	relative_urls = Selector(text=entire_html).xpath('//li[@class="chapter "]//@href').extract() # list
	return relative_urls # 不包含当前的 active page

def get_page_content(url):
	print 'getting: %s' % url # test
	r = requests.get(url)
	if r.status_code != 200:
		print 'status: %d' % r.status_code
		return 'status code: %d' % r.status_code
	entire_html = r.text
	content_html = Selector(text=entire_html).xpath('//section[@class="normal"]').extract()[0]
	content_text = html2text.html2text(content_html)
	return content_text

def main():
	start_url = 'http://cen74.gitbooks.io/omooc2py/content/'
	
	url_list = [urljoin(start_url, url) for url in get_page_urls(start_url)]
	url_list.insert(0, start_url)
	
	for i in url_list:
		print i

	#if url_list == None:
	
	pages = [{'url':url, 'content':get_page_content(url)} for url in url_list]
	
	f = open('pages-text.txt', 'a')
	for url in url_list:
		f.write('%s\n' % url)
	for page in pages:
		#print 'URL: %s\n\nCONTENT:\n%s\n' % (page['url'], page['content'])
		print 'writing to file: %s' % page['url']
		f.write('URL: %s\n\nCONTENT:\n%s\n' % (page['url'], page['content']))
	f.close()

if __name__ == '__main__':
	main()