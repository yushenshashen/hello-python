#!/usr/bin/env python
# -*- coding: UTF-8 -*-

week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Satday','Sunday']

letter = raw_input('please input a letter: ')
letter = letter.upper()

if letter == 'M':
    print 'it is ',week[0]
elif letter == 'W':
    print 'it is ',week[2]
elif letter == 'F':
    print 'it is ',week[4]
elif letter == 'T':
    letter2 = raw_input('please input another letter: ')
    if letter2.lower() == 'u':
        print 'it is ',week[1]
    else:
        print 'it is ',week[3]

elif letter == 'S':
    letter2 = raw_input('please input another letter: ')
    if letter2.lower() == 'a':
        print 'it is ',week[5]
    else:
        print 'it is ',week[6]

else:
    print 'wrong'


