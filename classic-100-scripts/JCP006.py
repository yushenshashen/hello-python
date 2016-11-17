#! /usr/bin python


def fib(n):
	if n == 0: 
		return 1
	if n == 1 or n == 2:
		return 1
	if n > 2:
		return fib(n-2) + fib(n-1)

def fib2(n):
	f = [0,1,1]
	for i in range(2,n):
		f.append(f[-1] + f[-2])

	return f

print fib2(1)