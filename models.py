"""
models.py

Created by rumori on 2011-09-08.
Copyright (c) 2011 RMRI. All rights reserved.
"""

class Arrival():
	def Arrival(self):
		pass
	def __repr__(self):
		return str(self.interval) if self.interval else str(self.minutes)

class HourArrivals():
	def HourArrivals(self):
		self.hour = 0
		self.arrivals = None
	def __repr__(self):
		return '%d %s' % (self.hour, self.arrivals)

class Schedule():
	def Schedule(self):
		self.type = ''
		self.schooldays = ''
		self.hour_arrivals = None
	def __repr__(self):
		return u'%s %s' % (self.schooldays, self.hour_arrivals)
		
class Route():
	def Route():
		self.route = ''
		self.schedules = None
	
	def __repr__(self):
		return '%s %s' % (self.route, self.schedules)
