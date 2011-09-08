"""
export.py

Created by rumori on 2011-09-08.
Copyright (c) 2011 RMRI. All rights reserved.
"""

import re
import json

import htmlutils
from models import HourArrivals, Arrival, Schedule, Route

class Parser():
	def Parser(self):
		pass
		
	def parse(self, url):
		html = htmlutils.get_html(url)

		print url
		
		route = Route()
		route.route = self.extract_route(html)
		js_data = self.extract_js_data(html)
		if js_data:
			route.schedules = self.parse_js_data(js_data)

		return route

	def extract_route(self, html):
		#find route number in page
		m = re.findall("<h1 id=\"route_number\".*?><span>(.*?)</span></h1>", html)
		if len(m)>0:
			return m[0]
		else:
			m = re.findall("<h1 id=\"route_number\".*?>(.*?)</h1>", html)
			if len(m)>0:
				return m[0]
			
		return None

	def extract_js_data(self, html):
		#find the json data in the html page
		m = re.findall("<script type=\"text/javascript\">// <!\[CDATA\[(.*?)// \]\]></script>", html)
		if len(m)>0:
			return m[0]
		return None

	def parse_js_data(self, data):
		statements = data.split(';')
		
		# actual arrival data
		data = statements[1]
		index = data.index('=')
		data = data[index+1:]
		data_object = json.loads(data)
		
		stops = len(data_object) + 1

		# only parse the first one (the others are just shifted)
		schedules = self.parse_table(data_object[0])
		
		return schedules
		
	def parse_table(self, data):
		schedules = []
		rows = data
		for row in rows:
			for r in row:
				schedules.append(self.parse_table_section(r))
		return schedules
			
	def parse_table_section(self, section):
		data = section[0]
		text = section[1]
		schooldays = section[2]
	
		hourarrivals = []
	
		datarows = data.split("@")
		for datarow in datarows:
			columns = datarow.split("$")
			
			if datarow == '': continue;

			hourarrival = HourArrivals()
			hourarrival.hour = int(columns[1])
			hourarrival.arrivals = map(self.parse_arrival, columns[3:])

			hourarrivals.append(hourarrival)
		
		schedule = Schedule()
		schedule.type = text
		schedule.schooldays = schooldays
		schedule.hour_arrivals = hourarrivals

		return schedule
		
	def parse_arrival(self, value):
		parts = value.split('|')
		arrival = Arrival()
		arrival.note = parts[0]
		arrival.interval = None if parts[1]=='' else parts[1]
		arrival.lowfloor = (parts[2] == '1')
		arrival.minutes = 0 if parts[3]=='' else int(parts[3])
		return arrival
