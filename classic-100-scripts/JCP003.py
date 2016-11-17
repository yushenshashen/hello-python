#!/usr/bin/env python


import math

for i in range(10000):
	a = int(math.sqrt(i + 100))
	b = int(math.sqrt(i + 268))

	if (a*a == i + 100) and (b*b == i + 268):
		print i 
