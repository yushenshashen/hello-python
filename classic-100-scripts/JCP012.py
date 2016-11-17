#!/usr/bin/env python

from math import sqrt


number = []

for i in range(101,200):
    
    tag = 'on'

    k = int(sqrt(i+1))

    for j in range(2,k+1):
        if i % j == 0:
            tag = 'off'
            break

    if tag == 'on':
        
        number.append(i)



print number
print 'the total number of sushu is %d ' % len(number)

