#!/usr/bin/python
# -*- coding: UTF-8 -*-

#pay attention the time

if __name__ == '__main__':

	time = 1
	while time <=7:
		
		n = int(raw_input('input a number:'))
		while n>0 and n <=50:

			print n*'*'
			
			time += 1
			break