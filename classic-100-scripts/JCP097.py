#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':

	fp = open('a.txt',"w")  
	a = []
	flag = 'on'
	while flag == 'on':
		text = raw_input('input a string:')
		if text != '#':
			fp.write(text)
			a.append(text)
		else:
			flag = 'off'
 	
 	fp.close()





