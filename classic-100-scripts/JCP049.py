#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 5
haha = lambda x : x*x
print haha(a)

get_max = lambda x,y : (x>y)*x + (x<y)*y
get_min = lambda x,y : (x>y)*y + (x<y)*y

if __name__ == '__main__':

	c = 35
	d = 23
	print 'larger one is %d' % get_max(c,d)