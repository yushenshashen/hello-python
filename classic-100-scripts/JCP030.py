#!/usr/bin/env python
# -*- coding: UTF-8 -*-

for n in range(10000,100000):
	a = n/10000 
	b = n%10000/1000
	c = n%1000/100
	d = n%100/10
	e = n%10

	if a== e and b == d:
		#print n
		pass

n = 12321
n = str(n)
l = len(n)

for i in range(l):
	flag = 'on'
	if n[i] == n[l-1-i]:
		flag = 'on'
		break

if flag == 'on':
	print 'it is the number'
else:
	print 'not'


