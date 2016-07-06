#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Chukwunyere Igbokwe on May 19, 2016 by 1:46 AM

"""
Modul, which implements the class CalendarClock.
"""
# import inspect
from clock_class import Clock
from calender_class import Calendar

class CalendarClock(Clock, Calendar):

	def __init__(self, day,month,year,hours=0, minutes=0,seconds=0):
		Calendar.__init__(self, day, month, year)
		Clock.__init__(self, hours, minutes, seconds)

	def __str__(self):
		return Calendar.__str__(self) + ", " + Clock.__str__(self)

	def tick(self):
		"""
		advance the clock by one second
		"""
		previous_hour = self._hours
		Clock.tick(self)
		if self._hours < previous_hour:
			self.advance()


if __name__  == "__main__":
	x = CalendarClock(24,12,2016)
	print(x)
	for i in range(1000):
	  x.tick()
	for i in range(1000):
	  x.advance()
	print(x)
	print ""

	x = CalendarClock(31, 12, 2013, 23, 59, 59)
	print "One tick from ", x
	x.tick()
	print "to ", x

	x = CalendarClock(28, 2, 1900, 23, 59, 59)
	print "One tick from ", x
	x.tick()
	print "to ", x

	x = CalendarClock(28, 2, 2000, 23, 59, 59)
	print "One tick from ", x
	x.tick()
	print "to ", x

	x = CalendarClock(7, 2, 2013, 13, 55, 40)
	print "One tick from ", x
	x.tick()
	print "to ", x
   # print inspect.getsource(x.tick)