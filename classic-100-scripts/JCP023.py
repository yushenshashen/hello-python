'''
������23�� 
��Ŀ����ӡ������ͼ�������Σ�

   *
  ***
 *****
*******
 *****
  ***
   *
1.����������Ȱ�ͼ�ηֳ���������������ǰ����һ�����ɣ�������һ�����ɣ�����˫��
������������forѭ������һ������У��ڶ�������С� 
2.����Դ���룺 
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