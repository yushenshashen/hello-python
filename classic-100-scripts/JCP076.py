#!/usr/bin/python
# -*- coding: UTF-8 -*-


def double(n):
    s = 0
    for i in range(2,n+1,2):
        s += 1.0/i
    return s

def single(n):
    s = 0
    for i in range(1,n+1,2):
        s += 1.0/i
    return s

if __name__ == '__main__':

    n = int(raw_input('please input a number:'))

    if n%2==0:
        s = double(n)
    else:
        s = single(n)
        #s = 0
    print s