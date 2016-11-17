#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#程序分析：利用while语句,条件为输入的字符不为'\n'。

import string

#text = raw_input('please input a string: ')

text = '34fdgds hrd77&*'

letters = 0
space = 0 
digits = 0
others = 0

#for i in range(len(text)):
for i in text:
    
    if i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digits += 1
    else:
        others += 1

print '''letters is %d 
space is %d 
digits is %d 
others is %d ''' % (letters,space,digits,others)
