#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def one_hello():
	word = 'Hello!'
	return word

def three_hello():
	word = one_hello()
	word = 3 * (word + 'new  ')
	return word

if __name__ == '__main__':

	print three_hello()



