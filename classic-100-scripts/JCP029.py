#!/usr/bin/env python
# -*- coding: UTF-8 -*-

n = 23574

a = n/10000 
b = n%10000/1000
c = n%1000/100
d = n%100/10
e = n%10

if a!=0:
    print 'five number ',e,d,c,b,a 
