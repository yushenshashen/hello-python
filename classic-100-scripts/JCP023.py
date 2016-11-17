'''
【程序23】 
题目：打印出如下图案（菱形）

   *
  ***
 *****
*******
 *****
  ***
   *
1.程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重
　　　　　　for循环，第一层控制行，第二层控制列。 
2.程序源代码： 
'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from sys import stdout

for i in range(4):
    for j in range(3 - i):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print

for i in range(4,7):
    for j in range(i - 3):
        stdout.write(' ')
    for k in range(2*(6-i)+1):
        stdout.write('*')
    print 