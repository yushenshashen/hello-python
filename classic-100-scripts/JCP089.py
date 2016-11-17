#!/usr/bin/python
# -*- coding: UTF-8 -*-


##par attention to stdout 

from sys import stdout

if __name__ == '__main__':

    n = 5349
    a = n / 1000
    b = n %1000/100
    c = n % 100 /10
    d = n % 10

    new = []
    for i in [a,b,c,d]:

        new.append((i+5)%10)

    print new
    new[0],new[1],new[2],new[3] = new[3],new[2],new[1],new[0]


    for i in new:
        stdout.write(str(i))

