#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 6
b = 5

a,b = b,a

print a,b

def exchange(a,b):
	a,b = b,a
	return (a,b)

if __name__ == '__main__':
	x = 10
	y = 3
	print 'x = %d; y = %d' % (x,y)
	x,y = exchange(x,y)
	print 'x = %d; y = %d' % (x,y)
