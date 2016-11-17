#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def fact(n):
    t = 1
    for i in range(1,n+1):
        t = t*i

    return t

for i in range(1,5):
    print '%d! = %d ' % (i,fact(i))


def fact2(n):
    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n*fact2(n-1)

    return sum

for i in range(1,5):
    print '%d! = %d ' % (i,fact2(i))