#!/usr/bin/env python
# -*- coding: UTF-8 -*-

text = 'asdhf'

def rev(string):
    new_string = []
    l = len(string)
    for i in range(l):
        new_string.append(string[l-1-i])

    return ''.join(new_string)

print rev(text) 
