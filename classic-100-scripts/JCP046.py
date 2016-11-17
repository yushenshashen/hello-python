#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

n = int(raw_input('please input a number: '))

if n*n < 50:
	print 'it is < 50'
	sys.exit()
else:
	print 'n*n is ',n*n 