#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np

if __name__ == '__main__':

	a = np.array([[1,2,3],[4,5,6],[7,8,9]])
	b = np.asmatrix(a)

	print b

	s = 0
	for i in range(3):
		s = s + a[i][i]

	print s