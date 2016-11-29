#!/usr/bin/python

import random
import time

DNA = ['A','T','G','C']
d = {}
d['A'] = 'T'
d['T'] = 'A'
d['C'] = 'G'
d['G'] = 'C'


a = [5,4,3,2,1,0,0,1,1,0,0,1,2,3,4,5]
b = [0,2,3,4,4,3,2,0,0,2,3,4,4,3,2,0]

while True:
	for i in range(len(a)):

		l = random.choice(DNA)
		r = d[l]

		print (a[i]+10)*' ' + l + b[i]*'-' + r
		time.sleep(0.1)
