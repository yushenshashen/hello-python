#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':

    str1 = raw_input('input a string:\n')
    str2 = raw_input('input a sub string:\n')
    ncount = str1.count(str2)
    print ncount

##another way

import re

re.findall