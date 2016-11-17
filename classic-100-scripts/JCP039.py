#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np

if __name__ == '__main__':

    a = [3,5,6,8,10,20]

    n = 9

    if n > max(a):
        new = a.append(n)
    else:
        l = len(a)
        for i in range(l):
            if a[i] > n:

                #new = a[:i]
                #new = new.append(n)
                #new = new.append(a[i+1:])
                #break
                a.insert(i,n)
                break

    print a
