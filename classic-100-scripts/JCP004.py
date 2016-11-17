#!/usr/bin/env python

year = int(raw_input('year: '))
month = int(raw_input('month: '))
day = int(raw_input('day: '))

months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0 < month <= 12:
	result = months[month-1] + day
else:
	print 'month is wrong' 

#run nian
if(year % 4 == 0) and (month > 2):
	result += 1
print 'today is the %dth day' % result