#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n = 5

def autofun():
	n = 1
	print 'function n is %d' % n
	n += 2

if __name__ == '__main__':

	for i in range(3):

		print 'number is %d ' % n

		n += 1

		autofun()
