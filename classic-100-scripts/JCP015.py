#!/usr/bin/env python
# -*- coding: UTF-8 -*-

score = int(raw_input('please input score: '))

if score >= 90:
    grade = 'A'
elif 60 <= score < 90:
    grade = 'B'
elif score < 60:
    grade = 'C'


print grade

