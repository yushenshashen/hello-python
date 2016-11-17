#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#n = int(raw_input('please input a number: '))

def get_zhiyinshu(n):

    if not isinstance(n,int) or n < 0:
        print 'please input a correct number!'
    else:
        print '{} = '.format(n),

    while n not in [1]:
        for i in range(2,n+1):
            if n % i ==0:
                n /= i
                if n == 1:
                    print i
                else:
                    print '{} * '.format(i),
                break

print get_zhiyinshu(100)

