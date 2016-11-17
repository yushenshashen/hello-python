#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s = 0
t = 1
number = []

for i in range(1,21):
    
    t = t*i
    s = s + t
    number.append(t)

print number
print s