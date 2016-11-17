#!/usr/bin/env python
# -*- coding: UTF-8 -*-

s = 100.0
h = s / 2
n = 10

for i in range(2,n+1):
    s = s + 2 * h
    h = h / 2

print s,h

