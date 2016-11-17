#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    n1 = int(raw_input('n1 = : '))
    n2 = int(raw_input('n2 = : '))
    n3 = int(raw_input('n3 = : '))

    def swap(a,b):
    	if(a>b):
    		return(a,b)
    	else:
    		return(b,a)

    n = [n1,n2,n3]
    n.sort()
    n.reverse()
    print n