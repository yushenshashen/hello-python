#!/usr/bin/env python

a = int(raw_input('1st number: '))
b = int(raw_input('2ed number: '))
c = int(raw_input('3rd number: '))

number = []

#for i in range(3):
#	x = int(raw_input('int:'))
#	number.append(x)

number.append(a)
number.append(b)
number.append(c)

number.sort()

print number