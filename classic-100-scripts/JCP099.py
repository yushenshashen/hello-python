#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':

    with open('a','r') as file1:
        a = file1.read().strip()
    with open('b','r') as file2:
        b = file2.read().strip()

    c = a+b
    c = sorted(c)
    c = ''.join(c)
    #with open('c','w') as file:
        #file.write(c)
    f = open('c','w')
    f.write(c)
