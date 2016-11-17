#!/usr/bin/env python
# -*- coding: UTF-8 -*-

##list str
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Satday','Sunday']
new = ','.join(week)

##list is int
b = [2,4,6]
new = ','.join(str(i) for i in b)
print new