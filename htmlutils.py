"""
export.py

Created by rumori on 2011-09-08.
Copyright (c) 2011 RMRI. All rights reserved.
"""

# so dumb, give me a better solution :)

import urllib2
import re

def get_urls_with_prefix(page, prefix, format):
	
	html = get_html(page)

	matches = re.findall("<a(.*?)href=\"([^\"]*?)\">(.*?)</a>", html)
	
	urls = []
	for match in matches:
		url = match[1]
		length = len(url)
		if url[:len(prefix)] == prefix and url[length-len(format):] == format:
			urls.append(url)

	return urls

def get_html(url):
	f = urllib2.urlopen(url)
	data = f.read()
	f.close()
	data = stripText(data)
	return data

def stripAmps(text):
	return text.replace('&amp;', '&')
	
def stripText(text):
	#strip
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	text = text.replace('\t', '');
	
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');
	text = text.replace('\n', '');

	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	text = text.replace('\r', '');
	
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ');
	text = text.replace('  ', ' ')
	text = text.replace('  ', ' ')
	text = text.replace('> <', '><');
	text = text.replace(' />', '/>');
	return text
		
