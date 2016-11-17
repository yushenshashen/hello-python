#!/usr/bin/ python

from math import pow

for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):

            i = 100*a + 10*b + c

            pow_num = pow(a,3)+pow(b,3)+pow(c,3) 

            if i == pow_num:

                print i


##way2

for i in range(100,1000):

    a = i / 100

    b = i / 10 % 10

    c = i % 10
    

    pow_num = pow(a,3)+pow(b,3)+pow(c,3) 

    if i == pow_num:

        print i
