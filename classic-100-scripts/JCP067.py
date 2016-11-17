#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':

    a = [4,6,2,9,3,1]
    b = max(a)
    n = a.index(b)
    a[0],a[n] = b,a[0]

    print a
