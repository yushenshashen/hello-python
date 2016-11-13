#!/user/bin/env/python

n = 50
guess = int(input('please input a number: '))

if guess == n:
	print('you are right')
elif guess > n:
	print('you are bigger')
elif guess < n:
	print('you are smaller')

print('game over')
