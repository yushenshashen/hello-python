#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a = 2.0
b = 1.0

numbers = []

for i in range(1,21):
    number = a/b
    numbers.append(number)
    b,a = a,a+b

print sum(numbers)