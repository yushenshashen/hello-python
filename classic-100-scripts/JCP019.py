#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

from sys import stdout 

for i in range(1,1000):

    yinshu = []

    for j in range(1,i):

        if i % j == 0:

            yinshu.append(j)

    if i == sum(yinshu):
        print i

        #print yinshu
        for k in yinshu:

            stdout.write(str(k))
            stdout.write(' ')

        
        print ' '





