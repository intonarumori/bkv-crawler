"""
export.py

Created by rumori on 2011-09-08.
Copyright (c) 2011 RMRI. All rights reserved.
"""

from parser import Parser
import htmlutils

def load_schedules(mainpage, prefix):

	urls = htmlutils.get_urls_with_prefix(mainpage, prefix, 'html')

	url_prefix = 'http://www.bkv.hu'
	urls = map(lambda x: url_prefix + x, urls)

	parser = Parser()
	for url in urls:	
		# this is one example html parsed
	 	route = parser.parse(url)
		print route.route
		
		# we demonstrate one so skip the others
		break
	

def main():

#	parser = Parser()
#	route = parser.parse('http://www.bkv.hu/busz/71.html')

	load_schedules('http://www.bkv.hu/hu/busz_menetrend/?page=-1', '/busz')
#	load_schedules('http://www.bkv.hu/hu/villamos_menetrend', '/villamos')
#	load_schedules('http://www.bkv.hu/hu/metro_menetrend', '/metro')
#	load_schedules('http://www.bkv.hu/hu/trolibusz_menetrend', '/troli')
#	load_schedules('http://www.bkv.hu/hu/hev_menetrend', '/hev')
#	load_schedules('http://www.bkv.hu/hu/ejszakai_menetrend', '/ejszakai')
#	load_schedules('http://www.bkv.hu/hu/egyeb_menetrend', '/egyeb')
	

if __name__ == '__main__':
	main()

